from threading import Thread
from share.share import global_1field_order,server_addr
import json

class Worker:
    def __del__(self):
        self.sendData({'event':'offline'
                       ,'nickname':self.own_nickname})

    def __init__(self,udp_socket,own_nickname):
        self.udp_socket = udp_socket
        self.own_nickname = own_nickname
        self.peer_nickname = ''
        self.prompt = '没有活动>>>'

    def processRecv(self):
        while True:
            self.server_data,useless_addr = self.udp_socket.recvfrom(1024)
            print('data_from_server=',self.server_data)
            print(self.prompt, end='')

    def process(self):
        thread_recv = Thread(target=self.processRecv)
        thread_send = Thread(target=self.processInput)

        thread_send.start()
        thread_recv.start()

        thread_send.join()
        exit(0)
        thread_recv.join()

    def processInput(self):
        print(self.prompt,end='')
        while True:
            input_data = input() # TODO 需要自定义发送消息的数据结构
            self.anaylseInput(input_data)

    def anaylseInput(self,input_data):
        available_data = self.getAvailableField(input_data)

        '''查看在线用户'''
        '''一个命令的操作通常是：1.需要从服务器获取信息
                             2.另外一种情况是执行本地操作
            只要在global_1field_order中，说明这个命令有效，就可以发送带server
            至于具体命令是什么，由服务器判断'''
        if available_data == 'q':
            print('exit')
            exit(0)

        if len(available_data) == 1 and available_data[0] in global_1field_order:
            self.sendData({'event':available_data[0]})


    def getAvailableField(self,input_data):
        '''
        处理步骤
            1. 分割字符串
            2. 去掉统计''的个数
            3. 删除''n次
        '''
        d1 = input_data.split(' ')
        for i in range(d1.count('')):
            d1.remove('')
        return d1

    def sendData(self,data_sendto_server):
        '''
        主要数据:
            1. 发送方nickname
            2. 接受方nickname
            3. event
            4. message
        '''
        send_data = json.dumps(data_sendto_server)
        self.udp_socket.sendto(send_data.encode(), server_addr)

from PyQt5.QtWidgets import *

class Worker_GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("登录界面")
        self.resize(200,100)

        lay =QFormLayout()

        Lab1=QLabel("用户名")
        Lab2=QLabel("密码")

        self.Line1=QLineEdit()
        self.Line2=QLineEdit()
        self.Line3=QLineEdit()

        OkB=QPushButton("确定")
        CB =QPushButton("取消")

        lay.addRow(Lab1,self.Line1)
        lay.addRow(Lab2,self.Line2)
        lay.addRow(OkB, CB)
        self.setLayout(lay)

        CB.clicked.connect(lambda :self.close())
        OkB.clicked.connect(lambda :self.onLogin())

if __name__ == '__main__':
    # import asyncio
    # import threading
    # data = ''
    # async def hello():
    #     data = await input('in hello>>')
    #
    # async def world():
    #     print('in hello,data = ',data)
    #
    # loop = asyncio.get_event_loop()
    # task =[hello(),world()]
    # loop.run_until_complete(asyncio.wait(task))
    # loop.close()

    pass
'''
编程总结：
1. 若现在主程序中实现同时响应输入和输出，响应开启3个线程，即：主线程、输入线程、输出线程

私聊
组聊
查看在线用户
'''
