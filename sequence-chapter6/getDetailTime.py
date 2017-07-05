# !/usr/bin/env python
# coding=utf-8

'''将用户输入的分钟数转化为小时 + 分钟'''


def getClock(minutes):
    '把分钟数转化为：小时 + 分钟'
    hours = minutes / 60
    minutes_actually = minutes % 60
    print "%d 分钟是 %d 小时 %d 分钟" % (minutes, hours, minutes_actually)

if __name__ == "__main__":
    minutes = int(raw_input("请输入分钟数："))
    getClock(minutes)
