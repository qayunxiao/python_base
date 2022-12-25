# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 20:34
# @Author  : alvin
# @File    : 高级数据类型-列表.py
# @Software: PyCharm
list1=["e","d"]
my_list = [list1,1,2,3,"a","b",{"name":"age"},("qabc")]
print(my_list[2])#2
#区间
print(my_list[2:4])#[2, 3]
# print(my_list)
# print(my_list[0][0])
# print(my_list[2])
k=-1
for i in my_list:
    k+=1
    if  isinstance(i,list):
        print("这个{}值是list,位置是{}".format(i,k))

mylist1=[0,1,2,3,4,5,6,7,8,9]
mylist1.append(10)
mylist1.remove(3)
print(mylist1)
mylist1.pop(6)
mylist1[5]='b'
print(mylist1)

