import time
import os
import json
import functools
import asyncio as aio
from core.Executor import EXEC, AuthRole
from common import *
from common.Action import custom_msg_node
from common.Store import BOT_STORE
from common.Exceptions import *
from common.Typing import *
from templates.sdapi.api import SdApi
from templates.sdapi.api_help import help_docs, run_docs, status_docs, options_docs, set_docs


format_funcs = [str, str, int, int, int, str, float, int, int, float, lambda x: bool(int(x)), float, int, str, int, lambda x: json.loads(x)]

arg_names = ['prompt', 'negative_prompt', 'width', 'height', 'steps', 'sampler_name', 'cfg_scale', 'seed', 'subseed', 'subseed_strength', 'enable_hr', 'denoising_strength', 'hr_scale', 'hr_upscaler', 'hr_second_pass_steps', 'script_name', 'script_args', 'override_settings', 'limit_access']

arg_defaults = [-1, None, 512, 512, 20, 'DPM++ 2M SDE Karras', 7, None, None, None, None, None, None, None, None, None]

superior_ids = set(BOT_STORE.config.super_user + [BOT_STORE.config.owner] + \
                   BOT_STORE.config.white_list)
su_ids = set(BOT_STORE.config.super_user + [BOT_STORE.config.owner])

cq_image_path = '/home/melodyecho/Program/cqhttp/data/images'


def format_with_defaults(formatters: List[Callable], idx: int, arg: Any) -> Callable:
    if arg == '':
        raise ValueError
    elif arg == '/':
        return arg_defaults[idx]
    else:
        return formatters[idx](arg)


def open_api() -> SdApi:
    try:
        api = SdApi()
        BOT_STORE.logger.info("sdapi 已刷新本地配置缓存")
        return api
    except Exception as e:
        BOT_STORE.logger.warning(f"sdapi 初始化失败：{e.__str__()}")
        return None


def close(api: SdApi) -> None:
    api.session.close()


@EXEC.template(
    aliases=['画图', 'sd'],
    userLevel=AuthRole.USER,
    comment=help_docs,
    prompt='功能复杂，请参考具体的帮助信息',
    preLoad=(open_api, close),
    timeout=600
)
async def draw(session: BotSession, subcmd: str, *args) -> None:
    api: SdApi = EXEC.get_resource('draw')
    if api is None:
        await session.send("sdapi 状态异常，暂无法提供服务")
        return
    lock = EXEC.get_cmd_lock('draw')

    if subcmd == 'run':
        if lock.locked():
            await session.send(f"正在画另一张图呢，进度是 {round(float(api.progress), 3)*100}%, 等一会儿吧~")
            return
        async with lock:
            await draw_run(session, api, *args)
    elif subcmd == 'docs':
        await draw_docs(session, *args)
    elif subcmd == 'status':
        await draw_status(session, api)
    elif subcmd == 'options':
        await draw_options(session, api)
    elif subcmd == 'set':
        await draw_set(session, api, *args)
    else:
        raise BotCmdExecFailed("无效子命令")


async def draw_docs(session: BotSession, sub_name: str) -> None:
    if sub_name in ['run', 'status', 'options', 'set']:
        await session.send(globals()[sub_name + '_docs'])
    else:
        await session.send("不存在该子命令的帮助信息")


async def draw_run(session: BotSession, api: SdApi, *args) -> None:
    if len(args)<1 or len(args)>16:
        raise BotCmdExecFailed("提供的画图参数太少或太多")
    
    formatters = format_funcs.copy()[: len(args)]
    params = list(args)

    try:
        if params[0] in ('', '/'):
            await session.send("prompt 必须提供，不存在默认值，也不允许空值")
            return
        for i in range(len(params)):
            params[i] = format_with_defaults(formatters, i, params[i])
    except Exception as e:
        if len(params[i]) > 20:
            params[i] = params[i][:20] + '...'
        await session.send(f"参数格式化失败！对于参数 {arg_names[i]} 提供的值是 {params[i]}")
        return

    # 最后一个转为命名参数
    override_settings = None
    if len(params) == 16:
        override_settings = params[-1]
        params = params[:-1]

    try:
        await session.send("开始生成...")
        if session.event.msg.sender.id in superior_ids:
            req_func = functools.partial(api.txt2img, *params, override_settings=override_settings, limit_access=False)
        else:
            req_func = functools.partial(api.txt2img, *params)

        ret = await aio.get_running_loop().run_in_executor(None, req_func)
        images, draw_params, info = ret
        img_name = str(time.time())
        images[0].save(cq_image_path + img_name + '.png')

        await session.send_forward([
            custom_msg_node(
                image_msg(img_name + '.png', useCache=0),
                sendName="律汐 bot",
                sendId=BOT_STORE.meta.bot_id
            ),
            custom_msg_node(
                info.split(r'\n')[2],
                sendName="律汐 bot",
                sendId=BOT_STORE.meta.bot_id
            ),
            custom_msg_node(
                '正向提词：\n' + params[0],
                sendName="律汐 bot",
                sendId=BOT_STORE.meta.bot_id
            ),
            custom_msg_node(
                '反向提词：\n' + info.split(r'\n')[1][17:],
                sendName="律汐 bot",
                sendId=BOT_STORE.meta.bot_id
            )
        ])
        EXEC.callback(20, os.remove, cq_image_path + img_name + '.png')
    
    except SdApi.ApiBaseException as e:
        await session.send("异常抛出：\n" + e.err)
    except Exception as e:
        await session.send("异常抛出：\n" + e.__str__())


async def draw_status(session: BotSession, api: SdApi) -> None:
    try:
        endpoint = api.endpoint + '（ssh forward）'
        xformer_enable = api.store.cmd_args['xformers']
        opt_split_attention = api.store.cmd_args['opt_split_attention']
        disable_nan_check = api.store.cmd_args['disable_nan_check']
        nowebui = api.store.cmd_args['nowebui']
        no_half_vae = api.store.cmd_args['no_half_vae']
        no_half = api.store.cmd_args['no_half']
        model = api.store.options['sd_model_checkpoint']
        vae = api.store.options['sd_vae']
        clip = int(api.store.options['CLIP_stop_at_last_layers'])
        eta = api.store.options['eta_ancestral']
        eta_noise_seed_shift = int(api.store.options['eta_noise_seed_delta'])
        job_count, progress = api.job_count, round(float(api.progress), 3)*100

        status_str = f"远端 sd Server 状态： \n\
 ● 接口：{endpoint} \n\
 ● 正在进行的任务: {job_count}  {progress}%  \n\
 ● 当前模型：{model} \n\
 ● 当前 vae：{vae} \n\
 ● 当前 clip 步数：{clip} \n\
 ● eta：{eta} \n\
 ● eta 噪声种子偏移：{eta_noise_seed_shift} \n\
 ● 启用 xformers 优化：{xformer_enable}  \n\
 ● 启用跨注意层优化：{opt_split_attention}  \n\
 ● 禁用 nan 检查：{disable_nan_check}  \n\
 ● webui 同时启动：{not nowebui}  \n\
 ● 禁用半精度：{no_half}  \n\
 ● vae 上禁用半精度：{no_half_vae} \
"
        await session.send(status_str)
    except Exception as e:
        await session.send("异常抛出：\n" + e.__str__())


async def draw_options(session: BotSession, api: SdApi) -> None:
    lora_str_list = [lora_info[0] + f'（{lora_info[1]}）' for lora_info in api.store.loras]
    basic_sep = '\n'

    str_list = [
        f" ● 可用的模型：\n{ basic_sep.join(api.store.models) }",
        f" ● 可用的 vae：\n{ basic_sep.join(api.store.vaes) }",
        f" ● 可用的 loras（括号内为别称）：\n{ basic_sep.join(lora_str_list) }",
        f" ● 可用的采样器：\n{ basic_sep.join(api.store.samplers) }",
        f" ● 可用的超分算法：\n{ basic_sep.join(api.store.upsclaers) }",
        f" ● 可用的脚本：\n无（默认强制使用 nsfw 过滤脚本，其他不可用）"
    ]

    await session.send_forward([
        custom_msg_node(
            string,
            sendName="律汐 bot",
            sendId=BOT_STORE.meta.bot_id
        )
        for string in str_list
    ])


async def draw_set(session: BotSession, api: SdApi, *args) -> None:
    if session.event.msg.sender.id not in su_ids:
        return
    if len(args)%2 != 0:
        await session.send("配置名、值的个数不匹配")
        return

    names, vals = [], []
    for idx, arg in enumerate(args): 
        names.append(arg) if (idx+1)% 2 != 0 else vals.append(arg)

    try:
        for idx in range(len(vals)):
            vals[idx] = eval(vals[idx])
    except NameError:
        raise BotCmdExecFailed("任何配置项的值，请以 python 表达式格式给出，否则内部无法正确格式化类型")

    try:
        req_func = functools.partial(api.modify_option, dict(zip(names, vals)))
        refresh_func = functools.partial(api.refresh_store, api.store)
        await aio.get_running_loop().run_in_executor(None, req_func)
        await aio.get_running_loop().run_in_executor(None, refresh_func)
        await session.send("远端 sd 服务器配置已生效，本地缓存已更新")
    except SdApi.ApiBaseException as e:
        await session.send("异常抛出：\n" + e.err)
    except Exception as e:
        await session.send("异常抛出：\n" + e.__str__())