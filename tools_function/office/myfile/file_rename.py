# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 13:59
# @Author  : alvin
# @File    : file_rename.py
# @Software: PyCharm
import  glob
import shutil


def update_name(path,replace_str):
    res = glob.glob(path)
    # print(res,type(res))
    for data in res:
        #如果res的列表中仍然是路径 进行递归
        if glob.os.path.isdir(data):
            _path = glob.os.path.join(data,'*')
            update_name(_path,replace_str)
        else:
            #[/home/xxx,name.text]
            path_list = glob.os.path.split(data)
            name = path_list[-1]
            new_name= name.replace(replace_str,"")
            new_data=glob.os.path.join(path_list[0],new_name)
            shutil.move(data,new_data)



if __name__ == '__main__':
    path = glob.os.path.join(glob.os.getcwd())
    replace_str="【海量资源：itwangzi.cn】"
    print(path)
    update_name(r"D:\Downloads\BaiduNetdiskDownload\体系课-Java工程师2022版",replace_str)