import sys
sys.path.append('H:\Project\PythonChat')
from socket import *
from client.worker import Worker
from share.share import server_addr
import sys
from PyQt5 import QtWidgets
from client.signin import SignIn_GUI

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = SignIn_GUI()
    myshow.show()
    sys.exit(app.exec_())