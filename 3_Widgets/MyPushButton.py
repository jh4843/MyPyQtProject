import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        ## Add Toggle Button
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        ## Add QPushButton having clicked event
        btn2 = QPushButton(self)
        btn2.setText('Button&2')
        btn2.clicked.connect(self.btn2_clicked)

        ## Add disabled button
        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        ## Align buttons vertically
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('My PushButtons')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def btn2_clicked(self):
        msgboxReply = QMessageBox.question(self, 'Message', 'Do you like me?',
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if msgboxReply == QMessageBox.Yes:
            msgboxInfo = QMessageBox(self)
            msgboxInfo.setText("Me too")
            msgboxInfo.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())