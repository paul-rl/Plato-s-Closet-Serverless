# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI Design/PhoneNotFoundUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 107)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 10, 194, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.phoneNotFoundLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.phoneNotFoundLabel.setObjectName("phoneNotFoundLabel")
        self.verticalLayout.addWidget(self.phoneNotFoundLabel, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.registerLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.registerLabel.setObjectName("registerLabel")
        self.horizontalLayout.addWidget(self.registerLabel)
        self.yesButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.yesButton.setObjectName("yesButton")
        self.horizontalLayout.addWidget(self.yesButton)
        self.noButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.noButton.setObjectName("noButton")
        self.horizontalLayout.addWidget(self.noButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.phoneNotFoundLabel.setText(_translate("Dialog", "Phone # not present"))
        self.registerLabel.setText(_translate("Dialog", "Register?"))
        self.yesButton.setText(_translate("Dialog", "Yes"))
        self.noButton.setText(_translate("Dialog", "No"))