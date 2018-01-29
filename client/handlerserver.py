'''
处理服务器发来的消息
'''
class HandlerServer:
    def __init__(self,udp_socket,info):
        self.udp_socket = udp_socket
        self.info = info
        self.analyseEvent()

    def analyseEvent(self):
        print('self.data=',self.info)



