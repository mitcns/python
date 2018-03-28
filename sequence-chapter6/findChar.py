# !/usr/bin/env python
# coding=utf-8

'''字符串查找、替换'''

string_check = {
    'string': "请输入原始字符串:\n",
    'origchar': "请输入要查找的字符串:\n",
    'newchar': "请输入要替换的新文本:\n"
}


def findchr(string, char):
    if char in string:
        len_chr = len(char)
        len_str = len(string)
        for i in range(len_str - len_chr + 1):
            if string[i : i + len_chr] == char:
                return i
            #break
    else:
        return -1


def rfindchr(string, char):
    if char in string:
        len_chr = len(char)
        len_str = len(string)
        for i in range(len_str - len_chr + 1):
            if i == 0:
                str = string[(-i - len_chr) : ]
            else:
                str = string[(-i - len_chr) : -i]
            if str == char:
                return len_str - i - len_chr
            #break

    else:
        return -1


def subchr(string, origchar, newchar):
    if origchar in string:
        return string.replace(origchar, newchar)

CMDs = {
    'l': findchr,
    'r': rfindchr,
    'v': subchr
}
options = "lrvq"


def main():
    pr = """
    左查找(L)
    右查找(R)
    替换(V)
    退出(Q)
    键入你的选择："""
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except(EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print '\n 你选择了： %s' % choice

            if choice not in options:
                print '无效的选项，请重重新输入！'
            else:
                break
        if choice == 'q':
            break
        elif choice == 'v':
            print CMDs[choice](raw_input(string_check['string']), raw_input(string_check['origchar']), raw_input(string_check['newchar']))
        else:
            print CMDs[choice](raw_input(string_check['string']), raw_input(string_check['origchar']))

if __name__ == "__main__":
    main()
