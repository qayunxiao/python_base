# -*- coding: utf-8 -*-
# @Time    : 2023/1/2 14:48
# @Author  : alvin
# @File    : package_filter.py
# @Software: PyCharm
from functools import  reduce
frunts=["apple",'banana',"orange"]
#含有e的单次保留
res = filter(lambda x:'e' in x ,frunts)
print(list(res))

def filter_func(item):
    if "e" in item:
        return True
filter_res = filter(filter_func,frunts)
print(list(filter_res))

map_res = map(filter_func,frunts)
print(list(map_res))

reduce_res = reduce(lambda x,y:x+y,[0,1,2,3])
print(reduce_res)

reduce_str_res = reduce(lambda x,y:x+y,frunts)
print(reduce_str_res)