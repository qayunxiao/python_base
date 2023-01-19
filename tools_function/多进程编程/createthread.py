# -*- coding: utf-8 -*-
# @Time    : 2023/1/2 21:15
# @Author  : alvin
# @File    : createthread.py
# @Software: PyCharm
import random
import threading
import time

lists=[
    'python','django','torndao','flask',
    'bs5','request','uvloop'
]
new_lsits=[]

def work():
    if len(lists) == 0:
        return
    data = random.choice(lists)
    lists.remove(data)
    new_data = '{}_new'.format(data)
    new_lsits.append(new_data)
    time.sleep(1)

if __name__ == '__main__':
    start = time.time()
    print("old list len",len(lists))
    t_list=[]
    for i in range(len(lists)):
        t = threading.Thread(target=work)
        t_list.append(t)
        t.start()
        # work()
    for t in t_list:
        t.join()
    print("old list",lists)
    print("new list",new_lsits)
    print("new list len",len(new_lsits))
    print("time is {}".format((time.time()-start)))

