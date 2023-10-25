from GUI import MainWindowGUI
from PyQt5 import QtWidgets
from pathlib import Path
from PasswordEntryDlg import PasswordEntryDlg

class MainWindow(QtWidgets.QMainWindow, MainWindowGUI.Ui_MainWindow):
    ''' Main window of the program'''
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # Connect buttons
        self.editTextButton.clicked.connect(self.editTextMessage)
        self.exportButton.clicked.connect(self.exportPhoneRegistry)
        self.submitButton.clicked.connect(self.registerNumber)

        # Keep references of dialogues that can come from this main window
    # Function called when the edit text message button is clicked. On click, 
    # prompts the user to enter a password. On password success, the text edit 
    # dialog pops up and the user can change the text message to be sent.
    def editTextMessage(self):
        correctPassword = self.openPasswordDialog()
        if correctPassword:
            print("Password was correct!")
            openTextEditDialog()
        else:
            print("Password was incorrect!")

    def exportPhoneRegistry(self):
        print("Export Phone Registry")

    def registerNumber(self):
        print("Registering")

    def openPasswordDialog(self):
        dlg = PasswordEntryDlg(self)
        dlg.exec()
