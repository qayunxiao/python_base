# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 9:34
# @Author  : alvin
# @File    : file_contensfind.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2023/1/8 9:13
# @Author  : alvin
# @File    : file_findfie.py
# @Software: PyCharm
import glob
path=glob.os.path.join(glob.os.getcwd(),"*")
final_res=[]
#target 文件名。path查找路径
def search(path,target):
    res=glob.glob(path)
    #data 路径
    for data in res:
        #文件夹
        if glob.os.path.isdir(data):
            _path=glob.os.path.join(data,"*")
            # print("{} is filepath".format(data))
            search(_path,target)
        #文件
        else:
            f = open(data,'r',encoding='utf-8')
            try:
                content= f.read()
                if target in content:
                    final_res.append(data)
            except:
                print("data is not readonly")
                continue
            finally:
                f.close()
            f.close()
    return final_res

if __name__ == '__main__':
    print("path",path)
    res=search(path,target="alvin")
    print(res)