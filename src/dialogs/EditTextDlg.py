from pathlib import Path
from GUI import EditTextMessageGUI
from PyQt5.QtWidgets import QDialog


class EditTextDlg(QDialog):
    ''' Edit Text dialog '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = EditTextMessageGUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.initializeTextEdit()

        # Connect buttons
        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.confirmButton.clicked.connect(self.confirmChanges)

    # Sets the contents of the text box with the current message that will be
    # texted to vendors.
    def initializeTextEdit(self):
        path = Path().parent.absolute()
        f = open(path / 'src' / 'assets' / 'message.txt', 'r')
        self.ui.textBox.setText(f.read())
        f.close()

    # Confirms the changes made to the message that will be texted to vendors
    # and closes the dialog
    def confirmChanges(self):
        path = Path().parent.absolute()
        f = open(path / 'src' / 'assets' / 'text.txt', 'w')
        f.write(self.ui.textBox.toPlainText())
        f.close()
        self.close()
