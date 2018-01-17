'''
Usage:
    server.py
    server.py <port>

Options:
    -h --help show this

Example:
    server.py(defualt port is 10000)
    server.py <port>

'''

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# email:  iroan@qq.com
# date:   2018/1/17

from docopt import docopt
from twisted.internet import protocol,reactor
from time import ctime
import os


def use_Twisted_ex2_5(port):
    class TSServProtocol(protocol.Protocol):
        def connectionMade(self): #当一个客户端连接上该服务器程序时执行
            clnt = self.clnt = self.transport.getPeer().host
            print('---connected from:',clnt)
        def dataReceived(self, data):#当服务器接收到客户端发送的数据时执行
            self.transport.write(data)
    factory = protocol.Factory()#返回一个实例
    factory.protocol = TSServProtocol #新建的一个‘协议’
    print('waiting for connection and listen port:',port)
    reactor.listenTCP(int(port),factory)
    reactor.run()

if __name__ == '__main__':
    arguments = docopt(__doc__)
    port = arguments.get('<port>')
    if not port:
        port = 11000
    use_Twisted_ex2_5(port)