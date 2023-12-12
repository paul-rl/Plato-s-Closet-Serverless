from GUI import RegisterInput
from PyQt5.QtWidgets import QDialog

class RegisterDlg(QDialog):
    ''' Register dialog '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pt = parent
        self.ui = RegisterInput.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.submit)

    def submit(self):
        self.pt.setRegisterNumber(int(self.ui.lineEdit.text()))
        self.close()
