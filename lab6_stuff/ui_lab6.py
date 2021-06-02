# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab6xfaZle.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_lab6(object):
    def setupUi(self, lab6):
        if lab6.objectName():
            lab6.setObjectName(u"lab6")
        lab6.resize(500, 637)
        lab6.setStyleSheet(u"background-color: rgb(38, 41, 45);")
        self.centralwidget = QWidget(lab6)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 501, 31))
        self.frame_header.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(28, 31, 35)")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_header)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 6, 148, 20))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"color:rgb(160, 160, 160)")
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_exp = QPushButton(self.frame_header)
        self.pushButton_exp.setObjectName(u"pushButton_exp")
        self.pushButton_exp.setGeometry(QRect(455, 8, 15, 15))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.pushButton_exp.setFont(font1)
        self.pushButton_exp.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_exp.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-radius: 7px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 111, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 153, 0);\n"
"}")
        self.pushButton_close = QPushButton(self.frame_header)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(480, 8, 16, 16))
        self.pushButton_close.setFont(font1)
        self.pushButton_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_close.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border-radius: 8px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(175, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(229, 0, 0);\n"
"}")
        self.label_task = QLabel(self.centralwidget)
        self.label_task.setObjectName(u"label_task")
        self.label_task.setGeometry(QRect(0, 40, 491, 121))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(True)
        font2.setWeight(50)
        self.label_task.setFont(font2)
        self.label_task.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_task.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 170, 501, 461))
        self.page_menu = QWidget()
        self.page_menu.setObjectName(u"page_menu")
        self.label_intro = QLabel(self.page_menu)
        self.label_intro.setObjectName(u"label_intro")
        self.label_intro.setGeometry(QRect(100, 10, 316, 62))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_intro.setFont(font3)
        self.label_intro.setLayoutDirection(Qt.LeftToRight)
        self.label_intro.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_intro.setFrameShape(QFrame.NoFrame)
        self.label_intro.setAlignment(Qt.AlignCenter)
        self.pushButtonTo1 = QPushButton(self.page_menu)
        self.pushButtonTo1.setObjectName(u"pushButtonTo1")
        self.pushButtonTo1.setGeometry(QRect(140, 140, 231, 61))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.pushButtonTo1.setFont(font4)
        self.pushButtonTo1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonTo1.setStyleSheet(u"QPushButton{\n"
"	border-style:  solid;\n"
"	border-radius: 20px;\n"
"	border-width: 5px;\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border-color:rgb(53, 61, 70);\n"
"	background-color: rgb(67, 72, 79);\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(99, 107, 117);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(47, 51, 56);\n"
"}\n"
"")
        self.pushButtonTo2 = QPushButton(self.page_menu)
        self.pushButtonTo2.setObjectName(u"pushButtonTo2")
        self.pushButtonTo2.setGeometry(QRect(140, 280, 231, 61))
        self.pushButtonTo2.setFont(font4)
        self.pushButtonTo2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonTo2.setStyleSheet(u"QPushButton{\n"
"	border-style:  solid;\n"
"	border-radius: 20px;\n"
"	border-width: 5px;\n"
"	color: rgba(255, 255, 255, 200);\n"
"	border-color:rgb(53, 61, 70);\n"
"	background-color: rgb(67, 72, 79);\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(99, 107, 117);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(47, 51, 56);\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.page_menu)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.b_meth1 = QLineEdit(self.page1)
        self.b_meth1.setObjectName(u"b_meth1")
        self.b_meth1.setGeometry(QRect(260, 200, 31, 21))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.b_meth1.setFont(font5)
        self.b_meth1.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);")
        self.b_meth1.setAlignment(Qt.AlignCenter)
        self.label_intro1 = QLabel(self.page1)
        self.label_intro1.setObjectName(u"label_intro1")
        self.label_intro1.setGeometry(QRect(96, 0, 331, 62))
        self.label_intro1.setFont(font3)
        self.label_intro1.setLayoutDirection(Qt.LeftToRight)
        self.label_intro1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_intro1.setFrameShape(QFrame.NoFrame)
        self.label_intro1.setAlignment(Qt.AlignCenter)
        self.radioButton1 = QRadioButton(self.page1)
        self.radioButton1.setObjectName(u"radioButton1")
        self.radioButton1.setGeometry(QRect(216, 270, 91, 21))
        self.radioButton1.setFont(font5)
        self.radioButton1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButtonEval1 = QPushButton(self.page1)
        self.pushButtonEval1.setObjectName(u"pushButtonEval1")
        self.pushButtonEval1.setGeometry(QRect(166, 310, 181, 51))
        font6 = QFont()
        font6.setFamily(u"Bodoni MT Black")
        font6.setPointSize(13)
        font6.setBold(True)
        font6.setWeight(75)
        self.pushButtonEval1.setFont(font6)
        self.pushButtonEval1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonEval1.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")
        self.label_2 = QLabel(self.page1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(186, 187, 141, 41))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(20)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_2.setFont(font7)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(28, 31, 35);")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.x0_meth1 = QLineEdit(self.page1)
        self.x0_meth1.setObjectName(u"x0_meth1")
        self.x0_meth1.setGeometry(QRect(216, 141, 38, 21))
        self.x0_meth1.setFont(font5)
        self.x0_meth1.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);")
        self.x0_meth1.setAlignment(Qt.AlignCenter)
        self.y0_meth1 = QLineEdit(self.page1)
        self.y0_meth1.setObjectName(u"y0_meth1")
        self.y0_meth1.setGeometry(QRect(295, 140, 41, 21))
        self.y0_meth1.setFont(font5)
        self.y0_meth1.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);")
        self.y0_meth1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label = QLabel(self.page1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(171, 135, 181, 31))
        self.label.setFont(font4)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setAlignment(Qt.AlignCenter)
        self.a_meth1 = QLineEdit(self.page1)
        self.a_meth1.setObjectName(u"a_meth1")
        self.a_meth1.setGeometry(QRect(221, 200, 31, 21))
        self.a_meth1.setFont(font5)
        self.a_meth1.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);")
        self.a_meth1.setAlignment(Qt.AlignCenter)
        self.function_meth1 = QLineEdit(self.page1)
        self.function_meth1.setObjectName(u"function_meth1")
        self.function_meth1.setGeometry(QRect(136, 80, 241, 31))
        self.function_meth1.setFont(font)
        self.function_meth1.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 10px;")
        self.function_meth1.setAlignment(Qt.AlignCenter)
        self.function_meth1.setPlaceholderText(u"y' = f(x,y)")
        self.pushButtonBack1 = QPushButton(self.page1)
        self.pushButtonBack1.setObjectName(u"pushButtonBack1")
        self.pushButtonBack1.setGeometry(QRect(190, 390, 131, 41))
        font8 = QFont()
        font8.setFamily(u"Bodoni MT Black")
        font8.setPointSize(11)
        font8.setBold(True)
        font8.setWeight(75)
        self.pushButtonBack1.setFont(font8)
        self.pushButtonBack1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonBack1.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")
        self.stackedWidget.addWidget(self.page1)
        self.label_intro1.raise_()
        self.radioButton1.raise_()
        self.pushButtonEval1.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.a_meth1.raise_()
        self.function_meth1.raise_()
        self.b_meth1.raise_()
        self.x0_meth1.raise_()
        self.y0_meth1.raise_()
        self.pushButtonBack1.raise_()
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.y0_meth2 = QLineEdit(self.page2)
        self.y0_meth2.setObjectName(u"y0_meth2")
        self.y0_meth2.setGeometry(QRect(295, 140, 41, 21))
        self.y0_meth2.setFont(font5)
        self.y0_meth2.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);")
        self.y0_meth2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.a_meth2 = QLineEdit(self.page2)
        self.a_meth2.setObjectName(u"a_meth2")
        self.a_meth2.setGeometry(QRect(221, 200, 31, 21))
        self.a_meth2.setFont(font5)
        self.a_meth2.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);")
        self.a_meth2.setAlignment(Qt.AlignCenter)
        self.radioButton2 = QRadioButton(self.page2)
        self.radioButton2.setObjectName(u"radioButton2")
        self.radioButton2.setGeometry(QRect(216, 270, 91, 21))
        self.radioButton2.setFont(font5)
        self.radioButton2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.page2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(186, 187, 141, 41))
        self.label_3.setFont(font7)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(28, 31, 35);")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_intro2 = QLabel(self.page2)
        self.label_intro2.setObjectName(u"label_intro2")
        self.label_intro2.setGeometry(QRect(96, 0, 331, 62))
        self.label_intro2.setFont(font3)
        self.label_intro2.setLayoutDirection(Qt.LeftToRight)
        self.label_intro2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_intro2.setFrameShape(QFrame.NoFrame)
        self.label_intro2.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.page2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(171, 135, 181, 31))
        self.label_4.setFont(font4)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);\n"
"border-radius: 10px;")
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.x0_meth2 = QLineEdit(self.page2)
        self.x0_meth2.setObjectName(u"x0_meth2")
        self.x0_meth2.setGeometry(QRect(216, 141, 38, 21))
        self.x0_meth2.setFont(font5)
        self.x0_meth2.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);")
        self.x0_meth2.setAlignment(Qt.AlignCenter)
        self.pushButtonEval2 = QPushButton(self.page2)
        self.pushButtonEval2.setObjectName(u"pushButtonEval2")
        self.pushButtonEval2.setGeometry(QRect(166, 310, 181, 51))
        self.pushButtonEval2.setFont(font6)
        self.pushButtonEval2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonEval2.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")
        self.function_meth2 = QLineEdit(self.page2)
        self.function_meth2.setObjectName(u"function_meth2")
        self.function_meth2.setGeometry(QRect(136, 80, 241, 31))
        self.function_meth2.setFont(font)
        self.function_meth2.setStyleSheet(u"background-color: rgb(28, 31, 35);\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 10px;")
        self.function_meth2.setAlignment(Qt.AlignCenter)
        self.function_meth2.setPlaceholderText(u"y' = f(x,y)")
        self.b_meth2 = QLineEdit(self.page2)
        self.b_meth2.setObjectName(u"b_meth2")
        self.b_meth2.setGeometry(QRect(260, 200, 31, 21))
        self.b_meth2.setFont(font5)
        self.b_meth2.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 31, 35);")
        self.b_meth2.setAlignment(Qt.AlignCenter)
        self.pushButtonBack2 = QPushButton(self.page2)
        self.pushButtonBack2.setObjectName(u"pushButtonBack2")
        self.pushButtonBack2.setGeometry(QRect(190, 390, 131, 41))
        self.pushButtonBack2.setFont(font8)
        self.pushButtonBack2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonBack2.setStyleSheet(u"QPushButton {\n"
"	background-color: #5F15A9;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(81, 16, 145);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(68, 14, 121);\n"
"}")
        self.stackedWidget.addWidget(self.page2)
        self.radioButton2.raise_()
        self.label_3.raise_()
        self.label_intro2.raise_()
        self.label_4.raise_()
        self.x0_meth2.raise_()
        self.pushButtonEval2.raise_()
        self.function_meth2.raise_()
        self.b_meth2.raise_()
        self.y0_meth2.raise_()
        self.a_meth2.raise_()
        self.pushButtonBack2.raise_()
        lab6.setCentralWidget(self.centralwidget)

        self.retranslateUi(lab6)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(lab6)
    # setupUi

    def retranslateUi(self, lab6):
        lab6.setWindowTitle(QCoreApplication.translate("lab6", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("lab6", u"\u041b\u0430\u0431\u0430 6", None))
        self.pushButton_exp.setText("")
        self.pushButton_close.setText("")
        self.label_task.setText(QCoreApplication.translate("lab6", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u0417\u0430\u0432\u0434\u0430\u043d\u043d\u044f:</span> \u0437 \u0442\u043e\u0447\u043d\u0456\u0441\u0442\u044c\u044e \u0434\u043e 0.0001 \u0441\u043a\u043b\u0430\u0441\u0442\u0438 \u0440\u043e\u0437\u0432'\u044f\u0437\u043e\u043a</p><p align=\"center\">\u0437\u0430\u0434\u0430\u0447\u0456 \u041a\u043e\u0448\u0456 \u0434\u043b\u044f \u0437\u0432\u0438\u0447\u0430\u0439\u043d\u043e\u0433\u043e \u0434\u0438\u0444\u0435\u0440\u0435\u043d\u0446\u0456\u0439\u043d\u043e\u0433\u043e \u0440\u0456\u0432\u043d\u044f\u043d\u043d\u044f </p><p align=\"center\">\u043f\u0435\u0440\u0448\u043e\u0433\u043e \u043f\u043e\u0440\u044f\u0434\u043a\u0443 y' = f(x, y) \u043d\u0430 \u0432\u0456\u0434\u0440\u0456\u0437\u043a\u0443 [a; b] \u0437 \u043a\u0440\u043e\u043a\u043e\u043c</p><p align=\"center\">h = 0.1 \u0437\u0430 \u043f\u043e\u0447\u0430\u0442\u043a\u043e\u0432\u0438\u0445 \u0443\u043c\u043e\u0432 y(x<span style=\" vertical-align:sub;\">0</span>)=y<spa"
                        "n style=\" vertical-align:sub;\">0</span></p></body></html>", None))
        self.label_intro.setText(QCoreApplication.translate("lab6", u"\u0412\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u043c\u0435\u0442\u043e\u0434", None))
        self.pushButtonTo1.setText(QCoreApplication.translate("lab6", u"\u041c\u0435\u0442\u043e\u0434 \u0415\u0439\u043b\u0435\u0440\u0430", None))
        self.pushButtonTo2.setText(QCoreApplication.translate("lab6", u"\u041c\u0435\u0442\u043e\u0434 \u0415\u0439\u043b\u0435\u0440\u0430-\u041a\u043e\u0448\u0456", None))
        self.b_meth1.setText("")
        self.b_meth1.setPlaceholderText(QCoreApplication.translate("lab6", u"b", None))
        self.label_intro1.setText(QCoreApplication.translate("lab6", u"\u041c\u0435\u0442\u043e\u0434 \u0415\u0439\u043b\u0435\u0440\u0430", None))
        self.radioButton1.setText(QCoreApplication.translate("lab6", u"\u0413\u0440\u0430\u0444\u0456\u043a", None))
        self.pushButtonEval1.setText(QCoreApplication.translate("lab6", u"\u041e\u0431\u0447\u0438\u0441\u043b\u0438\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("lab6", u"[     ,     ]", None))
        self.x0_meth1.setText("")
        self.x0_meth1.setPlaceholderText(QCoreApplication.translate("lab6", u"x0", None))
        self.y0_meth1.setText("")
        self.y0_meth1.setPlaceholderText(QCoreApplication.translate("lab6", u"y0", None))
        self.label.setText(QCoreApplication.translate("lab6", u"   y(        )  =           ", None))
        self.a_meth1.setText("")
        self.a_meth1.setPlaceholderText(QCoreApplication.translate("lab6", u"a", None))
        self.function_meth1.setText("")
        self.pushButtonBack1.setText(QCoreApplication.translate("lab6", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.y0_meth2.setText("")
        self.y0_meth2.setPlaceholderText(QCoreApplication.translate("lab6", u"y0", None))
        self.a_meth2.setText("")
        self.a_meth2.setPlaceholderText(QCoreApplication.translate("lab6", u"a", None))
        self.radioButton2.setText(QCoreApplication.translate("lab6", u"\u0413\u0440\u0430\u0444\u0456\u043a", None))
        self.label_3.setText(QCoreApplication.translate("lab6", u"[     ,     ]", None))
        self.label_intro2.setText(QCoreApplication.translate("lab6", u"\u041c\u0435\u0442\u043e\u0434 \u0415\u0439\u043b\u0435\u0440\u0430-\u041a\u043e\u0448\u0456", None))
        self.label_4.setText(QCoreApplication.translate("lab6", u"   y(        )  =           ", None))
        self.x0_meth2.setText("")
        self.x0_meth2.setPlaceholderText(QCoreApplication.translate("lab6", u"x0", None))
        self.pushButtonEval2.setText(QCoreApplication.translate("lab6", u"\u041e\u0431\u0447\u0438\u0441\u043b\u0438\u0442\u0438", None))
        self.function_meth2.setText("")
        self.b_meth2.setText("")
        self.b_meth2.setPlaceholderText(QCoreApplication.translate("lab6", u"b", None))
        self.pushButtonBack2.setText(QCoreApplication.translate("lab6", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

