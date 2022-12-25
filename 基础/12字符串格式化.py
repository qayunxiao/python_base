# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 20:10
# @Author  : alvin
# @File    : 12字符串格式化.py
# @Software: PyCharm
content = "软件测试"
ds=20
s= "我来学习%s," %content + "我学习了%d" % ds +"小时"
print(s)
#%s 字符串 %d 是整数 %f浮点类型
r = "我跟着{},学习{},学费大概{:.2f}元".format("alvin","软件测试",1988.9233)
print(r)