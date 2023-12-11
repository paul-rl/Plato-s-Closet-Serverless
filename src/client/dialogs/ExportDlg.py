from GUI import ExportGUI
from PyQt5.QtWidgets import QDialog, QFileDialog
import csv
from pathlib import Path

class ExportDlg(QDialog):
    ''' Export dialog '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ExportGUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.pt = parent

        # Connect buttons
        self.ui.exportButton.clicked.connect(self.export)

    def export(self):
        # Parse data
        fromDate = self.ui.fromDateField.date().toPyDate()
        toDate = self.ui.toDateField.date().toPyDate()
        phoneNo = self.ui.phoneNoField.text()

        results = self.pt.db.query(fromDate, toDate, phoneNo)
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV Files(*.csv)', options=options)

        if file_name:
            with open(file_name, 'w', newline='') as f:
                csvWriter = csv.writer(f)
                for row in results:
                    csvWriter.writerow(row)

                self.setWindowTitle(str(Path().parent.absolute() / file_name) + " - Phone Registry")
                self.close()
                print("Exported!")
                return True
        else:
            #TODO: There was an error exporting your file
            print("Error exporting your file")
            self.close()
            return False
