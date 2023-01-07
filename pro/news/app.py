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
from service.role_service import RoleService
import os
import sys
__user_server = UserService()
__news_server = NewsService()
__role_server = RoleService()

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
            while True:
                os.system("cls")
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
                                    print(Fore.LIGHTBLUE_EX,"\n\t%d:::%d"%(page,count_page))
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
                                    elif int(opt) >=1 and int(opt) <=10:
                                        news_id = res[int(opt) -1][0]
                                        __news_server.update_unreview_news(news_id)
                            elif opt =="2":
                                page=1
                                while True:
                                    os.system("cls")
                                    count_page = __news_server.search_count()
                                    res = __news_server.search_list(page)
                                    for index in range(len(res)):
                                        one = res[index]
                                        print(Fore.LIGHTBLUE_EX,"\n\t%d\t%s\t%s\t%s"%(index+1,one[1],one[2],one[3]))
                                    print(Fore.LIGHTBLUE_EX,"--------------")
                                    print(Fore.LIGHTBLUE_EX,"\n\t%d:::%d"%(page,count_page))
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
                                    elif int(opt) >=1 and int(opt) <=10:
                                        news_id = res[int(opt) -1][0]
                                        __news_server.delete_by_id(news_id)
                            elif opt == "back":
                                break
                    elif opt == "2":
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTBLUE_EX,"\n\t1.添加用户")
                            print(Fore.LIGHTBLUE_EX,"\n\t2.修改用户")
                            print(Fore.LIGHTBLUE_EX,"\n\t3.删除用户")
                            print(Fore.LIGHTRED_EX,"\n\tback.返回上层")
                            opt = input("\n\t输入操作:")
                            if opt == "back":
                                break
                            elif opt=="1":
                                os.system("cls")
                                username = input("用户名:")
                                password = input("密 码:")
                                re_password = input("重复密码:")
                                if  password != re_password:
                                    print("\n\t 两次密码不一致(3秒自动返回)")
                                    time.sleep(3)
                                    continue
                                email = input("邮箱地址:")
                                res_role = __role_server.search_list()
                                for index in range(len(res_role)):
                                    one = res_role[index]
                                    print(Fore.LIGHTBLUE_EX,"\n\t%d.%s"%(index,one[1]))
                                print(Style.RESET_ALL)
                                opt = input("\n\t角色编号:")
                                role_id = res_role[int(opt)-1][0]
                                print("role_Id",role_id)
                                __user_server.insert_user(username,password,email,role_id)
                                print("\n\t 保存成功！(3秒自动返回)")
                            elif opt=="2":
                                page=1
                                while True:
                                    os.system("cls")
                                    count_page = __user_server.search_user_count()
                                    res = __user_server.search_user_list(page)
                                    # print("search_user_list res----",len(res),res)
                                    for index in range(len(res)):
                                        one = res[index]
                                        # print("search_user_list one----",one,index+1,one[0],one[1],one[2])
                                        print(Fore.LIGHTBLUE_EX,"\n\t%d\t%s\t%s"%(index+1,one[1],one[2]))
                                    print(Fore.LIGHTBLUE_EX,"--------------")
                                    print(Fore.LIGHTBLUE_EX,"\n\t%d:::%d"%(page,count_page))
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
                                    elif int(opt) >=1 and int(opt) <=10:
                                        os.system("cls")
                                        user_id = res[int(opt)-1][0]
                                        username = input("\n\t新的用户名：")
                                        password = input("\n\t新的密码：")
                                        re_password = input("\n\t再次输入密码：")
                                        if password != re_password:
                                            print("\n\t 两次密码不一致(3秒自动返回)")
                                            time.sleep(3)
                                            break
                                        email = input("\n\t邮箱地址:")
                                        res_role = __role_server.search_list()
                                        for index in range(len(res_role)):
                                            one = res_role[index]
                                            print(Fore.LIGHTBLUE_EX,"\n\t%d.%s"%(index,one[1]))
                                        print(Style.RESET_ALL)
                                        opt = input("\n\t角色编号:")
                                        role_id = res_role[int(opt)-1][0]
                                        opt=input("\n\t是否保存(Y/N)")
                                        if opt == "Y" or opt =="y":
                                            __user_server.update(user_id,username,password,email,role_id)
                                            print("\n\t 修改成功(3秒自动返回)")
                                            time.sleep(3)
                                            break
                            elif opt=="3":
                                page=1
                                while True:
                                    os.system("cls")
                                    count_page = __user_server.search_user_count()
                                    res = __user_server.search_user_list(page)
                                    # print("search_user_list res----",len(res),res)
                                    for index in range(len(res)):
                                        one = res[index]
                                        # print("search_user_list one----",one,index+1,one[0],one[1],one[2])
                                        print(Fore.LIGHTBLUE_EX,"\n\t%d\t%s\t%s"%(index+1,one[1],one[2]))
                                    print(Fore.LIGHTBLUE_EX,"--------------")
                                    print(Fore.LIGHTBLUE_EX,"\n\t%d:::%d"%(page,count_page))
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
                                    elif int(opt) >=1 and int(opt) <=10:
                                        os.system("cls")
                                        user_id = res[int(opt)-1][0]
                                        __user_server.delete_by_id(user_id)
                                        print("\n\t 删除成功(3秒自动返回)")
                                        time.sleep(3)

                    elif opt == "back":
                        break #结束当前循环
                    elif opt== "exit":
                        sys.exit(0)
        else:
            print("\n\t登录失败(3秒自动返回)")
            time.sleep(3)
    elif opt=="2":
        sys.exit(0) #退出死循环 0是安全退出