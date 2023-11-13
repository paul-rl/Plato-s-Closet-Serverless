from pathlib import Path
from GUI import PhoneNotFoundGUI
from PyQt5.QtWidgets import QDialog

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

    # Currently, this is the time at which the person was registered...
    # Might need to do two different times, registered time and sent time
    def sendAddEntryMessage(self):
        self.parent().msgHandler.sendAddEntryMsg(self.inputtedPhoneNo)
        self.close()
