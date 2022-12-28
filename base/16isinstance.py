# -*- coding: utf-8 -*-
# @Time    : 2022/12/28 9:20
# @Author  : alvin
# @File    : 16isinstance.py
# @Software: PyCharm

#Python中的 isinstance() 函数，是Python中的一个内置函数，
# 用来判断一个函数是否是一个已知的类型，类似 type()

str1="a"
if not isinstance(str1, str):
    raise TypeError('str应该是字符串类型')
if isinstance(str1,dict):
    raise TypeError('str1应该是字符串类型')

if  isinstance(str1,tuple):
    print(str1)

class A:
    pass
class B(A):
    pass
print(isinstance(A(),A))
print(type(A()) == A)
print(isinstance(B(),A))
print(type(B()) == A ) #False