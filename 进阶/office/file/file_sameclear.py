# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 9:55
# @Author  : alvin
# @File    : file_sameclear.py
# @Software: PyCharm
import  glob

data = {}
def clear(path):
    res = glob.glob(path)
    for _data in res:
        if glob.os.path.isdir(_data):
            _path= glob.os.path.join(_data,"*")
            clear(_path)
        else:
            name = glob.os.path.split(_data)[-1]
            if "zip" in name:
                continue
            f = open(_data,'r',encoding="utf8")
            content = f.read()
            if name in data:
                sub_data = data[name]
                for k,v in sub_data.ites():
                    if v== content:
                        glob.os.remove(_data)
                        print("will delete {}".format(_data))
                        is_delete = True
            if _content_dict == content:
                    glob.os.remove(_data)
            else:
                data[name] = content

if __name__ == '__main__':
    path = glob.os.path.join(glob.os.getcwd(),"*")
    clear(path)