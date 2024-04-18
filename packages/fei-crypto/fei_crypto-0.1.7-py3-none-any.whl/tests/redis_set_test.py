from tests import *
import os
import redis

if __name__ == '__main__':
    r = redis.Redis(
        host='127.0.0.1',
        port=6379,
        password=os.getenv('REDIS_PASSWORD'),
        db=0)

    pindao_dict: dict[str, list[tuple[str]]] = {}
    score_dict: dict[float, str] = {
        1.0: '中文博主',
        2.0: '提阿非罗',
        3.0: '英文博主',
        4.0: 'koltime'
    }

    channels = r.zrange("sorted_channels", 0, 1000, withscores=True)
    for item in channels:
        pindao = pindao_dict.setdefault(score_dict[item[1]], [])
        pindao.append(tuple(item[0].decode().split(',')))

        # print(item)
        # print(type(item[1]))
        # channel_info = item[0].decode().split(',')
        # print(channel_info[1], channel_info[2])

    text = "📚频道列表👇\n"
    for k, v in pindao_dict.items():
        text += f'【{k}】\n'
        for v_item in v:
            text += f'[{v_item[1]}]({v_item[2]})\n'

        text += '\n'

    print(text)
