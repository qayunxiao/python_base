# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 10:29
# @Author  : alvin
# @File    : 正则替换.py
# @Software: PyCharm
import re
language = 'PythonC#JavaPHPC#PHPC#'
# 把 C#转换为go
r = re.sub('C#','GO',language)
print(r)
# res = re.findall('.+@.+\.[a-zA-Z]+',data)
# print(res)
# return res

def findnum(string):
    comp=re.compile("[1-9]\d")
    list_str=comp.findall(string)
    list_num=[]
    for item in list_str:
        item=int(item)
        list_num.append(item)
    return list_num