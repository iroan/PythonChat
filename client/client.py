# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# email:  iroan@qq.com 
# date:   2018/1/17

'''
Usage:
    client.py
    client.py <ip> <port>

Options:
    -h --help show this

Example:
    client.py(defualt ip is 127.0.0.1 and port is 10000)
    client.py <ip> <port>
'''

from docopt import docopt
from twisted.internet import protocol,reactor
from time import ctime
import os

def Twisted(ip, port):
    from twisted.internet import protocol,reactor
    class TSClntProtocol(protocol.Protocol):
        def sendData(self):
            data = input('>>>')
            if data:
                self.transport.write(data.encode())
            else:
                self.transport.lostConnection()
        def connectionMade(self):
            self.sendData()
        def dataReceived(self,data):
            print(data.decode())
            self.sendData()
    class TSClntFactory(protocol.ClientFactory):
        protocol = TSClntProtocol
        clientConnectionLost = clientConnectionFailed =lambda self,connector,reason:reactor.stop()
    reactor.connectTCP(ip, port, TSClntFactory())
    reactor.run()

if __name__ == '__main__':
    arguments = docopt(__doc__)
    port = arguments.get('<port>')
    ip = arguments.get('<ip>')
    if not port:
        port = '11000'
    if not ip:
        ip = '127.0.0.1'
    Twisted(ip,int(port))
