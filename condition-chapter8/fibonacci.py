# !/usr/bin/env python
# coding=utf-8

"""斐波那契数列"""


def fibonacci(num):
    fibList = [1, 1]
    for i in xrange(2, num):
        fibList.append(fibList[i - 2] + fibList[i - 1])
    else:
        return fibList


if __name__ == "__main__":
    while True:
        num = int(raw_input("你想查看斐波那契数列的第几位的值？"))
        try:
            print "斐波那契数列中位于第 %d 的是 %d" % (num, fibonacci(num)[-1])
        except(EOFError, KeyboardInterrupt):
            break
