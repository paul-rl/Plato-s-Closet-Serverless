from GUI import PhoneFoundGUI
from PyQt5.QtWidgets import QDialog


# TODO: Make this send message to server
class PhoneFoundDlg(QDialog):
    ''' Phone Found dialog '''
    def __init__(self, phoneNo, orderNo, parent=None):
        super().__init__(parent)
        self.ui = PhoneFoundGUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.inputtedPhoneNo = phoneNo
        self.inputtedOrderNo = orderNo
        
        # Connect buttons
        self.ui.yesButton.clicked.connect(self.sendText)
        self.ui.noButton.clicked.connect(self.close)

    def sendText(self):
        self.parent().msgHandler.sendSendTextMsg(self.inputtedPhoneNo)
        print("Sent Text to " + self.inputtedPhoneNo)
        self.close()
