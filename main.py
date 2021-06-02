import sys, time, os
import numpy as np
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from main_stuff.ui_main_menu import Ui_MainMenu

from main_stuff.ui_prestart import Ui_MainWindow


class MainMenu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.pushButton_2.clicked.connect(self.start_lab_2)
        self.ui.pushButton_3.clicked.connect(self.start_lab_3)
        self.ui.pushButton_4.clicked.connect(self.start_lab_4)
        self.ui.pushButton_5.clicked.connect(self.start_lab_5)
        self.ui.pushButton_6.clicked.connect(self.start_lab_6)
        self.ui.pushButton_close.clicked.connect(app.exit)
        self.ui.pushButton_exp.clicked.connect(self.showMinimized)

        self.show()

    def mousePressEvent(self, event):

        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):

        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    @staticmethod
    def show_message(self):
        msg = QMessageBox()
        msg.setText("Work in progress!")
        msg.setWindowTitle("Info")
        msg.setIcon(QMessageBox.Information)
        # msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet("background-color: rgb(38, 41, 58);"
                          "color: white;"
                          "font: Segoe UI;"
                          "font-size: 20px;")
        msg.setGeometry(650, 500, 1500, 1000)
        msg.exec_()

    def start_lab_2(self):
        self.close()
        os.system('python lab2.py')

    def start_lab_3(self):
        self.close()
        os.system('python lab3.py')

    def start_lab_4(self):
        self.close()
        os.system('python lab4.py')

    def start_lab_5(self):
        self.close()
        os.system('python lab5.py')

    def start_lab_6(self):
        self.close()
        os.system('python lab6.py')


class PreStart(QMainWindow):
    i = 1

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.shown)
        # TIMER IN MILLISECONDS
        self.timer.start(12)
        self.show()

    def shown(self):
        if self.i > 254:
            self.timer.stop()
            print("done!")

            self.main = MainMenu()
            time.sleep(1)
            self.main.show()

            self.close()

        self.ui.label.setStyleSheet(f"color: rgba(255, 255, 255, {self.i})")
        self.ui.label_2.setStyleSheet(f"color: rgba(255, 255, 255, {self.i})")
        self.i += 1


if __name__ == "__main__":
    app = QApplication.instance()
    if app == None:
        app = QApplication()
    window = PreStart()
    sys.exit(app.exec_())
