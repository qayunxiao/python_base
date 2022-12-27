# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 11:37
# @Author  : alvin
# @File    : 交换变量拆包.py
# @Software: PyCharm
a=10
b=20
c=a
a=b
b=c
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)
a,b = b,a
print(a,b)
x,y,z=[1,2,3]
print(x,y,z)