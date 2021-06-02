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

from lab5_stuff.ui_splash_screen5 import Ui_SplashScreen

from lab5_stuff.ui_lab5 import Ui_lab5

from py_expression_eval import Parser

from sympy import *


class MainWindow(QMainWindow):
    fx = ""
    x1 = 0
    x2 = 0
    parser = Parser()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_lab5()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("border-radius: 10px; "
                           "background-color: rgb(38, 41, 45);"
                           )

        self.ui.pushButton_close.clicked.connect(app.exit)
        self.ui.pushButton_exp.clicked.connect(self.showMinimized)
        self.ui.pushButtonEval.clicked.connect(self.calculate)

        self.show()

    def newton(self, x, d1fx):
        xn = [x[0]]
        fx = self.parser.parse(self.fx).evaluate({'x': x[0]})
        dfx = self.parser.parse(d1fx).evaluate({'x': x[0]})
        xn.append(xn[0] - fx/dfx)
        print(xn[0], fx, dfx)

        while abs(xn[-1] - xn[-2]) > 0.0001:
            fx = self.parser.parse(self.fx).evaluate({'x': xn[-1]})
            dfx = self.parser.parse(d1fx).evaluate({'x': xn[-1]})
            xn.append(xn[-1] - fx / dfx)
            print(xn[-2], fx, dfx)

        return round(xn[-1], 4)

    def bisection(self, x):
        a = x[0]
        b = x[-1]
        xn = (a + b)/2
        print(a, b, float(xn))

        while abs(a - b) > 0.0002:
            if self.parser.parse(self.fx).evaluate({'x': xn}) > 0:
                b = xn
            else:
                a = xn
            xn = (a + b)/2
            print(float(a), float(b), float(xn))

        return round(xn, 4)

    def calculate(self):
        self.fx = self.ui.equasion.text()
        x = Symbol('x')
        dfx = diff(self.fx)
        res = list(solveset(dfx, domain=S.Reals))
        x1 = [min(res) - 1, min(res)]
        x2 = [max(res), max(res) + 1]

        while True:
            if self.parser.parse(self.fx).evaluate({'x': x2[0]}) * self.parser.parse(self.fx).evaluate({'x': x2[1]}) < 0:
                break
            else:
                x2[0] = x2[1]
                x2[1] += 1

        self.ui.label_x1.setStyleSheet("color: rgb(255, 255, 255);"
                                       "background-color: rgb(38, 41, 45);")
        self.ui.label_x2.setStyleSheet("color: rgb(255, 255, 255);"
                                       "background-color: rgb(38, 41, 45);")
        self.ui.label_x1.setText(str(self.newton(x1, str(dfx))))
        self.ui.label_x2.setText(str(self.bisection(x2)))

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
