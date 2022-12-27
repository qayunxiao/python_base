# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 21:34
# @Author  : alvin
# @File    : html_testrunnerReport.py
# @Software: PyCharm
import  unittest
import os
from HtmlTestRunner3 import HTMLTestRunner

path=os.path.join(os.path.dirname(os.getcwd()),'case')
print(path)
suite = unittest.TestLoader().discover(path,"hm*.py")

HTMLTestRunner()
file="report.html"
with open (file,'wb',) as f:
    runner = HTMLTestRunner(f)
#运行套件
    runner.run(suite)