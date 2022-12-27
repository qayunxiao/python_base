# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 16:00
# @Author  : alvin
# @File    : TestSuite_Runner.py
# @Software: PyCharm
from tools_function.unittest.case.TestCase01 import testDemo1
from tools_function.unittest.case.TestCase02 import testDemo2
testDemo2
#1、导包
import unittest
#2、实例化套件对象
suite = unittest.TestSuite()
#3、使用套件对象添加用例方法
#方式1 套件对象.addTest(测试类名('方法名'))，复制类名，使用自动导包
suite.addTest(testDemo1('test_method01'))
suite.addTest(testDemo2('test_method01'))
#4、实例化运行对象
runner = unittest.TextTestRunner()
#5、运行套件对象
runner.run(suite)
