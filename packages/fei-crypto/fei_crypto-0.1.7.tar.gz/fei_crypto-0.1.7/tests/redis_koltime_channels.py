from tests import *
import os
import redis

if __name__ == '__main__':
    r = redis.Redis(
        host='192.168.123.11',
        port=6379,
        password=os.getenv('REDIS_PASSWORD'),
        db=0)

    pindao_sorted_set: list[tuple[str, float]] = [
        ('-1001822533506,实时新闻,https://t.me/+CLTXU0aHmOswNTZh', 4.0),
        ('-1002058073601,交易日志,https://t.me/+mfx6PIi_7nM2ZDY5', 4.0),
        ('-1002106742126,比特币峰哥,https://t.me/+ALTRP0Pi-sY2NTYx', 1.0),
        ('-1001928366759,比特智家人群,https://t.me/+Kczxm1APrzcwNDU5', 1.0),
        ('-1002141724703,舒琴vip信息发布群,https://t.me/+hmGkWmckS7Y5YWJh', 1.0),
        ('-1002125449406,米哥分析频道Pro,https://t.me/+4m43rMNGOoszNjFh', 1.0),
        ('-1001874907450,提阿菲罗-股市分析,https://t.me/+KmmXExqdWYZiZGFh', 2.0),
        ('-1001977744186,提阿菲罗-初始之塔,https://t.me/+DWnhqIKwGR40MDEx', 2.0),
        ('-1001913549306,提阿菲罗-BTC-ETH,https://t.me/+vfh0JTDzuFAwYjYx', 2.0),
        ('-1001608954412,提阿菲罗-山寨,https://t.me/+A2UMjV1d-ZE5ZDlh', 2.0),
        ('-1001872228180,提阿菲罗-互助,https://t.me/+p_60DbTEiORlZjUx', 2.0),
        ('-1001613491861,提阿菲罗-复盘,https://t.me/+BmsdHmwwa140ODY5', 2.0),
        ('-1001639092034,提阿菲罗-雜談,https://t.me/+XTA-jmOow7ozNmUx', 2.0),
        ('-1002044254306,Dr-Profit-Premium,https://t.me/+RXj4YrJ72slhZGZh', 3.0),
        ('-1001529044600,Vikings-VIP,https://t.me/+QF4vsy_ppks1NzRh', 3.0),
        ('-1002130903383,Scalping-300,https://t.me/+VdIoW3OXEnwzYzYx', 3.0),
        ('-1001802031399,Rose-Premium,https://t.me/+QJ1wqOrXGQAwMmIx', 3.0),
        ('-1001953261223,Future-125x,https://t.me/+hED0XsOgvFMxMTgx', 3.0),
        ('-1001922980030,CCC,https://t.me/+8atBs6zE9xE5MmFh', 3.0),
        ('-1002076500413,klondike,https://t.me/+e0mkiIGJ_xI0YTVh', 3.0),
        ('-1002007321187,WWG-Full,https://t.me/+yaH5J0goqYBlODYx', 3.0),
        ('-1002039765755,WWG-Coinguru,https://t.me/+RdPF6mSz4m8yODM5', 3.0),
        ('-1002136805635,WWG-Trades,https://t.me/+iHRaqQz6SKUzOWMx', 3.0),
        ('-1002006972061,WWG-Hbj,https://t.me/+NSaXsfZaOg0yOTNh', 3.0),
        ('-1002066980585,Eli,https://t.me/+QjNgmwjQtAYzM2Q5', 3.0),
        ('-1002137050425,Woods,https://t.me/+YfRWHc3Gq6JhOGQx', 3.0),
        ('-1002059758917,Johnny,https://t.me/+u4my9wuDIJo1ZDcx', 3.0),
        ('-1002007381555,Rezeh,https://t.me/+bnAFzhnFwnIyYjIx', 3.0),
    ]

    for v in pindao_sorted_set:
        r.zadd('koltime_menu_bot_channels', {v[0]: v[1]})
        print(v)
