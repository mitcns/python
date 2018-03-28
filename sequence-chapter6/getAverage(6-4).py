# !/usr/bin/env python
# coding=utf-8

#import math
import string
'''输入测试成绩，获取平均分'''
textScore = []

letters = string.letters


def inputScore():
    score = raw_input("请输入测试成绩：").strip()
    return score


def getAverage(list):
    return round(sum(list)/len(list), 2)


def main():
    while True:
        try:
            getInput = inputScore()
            for item in getInput:
                if item in letters:
                    print "测试成绩不能输入字母！"
                    main()
            textScore.append(float(getInput))
            average_num = getAverage(textScore)
        except(EOFError, KeyboardInterrupt, IndexError):
            break
        print average_num

if __name__ == '__main__':
    main()
