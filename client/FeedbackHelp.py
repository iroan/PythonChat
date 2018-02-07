from PyQt5.QtWidgets import *
from share.share import server_addr,packSendData
from .ProcessRecv import ProcessRecv

class FeedbackHelp(QWidget):
    def __init__(self,parent = None):
        super(FeedbackHelp,self).__init__(parent)
        self.setWindowTitle('反馈与帮助')
        hlay = QHBoxLayout()
        text = QTextEdit()
        text.append('不管您是使用该程序，还是想拿这个项目练手的coder。')
        text.append('如果有任何关于该软件使用、环境配置、源码求助等问题,有以下两种方式联系到作者：')
        text.append('   1. 发送邮件，邮箱地址：2654189525@qq.com')
        text.append('   2. 发布Issue，地址：https://github.com/iroan/PythonChat/issues')
        text.append('\n欢迎骚扰！！！')
        hlay.addWidget(text)
        self.setLayout(hlay)

