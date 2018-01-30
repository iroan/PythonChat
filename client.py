import sys
sys.path.append('H:\Project\PythonChat')
from socket import *
from client.signin import SignIn
from client.worker import Worker
from share.share import server_addr

def Main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.connect(server_addr)

    signin = SignIn(udp_socket, server_addr)
    result = signin.processSignIn()

    if result:
        Worker(udp_socket,signin.getUserNickName()).process()

    udp_socket.close()

if __name__ == '__main__':
    Main()