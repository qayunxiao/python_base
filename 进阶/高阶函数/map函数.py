# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 11:10
# @Author  : alvin
# @File    : map函数.py
# @Software: PyCharm
my_l =[1,2,3,4,5]
def add_one(e):
    return e +1
r= map(add_one,my_l)
print(list(r))#[2, 3, 4, 5, 6]
print(list (map(lambda e:e+1,my_l)) )