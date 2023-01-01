# -*- coding: utf-8 -*-
# @Time    : 2023/1/1 15:51
# @Author  : alvin
# @File    : file_read.py
# @Software: PyCharm
import  os
file_path = os.getcwd()#当前目录
file_before = os.path.dirname(os.getcwd() )#当前上一层目录
# print(file_path,file_before)
file_name =os.path.join(file_before,"unittest","TestSuite_Runner.py")
with open(file_name,'r',encoding='utf8') as f :
    # data=f.read()
    # data = f.readlines()#列表数据类型，for去遍历
    data = f.readline()
    print(data)
    data = f.readline()
    print(data)

# print(data)
# print(type(data))
# for i in data:
#     print(i)
