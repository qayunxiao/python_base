# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 19:40
# @Author  : alvin
# @File    : parameterized_demo.py
# @Software: PyCharm

import  unittest
from parameterized import  parameterized
from tools.loginF import loginf
#组织测试数据 [(),(),()] ，传参使用装饰器,数据和参数保持一致
data=[
    ("admin","password","登录成功"),
    ("admin","password1","登录失败"),
    ("admin1","password","登录失败")
]
class TestLogin(unittest.TestCase):
    @parameterized.expand(data)
    def test_login(self,username,passowrd,expect):
        self.assertEqual(expect,loginf(username,passowrd))