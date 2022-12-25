# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 21:22
# @Author  : alvin
# @File    : 14函数.py
# @Software: PyCharm
def add(x,y):
    if x == 1:
        return "我们不计算简单的"
    return x+y

res= add(1,2)
print(res)
print(add(2,1))
#函数默认参数 必须放在尾部
def  calc_bmi(w,h,name="alvin老师"):
    bmi  = w / (h**2)
    return "您的，{}，bmi指数是：{}".format(name,bmi)
r= calc_bmi(75,1.85)
r2= calc_bmi(65,1.85,"小强")
print(r,r2)

#不定长参数 传入函数里面是元祖
def my_f(*param):
    # print(param)
    for i in param:
        print(i)
my_f(1,2,3)
#指定参数名称,不需要按照顺序传入参数
def  calc_bmi( h,w,name="alvin老师"):
    bmi  = w / (h**2)
    return "您的，{}，bmi指数是：{}".format(name,bmi)
r2= calc_bmi(w=65,h=1.85,name="小强")
print( r2)

#可变参数 函数接受参数之后，内部变长字典数据类型
def my_f2(**param):
    # print(param)
    for k,v in param.items():
        print(k,v)
my_f2(a=1,b=2,c=3)
my_f2(w=65,h=1.85,name="小强")

#多个返回值  返回的时候，如果接受变量为1个的时候，就把返回值变长一个元祖的数据类型
def fun1():
    i=1
    j=2
    return i,j,"qatest"
r= fun1()
print(r)

#函数递归
# def function1():
#     print("函数1运作")
#     function2()
#     return 1
# def function2():
#     print("函数2运作")
#     return 2
#
# r=function1()
# print(r)

#函数递归
def function1():
    print("函数1运作")
    return function1()
def function2():
    print("函数2运作")
    return 2
def f_dg(i):
    print("函数运行次数：{}".format(i))
    i+=1
    if i == 50:
        return 50
    return f_dg(i)
r=f_dg(1)
print(r)

def add(i):
    if i == 0:
        return 0
    return i + add(i-1)
print(add(10))
