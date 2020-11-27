import sqlite3
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from main_ui import Ui_MainWindow
from add import Ui_window


class MyWidget(QMainWindow, Ui_MainWindow, Ui_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.title = ''
        self.country = ''
        self.taste = ''
        self.flaver = ''
        self.table()
        self.pushButton_2.clicked.connect(self.add)

    def add(self):
        self.dasupUi(self)
        self.title = self.lineEdit_2.text()
        self.country = self.lineEdit_3.text()
        self.taste = self.lineEdit_4.text()
        self.flaver = self.lineEdit_5.text()
        self.pushButton_3.clicked.connect(self.reove)

    def reove(self):
        if self.title:
            self.con.cursor().execute(f"""INSERT INTO cofe(*) VALUES('{self.title}', '{self.country}', '{self.taste}', 
            '{self.flaver}')""")
        self.con.commit()
        self.con.close()
        self.setupUi(self)
        self.table()

    def table(self):
        self.con = sqlite3.connect("data/coffee.sqlite")
        cur = self.con.cursor()
        result = cur.execute(f"""
                                    SELECT * FROM cofe""").fetchall()
        self.tableWidget.setRowCount(len(result))

        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название', 'страна', 'вкус', 'аромат'])


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
