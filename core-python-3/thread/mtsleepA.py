# !/usr/bin/env python
# coding=utf-8

import thread
from time import sleep, ctime

def loop0():
    print 'loop0 开始执行时间：', ctime()
    sleep(4)
    print 'loop0 执行结束时间：', ctime()

def loop1():
    print 'loop1 开始执行时间：', ctime()
    sleep(2)
    print 'loop1 执行结束时间：', ctime()

def main():
    print '主程序开始执行时间：', ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print '执行完毕时间：', ctime()

if __name__ == '__main__':
    main()