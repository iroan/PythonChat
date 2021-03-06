from ser.db import MySqlHelper
import json
from com.share import packSendData
from com.log import logger_server
class Worker:
    def __init__(self,udp_socket,data_from_client,client_addr):
        self.udp_socket = udp_socket
        self.client_addr = client_addr
        self.data_from_client = data_from_client
        self.is_1_Flag = '在线'
        self.mysqlhelper = MySqlHelper('iroan','iroanMYS47','ssltools')

    def processMessage(self):
        if self.data_from_client.get('event') == 'alter_own_info':
            self.alterOwnInfo()

        if self.data_from_client.get('event') == 'get_own_info':
            self.getOwnInfo()

        if self.data_from_client.get('event') == 'get_history':
            self.getHistory()

        if self.data_from_client.get('event') == 'broadcast':
            self.broadCast()

        if self.data_from_client.get('event') == 'secret_chat':
            self.secretChat()

        if self.data_from_client.get('event') == 'group_chat':
            self.groupChat()

        if self.data_from_client.get('event') == 'register':
            self.register()

        if self.data_from_client.get('event') == 'signin':
            self.signin()

        if self.data_from_client.get('event') == 'get_all_users_info':
            self.getUsers()

        if self.data_from_client.get('event') == 'offline':
                self.offline()

    def groupChat(self): #TODO 后期要实现消息离线发送功能
        '''
        功能：
            1. 获取peer_nickname的在线成员
            2. 插入聊天记录
            2. 获取peer_nickname的在线成员的addr
            3. 获取peer_nickname的在线成员的转发消息
        '''
        sql = 'select ip,port from user where isOnline = %s and department = %s;'
        addr = self.mysqlhelper.read_all(sql, ['在线',self.data_from_client.get('peer_nickname')])
        self.insertMessageHistory(self.data_from_client)
        for temp in addr:
            packSendData(self.udp_socket, (temp[0],int(temp[1])), self.data_from_client)

    def alterOwnInfo(self):
        data = self.data_from_client
        changed_words = data.get('changed_words')
        if changed_words == 'nickName':
            sql = 'update user set nickName = %s where nickName = %s;'
        elif changed_words == 'trueName':
            sql = 'update user set trueName = %s where nickName = %s;'
        elif changed_words == 'gender':
            sql = 'update user set gender = %s where nickName = %s;'
        elif changed_words == 'department':
            sql = 'update user set department = %s where nickName = %s;'
        elif changed_words == 'position':
            sql = 'update user set position = %s where nickName = %s;'
        elif changed_words == 'introduce':
            sql = 'update user set introduce = %s where nickName = %s;'
        elif changed_words == 'email':
            sql = 'update user set email = %s where nickName = %s;'
        elif changed_words == 'phone':
            sql = 'update user set phone = %s where nickName = %s;'
        res = self.mysqlhelper.execute(sql, [data.get('data'),data.get('own_nickname')])
        status = ''
        if res == 0:
            status = '修改失败'
        elif res == 1:
            status = '修改成功'
        packSendData(self.udp_socket, self.client_addr, {'event': 'alter_own_info',
                                                         'own_nickname': data.get('own_nickname'),
                                                         'status': status})

    def getOwnInfo(self):
        sql = 'select nickName,trueName,gender,department,position,introduce,email,phone ' \
              'from user where nickName = %s;'
        data = self.mysqlhelper.read_all(sql, [self.data_from_client.get('own_nickname')])

        packSendData(self.udp_socket,self.client_addr, {'data':data,
                                                        'event':'get_own_info'})

    def getHistory(self):
        sql = 'select nickNameSend,nickNameRecv,sendTime,message ' \
              'from messagehistory where nickNameSend = %s or nickNameRecv = %s;'
        data = self.mysqlhelper.read_all(sql, [self.data_from_client.get('own_nickname')
                                           ,self.data_from_client.get('own_nickname')])
        packSendData(self.udp_socket,self.client_addr, data)

    def broadCast(self):
        sql = 'select ip,port from user where isOnline = %s;'
        addr = self.mysqlhelper.read_all(sql, ['在线'])
        self.insertMessageHistory(self.data_from_client)
        for temp in addr:
            packSendData(self.udp_socket, (temp[0],int(temp[1])), self.data_from_client)

    def secretChat(self):
        '''
        功能：
            1. 判断peer_nickname是否在线
                在线获取address
                不在线，回复own_nickname，对方不在线
            2. 向message_history写入聊天记录
            3. 向peer_nickname转发信息
        '''
        sql = 'select ip,port from user where nickName = %s;'
        addr = self.mysqlhelper.read_all(sql, [self.data_from_client.get('peer_nickname')])

        addr = (addr[0][0],int(addr[0][1]))# addr是嵌套的元组，addr[0]才是有效地址
        if addr[0][0] == '' and addr[0][1] == '':
            data = {'event': 'secret_chat'
                , 'peer_nickname': self.data_from_client.get('peer_nickname')
                , 'data': '消息发送失败，'+ self.data_from_client.get('peer_nickname') +'不在线！'}
            packSendData(self.udp_socket,self.client_addr,data)
        else:
            self.insertMessageHistory(self.data_from_client)
            packSendData(self.udp_socket,addr,self.data_from_client)

    def insertMessageHistory(self,data):
        sql = 'insert into messagehistory(nickNameSend,nickNameRecv,sendTime,message) values(%s,%s,%s,%s);'
        res = self.mysqlhelper.execute(sql,[data.get('own_nickname')
            ,data.get('peer_nickname')
            ,self.getTime()
            ,data.get('data')])

    def getTime(self):
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def offline(self):
        sql = 'update user set isOnline = %s where nickName = %s;'
        self.mysqlhelper.execute(sql, ['离线',self.data_from_client.get('nickname')])


    def register(self):

        sql = 'insert into user(nickName,password) values(%s,%s);'
        res = self.mysqlhelper.execute(sql
                                       , [self.data_from_client.get('nickname')
                                                    ,self.data_from_client.get('password')])
        response_client = ''
        if res == 0:
            response_client = '注册失败-因为该昵称已经被使用，请换一个昵称注册'
            logger_server.info(response_client)
        elif res == 1:
            response_client = '注册成功，请登录使用'
        else:
            response_client = '注册失败-程序错误'
            logger_server.error(response_client)
        self.udp_socket.sendto(response_client.encode(),self.client_addr)

    def signin(self):
        sql = 'select isOnline,password from user where nickName = %s;'
        res = self.mysqlhelper.read_all(sql,[self.data_from_client.get('nickname')]) # TODO isOnline要设置默认值离线
        # 'navicat 设置索引中的名是什么意思、有什么作用'
        response_client = ''
        if res == ():
            response_client = '该用户未注册'
            logger_server.info(response_client)

        elif self.data_from_client.get('password') == res[0][1]:
            if res[0][0] == self.is_1_Flag:
                response_client = '该用户已登录，不能重复登录' # TODO 需要支持重复登录吗？
                logger_server.info(response_client)
            if res[0][0] != self.is_1_Flag:
                sql = 'update user set isOnline = %s where nickName = %s;'
                self.mysqlhelper.execute(sql, ['在线',self.data_from_client.get('nickname')])
                self.updateUserLoginAddr(self.data_from_client.get('nickname')
                                         ,self.client_addr)
                response_client = '登录成功'
        else:
            response_client = '密码错误'
            logger_server.error(response_client)
        self.udp_socket.sendto(response_client.encode(),self.client_addr)

    def updateUserLoginAddr(self,nickname,addr):
        sql = 'update user set ip = %s, port = %s where nickName = %s;'
        self.mysqlhelper.execute(sql, [addr[0],addr[1], nickname])

    def getUsers(self):
        sql = 'select nickName,trueName,department,isOnline from user;'
        data = self.mysqlhelper.read_all(sql)
        response_client = json.dumps({'event':'sol'
                                         ,'data':data})
        self.udp_socket.sendto(response_client.encode(), self.client_addr)

if __name__ == '__main__':

    # 测试任意参数
    def test(*params):
        print(list[params])
    test('wangk','cgr','123')

    pass
    # work = Worker('','','').getUsers()