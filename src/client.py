import sys
# sys.path.append('H:\Project\PythonChat\src')
from PyQt5 import QtWidgets
from cli.Login import Login

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = Login()
    myshow.show()
    sys.exit(app.exec_())