# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 17:01
# @Author  : alvin
# @File    : case1计算身高体重.py
# @Software: PyCharm
#孩子的身高=父母身高之和* 0.54
fa_height = input("请输入父亲身高 :")
print("父亲身高:",fa_height)
ma_height = input("请输母亲身高 :")
print("请输母亲身高:",ma_height)
child_height = (float(fa_height)+float(ma_height))* 0.54
print("孩子的身高:",child_height)