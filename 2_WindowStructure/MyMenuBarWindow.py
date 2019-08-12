import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        ## Set Action for Open
        openAction = QAction(QIcon('..\\icon\\open.png'), 'Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open Files')
        openAction.triggered.connect(self.OpenFiles)

        ## Set Action for quit
        exitAction = QAction(QIcon('..\\icon\\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        ## Set Menu Bar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        ### Add menu to File
        fileMenu = menubar.addMenu('&File')
        #### Add Open action to menu bar
        fileMenu.addAction(openAction)
        #### Add Separator to menu bar
        fileMenu.addSeparator()
        #### Add exit action to menu bar
        fileMenu.addAction(exitAction)


        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    # Add & Write in the file(.\\OutFile\\New File.txt)
    def OpenFiles(self):

        ## path for output file.
        dir_path ='.\\OutFile'

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