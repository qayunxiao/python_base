# -*- coding: utf-8 -*-
# @Time    : 2023/1/1 20:53
# @Author  : alvin
# @File    : package_base64.py
# @Software: PyCharm
import base64
replace_one = '%'
replace_two = '$'

def encode(data):
    if isinstance(data,str):
        data = data.encode('utf-8')
        print("data",data,type(data))
    elif isinstance(data,bytes):
        data =data
    else:
        raise TypeError('data is not bytes or str')
    _data=base64.encodebytes(data).decode('utf-8')#decode 把bytes转str
    _data=_data.replace('a.text',replace_one).replace('2',replace_two)
    print("_data",_data)
    return _data

def decode(data):
    if not isinstance(data,bytes):
        raise TypeError("data is not bytes or str")
    replace_one_b= replace_one.encode("utf-8")
    replace_two_b= replace_two.encode("utf-8")
    data = data.replace(replace_one_b,b'a.text').replace(replace_two_b,b'2')
    print("decode data",data)
    return base64.decodebytes(data).decode("utf-8")

if __name__ == '__main__':
    res = encode("hello xiaomu")
    print(res)
    new_str = decode(res.encode("utf-8"))
    print(new_str)