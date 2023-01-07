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
from service.news_service import NewsService
import os
import sys
__user_server = UserService()
__news_server = NewsService()

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
                    if opt== "1":
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTBLUE_EX,"\n\t1.审批新闻")
                            print(Fore.LIGHTBLUE_EX,"\n\t2.删除新闻")
                            print(Fore.LIGHTRED_EX,"\n\tback.返回上层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号:")
                            if opt =="1":
                                page=1
                                while True:
                                    os.system("cls")
                                    count_page = __news_server.search_unreview_count_page()
                                    res = __news_server.search_unreview_list(page)
                                    for index in range(len(res)):
                                        one = res[index]
                                        print(Fore.LIGHTBLUE_EX,"\n\t%d\t%s\t%s\t%s"%(index+1,one[1],one[2],one[3]))
                                    print(Fore.LIGHTBLUE_EX,"--------------")
                                    print(Fore.LIGHTBLUE_EX,"\n\tback.返回上一层")
                                    print(Fore.LIGHTBLUE_EX,"\n\tprev. 上一页")
                                    print(Fore.LIGHTBLUE_EX,"\n\tnext. 下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号：")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page >1:
                                        page -=1
                                    elif opt == "next" and page < count_page:
                                        page +=1
                    elif opt == "back":
                        break #结束当前循环
                    elif opt== "exit":
                        sys.exit(0)
        else:
            print("\n\t登录失败(3秒自动返回)")
            time.sleep(3)
    elif opt=="2":
        sys.exit(0) #退出死循环 0是安全退出