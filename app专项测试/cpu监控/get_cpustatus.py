# -*- coding: utf-8 -*-
# @Time    : 2022/12/26 9:13
# @Author  : alvin
# @File    : get_cpustatus.py
# @Software: PyCharm
import csv
import os
import time


class Controller(object):
    def __init__(self,count):
        self.counter = count
        self.alldata= [("timestamp","cpustatus")]

    def runone(self):
        print("run")
        res = os.popen("adb shell dumpsys cpuinfo | grep com.android.browser")
        cpuvalue ="0"
        for line in res.readlines():
            cpuvalue = line.split("%")[0]
        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime,cpuvalue))

    def savedata_tocsv(self):
        print("写文件")
        with open ("cpustats.csv",'wb') as f:
            writer = csv.writer(f)
            writer.writerows(self.alldata)


        #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

if __name__ == '__main__':
    controller = Controller(1)
    controller.runone()
    controller.savedata_tocsv()
