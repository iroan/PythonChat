from share.sha import getSha1
import json
from socket import *
from share.share import server_addr
from PyQt5.QtWidgets import *

class SignIn_GUI(QWidget):
    def __del__(self):
        self.udp_socket.close()

    def __init__(self):
        super().__init__()
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.udp_socket.connect(server_addr)

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
            from client.main import MainGUI
            self.main_gui = MainGUI(self.udp_socket)
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
        self.udp_socket.sendto(data1.encode(),self.addr)
        result = self.udp_socket.recvfrom(1024)
        print(result[0].decode())

    def getNickName_Password(self):
        self.nickname = self.Line1.text()
        self.password = getSha1(self.Line2.text())

if __name__ == '__main__':
    pass
