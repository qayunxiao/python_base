# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 20:18
# @Author  : alvin
# @File    : 13字符串查找和成员运算.py
# @Software: PyCharm
s ="我做软件测试工作"
res = s.find("软件")
print(res)
if res != -1:
    print("查找到了")
else:
    print("没找到")
print("测试" in "我跟着大师学习软件测试,软件测试技术，跟我学测试")
stra="我跟着大师学习软件测试,软件测试技术，跟我学测试"
c="测1试"
def counts(c,stra):
    rawlen= len(stra)
    #替换成空
    newlen=len(stra.replace(c,""))
    counts = int((rawlen-newlen)/len(c))
    print(counts)
    return  counts

counts(c,stra)

strslit="hello world and itest and it docker django and qatest"
res1=strslit.split("and") #按and拆分
res2=strslit.split("and",1) #按and拆分1次
res3=strslit.split()#按空白字符拆分

print(res3 )

join_list=['hello', 'world', 'and', 'itest', 'and', 'it', 'docker', 'django', 'and', 'qatest']
str='and'.join(join_list)
print(str)