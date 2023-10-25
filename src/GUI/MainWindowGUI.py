# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 225)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 362, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.adminButtonsLayout = QtWidgets.QHBoxLayout()
        self.adminButtonsLayout.setObjectName("adminButtonsLayout")
        self.exportButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exportButton.setObjectName("exportButton")
        self.adminButtonsLayout.addWidget(self.exportButton)
        self.editTextButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.editTextButton.setObjectName("editTextButton")
        self.adminButtonsLayout.addWidget(self.editTextButton)
        self.verticalLayout.addLayout(self.adminButtonsLayout)
        self.vendorInfoLayout = QtWidgets.QHBoxLayout()
        self.vendorInfoLayout.setObjectName("vendorInfoLayout")
        self.VendorPhoneNo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.VendorPhoneNo.setObjectName("VendorPhoneNo")
        self.vendorInfoLayout.addWidget(self.VendorPhoneNo)
        self.VendorPhoneNoInputField = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.VendorPhoneNoInputField.setObjectName("VendorPhoneNoInputField")
        self.vendorInfoLayout.addWidget(self.VendorPhoneNoInputField)
        self.verticalLayout.addLayout(self.vendorInfoLayout)
        self.submitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.submitButton.setObjectName("submitButton")
        self.verticalLayout.addWidget(self.submitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 401, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exportButton.setText(_translate("MainWindow", "Export Phone Registry"))
        self.editTextButton.setText(_translate("MainWindow", "Edit Text Message"))
        self.VendorPhoneNo.setText(_translate("MainWindow", "Vendor Phone Number:"))
        self.VendorPhoneNoInputField.setPlaceholderText(_translate("MainWindow", "(XXX) XXX-XXXX"))
        self.submitButton.setText(_translate("MainWindow", "Check if this number is registered"))
