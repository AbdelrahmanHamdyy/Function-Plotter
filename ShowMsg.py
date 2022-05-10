from PyQt5.QtWidgets import QMessageBox


# Message Box
def ShowError(self, msg):
    QMessageBox.critical(self, "Error", msg)
