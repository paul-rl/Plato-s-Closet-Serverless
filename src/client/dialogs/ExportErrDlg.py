from pathlib import Path
from GUI import ExportError
from PyQt5.QtWidgets import QDialog

class ExportErrDlg(QDialog):
    ''' Export error dialog '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ExportError.Ui_Dialog()
        self.ui.setupUi(self)
