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

from lab4_stuff.ui_splash_screen4 import Ui_SplashScreen

from lab4_stuff.ui_lab4 import Ui_lab4

from py_expression_eval import Parser


class MainWindow(QMainWindow):
    a = 0
    b = 0
    n = 0
    h = 0
    fx = ""
    res = 0
    parser = Parser()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_lab4()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("border-radius: 10px; "
                           "background-color: rgb(38, 41, 45);"
                           )

        self.ui.pushButton_close.clicked.connect(self.close)
        self.ui.pushButton_exp.clicked.connect(self.showMinimized)

        self.ui.pushButtonBack1.clicked.connect(self.back)
        self.ui.pushButtonBack2.clicked.connect(self.back)
        self.ui.pushButtonBack3.clicked.connect(self.back)

        self.ui.pushButtonTo1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButtonTo2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButtonTo3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))

        self.ui.pushButtonEval1.clicked.connect(self.firstMethod)
        self.ui.pushButtonEval2.clicked.connect(self.secondMethod)
        self.ui.pushButtonEval3.clicked.connect(self.thirdMethod)

        self.show()

    def firstMethod(self):
        self.a = float(self.ui.a1.text())
        self.b = float(self.ui.b1.text())
        self.n = float(self.ui.n1.text())
        self.fx = self.ui.function_meth1.text()

        self.h = (self.b - self.a)/self.n

        x = np.arange(self.a, self.b + 0.0001, self.h)

        y = []
        for i in x:
            y.append(round(self.parser.parse(self.fx).evaluate({'x': i}), 4))
        print(f"{x}\n{y}")
        self.res = round(self.h * sum(y[:-1]), 4)
        res = "\n"

        res += str(self.res) + "(ліві)\n"

        self.res = round(self.h * sum(y[1:]), 4)
        res += str(self.res) + "(праві)\n"

        x += self.h/2
        x = x[:-1]
        y = []
        for i in x:
            y.append(round(self.parser.parse(self.fx).evaluate({'x': i}), 4))
        print(f"{x}\n{y}")
        self.res = round(self.h * sum(y), 4)
        res += str(self.res) + "(середні)\n"

        self.ui.label_result1.setStyleSheet("color: rgb(255, 255, 255);"
                                            "background-color: rgb(23, 25, 28);"
                                            "border-radius: 10px;"
                                            "font-size: 16px;")
        self.ui.label_result1.setText(res)

    def secondMethod(self):
        self.a = float(self.ui.a2.text())
        self.b = float(self.ui.b2.text())
        self.n = float(self.ui.n2.text())
        self.fx = self.ui.function_meth2.text()

        self.h = (self.b - self.a) / self.n

        x = np.arange(self.a, self.b + 0.0001, self.h)
        y = []
        for i in x:
            y.append(round(self.parser.parse(self.fx).evaluate({'x': i}), 4))
        print(f"{x}\n{y}")

        self.res = round(self.h/3 * (y[0] + y[-1] + 4*sum(y[1:-1:2]) + 2*sum(y[2:-2:2])), 4)

        self.ui.label_result2.setStyleSheet("color: rgb(255, 255, 255);"
                                            "background-color: rgb(23, 25, 28);"
                                            "border-radius: 10px;"
                                            "font-size: 26px;")
        self.ui.label_result2.setText(str(self.res))

    def thirdMethod(self):
        self.a = float(self.ui.a2_2.text())
        self.b = float(self.ui.b2_2.text())
        self.n = float(self.ui.n3.text())
        self.fx = self.ui.function_meth3.text()

        self.h = (self.b - self.a) / self.n

        x = np.arange(self.a, self.b + 0.0001, self.h)
        y = []
        for i in x:
            y.append(round(self.parser.parse(self.fx).evaluate({'x': i}), 4))
        print(f"{x}\n{y}")

        print((y[0] + y[-1])/2)
        print(sum(y[1:-2]))
        self.res = round(self.h*((y[0] + y[-1])/2 + sum(y[1:-1])), 4)

        self.ui.label_result3.setStyleSheet("color: rgb(255, 255, 255);"
                                            "background-color: rgb(23, 25, 28);"
                                            "border-radius: 10px;"
                                            "font-size: 26px;")
        self.ui.label_result3.setText(str(self.res))

    def back(self):
        self.ui.stackedWidget.setCurrentIndex(0)

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
