from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 300, 200, 300)
    win.setWindowTitle("Teste")
    label = QtWidgets.QLabel(win)
    label.setText("Primeiro label")
    label.move(10, 10)

    win.show()
    sys.exit(app.exec_())


window()
