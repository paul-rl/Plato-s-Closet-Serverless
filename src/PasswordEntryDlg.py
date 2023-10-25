from GUI import PasswordEntryGUI
from PyQt5.QtWidgets import QDialog


class PasswordEntryDlg(QDialog):
    ''' Password entry dialog '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = PasswordEntryGUI.Ui_Dialog()
        self.ui.setupUi(self)
