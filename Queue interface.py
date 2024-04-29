from PyQt5.QtWidgets import *  # QMainWindow, QApplication, QSlider, QLabel, QTableWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import random
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Загрузите файл пользовательского интерфейса
        uic.loadUi("Queue.ui", self)

        # Определите наши виджеты
        self.slider = self.findChild(QSlider, "horizontalSlider_D1")
        self.label = self.findChild(QLineEdit, "label_for_slader_D1")
        self.slider2 = self.findChild(QSlider, "horizontalSlider_D2")
        self.label2 = self.findChild(QLineEdit, "label_for_slader_D2")

        # Установить свойства ползунка
        self.slider_properties(self.slider)
        self.slider_properties(self.slider2)

        self.MaxPriorities = [0] * 10
        self.timer1 = QTimer(self)
        self.timer2 = QTimer(self)

        self.pushButton_Start_D1.clicked.connect(self.start_timer_d1)
        self.pushButton_Stop_D1.clicked.connect(self.stop_timer_d1)
        self.slider.valueChanged.connect(self.start_timer_d1)

        self.pushButton_Start_D2.clicked.connect(self.start_timer_d2)
        self.pushButton_Stop_D2.clicked.connect(self.stop_timer_d2)
        self.slider2.valueChanged.connect(self.start_timer_d2)

        self.timer1.timeout.connect(self.queue_table)
        self.timer2.timeout.connect(self.queue_table_2)

        self.processed = [0] * 10
        self.data_table()

        # Show The App
        self.show()

    def slider_properties(self, slider):
        slider.setMinimum(100)
        slider.setMaximum(500)
        slider.setValue(0)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(5)
        slider.setSingleStep(5)

    def start_timer_d1(self, value):
        if value:
            self.label.setText(str(value) + " мс")
        else:
            value = self.slider.value()
        self.timer1.start(value)
        self.pushButton_Start_D1.setEnabled(False)
        self.pushButton_Stop_D1.setEnabled(True)

    def stop_timer_d1(self):
        self.timer1.stop()
        self.pushButton_Start_D1.setEnabled(True)
        self.pushButton_Stop_D1.setEnabled(False)

    def start_timer_d2(self, value):
        if value:
            self.label2.setText(str(value) + " мс")
        else:
            value = self.slider2.value()
        self.timer2.start(value)
        self.pushButton_Start_D2.setEnabled(False)
        self.pushButton_Stop_D2.setEnabled(True)

    def stop_timer_d2(self):
        self.timer2.stop()
        self.pushButton_Start_D2.setEnabled(True)
        self.pushButton_Stop_D2.setEnabled(False)

    def queue_table(self):
        line = random.randint(0, 9)  # Он же приоритет
        if self.MaxPriorities[line] < 10:
            column = self.MaxPriorities[line]
            item = str(random.randint(1, 10))
            self.tableWidget_queue.setItem(line, column, QTableWidgetItem(item))
            self.tableWidget_queue.item(line, column).setBackground(QColor(250, 250, 0))
            self.MaxPriorities[line] += 1
            self.data_table()

    def queue_table_2(self):
        # Ищем первую заполненную строку(приоритет)
        count = 0
        for i in range(9, -1, -1):
            if self.MaxPriorities[i] != 0:
                count = i

        # Смещаем элементы на одну позицию влево
        for col in range(self.MaxPriorities[count]):
            item = self.tableWidget_queue.item(count, col)
            next_item = self.tableWidget_queue.item(count, col + 1)
            if item and next_item:
                item.setText(next_item.text())

        # Очищаем последнюю колонку
        self.tableWidget_queue.setItem(count, self.MaxPriorities[count] - 1, QTableWidgetItem(""))
        if self.MaxPriorities[count] != 0:
            self.MaxPriorities[count] -= 1
            self.processed[count] += 1

        self.data_table()

    def data_table(self):
        count = 0
        for i in self.MaxPriorities:
            self.tableWidget_properties.setItem(count, 0, QTableWidgetItem(str(i)))
            count += 1

        count = 0
        for i in self.processed:
            self.tableWidget_properties.setItem(count, 1, QTableWidgetItem(str(i)))
            count += 1

        for i in range(self.tableWidget_properties.rowCount()):
            item = QTableWidgetItem(str(int(self.tableWidget_properties.item(i, 0).text()) + int(
                self.tableWidget_properties.item(i, 1).text())))
            self.tableWidget_properties.setItem(i, 2, item)

        # self.ui.tableWidget_queue.setColumnWidth(0, 120)
        # self.ui.tableWidget_queue.setColumnWidth(1, 50)

        # for item in self.tableWidget_queue.selectedItems():
        #     print(item.row(), item.column(), item.text())


# Initialize The App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()
