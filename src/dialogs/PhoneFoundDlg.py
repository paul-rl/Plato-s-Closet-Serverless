from pathlib import Path
from GUI import PhoneFoundGUI
from PyQt5.QtWidgets import QDialog


class PhoneFoundDlg(QDialog):
    ''' Phone Found dialog '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = PhoneFoundGUI.Ui_Dialog()
        self.ui.setupUi(self)
        
        # Connect buttons
        self.ui.yesButton.clicked.connect(self.sendText)
        self.ui.noButton.clicked.connect(self.close)

    def sendText(self):
        print("Sent Text")
