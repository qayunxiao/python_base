# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 13:19
# @Author  : alvin
# @File    : 对象的封装.py
# @Software: PyCharm
#类名称 ：多个单词组成 每个首字母大写
class BeautifulGirl():
    #类属性
    eye = ""
    nose=""
    mouth=""
    hair=""
    face=""
    #构造函数
    def __init__(self,eye,nose,mouth,hair,face):
        self.eye = eye
        self.nose = nose
        self.mouth= mouth
        self.hair=hair
        self.face=face
        print("构造运行了")
    #类方法
    def dance(self):
        print("跳舞")
    def get_beautiful_girl(self):
        print("外貌")
        print(self.eye,self.face,self.hair,self.mouth)

#实例化是获取具体对象的过程
girl = BeautifulGirl("大大眼睛","小巧鼻子","薄薄嘴唇","乌黑头发","小脸")
girl.dance()
girl.get_beautiful_girl()
girl2 = BeautifulGirl("小小眼睛","小巧鼻子","薄薄嘴唇","乌黑头发","小脸")
girl2.get_beautiful_girl()