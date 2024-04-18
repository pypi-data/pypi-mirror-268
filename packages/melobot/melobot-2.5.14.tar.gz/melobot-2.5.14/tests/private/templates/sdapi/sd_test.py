from api import SdApi


api = SdApi()
prompt = '(((masterpiece))),(((best quality))),((an extremely delicate and beautiful)),(((extremely detailed 8k wallpaper))),a sunny day,((whole body shot)),(in a grassland),(detailed grass),(((only one girl))),((a girl sitting on grass)),((look at viewer sideway)),(long hair over shoulder),((aqua gradient hair)),((crossed bangs)),hair between eyes,(white hair flower with green leaves),detailed face,(beautiful detailed eyes),(aqua eyes),detailed mouth and nose,(cute smile),light blush,small breasts,((aqua serafuku with a bow)),aqua skirt,((yokozuwari)),((slender legs)),white pantyhose,((brown loafers shoe)),beautiful and warm lighting'
negative_prompt = 'nsfw,lowres,bad anatomy,bad hands,((bad legs)),((three or four legs)),(bad feet),text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry,bad mouth,(((two girls)))'
steps = 28
seed = 3736812062
subseed = 1016585624
strength = 0.1
cfg = 8
denosing = 0.4


images, params, info = api.txt2img(prompt, negative_prompt, steps=steps, cfg_scale=cfg, seed=seed, 
                                   subseed=subseed, subseed_strength=strength, limit_access=False)
images[0].save('./test.png')
print(info.split(r'\n')[2])