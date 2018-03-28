# !/usr/bin/env python
# coding=utf-8

from atexit import register
from random import randrange
from threading import Thread, currentThread, Lock
from time import ctime, sleep
lock = Lock()

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

loops = (randrange(2, 5) for x in xrange(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(nsec):
    myName = currentThread().name
    lock.acquire()
    remaining.add(myName)
    print '[%s] Started at %s' % (myName, ctime())
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myName)
    print '[%s] Completed at %s (%d secs)' % (myName, ctime(), nsec)
    print '     remaining: %s' % (remaining or 'NONE')
    lock.release()

def main():
    for pause in loops:
        Thread(target=loop, args=(pause, )).start()

@register
def _atextit():
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
