import sys
from PyQt5.QtWidgets import *
from share.share import server_addr,packSendData
from .CenterWidget import CenterWidget
from .BroadCast import BroadCast
from .ViewChatHistory import ViewChatHistory

class Main(QMainWindow):
    def __init__(self,udp_socket,nickname,parent = None):
        super(Main, self).__init__(parent)
        self.udp_socket = udp_socket
        self.own_nickname = nickname
        self.setWindowTitle('SSLTools')

        self.central_widget = CenterWidget(self.udp_socket, self.own_nickname)
        self.setCentralWidget(self.central_widget)

        self.setMenuChat()
        self.setMenuView()


    def setMenuView(self):
        self.menu_view = self.menuBar().addMenu('查看')
        self.action_view_history = QAction('通讯历史', self.menu_view)
        self.menu_view.addAction(self.action_view_history)
        self.action_view_history.triggered.connect(self.onViewChatHistory)

    def setMenuChat(self):
        self.menu_chat = self.menuBar().addMenu('通讯')

        self.action_chat = QAction('聊天', self.menu_chat)
        self.action_broadcast = QAction('广播', self.menu_chat)
        self.action_quit = QAction('退出', self.menu_chat)

        self.menu_chat.addAction(self.action_chat)
        self.menu_chat.addAction(self.action_broadcast)
        self.menu_chat.addAction(self.action_quit)

        self.action_chat.triggered.connect(self.onChat)
        self.action_quit.triggered.connect(self.onQuit)
        self.action_broadcast.triggered.connect(self.onBroadCast)

    def onChat(self):
        self.central_widget.show()

    def onQuit(self):
        packSendData(self.udp_socket, server_addr, {'event': 'offline', 'nickname': self.own_nickname})
        sys.exit()

    def onBroadCast(self):
        self.broadcast = BroadCast(self.udp_socket, self.own_nickname)
        self.broadcast.show()

    def onViewChatHistory(self):
        self.chat_history= ViewChatHistory(self.udp_socket, self.own_nickname)
        self.chat_history.show()
