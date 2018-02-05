from PyQt5.QtCore import QThread,pyqtSignal,Qt
import json

class ProcessRecv(QThread):
    dataRecved = pyqtSignal(object)
    def __init__(self,udp_socket):
        super(ProcessRecv, self).__init__()
        self.udp_socket = udp_socket

    def run(self):
        while True:
            recv_date,addr = self.udp_socket.recvfrom(1024)
            data = json.loads(recv_date)
            self.dataRecved.emit(data)

