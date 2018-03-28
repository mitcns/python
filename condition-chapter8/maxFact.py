# !/usr/bin/env python
# coding=utf-8


def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print '%d 的最大公约数是 %d' % (num,  count), False
            break
        count -= 1
    else:
        print num, "是一个素数！", True

for eachNum in range(10, 21):
    showMaxFactor(eachNum)


