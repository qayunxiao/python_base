# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 11:16
# @Author  : alvin
# @File    : 01函数.py
# @Software: PyCharm

my_list1=[1,2]
def func(list1):
    list1.append(10)
func(my_list1)
print(my_list1)#[1, 2, 10]

my_list2=[1,2]
def func2(list1):
    list1[0]=10
func2(my_list2)
print(my_list2)#[10, 2]

my_list3=["a","b"]
def func3(list1):
    list1 +=[1,2] #list1.extend([1,2])
func3(my_list3)
print(my_list3)#['a', 'b', 1, 2]