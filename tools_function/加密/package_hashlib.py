# -*- coding: utf-8 -*-
# @Time    : 2023/1/1 19:08
# @Author  : alvin
# @File    : package_hashlib.py
# @Software: PyCharm
import  time
import hashlib
base_sign="alvins"

def custom():
    a_timestamp =int( time.time())
    #根据时间戳 base_sign签名生成
    _token = "{}{}".format(base_sign,a_timestamp)
    hashobj = hashlib.sha512(_token.encode('utf-8'))#bytes类型
    a_token= hashobj.hexdigest()#16进制
    print(_token,a_token,a_timestamp)
    return a_token,a_timestamp

def b_service_check(token,timestamp):
    _token = "{}{}".format(base_sign,timestamp)
    #与客户端加密方式一致
    b_token = hashlib.sha512(_token.encode("utf-8")).hexdigest()
    if token == b_token:
        return True
    else:
        return False

if __name__ == '__main__':
    need_help_token,timestamp = custom()
    time.sleep(1)
    print(int(time.time()))
    result = b_service_check(need_help_token,timestamp)
    print(result)
    if result == True:
        print("a合法 b可以提供服务")
    else:
        print("a不合法 b不可以提供服务")
