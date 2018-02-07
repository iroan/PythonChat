from PyQt5.QtWidgets import *
from share.share import server_addr,packSendData
from .ProcessRecv import ProcessRecv
from share.log import logger_client
class ViewOwnInfo(QWidget):
    '''
    修改的方案：
        1. 改变一项就向服务器提交一项
        2. 设置提交按钮，按下按钮就读取各项内容，向服务器提交

    选择1，理由是：一般来讲，用户很少一次性修改个人信息的全部选项
    '''
    def __init__(self,udp_socket,own_nickname,parent = None):
        super(ViewOwnInfo,self).__init__(parent)
        self.udp_socket = udp_socket
        self.own_nickname = own_nickname
        self.setWindowTitle('个人信息')
        self.setUI()

        self.recv_thread = ProcessRecv(self.udp_socket)
        self.recv_thread.start()
        self.recv_thread.dataRecved.connect(self.recvMessage)

        packSendData(self.udp_socket, server_addr, {'event': 'get_own_info', 'own_nickname': self.own_nickname})

    def recvMessage(self,data):
        logger_client.debug('client/ViewOwnInfo.py:19\t'+str(data))
        if data.get('event') == 'get_own_info':
            data = data.get('data')
            self.row_count = 8
            column_count = 1
            self.table.setRowCount(self.row_count)
            self.table.setColumnCount(column_count)
            self.table.setVerticalHeaderLabels(['昵称','真实姓名','性别','所在部门','职位','介绍你自己','邮箱','电话号码'])
            self.table.setHorizontalHeaderLabels(['内容'])

            for row_index in range(self.row_count):
                item = QTableWidgetItem(data[0][row_index])
                self.table.setItem(row_index,0,item)

            # 加载完数据，再检测数据是否变化
            self.table.cellChanged.connect(self.onCellChanged)
        elif data.get('event') == 'alter_own_info':
            QMessageBox(text=data.get('status')).exec()

    def setUI(self):
        hlay = QVBoxLayout()
        self.table = QTableWidget()
        hlay.addWidget(self.table)
        self.setLayout(hlay)

    def onCellChanged(self,row,column):
        changed_words =  ['nickName','trueName','gender','department','position','introduce','email','phone']
        packSendData(self.udp_socket, server_addr, {'event': 'alter_own_info',
                                                    'own_nickname': self.own_nickname,
                                                    'changed_words': changed_words[row],
                                                    'data':self.table.item(row,0).text()})
