import json
from threading import Thread

class Worker:
    def __init__(self,udp_socket,addr,user_nickname):
        self.udp_socket = udp_socket
        self.addr = addr
        self.user_nickname = user_nickname
        self.create_process_input()
        self.process_server_message()

    def process_server_message(self):
        while True:
            recv_data = self.udp_socket.recvfrom(1024)
            print('recv_data=',recv_data)

    def create_process_input(self):
        thread_send = Thread(target=self.process_input)
        thread_send.start()
        thread_send.join()

    def process_input(self):
        print('in process_input')
        while True:
            data = input('>>>') # TODO 需要自定义发送消息的数据结构
            data ={'data':data,}
            data1 = json.dumps(data)
            self.udp_socket.sendto(data1.encode(),self.addr)

