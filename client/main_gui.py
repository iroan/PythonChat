from PyQt5.QtWidgets import *
from share.share import server_addr,packSendData
from .CenterWidget import CenterWidget
from .BroadCast import BroadCast

class Main(QMainWindow):
    def __init__(self,udp_socket,nickname,parent = None):
        super(Main, self).__init__(parent)
        self.udp_socket = udp_socket
        self.own_nickname = nickname

        menu_chat = self.menuBar().addMenu('聊天')
        self.action_quit = QAction('退出',menu_chat)
        self.action_broadcast = QAction('广播',menu_chat)

        menu_chat.addAction(self.action_quit)
        menu_chat.addAction(self.action_broadcast)

        self.action_quit.triggered.connect(self.onQuit)
        self.action_quit.triggered.connect(self.close)
        self.action_broadcast.triggered.connect(self.onBroadCast)

        self.setWindowTitle('SSLTools')
        central_widget = CenterWidget(self.udp_socket, self.own_nickname)
        self.setCentralWidget(central_widget)

    def onQuit(self):
        packSendData(self.udp_socket, server_addr, {'event': 'offline', 'nickname': self.own_nickname})

    def onBroadCast(self):
        self.broadcast = BroadCast(self.udp_socket, self.own_nickname)
        self.broadcast.show()