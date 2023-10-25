from GUI import PasswordEntryGUI
from PyQt5.QtWidgets import QDialog


class PasswordEntryDlg(QDialog):
    ''' Password entry dialog '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = PasswordEntryGUI.Ui_Dialog()
        self.ui.setupUi(self)

        # TODO: CHANGE PASSWORD IMPLEMENTATION
        self.password = "123"
        self.passwordCorrect = False
        # Connect submit button
        self.ui.submitButton.clicked.connect(self.verifyPassword)

    def verifyPassword(self):
        self.passwordCorrect = self.ui.passwordField.text() == "123"
        if (self.passwordCorrect):
            self.close()
