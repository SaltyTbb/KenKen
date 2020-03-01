from KenKenGameV3 import Game
import sys
from PySide2 import QtCore, QtWidgets

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Game()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())