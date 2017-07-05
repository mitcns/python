# !/usr/bin/env python
# coding=utf-8

"""中级定制，数值定制"""

class Time60(object):
    'Time60 - track hours and minutes'

    def __init__(self, hr, minute):
        'Time60 constructor - takes hours & minutes'
        self.hr = hr
        self.min = minute

    def __str__(self):
        'Time60 - string representation'
        return '%d:%d' % (self.hr, self.minute)

    __repr__ = __str__

    def __add__(self, other):
        'Time60 - overloading the addition operator'
        return self.__class__(self.hr + other.hr, self.minute + other.minute)

    def __iadd__(self, other):
        'Time60 - overloading in-place addition'
        self.hr += other.hr
        self.minute += other.minute

