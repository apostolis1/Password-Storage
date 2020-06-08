# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchData.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(397, 357)
        self.dataDisplayTable = QtWidgets.QTableWidget(Dialog)
        self.dataDisplayTable.setGeometry(QtCore.QRect(10, 10, 381, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dataDisplayTable.setFont(font)
        self.dataDisplayTable.setObjectName("dataDisplayTable")
        self.dataDisplayTable.setColumnCount(3)
        self.dataDisplayTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataDisplayTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataDisplayTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataDisplayTable.setHorizontalHeaderItem(2, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 290, 381, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.okBtn.setFont(font)
        self.okBtn.setDefault(False)
        self.okBtn.setObjectName("okBtn")
        self.horizontalLayout.addWidget(self.okBtn)

        #Changes
        self.dataDisplayTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        header = self.dataDisplayTable.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.okBtn.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Search Results"))
        item = self.dataDisplayTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Site"))
        item = self.dataDisplayTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Username/Email"))
        item = self.dataDisplayTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Password"))
        self.okBtn.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
