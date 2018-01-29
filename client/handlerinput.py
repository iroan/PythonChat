from share.share import global_order,addr
import json
class HandlerInput:
    def __init__(self,udp_socket,info):
        self.to_send_data = info
        self.udp_socket = udp_socket
        self.to_send_data['prompt'] = '没有活动'

    def anaylseInput(self,input_data):
        available_data = self.getAvailableField(input_data)
        if available_data[0] == 'sol' and len(available_data) == 1:
            self.to_send_data.get()
            self.sendto(self.to_send_data)

    def getAvailableField(self,input_data):
        '''
        处理步骤
            1. 分割字符串
            2. 去掉统计''的个数
            3. 删除''n次
        '''
        d1 = input_data.split(' ')
        for i in range(d1.count('')):
            d1.remove('')
        return d1
    def sendto(self,data):
        '''
        主要数据:
            1. 发送方nickname
            2. 接受方nickname
            3. event
            4. message
        '''
        data1 = json.dumps(data)
        self.udp_socket.sendto(data1.encode(), addr)


if __name__ == '__main__':
    h = HandlerInput()
    a = h.getAvailableField(input('>>>'))
    print(a)




