# -*- coding: utf-8 -*-
# @Time    : 2023/1/11 21:21
# @Author  : alvin
# @File    : file_renamdir.py
# @Software: PyCharm
import glob
import  shutil
import os

#目录批量修改
def update_dirname_str(path,find_str,replace_str=""):
    res = glob.glob(os.path.join(path,"*"))
    for data in  res:
        if glob.os.path.isdir(data):
            _path = glob.os.path.join(data,"*")
            #('D:\\tmp', '2332') <class 'tuple'>
            path_list = glob.os.path.split(data)
            last_dirname = path_list[-1]
            for _find_str in find_str:
                new_dirname = last_dirname.replace(_find_str,replace_str)
                if len(new_dirname) == 0:
                    print("new_dirname is zero")
                    exit(-1)
            # print(glob.os.path.join(path_list[0],new_dirname))
                new_dirpath=glob.os.path.join(path_list[0],new_dirname)
                shutil.move(data,new_dirpath)
                try:
                    update_dirname_str(_path,find_str,replace_str="")
                    #上级路径修改了，再次遍历需要使用新的路径
                    update_dirname_str(new_dirpath,find_str,replace_str="")
                except Exception as e:
                    print(e,new_dirpath,_path)
                except PermissionError:
                    continue
                except FileNotFoundError:
                    continue

        else:
            pass

# os.rename("back.log","rename.log")

if __name__ == '__main__':
    path=r"G:\IT王子\性能测试入门-jmeter工具与监控"
    find_str_list =["【更多IT教程 微信itwangzi】","更多it课程访问www.itwangzi.com","_慕课网"
                    ,"【更多教程微信：itwangzi】【更多IT教程 微信itwangzi】"
                    ,"【更多IT教程 微信itwangzi】"]
    print("关闭当前操作的文件夹: {}".format(path))
    update_dirname_str(path,find_str_list,replace_str="")
    print("批量修改文件名完成！")
