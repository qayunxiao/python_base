# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 10:22
# @Author  : alvin
# @File    : ArrayADI.py
# @Software: PyCharm

class Array(object):
    def __init__(self,size=32):
        self.size = size
        self.items = [None] * size

    def __getitem__(self, index):
        return self.items[index]
    def __setitem__(self, index, value):
        self.items[index] = value
    def __len__(self):
        return self.size
    def clear(self,value=None):
        for i in range(len(self.items)):
            self.items= value
    def __iter__(self):
        for item in self.items:
            yield item

arr = Array(3)
arr[0]=1
arr.__setitem__(2,"alvin")
arr[2]=3

print(arr[2])