# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 14:32
# @Author  : alvin
# @File    : readexcel.py
# @Software: PyCharm
import xlrd
#  (2.0.1) xlrd.biffh.XLRDError: Excel xlsx file; not supported pip install xlrd==1.2
excel = xlrd.open_workbook("study.xlsx")
print(excel)
#获取工作簿
book = excel.sheet_by_name("学生手册")
# book=excel.sheet_by_index(0)
# for i in excel.sheets():
#     print(i.name)
#获取每行数据
for i in book.get_rows():
    content = []
    for j in i:
        content.append(j.value)
    print(content)