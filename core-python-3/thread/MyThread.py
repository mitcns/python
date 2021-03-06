# !/usr/bin/env python
# coding=utf-8

import threading
from time import sleep, ctime
lock = threading.Lock()
class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        # threading.Thread.__init__(self)
        super(MyThread, self).__init__()
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        lock.acquire()
        print 'starting', self.name, 'at:', ctime()
        lock.release()
        self.res = self.func(*self.args)
        print self.name, 'finished at:', ctime()
