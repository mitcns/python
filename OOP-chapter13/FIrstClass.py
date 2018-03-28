# !/usr/bin/env python
# coding=utf-8

"""创建一个类！"""

class AddrBookEntry(object):  # 类定义
    'address book entry class'

    def __init__(self, nm, ph):  # 定义构造器
        self.name = nm
        self.phone = ph
        print 'Created instance for:', self.name

    def updatePhone(self, newph):
        self.phone = newph
        print 'Update phone# for:', self.name

# 创建子类
class EmplAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry class'  # 员工地址簿

    def __init__(self, nm, ph, userId, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = userId
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print 'Update e-mail address for:', self.name

# 创建带引用计数的 class
class InstTrack(object):
    ''
    count = 0  # count 是一个类属性

    def __init__(self):  # 增加 count
        InstTrack.count += 1

    def __del__(self):  # 减少 count
        InstTrack.count -= 1

    @staticmethod  # 引入 staticmethod 装饰器
    def howMany():  # 返回 count
        return InstTrack.count


class TestStaticMethod:
    @staticmethod
    def foo():
        print 'calling static method foo()'


class TestClassMethod:
    @classmethod
    def foo(cls):
        print 'calling class method foo()'
        print 'foo() is part of class:', cls.__name__