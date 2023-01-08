# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 9:13
# @Author  : alvin
# @File    : file_findfie.py
# @Software: PyCharm
import glob
target=glob.os.path.join(glob.os.getcwd(),"*")
def search(path):
    return glob.glob(path)

if __name__ == '__main__':
    res = search(target)
    print(res)