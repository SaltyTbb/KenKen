# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication,QPushButton,QMessageBox

class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 550)
        Dialog.setMinimumSize(QtCore.QSize(700, 550))
        Dialog.setMaximumSize(QtCore.QSize(700, 550))
        Dialog.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.table_kenken = QtWidgets.QTableWidget(Dialog)
        self.table_kenken.setEnabled(True)
        self.table_kenken.setGeometry(QtCore.QRect(60, 90, 425, 425))
        self.table_kenken.setMinimumSize(QtCore.QSize(425, 425))
        self.table_kenken.setMaximumSize(QtCore.QSize(425, 425))
        self.table_kenken.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"font: 63 24pt \"Segoe UI Semibold\";")
        self.table_kenken.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_kenken.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table_kenken.setObjectName("table_kenken")
        self.table_kenken.setColumnCount(6)
        self.table_kenken.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.table_kenken.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kenken.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kenken.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kenken.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kenken.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kenken.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kenken.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kenken.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kenken.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kenken.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kenken.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kenken.setHorizontalHeaderItem(5, item)
        self.table_kenken.horizontalHeader().setVisible(False)
        self.table_kenken.horizontalHeader().setCascadingSectionResizes(False)
        self.table_kenken.horizontalHeader().setDefaultSectionSize(70)
        self.table_kenken.horizontalHeader().setMinimumSectionSize(70)
        self.table_kenken.verticalHeader().setVisible(False)
        self.table_kenken.verticalHeader().setDefaultSectionSize(70)
        self.btn_clear = QtWidgets.QPushButton(Dialog)
        self.btn_clear.setGeometry(QtCore.QRect(500, 480, 93, 28))
        self.btn_clear.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_submit = QtWidgets.QPushButton(Dialog)
        self.btn_submit.setGeometry(QtCore.QRect(600, 480, 93, 28))
        self.btn_submit.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.btn_submit.setObjectName("btn_submit")
        self.btn_load = QtWidgets.QPushButton(Dialog)
        self.btn_load.setGeometry(QtCore.QRect(100, 40, 93, 28))
        self.btn_load.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.btn_load.setObjectName("btn_load")
        self.btn_solve = QtWidgets.QPushButton(Dialog)
        self.btn_solve.setGeometry(QtCore.QRect(490, 20, 93, 28))
        self.btn_solve.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.btn_solve.setObjectName("btn_solve")
        self.txt_level = QtWidgets.QTextEdit(Dialog)
        self.txt_level.setGeometry(QtCore.QRect(50, 40, 41, 31))
        self.txt_level.setObjectName("txt_level")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 21))
        self.label.setObjectName("label")
        self.btn_quit = QtWidgets.QPushButton(Dialog)
        self.btn_quit.setGeometry(QtCore.QRect(600, 20, 93, 28))
        self.btn_quit.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.btn_quit.setObjectName("btn_quit")
        self.txt_cells = QtWidgets.QTextEdit(Dialog)
        self.txt_cells.setGeometry(QtCore.QRect(490, 70, 161, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_cells.setFont(font)
        self.txt_cells.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txt_cells.setObjectName("txt_cells")
        self.txt_rules = QtWidgets.QTextEdit(Dialog)
        self.txt_rules.setGeometry(QtCore.QRect(490, 230, 101, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_rules.setFont(font)
        self.txt_rules.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txt_rules.setObjectName("txt_rules")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btn_quit.clicked.connect(self.quitApp)
        self.btn_load.clicked.connect(self.loadLevel)
        self.btn_submit.clicked.connect(self.submitAnswer)
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.table_kenken.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "New Row"))
        item = self.table_kenken.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "New Row"))
        item = self.table_kenken.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "New Row"))
        item = self.table_kenken.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "New Row"))
        item = self.table_kenken.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "New Row"))
        item = self.table_kenken.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "New Row"))
        item = self.table_kenken.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "New Column"))
        item = self.table_kenken.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "New Column"))
        item = self.table_kenken.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "New Column"))
        item = self.table_kenken.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "New Column"))
        item = self.table_kenken.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "New Column"))
        item = self.table_kenken.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "New Column"))
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

