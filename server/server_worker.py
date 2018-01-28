class Worker:
    '''
    功能：
        1. 处理从client收到的数据，
            1. 判断是哪个用户发送的

    '''
    def __init__(self,nickname):
        self.nickname = nickname