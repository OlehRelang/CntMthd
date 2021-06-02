# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab2wAhodC.ui'
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


class Ui_Lab2(object):
    def setupUi(self, Lab2):
        if Lab2.objectName():
            Lab2.setObjectName(u"Lab2")
        Lab2.resize(426, 602)
        Lab2.setAutoFillBackground(False)
        Lab2.setStyleSheet(u"background-color: rgb(38, 41, 45);\n"
"")
        self.centralwidget = QWidget(Lab2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_task = QLabel(self.centralwidget)
        self.label_task.setObjectName(u"label_task")
        self.label_task.setGeometry(QRect(10, 60, 411, 91))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_task.setFont(font)
        self.label_task.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_task.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(52, 200, 51, 16))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(52, 219, 61, 31))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton1 = QPushButton(self.centralwidget)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setGeometry(QRect(137, 298, 171, 41))
        font2 = QFont()
        font2.setFamily(u"Bodoni MT Black")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton1.setFont(font2)
        self.pushButton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton1.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton1.setFlat(False)
        self.label_result1 = QLabel(self.centralwidget)
        self.label_result1.setObjectName(u"label_result1")
        self.label_result1.setGeometry(QRect(118, 350, 211, 31))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_result1.setFont(font3)
        self.label_result1.setStyleSheet(u"background-color: rgb(60, 13, 107);\n"
"color: rgba(255, 255, 255, 150);\n"
"border-radius: 10px;")
        self.label_result1.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(105, 174, 231, 21))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(104, 430, 241, 21))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 468, 71, 21))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_9 = QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(170, 469, 31, 21))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.lineEdit_9.setFont(font4)
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(38, 41, 45);\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.lineEdit_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(210, 469, 51, 21))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_result2 = QLabel(self.centralwidget)
        self.label_result2.setObjectName(u"label_result2")
        self.label_result2.setGeometry(QRect(270, 470, 61, 21))
        self.label_result2.setFont(font1)
        self.label_result2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_result2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton2 = QPushButton(self.centralwidget)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setGeometry(QRect(152, 510, 141, 41))
        self.pushButton2.setFont(font2)
        self.pushButton2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton2.setStyleSheet(u"QPushButton {\n"
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
        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(290, 229, 52, 23))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.lineEdit_7.setFont(font5)
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(19, 22, 25);\n"
"color:rgba(211, 211, 211, 180);\n"
"border: none;")
        self.lineEdit_7.setAlignment(Qt.AlignCenter)
        self.lineEdit_0 = QLineEdit(self.centralwidget)
        self.lineEdit_0.setObjectName(u"lineEdit_0")
        self.lineEdit_0.setGeometry(QRect(113, 200, 53, 23))
        self.lineEdit_0.setFont(font5)
        self.lineEdit_0.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_0.setStyleSheet(u"background-color: rgb(19, 22, 25);\n"
"color:rgba(211, 211, 211, 180);\n"
"border: none;")
        self.lineEdit_0.setAlignment(Qt.AlignCenter)
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(172, 229, 53, 23))
        self.lineEdit_5.setFont(font5)
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(19, 22, 25);\n"
"color:rgba(211, 211, 211, 180);\n"
"border: none;")
        self.lineEdit_5.setAlignment(Qt.AlignCenter)
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(231, 229, 53, 23))
        self.lineEdit_6.setFont(font5)
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(19, 22, 25);\n"
"color:rgba(211, 211, 211, 180);\n"
"border: none;")
        self.lineEdit_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(113, 229, 53, 23))
        self.lineEdit_4.setFont(font5)
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(19, 22, 25);\n"
"color:rgba(211, 211, 211, 180);\n"
"border: none;")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(231, 200, 53, 23))
        self.lineEdit_2.setFont(font5)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(19, 22, 25);\n"
"color:rgba(211, 211, 211, 180);\n"
"border: none;")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_1 = QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(172, 200, 53, 23))
        self.lineEdit_1.setFont(font5)
        self.lineEdit_1.setStyleSheet(u"background-color: rgb(19, 22, 25);\n"
"color:rgba(211, 211, 211, 180);\n"
"border: none;")
        self.lineEdit_1.setAlignment(Qt.AlignCenter)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(290, 200, 52, 23))
        self.lineEdit_3.setFont(font5)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(19, 22, 25);\n"
"color:rgba(211, 211, 211, 180);\n"
"border: none;")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 431, 31))
        self.frame_header.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(28, 31, 35)")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_header)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 6, 148, 20))
        self.label.setFont(font4)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color:rgb(160, 160, 160)")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_exp = QPushButton(self.frame_header)
        self.pushButton_exp.setObjectName(u"pushButton_exp")
        self.pushButton_exp.setGeometry(QRect(377, 8, 15, 15))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setWeight(50)
        self.pushButton_exp.setFont(font6)
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
        self.pushButton_close.setGeometry(QRect(401, 8, 16, 16))
        self.pushButton_close.setFont(font6)
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
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(193, 270, 61, 17))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(9)
        self.radioButton.setFont(font7)
        self.radioButton.setStyleSheet(u"color: rgb(255, 255, 255)")
        Lab2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Lab2)

        QMetaObject.connectSlotsByName(Lab2)
    # setupUi

    def retranslateUi(self, Lab2):
        Lab2.setWindowTitle(QCoreApplication.translate("Lab2", u"MainWindow", None))
        self.label_task.setText(QCoreApplication.translate("Lab2", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">\u0417\u0430\u0432\u0434\u0430\u043d\u043d\u044f: </span><span style=\" font-size:10pt; font-weight:400;\">\u041f\u043e\u0431\u0443\u0434\u0443\u0432\u0430\u0442\u0438 \u0456\u043d\u0442\u0435\u0440\u043f\u043e\u043b\u044f\u0446\u0456\u0439\u043d\u0438\u0439 \u0431\u0430\u0433\u0430\u0442\u043e\u0447\u043b\u0435\u043d \u041b\u0430\u0433\u0440\u0430\u043d\u0436\u0430 \u0434\u043b\u044f </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:400;\">\u0444\u0443\u043d\u043a\u0446\u0456\u0457 f(x), \u0449\u043e \u0437\u0430\u0434\u0430\u043d\u0430 \u0442\u0430\u0431\u043b\u0438\u0446\u0435\u044e, \u0442\u0430 \u0437 \u0442\u043e\u0447\u043d\u0456\u0441\u0442\u044c\u044e \u0434\u043e 0,001 </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:400;\">\u043e\u0431\u0447\u0438\u0441\u043b\u0438\u0442\u0438 \u043d\u0430\u0431\u043b\u0438\u0436\u0435\u043d\u0456 \u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044f \u0444"
                        "\u0443\u043d\u043a\u0446\u0456\u0457 \u0443 \u0437\u0430\u0434\u0430\u043d\u0438\u0445 \u0442\u043e\u0447\u043a\u0430\u0445. </span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Lab2", u"x", None))
        self.label_3.setText(QCoreApplication.translate("Lab2", u"f(x)", None))
        self.pushButton1.setText(QCoreApplication.translate("Lab2", u"\u041f\u043e\u0431\u0443\u0434\u0443\u0432\u0430\u0442\u0438 \u043c\u043d\u043e\u0433\u043e\u0447\u043b\u0435\u043d", None))
        self.label_result1.setText(QCoreApplication.translate("Lab2", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.label_5.setText(QCoreApplication.translate("Lab2", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u044c \u0444\u0443\u043d\u043a\u0446\u0456\u0457", None))
        self.label_6.setText(QCoreApplication.translate("Lab2", u"\u041d\u0430\u0431\u0438\u043b\u0436\u0435\u043d\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044f \u0432 \u0442\u043e\u0447\u0446\u0456", None))
        self.label_7.setText(QCoreApplication.translate("Lab2", u"x = ", None))
        self.lineEdit_9.setText(QCoreApplication.translate("Lab2", u"......", None))
        self.label_8.setText(QCoreApplication.translate("Lab2", u"f(x)  \u2248", None))
        self.label_result2.setText("")
        self.pushButton2.setText(QCoreApplication.translate("Lab2", u"\u041e\u0431\u0447\u0438\u0441\u043b\u0438\u0442\u0438", None))
        self.lineEdit_7.setText(QCoreApplication.translate("Lab2", u"y3", None))
        self.lineEdit_0.setText(QCoreApplication.translate("Lab2", u"x0", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Lab2", u"y1", None))
        self.lineEdit_6.setText(QCoreApplication.translate("Lab2", u"y2", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Lab2", u"y0", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Lab2", u"x2", None))
        self.lineEdit_1.setText(QCoreApplication.translate("Lab2", u"x1", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Lab2", u"x3", None))
        self.label.setText(QCoreApplication.translate("Lab2", u"\u041b\u0430\u0431\u0430 2", None))
        self.pushButton_exp.setText("")
        self.pushButton_close.setText("")
        self.radioButton.setText(QCoreApplication.translate("Lab2", u"\u0413\u0440\u0430\u0444\u0456\u043a", None))
    # retranslateUi

