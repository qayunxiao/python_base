# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 21:11
# @Author  : alvin
# @File    : 10for循环.py
# @Software: PyCharm
s="abcde"
l=["a","b","c","d","e"]
t=("a","b","c")
dict1={"name":"alvin","age":20}
print(s[1])
print(l[2])

for i in s:
    print(i)

for iw in l:
    print(iw)

for t1 in t:
    print(t1)

for k in dict1.keys():
    print(k)
for v in dict1.values():
    print(v)
print(type(dict1.items()))
for k,v in dict1.items():
    print(k,v)