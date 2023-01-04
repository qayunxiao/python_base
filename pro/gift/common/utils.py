# -*- coding: utf-8 -*-
# @Time    : 2023/1/3 19:51
# @Author  : alvin
# @File    : utils.py
# @Software: PyCharm
import os
import time

from common.myerror import NotFileError, FormatError, NotPathError

def check_file(path):
    print("path",path)
    if not os.path.exists( path ):
        raise NotPathError( 'NOT Found :{}'.format( path ) )
    if not path.endswith( '.json' ):
        raise FormatError( "need json format" )
    if not os.path.isfile( path ):
        raise NotFileError()


def timestamp_to_string(timestamp):
    time_obj = time.localtime( timestamp )
    time_str = time.strftime( "%Y-%m-%d %H:%M:%S", time_obj )
    return time_str


if __name__ == '__main__':
    s = timestamp_to_string( time.time() )
    print( s )
