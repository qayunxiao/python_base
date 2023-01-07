# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 20:48
# @Author  : alvin
# @File    : file_test.py
# @Software: PyCharm
#py3.8包
from shutil import  copy
from shutil import copyfile
import os
print(os.path.dirname(os.getcwd()))
src_file  = os.path.join(os.path.dirname(os.getcwd()),"file.text")
tar_file = os.path.join(os.path.dirname(os.getcwd()),"copy")
# copy(src_file,tar_file)
tar_copyfile = os.path.join(os.path.dirname(os.getcwd()),"copy","copyfile.text")

copyfile(src_file,tar_copyfile)