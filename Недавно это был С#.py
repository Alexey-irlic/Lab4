import random
import tkinter as tk
from tkinter import ttk


class Form1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Form1")
        self.MaxPriorities = [[0 for _ in range(20)] for _ in range(10)]
        self.maxRequests = [[0 for _ in range(3)] for _ in range(10)]

        self.create_widgets()

    def create_widgets(self):
        # Create trackbar1
        trackbar1_label = tk.Label(self, text="Trackbar1:")
        trackbar1_label.grid(row=0, column=0)
        self.trackbar1 = ttk.Scale(self, from_=100, to=1000, orient=tk.HORIZONTAL, command=self.trackbar1_value_changed)
        self.trackbar1.grid(row=0, column=1)

        # Create dataGridView1
        dataGridView1_label = tk.Label(self, text="DataGridView1:")
        dataGridView1_label.grid(row=1, column=0)
        self.dataGridView1 = tk.Frame(self)
        self.dataGridView1.grid(row=1, column=1)
        for i in range(10):
            for j in range(20):
                cell = tk.Entry(self.dataGridView1, width=2)
                cell.grid(row=i, column=j)

        # Create buttons for dataGridView1
        btStartD1 = tk.Button(self, text="Start D1", command=self.btStartD1_Click)
        btStartD1.grid(row=2, column=0)
        btStopD1 = tk.Button(self, text="Stop D1", command=self.btStopD1_Click)
        btStopD1.grid(row=2, column=1)

        # Create dataGridView2
        dataGridView2_label = tk.Label(self, text="DataGridView2:")
        dataGridView2_label.grid(row=3, column=0)
        self.dataGridView2 = tk.Frame(self)
        self.dataGridView2.grid(row=3, column=1)
        for i in range(10):
            for j in range(3):
                cell = tk.Entry(self.dataGridView2, width=20)
                cell.grid(row=i, column=j)

        # Create buttons for dataGridView2
        btStartD2 = tk.Button(self, text="Start D2", command=self.btStartD2_Click)
        btStartD2.grid(row=4, column=0)
        btStopD2 = tk.Button(self, text="Stop D2", command=self.btStopD2_Click)
        btStopD2.grid(row=4, column=1)

        # Create trackbar2
        trackbar2_label = tk.Label(self, text="Trackbar2:")
        trackbar2_label.grid(row=5, column=0)
        self.trackbar2 = ttk.Scale(self, from_=10, to=100, orient=tk.HORIZONTAL, command=self.trackbar2_value_changed)
        self.trackbar2.grid(row=5, column=1)

        # Create labels
        self.label1 = tk.Label(self, text="")
        self.label1.grid(row=6, column=0)
        self.label2 = tk.Label(self, text="")
        self.label2.grid(row=6, column=1)

        # Create exit button
        exit_button = tk.Button(self, text="Exit", command=self.exit_app)
        exit_button.grid(row=7, column=0)

        # Initialize timer
        self.timer1 = None
        self.timer2 = None

    def trackbar1_value_changed(self, event):
        if self.timer1:
            self.after_cancel(self.timer1)
        interval = self.trackbar1.get()
        self.timer1 = self.after(interval, self.timer1_tick)

    def trackbar2_value_changed(self, event):
        if self.timer2:
            self.after_cancel(self.timer2)
        interval = self.trackbar2.get()
        self.timer2 = self.after(interval, self.timer2_tick)

    def btStartD1_Click(self):
        self.trackbar1_value_changed(None)

    def btStopD1_Click(self):
        if self.timer1:
            self.after_cancel(self.timer1)
            self.timer1 = None

    def btStartD2_Click(self):
        self.trackbar2_value_changed(None)

    def btStopD2_Click(self):
        if self.timer2:
            self.after_cancel(self.timer2)
            self.timer2 = None

    def timer1_tick(self):
        interval = self.trackbar1.get()
        self.label1.config(text=f"{interval} ms", visible=True)
        priorities = random.randint(0, 9)
        time = random.randint(1, 50)
        k = 0
        while self.MaxPriorities[priorities][k] != 0:
            k += 1
            if k == 20:
                break

        if k < 20:
            self.MaxPriorities[priorities][k] = time

        for i in range(10):
            for j in range(20):
                cell = self.dataGridView1.grid_slaves(row=i, column=j)[0]
                if self.MaxPriorities[i][j] != 0:
                    cell.delete(0, tk.END)
                    cell.insert(0, str(self.MaxPriorities[i][j]))
                else:
                    cell.delete(0, tk.END)

        for i in range(10):
            self.maxRequests[i][0] = sum(1 for j in range(20) if self.MaxPriorities[i][j] != 0)
            cell = self.dataGridView2.grid_slaves(row=i, column=0)[0]
            cell.delete(0, tk.END)
            cell.insert(0, str(self.maxRequests[i][0]))

        self.timer1 = self.after(interval, self.timer1_tick)

    def timer2_tick(self):
        interval = self.trackbar2.get()
        self.label2.config(text=f"{interval} ms", visible=True)
        for i in range(10):
            if self.MaxPriorities[i][0] != 0:
                self.MaxPriorities[i][0] -= 1
                cell = self.dataGridView1.grid_slaves(row=i, column=0)[0]
                cell.delete(0, tk.END)
                cell.insert(0, str(self.MaxPriorities[i][0]))
                if self.MaxPriorities[i][0] == 0:
                    self.maxRequests[i][1] += 1
                    self.maxRequests[i][0] -= 1
                    cell = self.dataGridView2.grid_slaves(row=i, column=1)[0]
                    cell.delete(0, tk.END)
                    cell.insert(0, str(self.maxRequests[i][1]))
                    cell = self.dataGridView2.grid_slaves(row=i, column=0)[0]
                    cell.delete(0, tk.END)
                    cell.insert(0, str(self.maxRequests[i][0]))
                    cell = self.dataGridView2.grid_slaves(row=i, column=2)[0]
                    cell.delete(0, tk.END)
                    cell.insert(0, str(self.maxRequests[i][0] + self.maxRequests[i][1]))
                    for j in range(19):
                        self.MaxPriorities[i][j] = self.MaxPriorities[i][j + 1]
                    self.MaxPriorities[i][19] = 0
                    cell = self.dataGridView1.grid_slaves(row=i, column=19)[0]
                    cell.delete(0, tk.END)
                    for j in range(19):
                        cell = self.dataGridView1.grid_slaves(row=i, column=j)[0]
                        if self.MaxPriorities[i][j] == 0:
                            cell.delete(0, tk.END)
                        else:
                            cell.delete(0, tk.END)
                            cell.insert(0, str(self.MaxPriorities[i][j]))
                break

        self.timer2 = self.after(interval, self.timer2_tick)

    def exit_app(self):
        self.quit()


if __name__ == "__main__":
    app = Form1()
    app.mainloop()
