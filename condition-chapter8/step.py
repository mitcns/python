# !/usr/bin/env/ python
# coding=utf-8

"""步长模拟函数"""


def getList():
    startNum = int(raw_input("输入初始值："))
    endNum = int(raw_input("输入结束值："))
    stepNum = int(raw_input("输入步长："))

    aList = range(startNum, endNum, stepNum)
    aList.append(endNum)

    return aList


def likeRange():
    startNum = int(raw_input("输入初始值："))
    endNum = int(raw_input("输入结束值："))
    stepNum = int(raw_input("输入步长："))

    while startNum <= endNum:
        yield startNum
        startNum += stepNum

if __name__ == "__main__":
    # for i in getList():
       # print i
    for i in likeRange():
        print i
