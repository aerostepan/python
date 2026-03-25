import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.initUI()


    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("Number 1",self)
        label2 = QLabel("Number 2",self)
        label3 = QLabel("Number 3",self)
        label4 = QLabel("Number 4",self)
        label5 = QLabel("Number 5",self)

        label1.setAlignment(Qt.AlignCenter)
        label2.setAlignment(Qt.AlignCenter)
        label3.setAlignment(Qt.AlignCenter)
        label4.setAlignment(Qt.AlignCenter)
        label5.setAlignment(Qt.AlignCenter)

        label1.setStyleSheet("background-color: red")
        label2.setStyleSheet("background-color: orange")
        label3.setStyleSheet("background-color: green")
        label4.setStyleSheet("background-color: blue")
        label5.setStyleSheet("background-color: purple")

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()