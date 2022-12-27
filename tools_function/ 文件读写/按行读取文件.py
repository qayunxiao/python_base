# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 13:39
# @Author  : alvin
# @File    : 按行读取文件.py
# @Software: PyCharm
# with open("write.txt","r",encoding="utf-8") as f:
#     buf = f.readline()
#     print(buf)

# with open("write.txt","r",encoding="utf-8") as fr:
#     for i in fr:
#         print(i,end='')

# with open("write.txt","r",encoding="utf-8") as fr:
#     while True:
#         buf = fr.readline()
#         if len(buf) == 0:
#             break
#         else:
#             print(buf,end='')
with open("write.txt","r",encoding="utf-8") as fr:
    while True:
        buf = fr.readline()
        if buf :
            print(buf,end='')
        else:
            break