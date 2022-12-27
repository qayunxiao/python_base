# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 8:52
# @Author  : alvin
# @File    : 字符串.py
# @Software: PyCharm
my_str="abcd1234"
#从左到右，由0开始
print(my_str[1])#b
print(my_str[-2])#3
print(my_str[len(my_str)-1])
#切片 获取字符串多个字符 字符串[start:end:step] start是开始，end是结束位置 不能取到这个位置字符
# step是等差数列的差值,所取相邻字符下标直接差值，默认是1 可以不写
my_str2="0123456789"
print(my_str2[1:5])#1234
print(my_str2[1:]) #123456789
print(my_str2[:]) #取全部0123456789
print(my_str2[::-1])#翻转

