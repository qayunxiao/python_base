# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 19:26
# @Author  : alvin
# @File    : case3计算器.py
# @Software: PyCharm

number_times = 1
result =0
while True:
    if number_times == 1:
        f_number=int(input("输入第1个数:"))
        operator=(input("输入操作:"))
        if operator == "q":
            print("退出程序")
            break
        elif operator == "c":
            print("清零")
            number_times = 1
            result = 0
        s_number=(input("输入下个数字:"))
        result = float(result)
        s_number = float(s_number)
        if operator == "+":
            result = f_number+s_number
        elif operator == "-":
            result = f_number-s_number
        elif operator == "*":
            result = f_number*s_number
        elif operator == "/":
            result = f_number/s_number
        else:
            print("不知道操作")
        print("计算的结果",result)
        number_times +=1
    else:
        operator=(input("输入操作:"))
        print("result",result)
        if operator == "q":
            print("退出程序")
            break
        elif operator == "c":
            print("清零")
            number_times = 1
            result = 0
            continue
        s_number=(input("输入第二个数:"))
        result = float(result)
        s_number = float(s_number)
        if operator == "+":
            result +=s_number
        elif operator == "-":
            result -=s_number
        elif operator == "*":
            result *=s_number
        elif operator == "/":
            result /=s_number
        else:
            print("不知道操作")
        print("计算的结果",result)
        print("当前运算次数:"+str(number_times))
        number_times +=1
