# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 16:58
# @Author  : alvin
# @File    : test_loader.py
# @Software: PyCharm
import  unittest
#2 实例化加载对象并添加用例 unittest.TestLoader().discover('用例路径','代码文件名')
#代码文件名可以使用*（ 任意字符）通配符
# print(type(unittest.TestLoader().discover("./case","hm*.py")))
suite = unittest.TestLoader().discover("./case","hm*.py")
print("suite",suite)
#3实例化运行对象
runner = unittest.TextTestRunner()
#4执行测试
runner.run(suite)
