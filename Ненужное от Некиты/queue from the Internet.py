from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self. next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self. tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return data
        else:
            return None

    def front(self):
        if self.head is not None:
            return self.head.data
        else:
            return None

    def is_empty(self):
        return self.head is None

    def display(self, scene):
        pen = QPen(QColor(0, 255, 0))
        font = QFont("Arial", 10)
        y = 100
        current_node = self.head
        while current_node is not None:
            # Draw node rectangle
            scene. addRect(50, y, 50, 50, pen)
            # Draw node text
            text = scene.addText(str(current_node.data), font)
            text.setDefaultTextColor(QColor(255, 255, 255))
            text.setPos(70, y + 10)
            current_node = current_node.next
            y+=70


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Queue Demo")
        self. setFixedSize(500, 500)

        self. scene = QGraphicsScene(self)
        self. view = QGraphicsView(self. scene, self)
        self. view. setGeometry(0, 0, 500, 500)

        self. queue = Queue()
        self. queue. enqueue(10)
        self. queue. enqueue(20)
        self. queue. enqueue(30)

        self. queue. display(self. scene)

        # Add UI elements
        enqueue_button = QPushButton("Enqueue", self)
        enqueue_button. move(10, 10)
        enqueue_button.clicked.connect(self.handle_enqueue)

        dequeue_button = QPushButton("Dequeue", self)
        dequeue_button. move(10, 40)
        dequeue_button.clicked.connect(self.handle_dequeue)

        front_button = QPushButton("Front", self)
        front_button. move(10, 70)
        front_button.clicked.connect(self.handle_front)

        clear_button = QPushButton("Clear", self)
        clear_button. move(10, 100)
        clear_button.clicked.connect(self.handle_clear)

        self. data_edit = QLineEdit(self)
        self. data_edit. move(100, 10)

    def handle_enqueue(self):
        data = self. data_edit. text()
        if data != "":
            self. queue. enqueue(data)
            self. scene. clear()
            self. queue. display(self. scene)

    def handle_dequeue(self):
        data = self. queue. dequeue()
        if data is not None:
            QMessageBox. information(self, "Dequeue", "Dequeued value: " + str(data))
            self. scene. clear()
            self. queue. display(self. scene)
        else:
            QMessageBox. warning(self, "Dequeue", "Queue is empty")

    def handle_front(self):
        data = self. queue. front()
        if data is not None:
            QMessageBox. information(self, "Front", "Front value: " + str(data))
        else:
            QMessageBox. warning(self, "Front", "Queue is empty")

    def handle_clear(self):
        self. queue = Queue()
        self. scene. clear()


if __name__ == "__main__":
    app = QApplication(sys. argv)
    window = MainWindow()
    window. show()
    sys. exit(app. exec_())