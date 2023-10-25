from GUI import MainWindowGUI
from PyQt5 import QtWidgets
from dialogs.PasswordEntryDlg import PasswordEntryDlg
from dialogs.EditTextDlg import EditTextDlg
from dialogs.ExportDlg import ExportDlg
from dialogs.PhoneFoundDlg import PhoneFoundDlg
from dialogs.PhoneNotFoundDlg import PhoneNotFoundDlg


class MainWindow(QtWidgets.QMainWindow, MainWindowGUI.Ui_MainWindow):
    ''' Main window of the program'''
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

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
        #TODO: Change how it checks if phone found
        if False:  # DB Contains phone #
            self.phoneFoundDialog()
        else:  # DB does not contain phone #
            self.phoneNotFoundDialog()
        print("Registering")

    def phoneFoundDialog(self):
        dlg = PhoneFoundDlg(self)
        dlg.exec()

    def phoneNotFoundDialog(self):
        dlg = PhoneNotFoundDlg(self)
        dlg.exec()
    
    def openPasswordDialog(self):
        dlg = PasswordEntryDlg(self)
        dlg.exec()
        return dlg.passwordCorrect
