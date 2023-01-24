# -*- coding: utf-8 -*-
# @Time    : 2023/1/19 19:56
# @Author  : alvin
# @File    : 函数参数.py
# @Software: PyCharm

def sumdata(a,b): #形式参数
    return a+b
print(sumdata(100,200)) #实际参数

def foo2(a,b):
    print((a*3 + b*5) /23)
foo2(3,4)# 简写
foo2(a=5,b=2)#完整写法
foo2(b=2,a=5)
foo2(3,b=4) #先简写 后完整

def sumdata2(a,b):
    # return a+b,a-b,a*b,a**b #元祖
    return [a+b,a-b,a*b,a**b]#列表是一个对象，返回不需要元祖

print(sumdata2(3,6))
print(1,2,3,sep='%%')

def fun6(a,*args):
    return a,args

print(fun6(1,2,3,4,5,6))