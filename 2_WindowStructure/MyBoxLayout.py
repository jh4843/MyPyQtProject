import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        ## Make three buttons
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        editButton = QPushButton('Edit')

        ## Make Upper Horizontal Box consisting of one button (Edit Button)
        hboxUp = QHBoxLayout()
        ## Make spaces (left: 2, right 2)
        hboxUp.addStretch(2)
        hboxUp.addWidget(editButton)
        hboxUp.addStretch(2)

        ## Make Upper Horizontal Box consisting of two buttons (Ok Button, Cancel Button)
        hboxDown = QHBoxLayout()
        ## Make spaces (left: 1, right 2)
        hboxDown.addStretch(1)
        hboxDown.addWidget(okButton)
        hboxDown.addWidget(cancelButton)
        hboxDown.addStretch(2)

        ## Make Vertical Box consisting of two horizontal boxes (hBoxUp, hBoxDown)
        vbox = QVBoxLayout()
        ## Make spaces (up: 2, down 1)
        vbox.addStretch(2)
        vbox.addLayout(hboxUp)
        vbox.addLayout(hboxDown)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 500, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())