from share.sha import getSha1
import json
from socket import *
from share.share import server_addr,packSendData
from PyQt5.QtWidgets import *

class SignIn(QWidget):
    def __del__(self):
        packSendData(self.udp_socket,server_addr,{'event': 'offline', 'nickname': self.own_nickname})
        pass

    def __init__(self):
        super().__init__()
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.udp_socket.connect(server_addr)

        self.setWindowTitle("登录界面")
        self.resize(200,100)

        lay =QGridLayout()

        Lab1=QLabel("用户名:")
        Lab2=QLabel("密 码:")

        self.Line1=QLineEdit()
        self.Line2=QLineEdit()
        self.Line3=QLineEdit()

        btn_confirm=QPushButton("&F确定")
        btn_register=QPushButton("&R注册")
        btn_cancel =QPushButton("&C取消")

        lay.addWidget(Lab1,0,0,1,1)
        lay.addWidget(self.Line1,0,1,1,2)
        lay.addWidget(Lab2,1,0,1,1)
        lay.addWidget(self.Line2,1,1,1,2)
        lay.addWidget(btn_confirm,2,0,1,1)
        lay.addWidget(btn_register,2,1,1,1)
        lay.addWidget(btn_cancel,2,2,1,1)
        self.setLayout(lay)

        btn_cancel.clicked.connect(lambda :self.close())
        btn_confirm.clicked.connect(lambda :self.onLogin())
        btn_register.clicked.connect(lambda :self.onRegister())

    def onLogin(self):
        self.getNickName_Password()
        data = {'event':'signin'
                ,'nickname':self.nickname
                ,'password':self.password}
        data1 = json.dumps(data)
        self.udp_socket.sendto(data1.encode(),server_addr)
        result = self.udp_socket.recvfrom(1024)
        res = result[0].decode()
        print(res)
        if res == '登录成功':
            from client.main_gui import Main
            self.main_gui = Main(self.udp_socket,self.nickname)
            self.main_gui.show()
            self.hide()
            # pass

    # TODO 登录界面刚开始只显示登录按钮，若发现为注册，再显示登录按钮
    # 注册之后要提醒登录
    def onRegister(self):
        self.getNickName_Password()
        data = {'event':'register'
                ,'nickname':self.nickname
                ,'password':self.password}
        data1 = json.dumps(data)
        print('in onRegister')
        self.udp_socket.sendto(data1.encode(),server_addr)
        result = self.udp_socket.recvfrom(1024)
        print('in onRegister1')
        print(result[0].decode())

    def getNickName_Password(self):
        self.nickname = self.Line1.text()
        self.password = getSha1(self.Line2.text())

if __name__ == '__main__':
    SignIn()
    pass
