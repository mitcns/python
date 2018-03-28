# !/usr/bin/env python
# coding=utf-8

"""创建一个 TCP 服务器，接收来自客户端消息，加时间戳并发送给客户端"""

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from: ', addr
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        # print data
        if not data:
            break
        print data
        tcpCliSock.send('[%s] %s' % (ctime(), data))
        # print tcpSerSock.recv()
    tcpCliSock.close()
tcpSerSock.close()
