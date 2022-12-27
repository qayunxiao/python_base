# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 17:29
# @Author  : alvin
# @File    : case2计算BMI.py
# @Software: PyCharm
weight = input("输入BMI指数计算器，请输入体重KG:")
height = input("请输入身高米:")
weight_float = float(weight)
height_float = float(height)
bmi = weight_float/(height_float*weight_float)
print("您的BMI指数",str(bmi))
if bmi < 18.5:
    print("你的体重太轻了 ，回家吃点好的")
elif bmi > 18.5 and bmi < 24:
    print("太棒了，您的bmi范围标准")
elif bmi > 24 and bmi < 28:
    print("你体重有些重，注意饮食，需要控制一下")
elif  bmi >28:
    print("超重了")