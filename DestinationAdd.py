from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_destinationAddWindow(object):
    def setupUi(self, destinationAddWindow):
        destinationAddWindow.setObjectName("destinationAddWindow")
        destinationAddWindow.setFixedSize(350, 250)
        self.mainWidget = QtWidgets.QWidget(destinationAddWindow)
        self.mainWidget.setGeometry(QtCore.QRect(0, 0, 350, 250))
        self.mainWidget.setStyleSheet("QWidget{\n"
"background-color:rgb(7, 25, 23);\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(72, 168, 96);\n"
"color:rgb(0,0,0);\n"
"border:none;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(52, 148, 76);\n"
"}\n"
"QPlainTextEdit {\n"
"border: 1px solid rgb(128,128,128);\n"
"}")
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Content Widget
        self.contentWidget = QtWidgets.QWidget(self.mainWidget)
        self.contentWidget.setObjectName("contentWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.contentWidget)
        self.verticalLayout.setObjectName("verticalLayout")
            # Name
        self.nameLayout = QtWidgets.QHBoxLayout()
        self.nameLayout.setObjectName("nameLayout")
        self.nameLabel = QtWidgets.QLabel(self.contentWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLayout.addWidget(self.nameLabel)
        self.namePlainTextEdit = QtWidgets.QPlainTextEdit(self.contentWidget)
        self.namePlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.namePlainTextEdit.setObjectName("namePlainTextEdit")
        self.nameLayout.addWidget(self.namePlainTextEdit)
        self.verticalLayout.addLayout(self.nameLayout)
            # Country
        self.countryLayout = QtWidgets.QHBoxLayout()
        self.countryLayout.setObjectName("countryLayout")
        self.countryLabel = QtWidgets.QLabel(self.contentWidget)
        self.countryLabel.setObjectName("countryLabel")
        self.countryLayout.addWidget(self.countryLabel)
        self.countryPlainTextEdit = QtWidgets.QPlainTextEdit(self.contentWidget)
        self.countryPlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.countryPlainTextEdit.setObjectName("countryPlainTextEdit")
        self.countryLayout.addWidget(self.countryPlainTextEdit)
        self.verticalLayout.addLayout(self.countryLayout)
            # Town
        self.townLayout = QtWidgets.QHBoxLayout()
        self.townLayout.setObjectName("townLayout")
        self.townlabel = QtWidgets.QLabel(self.contentWidget)
        self.townlabel.setObjectName("townlabel")
        self.townLayout.addWidget(self.townlabel)
        self.townPlainTextEdit = QtWidgets.QPlainTextEdit(self.contentWidget)
        self.townPlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.townPlainTextEdit.setObjectName("townPlainTextEdit")
        self.townLayout.addWidget(self.townPlainTextEdit)
        self.verticalLayout.addLayout(self.townLayout)
            # Description
        self.descLayout = QtWidgets.QHBoxLayout()
        self.descLayout.setObjectName("descLayout")
        self.descLabel = QtWidgets.QLabel(self.contentWidget)
        self.descLabel.setObjectName("descLabel")
        self.descLayout.addWidget(self.descLabel)
        self.descPlainTextEdit = QtWidgets.QPlainTextEdit(self.contentWidget)
        self.descPlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 80))
        self.descPlainTextEdit.setObjectName("descPlainTextEdit")
        self.descLayout.addWidget(self.descPlainTextEdit)
        self.verticalLayout.addLayout(self.descLayout)
        self.verticalLayout_3.addWidget(self.contentWidget)

        # Buttons Layout
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.addButton = QtWidgets.QPushButton(self.mainWidget)
        self.addButton.setMinimumSize(QtCore.QSize(100, 25))
        self.addButton.setSizeIncrement(QtCore.QSize(100, 0))
        self.addButton.setObjectName("addButton")
        self.buttonsLayout.addWidget(self.addButton, 0, QtCore.Qt.AlignHCenter)
        self.cancelButton = QtWidgets.QPushButton(self.mainWidget)
        self.cancelButton.setMinimumSize(QtCore.QSize(100, 25))
        self.cancelButton.setSizeIncrement(QtCore.QSize(100, 0))
        self.cancelButton.setObjectName("cancelButton")
        self.buttonsLayout.addWidget(self.cancelButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.buttonsLayout)

        self.retranslateUi(destinationAddWindow)
        QtCore.QMetaObject.connectSlotsByName(destinationAddWindow)

    def retranslateUi(self, destinationAddWindow):
        _translate = QtCore.QCoreApplication.translate
        destinationAddWindow.setWindowTitle(_translate("destinationAddWindow", "Adding Destination"))
        self.nameLabel.setText(_translate("destinationAddWindow", "Name:"))
        self.countryLabel.setText(_translate("destinationAddWindow", "Country:"))
        self.townlabel.setText(_translate("destinationAddWindow", "Town:"))
        self.descLabel.setText(_translate("destinationAddWindow", "Description:"))
        self.addButton.setText(_translate("destinationAddWindow", "Add"))
        self.cancelButton.setText(_translate("destinationAddWindow", "Cancel"))
