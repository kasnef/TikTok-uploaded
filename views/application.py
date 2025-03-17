import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Action Tracker")
        self.setMinimumSize(640, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.description_label = QLabel("Description:")
        self.description_input = QLineEdit()
        self.layout.addWidget(self.description_label)
        self.layout.addWidget(self.description_input)

        self.wait_time_label = QLabel("Wait Time:")
        self.wait_time_input = QLineEdit()
        self.layout.addWidget(self.wait_time_label)
        self.layout.addWidget(self.wait_time_input)

        self.processes_label = QLabel("Number of Processes:")
        self.processes_input = QLineEdit()
        self.layout.addWidget(self.processes_label)
        self.layout.addWidget(self.processes_input)

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.pause_button = QPushButton("Pause")
        self.add_task_button = QPushButton("Add New Task")

        self.start_button.clicked.connect(self.start_action)
        self.stop_button.clicked.connect(self.stop_action)
        self.pause_button.clicked.connect(self.pause_action)
        self.add_task_button.clicked.connect(self.add_task)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.start_button)
        self.button_layout.addWidget(self.stop_button)
        self.button_layout.addWidget(self.pause_button)
        self.button_layout.addWidget(self.add_task_button)
        self.layout.addLayout(self.button_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(6)  # Added one column for counting numbers
        self.table.setHorizontalHeaderLabels(["ID", "Name", "User", "Action", "Check", "Counting Numbers"])
        self.layout.addWidget(self.table)

        self.counting_timer = QTimer()
        self.counting_timer.timeout.connect(self.update_counting_numbers)

    def start_action(self):
        id = random.randint(100, 9999999)
        name = "Counting Numbers"
        user = "Fish"
        action = "counting numbers"
        check = "active"

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(str(id)))
        self.table.setItem(row_position, 1, QTableWidgetItem(name))
        self.table.setItem(row_position, 2, QTableWidgetItem(user))
        self.table.setItem(row_position, 3, QTableWidgetItem(action))
        self.table.setItem(row_position, 4, QTableWidgetItem(check))
        self.table.setItem(row_position, 5, QTableWidgetItem("0"))  # Initialize counting numbers to 0

        self.counting_timer.start(1000)  # Update counting numbers every second

    def stop_action(self):
        selected_row = self.table.currentRow()
        if selected_row != -1:
            self.table.item(selected_row, 4).setText("stopped")
            self.counting_timer.stop()  # Stop counting when action is stopped

    def pause_action(self):
        self.counting_timer.stop()  # Pause counting

    def update_counting_numbers(self):
        for row in range(self.table.rowCount()):
            if self.table.item(row, 4).text() == "active":
                current_count = int(self.table.item(row, 5).text())
                self.table.item(row, 5).setText(str(current_count + 1))

    def add_task(self):
        id = random.randint(100, 9999999)
        name = "Counting Numbers"
        user = "Fish"
        action = "counting numbers"
        check = "active"

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(str(id)))
        self.table.setItem(row_position, 1, QTableWidgetItem(name))
        self.table.setItem(row_position, 2, QTableWidgetItem(user))
        self.table.setItem(row_position, 3, QTableWidgetItem(action))
        self.table.setItem(row_position, 4, QTableWidgetItem(check))
        self.table.setItem(row_position, 5, QTableWidgetItem("0"))  # Initialize counting numbers to 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
