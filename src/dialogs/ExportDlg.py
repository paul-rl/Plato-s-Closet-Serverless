from GUI import ExportGUI
from PyQt5.QtWidgets import QDialog

class ExportDlg(QDialog):
    ''' Export dialog '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ExportGUI.Ui_Dialog()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.exportButton.clicked.connect(self.export)

    # TODO: We are exporting
    def export(self):
        fromDate = self.ui.fromDateField.date().toPyDate()
        toDate = self.ui.toDateField.date().toPyDate()
        phoneNo = self.ui.phoneNoField.text()

        #database.query()
        
        print("Exported!")
        self.close()
