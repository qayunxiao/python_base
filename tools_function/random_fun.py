# -*- coding: utf-8 -*-
# @Time    : 2023/1/2 11:30
# @Author  : alvin
# @File    : random_fun.py
# @Software: PyCharm

import random
print(random.random()) #0-1浮点小数
print(random.uniform(1,10))# 1-10返回随机浮点数
print(random.randint(1,100))# 1-100返回随机整数
print(random.choice(['a','b','c']))
print(random.choice("abcdef"))
print(random.choice((1,2,3,4,5,6)))
print(random.sample(['a','b','c','d','e'],2)) #返回指定元素个数 列表类型
print(random.sample("abcdef",2)) #返回指定元素个数
print(random.randrange(0,100,1))
print(random.choice(  range(0,100,1) ))
for i in range(0,100,2):
    print(i)