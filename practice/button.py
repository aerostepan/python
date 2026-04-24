import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.label = QLabel('Hello, PyQt5!', self)
        self.initUI()

    def initUI(self):
        self.button = QPushButton('Click Me', self)
        self.button.setGeometry(200, 200, 100, 50)
        self.button.setStyleSheet('background-color: lightblue; font-size: 16px;')
        self.button.clicked.connect(self.on_button_click)
        self.label.setGeometry(200, 100, 200, 50)  
        self.label.setStyleSheet('font-size: 18px; color: darkblue;')

    def on_button_click(self):
        self.button.setText('Clicked!')
        self.button.setStyleSheet('background-color: lightgreen; font-size: 16px;')
        self.button.setDisabled(True)


        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())