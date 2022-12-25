# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 14:04
# @Author  : alvin
# @File    : 类的继承.py
# @Software: PyCharm
class Fa(object):
    age ="34"
    def __init__(self,name):
        self.name = name
        print("父类构造函数运行了")
    def fa_money(self):
        print("爸爸有很多钱")
    def __fa_knowleger(self):
        print("爸爸的知识")
    def face(self):
        print("爸爸长的帅！")
    @staticmethod
    def study():
        print("爸爸在学习")
    @classmethod
    def fa_friend(cls):
        print("爸爸有很多朋友")
class Mo():
    def face(self):
        print("妈妈长的漂亮")

class Son(Fa):
    def __init__(self):
        print("子类的构造函数运行了")

# son = Son("小王")
#继承中 子类有构造函数 那么不会调用父类的构造函数
son =Son()

son.fa_money()
# son.__fa_knowleger()

class Son2(Fa,Mo):
    def __init__(self):
        print("二儿子改造函数运行了")

son2=Son2()
son2.face()#爸爸长的帅！

#当多继承 多个父类有同一个名称变量或方法，就近原则 写在最前面先继承