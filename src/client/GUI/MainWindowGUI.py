# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI Design/MainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(373, 194)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.adminButtonsLayout = QtWidgets.QHBoxLayout()
        self.adminButtonsLayout.setObjectName("adminButtonsLayout")
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportButton.setObjectName("exportButton")
        self.adminButtonsLayout.addWidget(self.exportButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.editTextButton = QtWidgets.QPushButton(self.centralwidget)
        self.editTextButton.setObjectName("editTextButton")
        self.adminButtonsLayout.addWidget(self.editTextButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.adminButtonsLayout)
        self.vendorInfoLayout = QtWidgets.QHBoxLayout()
        self.vendorInfoLayout.setObjectName("vendorInfoLayout")
        self.VendorPhoneNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.VendorPhoneNoLabel.setObjectName("VendorPhoneNoLabel")
        self.vendorInfoLayout.addWidget(self.VendorPhoneNoLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.VendorPhoneNoInput = QtWidgets.QLineEdit(self.centralwidget)
        self.VendorPhoneNoInput.setCursorPosition(14)
        self.VendorPhoneNoInput.setObjectName("VendorPhoneNoInput")
        self.vendorInfoLayout.addWidget(self.VendorPhoneNoInput, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.vendorInfoLayout)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setObjectName("submitButton")
        self.verticalLayout.addWidget(self.submitButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 373, 21))
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
        self.VendorPhoneNoLabel.setText(_translate("MainWindow", "Vendor Phone Number:"))
        self.VendorPhoneNoInput.setInputMask(_translate("MainWindow", "(999) 999-9999"))
        self.VendorPhoneNoInput.setText(_translate("MainWindow", "() -"))
        self.submitButton.setText(_translate("MainWindow", "Verify Registration"))
