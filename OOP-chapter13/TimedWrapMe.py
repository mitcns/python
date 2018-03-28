# !/usr/bin/env python
# coding=utf-8

"""包装标准类型"""

from time import time, ctime

class TimedWrapMe(object):

    def __init__(self, obj):
        self.__data = obj
        self.__ctime = self.__mtime = self.__atime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def getTimeVal(self, t_type):
        if not isinstance(t_type, str) or t_type[0] not in 'cma':
            raise TypeError, "argument of 'c', 'm, or 'a' req'd"
        return getattr(self, '_%s__%stime' % (self.__class__.__name__, t_type[0]))

    def getTimeStr(self, t_type):
        return ctime(self.getTimeVal(t_type))

    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def __repr__(self):
        self.__atime = time()
        return str(self.__data)

    __str__ = __repr__
    # def __str__(self):
    #     self.__atime = time()
    #     return str(self.__data)

    def __getattr__(self, attr):  # attr 不是 built-in 方法 TODO 可有可无 ？
        self.__atime = time()
        return getattr(self.__data, attr)

if __name__ == "__main__":
    newTime = TimedWrapMe(1182)
    print newTime
    print newTime.getTimeStr('a')
    newTime
    print newTime.getTimeStr('a')
    print newTime.get()
    print newTime.set(123), newTime.getTimeStr('a')
    print newTime.get() + 2