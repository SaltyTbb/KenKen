# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QApplication,QPushButton,QMessageBox

class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 550)
        Dialog.setMinimumSize(QtCore.QSize(700, 550))
        Dialog.setMaximumSize(QtCore.QSize(700, 550))
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(50, 100, 371, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btn_clear = QtWidgets.QPushButton(Dialog)
        self.btn_clear.setGeometry(QtCore.QRect(580, 350, 93, 28))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_submit = QtWidgets.QPushButton(Dialog)
        self.btn_submit.setGeometry(QtCore.QRect(580, 310, 93, 28))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_load = QtWidgets.QPushButton(Dialog)
        self.btn_load.setGeometry(QtCore.QRect(100, 40, 93, 28))
        self.btn_load.setObjectName("btn_load")
        self.btn_solve = QtWidgets.QPushButton(Dialog)
        self.btn_solve.setGeometry(QtCore.QRect(580, 390, 93, 28))
        self.btn_solve.setObjectName("btn_solve")
        self.txt_level = QtWidgets.QTextEdit(Dialog)
        self.txt_level.setGeometry(QtCore.QRect(50, 40, 41, 31))
        self.txt_level.setObjectName("txt_level")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 21))
        self.label.setObjectName("label")
        self.btn_quit = QtWidgets.QPushButton(Dialog)
        self.btn_quit.setGeometry(QtCore.QRect(580, 430, 93, 28))
        self.btn_quit.setObjectName("btn_quit")

        self.btn_quit.clicked.connect(self.quitApp)
        self.btn_load.clicked.connect(self.loadLevel)
        self.btn_submit.clicked.connect(self.submitAnswer)
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_clear.setText(_translate("Dialog", "Clear"))
        self.btn_submit.setText(_translate("Dialog", "Submit"))
        self.btn_load.setText(_translate("Dialog", "Load Level"))
        self.btn_solve.setText(_translate("Dialog", "Solve"))
        self.txt_level.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label.setText(_translate("Dialog", "Enter a number to load level:"))
        self.btn_quit.setText(_translate("Dialog", "Quit"))

    def quitApp(self):
        ans=QMessageBox.question(self,"Quit","Sure to quit KenKen?",QMessageBox.Yes|QMessageBox.No)
        if ans==QMessageBox.Yes:
            sys.exit()

    def loadLevel(self):
        pass

    def submitAnswer(self):
        pass

    def solve(self):
        pass

    def clear(self):
        pass

