# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 10:02
# @Author  : alvin
# @File    : 闭包.py
# @Software: PyCharm
# def fun1():
#     print("函数1运行")
#     return fun2
# def fun2():
#     print("函数2运行")
#     return 2
# r=fun1()
# print(r)
# r2=r() #r=func2
# print(r2)

def fun1():
    print("函数1运行")
    def fun2():
        print("函数2运行")
    return fun2
f2=fun1()
print(f2)
f2()
#在一个函数，比如func1中的内部定义了另外一个函数func2 并且func1的返回值是fun2的一个引用（函数名） 这就是闭包