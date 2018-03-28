# !/usr/bin/env python
# coding=utf-8
"""该脚本使用了锁和信号量来模拟一个糖果机"""

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import ctime, sleep

lock = Lock()
MAX = 5
candyTray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print 'Refilling candy...',
    try:
        candyTray.release()
    except ValueError:
        print 'full, skipping'
    else:
        print 'OK'
    lock.release()

def buy():
    lock.acquire()
    print 'Buying candy...',
    if candyTray.acquire(False):
        print 'OK', ctime()
    else:
        print 'empty, skipping'
    lock.release()

def producer(loops):
    for i in xrange(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in xrange(loops):
        buy()
        sleep(randrange(3))

def main():
    print 'candy store open at:', ctime()
    nloops = randrange(2, 6)
    print 'THE CANDY MACHINE (full with {0} bars)!'.format(MAX)
    Thread(target=consumer, args=(randrange(nloops, nloops + MAX + 2),)).start()
    Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
