# -*- coding: utf-8 -*-
# @Time    : 2023/1/2 11:22
# @Author  : alvin
# @File    : function02.py
# @Software: PyCharm

class Test(object):
    a=1
    b=2
    def __init__(self):
        self.a = self.a
        self.b = self.b

test=Test()
res= vars(test)
print(res)
print(test.a)
print(hasattr(test,'a'))
print(hasattr(list,'append'))

setattr(test,'c',3)
print(test.c)
print(vars(test))
# print(setattr(list,'appends'))

a=['',None,True,0]
print(any(a))