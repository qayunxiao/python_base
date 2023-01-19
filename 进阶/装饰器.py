# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 10:40
# @Author  : alvin
# @File    : 装饰器.py
# @Software: PyCharm

# 装饰器
# 语法糖   java语言中，注解
#
# def runtime(func):
#     def warpper():
#         print(1)
#         return func()
#     return warpper
#
# @runtime
# def my_func1():
#     print("函数1运行")
#     return 2
#
# r = my_func1()
# print(r)

# 导入外部模块
# import c1
# c1.func1()
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

@runtime
def my_func2():
    print("函数2运行")

my_func2()

# pytest_demo

