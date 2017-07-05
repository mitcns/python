# !/usr/bin/env python
# coding=utf-8

"""         文本处理
    要求输入一个姓名列表输入格式"Last Name, First Name"
"""


def nameTrack():
    inputNum = int(raw_input("请输入要录入的姓名数："))
    errorTimes, nameLists = 0, []
    while inputNum:
        try:
            inputNames = raw_input("输入用户名")
        except(EOFError, KeyboardInterrupt):
            break

        if len(inputNames):
            nameCell = inputNames.split(',')
            if len(nameCell) == 2:
                if 0 not in [len(x) for x in nameCell]:
                    nameLists.append(inputNames)
                    inputNum -= 1
                else:
                    print "姓或名要用不能为空"
                    errorTimes += 1
                    print "你已经输错%d次了！骚年，你瞎了吗？" % errorTimes
            else:
                print "姓和名要用逗号隔开"
                errorTimes += 1
                print "你已经输错%d次了！骚年，你瞎了吗？" % errorTimes
                #continue
    else:
        return nameLists

if __name__ == "__main__":
    while True:
        names = nameTrack()
        print "你输入的姓名列表如下（排序后）："
        for item in sorted(names):
            print item
