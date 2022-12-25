# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 11:19
# @Author  : alvin
# @File    : reduce自动堆叠计算函数.py
# @Software: PyCharm
from functools import reduce
a=[2,4,6,8,10]
def add(x,y):
    return x+y
res = reduce(add,a)
print(res)
