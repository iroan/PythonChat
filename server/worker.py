from server.db import MySqlHelper
import json
class Worker:
    def __init__(self,udp_socket,data_from_client,client_addr):
        self.udp_socket = udp_socket
        self.client_addr = client_addr
        self.data_from_client = data_from_client
        self.is_1_Flag = b'\x01'
        self.mysqlhelper = MySqlHelper('iroan','iroanMYS47','ssltools')

    def processMessage(self):
        if self.data_from_client.get('event') == 'register':
            self.register()

        if self.data_from_client.get('event') == 'signin':
            self.signin()

        if self.data_from_client.get('event') == 'sol':
            self.getOnlineClient()

        if self.data_from_client.get('event') == 'offline':
            self.offline()

    def offline(self):
        sql = 'update user set isOnline = 0 where nickName = %s;'
        self.mysqlhelper.execute(sql, [self.data_from_client.get('nickname')])


    def register(self):

        sql = 'insert into user(nickName,password) values(%s,%s);'
        res = self.mysqlhelper.execute(sql
                                       , [self.data_from_client.get('nickname')
                                                    ,self.data_from_client.get('password')])
        response_client = ''
        if res == 0:
            response_client = '注册失败-因为该昵称已经被使用，请换一个昵称注册'
        elif res == 1:
            response_client = '注册成功，请登录使用'
        else:
            response_client = '注册失败-程序错误'
        self.udp_socket.sendto(response_client.encode(),self.client_addr)

    def signin(self):
        sql = 'select isOnline,password from user where nickName = %s;'
        res = self.mysqlhelper.read_all(sql,[self.data_from_client.get('nickname')]) # TODO isOnline要设置默认值0
        # 'navicat 设置索引中的名是什么意思、有什么作用'
        response_client = ''
        if res == ():
            response_client = '该用户未注册'

        if self.data_from_client.get('password') == res[0][1]:
            if res[0][0] == self.is_1_Flag:
                response_client = '该用户已登录，不能重复登录' # TODO 需要支持重复登录吗？
            if res[0][0] != self.is_1_Flag:
                sql = 'update user set isOnline = 1 where nickName = %s;'
                self.mysqlhelper.execute(sql, [self.data_from_client.get('nickname')])
                response_client = '登录成功'
        else:
            response_client = '密码错误'
        self.udp_socket.sendto(response_client.encode(),self.client_addr)

    def getOnlineClient(self):
        sql = 'select nickName from user where isOnline = 1;'
        data = self.mysqlhelper.read_all(sql)
        print('data =\n', data)
        response_client = json.dumps({'event':'sol'
                                ,'data':data})

        print('response_client =\n',response_client)
        self.udp_socket.sendto(response_client.encode(), self.client_addr)
