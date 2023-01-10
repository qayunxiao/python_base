# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 20:48
# @Author  : alvin
# @File    : file_test.py
# @Software: PyCharm
#py3.8包
from glob import glob
from shutil import copy, rmtree
from shutil import copyfile
from shutil import  move,make_archive,unpack_archive
from shutil import  copytree
import os
print(os.path.dirname(os.getcwd()))
src_file  = os.path.join(os.path.dirname(os.getcwd()),"filecopytree.text")
tar_file = os.path.join(os.path.dirname(os.getcwd()),"copy")
# copy(src_file,tar_file)
tar_copyfile = os.path.join(os.path.dirname(os.getcwd()),"copy","copyfile.text")
tar_movefile = os.path.join(os.path.dirname(os.getcwd()),"myfile","move.text")
# copyfile(src_file,tar_copyfile)
#相同路径下属于重命名
# move("copyfile.text",tar_movefile)
# move("move.text","ename.text")
# move("test2","testqa/test3/test4")
# move("testqa/test3/test4","test2")

#删除
# os.remove("remove.text")
#压缩文件
print(os.path.join(os.path.dirname(os.getcwd()),"myfile"))
# make_archive('tar_file','zip',os.path.join(os.path.dirname(os.getcwd()),"myfile"))
#解压缩
tar_unpack_archive = os.path.join(os.path.dirname(os.getcwd()),"tar_file")
# unpack_archive("tar_file.zip",tar_unpack_archive)
#目标文件夹不能存 否则报错
# copytree("test1",os.path.join(os.path.dirname(os.getcwd()),"copytree"))
#copy1必须存在
# rmtree(os.path.join(os.path.dirname(os.getcwd()),"copy1"))
targets=os.path.join(os.path.dirname(os.getcwd()),"myfile")
res = glob(targets+'/*.py')
print("res",res,targets)