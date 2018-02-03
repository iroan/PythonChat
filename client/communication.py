import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
from socket import *
from share.share import server_addr,sendData

class CommWidget(QWidget):
    '''
    功能：
        1. 提供私聊、组聊GUI
        2. 检测发送消息的事件
        3. 处理、显示从服务器接收到的信息
    '''
    def __init__(self,udp_socket,own_nickname,peer_nickname,parent = None):
        super(CommWidget,self).__init__(parent)
        self.udp_socket = udp_socket
        self.peer_nickname = peer_nickname
        self.own_nickname = own_nickname
        self.setWindowTitle('与-'+ peer_nickname + '-对话')
        self._gui()

    def _gui(self):
        self.history_text = QTextEdit()
        self.input_text = QTextEdit()
        history_label = QLabel('历史记录:')
        input_label = QLabel('输入消息:')
        btn_quit = QPushButton('&Q退出')
        btn_send = QPushButton('&S发送')

        self.vlay = QVBoxLayout()
        self.vlay.addWidget(history_label)
        self.vlay.addWidget(self.history_text)
        self.vlay.addWidget(input_label)
        self.vlay.addWidget(self.input_text)
        self.vlay.addWidget(btn_quit)
        self.vlay.addWidget(btn_send)

        btn_quit.clicked.connect(self.close)
        btn_send.clicked.connect(self.sendMessage)

        self.setLayout(self.vlay)

    def sendMessage(self):
        print('in sendMessage')
        data = {'event':'secret_chat'
                ,'own_nickname':self.own_nickname
                ,'peer_nickname':self.peer_nickname
                ,'data':self.input_text.toPlainText()}
        self.input_text.clear()
        self.input_text.focusWidget()
        print('data=',data)
        sendData(self.udp_socket,data)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    comm = CommWidget('','' ,'')
    comm.show()
    sys.exit(app.exec_())