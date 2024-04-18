import base64

from tests import *
import os
import redis

if __name__ == '__main__':
    r = redis.Redis(
        host='192.168.123.11',
        port=6379,
        password=os.getenv('REDIS_PASSWORD'),
        db=0)
    with open("d:/BaiduSyncdisk/assets/png/koltime/koltime_menu_bot.png", "rb") as f:
        base64_data = base64.b64encode(f.read()).decode()
        r.hsetnx('koltime_menu_bot', 'pic_base64', base64_data)

    caption = """
🎉 欢迎您来到koltime社区

📈 我们是华语₿圈信息聚合平台

🦄 50+全球优质博主会员信息 
🦄 100+频道即时同步、7x24小时更新 
🦄 价值2万U的教学视频  
🦄 信息即时翻译、无障碍浏览国内外优质内容
🦄 定期淘汰表现不佳的博主，无需担心踩雷  
🦄 1年+稳定不间断运行 

✨✨✨ 一切尽在koltime!
    """
    r.hsetnx('koltime_menu_bot', 'description', caption)
    r.hsetnx('koltime_menu_bot', 'pic_url', 'https://arweave.net/DZ_ZI6r4pfVP5u0e-lCOGESM4JMjN0OPXVrgyZLrU8U')
    description = r.hget('koltime_menu_bot', 'description')
    print(type(description))
    if isinstance(description, bytes):
        print(description.decode())

    # r.hsetnx('koltime_menu_bot', 'pic', pic)
    # print(r.hget('koltime_menu_bot', 'desc'))
