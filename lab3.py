import sys, time, csv, os
import numpy as np
import platform
import matplotlib.pyplot as plt
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from lab3_stuff.ui_splash_screen3 import Ui_SplashScreen

from lab3_stuff.ui_lab3 import Ui_Lab3


class MainWindow(QMainWindow):
    x = []
    y = []
    table = []
    h = 0
    q = 0
    point = 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Lab3()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("border-radius: 10px; "
                           "background-color: rgb(38, 41, 45);"
                           )

        self.ui.pushButton_close.clicked.connect(self.close)
        self.ui.pushButton_exp.clicked.connect(self.showMinimized)

        self.ui.pushButton_left.clicked.connect(self.left)
        self.ui.pushButton_right.clicked.connect(self.right)
        self.ui.pushButton2.clicked.connect(self.takeAction)

        self.setAcceptDrops(True)

        self.show()

    def left(self):
        self.ui.stackedWidget.setCurrentIndex((self.ui.stackedWidget.currentIndex() - 1) % 3)

    def right(self):
        self.ui.stackedWidget.setCurrentIndex((self.ui.stackedWidget.currentIndex() + 1) % 3)

    def calc(self, lst):
        res = []
        for i in range(len(lst) - 1):
            res.append(round(round(lst[i], 3) - round(lst[i + 1], 3), 3))
        return res

    def make_table(self, y):
        y = y[::-1]
        rs = []
        for i in range(len(y) - 1):
            y = self.calc(y)
            rs.append(y[::-1])
        return rs

    def dragEnterEvent(self, event):
        self.ui.stackedWidget.setCurrentIndex(2)
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        self.ui.label_3.setText(f"Table uploaded\n {os.path.split(files[0])[1]}")
        with open(files[0], 'r') as f:
            readed = csv.reader(f)
            lst = list(readed)
            self.x = list(map(float, lst[0]))
            self.y = list(map(float, lst[1]))

    def printTable(self, table):
        for i in table:
            print(i)

    def takeAction(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            self.x = list(np.arange(2.4, 4.8, 0.2))
            self.y = [3.526, 3.782, 3.945, 4.043, 4.104, 4.155, 4.222, 4.331, 4.507, 4.775, 5.159, 5.683]
        elif self.ui.stackedWidget.currentIndex() == 1:
            self.x = list(np.arange(1.5, 7.5, 0.5))
            self.y = [10.517, 10.193, 9.807, 9.387, 8.977, 8.637, 8.442, 8.482, 8.862, 9.701, 11.132, 13.302]

        self.table = self.make_table(self.y)
        self.printTable(self.table)
        self.h = self.x[1] - self.x[0]
        try:
            self.point = float(self.ui.lineEdit_input.text())
        except ValueError:
            self.show_message(self, "Invalid input!")
            return

        if self.point not in self.x:
            closest_value = min(self.x, key=lambda list_value: abs(list_value - self.point))
            if self.point < self.x[(len(self.x) - 1)//2]:
                if self.point - closest_value < 0:
                    closest_value -= self.h
                self.q = (self.point - closest_value)/self.h
                res1 = self.first_newton_first_derivative(self.q, self.x.index(closest_value))
                res2 = self.first_newton_second_derivative(self.q, self.x.index(closest_value))
                self.ui.label_result1.setText(str(round(res1, 3)))
                self.ui.label_result2.setText(str(round(res2, 3)))
            else:
                if self.point - closest_value > 0:
                    closest_value += self.h
                self.q = round((self.point - closest_value)/self.h, 3)
                res1 = self.second_newton_first_derivative(self.q, self.x.index(closest_value))
                res2 = self.second_newton_second_derivative(self.q, self.x.index(closest_value))
                self.ui.label_result1.setText(str(round(res1, 3)))
                self.ui.label_result2.setText(str(round(res2, 3)))
            print(closest_value)
            print(self.q)
        else:
            if self.point < self.x[(len(self.x) - 1)//2]:
                res1 = self.first_newton_first_derivative(0, self.x.index(self.point))
                res2 = self.first_newton_second_derivative(0, self.x.index(self.point))
                self.ui.label_result1.setText(str(round(res1, 3)))
                self.ui.label_result2.setText(str(round(res2, 3)))
            else:
                res1 = self.second_newton_first_derivative(0, self.x.index(self.point))
                res2 = self.second_newton_second_derivative(0, self.x.index(self.point))
                self.ui.label_result1.setText(str(round(res1, 3)))
                self.ui.label_result2.setText(str(round(res2, 3)))

    def first_newton_first_derivative(self, q, i):
        return 1/self.h*(self.table[0][i] + (2*q - 1)/2 * self.table[1][i] + (3*q**2 - 6*q + 2)/6 * self.table[2][i] +
                         (2*q**3 - 9*q**2 + 11*q - 3)/12 * self.table[3][i])

    def first_newton_second_derivative(self, q, i):
        return 1/self.h**2*(self.table[1][i] + (q - 1) * self.table[2][i] + (6*q**2 - 18*q + 11)/12 * self.table[3][i])

    def second_newton_first_derivative(self, q, i):
        return 1/self.h*(self.table[0][i - 1] + (2*q + 1)/2 * self.table[1][i - 2] + (3*q**2 + 6*q + 2)/6 *
                         self.table[2][i - 3] + (2*q**3 + 9*q**2 + 11*q + 3)/12 * self.table[3][i - 4])

    def second_newton_second_derivative(self, q, i):
        return 1/self.h**2*(self.table[1][i - 2] + (q + 1)*self.table[2][i - 3] +
                            (6*q**2 + 18*q + 11)/12 * self.table[3][i - 4])

    @staticmethod
    def show_message(self, text):
        msg = QMessageBox()
        msg.setText(text)
        msg.setWindowTitle("Info")
        msg.setIcon(QMessageBox.Warning)
        msg.setStyleSheet("background-color: rgb(38, 41, 58);"
                          "color: white;"
                          "font: Segoe UI;"
                          "font-size: 20px;")
        msg.setGeometry(650, 500, 1500, 1000)
        msg.exec_()

    def mousePressEvent(self, event):

        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):

        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


class SplashScreen(QMainWindow):
    counter = 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(18)

        # # Change Texts
        QtCore.QTimer.singleShot(550, lambda: self.ui.label_loading.setText("<strong>loading</strong> database..."))
        QtCore.QTimer.singleShot(1050,
                                 lambda: self.ui.label_loading.setText("<strong>loading</strong> user interface..."))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(self.counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if self.counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            time.sleep(1)
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        self.counter += 1


if __name__ == "__main__":
    app = QApplication.instance()
    if app == None:
        app = QApplication()
    window = SplashScreen()
    sys.exit(app.exec_())
