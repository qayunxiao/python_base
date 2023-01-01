# -*- coding: utf-8 -*-
# @Time    : 2023/1/1 15:38
# @Author  : alvin
# @File    : package_open.py
# @Software: PyCharm
import  os

def create_package(path):
    if os.path.exists(path):
        raise  Exception('{}已经存在 不可以创建',path)
    os.makedirs(path)
    init_path = os.path.join(path,'__init_.py')
    f = open(init_path,'w')
    f.write("'#coding:utf-8'\n")
    f.close()

class Opens(object):
    def __init__(self,path,mode='w',is_return =True):
        self.path =path
        self.mode = mode
        self.is_return = is_return
    def writer(self,message):
        f = open(self.path,mode=self.mode)
        if self.is_return:
            message = '{}\n'.format(message)
        f.write(message)
        f.close()
    def read(self,is_strip=True):
        res=[]
        with open(self.path,mode=self.mode) as f:
            data = f.readlines()
        for line in data:
            if is_strip == True:
                temp = line.split()
                if temp != "":
                    res.append(temp)
            else:
                if line != '':
                    res.append(line)
        return res


if __name__ == '__main__':
    current_path = os.getcwd()
    print("current:",current_path)
    # path = os.path.join(current_path,'test1')
    # print("path",path)
    # create_package(path)
    open_path = os.path.join(current_path,'b.text')
    o = Opens(open_path,mode='r')
    # o.writer('你好 alvin')
    data =o.read(is_strip=False)
    print(data)