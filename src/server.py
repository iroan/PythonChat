'''
本文档概念性名词注释：
client用户：连接上server的普通client
client管理员：连接上server的具有特殊权限的client
worker类：
    client worker指管理client业务逻辑的一个类
    server worker指管理server业务逻辑的一个类
'''

from com import share
from com.log import logger_server
from socket import socket,AF_INET,SOCK_DGRAM
import json
from threading import Thread
class Main:
    def __init__(self):
        self.udp_sock = socket(AF_INET, SOCK_DGRAM)
        self.udp_sock.bind(('', share.server_addr[1]))
        while True:
            try:
                self.recv_date,self.client_addr = self.udp_sock.recvfrom(1024)
                thread = Thread(target=self.work)
                thread.start()
                thread.join()
            except ConnectionRefusedError as e:
                logger_server.error('ser.py:26' + str(e))

    def work(self):
        data = json.loads(self.recv_date)
        logger_server.debug('ser.py:30' + str(data))
        from ser.worker import Worker
        Worker(self.udp_sock,data,self.client_addr).processMessage()

if __name__ == '__main__':
    Main()