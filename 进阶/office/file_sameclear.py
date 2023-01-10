# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 9:55
# @Author  : alvin
# @File    : file_sameclear.py
# @Software: PyCharm
import  glob
import hashlib

data = {}


def clear(path):
    global f
    res = glob.glob(path)
    for _data in res:
        if glob.os.path.isdir(_data):
            _path= glob.os.path.join(_data,"*")
            clear(_path)
        else:
            name = glob.os.path.split(_data)[-1]
            is_byte=False
            # print(name,data)
            if name in data:
                sub_data = data[name]
                is_delete=False
                for k,v in sub_data.items():
                    if v== get_md5(_data):
                        # glob.os.remove(_data)
                        print("will delete {}".format(_data))
                        is_delete = True
                if not is_delete:
                    data[name][_data]=get_md5(_data)

            else:
                data[name] = {
                    _data:get_md5(_data)
                }

def get_md5(filepath):
    file_type_list=["zip","rar","mp4"]
    name = glob.os.path.split(filepath)[-1]
    fix_name = name.split(".")[-1]
    if fix_name in file_type_list:
        with open(filepath,'rb') as f:
            content = f.read()
            hash_content_obj = hashlib.md5(content)
    else:
        with open(filepath,'r',encoding="utf-8") as f:
            content = f.read()
            hash_content_obj = hashlib.md5(content.encode("utf-8"))
    hash_content=hash_content_obj.hexdigest()
    return hash_content

if __name__ == '__main__':
    # path = glob.os.path.join(r"D:\IT\12.【华测教育】接口自动化测试postman接口关联实战","*")
    path = glob.os.path.join(glob.os.getcwd(),"myfile","*")
    print("path",path)
    clear(path)

    # print(data)
    for i,v in data.items():
        for _k,v in v.items():
            print(i,_k,v)
    # get_md5(r"D:\Sourcetree\yunxiao\python_base\进阶\office\myfile\file_test.py")
