from PyQt5.QtWidgets import *
from com.share import server_addr,packSendData
from .ProcessRecv import ProcessRecv

class BroadCast(QWidget):
        '''
        功能：
            1. 提供广播GUI
            2. 检测发送消息的事件
            3. 处理、显示从服务器接收到的信息
        '''
        def __init__(self, udp_socket, own_nickname, parent=None):
            super(BroadCast, self).__init__(parent)
            self.udp_socket = udp_socket
            self.own_nickname = own_nickname
            self.setWindowTitle('广播')
            self._gui()
            self.recv_thread = ProcessRecv(self.udp_socket)
            self.recv_thread.start()
            self.recv_thread.dataRecved.connect(self.recvMessage)

        def recvMessage(self, data):
            print('in recvMessage data=',data)
            if data.get('event') == 'broadcast':
                self.history_text.append(data.get('data'))

        def _gui(self):
            self.history_text = QTextEdit()
            self.input_text = QTextEdit()
            history_label = QLabel('&H历史记录:')
            input_label = QLabel('&I输入消息:')
            input_label.setBuddy(self.input_text)
            history_label.setBuddy(self.history_text)

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
            data = {'event': 'broadcast'
                , 'own_nickname': self.own_nickname
                , 'peer_nickname': 'broadcast'
                , 'data': self.input_text.toPlainText()}
            self.input_text.clear()
            self.input_text.focusWidget()
            print('data=', data)
            packSendData(self.udp_socket, server_addr, data)

# TODO 组聊发送消息收到和收不到交替现象