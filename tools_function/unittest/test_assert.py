# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 18:53
# @Author  : alvin
# @File    : test_fixture.py
# @Software: PyCharm
import  unittest

from tools.loginF import loginf


class TestLogin(unittest.TestCase):

    def test_login_userpassword_ok(self):
        print("test_login_userpassword_ok")
        self.assertEqual("登录成功",loginf("admin","password"))
    def test_login_userpassword_error(self):
        print("test_login_userpassword_error")
        self.assertEqual("登录失败",loginf("admin","password1"))
    def test_login_userpassword_error_passw(self):
        print("test_login_userpassword_error_passw")
        self.assertEqual("登录失败",loginf("admin","password"))

