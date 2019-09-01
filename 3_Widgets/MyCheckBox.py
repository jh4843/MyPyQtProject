import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QCheckBox, QVBoxLayout, QStatusBar

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):

        ## Make 3 checkboxes
        self.checkBox1 = QCheckBox("Apple", self)
        self.checkBox2 = QCheckBox("Banana", self)
        self.checkBox3 = QCheckBox("Grape", self)

        ## Connect checkboxState function
        self.checkBox1.stateChanged.connect(self.checkBoxState)
        self.checkBox2.stateChanged.connect(self.checkBoxState)
        self.checkBox3.stateChanged.connect(self.checkBoxState)

        ## checkBox3 has three state
        self.checkBox3.setTristate(True)

        ## Arrange checkboxes using VBoxLayout
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.checkBox1)
        self.vbox.addWidget(self.checkBox2)
        self.vbox.addWidget(self.checkBox3)


        ## Use QWidget class to arrange CentralWidget
        widget = QWidget()
        widget.setLayout(self.vbox)

        self.setCentralWidget(widget)
        self.setGeometry(400, 200, 500, 400)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
        self.setWindowTitle("MyCheckBox Window")

        self.show()

    def checkBoxState(self):
        msg = ""
        if self.checkBox1.isChecked() == True:
            msg += "Apple "
        if self.checkBox2.isChecked() == True:
            msg += "Banana "
        if self.checkBox3.isChecked() == True:
            msg += "Grape "

        if msg != "":
            msg = "checked " + msg

        self.statusBar.showMessage(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    sys.exit(app.exec_())
