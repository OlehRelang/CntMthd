# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab5fawmDT.ui'
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


class Ui_lab5(object):
    def setupUi(self, lab5):
        if lab5.objectName():
            lab5.setObjectName(u"lab5")
        lab5.resize(450, 563)
        lab5.setStyleSheet(u"background-color: rgb(38, 41, 45);")
        self.centralwidget = QWidget(lab5)
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
        self.equasion = QLineEdit(self.centralwidget)
        self.equasion.setObjectName(u"equasion")
        self.equasion.setGeometry(QRect(110, 150, 311, 71))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.equasion.setFont(font3)
        self.equasion.setStyleSheet(u"background-color: rgb(38, 41, 45);\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.equasion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.equasion.setPlaceholderText(u"\u0412\u0430\u0448\u0435 \u0440\u0456\u0432\u043d\u044f\u043d\u043d\u044f")
        self.label_1_5 = QLabel(self.centralwidget)
        self.label_1_5.setObjectName(u"label_1_5")
        self.label_1_5.setGeometry(QRect(40, 150, 75, 66))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(17)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_1_5.setFont(font4)
        self.label_1_5.setLayoutDirection(Qt.LeftToRight)
        self.label_1_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_1_5.setFrameShape(QFrame.NoFrame)
        self.label_1_5.setAlignment(Qt.AlignCenter)
        self.label_meth3 = QLabel(self.centralwidget)
        self.label_meth3.setObjectName(u"label_meth3")
        self.label_meth3.setGeometry(QRect(60, 110, 331, 31))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_meth3.setFont(font5)
        self.label_meth3.setLayoutDirection(Qt.LeftToRight)
        self.label_meth3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_meth3.setFrameShape(QFrame.NoFrame)
        self.label_meth3.setAlignment(Qt.AlignCenter)
        self.label_1_6 = QLabel(self.centralwidget)
        self.label_1_6.setObjectName(u"label_1_6")
        self.label_1_6.setGeometry(QRect(140, 280, 61, 61))
        self.label_1_6.setFont(font4)
        self.label_1_6.setLayoutDirection(Qt.LeftToRight)
        self.label_1_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_1_6.setFrameShape(QFrame.NoFrame)
        self.label_1_6.setAlignment(Qt.AlignCenter)
        self.label_1_7 = QLabel(self.centralwidget)
        self.label_1_7.setObjectName(u"label_1_7")
        self.label_1_7.setGeometry(QRect(140, 350, 61, 61))
        self.label_1_7.setFont(font4)
        self.label_1_7.setLayoutDirection(Qt.LeftToRight)
        self.label_1_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_1_7.setFrameShape(QFrame.NoFrame)
        self.label_1_7.setAlignment(Qt.AlignCenter)
        self.label_x1 = QLabel(self.centralwidget)
        self.label_x1.setObjectName(u"label_x1")
        self.label_x1.setGeometry(QRect(200, 280, 141, 61))
        self.label_x1.setFont(font4)
        self.label_x1.setLayoutDirection(Qt.LeftToRight)
        self.label_x1.setStyleSheet(u"color:rgb(160, 160, 160);")
        self.label_x1.setFrameShape(QFrame.NoFrame)
        self.label_x1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_x2 = QLabel(self.centralwidget)
        self.label_x2.setObjectName(u"label_x2")
        self.label_x2.setGeometry(QRect(200, 350, 141, 61))
        self.label_x2.setFont(font4)
        self.label_x2.setLayoutDirection(Qt.LeftToRight)
        self.label_x2.setStyleSheet(u"color:rgb(160, 160, 160);")
        self.label_x2.setFrameShape(QFrame.NoFrame)
        self.label_x2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_meth3_2 = QLabel(self.centralwidget)
        self.label_meth3_2.setObjectName(u"label_meth3_2")
        self.label_meth3_2.setGeometry(QRect(70, 240, 321, 31))
        self.label_meth3_2.setFont(font5)
        self.label_meth3_2.setLayoutDirection(Qt.LeftToRight)
        self.label_meth3_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_meth3_2.setFrameShape(QFrame.NoFrame)
        self.label_meth3_2.setAlignment(Qt.AlignCenter)
        self.pushButtonEval = QPushButton(self.centralwidget)
        self.pushButtonEval.setObjectName(u"pushButtonEval")
        self.pushButtonEval.setGeometry(QRect(140, 460, 181, 51))
        font6 = QFont()
        font6.setFamily(u"Bodoni MT Black")
        font6.setPointSize(13)
        font6.setBold(True)
        font6.setWeight(75)
        self.pushButtonEval.setFont(font6)
        self.pushButtonEval.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButtonEval.setStyleSheet(u"QPushButton {\n"
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
        lab5.setCentralWidget(self.centralwidget)
        self.frame_header.raise_()
        self.label_task.raise_()
        self.label_1_5.raise_()
        self.label_meth3.raise_()
        self.equasion.raise_()
        self.label_1_6.raise_()
        self.label_1_7.raise_()
        self.label_x1.raise_()
        self.label_x2.raise_()
        self.label_meth3_2.raise_()
        self.pushButtonEval.raise_()

        self.retranslateUi(lab5)

        QMetaObject.connectSlotsByName(lab5)
    # setupUi

    def retranslateUi(self, lab5):
        lab5.setWindowTitle(QCoreApplication.translate("lab5", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("lab5", u"\u041b\u0430\u0431\u0430 5", None))
        self.pushButton_exp.setText("")
        self.pushButton_close.setText("")
        self.label_task.setText(QCoreApplication.translate("lab5", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u0417\u0430\u0432\u0434\u0430\u043d\u043d\u044f:</span> \u0440\u043e\u0437\u0432'\u044f\u0437\u0430\u0442\u0438 \u043d\u0435\u043b\u0456\u043d\u0456\u0439\u043d\u0435 \u0430\u043b\u0433\u0435\u0431\u0440\u0430\u0457\u0447\u043d\u0435<br/>\u0440\u0456\u0432\u043d\u044f\u043d\u043d\u044f f(x) = 0 \u0437 \u0442\u043e\u0447\u043d\u0456\u0441\u0442\u044e \u0434\u043e 0.0001</p></body></html>", None))
        self.equasion.setText("")
        self.label_1_5.setText(QCoreApplication.translate("lab5", u"f(x) =", None))
        self.label_meth3.setText(QCoreApplication.translate("lab5", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0440\u0456\u0432\u043d\u044f\u043d\u043d\u044f", None))
        self.label_1_6.setText(QCoreApplication.translate("lab5", u"<html><head/><body><p>x<span style=\" vertical-align:sub;\">1 </span><span style=\" font-size:14pt;\">\u2248</span></p></body></html>", None))
        self.label_1_7.setText(QCoreApplication.translate("lab5", u"<html><head/><body><p>x<span style=\" vertical-align:sub;\">2 </span><span style=\" font-size:14pt;\">\u2248</span></p></body></html>", None))
        self.label_x1.setText(QCoreApplication.translate("lab5", u"*\u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442*", None))
        self.label_x2.setText(QCoreApplication.translate("lab5", u"*\u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442*", None))
        self.label_meth3_2.setText(QCoreApplication.translate("lab5", u"\u0412\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u044c", None))
        self.pushButtonEval.setText(QCoreApplication.translate("lab5", u"\u041e\u0431\u0447\u0438\u0441\u043b\u0438\u0442\u0438", None))
    # retranslateUi

