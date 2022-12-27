# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 18:53
# @Author  : alvin
# @File    : test_fixture.py
# @Software: PyCharm
import  unittest

class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        print("输入网址...")
    def tearDown(self) -> None:
        print("关闭当前页面...")
    @classmethod
    def setUpClass(cls) -> None:
        print("1打开浏览器...")
    @classmethod
    def tearDownClass(cls) -> None:
        print("5关闭览器...")
    def test_1(self):
        print("输入正确测试用例")
    def test_2(self):
        print("输入错误测试用例")

