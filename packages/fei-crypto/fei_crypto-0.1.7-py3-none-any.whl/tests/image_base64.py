import base64
import os
import requests
from dotenv import load_dotenv

load_dotenv('d:/.env')

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, './captcha.jpg')
    with open(file_path, 'rb') as f:
        b64_string = base64.b64encode(f.read()).decode('utf-8')
    print(b64_string)
    host = 'https://yzmcolor.market.alicloudapi.com'
    request_path = '/yzmSpeed'
    method = 'POST'
    appcode = os.getenv('ALIYUN_OCR_APPCODE')
    url = host + request_path
    header = {'Authorization': 'APPCODE ' + appcode, "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}
    data = {
        'pri_id': 'dn',
        'v_pic': b64_string
    }
    resp = requests.post(url, data=data, headers=header)
    print('-' * 50)
    print("status_code:{0}".format(resp.status_code))
    print("resp_text:{0}".format(resp.text))
    print("resp_json:{0}".format(resp.json()))
    print("resp_json:{0}".format(resp.json()['v_code']))
    print("resp_json:{0}".format(resp.json()['msg']))
    print("resp_json:{0}".format(resp.json()['errCode']))
