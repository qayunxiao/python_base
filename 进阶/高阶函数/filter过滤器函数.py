# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 11:27
# @Author  : alvin
# @File    : filter过滤器函数.py
# @Software: PyCharm
letter =["a","B","c","D","e","F"]
upper_letter = filter(lambda x:x == x.upper(),letter)
print(upper_letter)
print(list(upper_letter))
student_name = ['李元芳',"李建国","忘事实"]
stre1=" ss"
a=stre1.lstrip()
print(a)
print(list (filter(lambda  x:x.startswith("李"),student_name)) )

res = filter(lambda x:x>1,[0,1,2] )