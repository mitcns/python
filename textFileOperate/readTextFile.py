# coding=utf-8
# !/usr/bin/env python

'readTextFile.py -- read & display text file'

# get filename
fname = raw_input('请输入要查看的文件名：')
print

# attempt to open file for reading
try:
    fobj = open(fname, "r")
except IOError, e:
    print "*** file open error:", e
else:
    # display contents to the screen
    for eachLine in fobj:
        print eachLine,
    fobj.close()