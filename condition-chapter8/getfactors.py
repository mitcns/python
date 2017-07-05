# !/usr/bin/env python
# coding=utf-8

"""求约数"""


def getFactors(num):
    # 优化循环次数
    factor = num / 2
    while factor >= 1:
        if num % factor == 0:
            yield factor
        factor -= 1
    else:
        yield num

if __name__ == "__main__":
    num = int(raw_input("请输入数字："))
    print "%d的约数:" % num,
    for i in sorted(getFactors(num)):
        print i,
