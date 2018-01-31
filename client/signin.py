from share.sha import getSha1
import json

class SignIn():

    def __init__(self,udp_socket,addr):
        self.udp_socket = udp_socket
        self.addr = addr

    def processSignIn(self):
        print('注册-输入:1'.center(40))
        print('登录-输入:2'.center(40))
        num = input('输入数字:')
        if num == '1':
            self.register()
        elif num == '2':
            return self.signin()
        else:
            print('输入不合法！')

    def signin(self):
        self._get_nickname_password()
        data = {'event':'signin'
                ,'nickname':self.nickname
                ,'password':self.password}
        data1 = json.dumps(data)
        self.udp_socket.sendto(data1.encode(),self.addr)
        result = self.udp_socket.recvfrom(1024)
        res = result[0].decode()
        print(res)
        if res == '登录成功':
            return True

    def register(self):
        self._get_nickname_password()
        data = {'event':'register'
                ,'nickname':self.nickname
                ,'password':self.password}
        data1 = json.dumps(data)
        self.udp_socket.sendto(data1.encode(),self.addr)
        result = self.udp_socket.recvfrom(1024)
        print(result[0].decode())
        return True

    def _get_nickname_password(self):
        self.nickname = input('请输入昵称:')
        password = self._get_password1('请输入密码: ') # TODO 优化密码输入
        self.password = getSha1(password)

    def _get_password(self,prompt): # 会以*提示输入
        pass

    def _get_password1(self,prompt): # 不提示输入个数
        import getpass
        return getpass.getpass(prompt)


    def getUserNickName(self):
        return self.nickname

from PyQt5.QtWidgets import *
class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("登录界面")
        self.resize(200,100)

        lay =QFormLayout()

        Lab1=QLabel("用户名")
        Lab2=QLabel("密码")

        Line1=QLineEdit()
        Line2=QLineEdit()
        self.Line3=QLineEdit()

        OkB=QPushButton("确定")
        CB =QPushButton("取消")

        lay.addRow(Lab1,Line1)
        lay.addRow(Lab2,Line2)
        lay.addRow(self.Line3)
        lay.addRow(OkB, CB)
        self.setLayout(lay)

        CB.clicked.connect(lambda :self.close())
        OkB.clicked.connect(lambda :self.Print())

    def Print(self):
        print('-------')
        self.Line3.setText('wkxwkx')

if __name__ == '__main__':
    # s1 = SignIn(' ')
    # s1.processSignIn()
    pass
