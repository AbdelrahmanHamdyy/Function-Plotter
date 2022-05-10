from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QWidget, QDialog, QMainWindow, QPushButton, QLineEdit
from Graph import *
from ShowMsg import *
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        # Load Screen
        uic.loadUi('Design.ui', self)
        # Button
        self.findChild(QPushButton, "Plot").clicked.connect(self.Run)
        # Get Input from each field
        self.function = self.findChild(QLineEdit, "Function")
        self.minVal = self.findChild(QLineEdit, "Min")
        self.maxVal = self.findChild(QLineEdit, "Max")
        # Show Window
        self.show()

    # Call Graph with the 3 main parameters and plot the function
    def Run(self):
        try:
            P = Graph(self.function.text(), self.minVal.text(), self.maxVal.text())
            P.Plot()
        except ValueError as error:
            # For error messages shown and retrieved from the ValueError in the Validation Class
            ErrorMessage = error.args[0]
            ShowError(self, ErrorMessage)
            return


# Main
if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    currWindow = UI()
    sys.exit(application.exec_())
