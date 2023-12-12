from PyQt5.QtWidgets import QMessageBox


def displayErrorDlg(parent, errorText):
    msg = QMessageBox(parent)
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(errorText)
    msg.setWindowTitle("Error")
    msg.exec_()