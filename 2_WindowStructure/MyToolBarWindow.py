import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        openAction = QAction(QIcon('..\\icon\\open.png'), 'Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open File')
        openAction.triggered.connect(self.OpenFiles)

        exitAction = QAction(QIcon('..\\icon\\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('Open')
        self.toolbar.addAction(openAction)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    # Add & Write in the file(.\\OutFile\\New File.txt)
    def OpenFiles(self):

        ## path for output file.
        dir_path = '.\\OutFile'

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        ## create and write to file
        f = open(".\\OutFile\\New File.txt", 'w')
        for i in range(1, 11):
            data = "%d번째 줄입니다.\n" % i
            f.write(data)
        f.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())