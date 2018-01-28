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

'''
本文档概念性名词注释：
client用户：连接上server的普通client
client管理员：连接上server的具有特殊权限的client
worker类：
    client worker指管理client业务逻辑的一个类
    server worker指管理server业务逻辑的一个类
'''

# from docopt import docopt
from socket import *
from threading import Thread
from share import share
import json

def Main():
    udp_sock = socket(AF_INET,SOCK_DGRAM)
    udp_sock.bind(('',share.addr[1]))
    while True:
        recv_date,client_addr = udp_sock.recvfrom(1024)
        print('recv_date=',recv_date)
        data = json.loads(recv_date)
        from server.worker import Worker
        work = Worker(udp_sock,data,client_addr)

def User():
    pass # TODO 实现server转发client用户通讯消息

if __name__ == '__main__':
    Main()
    # from db import MySqlHelper
    # mysqlhelper = MySqlHelper('iroan','iroanMYS47','ssltools')
    # res = mysqlhelper.read_all('select * from user_test')
    # print(res)
    pass