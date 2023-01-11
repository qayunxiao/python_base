# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 9:55
# @Author  : alvin
# @File    : file_sameclear.py
# @Software: PyCharm
import  glob
import hashlib
import os
from package_log import  init_log

data = {}
type_set = {"text","mp4"}
current=os.getcwd()
paths = os.path.join(current,'back.log')
log=init_log(paths)

# log.warning("this is first warn log info")

def clear(path):
    global f
    res = glob.glob(path)
    file_count=0
    for _data in res:
        if glob.os.path.isdir(_data):
            _path= glob.os.path.join(_data,"*")
            clear(_path)
        else:
            name = glob.os.path.split(_data)[-1]
            is_byte=False
            file_count=file_count+1
            # print(name,data)
            if name in data:
                sub_data = data[name]
                is_delete=False
                for k,v in sub_data.items():
                    if v== get_md5_any(_data):
                        # glob.os.remove(_data)
                        log.info("will delete path:"+_data +" md5 is:"+get_md5_any(_data)+" k is:"+k)
                        is_delete = True
                if not is_delete:
                    data[name][_data]=get_md5_any(_data)
            else:
                data[name] = {
                    _data:get_md5_any(_data)
                }
            # print("file_count",file_count)

def get_md5(filepath):
    file_type_list=['7z', 'css', 'mp4', 'handlebars', 'txt', 'cfg', 'asf',
                    'exe', 'tif', 'gif', 'js', 'PNG', 'ppt', 'avi', 'png', 'CR2',
                    'dmg', 'LICENSE', 'FLV', 'BUP', 'MOV', 'TIF', 'db', 'rar',
                    'vob', 'f4v', 'zip', 'json', 'pdf', '3FR', 'psd', 'jpg',
                    'url', 'swf', 'mht', 'docx', 'text', 'dng', 'doc', 'VOB',
                    'JPG', 'm4a', 'html', 'IFO']
    name = glob.os.path.split(filepath)[-1]
    fix_name = name.split(".")[-1]
    if fix_name in file_type_list:
        with open(filepath,'rb') as f:
            print("filepath rb",filepath)
            content = f.read()
            hash_content_obj = hashlib.md5(content)
    else:
        with open(filepath,'r',encoding="utf-8") as f:
            print("filepath r",filepath)
            content = f.read()
            hash_content_obj = hashlib.md5(content.encode("utf-8"))
    hash_content=hash_content_obj.hexdigest()
    return hash_content

def get_md5_any(filepath):
    name = glob.os.path.split(filepath)[-1]
    fix_name = name.split(".")[-1]
    if fix_name not in type_set:
        type_set.add(fix_name)
    try:
        with open(filepath,'rb') as f:
            # print("get_md5_any filepath rb",filepath)
            content = f.read()
    except Exception as e:
        print(e)
        content=b' 1'
    hash_content_obj = hashlib.md5(content)
    hash_content=hash_content_obj.hexdigest()
    return hash_content


if __name__ == '__main__':
    # path = glob.os.path.join(r"D:\IT\12.【华测教育】接口自动化测试postman接口关联实战","*")
    path = glob.os.path.join(r"D:\work\hl","*")
    clear(path)
    print("type_set",type_set)
    print("over")
    # print(data)
    # for i,v in data.items():
    #     for _k,v in v.items():
    #         print(i,_k,v)
    # get_md5(r"D:\Sourcetree\yunxiao\python_base\进阶\office\myfile\file_test.py")
