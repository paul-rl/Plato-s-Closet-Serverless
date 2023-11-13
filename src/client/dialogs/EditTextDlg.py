from GUI import EditTextMessageGUI
from PyQt5.QtWidgets import QDialog
from pathlib import Path
import sys
sys.path.insert(0, str(Path().parent.absolute() / 'src'))
import shared.textBody

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
        text = getTextBody()
        self.ui.textBox.setText(text)

    # Confirms the changes made to the message that will be texted to vendors
    # and closes the dialog
    # TODO: Ask wheter or not she wants to be able to put emojis in texts
    def confirmChanges(self):
        setTextBody(self.ui.textBox.toPlainText())
        self.close()
