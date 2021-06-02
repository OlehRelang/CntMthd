# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab4yzoezZ.ui'
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


class Ui_lab4(object):
    def setupUi(self, lab4):
        if lab4.objectName():
            lab4.setObjectName(u"lab4")
        lab4.resize(447, 578)
        lab4.setStyleSheet(u"background-color: rgb(38, 41, 45);")
        self.centralwidget = QWidget(lab4)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 450, 31))
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
        self.pushButton_exp.setGeometry(QRect(400, 8, 15, 15))
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
        self.pushButton_close.setGeometry(QRect(425, 8, 16, 16))
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
        self.label_task.setGeometry(QRect(0, 40, 450, 61))
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
        self.stackedWidget.setGeometry(QRect(0, 109, 450, 461))
        self.stackedWidget.setStyleSheet(u"")
        self.page_menu = QWidget()
        self.page_menu.setObjectName(u"page_menu")
        self.pushButtonTo1 = QPushButton(self.page_menu)
        self.pushButtonTo1.setObjectName(u"pushButtonTo1")
        self.pushButtonTo1.setGeometry(QRect(110, 120, 241, 61))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButtonTo1.setFont(font3)
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
        self.pushButtonTo2.setGeometry(QRect(110, 230, 241, 61))
        self.pushButtonTo2.setFont(font3)
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
        self.pushButtonTo3 = QPushButton(self.page_menu)
        self.pushButtonTo3.setObjectName(u"pushButtonTo3")
        self.pushButtonTo3.setGeometry(QRect(110, 340, 241, 61))
        self.pushButtonTo3.setFont(font3)
        self.pushButtonTo3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonTo3.setStyleSheet(u"QPushButton{\n"
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
        self.label_intro = QLabel(self.page_menu)
        self.label_intro.setObjectName(u"label_intro")
        self.label_intro.setGeometry(QRect(70, 10, 316, 62))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_intro.setFont(font4)
        self.label_intro.setLayoutDirection(Qt.LeftToRight)
        self.label_intro.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_intro.setFrameShape(QFrame.NoFrame)
        self.label_intro.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_menu)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.label_meth1 = QLabel(self.page_1)
        self.label_meth1.setObjectName(u"label_meth1")
        self.label_meth1.setGeometry(QRect(60, 0, 331, 31))
        self.label_meth1.setFont(font3)
        self.label_meth1.setLayoutDirection(Qt.LeftToRight)
        self.label_meth1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_meth1.setFrameShape(QFrame.NoFrame)
        self.label_meth1.setAlignment(Qt.AlignCenter)
        self.label_1_1 = QLabel(self.page_1)
        self.label_1_1.setObjectName(u"label_1_1")
        self.label_1_1.setGeometry(QRect(130, 40, 61, 31))
        self.label_1_1.setFont(font3)
        self.label_1_1.setLayoutDirection(Qt.LeftToRight)
        self.label_1_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_1_1.setFrameShape(QFrame.NoFrame)
        self.label_1_1.setAlignment(Qt.AlignCenter)
        self.function_meth1 = QLineEdit(self.page_1)
        self.function_meth1.setObjectName(u"function_meth1")
        self.function_meth1.setGeometry(QRect(190, 40, 221, 31))
        self.function_meth1.setFont(font)
        self.function_meth1.setStyleSheet(u"background-color: rgb(38, 41, 45);\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.function_meth1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.function_meth1.setPlaceholderText(u"\u0412\u0430\u0448\u0430 \u0444\u0443\u043d\u043a\u0446\u0456\u044f")
        self.label_1_2 = QLabel(self.page_1)
        self.label_1_2.setObjectName(u"label_1_2")
        self.label_1_2.setGeometry(QRect(50, 130, 261, 101))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(26)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_1_2.setFont(font5)
        self.label_1_2.setLayoutDirection(Qt.LeftToRight)
        self.label_1_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 25, 28);\n"
"border-radius: 10px;")
        self.label_1_2.setFrameShape(QFrame.NoFrame)
        self.label_1_2.setAlignment(Qt.AlignCenter)
        self.label_result1 = QLabel(self.page_1)
        self.label_result1.setObjectName(u"label_result1")
        self.label_result1.setGeometry(QRect(260, 130, 141, 101))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(17)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_result1.setFont(font6)
        self.label_result1.setStyleSheet(u"color: rgb(160, 160, 160);\n"
"background-color: rgb(23, 25, 28);\n"
"border-radius: 10px;")
        self.label_result1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButtonEval1 = QPushButton(self.page_1)
        self.pushButtonEval1.setObjectName(u"pushButtonEval1")
        self.pushButtonEval1.setGeometry(QRect(140, 290, 181, 51))
        font7 = QFont()
        font7.setFamily(u"Bodoni MT Black")
        font7.setPointSize(13)
        font7.setBold(True)
        font7.setWeight(75)
        self.pushButtonEval1.setFont(font7)
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
        self.pushButtonBack1 = QPushButton(self.page_1)
        self.pushButtonBack1.setObjectName(u"pushButtonBack1")
        self.pushButtonBack1.setGeometry(QRect(160, 410, 141, 41))
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
        self.b1 = QLineEdit(self.page_1)
        self.b1.setObjectName(u"b1")
        self.b1.setGeometry(QRect(104, 143, 31, 21))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(9)
        font9.setBold(True)
        font9.setWeight(75)
        self.b1.setFont(font9)
        self.b1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: rgb(23, 25, 28);")
        self.b1.setAlignment(Qt.AlignCenter)
        self.a1 = QLineEdit(self.page_1)
        self.a1.setObjectName(u"a1")
        self.a1.setGeometry(QRect(96, 206, 31, 21))
        self.a1.setFont(font9)
        self.a1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: rgb(23, 25, 28);")
        self.a1.setAlignment(Qt.AlignCenter)
        self.label_1_7 = QLabel(self.page_1)
        self.label_1_7.setObjectName(u"label_1_7")
        self.label_1_7.setGeometry(QRect(156, 80, 31, 31))
        self.label_1_7.setFont(font3)
        self.label_1_7.setLayoutDirection(Qt.LeftToRight)
        self.label_1_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_1_7.setFrameShape(QFrame.NoFrame)
        self.label_1_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.n1 = QLineEdit(self.page_1)
        self.n1.setObjectName(u"n1")
        self.n1.setGeometry(QRect(189, 80, 91, 31))
        self.n1.setFont(font3)
        self.n1.setStyleSheet(u"background-color: rgb(38, 41, 45);\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.n1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.n1.setPlaceholderText(u"*\u0447\u0438\u0441\u043b\u043e*")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_meth2 = QLabel(self.page_2)
        self.label_meth2.setObjectName(u"label_meth2")
        self.label_meth2.setGeometry(QRect(65, 0, 331, 31))
        self.label_meth2.setFont(font3)
        self.label_meth2.setLayoutDirection(Qt.LeftToRight)
        self.label_meth2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_meth2.setFrameShape(QFrame.NoFrame)
        self.label_meth2.setAlignment(Qt.AlignCenter)
        self.label_1_3 = QLabel(self.page_2)
        self.label_1_3.setObjectName(u"label_1_3")
        self.label_1_3.setGeometry(QRect(130, 40, 61, 31))
        self.label_1_3.setFont(font3)
        self.label_1_3.setLayoutDirection(Qt.LeftToRight)
        self.label_1_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_1_3.setFrameShape(QFrame.NoFrame)
        self.label_1_3.setAlignment(Qt.AlignCenter)
        self.function_meth2 = QLineEdit(self.page_2)
        self.function_meth2.setObjectName(u"function_meth2")
        self.function_meth2.setGeometry(QRect(190, 40, 221, 31))
        self.function_meth2.setFont(font)
        self.function_meth2.setStyleSheet(u"background-color: rgb(38, 41, 45);\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.function_meth2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.function_meth2.setPlaceholderText(u"\u0412\u0430\u0448\u0430 \u0444\u0443\u043d\u043a\u0446\u0456\u044f")
        self.label_result2 = QLabel(self.page_2)
        self.label_result2.setObjectName(u"label_result2")
        self.label_result2.setGeometry(QRect(260, 130, 141, 101))
        self.label_result2.setFont(font6)
        self.label_result2.setStyleSheet(u"color: rgb(160, 160, 160);\n"
"background-color: rgb(23, 25, 28);\n"
"border-radius: 10px;")
        self.label_result2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_1_4 = QLabel(self.page_2)
        self.label_1_4.setObjectName(u"label_1_4")
        self.label_1_4.setGeometry(QRect(50, 130, 261, 101))
        self.label_1_4.setFont(font5)
        self.label_1_4.setLayoutDirection(Qt.LeftToRight)
        self.label_1_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 25, 28);\n"
"border-radius: 10px;")
        self.label_1_4.setFrameShape(QFrame.NoFrame)
        self.label_1_4.setAlignment(Qt.AlignCenter)
        self.a2 = QLineEdit(self.page_2)
        self.a2.setObjectName(u"a2")
        self.a2.setGeometry(QRect(96, 206, 31, 21))
        self.a2.setFont(font9)
        self.a2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: rgb(23, 25, 28);")
        self.a2.setAlignment(Qt.AlignCenter)
        self.b2 = QLineEdit(self.page_2)
        self.b2.setObjectName(u"b2")
        self.b2.setGeometry(QRect(104, 143, 31, 21))
        self.b2.setFont(font9)
        self.b2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: rgb(23, 25, 28);")
        self.b2.setAlignment(Qt.AlignCenter)
        self.pushButtonEval2 = QPushButton(self.page_2)
        self.pushButtonEval2.setObjectName(u"pushButtonEval2")
        self.pushButtonEval2.setGeometry(QRect(140, 290, 181, 51))
        self.pushButtonEval2.setFont(font7)
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
        self.pushButtonBack2 = QPushButton(self.page_2)
        self.pushButtonBack2.setObjectName(u"pushButtonBack2")
        self.pushButtonBack2.setGeometry(QRect(160, 410, 141, 41))
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
        self.n2 = QLineEdit(self.page_2)
        self.n2.setObjectName(u"n2")
        self.n2.setGeometry(QRect(189, 80, 91, 31))
        self.n2.setFont(font3)
        self.n2.setStyleSheet(u"background-color: rgb(38, 41, 45);\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.n2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.n2.setPlaceholderText(u"*\u0447\u0438\u0441\u043b\u043e*")
        self.label_1_8 = QLabel(self.page_2)
        self.label_1_8.setObjectName(u"label_1_8")
        self.label_1_8.setGeometry(QRect(156, 80, 31, 31))
        self.label_1_8.setFont(font3)
        self.label_1_8.setLayoutDirection(Qt.LeftToRight)
        self.label_1_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_1_8.setFrameShape(QFrame.NoFrame)
        self.label_1_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.label_meth2.raise_()
        self.label_1_3.raise_()
        self.function_meth2.raise_()
        self.label_1_4.raise_()
        self.label_result2.raise_()
        self.a2.raise_()
        self.b2.raise_()
        self.pushButtonEval2.raise_()
        self.pushButtonBack2.raise_()
        self.n2.raise_()
        self.label_1_8.raise_()
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_meth3 = QLabel(self.page_3)
        self.label_meth3.setObjectName(u"label_meth3")
        self.label_meth3.setGeometry(QRect(70, 0, 321, 31))
        self.label_meth3.setFont(font3)
        self.label_meth3.setLayoutDirection(Qt.LeftToRight)
        self.label_meth3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_meth3.setFrameShape(QFrame.NoFrame)
        self.label_meth3.setAlignment(Qt.AlignCenter)
        self.function_meth3 = QLineEdit(self.page_3)
        self.function_meth3.setObjectName(u"function_meth3")
        self.function_meth3.setGeometry(QRect(190, 40, 221, 31))
        self.function_meth3.setFont(font)
        self.function_meth3.setStyleSheet(u"background-color: rgb(38, 41, 45);\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.function_meth3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.function_meth3.setPlaceholderText(u"\u0412\u0430\u0448\u0430 \u0444\u0443\u043d\u043a\u0446\u0456\u044f")
        self.label_1_5 = QLabel(self.page_3)
        self.label_1_5.setObjectName(u"label_1_5")
        self.label_1_5.setGeometry(QRect(130, 40, 61, 31))
        self.label_1_5.setFont(font3)
        self.label_1_5.setLayoutDirection(Qt.LeftToRight)
        self.label_1_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_1_5.setFrameShape(QFrame.NoFrame)
        self.label_1_5.setAlignment(Qt.AlignCenter)
        self.pushButtonBack3 = QPushButton(self.page_3)
        self.pushButtonBack3.setObjectName(u"pushButtonBack3")
        self.pushButtonBack3.setGeometry(QRect(160, 410, 141, 41))
        self.pushButtonBack3.setFont(font8)
        self.pushButtonBack3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonBack3.setStyleSheet(u"QPushButton {\n"
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
        self.pushButtonEval3 = QPushButton(self.page_3)
        self.pushButtonEval3.setObjectName(u"pushButtonEval3")
        self.pushButtonEval3.setGeometry(QRect(140, 290, 181, 51))
        self.pushButtonEval3.setFont(font7)
        self.pushButtonEval3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonEval3.setStyleSheet(u"QPushButton {\n"
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
        self.label_result3 = QLabel(self.page_3)
        self.label_result3.setObjectName(u"label_result3")
        self.label_result3.setGeometry(QRect(260, 130, 141, 101))
        self.label_result3.setFont(font6)
        self.label_result3.setStyleSheet(u"color: rgb(160, 160, 160);\n"
"background-color: rgb(23, 25, 28);\n"
"border-radius: 10px;")
        self.label_result3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.a2_2 = QLineEdit(self.page_3)
        self.a2_2.setObjectName(u"a2_2")
        self.a2_2.setGeometry(QRect(96, 206, 31, 21))
        self.a2_2.setFont(font9)
        self.a2_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: rgb(23, 25, 28);")
        self.a2_2.setAlignment(Qt.AlignCenter)
        self.b2_2 = QLineEdit(self.page_3)
        self.b2_2.setObjectName(u"b2_2")
        self.b2_2.setGeometry(QRect(104, 143, 31, 21))
        self.b2_2.setFont(font9)
        self.b2_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: rgb(23, 25, 28);")
        self.b2_2.setAlignment(Qt.AlignCenter)
        self.label_1_6 = QLabel(self.page_3)
        self.label_1_6.setObjectName(u"label_1_6")
        self.label_1_6.setGeometry(QRect(50, 130, 261, 101))
        self.label_1_6.setFont(font5)
        self.label_1_6.setLayoutDirection(Qt.LeftToRight)
        self.label_1_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 25, 28);\n"
"border-radius: 10px;")
        self.label_1_6.setFrameShape(QFrame.NoFrame)
        self.label_1_6.setAlignment(Qt.AlignCenter)
        self.n3 = QLineEdit(self.page_3)
        self.n3.setObjectName(u"n3")
        self.n3.setGeometry(QRect(189, 80, 91, 31))
        self.n3.setFont(font3)
        self.n3.setStyleSheet(u"background-color: rgb(38, 41, 45);\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.n3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.n3.setPlaceholderText(u"*\u0447\u0438\u0441\u043b\u043e*")
        self.label_1_9 = QLabel(self.page_3)
        self.label_1_9.setObjectName(u"label_1_9")
        self.label_1_9.setGeometry(QRect(156, 80, 31, 31))
        self.label_1_9.setFont(font3)
        self.label_1_9.setLayoutDirection(Qt.LeftToRight)
        self.label_1_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_1_9.setFrameShape(QFrame.NoFrame)
        self.label_1_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_3)
        self.label_1_6.raise_()
        self.label_meth3.raise_()
        self.function_meth3.raise_()
        self.label_1_5.raise_()
        self.pushButtonBack3.raise_()
        self.pushButtonEval3.raise_()
        self.label_result3.raise_()
        self.a2_2.raise_()
        self.b2_2.raise_()
        self.n3.raise_()
        self.label_1_9.raise_()
        lab4.setCentralWidget(self.centralwidget)

        self.retranslateUi(lab4)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(lab4)
    # setupUi

    def retranslateUi(self, lab4):
        lab4.setWindowTitle(QCoreApplication.translate("lab4", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("lab4", u"\u041b\u0430\u0431\u0430 4", None))
        self.pushButton_exp.setText("")
        self.pushButton_close.setText("")
        self.label_task.setText(QCoreApplication.translate("lab4", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u0417\u0430\u0432\u0434\u0430\u043d\u043d\u044f:</span> \u0437 \u0442\u043e\u0447\u043d\u0456\u0441\u0442\u044c\u044e \u0434\u043e 0.0001 \u043e\u0431\u0447\u0438\u0441\u043b\u0438\u0442\u0438<br/>\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044f \u0432\u0438\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0445 \u0456\u043d\u0442\u0435\u0433\u0440\u0430\u043b\u0456\u0432</p></body></html>", None))
        self.pushButtonTo1.setText(QCoreApplication.translate("lab4", u"\u041c\u0435\u0442\u043e\u0434 \u043f\u0440\u044f\u043c\u043e\u043a\u0443\u0442\u043d\u0438\u043a\u0456\u0432", None))
        self.pushButtonTo2.setText(QCoreApplication.translate("lab4", u"\u041c\u0435\u0442\u043e\u0434 \u0421\u0456\u043c\u043f\u0441\u043e\u043d\u0430", None))
        self.pushButtonTo3.setText(QCoreApplication.translate("lab4", u"\u041c\u0435\u0442\u043e\u0434 \u0442\u0440\u0430\u043f\u0435\u0446\u0456\u0439", None))
        self.label_intro.setText(QCoreApplication.translate("lab4", u"\u0412\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u043c\u0435\u0442\u043e\u0434", None))
        self.label_meth1.setText(QCoreApplication.translate("lab4", u"\u041c\u0435\u0442\u043e\u0434 \u043f\u0440\u044f\u043c\u043e\u043a\u0443\u0442\u043d\u0438\u043a\u0456\u0432", None))
        self.label_1_1.setText(QCoreApplication.translate("lab4", u"f(x) =", None))
        self.function_meth1.setText("")
        self.label_1_2.setText(QCoreApplication.translate("lab4", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:400;\">\u222b</span><span style=\" font-size:24pt;\">f(x)dx</span><span style=\" font-size:28pt;\"> \u2248</span></p></body></html>", None))
        self.label_result1.setText(QCoreApplication.translate("lab4", u"<html><head/><body><p>*\u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442*</p></body></html>", None))
        self.pushButtonEval1.setText(QCoreApplication.translate("lab4", u"\u041e\u0431\u0447\u0438\u0441\u043b\u0438\u0442\u0438", None))
        self.pushButtonBack1.setText(QCoreApplication.translate("lab4", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.b1.setPlaceholderText(QCoreApplication.translate("lab4", u"b", None))
        self.a1.setPlaceholderText(QCoreApplication.translate("lab4", u"a", None))
        self.label_1_7.setText(QCoreApplication.translate("lab4", u"n =", None))
        self.n1.setText("")
        self.label_meth2.setText(QCoreApplication.translate("lab4", u"\u041c\u0435\u0442\u043e\u0434 \u0421\u0456\u043c\u043f\u0441\u043e\u043d\u0430", None))
        self.label_1_3.setText(QCoreApplication.translate("lab4", u"f(x) =", None))
        self.function_meth2.setText("")
        self.label_result2.setText(QCoreApplication.translate("lab4", u"<html><head/><body><p>*\u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442*</p></body></html>", None))
        self.label_1_4.setText(QCoreApplication.translate("lab4", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:400;\">\u222b</span><span style=\" font-size:24pt;\">f(x)dx</span><span style=\" font-size:28pt;\"> \u2248</span></p></body></html>", None))
        self.a2.setPlaceholderText(QCoreApplication.translate("lab4", u"a", None))
        self.b2.setPlaceholderText(QCoreApplication.translate("lab4", u"b", None))
        self.pushButtonEval2.setText(QCoreApplication.translate("lab4", u"\u041e\u0431\u0447\u0438\u0441\u043b\u0438\u0442\u0438", None))
        self.pushButtonBack2.setText(QCoreApplication.translate("lab4", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.n2.setText("")
        self.label_1_8.setText(QCoreApplication.translate("lab4", u"n =", None))
        self.label_meth3.setText(QCoreApplication.translate("lab4", u"\u041c\u0435\u0442\u043e\u0434 \u0442\u0440\u0430\u043f\u0435\u0446\u0456\u0439", None))
        self.function_meth3.setText("")
        self.label_1_5.setText(QCoreApplication.translate("lab4", u"f(x) =", None))
        self.pushButtonBack3.setText(QCoreApplication.translate("lab4", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pushButtonEval3.setText(QCoreApplication.translate("lab4", u"\u041e\u0431\u0447\u0438\u0441\u043b\u0438\u0442\u0438", None))
        self.label_result3.setText(QCoreApplication.translate("lab4", u"<html><head/><body><p>*\u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442*</p></body></html>", None))
        self.a2_2.setPlaceholderText(QCoreApplication.translate("lab4", u"a", None))
        self.b2_2.setPlaceholderText(QCoreApplication.translate("lab4", u"b", None))
        self.label_1_6.setText(QCoreApplication.translate("lab4", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:400;\">\u222b</span><span style=\" font-size:24pt;\">f(x)dx</span><span style=\" font-size:28pt;\"> \u2248</span></p></body></html>", None))
        self.n3.setText("")
        self.label_1_9.setText(QCoreApplication.translate("lab4", u"n =", None))
    # retranslateUi

