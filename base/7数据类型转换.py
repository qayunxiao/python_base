# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 16:42
# @Author  : alvin
# @File    : 7数据类型转换.py
# @Software: PyCharm
# 查看数据类型
a=3
print(type(a))
# 整数转浮点
a2=float(a)
print(type(a2))
# 整数转字符串
a3=str(a)
print(type(a3))
# 整数转布尔类型
a4=bool(a)
print(type(a4),a4)

b=1.3
b1= int(b)
print(type(b1),b1)
b2= str(b)
print(type(b2),b2)
b3= bool(b)
print(type(b3),b3)
c="1.3"
c1=int(c)
print("c1",c1,type(c1))