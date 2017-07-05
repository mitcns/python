# !/usr/bin/env python
# coding=utf-8

"""随机序列迭代器"""

from random import choice

class RandSeq(object):
    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        return self

    def next(self):
        return choice(self.data)

