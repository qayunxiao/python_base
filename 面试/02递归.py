# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 11:29
# @Author  : alvin
# @File    : 02递归.py
# @Software: PyCharm
def add(i):
    if i == 0:
        return 0
    return i + add(i-1)
print(add(10))