# !/usr/bin/env python
# coding=utf-8

"""multiple types set class"""

class NumStr(object):
    ''

    def __init__(self, num=0, string=''):
        self.num = num
        self.string = string

    def __str__(self):
        return '[%d :: %r]' % (self.num, self.string)

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, NumStr):
            return self.__class__(self.num + other.num, self.string + other.string)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'

    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(self.num * num, self.string * num)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'

    def __nonzero__(self):
        return self.num or len(self.string)

    # TODO 可以声明为静态方法
    def __norm_cval(self, cmpres):
        return cmp(cmpres, 0)

    def __cmp__(self, other):
        return self.__norm_cval(cmp(self.num, other.num)) + self.__norm_cval(cmp(self.string, other.string))

if __name__ == "__main__":
    a = NumStr(3, 'ma')
    b = NumStr(1, 'liu')
    c = NumStr(2, 'teng')
    d = NumStr()
    e = NumStr(string='ye')
    f = NumStr(1)
    print a, b, c, d, e, f
    print a < b, b < c, a == a
    print b * 2, a * 4, a + b + c
    print cmp(a, b), cmp(a, c), cmp(a, a)
    print isinstance(a, NumStr), a.__class__, a.__str__, a  # 方法重写了
