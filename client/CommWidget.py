import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from share.share import packSendData
from .ProcessRecv import ProcessRecv
from share.share import server_addr

class CommWidget(QWidget):
    '''
    功能：
        1. 提供私聊、组聊GUI
        2. 检测发送消息的事件
        3. 处理、显示从服务器接收到的信息
    '''

    def __init__(self,udp_socket,own_nickname,peer_nickname,isSecretChat = None,parent = None):
        super(CommWidget,self).__init__(parent)
        self.udp_socket = udp_socket
        self.peer_nickname = peer_nickname
        self.own_nickname = own_nickname
        self.isSecretChat = isSecretChat
        self.setWindowTitle(peer_nickname)
        self._gui()

        self.recv_thread = ProcessRecv(self.udp_socket)
        self.recv_thread.start()
        self.recv_thread.dataRecved.connect(self.recvMessage)

    def recvMessage(self,data):
        if data.get('peer_nickname') == self.own_nickname and data.get('own_nickname') == self.peer_nickname:
            self.history_text.append(data.get('data') )
        elif data.get('peer_nickname') == self.peer_nickname:
            self.history_text.append(data.get('data'))

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
        if self.isSecretChat:
            flag = 'secret_chat'
        else:
            flag = 'group_chat'
        data = {'event':flag
                ,'own_nickname':self.own_nickname
                ,'peer_nickname':self.peer_nickname
                ,'data':self.input_text.toPlainText()}
        self.input_text.clear()
        self.input_text.focusWidget()
        print('data=',data)
        packSendData(self.udp_socket,server_addr,data)

if __name__ == '__main__':
    # app = QtWidgets.QApplication(sys.argv)
    # comm = CommWidget('','' ,'')
    # comm.show()
    # sys.exit(app.exec_())
    pass