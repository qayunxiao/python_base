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
mylist3=[0,1,2,3,4,5,6,7,8,9,20,10,11]
# print(mylist3[::-1])
# print(mylist3.reverse())
list4=mylist3[:]
list5=mylist3.copy()
print(list4,list5)
mylist3.sort()
print(mylist3)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20]
person_info=[["张三","18","测试"],["李四","19","开发"]]
print(len(person_info),person_info[0])
print(person_info[0].append("男"))
person_info[0][1]="20"
print(person_info)
mylist4=[0,1,2,3,4,5,6,7,8,9,20,10,11,2,4]
set(mylist4)
#set 集合，不能有重复数据，有的话自动去重
print(list(set(mylist4)))
new_l=[]
for i in mylist4:
    if i not in  new_l:
        new_l.append(i)

print(new_l)