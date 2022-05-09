from PyQt5.QtWidgets import QMessageBox


def ShowError(self, msg):
    QMessageBox.critical(self, "Error", msg)
