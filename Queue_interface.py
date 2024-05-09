from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import random
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Загрузка файла пользовательского интерфейса
        uic.loadUi("Queue_02.ui", self)

        self.num_of_app = [0] * 10  # Хранение количества элементов каждой строки (приоритета)
        self.processed_applications = [0] * 10  # Количество обработанных заявок (для таблицы со статистикой)

        # Определение виджетов
        self.slider1 = self.findChild(QSlider, "horizontalSlider_D1")
        self.label1 = self.findChild(QLabel, "label_for_slader_D1")
        self.slider2 = self.findChild(QSlider, "horizontalSlider_D2")
        self.label2 = self.findChild(QLabel, "label_for_slader_D2")

        # Установка свойств ползунков
        self.slider_properties(self.slider1)
        self.slider_properties(self.slider2)

        # Создание таймеров
        self.timer1 = QTimer(self)
        self.timer2 = QTimer(self)

        # Подсоединение к первому таймеру кнопок старт/стоп и ползунка
        self.pushButton_Start_D1.clicked.connect(self.start_timer_d1)
        self.pushButton_Stop_D1.clicked.connect(self.stop_timer_d1)
        self.slider1.valueChanged.connect(self.start_timer_d1)

        # Подсоединение к второму таймеру кнопок старт/стоп и ползунка
        self.pushButton_Start_D2.clicked.connect(self.start_timer_d2)
        self.pushButton_Stop_D2.clicked.connect(self.stop_timer_d2)
        self.slider2.valueChanged.connect(self.start_timer_d2)

        # Таймеры подсоединяются к диспетчерам
        self.timer1.timeout.connect(self.d1)
        self.timer2.timeout.connect(self.d2)

        # Show The App
        self.show()

    def slider_properties(self, slider):
        slider.setMinimum(100)
        slider.setMaximum(1000)
        slider.setValue(0)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(50)
        slider.setSingleStep(50)

    def start_timer_d1(self, value):
        if value:
            self.label1.setText(str(value) + " мс")
        else:
            value = self.slider1.value()
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

    def d1(self):
        line = random.randint(0, 9)
        if self.num_of_app[line] < 10:
            column = self.num_of_app[line]
            item = str(random.randint(1, 10))
            self.tableWidget_queue.setItem(line, column, QTableWidgetItem(item))
            self.tableWidget_queue.item(line, column).setBackground(QColor(250, 232, 172))
            self.num_of_app[line] += 1

        # Обновляем статистику
        self.data_table()

    def d2(self):
        # Ищем первую заполненную строку(приоритет)
        priority = 0
        for i in range(9, -1, -1):
            if self.num_of_app[i] != 0:
                priority = i

        # Смещаем элементы на одну позицию влево
        for col in range(self.num_of_app[priority]):
            item = self.tableWidget_queue.item(priority, col)
            next_item = self.tableWidget_queue.item(priority, col + 1)
            if item and next_item:
                item.setText(next_item.text())

        # Очищаем последнюю колонку
        self.tableWidget_queue.setItem(priority, self.num_of_app[priority] - 1, QTableWidgetItem(""))
        if self.num_of_app[priority] != 0:
            self.num_of_app[priority] -= 1
            self.processed_applications[priority] += 1

        # Обновляем статистику
        self.data_table()

    def data_table(self):
        # Количество заявок в системе
        count = 0
        for i in self.num_of_app:
            self.tableWidget_properties.setItem(count, 0, QTableWidgetItem(str(i)))
            count += 1

        # Количество обработанных заявок
        count = 0
        for i in self.processed_applications:
            self.tableWidget_properties.setItem(count, 1, QTableWidgetItem(str(i)))
            count += 1

        # Общее количество заявок
        for i in range(self.tableWidget_properties.rowCount()):
            item = QTableWidgetItem(str(int(self.tableWidget_properties.item(i, 0).text()) + int(
                self.tableWidget_properties.item(i, 1).text())))
            self.tableWidget_properties.setItem(i, 2, item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()
