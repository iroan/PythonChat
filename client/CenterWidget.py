from PyQt5.QtWidgets import *
import json
from share.share import server_addr,packSendData
from .CommWidget import CommWidget

class CenterWidget(QWidget):
    def __init__(self,udp_socket,own_nickname,parent = None):
        super(CenterWidget,self).__init__(parent)
        self.udp_socket = udp_socket
        self.own_nickname = own_nickname

        packSendData(self.udp_socket,server_addr,{'event': 'get_all_users_info'})
        data, addr = self.udp_socket.recvfrom(1024)
        datafromserver = json.loads(data)

        hlay = QVBoxLayout()
        self.tree = QTreeWidget() # 设置列数
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['昵称', '姓名', '状态']) # 设置头的标题
        temp = self.loads(datafromserver.get('data'))
        str = '在线人数:'+repr(temp[0])+'  离线人数:'+repr(temp[1])+'  总人数:'+repr(temp[2])
        self.lab = QLabel(str)
        hlay.addWidget(self.lab)
        hlay.addWidget(self.tree)

        self.setLayout(hlay)

        self.tree.clicked.connect(self.onItemClick)
        self.tree.activated.connect(self.onItemClick)

    def onItemClick(self):
        '''
        功能：判断用户点击的是一个用户item、还是一个组item
            1. 是用户item就发送私密消息
            2. 是组item就发送组消息
        :return:
        '''
        item = self.tree.currentItem()
        item = self.tree.currentItem()
        isSecret = None
        if '部' in item.text(0) and item.text(1) == '':
            isSecret = False
        elif item.text(0) == '其他':
            isSecret = False
        else:
            isSecret = True
        self.comm = CommWidget(self.udp_socket, self.own_nickname, item.text(0),isSecret)
        self.comm.show()

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

        all_user = len(data)
        online_user = 0
        offline_user = 0

        for row_date in data: # 遍历每一行数据（一个用户的数据）
            # print(row_date)
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
                    if row_date[3] == '在线':
                        online_user = online_user + 1
                    elif row_date[3] == '离线':
                       offline_user = offline_user + 1
        return (online_user,offline_user,all_user)