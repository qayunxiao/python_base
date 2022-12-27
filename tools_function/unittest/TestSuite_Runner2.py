# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 16:00
# @Author  : alvin
# @File    : TestSuite_Runner.py
# @Software: PyCharm

#1、导包
import  unittest
#2、实例化套件对象
from tools_function.unittest.case.TestCase01 import testDemo1

suite = unittest.TestSuite()
#3、使用套件对象添加用例方法
suite.addTest(unittest.makeSuite(testDemo1))
#方式2 一个测试类的所有方法添加
#4、实例化运行对象
runer = unittest.TextTestRunner()
#5、运行套件对象
runer.run(suite)