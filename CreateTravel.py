from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from datetime import date


class Ui_createTravelWindow(object):
    def setupUi(self, createTravelWindow):
        self.createTravelWindow = createTravelWindow
        self.today = str(date.today()).split("-") # yyyy-MM-dd
        font = QtGui.QFont()

        createTravelWindow.setObjectName("createTravelWindow")
        createTravelWindow.setFixedSize(500, 500)

        self.mainWidget = QtWidgets.QWidget(createTravelWindow)
        self.mainWidget.setGeometry(QtCore.QRect(0, 0, 500, 500))
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
"QListWidget{\n"
"border:1px solid rgb(128,128,128);;\n"
"}\n"
"QListWidget::item{\n"
"background-color:rgb(72, 168, 96);\n"
"color:black;\n"
"border-bottom:1px solid black;\n"
"height:20px;\n"
"}\n"
"QListWidget::item:hover{\n"
"background-color:rgb(52, 138, 76);\n"
"}\n"
"QListWidget::item:selected{\n"
"background-color:rgb(32, 118, 56);\n"
"}\n"
"QPlainTextEdit {\n"
"border: 1px solid rgb(128,128,128);\n"
"}\n"
"QDateEdit {\n"
"border: 1px solid rgb(128,128,128);\n"
"}\n"
"QSpinBox {\n"
"border: 1px solid rgb(128,128,128);\n"
"}")
        self.mainWidget.setObjectName("mainWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Left Side
        self.widget_1 = QtWidgets.QWidget(self.mainWidget)
        self.widget_1.setObjectName("widget_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_1)
        self.verticalLayout.setObjectName("verticalLayout")

        font.setPointSize(14)
        self.destinationLabel = QtWidgets.QLabel(self.widget_1)
        self.destinationLabel.setFont(font)
        self.destinationLabel.setObjectName("destinationLabel")
        self.verticalLayout.addWidget(self.destinationLabel, 0, QtCore.Qt.AlignHCenter)

        font.setPointSize(12)
        self.destinationList = QtWidgets.QListWidget(self.widget_1)
        self.destinationList.setFont(font)
        self.destinationList.setObjectName("destinationList")
        self.verticalLayout.addWidget(self.destinationList)

        self.addButton = QtWidgets.QPushButton(self.widget_1)
        self.addButton.setMinimumSize(QtCore.QSize(0, 25))
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.addClicked)

        self.previewButton = QtWidgets.QPushButton(self.widget_1)
        self.previewButton.setMinimumSize(QtCore.QSize(0, 25))
        self.previewButton.setObjectName("previewButton")
        self.previewButton.clicked.connect(self.previewClicked)

        self.removeButton = QtWidgets.QPushButton(self.widget_1)
        self.removeButton.setMinimumSize(QtCore.QSize(0, 25))
        self.removeButton.setObjectName("removeButton")
        self.removeButton.clicked.connect(self.removeClicked)

        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setObjectName("horizontalLayout_2")
        self.buttonsLayout.addWidget(self.addButton)
        self.buttonsLayout.addWidget(self.previewButton)
        self.buttonsLayout.addWidget(self.removeButton)
        self.verticalLayout.addLayout(self.buttonsLayout)

        self.horizontalLayout.addWidget(self.widget_1)

        # Right Side
        self.widget_2 = QtWidgets.QWidget(self.mainWidget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_2.setObjectName("widget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.nameLayout = QtWidgets.QVBoxLayout()
        self.nameLayout.setSpacing(2)
        self.nameLayout.setObjectName("verticalLayout_5")
        self.nameLabel = QtWidgets.QLabel(self.widget_2)
        font.setPointSize(10)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLayout.addWidget(self.nameLabel, 0, QtCore.Qt.AlignHCenter)
        self.namePlainTextEdit = QtWidgets.QPlainTextEdit(self.widget_2)
        self.namePlainTextEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.namePlainTextEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.namePlainTextEdit.setObjectName("namePlainTextEdit")
        self.nameLayout.addWidget(self.namePlainTextEdit, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.nameLayout)
        
        self.fromLayout = QtWidgets.QVBoxLayout()
        self.fromLayout.setSpacing(2)
        self.fromLayout.setObjectName("verticalLayout_3")
        self.fromLabel = QtWidgets.QLabel(self.widget_2)
        font.setPointSize(9)
        self.fromLabel.setFont(font)
        self.fromLabel.setObjectName("fromLabel")
        self.fromLayout.addWidget(self.fromLabel, 0, QtCore.Qt.AlignHCenter)
        self.fromDateEdit = QtWidgets.QDateEdit(self.widget_2)
        self.fromDateEdit.setMinimumSize(QtCore.QSize(130, 25))
        self.fromDateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.fromDateEdit.setCalendarPopup(True)
        self.fromDateEdit.setDate(QtCore.QDate(int(self.today[0]), int(self.today[1]), int(self.today[2])))
        self.fromDateEdit.setObjectName("fromDateEdit")
        self.fromLayout.addWidget(self.fromDateEdit, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.fromLayout)

        self.toLayout = QtWidgets.QVBoxLayout()
        self.toLayout.setSpacing(2)
        self.toLayout.setObjectName("verticalLayout_4")
        self.toLabel = QtWidgets.QLabel(self.widget_2)
        font.setPointSize(9)
        self.toLabel.setFont(font)
        self.toLabel.setObjectName("toLabel")
        self.toLayout.addWidget(self.toLabel, 0, QtCore.Qt.AlignHCenter)
        self.toDateEdit = QtWidgets.QDateEdit(self.widget_2)
        self.toDateEdit.setMinimumSize(QtCore.QSize(130, 25))
        self.toDateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.toDateEdit.setReadOnly(False)
        self.toDateEdit.setCalendarPopup(True)
        self.toDateEdit.setDate(QtCore.QDate(int(self.today[0]), int(self.today[1]), int(self.today[2])))
        self.toDateEdit.setObjectName("toDateEdit")
        self.toLayout.addWidget(self.toDateEdit, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.toLayout)

        self.budgetLayout = QtWidgets.QVBoxLayout()
        self.budgetLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.budgetLayout.setSpacing(2)
        self.budgetLayout.setObjectName("verticalLayout_6")
        self.budgetLabel = QtWidgets.QLabel(self.widget_2)
        font.setPointSize(9)
        self.budgetLabel.setFont(font)
        self.budgetLabel.setObjectName("budgetLabel")
        self.budgetLayout.addWidget(self.budgetLabel, 0, QtCore.Qt.AlignHCenter)
        self.budgetSpinBox = QtWidgets.QSpinBox(self.widget_2)
        self.budgetSpinBox.setMinimumSize(QtCore.QSize(130, 25))
        self.budgetSpinBox.setStyleSheet("")
        self.budgetSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.budgetSpinBox.setSuffix("")
        self.budgetSpinBox.setPrefix("")
        self.budgetSpinBox.setMaximum(999999999)
        self.budgetSpinBox.setSingleStep(10)
        self.budgetSpinBox.setObjectName("budgetSpinBox")
        self.budgetLayout.addWidget(self.budgetSpinBox, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.budgetLayout)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.saveButton = QtWidgets.QPushButton(self.widget_2)
        self.saveButton.setMinimumSize(QtCore.QSize(130, 30))
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout_2.addWidget(self.saveButton, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.widget_2)

        self.retranslateUi(createTravelWindow)
        QtCore.QMetaObject.connectSlotsByName(createTravelWindow)

    def retranslateUi(self, createTravelWindow):
        _translate = QtCore.QCoreApplication.translate
        createTravelWindow.setWindowTitle(_translate("createTravelWindow", "Creating Travel"))
        self.destinationLabel.setText(_translate("createTravelWindow", "Destination List"))
        self.addButton.setText(_translate("createTravelWindow", "Add"))
        self.previewButton.setText(_translate("createTravelWindow", "Preview"))
        self.removeButton.setText(_translate("createTravelWindow", "Delete"))
        self.nameLabel.setText(_translate("createTravelWindow", "Travel Name : "))
        self.fromLabel.setText(_translate("createTravelWindow", "From:"))
        self.fromDateEdit.setDisplayFormat(_translate("createTravelWindow", "d/MM/yyyy"))
        self.toLabel.setText(_translate("createTravelWindow", "To:"))
        self.toDateEdit.setDisplayFormat(_translate("createTravelWindow", "d/MM/yyyy"))
        self.budgetLabel.setText(_translate("createTravelWindow", "Budget: "))
        self.saveButton.setText(_translate("createTravelWindow", "Save"))

    def addClicked(self):
        from DestinationManager import Ui_destinationManagerWindow

        def addToTravelClicked():
            selectedItem = self.destinationUi.destinationList.selectedItems()[0].text()
            item = QListWidgetItem(selectedItem)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.destinationList.addItem(item)
            self.destinationWindow.close()
            
        self.destinationWindow = QtWidgets.QMainWindow()
        self.destinationUi = Ui_destinationManagerWindow()
        self.destinationUi.setupUi(self.destinationWindow)

        screen = QtWidgets.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.destinationWindow.width()) // 2
        y = (screen.height() - self.destinationWindow.height()) // 2
        self.destinationWindow.move(x,y)

        self.destinationWindow.show()

        self.destinationUi.addtotravelButton.clicked.connect(addToTravelClicked)

    def removeClicked(self):
        selectedItem = self.destinationList.currentItem()
        self.destinationList.takeItem(self.destinationList.row(selectedItem))

    def editClicked(self):
        pass

    def previewClicked(self):
        pass

    def saveClicked(self):
        pass
