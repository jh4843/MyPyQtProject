import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QStatusBar

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Window Title 설정
        self.setWindowTitle('Statusbar')
        ## 위치, 크기 를 기존 move(), resize()로 사용하던것을 하나의 함수로 통합사용
        self.setGeometry(300, 300, 500, 300)

        # LineEdit 설정
        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(20, 20)
        ## textChanged Signal이 발생되었을 때, 내가 정의한 아래 함수가 호출될수 있도록 연결해 준다.
        self.lineEdit.textChanged.connect(self.lineeditTextChanged)

        # StatusBar 설정
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
        ##  초기 값은 Ready 로 표시되도록 한다.
        self.statusBar.showMessage('Ready')

    ## lineedit 의 Text가 변경되었을때, 호출되는 함수를 정의
    def lineeditTextChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
