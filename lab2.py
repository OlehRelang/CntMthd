import sys, time
import numpy as np
import platform
import matplotlib.pyplot as plt
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from lab2_stuff.ui_splash_screen import Ui_SplashScreen

from lab2_stuff.ui_lab2 import Ui_Lab2


class MainWindow(QMainWindow):
    xx = 0
    x = []
    y = []
    res = []

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Lab2()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.setWindowTitle("Лабораторна робота №2")

        # self.setWindowIcon(QtGui.QIcon('symbol_sum.png'))
        self.setStyleSheet("border-radius: 10px; "
                           "background-color: rgb(38, 41, 45);"
                           )

        self.ui.pushButton1.clicked.connect(self.click1)
        self.ui.pushButton2.clicked.connect(self.click2)
        self.ui.pushButton_close.clicked.connect(app.exit)
        self.ui.pushButton_exp.clicked.connect(self.showMinimized)

    def mousePressEvent(self, event):

        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):

        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def click1(self):
        self.x.clear()
        self.y.clear()
        self.res = np.zeros((4,), dtype=float)
        try:
            self.x.append(float(self.ui.lineEdit_0.text()))
            self.x.append(float(self.ui.lineEdit_1.text()))
            self.x.append(float(self.ui.lineEdit_2.text()))
            self.x.append(float(self.ui.lineEdit_3.text()))

            self.y.append(float(self.ui.lineEdit_4.text()))
            self.y.append(float(self.ui.lineEdit_5.text()))
            self.y.append(float(self.ui.lineEdit_6.text()))
            self.y.append(float(self.ui.lineEdit_7.text()))
        except ValueError:
            self.show_message(self, "Invalid input!")
            return

        self.calc()

        if self.ui.radioButton.isChecked():
            x = np.arange(-3, 1.5, 0.1)
            y = self.res[0]*x**3 + self.res[1]*x**2 + self.res[2]*x + self.res[3]
            plt.plot(x, y)
            plt.grid(True)
            plt.show()

    def calc_nom(self, x):
        return np.array([1, -1*(x[0] + x[1] + x[2]), (x[0]*x[1] + x[0]*x[2] + x[1]*x[2]), -1*(x[0]*x[1]*x[2])])

    def calc_denom(self, xi, x):
        return (xi - x[0])*(xi - x[1])*(xi - x[2])

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

    def calc(self):
        for i in range(4):
            x = self.x.copy()
            xi = x.pop(i)
            self.res += self.calc_nom(x) * (self.y[i] / self.calc_denom(xi, x))
        print(self.res)
        self.printPolynomial(self.res)

    def printPolynomial(self, res):
        self.ui.label_result1.setStyleSheet("color: white; "
                                            "background-color: rgb(60, 13, 107); "
                                            "border-radius: 10px;"
                                            "font: Segoe UI;"
                                            "font-size: 12px;")
        self.ui.label_result1.setText(f"{round(res[0], 3)}" + "x³ "
                                      f"{'+ ' + str(round(res[1], 3)) if res[1] > 0 else '- ' + str(-round(res[1], 3))}" + "x² "
                                      f"{'+ ' + str(round(res[2], 3)) if res[2] > 0 else '- ' + str(-round(res[2], 3))}" + "x "
                                      f"{'+ ' + str(round(res[3], 3)) if res[3] > 0 else '- ' + str(-round(res[3], 3))}")
        print(self.ui.label_result1.text())

    def click2(self):
        try:
            self.xx = float(self.ui.lineEdit_9.text())
        except ValueError:
            self.show_message(self, "Invalid input!")
            return
        res = self.res[0]*self.xx**3 + self.res[1]*self.xx**2 + self.res[2]*self.xx + self.res[3]
        self.ui.label_result2.setText(f"{res:.3f}")


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
