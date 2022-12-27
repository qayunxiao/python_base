# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 13:33
# @Author  : alvin
# @File    : 读文件.py
# @Software: PyCharm
f=open("write.txt",'r',encoding='utf-8')
buf=f.read()
print(buf)
f.close()