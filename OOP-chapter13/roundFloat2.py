# !/usr/bin/env python
# coding=utf-8

"""简单定制，float"""

class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), "Value must be a float!"
        self.value = round(val, 2)

    def __str__(self):
        return '%.2f' % self.value

    __repr__ = __str__

if __name__ == "__main__":
    rfm = RoundFloatManual(5.699)
    print rfm
