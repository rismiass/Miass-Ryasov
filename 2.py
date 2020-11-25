import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
from random import randint
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(Ui_MainWindow)
        self.pushButton.clicked.connect(self.run)
        self.flag = 0

    def run(self):
        self.flag = 1

    def paintEvent(self, event):
        if self.flag == 1:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.drawEllipse(200, 200, randint(10, 100), randint(10, 100))
            qp.end()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
