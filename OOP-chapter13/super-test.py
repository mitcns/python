# !/usr/bin/env python
# coding=utf-8

"""super func test"""

class Base(object):
    def __init__(self):
        print 'in Base'
        print 'out Base'


class A(Base):
    def __init__(self):
        print 'in A'
        super(A, self).__init__()
        print 'out A'

class B(Base):
    def __init__(self):
        print 'in B'
        super(B, self).__init__()
        print 'out B'

class C(A, B):  # MRO 广度优先搜索
    def __init__(self):
        print 'in C'
        super(C, self).__init__()
        print 'out C'

if __name__ == "__main__":
    c = C()
