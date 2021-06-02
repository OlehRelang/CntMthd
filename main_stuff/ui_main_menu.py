# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menuMSxoLL.ui'
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


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(437, 682)
        self.centralwidget = QWidget(MainMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(38, 41, 45);\n"
"border-radius: 10px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_header = QFrame(self.frame)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 421, 31))
        self.frame_header.setStyleSheet(u"border-radius: 10px;\n"
"background-color:rgb(28, 31, 35)")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_header)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 6, 148, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color:rgb(160, 160, 160)")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_exp = QPushButton(self.frame_header)
        self.pushButton_exp.setObjectName(u"pushButton_exp")
        self.pushButton_exp.setGeometry(QRect(373, 8, 15, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.pushButton_exp.setFont(font2)
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
        self.pushButton_close.setGeometry(QRect(394, 8, 16, 16))
        self.pushButton_close.setFont(font2)
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
        self.frame_credits = QFrame(self.frame)
        self.frame_credits.setObjectName(u"frame_credits")
        self.frame_credits.setGeometry(QRect(0, 630, 421, 31))
        self.frame_credits.setStyleSheet(u"border-radius: 10px;\n"
"")
        self.frame_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_credits.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_credits)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 0, 181, 21))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_2.setFont(font3)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"color: rgb(208, 209, 185);")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 90, 421, 71))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(25)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_3.setFont(font4)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 180, 211, 411))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(17)
        font5.setBold(True)
        font5.setWeight(75)
        self.pushButton_2.setFont(font5)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border-style:  solid;\n"
"	border-radius: 15px;\n"
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

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font5)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border-style:  solid;\n"
"	border-radius: 15px;\n"
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

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font5)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border-style:  solid;\n"
"	border-radius: 15px;\n"
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

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font5)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	border-style:  solid;\n"
"	border-radius: 15px;\n"
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

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font5)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	border-style:  solid;\n"
"	border-radius: 15px;\n"
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

        self.verticalLayout.addWidget(self.pushButton_6)


        self.horizontalLayout.addWidget(self.frame)

        MainMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainMenu)

        QMetaObject.connectSlotsByName(MainMenu)
    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainMenu", u"\u0427\u0438\u0441\u0435\u043b\u044c\u043d\u0456 \u043c\u0435\u0442\u043e\u0434\u0438", None))
        self.pushButton_exp.setText("")
        self.pushButton_close.setText("")
        self.label_2.setText(QCoreApplication.translate("MainMenu", u"<strong>Created:</strong> \u0421\u0435\u043c\u0447\u0443\u043a \u041e\u043b\u0435\u0433", None))
        self.label_3.setText(QCoreApplication.translate("MainMenu", u"  \u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0456 \u0440\u043e\u0431\u043e\u0442\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainMenu", u"\u041b\u0430\u0431\u0430 2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainMenu", u"\u041b\u0430\u0431\u0430 3", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainMenu", u"\u041b\u0430\u0431\u0430 4", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainMenu", u"\u041b\u0430\u0431\u0430 5", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainMenu", u"\u041b\u0430\u0431\u0430 6", None))
    # retranslateUi

