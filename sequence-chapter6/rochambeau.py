# !/usr/bin/env python
# coding=utf-8

'''石头剪刀布
    rules：
      a.the paper covers the rock,
      b.the rock breaks the scissors,
      c.the scissors cut the paper.
'''

import random

rochdic = {
    'r': 0,
    'p': 1,
    's': 2
}

computer_choice = {
    0: '石头',
    1: '布',
    2: '剪刀'
}

man_choice = {
    'r': '石头',
    'p': '布',
    's': '剪刀'
}


def rochambeau():
    pr = """\
    键入你的选择
    R 代表 石头
    P 代表 布
    S 代表 剪刀\n"""

    while True:
        u_choice = raw_input(pr).strip()[0].lower()
        c_choice = random.randrange(3)

        result = rochdic[u_choice] - c_choice
        print "你出了%s 电脑出了%s" % (man_choice[u_choice], computer_choice[c_choice]),
        if result == 0:
            print "平局！"
        elif result == -1 or result == 2:
            print "你输了"
        else:
            print "你赢了"

if __name__ == "__main__":
    rochambeau()
