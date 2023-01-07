# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 20:48
# @Author  : alvin
# @File    : file_test.py
# @Software: PyCharm
#py3.8包
from shutil import  copy
from shutil import copyfile
from shutil import  move,make_archive,unpack_archive
import os
print(os.path.dirname(os.getcwd()))
src_file  = os.path.join(os.path.dirname(os.getcwd()),"filecopytree.text")
tar_file = os.path.join(os.path.dirname(os.getcwd()),"copy")
# copy(src_file,tar_file)
tar_copyfile = os.path.join(os.path.dirname(os.getcwd()),"copy","copyfile.text")
tar_movefile = os.path.join( os.path.dirname(os.getcwd()),"file", "move.text" )
# copyfile(src_file,tar_copyfile)
# move("copyfile.text",tar_movefile)
# move("move.text","ename.text")
#删除
# os.remove("remove.text")
#压缩文件
make_archive('tar_file','zip',tar_file)
#解压缩
tar_unpack_archive = os.path.join(os.path.dirname(os.getcwd()),"file")
# unpack_archive("tar_file.zip",tar_unpack_archive)