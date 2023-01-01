# -*- coding: utf-8 -*-
# @Time    : 2023/1/1 19:08
# @Author  : alvin
# @File    : package_hashlib.py
# @Software: PyCharm
import  time
import hashlib
base_sign="muke"

def custom():
    a_timestamp =int( time.time())
    _token = "{}{}".format(base_sign,a_timestamp)
    hashobj = hashlib.sha1(_token.encode('utf-8'))
    a_token= hashobj.hexdigest()
    print(a_token,a_timestamp)
    return a_token,a_timestamp

def b_service_check(token,timestamp):
    _token = "{}{}".format(base_sign,timestamp)
    b_token = hashlib.sha1(_token.encode("utf-8")).hexdigest()
    if token == b_token:
        return True
    else:
        return False

if __name__ == '__main__':
    need_help_token,timestamp = custom()
    time.sleep(1)
    print(int(time.time()))
    result = b_service_check(need_help_token,int(time.time()))
    print(result)