# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 14:35
# @Author  : alvin
# @File    : 类的多态.py
# @Software: PyCharm
#多种形态

class Animal():
    def run(self):
        print("动物开始跑")
#子类继承父类方法继续重新run方法
class Dog(Animal):
    def run(self):
        print("dog run")
class Cat(Animal):
    def run(self):
        print("cat跑")
class People(Animal):
    def run(self):
        print("人类跑")
dog = Dog()
dog.run()
cat = Cat()
cat.run()
person = People()
person.run()
#多态性 根据传入对象不同调用不同方法
class A(Animal):
    pass
a= A()
def run(obj):
    obj.run()
run(dog)
run(cat)
run(a)