# !/usr/bin/env python
# coding=utf-8

"""创建一个 UDP 客户端，向服务端发送信息，并接收服务器返回带有时间戳的信息"""

from socket import *

HOST = 'localhost'
PORT = 21578
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('请输入要发送的消息：')

    if not data:
        break

    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)

    if not data:
        break

    print data

udpCliSock.close()
