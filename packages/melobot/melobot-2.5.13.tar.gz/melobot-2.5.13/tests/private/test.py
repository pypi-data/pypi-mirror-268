import sys

sys.path.append("../../src")


from rich import print

from melobot.utils.parser import CmdParser

p = CmdParser("/", " ", ["ask", "test", "789"])
a = p.parse("/ask")
b = p.parse("/ask test 123")
c = p.parse("asl;jdf;lajf;")


# import json
# import sys
# import time

# from rich import print

# sys.path.append("../../")
# sys.path.append("../../src")
# import asyncio
# import inspect
# from typing import Any

# from melobot import send_reply
# from melobot.base import BotAction
# from melobot.context.action import MsgDelActionArgs, _process_msg
# from melobot.models.msg import image_msg, text_msg
# from melobot.base.tools import is_retcoro


# def timeit(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         res = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f"{func.__name__} cost {end - start:0.9f}s")
#         return res

#     return wrapper


# def test2():
#     return 123


# async def test():
#     pass


# async def main():
#     alist = (
#         send_reply,
#         send_reply("123"),
#         asyncio.Future(),
#         asyncio.create_task(test()),
#         lambda: send_reply("123"),
#         test,
#         test(),
#         test2,
#         test2(),
#     )
#     res = (True, False, False, False, True, True, False, False, False)
#     print(tuple(is_retcoro(_, safe_mode=True) for _ in alist) == res)


# asyncio.run(main())

# # start = time.perf_counter()
# # e = MessageEvent(
# #     json.loads(
# #         '{"message_type":"private","sub_type":"friend","message_id":1961549407,"user_id":1574260633,"message":[{"type":"text","data":{"text":"123salkdjf;"}},{"type":"face","data":{"id":"179"}},{"type":"image","data":{"file":"https://multimedia.nt.qq.com.cn/download?appid=1406\u0026fileid=CgoxNTc0MjYwNjMzEhQKN-5rVLOAimuVKucqJjPpzAvSKhjUpgEg_goo6OfInq7BhQM\u0026rkey=CAMSMHAklpltlJtlxKiw85Hus6KgJCAgftqnl9Ha6Ng-Il6rrLoH84r_LeFjMFWyqgV5hA\u0026spec=0","url":"https://multimedia.nt.qq.com.cn/download?appid=1406\u0026fileid=CgoxNTc0MjYwNjMzEhQKN-5rVLOAimuVKucqJjPpzAvSKhjUpgEg_goo6OfInq7BhQM\u0026rkey=CAMSMHAklpltlJtlxKiw85Hus6KgJCAgftqnl9Ha6Ng-Il6rrLoH84r_LeFjMFWyqgV5hA\u0026spec=0","summary":"[\u52A8\u753B\u8868\u60C5]"}}],"raw_message":"123salkdjf;[CQ:face,id=179][CQ:image,file=https://multimedia.nt.qq.com.cn/download?appid=1406\u0026amp;fileid=CgoxNTc0MjYwNjMzEhQKN-5rVLOAimuVKucqJjPpzAvSKhjUpgEg_goo6OfInq7BhQM\u0026amp;rkey=CAMSMHAklpltlJtlxKiw85Hus6KgJCAgftqnl9Ha6Ng-Il6rrLoH84r_LeFjMFWyqgV5hA\u0026amp;spec=0]","font":0,"sender":{"user_id":1574260633,"nickname":"Melorenae\u5F8B\u56DE","sex":"unknown"},"time":1713085889,"self_id":1801297943,"post_type":"message"}'
# #     )
# # )
# # print(f"{e:hexid}, {e:raw}")
# # a = BotAction(MsgDelActionArgs(12312131231233), "13781273712983")
# # print()
# # print(f"{a:hexid}, {a:raw}")
# # print(time.perf_counter() - start)
