# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 9:44
# @Author  : alvin
# @File    : app.py
# @Software: PyCharm
import time

from colorama import  Fore,Style
#密码加星
from getpass import  getpass
from service.user_server import UserService
import os
import sys
__user_server = UserService()

while True:
    # 清空控制台
    os.system("cls")
    print(Fore.LIGHTBLUE_EX,"\n\t========================")
    print(Fore.LIGHTBLUE_EX,"\n\t欢迎使用新闻管理系统")
    print(Fore.LIGHTBLUE_EX,"\n\t========================")
    print(Fore.LIGHTBLUE_EX,"\n\t1.登录系统")
    print(Fore.LIGHTBLUE_EX,"\n\t2.退出系统")
    print(Style.RESET_ALL)# 重置颜色
    opt = input("\n\t输入操作编号:")
    if opt == "1":
        username = input("\n\t用户名:")
        password = input("\n\t密 码:")
        res= __user_server.login(username,password)
        if res == True:
            role=__user_server.search_user_role(username)
            os.system("cls")
            while True:
                if role == "新闻编辑":
                    print("tes")
                elif role == "管理员":
                    print(Fore.LIGHTBLUE_EX,"\n\t1.新闻管理")
                    print(Fore.LIGHTBLUE_EX,"\n\t2.用户管理")
                    print(Fore.LIGHTRED_EX,"\n\tback.退出登录")
                    print(Fore.LIGHTRED_EX,"\n\texit.退出系统")
                    print(Style.RESET_ALL)# 重置颜色
                    opt = input("\n\t输入操作编号:")
                    if opt == "back":
                        break #结束当前循环
                    elif opt== "exit":
                        sys.exit(0)
        else:
            print("\n\t登录失败(3秒自动返回)")
            time.sleep(3)
    elif opt=="2":
        sys.exit(0) #退出死循环 0是安全退出