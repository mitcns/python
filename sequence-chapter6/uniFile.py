# coding=utf-8
# !/usr/bin/env python
'''
    An example of reading & writing Unicode strings: Writes
    a Unicode string to afile in utf-8 & reads it back in.
'''

CODEC = 'utf-8'
FILE = 'unicode.txt'

helloOut = u"你好，小马！\n"
bytesOut = helloOut.encode(CODEC)
f = open(FILE, "w")
f.write(bytesOut)
f.close()

f = open(FILE, 'r')
bytesIn = f.read()
f.close()
helloIn = bytesIn.decode(CODEC)

print helloIn,
