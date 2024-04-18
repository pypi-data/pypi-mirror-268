import sys

sys.path.append("../src")

from melobot import BotPlugin, ForwardWsConn, MeloBot, msg_text, send_reply

bot1 = MeloBot("test1")
bot2 = MeloBot("test2")


class MyPlugin(BotPlugin):
    def __init__(self) -> None:
        super().__init__()

    @BotPlugin.on_start_match(".hello")
    async def hello(self) -> None:
        s = msg_text()
        await send_reply(s[6:])

    @bot1.on_loaded()
    async def tip(self) -> None:
        self.LOGGER.info("本插件已被加载！")


class MyPlugin2(BotPlugin):
    def __init__(self) -> None:
        super().__init__()

    @BotPlugin.on_start_match(".hello")
    async def hello(self) -> None:
        s = msg_text()
        await send_reply(s[6:] + "okokok")


if __name__ == "__main__":
    conn1 = ForwardWsConn("127.0.0.1", 8080)
    bot1.init(conn1, log_level="DEBUG")
    bot1.load_plugin(MyPlugin)

    conn2 = ForwardWsConn("127.0.0.1", 8081)
    bot2.init(conn2, log_level="DEBUG")
    bot2.load_plugin(MyPlugin2)

    MeloBot.start(bot1, bot2)
