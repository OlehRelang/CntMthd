# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab3GmWpEC.ui'
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


class Ui_Lab3(object):
    def setupUi(self, Lab3):
        if Lab3.objectName():
            Lab3.setObjectName(u"Lab3")
        Lab3.resize(519, 830)
        Lab3.setStyleSheet(u"background-color: rgb(38, 41, 45);")
        self.centralwidget = QWidget(Lab3)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(150, 210, 221, 371))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(28, 31, 34);\n"
"border-radius:10px;")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.tableWidget = QTableWidget(self.page_1)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        brush1 = QBrush(QColor(19, 22, 25, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 12):
            self.tableWidget.setRowCount(12)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setBackground(QColor(255, 255, 255));
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(2, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(4, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(5, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(5, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(6, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(6, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(7, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(7, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(8, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(8, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(9, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(9, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(10, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(10, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(11, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(11, 1, __qtablewidgetitem37)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 50, 181, 311))
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	background-color:rgb(19, 22, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	qproperty-textAlignment: AlignHCenter, AlignHCenter;\n"
"	font: 85 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	text-align: center;\n"
"    background-color: rgb(19, 22, 25);\n"
"	color: rgb(255, 255, 255);\n"
"    height: 32px;\n"
"}\n"
"\n"
"QTableCornerButton::section{\n"
"	background-color: rgb(19, 22, 25);\n"
"}")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(12)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(23)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(13, 10, 201, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.tableWidget_2 = QTableWidget(self.page_2)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem38.setForeground(brush);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setForeground(brush1);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        if (self.tableWidget_2.rowCount() < 12):
            self.tableWidget_2.setRowCount(12)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setBackground(QColor(255, 255, 255));
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(3, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(3, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(4, 0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(4, 1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(5, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(5, 1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(6, 0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(6, 1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(7, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(7, 1, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(8, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(8, 1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(9, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(9, 1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(10, 0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(10, 1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(11, 0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(11, 1, __qtablewidgetitem75)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(20, 50, 181, 311))
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"	background-color:rgb(19, 22, 25);\n"
"	color: rgb(255, 255, 255);\n"
"	qproperty-textAlignment: AlignHCenter, AlignHCenter;\n"
"	font: 85 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	text-align: center;\n"
"    background-color: rgb(19, 22, 25);\n"
"	color: rgb(255, 255, 255);\n"
"    height: 32px;\n"
"}\n"
"\n"
"QTableCornerButton::section{\n"
"	background-color: rgb(19, 22, 25);\n"
"}")
        self.tableWidget_2.setFrameShape(QFrame.NoFrame)
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setCornerButtonEnabled(True)
        self.tableWidget_2.setRowCount(12)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(75)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(23)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(13, 10, 201, 31))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 140, 161, 61))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"align: center;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 40, 511, 121))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(True)
        font1.setWeight(50)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 180, 201, 31))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setGeometry(QRect(0, 0, 521, 31))
        self.frame_header.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(28, 31, 35)")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_header)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 6, 148, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"color:rgb(160, 160, 160)")
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_exp = QPushButton(self.frame_header)
        self.pushButton_exp.setObjectName(u"pushButton_exp")
        self.pushButton_exp.setGeometry(QRect(470, 8, 15, 15))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.pushButton_exp.setFont(font3)
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
        self.pushButton_close.setGeometry(QRect(495, 8, 16, 16))
        self.pushButton_close.setFont(font3)
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
        self.pushButton2 = QPushButton(self.centralwidget)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setGeometry(QRect(190, 750, 151, 41))
        font4 = QFont()
        font4.setFamily(u"Bodoni MT Black")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.pushButton2.setFont(font4)
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
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(160, 590, 201, 31))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_8.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lineEdit_input = QLineEdit(self.centralwidget)
        self.lineEdit_input.setObjectName(u"lineEdit_input")
        self.lineEdit_input.setGeometry(QRect(260, 631, 71, 21))
        self.lineEdit_input.setFont(font2)
        self.lineEdit_input.setStyleSheet(u"background-color: rgb(38, 41, 45);\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.lineEdit_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(185, 630, 71, 21))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(200, 669, 51, 21))
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_result1 = QLabel(self.centralwidget)
        self.label_result1.setObjectName(u"label_result1")
        self.label_result1.setGeometry(QRect(260, 670, 91, 21))
        self.label_result1.setFont(font5)
        self.label_result1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_result1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(180, 699, 71, 21))
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_result2 = QLabel(self.centralwidget)
        self.label_result2.setObjectName(u"label_result2")
        self.label_result2.setGeometry(QRect(260, 700, 91, 21))
        self.label_result2.setFont(font5)
        self.label_result2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_result2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_right = QPushButton(self.centralwidget)
        self.pushButton_right.setObjectName(u"pushButton_right")
        self.pushButton_right.setGeometry(QRect(400, 360, 75, 91))
        font6 = QFont()
        font6.setPointSize(16)
        self.pushButton_right.setFont(font6)
        self.pushButton_right.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_right.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(28, 31, 34);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(53, 59, 65);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(19, 22, 25);\n"
"}")
        self.pushButton_left = QPushButton(self.centralwidget)
        self.pushButton_left.setObjectName(u"pushButton_left")
        self.pushButton_left.setGeometry(QRect(50, 360, 75, 91))
        self.pushButton_left.setFont(font6)
        self.pushButton_left.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_left.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(28, 31, 34);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(53, 59, 65);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(19, 22, 25);\n"
"}")
        Lab3.setCentralWidget(self.centralwidget)

        self.retranslateUi(Lab3)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Lab3)
    # setupUi

    def retranslateUi(self, Lab3):
        Lab3.setWindowTitle(QCoreApplication.translate("Lab3", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Lab3", u"X", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Lab3", u"Y", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Lab3", u"0", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Lab3", u"1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Lab3", u"2", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Lab3", u"3", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Lab3", u"4", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Lab3", u"5", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Lab3", u"6", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Lab3", u"7", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Lab3", u"8", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Lab3", u"9", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Lab3", u"10", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Lab3", u"11", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem14 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Lab3", u"2.4", None));
        ___qtablewidgetitem15 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Lab3", u"3.526", None));
        ___qtablewidgetitem16 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Lab3", u"2.6", None));
        ___qtablewidgetitem17 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Lab3", u"3.782", None));
        ___qtablewidgetitem18 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Lab3", u"2.8", None));
        ___qtablewidgetitem19 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Lab3", u"3.945", None));
        ___qtablewidgetitem20 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Lab3", u"3.0", None));
        ___qtablewidgetitem21 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Lab3", u"4.043", None));
        ___qtablewidgetitem22 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Lab3", u"3.2", None));
        ___qtablewidgetitem23 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Lab3", u"4.104", None));
        ___qtablewidgetitem24 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Lab3", u"3.4", None));
        ___qtablewidgetitem25 = self.tableWidget.item(5, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Lab3", u"4.155", None));
        ___qtablewidgetitem26 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Lab3", u"3.6", None));
        ___qtablewidgetitem27 = self.tableWidget.item(6, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Lab3", u"4.222", None));
        ___qtablewidgetitem28 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Lab3", u"3.8", None));
        ___qtablewidgetitem29 = self.tableWidget.item(7, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Lab3", u"4.331", None));
        ___qtablewidgetitem30 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Lab3", u"4.0", None));
        ___qtablewidgetitem31 = self.tableWidget.item(8, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Lab3", u"4.507", None));
        ___qtablewidgetitem32 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Lab3", u"4.2", None));
        ___qtablewidgetitem33 = self.tableWidget.item(9, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Lab3", u"4.775", None));
        ___qtablewidgetitem34 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Lab3", u"4.4", None));
        ___qtablewidgetitem35 = self.tableWidget.item(10, 1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Lab3", u"5.159", None));
        ___qtablewidgetitem36 = self.tableWidget.item(11, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Lab3", u"4.6", None));
        ___qtablewidgetitem37 = self.tableWidget.item(11, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Lab3", u"5.683", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("Lab3", u"\u0412\u0430\u0440\u0456\u0430\u043d\u0442 2n+1", None))
        ___qtablewidgetitem38 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Lab3", u"X", None));
        ___qtablewidgetitem39 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Lab3", u"Y", None));
        ___qtablewidgetitem40 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Lab3", u"0", None));
        ___qtablewidgetitem41 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Lab3", u"1", None));
        ___qtablewidgetitem42 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Lab3", u"2", None));
        ___qtablewidgetitem43 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Lab3", u"3", None));
        ___qtablewidgetitem44 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("Lab3", u"4", None));
        ___qtablewidgetitem45 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("Lab3", u"5", None));
        ___qtablewidgetitem46 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("Lab3", u"6", None));
        ___qtablewidgetitem47 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("Lab3", u"7", None));
        ___qtablewidgetitem48 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("Lab3", u"8", None));
        ___qtablewidgetitem49 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("Lab3", u"9", None));
        ___qtablewidgetitem50 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("Lab3", u"10", None));
        ___qtablewidgetitem51 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("Lab3", u"11", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem52 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("Lab3", u"1.5", None));
        ___qtablewidgetitem53 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("Lab3", u"10.517", None));
        ___qtablewidgetitem54 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("Lab3", u"2.0", None));
        ___qtablewidgetitem55 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("Lab3", u"10.193", None));
        ___qtablewidgetitem56 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("Lab3", u"2.5", None));
        ___qtablewidgetitem57 = self.tableWidget_2.item(2, 1)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("Lab3", u"9.807", None));
        ___qtablewidgetitem58 = self.tableWidget_2.item(3, 0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("Lab3", u"3.0", None));
        ___qtablewidgetitem59 = self.tableWidget_2.item(3, 1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("Lab3", u"9.387", None));
        ___qtablewidgetitem60 = self.tableWidget_2.item(4, 0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("Lab3", u"3.5", None));
        ___qtablewidgetitem61 = self.tableWidget_2.item(4, 1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("Lab3", u"8.977", None));
        ___qtablewidgetitem62 = self.tableWidget_2.item(5, 0)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("Lab3", u"4.0", None));
        ___qtablewidgetitem63 = self.tableWidget_2.item(5, 1)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("Lab3", u"8.637", None));
        ___qtablewidgetitem64 = self.tableWidget_2.item(6, 0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("Lab3", u"4.5", None));
        ___qtablewidgetitem65 = self.tableWidget_2.item(6, 1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("Lab3", u"8.442", None));
        ___qtablewidgetitem66 = self.tableWidget_2.item(7, 0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("Lab3", u"5.0", None));
        ___qtablewidgetitem67 = self.tableWidget_2.item(7, 1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("Lab3", u"8.482", None));
        ___qtablewidgetitem68 = self.tableWidget_2.item(8, 0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("Lab3", u"5.5", None));
        ___qtablewidgetitem69 = self.tableWidget_2.item(8, 1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("Lab3", u"8.862", None));
        ___qtablewidgetitem70 = self.tableWidget_2.item(9, 0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("Lab3", u"6.0", None));
        ___qtablewidgetitem71 = self.tableWidget_2.item(9, 1)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("Lab3", u"9.701", None));
        ___qtablewidgetitem72 = self.tableWidget_2.item(10, 0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("Lab3", u"6.5", None));
        ___qtablewidgetitem73 = self.tableWidget_2.item(10, 1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("Lab3", u"11.132", None));
        ___qtablewidgetitem74 = self.tableWidget_2.item(11, 0)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("Lab3", u"7.0", None));
        ___qtablewidgetitem75 = self.tableWidget_2.item(11, 1)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("Lab3", u"13.302", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.label_7.setText(QCoreApplication.translate("Lab3", u"\u0412\u0430\u0440\u0456\u0430\u043d\u0442 2n", None))
        self.label_3.setText(QCoreApplication.translate("Lab3", u"<html><head/><body><p>\u0412\u0430\u0448\u0430 \u0442\u0430\u0431\u043b\u0438\u0446\u044f</p><p><span style=\" font-weight:400;\">.csv</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Lab3", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u0417\u0430\u0432\u0434\u0430\u043d\u043d\u044f:</span> \u0437\u0430 \u0434\u043e\u043f\u043e\u043c\u043e\u0433\u043e\u044e \u0456\u043d\u0442\u0435\u0440\u043f\u043e\u043b\u044f\u0446\u0456\u0439\u043d\u0438\u0445 \u0444\u043e\u0440\u043c\u0443\u043b \u041d\u044c\u044e\u0442\u043e\u043d\u0430 \u0437</p><p align=\"center\">\u0442\u043e\u0447\u043d\u0456\u0441\u0442\u044e \u0434\u043e 0.001 \u0437\u043d\u0430\u0439\u0442\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044f \u043f\u0435\u0440\u0448\u043e\u0457 \u0442\u0430 \u0434\u0440\u0443\u0433\u043e\u0457 \u043f\u043e\u0445\u0456\u0434\u043d\u0438\u0445 \u0437\u0430</p><p align=\"center\">\u0434\u0430\u043d\u0438\u0445 \u0437\u043d\u0430\u0447\u0435\u043d\u044c \u0430\u0440\u0433\u0443\u043c\u0435\u043d\u0442\u0443 \u0434\u043b\u044f \u0444\u0443\u043d\u043a\u0446\u0456\u0457 y = f(x), </p><p align=\"center\">\u0449\u043e \u0437\u0430\u0434\u0430\u043d\u0430 \u0442\u0430\u0431\u043b\u0438"
                        "\u0446\u0435\u044e:</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Lab3", u"\u0412\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u044e", None))
        self.label_6.setText(QCoreApplication.translate("Lab3", u"\u041b\u0430\u0431\u0430 3", None))
        self.pushButton_exp.setText("")
        self.pushButton_close.setText("")
        self.pushButton2.setText(QCoreApplication.translate("Lab3", u"\u041e\u0431\u0447\u0438\u0441\u043b\u0438\u0442\u0438", None))
        self.label_8.setText(QCoreApplication.translate("Lab3", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0442\u043e\u0447\u043a\u0443", None))
        self.lineEdit_input.setText(QCoreApplication.translate("Lab3", u"......", None))
        self.label_9.setText(QCoreApplication.translate("Lab3", u"x  = ", None))
        self.label_10.setText(QCoreApplication.translate("Lab3", u"f'(x)  \u2248", None))
        self.label_result1.setText("")
        self.label_11.setText(QCoreApplication.translate("Lab3", u"f''(x)  \u2248", None))
        self.label_result2.setText("")
        self.pushButton_right.setText(QCoreApplication.translate("Lab3", u">>", None))
        self.pushButton_left.setText(QCoreApplication.translate("Lab3", u"<<", None))
    # retranslateUi

