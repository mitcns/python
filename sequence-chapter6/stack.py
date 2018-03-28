# !/usr/bin/env python
# coding=utf-8

stack = []


def pushit():
    stack.append(raw_input(' 输入一个新的字符串： ').strip())


def popit():
    if len(stack) == 0:
        print '不能从空堆栈做 pop 操作'
    else:
        print '删除了 ', `stack.pop()`


def viewstack():
    print stack  # calls str() internally


CMDs = {'u': pushit, 'o': popit, 'v': viewstack}


def showmenu():
    pr = """
        p(U)sh
        p(O)p
        (V)iew
        (Q)uit

        enter choice: """

    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print '\n你选择了：%s' % choice
            if choice not in 'uovq':
                print '无效的选项，请重试！'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()


if __name__ == '__main__':
    showmenu()
