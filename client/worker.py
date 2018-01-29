import json
from threading import Thread
from client.handlerserver import HandlerServer

class Worker:
    def __init__(self,udp_socket,own_nickname):
        self.info = {}
        self.udp_socket = udp_socket
        self.info['own_nickname'] = own_nickname
        self.create_process_input()
        self.process_server_message()

    def process_server_message(self):
        while True:
            data,addr = self.udp_socket.recvfrom(1024)
            self.info['recv_data'] = data
            HandlerServer(self.udp_socket,self.info)

    def create_process_input(self):
        thread_send = Thread(target=self.process_input)
        thread_send.start()
        thread_send.join()

    def process_input(self):
        print('in process_input')
        while True:
            data = input('>>>') # TODO 需要自定义发送消息的数据结构
            self.info['input_data'] = data
            data1 = json.dumps(data)
            self.udp_socket.sendto(data1.encode(),self.addr)
