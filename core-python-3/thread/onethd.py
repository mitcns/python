# !/usr/bin/env python
# coding=utf-8

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
    loop0()
    loop1()
    print '执行完毕时间：', ctime()

if __name__ == '__main__':
    main()