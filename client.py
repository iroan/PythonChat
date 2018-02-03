import sys
sys.path.append('H:\Project\PythonChat')
from socket import *
from share.share import server_addr
import sys
from PyQt5 import QtWidgets
from client.signin import SignIn

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = SignIn()
    myshow.show()
    sys.exit(app.exec_())