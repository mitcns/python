# coding=utf-8
class FooClass(object):
    version = 0.1  # class (data) attribute

    def __init__(self, nm='小马'):
        self.name = nm
        print '为%s创建一个 class' % nm

    def show_name(self):
        print '你的名字是：%s' % self.name
        print '我的名字是：%s' % self.__class__.__name__

    def show_ver(self):
        print self.version

    @staticmethod
    def addMe2Me(x):
        return x + x


foo1 = FooClass()

foo1.show_name()

foo1.show_ver()

print foo1.addMe2Me(5)