import sys
from PyQt5 import QtWidgets
from signin1 import Ui_Form

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = Ui_Form()
    myshow.show()
    sys.exit(app.exec_())
