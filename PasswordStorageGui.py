# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQtGui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Encryptor
from addDataGui import Ui_addDataDialog
from PwdChangeGui import Ui_PwdChangeDialog
from SearchDataGui import Ui_Dialog


class Ui_PasswordStorage(object):
    def __init__(self):
        super().__init__()

    def pwdChange(self):
        pwdChangeDialog = QtWidgets.QDialog()
        ui = Ui_PwdChangeDialog()
        ui.setupUi(pwdChangeDialog)
        pwdChangeDialog.show()
        ui.oldPwdLine.setText(self.pwdLine.text())
        rsps = pwdChangeDialog.exec_()
        if rsps == QtWidgets.QDialog.Accepted:
            oldpwd = ui.oldPwdLine.text()
            newpwd = ui.newPwdLine.text()
            tempEncryptor = Encryptor.Encryptor(oldpwd)
            tempEncryptor.encryptWithNewPassword(newpwd)
            self.pwdLine.setText(newpwd)
            self.LoadData()


    def deleteAllData(self):
        temp_encryptor = Encryptor.Encryptor("")
        temp_encryptor.deleteData()
        while self.DatabaseTable.rowCount() > 0:
            self.DatabaseTable.removeRow(0)


    def deleteCustomData(self):
        temp_encryptor = Encryptor.Encryptor("")
        if self.DatabaseTable.selectionModel().hasSelection():
            data_id = self.DatabaseTable.currentRow()+1
            temp_encryptor.deleteCustomData(data_id)
            print("tried to delete with id: " + str(data_id))
            self.LoadData()
        else:
            print("Select Credentials to delete")

    def addDataGui(self):
        addDataDialog = QtWidgets.QDialog()
        ui = Ui_addDataDialog()
        ui.setupUi(addDataDialog)
        addDataDialog.show()
        ui.lineEdit_4.setText(self.pwdLine.text())
        rsps = addDataDialog.exec_()
        if rsps == QtWidgets.QDialog.Accepted:
            site = ui.lineEdit.text()
            username = ui.lineEdit_2.text()
            pwd = ui.lineEdit_3.text()
            decryptPwd = ui.lineEdit_4.text()
            encryptor = Encryptor.Encryptor(decryptPwd)
            encryptor.addData(site, username, pwd)
            self.pwdLine.setText(decryptPwd)
        self.LoadData()


    def showError(self):
            errorMsg = QtWidgets.QMessageBox()
            errorMsg.setWindowTitle('Error')
            errorMsg.setIcon(QtWidgets.QMessageBox.Critical)
            errorMsg.setText('Nothing found\nMake sure the password and the parameter you have selected are correct')
            errorMsg.exec_()
            return
        
    def search(self):
        #Get all data
        #Decrypt all data with the given password and save in python dictionary (list?)
        #Search in the decrypted list for the given param 
        searchDialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(searchDialog)
        passwrd = self.pwdLine.text()
        encryptor = Encryptor.Encryptor(passwrd)
        try:    
            results = encryptor.getDecreptedData()
        except:
            print("Something Went Wrong")
            return
        queryTranslate = {
            'Site': 0, 
            'Username/Email':1
        }
        searchparam = self.searchDropdown.currentText()
        t = self.pwdLine_2.text()
        final = []
        try:
            for result in results:
                if t in result[queryTranslate[searchparam]].decode():
                    final.append(result)
        except:
            pass
        if len(final) == 0:
            self.showError()
            return
        for row_number, row_data in enumerate(final):
            ui.dataDisplayTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                ui.dataDisplayTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(data.decode()))
        searchDialog.show()

        searchDialog.exec_()


    def LoadData(self):
        passwrd = self.pwdLine.text()
        encryptor = Encryptor.Encryptor(passwrd)

        #delete existing data
        while self.DatabaseTable.rowCount() > 0:
            self.DatabaseTable.removeRow(0)

        results = encryptor.getDecreptedData()
        for row_number, row_data in enumerate(results):
            self.DatabaseTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                 self.DatabaseTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem((data.decode())))

    def setupUi(self, PasswordStorage):
        PasswordStorage.setObjectName("PasswordStorage")
        PasswordStorage.resize(680, 601)
        PasswordStorage.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(PasswordStorage)
        self.centralwidget.setObjectName("centralwidget")
        self.decryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.decryptBtn.setGeometry(QtCore.QRect(530, 390, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.decryptBtn.setFont(font)
        self.decryptBtn.setObjectName("decryptBtn")
        self.DatabaseTable = QtWidgets.QTableWidget(self.centralwidget)
        self.DatabaseTable.setGeometry(QtCore.QRect(10, 50, 651, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DatabaseTable.setFont(font)
        self.DatabaseTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.DatabaseTable.setAlternatingRowColors(True)
        self.DatabaseTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.DatabaseTable.setRowCount(0)
        self.DatabaseTable.setColumnCount(3)
        self.DatabaseTable.setObjectName("DatabaseTable")
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DatabaseTable.setHorizontalHeaderItem(2, item)
        self.DatabaseTable.verticalHeader().setMinimumSectionSize(50)
        self.searchDropdown = QtWidgets.QComboBox(self.centralwidget)
        self.searchDropdown.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchDropdown.setFont(font)
        self.searchDropdown.setObjectName("searchDropdown")
        self.searchDropdown.addItem("")
        self.searchDropdown.addItem("")
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchBtn.setGeometry(QtCore.QRect(550, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchBtn.setFont(font)
        self.searchBtn.setObjectName("searchBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 390, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 430, 651, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout.addWidget(self.addBtn)
        self.pwdChangeBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pwdChangeBtn.setFont(font)
        self.pwdChangeBtn.setObjectName("pwdChangeBtn")
        self.horizontalLayout.addWidget(self.pwdChangeBtn)
        self.delCustomBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delCustomBtn.setFont(font)
        self.delCustomBtn.setObjectName("delCustomBtn")
        self.horizontalLayout.addWidget(self.delCustomBtn)
        self.delAllBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delAllBtn.setFont(font)
        self.delAllBtn.setObjectName("delAllBtn")
        self.horizontalLayout.addWidget(self.delAllBtn)
        self.pwdLine = QtWidgets.QLineEdit(self.centralwidget)
        self.pwdLine.setGeometry(QtCore.QRect(110, 389, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pwdLine.setFont(font)
        self.pwdLine.setObjectName("pwdLine")
        self.pwdLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.pwdLine_2.setGeometry(QtCore.QRect(120, 10, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pwdLine_2.setFont(font)
        self.pwdLine_2.setObjectName("searchLine")
        PasswordStorage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PasswordStorage)
        self.statusbar.setObjectName("statusbar")
        PasswordStorage.setStatusBar(self.statusbar)

        #Changes to Automated code below


        header = self.DatabaseTable.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.decryptBtn.clicked.connect(self.LoadData)
        self.delAllBtn.clicked.connect(self.deleteAllData)
        self.addBtn.clicked.connect(self.addDataGui)
        self.delCustomBtn.clicked.connect(self.deleteCustomData)
        self.pwdChangeBtn.clicked.connect(self.pwdChange)
        self.searchBtn.clicked.connect(self.search)

        self.retranslateUi(PasswordStorage)
        QtCore.QMetaObject.connectSlotsByName(PasswordStorage)

    def retranslateUi(self, PasswordStorage):
        _translate = QtCore.QCoreApplication.translate
        PasswordStorage.setWindowTitle(_translate("PasswordStorage", "Password Storage"))
        self.decryptBtn.setText(_translate("PasswordStorage", "Decrypt"))
        item = self.DatabaseTable.horizontalHeaderItem(0)
        item.setText(_translate("PasswordStorage", "Site"))
        item = self.DatabaseTable.horizontalHeaderItem(1)
        item.setText(_translate("PasswordStorage", "Username/Email"))
        item = self.DatabaseTable.horizontalHeaderItem(2)
        item.setText(_translate("PasswordStorage", "Password"))
        self.searchDropdown.setItemText(0, _translate("PasswordStorage", "Site"))
        self.searchDropdown.setItemText(1, _translate("PasswordStorage", "Username/Email"))
        self.searchBtn.setText(_translate("PasswordStorage", "Search"))
        self.label.setText(_translate("PasswordStorage", "Password :"))
        self.addBtn.setText(_translate("PasswordStorage", "Add Data"))
        self.pwdChangeBtn.setText(_translate("PasswordStorage", "Change Password"))
        self.delCustomBtn.setText(_translate("PasswordStorage", "Delete Selected Data"))
        self.delAllBtn.setText(_translate("PasswordStorage", "Delete All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordStorage = QtWidgets.QMainWindow()
    ui = Ui_PasswordStorage()
    ui.setupUi(PasswordStorage)
    PasswordStorage.show()
    sys.exit(app.exec_())
