from server.db import MySqlHelper
from server.signin import SignIn

class Worker:
    def __init__(self,udp_socket,data,addr):
        self.udp_socket = udp_socket
        self.client_data = {}
        self.client_data = data
        self.mysqlhelper = MySqlHelper('iroan', 'iroanMYS47', 'ssltools')
        self.addr = addr
        self.processMessage()

    def processMessage(self):
        if self.client_data.get('event') == 'register':
            self.register()

        if self.client_data.get('event') == 'signin':
            self.signin()

    def register(self):
        nickname = self.client_data.get('nickname')
        password = self.client_data.get('password')
        s1 = SignIn(nickname,password)
        result = s1.register()
        self.udp_socket.sendto(result.encode(),self.addr)


    def signin(self):
        nickname = self.client_data.get('nickname')
        password = self.client_data.get('password')
        s1 = SignIn(nickname,password)
        result = s1.singin()
        self.udp_socket.sendto(result.encode(),self.addr)
