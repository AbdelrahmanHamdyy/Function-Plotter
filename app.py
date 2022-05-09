from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QWidget, QDialog, QMainWindow, QPushButton, QLineEdit
from Graph import *
from ShowMsg import *
import sys


class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('Design.ui', self)
        self.findChild(QPushButton, "Plot").clicked.connect(self.Run)
        self.function = self.findChild(QLineEdit, "Function")
        self.minVal = self.findChild(QLineEdit, "Min")
        self.maxVal = self.findChild(QLineEdit, "Max")
        self.show()

    def Run(self):
        try:
            P = Graph(self.function.text(), self.minVal.text(), self.maxVal.text())
            P.Plot()
        except ValueError as error:
            ErrorMessage = error.args[0]
            ShowError(self, ErrorMessage)
            return


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    currWindow = UI()
    sys.exit(application.exec_())
