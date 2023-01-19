# -*- coding: utf-8 -*-
# @Time    : 2023/1/15 16:15
# @Author  : alvin
# @File    : image_copy.py
# @Software: PyCharm
import  shutil

for i in range(1001):
    filename  = "微信图片_20232023{}.jpg".format(i)
    shutil.copyfile("微信图片_20230115162821.jpg", filename)