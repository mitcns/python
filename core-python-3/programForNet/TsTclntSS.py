# !/usr/bin/env python
# coding=utf-8

"""SocketServer 类创建时间戳 TCP 客户端"""

from socket import *

HOST = 'localhost'
PORT = 22567
BUFSIZ = 2014
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    data = raw_input('请输入信息：')

    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZ)

    if not data:
        break

    print data.strip()
    tcpCliSock.close()
