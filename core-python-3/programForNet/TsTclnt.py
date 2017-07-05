# !/usr/bin/env python
# coding=utf-8

"""创建一个 TCP 客户端，提示用户输入发送到服务器端的笑嘻嘻，并接受从服务器端返回加了时间戳的消息"""

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('请输入要传给服务器的消息：')
    if not data:
        break

    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)

    if not data:
        break
    print data
tcpCliSock.close()
