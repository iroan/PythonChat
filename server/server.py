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
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from time import ctime
import os


class UDPProtocol(DatagramProtocol):
    def datagramReceived(self, datagram, addr):
        self.transport.write(datagram,addr)

def main(port):
    print('waiting for connection and listen port:',port)
    reactor.listenUDP(int(port),UDPProtocol())
    reactor.run()

if __name__ == '__main__':
    arguments = docopt(__doc__)
    port = arguments.get('<port>')
    if not port:
        port = 11000
    main(port)