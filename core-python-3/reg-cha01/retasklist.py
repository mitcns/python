# !/usr/bin/env python
# coding=utf-8

"""处理 DOS 环境下 tasklist 命令的输出"""

import os, re

f = os.popen('tasklist /nh', 'r')

for eachLine in f:
    print re.findall(
        r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',
        eachLine.rstrip()
    )
f.close()
