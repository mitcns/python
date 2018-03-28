# !/usr/bin/env python
# coding=utf-8

"""safe open fun"""

def open_safe(fileName, mode="r"):
    try:
        f = open(fileName, mode)
    except IOError, e:
        return None
    else:
        return f