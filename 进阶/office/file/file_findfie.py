# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 9:13
# @Author  : alvin
# @File    : file_findfie.py
# @Software: PyCharm
import glob
path=glob.os.path.join(glob.os.getcwd(),"*")
final_res=[]
#target 文件名。path查找路径
def search(path,target):
    res=glob.glob(path)
    for data in res:
        #文件夹
        if glob.os.path.isdir(data):
            _path=glob.os.path.join(data,"*")
            # print("{} is filepath".format(data))
            search(_path,target)
        else:
            if target in data:
                final_res.append(data)
    return final_res

if __name__ == '__main__':
    print("path",path)
    res=search(path,target="test2")
    print(res)