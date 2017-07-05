# !/usr/bin/env python
# coding=utf-8

"""包装文件对象类"""

class CapOpen(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    __repr__ = __str__

    def write(self, line):
        self.file.write(line.upper())

    def __getattr__(self, attr):
        return getattr(self.file, attr)

if __name__ == '__main__':
    f = CapOpen('test.txt', 'w')
    f.write("mazhanchuan\n")
    f.write("Python\n")
    f.write("xuexizhong!")
    f.close()
    g = open('test.txt')
    for item in g:
        print item,
    g.close()
