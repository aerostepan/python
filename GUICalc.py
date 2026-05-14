from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout
from PyQt5.QtCore import QSize, Qt
import sys


#DONE Need to be able to click the buttons and have the label update to show the button that was clicked.
#DONE Need to add button for arithmetic operations and have the label update to show the operation that was clicked.
#Need to be able to click the buttons in a sequence and have the label update to show the sequence of buttons that were clicked.
#DONE Need to add functionality to operation buttons
#DONE Need to be able to click the equals button and have the label update to show the result of the calculation.
#DONE Need to add reset button to clear the label and reset the calculator.


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt5 Calculator")

        self.label = QLabel("0")
        self.expression = ""

        positions = [

    (1,0), (1,1), (1,2),

    (2,0), (2,1), (2,2),

    (3,0), (3,1), (3,2)
                    ]
        layout = QGridLayout()
        
        for num, position in zip(range(1,10), positions):
            button = QPushButton(str(num))
            button.clicked.connect(lambda _, value=num: self.button_clicked(value))
            setattr(self, f"button{num}", button)
            layout.addWidget(button, *position)

        self.button0 = QPushButton("0")
        self.button0.clicked.connect(lambda: self.button_clicked(0))#
        layout.addWidget(self.button0, 4, 1)

        self.buttonEquals = QPushButton("=")
        self.buttonEquals.clicked.connect(lambda: self.button_clicked("="))
        layout.addWidget(self.buttonEquals, 4, 0)

        self.buttonAdd = QPushButton("+")
        self.buttonAdd.clicked.connect(lambda: self.button_clicked("+"))
        layout.addWidget(self.buttonAdd, 1, 3)

        self.buttonSubtract = QPushButton("-")
        self.buttonSubtract.clicked.connect(lambda: self.button_clicked("-")) 
        layout.addWidget(self.buttonSubtract, 2, 3)

        self.buttonMultiply = QPushButton("*")
        self.buttonMultiply.clicked.connect(lambda: self.button_clicked("*"))
        layout.addWidget(self.buttonMultiply, 3, 3)

        self.buttonDevide = QPushButton("/")
        self.buttonDevide.clicked.connect(lambda: self.button_clicked("/"))
        layout.addWidget(self.buttonDevide, 4, 3)

        self.buttonReset = QPushButton("C")
        self.buttonReset.clicked.connect(self.reset)
        layout.addWidget(self.buttonReset, 0, 3)



        layout.addWidget(self.label, 0, 1)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        

    def button_clicked(self, value):
        if value == "=":
            self.calculate()
            return
        sender = self.sender()
        self.expression += str(value)
        self.label.setText(self.expression)

    def reset(self):
        self.expression = ""
        self.label.setText("0")

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.label.setText(self.expression)
        except:
            self.label.setText("Error")
            self.expression = ""



    
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()