# -*- coding: utf-8 -*-
# @Time    : 2023/1/15 16:15
# @Author  :
# @File    : image_copy.py
# @Software: PyCharm
import  shutil

for i in range(501):
    filename  = "微信图片_20230204{}.jpg".format(i)
    shutil.copyfile("test.jpg", filename)