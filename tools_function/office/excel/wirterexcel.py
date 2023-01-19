# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 14:54
# @Author  : alvin
# @File    : wirterexcel.py
# @Software: PyCharm
import xlsxwriter
import xlrd
excel = xlsxwriter.Workbook( "writedata.xlsx" )
book = excel.add_worksheet("alvin")
title = ["姓名","性别","年龄","成绩","等级"]
for index ,data in enumerate(title):
    #0行，列，内容
    book.write(0,index,data)
excel.close()

def read():
    excel = xlrd.open_workbook( "study.xlsx" )
    book = excel.sheet_by_index(0)
    res = []
    for i in book.get_rows():
        content=[]
        for  j in i:
            content.append(j.value)
        res.append(content)
    return res


def write(content):
    print("content",content)
    excel = xlsxwriter.Workbook( "writedata.xlsx" )
    book = excel.add_worksheet("alvin")
    for index,data in enumerate(content):
        # print(data)
        for sub_index,sub_data in enumerate(data):
            print(sub_index,sub_data)
            book.write(index,sub_index,sub_data)
    excel.close()

if __name__ == '__main__':
    res = read()
    # print(res)
    write(res)