# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addData.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addDataDialog(object):
    def setupUi(self, addDataDialog):
        addDataDialog.setObjectName("addDataDialog")
        addDataDialog.resize(534, 409)
        self.gridLayout = QtWidgets.QGridLayout(addDataDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(addDataDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(addDataDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(addDataDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(addDataDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(addDataDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(addDataDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(addDataDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(addDataDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(addDataDialog)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 4)

        self.retranslateUi(addDataDialog)
        self.buttonBox.accepted.connect(addDataDialog.accept)
        self.buttonBox.rejected.connect(addDataDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(addDataDialog)

    def retranslateUi(self, addDataDialog):
        _translate = QtCore.QCoreApplication.translate
        addDataDialog.setWindowTitle(_translate("addDataDialog", "Add Credentials"))
        self.label_3.setText(_translate("addDataDialog", "Password"))
        self.label.setText(_translate("addDataDialog", "Site"))
        self.label_2.setText(_translate("addDataDialog", "Username/Email"))
        self.label_4.setText(_translate("addDataDialog", "Decryption Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addDataDialog = QtWidgets.QDialog()
    ui = Ui_addDataDialog()
    ui.setupUi(addDataDialog)
    addDataDialog.show()
    sys.exit(app.exec_())
