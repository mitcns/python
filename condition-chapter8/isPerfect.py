# !/usr/bin/env/ python
# coding=utf-8

"""完全数"""


def isPerfect(num):
    aList = []
    for i in xrange(1, num):
        if num % i == 0:
            aList.append(i)
    else:
        if sum(aList) == num:
            return True
        else:
            return False

if __name__ == "__main__":
    while True:
        num = int(raw_input("请输入数值："))
        try:
            if isPerfect(num):
                print "%d是一个完全数！" % num
            else:
                print "渣渣，你输入的是个什么玩意儿！"
        except(EOFError, KeyboardInterrupt):
            break
