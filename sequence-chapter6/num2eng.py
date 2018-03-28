# !/usr/bin/env python
# coding=utf-8


def num2eng(num):
    '''将数字转化为英文表示'''
    # set a dictionary for num & English text
    n2e = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    numList = []

    for i in range(len(num)):
        numList.append(n2e[int(num[i])])

    print '-'.join(numList)


def main():
    inputNum = raw_input('请输入一个数字：')
    num2eng(inputNum)


if __name__ == "__main__":
    main()
