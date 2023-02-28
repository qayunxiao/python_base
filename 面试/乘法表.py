# -*- coding: utf-8 -*-
# @Time    : 2023/2/27 9:39
# @Author  : alvin
# @File    : 乘法表.py
# @Software: PyCharm

for row in range(1,10):
    for sub in range(1,row+1):
        print("{}+{}={}".format(sub,row,sub*row),end=' ')
    print()#换行