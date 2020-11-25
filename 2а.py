import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import random
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.flag = 0

    def run(self):
        self.flag = 1

    def paintEvent(self, event):
        if self.flag == 1:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 215, 0))
            qp.drawEllipse(200, 200, random.randint(10, 100),  random.randint(10, 100))
            qp.end()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
