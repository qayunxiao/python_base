# -*- coding: utf-8 -*-
# @Time    : 2023/2/16 10:02
# @Author  : alvin
# @File    : renamefile.py
# @Software: PyCharm
import csv
from chardet.universaldetector import UniversalDetector
import pandas as pd
import csv
#chardet获取编码
# with open("./rename.csv",encoding="utf-8") as f:
#     for row in csv.reader(f,skipinitialspace=True):
#         print(row)
def read_csvfile(file):
    df = pd.read_csv(file,encoding="utf-8")
    return df

def read_file(file):
    '读取文件二进制内容'
    with open(file,'rb') as f:
        return f.read()

def get_encode_info(file):
    with open(file,'rb') as f:
        detector = UniversalDetector()
        for line in f.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result['encoding']

def convert_encode(file,original_encode,des_ecode='utf-8'):
    '默认转utf-8'
    file_content = read_file(file)
    file_decode = file_content.decode(original_encode,'ignore')
    file_encode = file_decode.encode(des_ecode)
    print(file_decode,file_encode)
    with open(file,'wb') as f:
        f.write(file_encode)


if __name__ == '__main__':
    res = get_encode_info("./rename.csv")
    print(res)
    # convert_encode("./rename.csv",res)
    csv = read_csvfile("./rename.csv")
    print(csv)