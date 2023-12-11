import typing
from GUI import MainWindowGUI
from PyQt5 import QtGui, QtWidgets, QtCore
from dialogs.PasswordEntryDlg import PasswordEntryDlg
from dialogs.EditTextDlg import EditTextDlg
from dialogs.ExportDlg import ExportDlg
from dialogs.PhoneFoundDlg import PhoneFoundDlg
from dialogs.PhoneNotFoundDlg import PhoneNotFoundDlg
from clientMessagingHandler import ClientMessagingHandler
from database import Database
from messaging import TextingClient


# TODO: Send message to server to sever connection on window close
class MainWindow(QtWidgets.QMainWindow, MainWindowGUI.Ui_MainWindow):
    ''' Main window of the program'''
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setupUi(self)

        self.db = Database()
        self.textClient = TextingClient()
        

        # Connect buttons
        self.editTextButton.clicked.connect(self.editTextMessage)
        self.exportButton.clicked.connect(self.exportPhoneRegistry)
        self.submitButton.clicked.connect(self.registerNumber)

        # Set event filter for vendor # cursor position
        self.VendorPhoneNoInput.installEventFilter(self)
    
    def eventFilter(self, source, event):
        if source == self.VendorPhoneNoInput and event.type() == QtCore.QEvent.MouseButtonPress:
            self.VendorPhoneNoInput.setFocus(QtCore.Qt.MouseFocusReason)
            self.VendorPhoneNoInput.setCursorPosition(0)
            return True
        return super().eventFilter(source, event)

    # Function called when the edit text message button is clicked. On click,
    # prompts the user to enter a password. On password success, the text edit
    # dialog pops up and the user can change the text message to be sent.
    def editTextMessage(self):
        passwordCorrect = self.openPasswordDialog()
        if passwordCorrect:
            self.openEditTextDialog()

    # Function called after successful password input. The text message sent to 
    # users can be edited from the provided dialog
    def openEditTextDialog(self):
        dlg = EditTextDlg(self)
        dlg.exec()

    # Function called when the export phone registry button is clicked.
    # On click, prompts the user to enter a password. On a success,
    # the export dialog pops up. On a failure, the password dialog closes.
    def exportPhoneRegistry(self):
        passWordCorrect = self.openPasswordDialog()
        if passWordCorrect:
            self.openExportDialog()

    # Function called after successful password input. Allows exporting
    # database information.
    def openExportDialog(self):
        dlg = ExportDlg(self)
        dlg.exec()

    def registerNumber(self):
        print("Registering")
        # Remove all non-numeric characters from phone number
        vendorPhoneNo = self.VendorPhoneNoInput.text().strip()
        vendorPhoneNo = ''.join(c for c in vendorPhoneNo if c.isdigit())

        # Clear input fields
        self.VendorPhoneNoInput.setText("")

        if len(vendorPhoneNo) == 10:
            result = self.db.query(phoneNo=vendorPhoneNo)
            if result:
                self.phoneFoundDialog(vendorPhoneNo)
            else:
                self.phoneNotFoundDialog(vendorPhoneNo)
        else:
            print("Please provide a valid phone #")

    def phoneFoundDialog(self, phoneNo):
        dlg = PhoneFoundDlg(phoneNo, self)
        dlg.exec()

    def phoneNotFoundDialog(self, phoneNo):
        dlg = PhoneNotFoundDlg(phoneNo, self)
        dlg.exec()

    def openPasswordDialog(self):
        dlg = PasswordEntryDlg(self)
        dlg.exec()
        return dlg.passwordCorrect
