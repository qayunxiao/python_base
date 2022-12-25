# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 20:18
# @Author  : alvin
# @File    : 13字符串查找和成员运算.py
# @Software: PyCharm
s ="我做软件测试工作"
res = s.find("软件")
print(res)
if res != -1:
    print("查找到了")
else:
    print("没找到")
print("测试" in "我跟着大师学习软件测试")