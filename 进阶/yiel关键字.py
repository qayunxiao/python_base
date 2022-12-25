# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 10:43
# @Author  : alvin
# @File    : yiel关键字.py
# @Software: PyCharm

#yiel返回是生成器对象
def func1():
    return "自信的生命最美丽"
    print("含泪播种的人必须能含笑收获")

# r1 = func1()
# print(r1)

def func2():
    # print("勤于反省，才有不断进步的可能")
    # yield返回的是一个生产器对象
    yield "一个人，想要优秀，你必须要敢于挑战"
    # print("有志者事竟成，苦心人天不负")
    yield "第二个yield"
    # print("第二个yield后边的print")
r2 = func2()
print(r2)
# r2.__next__()
# r2.__next__()
# r2.__next__()

# 生成器对象可以使用for循环来进行迭代
# for i in r2:
#     print(i)

count = 1
for i in r2:
    # 这里打印的i是生成器对象yield后边的那个返回值
    print(i)
    count += 1
    print("for循环调用生成器的{}打印".format(count))
    print("*"*20)


