import re

from ..base.abc import BotParser
from ..base.exceptions import BotValueError
from ..base.typing import TYPE_CHECKING, Optional, ParseArgs

if TYPE_CHECKING:
    from .formatter import CmdArgFormatter


class CmdParser(BotParser):
    """命令解析器

    通过解析命令名和命令参数的形式，解析字符串。
    """

    def __init__(
        self,
        cmd_start: str | list[str],
        cmd_sep: str | list[str],
        target: str | list[str],
        formatters: Optional[list[Optional["CmdArgFormatter"]]] = None,
    ) -> None:
        """初始化一个命令解析器

        .. admonition:: 注意
           :class: caution

           - 命令起始符和命令间隔符不允许包含：引号，各种括号，反斜杠，数字，英文，控制字符及各类空白字符。
           - 命令起始符不能是命令间隔符的子序列，反之亦然。

        :param cmd_start: 命令起始符（可以是字符串或字符串列表）
        :param cmd_sep: 命令间隔符（可以是字符串或字符串列表）
        :param target: 匹配的命令名
        :param formatters: 格式化器列表（列表可以包含空值，即此位置的参数无格式化）
        """
        i1 = cmd_start if isinstance(cmd_start, str) else "".join(cmd_start)
        i2 = cmd_sep if isinstance(cmd_sep, str) else "".join(cmd_sep)
        super().__init__(f"{i1}\u0000{i2}")
        self.targets = target if isinstance(target, list) else [target]
        self.formatters = [] if formatters is None else formatters
        self.need_format = (
            True if target is not None and len(self.formatters) > 0 else False
        )

        self.start_tokens = cmd_start if isinstance(cmd_start, list) else [cmd_start]
        self.sep_tokens = cmd_sep if isinstance(cmd_sep, list) else [cmd_sep]
        self.ban_regex = re.compile(r"[\'\"\\\(\)\[\]\{\}\r\n\ta-zA-Z0-9]")
        self._build_parse_regex()

        if self.ban_regex.findall(f"{''.join(cmd_start)}{''.join(cmd_sep)}"):
            raise BotValueError("存在命令解析器不支持的命令起始符，或命令间隔符")

    def _build_parse_regex(self):
        """建立用于命令解析的正则 Pattern 对象，包含命令起始符正则 pattern 和 命令间隔符正则 pattern"""
        temp_regex = re.compile(
            r"([\`\-\=\~\!\@\#\$\%\^\&\*\(\)\_\+\[\]\{\}\|\:\,\.\/\<\>\?])"
        )
        if not len(set(self.sep_tokens) & set(self.start_tokens)):
            self.cmd_sep = [
                temp_regex.sub(r"\\\1", sep_token) for sep_token in self.sep_tokens
            ]
            self.cmd_start = [
                temp_regex.sub(r"\\\1", start_token)
                for start_token in self.start_tokens
            ]
            self.sep_parse_regex = re.compile(rf"{'|'.join(self.cmd_sep)}")
            self.start_parse_regex = re.compile(rf"{'|'.join(self.cmd_start)}")
        else:
            raise BotValueError("命令解析器起始符不能和间隔符重合")

    def _split_string(
        self, string: str, regex: re.Pattern, popFirst: bool = True
    ) -> list[str]:
        """按照指定正则 pattern，对 string 进行分割"""
        # 将复杂的各种分隔符替换为 特殊字符，方便分割
        temp_string = regex.sub("\u0000", string)
        temp_list = re.split("\u0000", temp_string)
        if popFirst:
            temp_list.pop(0)
        return list(filter(lambda x: x != "", temp_list))

    def _parse(self, text: str, textFilter: bool = True) -> dict[str, list[str]]:
        pure_string = text.strip() if textFilter else text
        cmd_strings = self._split_string(pure_string, self.start_parse_regex)
        cmd_seqs = [
            self._split_string(s, self.sep_parse_regex, False) for s in cmd_strings
        ]
        cmd_seqs = list(filter(lambda x: x != [], cmd_seqs))
        cmd_dict: dict[str, list[str]] = {}
        for seq in cmd_seqs:
            if len(seq) == 0:
                continue
            cmd_dict[seq[0]] = seq[1:]
        return cmd_dict

    def parse(self, text: str) -> dict[str, ParseArgs]:
        cmd_dict = self._parse(text)
        return {target: ParseArgs(cmd_dict.get(target)) for target in self.targets}

    def test(
        self, args_dict: dict[str, ParseArgs] | None
    ) -> tuple[bool, Optional[str], Optional[ParseArgs]]:
        # 测试是否匹配。返回三元组：（是否匹配成功，匹配成功的命令名，匹配成功的命令参数）。
        # 最后两个返回值若不存在，则返回 None。
        if args_dict is None:
            return (False, None, None)
        for group_id in args_dict.keys():
            if group_id in self.targets:
                return (True, group_id, args_dict[group_id])
        return (False, None, None)

    async def format(self, group_id: str, args: ParseArgs) -> bool:
        # 格式化命令解析参数
        if hasattr(args, "formatted"):
            return True
        for idx, formatter in enumerate(self.formatters):
            if formatter is None:
                continue
            status = await formatter.format(group_id, args, idx)
            if not status:
                return False
        args.vals = args.vals[: len(self.formatters)]  # type: ignore
        args.formatted = True  # type: ignore
        return True


class CmdParserGen:
    """命令解析器的生成器

    预先存储命令起始符和命令间隔符，指定匹配的命令名后返回一个命令解析器。
    """

    def __init__(self, cmd_start: str | list[str], cmd_sep: str | list[str]) -> None:
        """初始化一个命令解析器的生成器

        .. admonition:: 注意
           :class: caution

           - 命令起始符和命令间隔符不允许包含：引号，各种括号，反斜杠，数字，英文，控制字符及各类空白字符。
           - 命令起始符不能是命令间隔符的子序列，反之亦然。

        :param cmd_start: 命令起始符（可以是字符串或字符串列表）
        :param cmd_sep: 命令间隔符（可以是字符串或字符串列表）
        """
        self.cmd_start = cmd_start
        self.cmd_sep = cmd_sep

    def gen(
        self,
        target: str | list[str],
        formatters: Optional[list[Optional["CmdArgFormatter"]]] = None,
    ) -> CmdParser:
        """生成匹配指定命令名的命令解析器

        :param target: 匹配的命令名
        :param formatters: 格式化器列表（列表可以包含空值，即此位置的参数无格式化选项）
        """
        return CmdParser(self.cmd_start, self.cmd_sep, target, formatters)
