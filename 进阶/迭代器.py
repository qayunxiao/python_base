# -*- coding: utf-8 -*-
# @Time    : 2023/1/2 14:26
# @Author  : alvin
# @File    : 迭代器.py
# @Software: PyCharm
iter_obj = iter((1,2,3))
def _next(iter_obj):
    try:
        return next(iter_obj)
    except StopIteration:
        return None

# print(_next(iter_obj))
# print(_next(iter_obj))
# print(_next(iter_obj))
# print(_next(iter_obj))

for i in  iter_obj:
    print(i)
def make_iter():
    for i in range(10):
        yield i

iter_objs = make_iter()
#内存数据空了
for i in iter_objs:
    print(i)
print("--------")
for i in iter_objs:
    print(i)

iter_o = (i for i in range(10))
for i in iter_o:
    print(i)
print("+++++++++")
for i in iter_o:
    print(i)
list=["al","ds","22"]
ite = iter(list)
for i in ite :
    print(i)