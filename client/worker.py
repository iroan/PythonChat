from threading import Thread
from client.handlerserver import HandlerServer
from client.handlerinput import HandlerInput
class Worker:
    def __init__(self,udp_socket,own_nickname):
        self.to_send_data = {}
        self.udp_socket = udp_socket
        self.to_send_data['own_nickname'] = own_nickname
        self.create_process_input()
        self.process_server_message()

    def process_server_message(self):
        while True:
            data,addr = self.udp_socket.recvfrom(1024)
            self.to_send_data['recv_data'] = data
            HandlerServer(self.udp_socket, self.to_send_data)

    def create_process_input(self):
        thread_send = Thread(target=self.process_input)
        thread_send.start()
        thread_send.join()

    def process_input(self):
        print('in process_input')
        handler_input = HandlerInput(self.udp_socket, self.to_send_data)
        while True:
            self.prompt = handler_input.to_send_data.get('prompt')
            input_data = input(self.prompt) # TODO 需要自定义发送消息的数据结构
            handler_input.anaylseInput(input_data)

if __name__ == '__main__':
    pass