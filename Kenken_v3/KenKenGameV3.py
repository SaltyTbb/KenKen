from KenKenUITemplate import Ui_Dialog
from KenKenGameV3Validator import Validator
from KenKenGameV3Level import Level
import math
from PySide2 import QtCore, QtWidgets,QtGui
from PySide2.QtWidgets import QApplication,QPushButton,QMessageBox


class Game(Ui_Dialog):

    level=Level({},"")
    colorCoding={}
    possibleSolutions=[]

    def loadLevel(self):
        
        super().loadLevel()
        levelInput=int(self.txt_level.toPlainText())
        
        
        file=open("./level/lvl_{}.txt".format(levelInput))
        rules=file.readline().strip().split(' ')
        cells=file.readline()
        
        rulesDict={rule.split('=')[0]:rule.split('=')[1] for rule in rules}
        self.level=Level(rulesDict,cells)

        self.table_kenken.setColumnCount(self.level.size)
        self.table_kenken.setRowCount(self.level.size)
        self.initCells(cells)

        displayedCell=""
        
        for index in range(len(cells)):
            displayedCell+=cells[index]+" "
            if (index+1)%self.level.size==0:
                displayedCell+="\n"
            

        self.txt_cells.setText(displayedCell)
        self.txt_rules.setText("\n".join(rules))

        
    
    def submitAnswer(self):
        super().submitAnswer()
        cells=self.level.cells
        
        try:
            answerInput=self.loadAnswer() #{'a':[1,2,3],'b':[2,4],...}
        except:
            QMessageBox.about(self,"Sorry :(","Your input is invalid, try again!")
            return

        if(self.validateAnswer(answerInput)):
            QMessageBox.about(self,"Congratulations","Your answer is perfect!")
        else:
            QMessageBox.about(self,"Sorry :(","Your answer is wrong, try harder!")

    
            

    def clear(self):
        super().clear()
        for y in range(self.level.size):
            for x in range(self.level.size):
                self.table_kenken.item(x,y).setText(' ')

    def solve(self):
        super().solve()
        initSolution='0'*len(self.level.cells)

        self.findAllSolutions(initSolution)
        solution=None
        for possibleSolution in self.possibleSolutions:
            if self.isTrueSolution(possibleSolution):
                solution=possibleSolution
                break
        
        size=self.level.size
        for index in range(len(solution)):
            self.table_kenken.item(index//size,index%size).setText(solution[index])
        
    def isTrueSolution(self,solution):
        answerInput={}
        for index in range(len(solution)):
            cell=self.level.cells[index]
            answer=solution[index]
            if cell not in answerInput:
                answerInput[cell]=[]
            answerInput[cell].append(answer)

        return self.validateAnswer(answerInput)

    def validateAnswer(self,answerInput):
        validator=Validator()
        for cell in answerInput:
            rule=self.level.rules[cell]
            if not validator.validateAnswer(answerInput[cell],rule):
                return False
        return True

    def initCells(self,cells):
        
        self.loadColor()

        size=self.level.size

        for index in range(len(cells)):
            cell=cells[index]
            self.table_kenken.setItem(index//size, index%size, QtWidgets.QTableWidgetItem())
            self.table_kenken.item(index//size,index%size).setBackground(QtGui.QColor(*self.colorCoding[cell]))

    def loadAnswer(self):
        answerInput={}
        cells=self.level.cells
        size=self.level.size
        for index in range(len(cells)):
            cell=cells[index]
            answer=int(self.table_kenken.item(index//size,index%size).text())
            if cell not in answerInput:
                answerInput[cell]=[]
            answerInput[cell].append(answer)
        return answerInput#{'a':[1,2,3],'b':[2,4],...}
        
    def findAllSolutions(self,currSolution):
        currIndex=currSolution.find('0')
        size=self.level.size
        if(currIndex==-1):
            self.possibleSolutions.append(currSolution)
        else:
            excludedNumbers={currSolution[index] for index in range(len(currSolution)) if currIndex % size == index % size or currIndex // size == index // size}
            for number in set('123456789'[:size])-excludedNumbers:
                self.findAllSolutions(currSolution[:currIndex] + number + currSolution[currIndex+1:])
        

    def loadColor(self):
        colorPool="""\
100 100 222,\
119 38 187,\
195 35 57,\
149 69 160,\
199 167 76,\
175 110 93,\
248 138 30,\
198 255 29,\
86 137 161,\
2 109 20,\
197 157 155,\
180 73 241,\
244 83 210,\
20 253 196,\
217 122 166,\
27 216 34,\
123 130 180,\
118 177 48,\
132 229 1,\
73 222 168,\
244 72 228,\
63 17 236,\
75 38 157,\
70 246 220,\
70 56 52,\
167 183 4"""
        colors=colorPool.split(',')
        for index in range(26):
            letter=chr(ord('a')+index)
            self.colorCoding[letter]=[int(color) for color in colors[index].split(' ')]
        