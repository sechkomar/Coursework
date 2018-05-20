# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog


class Ui_browseWindow(object):
    def setupUi(self, browseWindow):
        browseWindow.setObjectName("browseWindow")
        browseWindow.resize(510, 425)
        self.centralWidget = QtWidgets.QWidget(browseWindow)
        self.centralWidget.setObjectName("centralwidget")

        self.filePath = QtWidgets.QLineEdit(self.centralWidget)
        self.filePath.setGeometry(QtCore.QRect(20, 130, 331, 31))
        self.filePath.setObjectName("filePath")

        self.appDescriptionLabel = QtWidgets.QLabel(self.centralWidget)
        self.appDescriptionLabel.setGeometry(QtCore.QRect(30, 30, 421, 61))
        self.appDescriptionLabel.setObjectName("appDescription")

        self.browseFileButton = QtWidgets.QPushButton(self.centralWidget)
        self.browseFileButton.setGeometry(QtCore.QRect(360, 130, 31, 31))
        self.browseFileButton.setObjectName("browseFilePath")

        self.filePathLabel = QtWidgets.QLabel(self.centralWidget)
        self.filePathLabel.setGeometry(QtCore.QRect(20, 100, 67, 17))
        self.filePathLabel.setObjectName("filePathLabel")

        self.curveModeComboBox = QtWidgets.QComboBox(self.centralWidget)
        self.curveModeComboBox.setGeometry(QtCore.QRect(20, 210, 281, 31))
        self.curveModeComboBox.setObjectName("curveModeComboBox")
        self.curveModeComboBox.addItem("")
        self.curveModeComboBox.addItem("")
        self.curveModeComboBox.addItem("")

        self.curveModeLabel = QtWidgets.QLabel(self.centralWidget)
        self.curveModeLabel.setGeometry(QtCore.QRect(20, 180, 141, 17))
        self.curveModeLabel.setObjectName("curveModeLabel")

        self.colorsLabel = QtWidgets.QLabel(self.centralWidget)
        self.colorsLabel.setGeometry(QtCore.QRect(20, 270, 131, 17))
        self.colorsLabel.setObjectName("colorsLabel")

        self.colorsComboBox = QtWidgets.QComboBox(self.centralWidget)
        self.colorsComboBox.setGeometry(QtCore.QRect(20, 300, 281, 31))
        self.colorsComboBox.setObjectName("colorsComboBox")
        self.colorsComboBox.addItem("")
        self.colorsComboBox.addItem("")
        self.colorsComboBox.addItem("")

        self.okButton = QtWidgets.QPushButton(self.centralWidget)
        self.okButton.setGeometry(QtCore.QRect(390, 350, 101, 29))
        self.okButton.setObjectName("okButton")

        browseWindow.setCentralWidget(self.centralWidget)

        self.menubar = QtWidgets.QMenuBar(browseWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 23))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")

        browseWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(browseWindow)
        self.statusbar.setObjectName("statusbar")
        browseWindow.setStatusBar(self.statusbar)

        self.actionAbout = QtWidgets.QAction(browseWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionNew = QtWidgets.QAction(browseWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(browseWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuSave.addAction(self.actionSave)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(browseWindow)
        self.setActions()

        QtCore.QMetaObject.connectSlotsByName(browseWindow)


    def selectFile(self):
        file_path = QFileDialog.getOpenFileName()[0]
        self.filePath.setText(file_path)

    def retranslateUi(self, browseWindow):
        _translate = QtCore.QCoreApplication.translate
        browseWindow.setWindowTitle(_translate("browseWindow", "Pixel plot creator"))
        self.appDescriptionLabel.setText(_translate("browseWindow",
                                               "<html><head/><body><p><span style=\" font-size:12pt;\">Please select "
                                               "the file in .csv format, choose a curve mode </span></p><p><span "
                                               "style=\" font-size:12pt;\">and colors to create a pixel plot. "
                                               "</span></p></body></html>"))

        self.browseFileButton.setText(_translate("browseWindow", "..."))
        self.filePathLabel.setText(_translate("browseWindow", "File path"))

        self.filePath.setFont(QtGui.QFont("Noto Sans CJK TC Light", 10))

        self.curveModeComboBox.setCurrentText(_translate("browseWindow", "choose curve mode"))
        self.curveModeComboBox.setItemText(0, _translate("browseWindow", "Gorizontal mode"))
        self.curveModeComboBox.setItemText(1, _translate("browseWindow", "Hilbert curve"))
        self.curveModeComboBox.setItemText(2, _translate("browseWindow", "Morton curve"))
        self.curveModeLabel.setText(_translate("browseWindow", "Curve mode"))

        self.colorsLabel.setText(_translate("browseWindow", "Choose colors"))
        self.colorsComboBox.setCurrentText(_translate("browseWindow", "choose colors for plot"))

        self.colorsComboBox.setItemText(0, _translate("browseWindow", "red-black"))
        self.colorsComboBox.setItemText(1, _translate("browseWindow", "yellow-black"))
        self.colorsComboBox.setItemText(2, _translate("browseWindow", "random"))

        self.okButton.setText(_translate("browseWindow", "OK"))

        self.menuFile.setTitle(_translate("browseWindow", "File"))
        self.menuSave.setTitle(_translate("browseWindow", "Save"))
        self.menuHelp.setTitle(_translate("browseWindow", "Help"))
        self.menuExit.setTitle(_translate("browseWindow", "Exit"))
        self.actionAbout.setText(_translate("browseWindow", "About"))
        self.actionNew.setText(_translate("browseWindow", "New"))
        self.actionSave.setText(_translate("browseWindow", "Save"))

    def setActions(self):
        self.browseFileButton.clicked.connect(self.selectFile)
        pass
