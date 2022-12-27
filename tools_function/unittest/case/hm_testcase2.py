# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 15:29
# @Author  : alvin
# @File    : TestCase01.py
# @Software: PyCharm
#导包
import  unittest
#自定义测试类 需继承unittest的模块TestCase类
class testDemo2(unittest.TestCase):
    #书写测试方法 必须test开头，建议test_
    def test_method01(self):
        print("hm ceshi 2-1")
    def test_method02(self):
        print("hm ceshi 2-2")
# 测试执行
#光标放在类名后面
#光标放方法名后面