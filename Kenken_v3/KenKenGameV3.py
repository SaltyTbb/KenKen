from KenKenUITemplate import Ui_Dialog
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


def validateAnswer(answer, rule):
    # answer: list of string of user input|| rule: string of rule
    operater = rule[-1]
    expectedAnswer = int(rule[:-1])
    if(operater == '+'):
        total = 0
        for num in answer:
            total += int(num)
        return total == expectedAnswer

        """
        the for-loop can be replaced by
        return sum(list(map(lambda x: int(x), answer))) == expectedAnswer
        """

    elif(operater == '-'):
        num1 = int(answer[0])
        num2 = int(answer[1])
        return abs(num1-num2) == expectedAnswer

    elif(operater == '*'):
        total = 1
        for num in answer:
            total *= int(num)
        return total == expectedAnswer

    elif(operater == '/'):
        num1 = int(answer[0])
        num2 = int(answer[1])
        if(num1/num2 == expectedAnswer or num2/num1 == expectedAnswer):
            return True
        return False  # using else does the same thing here
    return False # this line should never be reached