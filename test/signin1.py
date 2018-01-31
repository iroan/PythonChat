# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *

class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("登录界面")
        self.resize(200,100)

        lay =QFormLayout()

        Lab1=QLabel("用户名")
        Lab2=QLabel("密码")

        Line1=QLineEdit()
        Line2=QLineEdit()
        self.Line3=QLineEdit()

        OkB=QPushButton("确定")
        CB =QPushButton("取消")

        lay.addRow(Lab1,Line1)
        lay.addRow(Lab2,Line2)
        lay.addRow(self.Line3)
        lay.addRow(OkB, CB)
        self.setLayout(lay)

        CB.clicked.connect(lambda :self.close())
        OkB.clicked.connect(lambda :self.Print())

    def Print(self):
        print('-------')
        self.Line3.setText('wkxwkx')
