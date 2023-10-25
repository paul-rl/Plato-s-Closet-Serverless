from GUI.MainWindowGUI import Ui_MainWindow
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # Connect buttons
        self.editTextButton.clicked.connect(self.editTextMessage)
        self.exportButton.clicked.connect(self.exportPhoneRegistry)
        self.submitButton.clicked.connect(self.registerNumber)

    def editTextMessage(self):
        print("Edit text message")

    def exportPhoneRegistry(self):
        print("Export Phone Registry")

    def registerNumber(self):
        print("Registering")