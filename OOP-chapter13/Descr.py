# !/usr/bin/env python
# coding=utf-8

"""用文件系统保存一个属性内容"""

import os, pickle

class FileDescr(object):
    saved = []

    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner=None):
        if self.name not in FileDescr.saved:
            raise AttributeError, '%r used before assignment' % self.name
        try:
            f = open(self.name, 'r')
            val = pickle.load(f)
            f.close()
            return val
        except(pickle.UnpicklingError, IOError, EOFError, AttributeError, ImportError, IndexError), e:
            raise AttributeError, "could not read %r: %s" % (self.name, e)

    def __set__(self, instance, value):
        f = open(self.name, 'w')
        try:
            pickle.dump(value, f)
            FileDescr.saved.append(self.name)
        except(TypeError, pickle.PicklingError), e:
            raise AttributeError, 'could not pickle %r' % self.name
        finally:
            f.close()

    def __delete__(self, instance):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except (OSError, ValueError), e:
            pass

class MyFileVarClass(object):
    foo = FileDescr('foo')
    bar = FileDescr('bar')


class HideX(object):
    def __init__(self, x):
        self.__x = x

    @property  # TODO @property 属性函数
    def x(self):
        pass

    # @x.getter
    # def fget(self):
    #     return self.__x

    @x.setter
    def x(self, x):
        assert isinstance(x, int), '"x" must be an integer!'
        self.__x = x

    @x.getter
    def x(self):
        return self.__x

if __name__ == "__main__":
    inst = HideX(1)
    print inst.x
    inst.x = 2
    print inst.x + 1