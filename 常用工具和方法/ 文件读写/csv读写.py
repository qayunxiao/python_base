# -*- coding: utf-8 -*-
# @Time    : 2022/12/26 14:41
# @Author  : alvin
# @File    : csv读写.py
# @Software: PyCharm
import  csv

class csv_action():
    def __init__(self):
        self.file_name = "qtest.csv"
        self.Dictfile_name = "qtestDict.csv"

    def csv_wirter_file(self):
        with open(self.file_name,'w',newline='') as csvfile:
            csvwirter = csv.writer(csvfile)
            csvwirter.writerow(['hello world', 'web site', 'www.biancheng.net'])
            csvwirter.writerows([('hello','world'), ('I','love','you')])

    def csv_Dwirter_file(self):
        with open(self.Dictfile_name,"w",newline='') as csv_f:
            #表字段名
            fieldnames = ['first_name', 'last_name']
            writer=csv.DictWriter(csv_f,fieldnames=fieldnames)
            writer.writeheader()#写表头
            # 多行写入
            writer.writerows([{'first_name': 'Baked', 'last_name': 'Beans'},{'first_name': 'Lovely', 'last_name': 'Spam'}])
            # 单行写入
            writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    def csv_reader_file(self):
        with open(self.file_name,'r',newline='') as csvf:
            reader = csv.reader(csvf)
            print("csv_reader_file reader",type(reader))
            for row in reader:
                print( "csv_reader_file row",row,type(row))
                print(','.join(row))

    def csv_Dictreader_file(self):
        with open(self.Dictfile_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print("csv_Dictreader_file reader",type(reader))
            for row in reader:
                print( "csv_Dictreader_file row",row,type(row))
                print(row['first_name'], row['last_name'])


if __name__ == '__main__':
    action = csv_action()
    action.csv_wirter_file()
    action.csv_reader_file()
    action.csv_Dwirter_file()
    action.csv_Dictreader_file()