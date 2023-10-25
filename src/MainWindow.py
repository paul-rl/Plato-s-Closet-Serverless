from GUI import MainWindowGUI
from PyQt5 import QtWidgets
from PasswordEntryDlg import PasswordEntryDlg
from EditTextDlg import EditTextDlg
from ExportDlg import ExportDlg


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
        self.openPasswordDialog()
        self.openEditTextDialog()

    def openEditTextDialog(self):
        dlg = EditTextDlg(self)
        dlg.exec()
    
    def openExportDialog(self):
        dlg = ExportDlg(self)
        dlg.exec()

    def exportPhoneRegistry(self):
        self.openPasswordDialog()
        self.openExportDialog()

    def registerNumber(self):
        print("Registering")

    def openPasswordDialog(self):
        dlg = PasswordEntryDlg(self)
        dlg.exec()
