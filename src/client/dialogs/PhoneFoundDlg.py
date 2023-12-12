from datetime import datetime
from GUI import PhoneFoundGUI
from PyQt5.QtWidgets import QDialog


class PhoneFoundDlg(QDialog):
    ''' Phone Found dialog '''
    def __init__(self, phoneNo, parent=None):
        super().__init__(parent)
        self.ui = PhoneFoundGUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.inputtedPhoneNo = phoneNo
        
        # Connect buttons
        self.ui.yesButton.clicked.connect(self.sendText)
        self.ui.noButton.clicked.connect(self.close)

    def sendText(self):
        self.parent().textClient.sendTextMessage(self.inputtedPhoneNo)
        self.parent().db.reportMessage(self.inputtedPhoneNo, datetime.now())
        print("Sent Text to " + self.inputtedPhoneNo)
        self.close()
