# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 11:47
# @Author  : alvin
# @File    : 匿名函数.py
# @Software: PyCharm
u_list=[
    {"username":"alvin","age":19},
    {"username":"tom","age":16},
    {"username":"kerry","age":20},
]
u_list.sort(key=lambda x:x['age'],reverse=True)
print(type(lambda x:x['age']))
print(u_list)
#匿名函数的参数是列表中的数据，在sort函数的内部，会调用key这个函数，从列表中获取的函数的返回值，返回值进行大熊啊比较
