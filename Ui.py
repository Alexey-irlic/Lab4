from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def application():
    app = QApplication(sys.argv)
    Window = QMainWindow()

    Window.setWindowTitle('Новое окно')
    Window.setGeometry(300, 250, 800, 600)

    mainText = QtWidgets.QLabel(Window)
    mainText.setText("Привет мир!")

    Window.show()
    sys.exit(app.exec_())


    