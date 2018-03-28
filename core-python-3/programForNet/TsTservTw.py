# !/usr/bin/env python
# coding=utf-8

"""使用 Twisted Inernet 类创建一个时间戳 TCP 服务器"""

from twisted.internet import protocol, reactor
from time import ctime

PORT = 23567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connected from: ', clnt

    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServProtocol

print 'waiting for connection...'

reactor.listenTCP(PORT, factory)
reactor.run()
