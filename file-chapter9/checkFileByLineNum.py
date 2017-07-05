# !/usr/bin/env python
# coding=utf-8

"""文件访问，输入数字 N 和文件 F ，然后显示文件 F 的前 N 行"""

num = int(raw_input("请输入要显示的行数："))
fileName = raw_input("请输入要显示的文件名：")

f = open(fileName, "r")


# line = (line.strip() for line in f)
while num:
    for eachLine in f:
        print eachLine,
        num -= 1
    else:
        f.close()
        break
