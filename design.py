# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Waitercopy.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Waiter(object):
    def setupUi(self, Waiter):
        Waiter.setObjectName("Waiter")
        Waiter.resize(736, 346)
        self.gridLayoutWidget = QtWidgets.QWidget(Waiter)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 60, 321, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.TABLES = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.TABLES.setContentsMargins(0, 0, 0, 0)
        self.TABLES.setObjectName("TABLES")
        self.check_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_3.setObjectName("check_3")
        self.TABLES.addWidget(self.check_3, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.check_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_4.setObjectName("check_4")
        self.TABLES.addWidget(self.check_4, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.check_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_2.setObjectName("check_2")
        self.TABLES.addWidget(self.check_2, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.check_1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_1.setObjectName("check_1")
        self.TABLES.addWidget(self.check_1, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_1 = QtWidgets.QLabel(Waiter)
        self.label_1.setGeometry(QtCore.QRect(160, 40, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Waiter)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 200, 321, 141))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.MENU = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.MENU.setContentsMargins(0, 0, 0, 0)
        self.MENU.setObjectName("MENU")
        self.CLOSE = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.CLOSE.setObjectName("CLOSE")
        self.MENU.addWidget(self.CLOSE, 1, 1, 1, 1)
        self.ADD = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.ADD.setObjectName("ADD")
        self.MENU.addWidget(self.ADD, 0, 1, 1, 1)
        self.SERVE = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.SERVE.setObjectName("SERVE")
        self.MENU.addWidget(self.SERVE, 0, 0, 1, 1)
        self.EXIT = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.EXIT.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.EXIT.setObjectName("EXIT")
        self.MENU.addWidget(self.EXIT, 1, 0, 1, 1)
        self.PREVIOUS = QtWidgets.QListWidget(Waiter)
        self.PREVIOUS.setGeometry(QtCore.QRect(360, 60, 341, 201))
        self.PREVIOUS.setObjectName("PREVIOUS")
        self.INPUT = QtWidgets.QLineEdit(Waiter)
        self.INPUT.setGeometry(QtCore.QRect(360, 280, 241, 25))
        self.INPUT.setText("")
        self.INPUT.setObjectName("INPUT")
        self.ENTER = QtWidgets.QPushButton(Waiter)
        self.ENTER.setGeometry(QtCore.QRect(610, 280, 91, 25))
        self.ENTER.setObjectName("ENTER")
        self.label_2 = QtWidgets.QLabel(Waiter)
        self.label_2.setGeometry(QtCore.QRect(450, 30, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.RELOAD = QtWidgets.QPushButton(Waiter)
        self.RELOAD.setGeometry(QtCore.QRect(680, 30, 21, 25))
        self.RELOAD.setObjectName("RELOAD")

        self.retranslateUi(Waiter)
        QtCore.QMetaObject.connectSlotsByName(Waiter)

    def retranslateUi(self, Waiter):
        _translate = QtCore.QCoreApplication.translate
        Waiter.setWindowTitle(_translate("Waiter", "Waiter"))
        self.check_3.setText(_translate("Waiter", "3"))
        self.check_4.setText(_translate("Waiter", "4"))
        self.check_2.setText(_translate("Waiter", "2"))
        self.check_1.setText(_translate("Waiter", "1"))
        self.label_1.setText(_translate("Waiter", "Tables"))
        self.CLOSE.setText(_translate("Waiter", "Close Table"))
        self.ADD.setText(_translate("Waiter", "Add order"))
        self.SERVE.setText(_translate("Waiter", "Serve"))
        self.EXIT.setText(_translate("Waiter", "Exit"))
        self.ENTER.setText(_translate("Waiter", "Enter"))
        self.label_2.setText(_translate("Waiter", "Previous orders"))
        self.RELOAD.setText(_translate("Waiter", "R"))