from socket import *
from client.signin import SignIn
from client.worker import Worker
from share.share import addr

def Main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.connect(addr)

    sn = SignIn(udp_socket,addr)
    res = sn.show_start_GUI()
    if res:
        work = Worker(udp_socket,sn.getUserNickName())
    udp_socket.close()

if __name__ == '__main__':
    Main()