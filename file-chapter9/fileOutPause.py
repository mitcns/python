# !/usr/bin/env python
# coding=utf-8
# import os
"""逐页显示文本文件， 25行，暂停一下，然后继续执行！"""

fileName = raw_input("请输入要查看的文件名：")

f = open(fileName)

flag = True

while flag:
    print "当前页内容是："
    i = 0

    while i < 25:
        eachLine = f.readline()
        if eachLine:
            print eachLine
            i += 1
        else:
            print "文件内容已显示完全！"
            flag = False
            break
    else:
        print "当前页面显示完全"

    if flag:
        continueKey = raw_input("按任意键继续").lower()
        if continueKey == 'q':
            break
    else:
        break

f.close()
# n = 0
# for eachLine in f:
#     print eachLine,
#     n += 1
#     if n == 25:
#         n = 0
#         os.system('stop') TODO set correct command