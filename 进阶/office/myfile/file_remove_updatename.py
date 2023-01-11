# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 9:54
# @Author  : alvin
# @File    : file_remove_updatename.py
# @Software: PyCharm
import glob
import os
import shutil
import re

from log.package_log import init_log

data = {}
type_set = {"text","mp4"}
current=os.getcwd()
paths = os.path.join(current,'back.log')
log=init_log(paths)

def remove_updatename(path,remove_name_list,replace_list):
    #返回路径列表
    res = glob.glob(path)
    for data in res:
        if glob.os.path.isdir(data):
            print("data",data)
            _path = glob.os.path.join(data,"*")
            print("_path",_path)
        #递归
            remove_updatename(_path,remove_name_list,replace_list)
        else:#如果不是路径，获取文件名
            path_list = glob.os.path.split(data)
            name = path_list[-1]
            for remove_name in remove_name_list:
                if name == remove_name:
                    # print("remove data name",data)
                    log.info("remove data name:{}".format(data))
                    os.remove(data)
            #如果需要替换的字符串在文件名里面 去替换成空
            for update_replace in replace_list:
                if update_replace in name:
                    new_name = name.replace(update_replace,"")
                    new_path = glob.os.path.join(path_list[0],new_name)
                    # print("update_replace-data",data )
                    # print("update_replace-new_path",new_path)
                    log.info("update_replace-new_path:{}".format(new_path))
                    shutil.move(data,new_path)
    return "处理完成"

def fix_name(path,sub_start):
    # 387702291210209022_Django应用2_.mp4
    sub_start=sub_start+1
    res = glob.glob(path)
    for data in res:
        if glob.os.path.isdir(data):
            _path = glob.os.path.join(data,"*")
            fix_name(_path,sub_start)
        else:
            path_list=glob.os.path.split(data)
            name = path_list[-1]
            new_name  = name[sub_start:]
            # print("new_name",new_name)
            new_data = glob.os.path.join(path_list[0],new_name)
            # print("new_data",new_data)
            # print("data",data)
            shutil.move(data,new_data)
    return "处理完成"

if __name__ == '__main__':
    path =r"G:\IT王子"
    remove_name_list=["思索IT获取更多课程.url","资料.url",
                      "面试合集.txt","看看我【www.sisuoit.com】.zip",
                      "软件下载.txt","下载必看【www.sisuoit.com】.txt"]
    replace_list=["【itwangzi资源站：itwangzijava .cn】","【海量资源：itwangzi.cn】"
                  ,"更多it课程访问www.itwangzi.com","【更多IT教程 微信itwangzi】"
        ,"【更多教程微信：itwangzi】","【海量一手：itwangzi .cn】","【itwangzi资源站：itwangzijava .cn】"
        ,"【itwangzi资源站：itwangzijava .cn】"]
    res=remove_updatename(path,remove_name_list,replace_list)
    print(res)
    # sub_start=16
    # fix_name(path,sub_start)