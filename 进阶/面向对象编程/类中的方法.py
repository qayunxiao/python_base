# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 13:44
# @Author  : alvin
# @File    : 类中的方法.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 13:34
# @Author  : alvin
# @File    : 类的私有属性.py
# @Software: PyCharm
class BeautifulGirl():
    #类属性
    eye = ""
    nose=""
    mouth=""
    hair=""
    # 私有属性
    __name = "alvin"

    #构造函数
    def __init__(self,eye,nose,mouth,hair,face):
        self.eye = eye
        self.nose = nose
        self.mouth= mouth
        self.hair=hair
        #实例变量
        self.face=face
        print("构造运行了")


    def get_beautiful_girl(self):
        print(self.__name)
        print(self.eye,self.face,self.hair,self.mouth)
    #类方法
    def dance(self):
        print("跳舞")
    #私有类方法
    def __dd(self):
        print("dd跳舞")
    #静态方法没参数 self,所以静态方法不能访问类属性
    @staticmethod
    def study():
        print("在学习")
    #类方法是不可以访问实例变量的，它可以访问类变量（类属性）
    @classmethod
    def girl_friend(cls):
        print(cls.__name)

#实例化是获取具体对象的过程
girl = BeautifulGirl("大大眼睛","小巧鼻子","薄薄嘴唇","乌黑头发","小脸")
# girl.dance()
# girl.get_beautiful_girl()
# print(BeautifulGirl.__dict__)
# print(girl._BeautifulGirl__dd())
print(girl.girl_friend())