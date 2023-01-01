# -*- coding: utf-8 -*-
# @Time    : 2023/1/1 15:25
# @Author  : alvin
# @File    : fiecrate.py
# @Software: PyCharm
mess = "python很有意思"
mess_i = mess.encode("utf-8")
print(mess_i)
# with open ( "filecreate.text", "wb" ) as f:
#     f.write(mess_i)

# with open ( "filecreate2.text", "w" ) as f2:
#     f2.write('1\n')
#     f2.write("2\n")

list2=["今天天气还好\n","今天去接哥哥了\n","python简单\n"]
with open("filecreate3.text","w",encoding="utf-8") as f3:
    f3.writelines(list2)