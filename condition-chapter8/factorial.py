# !/usr/bin/env/ python
# coding=utf-8

"""阶乘"""


def factorial(num):
    startNum = 1
    for i in xrange(1, num + 1):
        startNum *= i
    else:
        return startNum

if __name__ == "__main__":
    while True:
        num = int(raw_input("请输入阶乘整数："))
        try:
            print "%d! == %d" % (num, factorial(num))
        except(EOFError, KeyboardInterrupt):
            break
