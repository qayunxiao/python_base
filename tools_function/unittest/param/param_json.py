# -*- coding: utf-8 -*-
# @Time    : 2022/12/27 20:04
# @Author  : alvin
# @File    : param_json.py
# @Software: PyCharm

import unittest
import json

from nose_parameterized import parameterized

from tools.loginF import loginf

#组织数据 读取json文件
def get_test_data(filepath):
    with open(filepath,"r",encoding="utf-8") as f:
        #读取数据流，转化json格式文件，如果是read返回是str
        res=json.load(f)
        res_list=[]
        for logindata in res:
            #取到字典的值 转换元组之后添加res_list 形成[(),()]格式
            res_list.append(tuple(logindata.values()))
            # res_list.append((logindata['desc'],logindata['username'],logindata['password'],logindata['expect']) )
            # print("logindata",logindata['desc'],logindata['username'],logindata['password'],logindata['expect'])
        return res_list
version=30
class Test_param_json(unittest.TestCase):
    filepath="parameterized.json"
    @parameterized.expand(get_test_data(filepath))
    def test_login(self,desc,username,password,expect):
        print("desc",desc)
        print("username:",username,"password:",password,"expect:",expect)
        self.assertEqual(expect,loginf(username,password))
    @unittest.skip("不想测试")
    def test_login2(self,desc,username,password,expect):
        print("desc",desc)
        print("username:",username,"password:",password,"expect:",expect)
        self.assertEqual(expect,loginf(username,password))

    @unittest.skipIf(version >=30,"版本大于30")
    def test_login3(self,desc,username,password,expect):
        print("desc",desc)
        print("username:",username,"password:",password,"expect:",expect)
        self.assertEqual(expect,loginf(username,password))

# if __name__ == '__main__':
#     filepath="./parameterized.json"
#     get_test_data(filepath)