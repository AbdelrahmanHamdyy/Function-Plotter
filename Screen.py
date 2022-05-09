# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DesignLbBHEg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize, QMetaObject, QCoreApplication, QRect
from PyQt5.QtGui import QPalette, QBrush, QColor, QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QFrame, QLabel, QSpacerItem, QSizePolicy, QLineEdit, QPushButton, \
    QMenuBar, QStatusBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1073, 736)
        palette = QPalette()
        brush = QBrush(QColor(167, 167, 167, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(850, 580))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 110))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(14)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(14)
        font1.setItalic(True)
        font1.setUnderline(False)
        self.label_3.setFont(font1)
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.gridLayout_5.addWidget(self.frame_3, 2, 0, 1, 2)

        self.Title = QFrame(self.frame)
        self.Title.setObjectName(u"Title")
        self.Title.setMaximumSize(QSize(16777215, 128))
        self.Title.setFrameShape(QFrame.NoFrame)
        self.Title.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.Title)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.label_19 = QLabel(self.Title)
        self.label_19.setObjectName(u"label_19")
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(48)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setWeight(75)
        self.label_19.setFont(font2)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_19, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 2, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.gridLayout_5.addWidget(self.Title, 0, 0, 1, 2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Input = QFrame(self.frame_2)
        self.Input.setObjectName(u"Input")
        self.Input.setMaximumSize(QSize(16777215, 525))
        self.Input.setFrameShape(QFrame.NoFrame)
        self.Input.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.Input)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.Input)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 40))
        self.lineEdit_10.setMaximumSize(QSize(96, 16777215))
        font3 = QFont()
        font3.setFamily(u"Times New Roman")
        font3.setPointSize(14)
        self.lineEdit_10.setFont(font3)

        self.gridLayout.addWidget(self.lineEdit_10, 5, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.label = QLabel(self.Input)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamily(u"Times New Roman")
        font4.setPointSize(18)
        self.label.setFont(font4)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.label_8 = QLabel(self.Input)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.Input)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(100, 30))
        self.lineEdit_7.setMaximumSize(QSize(479, 16777215))
        font5 = QFont()
        font5.setFamily(u"Times New Roman")
        font5.setPointSize(12)
        self.lineEdit_7.setFont(font5)

        self.gridLayout.addWidget(self.lineEdit_7, 1, 2, 1, 1)

        self.label_10 = QLabel(self.Input)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)

        self.gridLayout.addWidget(self.label_10, 5, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.Input)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 40))
        self.lineEdit_8.setMaximumSize(QSize(96, 16777215))
        self.lineEdit_8.setFont(font3)

        self.gridLayout.addWidget(self.lineEdit_8, 3, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 6, 1, 1, 1)

        self.gridLayout_4.addWidget(self.Input, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 98))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(140, 75))
        font6 = QFont()
        font6.setFamily(u"Times New Roman")
        font6.setPointSize(16)
        font6.setBold(True)
        font6.setWeight(75)
        self.pushButton.setFont(font6)

        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.frame_4, 1, 0, 1, 1)

        self.gridLayout_5.addWidget(self.frame_2, 1, 0, 1, 2)

        self.gridLayout_9.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1073, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Function Plotter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Guidlines", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Supported Operators: + - * / ^", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Function Format: 5*x + 2^x - 6 / x", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Function Plotter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter a valid function: ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Min value for x = ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Max value for x = ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PLOT", None))
    # retranslateUi


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
