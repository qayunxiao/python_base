# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 13:36
# @Author  : alvin
# @File    : withopen.py
# @Software: PyCharm

with open("write.txt",'a.text',encoding='utf-8') as f:
    f.write("\n")
    f.write("withopen ")