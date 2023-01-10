# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 13:59
# @Author  : alvin
# @File    : file_rename.py
# @Software: PyCharm
import  glob
import os
import shutil

def remove_file(path,remove_name):
    #所有文件和目录，并返回一个列表
    a=glob.glob(r'D:\IT\柠檬班-Python自动化测试35期\*')
    res = glob.glob(path)
    #data是路径
    for data in res:
        print("data",data)
        if glob.os.path.isdir(data):
            _path = glob.os.path.join(data,"*")
            # print("_path",_path)
            remove_file(_path,remove_name)
        else:
            # 路径分隔["D:\IT\柠檬班-Python自动化测试35期\01python基础\20201028_开班典礼","20201028_开班典礼.mp4"]
            path_list = glob.os.path.split(data)
            name = path_list[-1]
            if name == remove_name:
                print("remove data myfile",data)
                os.remove(data)



if __name__ == '__main__':
    path=r"D:\IT\12.【华测教育】接口自动化测试postman接口关联实战\接口postman一期"
    remove_name='资料.url'
    print(remove_name,path)
    res = remove_file(path,remove_name)

