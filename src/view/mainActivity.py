from PyQt5 import uic

from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtGui

from src.controller.mainActivityController import MainActivityController
from src.util.configUtil import ConfigUtil

class MainActivity(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainActivity, self).__init__()
        
        print('@Debug: MainActivity init...')

        config = ConfigUtil(configType="APPLICATION")
        self.activityController = MainActivityController()
        
        uic.loadUi(config.getApplicationResoucePath() + config.getApplicationResourceByName(resourceName='ui_mainactivity_name'), self)

        self.resultLabel = self.findChild(QtWidgets.QLabel, 'result_label')
        self.departmentLabel = self.findChild(QtWidgets.QLabel, 'department_label')
        self.departmentSpecifiedLabel = self.findChild(QtWidgets.QLabel, 'department_specified_label')

        self.departmentLabel.setText('&' + self.departmentLabel.text())
        self.departmentSpecifiedLabel.setText('&' + self.departmentSpecifiedLabel.text())

        self.departmentLineEdit = self.findChild(QtWidgets.QLineEdit, 'department_lineEdit')
        self.departmentSpecifiedLineEdit = self.findChild(QtWidgets.QLineEdit, 'department_specified_lineEdit')

        self.searchPushButton = self.findChild(QtWidgets.QPushButton, 'search_pushButton')
        self.cancelPushButton = self.findChild(QtWidgets.QPushButton, 'cancel_pushButton')

        self.searchResultTableWidget = self.findChild(QtWidgets.QTableWidget, 'search_result_tableWidget')
        ## Reduce Id column width
        self.searchResultTableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.searchResultTableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.searchResultTableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        
        self.searchPushButton.clicked.connect(self.searchPushButtonClick)
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClick)

        self.departmentLabel.setBuddy(self.departmentLineEdit)
        self.departmentSpecifiedLabel.setBuddy(self.departmentSpecifiedLineEdit)

        self.show()


    def searchPushButtonClick(self):
        result = self.activityController.handleSearchButtonAction(self.departmentLineEdit.text(), self.departmentSpecifiedLineEdit.text())
        self.searchResultTableWidget.setRowCount(0)

        if result != None:
            for rowCount, rowData in enumerate(result):
                print('@Debug: Compiling tableResult...')
                self.searchResultTableWidget.insertRow(rowCount)
                for columnCount, data in enumerate(rowData):
                    self.searchResultTableWidget.setItem(rowCount, columnCount, QtWidgets.QTableWidgetItem(str(data)))
        
        self.resultLabel.setText(self.activityController.getResultCount(self.searchResultTableWidget.rowCount()))

    def cancelPushButtonClick(self):
        self.departmentLineEdit.clear()
        self.departmentSpecifiedLineEdit.clear()
        self.searchResultTableWidget.setRowCount(0)
        self.resultLabel.setText(self.activityController.getResultCount(0))