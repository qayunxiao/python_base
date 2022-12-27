# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 11:34
# @Author  : alvin
# @File    : 装饰器.py
# @Software: PyCharm
import datetime

def runtime(func):
    def warpper():
        print(datetime.datetime.now())
        return func()
    return warpper

@runtime
def my_func1():
    print("函数1运行")
my_func1()