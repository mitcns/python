# !/usr/bin/env python
# coding=utf-8

"""python2 & python3 通用版本"""

import os
from distutils.log import warn as printf
import re

with os.popen('who', 'r') as f:
    for eachLine in f:
        printf(re.split(r'\s\s+|\t', eachLine.rstrip()))
