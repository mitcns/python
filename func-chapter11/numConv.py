# !/usr/bin/env python
# coding=utf-8

"""用传入的转换函数简单地将一个序列的数转化为相同的类型"""

def convert(func, seq):
    'conv. sequence of numbers to same type'
    return [func(eachNum) for eachNum in seq]

mySeq = (123, 45.67, -6.2e8, 999999999L)

print convert(int, mySeq)
print convert(long, mySeq)
print convert(float, mySeq)