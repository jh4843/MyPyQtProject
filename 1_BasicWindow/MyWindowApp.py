import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super(MyApp, self).__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle('My First Window Application')
        self.setWindowIcon(QIcon('love.png'))
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())