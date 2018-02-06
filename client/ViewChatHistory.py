from PyQt5.QtWidgets import *
from share.share import server_addr,packSendData
from .ProcessRecv import ProcessRecv

class ViewChatHistory(QWidget):
    def __init__(self,udp_socket,own_nickname,parent = None):
        super(ViewChatHistory,self).__init__(parent)
        self.udp_socket = udp_socket
        self.own_nickname = own_nickname
        self.setWindowTitle('查看聊天历史')

        # 现象：此处要先创建接收线程、再发送数据
        #      若先发送数据，再创建接收线程，client会自动退出
        # 原因：
        self.recv_thread = ProcessRecv(self.udp_socket)
        self.recv_thread.start()
        self.recv_thread.dataRecved.connect(self.recvMessage)

        packSendData(self.udp_socket, server_addr, {'event': 'get_history', 'own_nickname': self.own_nickname})

    def recvMessage(self,data):
        print('data_history = ',data)
        hlay = QHBoxLayout()
        table = QTableWidget()

        row_count = len(data)
        column_count = len(data[0])
        table.setRowCount(row_count)
        table.setColumnCount(column_count)
        table.setHorizontalHeaderLabels(['发送者','接收者','发送时间','内容'])

        for row_index in range(row_count):
            for column_index in range(column_count):
                item = QTableWidgetItem(data[row_index][column_index])
                table.setItem(row_index,column_index,item)

        hlay.addWidget(table)
        self.setLayout(hlay)
