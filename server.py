'''
本文档概念性名词注释：
client用户：连接上server的普通client
client管理员：连接上server的具有特殊权限的client
worker类：
    client worker指管理client业务逻辑的一个类
    server worker指管理server业务逻辑的一个类
'''

from socket import *
from share import share
import json

def Main():
    udp_sock = socket(AF_INET,SOCK_DGRAM)
    udp_sock.bind(('',share.server_addr[1]))

    while True:
        recv_date,client_addr = udp_sock.recvfrom(1024)
        data = json.loads(recv_date)
        print('date from client=',data)
        from server.worker import Worker
        Worker(udp_sock,data,client_addr).processMessage()

if __name__ == '__main__':
    Main()
