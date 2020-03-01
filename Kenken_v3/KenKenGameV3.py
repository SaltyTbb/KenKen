from KenKenUITemplate import Ui_Dialog
from KenKenGameV3Validator import Validator
import sys
import os
from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QApplication,QPushButton,QMessageBox


class Game(Ui_Dialog):

    def loadLevel(self):
        print(self.txt_level.text())
        super().loadLevel()
    
    def submitAnswer(self):
        super().submitAnswer()

    def clear(self):
        super().clear()

    def solve(self):
        super().solve()
