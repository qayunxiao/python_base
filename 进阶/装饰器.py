# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 10:40
# @Author  : alvin
# @File    : 装饰器.py
# @Software: PyCharm

# 装饰器   装饰器本质上是一个Python函数(其实就是闭包)，它可以让其他函数
# 在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
# 装饰器用于有以下场景，比如:插入日志、性能测试、事务处理、缓存、权限校验等场景。
# def runtime(func):
#     def warpper():
#         print(1)
#         return func()
#     return warpper
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

