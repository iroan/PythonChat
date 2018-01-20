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
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from time import ctime
import os

class UDPProtocol(DatagramProtocol):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port

    def startProtocol(self):
        self.transport.connect(self.ip,int(self.port))
        self.sendDatagram(b'this is test by wkx')

    def sendDatagram(self,string):
        if len(string):
            self.transport.write(string)
        else:
            reactor.stop()

    def datagramReceived(self, datagram, addr):
        print('Datagram recived:',datagram)
def main(ip, port):
    reactor.listenUDP(0,UDPProtocol(ip,port))
    reactor.run()

if __name__ == '__main__':
    arguments = docopt(__doc__)
    port = arguments.get('<port>')
    ip = arguments.get('<ip>')
    if not port:
        port = '11000'
    if not ip:
        ip = '127.0.0.1'
    main(ip, int(port))
