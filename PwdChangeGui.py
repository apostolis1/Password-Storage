# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PwdChange.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PwdChangeDialog(object):
    def setupUi(self, PwdChangeDialog):
        PwdChangeDialog.setObjectName("PwdChangeDialog")
        PwdChangeDialog.resize(387, 275)
        self.buttonBox = QtWidgets.QDialogButtonBox(PwdChangeDialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(PwdChangeDialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 371, 211))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.oldPwdLine = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.oldPwdLine.setFont(font)
        self.oldPwdLine.setObjectName("oldPwdLine")
        self.gridLayout.addWidget(self.oldPwdLine, 0, 1, 1, 1)
        self.newPwdLine = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newPwdLine.setFont(font)
        self.newPwdLine.setObjectName("newPwdLine")
        self.gridLayout.addWidget(self.newPwdLine, 1, 1, 1, 1)

        self.retranslateUi(PwdChangeDialog)
        self.buttonBox.accepted.connect(PwdChangeDialog.accept)
        self.buttonBox.rejected.connect(PwdChangeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PwdChangeDialog)

    def retranslateUi(self, PwdChangeDialog):
        _translate = QtCore.QCoreApplication.translate
        PwdChangeDialog.setWindowTitle(_translate("PwdChangeDialog", "Change Password"))
        self.label.setText(_translate("PwdChangeDialog", "Old Password"))
        self.label_2.setText(_translate("PwdChangeDialog", "New Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PwdChangeDialog = QtWidgets.QDialog()
    ui = Ui_PwdChangeDialog()
    ui.setupUi(PwdChangeDialog)
    PwdChangeDialog.show()
    sys.exit(app.exec_())
