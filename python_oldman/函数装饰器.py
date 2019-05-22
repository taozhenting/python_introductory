#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('运行时间是%s' %(stop_time - start_time))
    return wrapper

@timmer  #test=timmer(test)
def test():
    time.sleep(3)
    print('test函数运行完毕')

test()