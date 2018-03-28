# !/usr/bin/env python
# coding=utf-8

queue = []
options = 'devq'


def enQ():
    queue.append(raw_input(' 输入一个新字符串： ').strip())


def deQ():
    if len(queue) == 0:
        print '空队列不能执行 pop 操作'
    else:
        print '删除 ', `queue.pop(0)`


def viewQ():
    print queue  # calls str() internally


CMDs = {
    'e': enQ,
    'd': deQ,
    'v': viewQ
}


def showmenu():
    pr = """
        队列新增(E)
        队列删除(D)
        查看队列(V)
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
        CMDs[choice]()


if __name__ == '__main__':
    showmenu()
