from PyQt5.QtWidgets import *  # QMainWindow, QApplication, QSlider, QLabel, QTableWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Загрузите файл пользовательского интерфейса
        uic.loadUi("Queue.ui", self)

        # Определите наши виджеты
        self.slider = self.findChild(QSlider, "horizontalSlider_D1")
        self.label = self.findChild(QLabel, "label_for_slader_D1")
        self.slider2 = self.findChild(QSlider, "horizontalSlider_D2")
        self.label2 = self.findChild(QLabel, "label_for_slader_D2")

        # Установить свойства ползунка
        self.slider_properties(self.slider)
        self.slider_properties(self.slider2)

        # Переместить ползунок
        self.slider.valueChanged.connect(self.slide_1)
        self.slider2.valueChanged.connect(self.slide_2)

        # Show The App
        self.show()

    def slider_properties(self, slider):
        slider.setMinimum(0)
        slider.setMaximum(50)
        slider.setValue(0)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(5)
        slider.setSingleStep(5)

    def slide_1(self, value):
        self.label.setText(str(value))

    def slide_2(self, value):
        self.label2.setText(str(value))


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
