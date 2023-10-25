from pathlib import Path
from GUI import PhoneNotFoundGUI
from PyQt5.QtWidgets import QDialog


class PhoneNotFoundDlg(QDialog):
    ''' Phone Found dialog '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = PhoneNotFoundGUI.Ui_Dialog()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.yesButton.clicked.connect(self.addToDb)
        self.ui.noButton.clicked.connect(self.close)

    def addToDb(self):
        print("Added to db")
