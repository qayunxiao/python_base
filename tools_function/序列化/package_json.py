# -*- coding: utf-8 -*-
# @Time    : 2023/1/1 17:00
# @Author  : alvin
# @File    : package_json.py
# @Software: PyCharm
import json
from log.package_log import init_log

log = init_log("json.log")
def read(path):
    with open(path,'r') as f:
        data= f.read()
    return json.loads(data)

def write(path,data):
    with open(path,"w") as f:
        if isinstance(data,dict):
            _data = json.dumps(data)
            f.write(_data)
        else:
            log.error("data is dict")
            raise  TypeError("data is dict")

data = {"name":"avlv","age":18,"top":179}

def my_wirte_json():
    with open("my_json.json","w",encoding="utf8") as f:
        f.write(json.dumps({"name":"海林","age":18,"top":179}))

if __name__ == '__main__':
    write("package_json.text",data)
    # res = read("package_json.text")
    # print(res,type(res))
    # res['sex']='b'
    # print(res)
    # write()