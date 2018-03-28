# !/usr/bin/env python
# coding=utf-8

"""float 函数对于参数要求十分严格，在此模拟一个'安全方式'来忽略错误，让解释器继续执行！"""


def safe_float(obj):
    try:
        retval = float(obj)
    except (ValueError, TypeError), e:
        retval = e
    return retval

print safe_float('12.34')
print safe_float("bad idea")
print safe_float({'a': 1})