import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
from socket import *
from share.share import server_addr,packSendData
from .communication import CommWidget

class Main(QMainWindow):
    def __init__(self,udp_socket,nickname,parent = None):
        super(Main, self).__init__(parent)
        self.udp_socket = udp_socket
        self.nickname = nickname

        menu_chat = self.menuBar().addMenu('聊天')
        self.action_quit = QAction('退出',menu_chat)
        menu_chat.addAction(self.action_quit)
        self.action_quit.triggered.connect(self.onQuit)
        self.action_quit.triggered.connect(self.close)

        self.setWindowTitle('SSLTools')
        central_widget = CenterWidget(self.udp_socket,self.nickname)
        self.setCentralWidget(central_widget)

    def onQuit(self):
        packSendData(self.udp_socket,server_addr,{'event': 'offline', 'nickname': self.nickname})

class CenterWidget(QWidget):
    def __init__(self,udp_socket,own_nickname,parent = None):
        super(CenterWidget,self).__init__(parent)
        self.udp_socket = udp_socket
        self.own_nickname = own_nickname

        packSendData(self.udp_socket,server_addr,{'event': 'get_all_users_info'})
        data, addr = self.udp_socket.recvfrom(1024)
        datafromserver = json.loads(data)

        hlay = QHBoxLayout()
        self.tree = QTreeWidget() # 设置列数
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['昵称', '姓名', '状态']) # 设置头的标题
        self.loads(datafromserver.get('data'))

        hlay.addWidget(self.tree)

        vlay_main = QHBoxLayout()
        vlay_main.addLayout(hlay)
        self.setLayout(vlay_main)

        self.tree.clicked.connect(self.onItemClick)
        # self.tree.pressed.connect(self.onItemClick)
        self.tree.activated.connect(self.onItemClick)

    def onItemClick(self):
        '''
        功能：判断用户点击的是一个用户item、还是一个组item
            1. 是用户item就发送私密消息
            2. 是组item就发送组消息
        :return:
        '''
        item = self.tree.currentItem()
        print('key = %s,value = %s' % (item.text(0), item.text(1)))
        item = self.tree.currentItem()
        nickname = item.text(0)
        self.comm = CommWidget(self.udp_socket,self.own_nickname,nickname)
        self.comm.show()
        # if '部' in nickname and name == '':
        #     comm = CommWidget(self.udp_socket,nickname)
        #     self.groupMessage(nickname)
        # else:
        #     self.userMessage(nickname)


    def userMessage(self,peer_nickname,data):
        '''
        发送消息
        1. 构造数据
        2. 发送数据
        '''
        packSendData(self.udp_socket,server_addr,{'event': 'offline'
                                 ,'nickname': self.nickname
                                 ,'peer_nickname':peer_nickname
                                 ,'data':data})

    def groupMessage(self,peer_nickname):
        pass

    def loads(self,data):
        '''加载数据：
                1. 检测item所在部门是否创建
                2. 已经创建，item加入该部门成为子对象
                3. 没有创建，创建该部门，且让该item成为子对象
        '''

        '''换一种思路：
            1. 先建部分
            2. 在添加item到对于的部门下面
        '''

        '''获取部门信息'''
        parents = set() # 集合，用于保存部门名称
        for row_date in data: # 遍历每一行数据（一个用户的数据）
            print(row_date)
            parents.add(row_date[2])

        '''新建部门item'''
        for row_date in parents: # 遍历每一行数据（一个用户的数据）
            item = QTreeWidgetItem(self.tree)  # root表示self.tree下下一级的一个item
            item.setText(0, row_date)

        '''按照用户所属部门新建用户item'''
        for row_date in data: # 遍历每一行数据（一个用户的数据）
            for i in range(self.tree.topLevelItemCount()):
                item = self.tree.topLevelItem(i)
                if row_date[2] == item.text(0):
                    root = QTreeWidgetItem(item)  # root表示self.tree下下一级的一个item
                    root.setText(0, row_date[0])
                    root.setText(1, row_date[1])
                    root.setText(2, row_date[3])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.connect(server_addr)
    myshow = Main(udp_socket,' ')
    myshow.show()
    sys.exit(app.exec_())
