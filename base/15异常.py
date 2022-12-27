# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 14:18
# @Author  : alvin
# @File    : 15异常.py
# @Software: PyCharm

# try:
#     num = input("请输入数字:")
#     num = int(num)
#     print(num)
#     a = 10/num
# except ValueError: #只能捕获ValueError类型及其子类的异常
#     print("异常了,输入数字",ValueError)
# except ZeroDivisionError:
#     print("不能输入0",ZeroDivisionError)


try:
    num = input("请输入数字:")
    num = int(num)
    print(num)
    a = 10/num
except Exception as e:
    print("错误信息",e)
else:
    print("没发生异常我会执行")
finally:
    print("不管是否有异常都执行")