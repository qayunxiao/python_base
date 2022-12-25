# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 10:56
# @Author  : alvin
# @File    : Lambda表达式.py
# @Software: PyCharm
import math
def circle_area(r):
    result = math.pi * r * r
    return result

r = circle_area(3)
print(r)
"""
lambda 是一个关键字
冒号前边的r是这个函数的参数
冒号后边的是这个函数的运算逻辑
"""

result = lambda r:math.pi * r * r
r = result(3)
print(r)

def calc_function(o):
    if o == "+":
        return lambda a,b : a + b
    elif o == "-":
        return lambda a,b : a - b
    elif o == "*":
        return lambda a,b : a * b
    elif o == "/":
        return lambda a,b : a / b

f = calc_function("*")
print(f)
r = f(3,4)
print(r)
