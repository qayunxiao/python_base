# -*- coding: utf-8 -*-
# @Time    : 2023/2/17 11:30
# @Author  : alvin
# @File    : 高级数据类型-集合set.py
# @Software: PyCharm
#set 集合是无序的，所以每次输出时元素的排序顺序可能都不相同。
#只能存储不可变的数据类型，包括整形、浮点型、字符串、元组，无法存储列表、字典、集合这些可变的数据类型，否则 Python 解释器会抛出 TypeError 错误
a={1,'c',True,(1,2,3)}
# print(a)
#创建空集合，只能使用 set() 函数实现。因为直接使用一对 {}，Python 解释器会将其视为一个空字典。
setb=set()
#访问集合元素最常用的方法是使用循环结构，将集合中的数据逐一读取出来。
# a1 = {1,'c',1,(1,2,3),'c'}
# for ele in a1:
#     print(ele,end=' ')
#列表去重，转set集合即可
alist=[1,"ab","cb",5,'ab',3,2,1]
aset1=set(alist)
print(aset1)
blist = list(aset1)
print(blist)
aset1.add(6)
print(aset1)
aset1.pop()
print(aset1,type(aset1))
# aset1.clear()
aset1.remove(6)
print(aset1)
# del aset1
