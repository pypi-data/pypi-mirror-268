import base64
import os

if __name__ == '__main__':
    print(os.getcwd())
    current_path = os.path.dirname(os.path.abspath(__file__))
    print(current_path)  # 获取当前 Python 脚本所在的路径)
    file_path = os.path.join(current_path, './captcha.jpg')  # 拼接相对路径
    print(file_path)
    with open(file_path, 'rb') as f:
        b64_string = base64.b64encode(f.read())
    print(b64_string.decode('utf-8'))

    print(os.path.basename('e:/github/feicrypto/fei-crypto-python/media/videos/360p15/btc.mp4'))
