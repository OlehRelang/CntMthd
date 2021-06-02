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

from lab6_stuff.ui_splash_screen6 import Ui_SplashScreen

from lab6_stuff.ui_lab6 import Ui_lab6

from py_expression_eval import Parser


class TableView(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setData(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)


class MainWindow(QMainWindow):
    a = 0
    b = 0
    fx = ""
    x0 = 0
    y0 = 0
    x = []
    y = []
    h = 0.1
    parser = Parser()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_lab6()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("border-radius: 10px; "
                           "background-color: rgb(38, 41, 45);"
                           )

        self.ui.pushButton_close.clicked.connect(app.exit)
        self.ui.pushButton_exp.clicked.connect(self.showMinimized)

        self.ui.pushButtonTo1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButtonTo2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))

        self.ui.pushButtonBack1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButtonBack2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        self.ui.pushButtonEval1.clicked.connect(self.calculate1)
        self.ui.pushButtonEval2.clicked.connect(self.calculate2)

        self.show()

    def calculate1(self):
        self.a = float(self.ui.a_meth1.text())
        self.b = float(self.ui.b_meth1.text())
        self.x0 = float(self.ui.x0_meth1.text())
        self.y0 = float(self.ui.y0_meth1.text())
        self.fx = self.ui.function_meth1.text()

        self.x = np.arange(self.a, self.b + self.h, self.h)
        self.y = np.zeros(len(self.x))
        self.y[0] = self.y0

        for i in range(1, len(self.x)):
            self.y[i] = self.y[i - 1] + self.h * float(self.parser.parse(self.fx).evaluate({'x': self.x[i - 1],
                                                                                            'y': self.y[i - 1]}))
        self.y = np.around(self.y, decimals=4)
        self.x = np.around(self.x, decimals=1)
        print(self.x)
        print(self.y)

        self.buildTable()

        if self.ui.radioButton1.isChecked():
            self.buildPlot()

    def calculate2(self):
        self.a = float(self.ui.a_meth2.text())
        self.b = float(self.ui.b_meth2.text())
        self.x0 = float(self.ui.x0_meth2.text())
        self.y0 = float(self.ui.y0_meth2.text())
        self.fx = self.ui.function_meth2.text()

        self.x = np.arange(self.a, self.b + self.h, self.h)
        self.y = np.zeros(len(self.x))
        self.y[0] = self.y0

        for i in range(1, len(self.x)):
            fxiyi = self.parser.parse(self.fx).evaluate({'x': self.x[i - 1], 'y': self.y[i - 1]})
            self.y[i] = self.y[i - 1] + self.h/2 * (fxiyi + self.parser.parse(self.fx).evaluate(
                                                                   {'x': self.x[i], 'y': self.y[i - 1] + self.h*fxiyi}
                                                                                               ))
        self.y = np.around(self.y, decimals=4)
        self.x = np.around(self.x, decimals=1)
        print(self.x)
        print(self.y)

        self.buildTable()

        if self.ui.radioButton2.isChecked():
            self.buildPlot()

    def buildTable(self):
        data = {'x': list(map(str, self.x)), 'y': list(map(str, self.y))}
        table = TableView(data, len(self.x), 2)
        table.setGeometry(100, 100, 150, 350)
        table.show()
        self.table = table

    def buildPlot(self):
        plt.plot(self.x, self.y, 'ko', self.x, self.y, 'k-')
        plt.axis([min(self.x) - self.h, max(self.x) + self.h, min(0, min(self.y)), max(self.y) + self.h])
        plt.title("Y = Y(x)")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()

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
