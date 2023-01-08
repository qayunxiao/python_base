# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 9:13
# @Author  : alvin
# @File    : file_findfie.py
# @Software: PyCharm
import glob
target=glob.os.path.join(glob.os.getcwd(),"*")
def search(path):
    res=glob.glob(path)
    for data in res:
        if glob.os.path.isdir(data):
            _target=glob.os.path.join(data,"*")
            # print("{} is filepath".format(data))
            search(_target)
        else:
            print("{} is file".format(data))

if __name__ == '__main__':
    search(target)
