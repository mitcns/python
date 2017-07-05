# !/usr/bin/env python
# coding=utf-8

"""调用 who 命令，然后通过不同类型的空白符分隔输入的数据解析输入"""

import os, re

f = os.popen('who', 'r')
for eachLine in f:
    print re.split(r'\s\s+|\t', eachLine.rstrip())

f.close()