from GUI import MainWindowGUI
from PyQt5 import QtWidgets
from dialogs.PasswordEntryDlg import PasswordEntryDlg
from dialogs.EditTextDlg import EditTextDlg
from dialogs.ExportDlg import ExportDlg
from dialogs.PhoneFoundDlg import PhoneFoundDlg
from dialogs.PhoneNotFoundDlg import PhoneNotFoundDlg
import database


class MainWindow(QtWidgets.QMainWindow, MainWindowGUI.Ui_MainWindow):
    ''' Main window of the program'''
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # TODO: Don't recreate tables every time
        self.connection = database.connect()
        database.create_table(self.connection)

        # Connect buttons
        self.editTextButton.clicked.connect(self.editTextMessage)
        self.exportButton.clicked.connect(self.exportPhoneRegistry)
        self.submitButton.clicked.connect(self.registerNumber)

    # Function called when the edit text message button is clicked. On click,
    # prompts the user to enter a password. On password success, the text edit
    # dialog pops up and the user can change the text message to be sent.
    def editTextMessage(self):
        passwordCorrect = self.openPasswordDialog()
        if passwordCorrect:
            self.openEditTextDialog()

    def openEditTextDialog(self):
        dlg = EditTextDlg(self)
        dlg.exec()

    def openExportDialog(self):
        dlg = ExportDlg(self)
        dlg.exec()

    def exportPhoneRegistry(self):
        passWordCorrect = self.openPasswordDialog()
        if passWordCorrect:
            self.openExportDialog()

    def registerNumber(self):
        # Remove all non-numeric characters from phone number
        vendorPhoneNo = self.VendorPhoneNoInputField.text()
        vendorPhoneNo = ''.join(c for c in vendorPhoneNo if c.isdigit())
        
        orderNo = 0
        if database.contains(self.connection, vendorPhoneNo, orderNo):
            self.phoneFoundDialog(vendorPhoneNo, orderNo)
        else:
            self.phoneNotFoundDialog(vendorPhoneNo, orderNo)

    def phoneFoundDialog(self, phoneNo, orderNo):
        dlg = PhoneFoundDlg(phoneNo, orderNo, self)
        dlg.exec()

    def phoneNotFoundDialog(self, phoneNo, orderNo):
        dlg = PhoneNotFoundDlg(phoneNo, orderNo, self)
        dlg.exec()
    
    def openPasswordDialog(self):
        dlg = PasswordEntryDlg(self)
        dlg.exec()
        return dlg.passwordCorrect
