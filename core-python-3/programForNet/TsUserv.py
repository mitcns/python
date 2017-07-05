# !/usr/bin/env python
# coding=utf-8

"""创建一个 UDP 服务器，接收客户端信息，并返回加了时间戳的信息"""

from socket import *
from time import ctime

HOST = ''
PORT = 21578
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
    print '...received from & returned to: ', addr

udpSerSock.close()
