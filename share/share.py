server_addr = ('127.0.0.1',11000)
global_1field_order = ('sol', 'soi', 'sch')

import json

def packSendData(udp_socket,addr,data_sendto_server):
    '''
    主要数据:
        1. 发送方nickname
        2. 接受方nickname
        3. event
        4. message
    '''
    print('udp_socket = ',udp_socket)
    print('addr = ',addr)
    print('data_sendto_server= ',data_sendto_server)

    send_data = json.dumps(data_sendto_server)
    udp_socket.sendto(send_data.encode(), addr)




