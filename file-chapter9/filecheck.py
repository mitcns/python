# !/usr/bin/env python
# coding=utf-8

"""文件过滤，忽略 注释"""

fileName = raw_input("请输入文件名：")

f = open(fileName, "r")

# for eachLine in (line.strip() for line in f):
for eachLine in f:
    line = eachLine.strip()
    # if eachLine and eachLine[0] == '#':
    if line.startswith('#'):
        continue
    elif '#' in line:
        loc = line.find("#")
        print line[:loc]
    else:
        print line
f.close()
