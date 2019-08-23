import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lbl1 = QLabel('Absolute Position', self)
        ## Move Label1 at x = 10px, y = 15px
        lbl1.move(10, 15)

        lbl2 = QLabel('tutorials', self)
        ## Move Label2 at x = 35px, y = 70px
        lbl2.move(35, 70)

        lbl3 = QLabel('for programmers', self)
        ## Move Label2 at x = 65px, y = 100px
        lbl3.move(65, 100)

        ## Create Window at x = 300px, y = 300 px, width = 400px, Height = 200px
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())