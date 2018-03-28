# !/usr/bin/env python
# coding=utf-8

"""使用 Twisted创建一个获取时间戳消息的 TCP 客户端"""
from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 23567

class TSClntProtocol(protocol.Protocol):

    def sendData(self):

        data = raw_input('请输入消息：')
        if data:
            print '...sending %s...' % data
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):

        self.sendData()

    def dataReceived(self, data):
        print data
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
