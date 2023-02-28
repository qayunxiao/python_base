# -*- coding: utf-8 -*-
# @Time    : 2023/2/26 11:09
# @Author  : alvin
# @File    : 列表和字典推导式.py
# @Software: PyCharm
key=['a','b','c']
value=["qa","test","yunxiao"]
d={}
for  i in range(len(key)):
    d[key[i]] =value[i]
print(d)

d2 = {keys:values for keys,values in zip(key,value) }
print(d2)
l=[i for i in range(10)]
print(l)
l2=(i for i in range(10))
print(l2)
for i in l2:
    print(i)