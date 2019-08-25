import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 200)

        self.labelName = QLabel("Name: ")
        self.labelAge = QLabel("Age: ")
        self.labelSex = QLabel("Sex: ")
        self.labelEditName = QLineEdit()
        self.lineEditAge = QLineEdit()
        self.lineEditSex = QLineEdit()
        self.buttonReg= QPushButton("Register")

        layout = QGridLayout()


        ##layout.setRowStretch(0, 70)
        ##layout.setRowStretch(0, 100)

        ## First row: a name label and lableEdit
        layout.addWidget(self.labelName, 0, 0)
        layout.addWidget(self.labelEditName, 0, 1)

        ## Second row: a Age label and lableEdit
        layout.addWidget(self.labelAge, 1, 0)
        layout.addWidget(self.lineEditAge, 1, 1)

        ## Third row: a Sex label and lableEdit
        layout.addWidget(self.labelSex, 2, 0)
        layout.addWidget(self.lineEditSex, 2, 1)

        ## Fourth row: Register button
        layout.addWidget(self.buttonReg, 3, 0)

        self.setWindowTitle('Grid Layout')
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()