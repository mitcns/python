# !/usr/bin/env python
# coding=utf-8

"""统计文件总行数"""

fileName = raw_input("请输入要打开的文件名：")

f = open(fileName, "r")

lineNum = len([line for line in f])
f.close()
print lineNum
