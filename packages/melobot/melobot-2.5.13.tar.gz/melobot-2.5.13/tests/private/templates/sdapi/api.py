import base64
import io
import json
import os
from typing import Any, Dict, List, Tuple

import requests
from PIL import Image
from requests import Response


class SdApi:

    class ApiBaseException(Exception):
        def __init__(self, err: str):
            super().__init__()
            self.err = f"[SdApiException] {err}"
            self.origin_err = err

        def __str__(self):
            return self.err

    class ValueError(ApiBaseException):
        def __init__(self, err: str):
            super().__init__(err)

    class ResponseError(ApiBaseException):
        def __init__(self, err: str):
            super().__init__(err)

    class ApiStore:
        def __init__(self) -> None:
            self.models: List[str]
            self.loras: List[Tuple[str, str]]
            self.samplers: List[str]
            self.upsclaers: List[str]
            self.options: Dict[str, str]
            self.cmd_args: Dict[str, str]
            self.scripts: Dict[str, List[str]]
            self.vaes: List[str]

        def fill(
            self,
            models,
            loras,
            samplers,
            upscalers,
            options,
            cmd_args,
            scripts,
            vae_list,
        ) -> None:
            (
                self.models,
                self.loras,
                self.samplers,
                self.upsclaers,
                self.options,
                self.cmd_args,
                self.scripts,
                self.vaes,
            ) = (
                models,
                loras,
                samplers,
                upscalers,
                options,
                cmd_args,
                scripts,
                vae_list,
            )

    def __init__(self) -> None:
        self.config_path = (
            os.sep.join(os.path.join(__file__).split(os.sep)[:-1])
            + os.sep
            + "config.json"
        )

        with open(self.config_path, encoding="utf-8") as fp:
            config = json.load(fp)
            self.endpoint = config["endpoint"]
            self.auth_user = config["username"]
            self.auth_pwd = config["password"]
            self.negative_prompt_default = config["negative_defaults"]
        self.session = requests.Session()
        self.session.auth = (self.auth_user, self.auth_pwd)

        self.store = SdApi.ApiStore()
        self.refresh_store(self.store)

    @property
    def progress(self) -> float:
        return self._get("/progress")["progress"]

    @property
    def job_count(self) -> int:
        return self._get("/progress")["state"]["job_count"]

    def _get(
        self,
        path: str,
        params: dict = None,
        headers: dict = None,
        pureResp: bool = False,
    ) -> dict | list | Response:
        resp = self.session.get(self.endpoint + path, params=params, headers=headers)
        if resp.status_code != 200:
            raise SdApi.ResponseError(
                f"error code: {resp.status_code}, content: {resp.json()}"
            )
        return resp if pureResp else resp.json()

    def _post(
        self,
        path: str,
        data: dict = None,
        headers: dict = None,
        pureResp: bool = False,
        jsonSendMode: bool = True,
    ) -> dict | list | Response:
        if jsonSendMode:
            resp = self.session.post(self.endpoint + path, json=data, headers=headers)
        else:
            resp = self.session.post(self.endpoint + path, data=data, headers=headers)

        if resp.status_code != 200:
            raise SdApi.ResponseError(
                f"error code: {resp.status_code}, content: {resp.json()}"
            )
        return resp if pureResp else resp.json()

    def _get_models(self) -> List[str]:
        content = self._get("/sd-models")
        return [model_info["title"] for model_info in content]

    def _get_loras(self) -> List[Tuple[str, str]]:
        content = self._get("/loras")
        return [(lora_info["name"], lora_info["alias"]) for lora_info in content]

    def _get_samplers(self) -> List[str]:
        content = self._get("/samplers")
        return [sampler_info["name"] for sampler_info in content]

    def _get_upsclaers(self) -> List[str]:
        content = self._get("/upscalers")
        return [upscaler_info["name"] for upscaler_info in content]

    def _get_options(self) -> Dict[str, str]:
        return self._get("/options")

    def _get_cmd_args(self) -> Dict[str, str]:
        return self._get("/cmd-flags")

    def _get_scripts(self) -> Dict[str, List[str]]:
        return self._get("/scripts")

    def _get_vaes(self) -> Dict[str, List[str]]:
        vae_infos = self._get("/sd-vae")
        return [info["model_name"] for info in vae_infos]

    def refresh_store(self, store: ApiStore) -> None:
        store.fill(
            self._get_models(),
            self._get_loras(),
            self._get_samplers(),
            self._get_upsclaers(),
            self._get_options(),
            self._get_cmd_args(),
            self._get_scripts(),
            self._get_vaes(),
        )
        # print("已刷新本地缓存")

    def skip(self) -> None:
        self._post("/skip")

    def interrupt(self) -> None:
        self._post("/interrupt")

    def modify_option(self, args: Tuple[str, str] | Dict[str, Any]) -> None:
        if isinstance(args, tuple):
            args = {args[0]: args[1]}
        self._post("/options", data=args)

    def txt2img(
        self,
        prompt: str,
        negative_prompt: str = None,
        width: int = 512,
        height: int = 512,
        steps: int = 20,
        sampler_name: str = "DPM++ 3M SDE Karras",
        cfg_scale: float = 7,
        seed: int = None,
        subseed: int = None,
        subseed_strength: float = None,
        enable_hr: bool = None,
        denoising_strength: float = None,
        hr_scale: int = None,
        hr_upscaler: str = None,
        hr_second_pass_steps: int = None,
        script_name: str = None,
        script_args: list = None,
        override_settings: Dict[str, str] = None,
        limit_access: bool = True,
    ) -> Tuple[List[Image.Image], dict, str]:
        """
        返回 Image 列表，生成参数字典，生成信息
        """
        if limit_access:
            if len(prompt) > 1000:
                raise SdApi.ValueError("正向提示词限制长度 1000")
            if negative_prompt is not None and len(negative_prompt) > 500:
                raise SdApi.ValueError("负向提示词限制长度 500")
            if width < 100 or width > 960 or height < 100 or height > 960:
                raise SdApi.ValueError("宽高限制： [100, 960]")
            if width * height > 518400:
                raise SdApi.ValueError("宽高乘积不得大于 518400")
            if steps < 10 or steps > 60:
                raise SdApi.ValueError("步数限制：[10, 60]")
            if cfg_scale < 1 or cfg_scale > 30:
                raise SdApi.ValueError("cfg限制：[1, 30]")
            if subseed_strength is not None and (
                subseed_strength < 0 or subseed_strength > 1
            ):
                raise SdApi.ValueError("差异随机种子限制：[0, 1]")
            if enable_hr is not None or override_settings is not None:
                raise SdApi.ValueError("无权使用高清修复或临时配置功能")
            (
                enable_hr,
                denoising_strength,
                hr_scale,
                hr_upscaler,
                hr_second_pass_steps,
                override_settings,
            ) = (None, None, None, None, None, None)
            script_name, script_args = "censorscript", [True, True]

        if negative_prompt is None:
            negative_prompt = self.negative_prompt_default

        copyed_args = locals().copy()
        copyed_args.pop("self")
        copyed_args.pop("limit_access")
        copyed_args = {k: v for k, v in copyed_args.items() if v is not None}

        content = self._post("/txt2img", data=copyed_args)
        return (
            [
                Image.open(io.BytesIO(base64.b64decode(image.split(",", 1)[0])))
                for image in content["images"]
            ],
            content["parameters"],
            content["info"],
        )
