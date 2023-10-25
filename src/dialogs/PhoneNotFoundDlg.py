from pathlib import Path
from GUI import PhoneNotFoundGUI
from PyQt5.QtWidgets import QDialog
import database
import datetime

class PhoneNotFoundDlg(QDialog):
    ''' Phone Found dialog '''
    def __init__(self, phoneNo, orderNo, parent=None):
        super().__init__(parent)
        self.ui = PhoneNotFoundGUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.inputtedPhoneNo = phoneNo
        self.inputtedOrderNo = orderNo

        # Connect buttons
        self.ui.yesButton.clicked.connect(self.addToDb)
        self.ui.noButton.clicked.connect(self.close)
        
    def addToDb(self):
        connection = database.connect()
        database.addEntry(connection, datetime.datetime.now(), phoneNo=self.inputtedPhoneNo, orderNo=self.inputtedOrderNo)
        self.close()
