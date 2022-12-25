# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 20:34
# @Author  : alvin
# @File    : 高级数据类型-列表.py
# @Software: PyCharm
dict1={"name":"alvin","age":20}
dict2={"addr":"北京"}
#访问所以的键
print(dict1.keys())
print(dict1.values())
print(dict1['name'])
dict1.update(dict2)
dict1['name']="AI"
dict1.pop("name")
print(dict1)
