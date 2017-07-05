# !/usr/bin/env python
# coding=utf-8

"""位操作，输入一个数字显示出两个数字间所有的整型十进制，二进制，八进制，十六进制表示，如果是可打印的 ASCII 也要把它打印出来"""


def main(startNum, endNum):
    tableHead = "十进制\t二进制\t八进制\t十六进制\t"
    tableHeadAdd = "ASCII"
    if endNum > 33:  # TODO 了解字符表示范围
        tableHead += tableHeadAdd
        print tableHead, "\n%s" % ('-' * 50)
        for item in xrange(startNum, endNum + 1):
            print "%3s\t%12s\t%5s\t%5s\t%5s" % (item, bin(item), oct(item), hex(item), chr(item))
    else:
        print tableHead, '\n%s' % ('-' * 50)
        for item in xrange(startNum, endNum + 1):
            print "%3s\t%12s\t%s5\t%5s\t" % (item, bin(item), oct(item), hex(item))

if __name__ == "__main__":
    while True:
        startNum = int(raw_input("请输入初始值 "))
        endNum = int(raw_input("请输入结束值 "))

        if startNum < endNum:
            try:
                main(startNum, endNum)
            except(EOFError, KeyboardInterrupt):
                break
        else:
            print "起始值应小于结束值"