# !/usr/bin/env python
# coding=utf-8
import math, cmath
"""safe math.sqrt() func"""

def safe_sqrt(x):
    try:
        num = math.sqrt(x)
    except ValueError:
        num = cmath.sqrt(x)
    return num

if __name__ == "__main__":
    x = float(raw_input("请输入一个任意数值："))
    print safe_sqrt(x)