import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_destinationManagerWindow(object):
    def setupUi(self, destinationManagerWindow):
        self.destinationManagerWindow = destinationManagerWindow
        font = QtGui.QFont()
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()

        destinationManagerWindow.setObjectName("destinationManagerWindow")
        destinationManagerWindow.setFixedSize(400, 650)
        self.mainWidget = QtWidgets.QWidget(destinationManagerWindow)
        self.mainWidget.setGeometry(QtCore.QRect(0, 0, 400, 650))
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
"}")
        self.mainWidget.setObjectName("mainWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Destination List
        self.destinationWidget = QtWidgets.QWidget(self.mainWidget)
        self.destinationWidget.setObjectName("destinationWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.destinationWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        font.setPointSize(14)
        self.destinationLabel = QtWidgets.QLabel(self.destinationWidget)
        self.destinationLabel.setFont(font)
        self.destinationLabel.setObjectName("destinationLabel")
        self.verticalLayout_4.addWidget(self.destinationLabel, 0, QtCore.Qt.AlignHCenter)
        self.destinationList = QtWidgets.QListWidget(self.destinationWidget)
        self.destinationList.setSelectionMode(QtWidgets.QListWidget.SingleSelection)
        self.destinationList.setObjectName("destinationList")
        self.verticalLayout_4.addWidget(self.destinationList)
        self.horizontalLayout.addWidget(self.destinationWidget)
        self.loadDestinationWidget()

        # Control Panel
        self.controlPanel = QtWidgets.QWidget(self.mainWidget)
        self.controlPanel.setMinimumSize(QtCore.QSize(180, 0))
        self.controlPanel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.controlPanel.setObjectName("controlPanel")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.controlPanel)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.searchLayout = QtWidgets.QVBoxLayout()
        self.searchLayout.setSpacing(6)
        self.searchLayout.setObjectName("searchLayout")
        self.searchLabel = QtWidgets.QLabel(self.controlPanel)
        font.setPointSize(13)
        self.searchLabel.setFont(font)
        self.searchLabel.setObjectName("searchLabel")
        self.searchLayout.addWidget(self.searchLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.searchPlainTextEdit = QtWidgets.QPlainTextEdit(self.controlPanel)
        self.searchPlainTextEdit.setMaximumSize(QtCore.QSize(150, 30))
        self.searchPlainTextEdit.textChanged.connect(self.searching)
        self.searchPlainTextEdit.setObjectName("searchPlainTextEdit")
        self.searchLayout.addWidget(self.searchPlainTextEdit, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.searchLayout)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)

        self.manageButtonsLayout = QtWidgets.QVBoxLayout()
        self.manageButtonsLayout.setObjectName("manageButtonsLayout")
        self.newButton = QtWidgets.QPushButton(self.controlPanel)
        self.newButton.setMinimumSize(QtCore.QSize(120, 25))
        self.newButton.clicked.connect(self.newClicked)
        self.newButton.setObjectName("newButton")
        self.manageButtonsLayout.addWidget(self.newButton, 0, QtCore.Qt.AlignHCenter)
        self.previewButton = QtWidgets.QPushButton(self.controlPanel)
        self.previewButton.setMinimumSize(QtCore.QSize(120, 25))
        self.previewButton.clicked.connect(self.previewClicked)
        self.previewButton.setObjectName("previewButton")
        self.manageButtonsLayout.addWidget(self.previewButton, 0, QtCore.Qt.AlignHCenter)
        self.editButton = QtWidgets.QPushButton(self.controlPanel)
        self.editButton.setMinimumSize(QtCore.QSize(120, 25))
        self.editButton.clicked.connect(self.editClicked)
        self.editButton.setObjectName("editButton")
        self.manageButtonsLayout.addWidget(self.editButton, 0, QtCore.Qt.AlignHCenter)
        self.deleteButton = QtWidgets.QPushButton(self.controlPanel)
        self.deleteButton.setMinimumSize(QtCore.QSize(120, 25))
        self.deleteButton.clicked.connect(self.deleteClicked)
        self.deleteButton.setObjectName("deleteButton")
        self.manageButtonsLayout.addWidget(self.deleteButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.manageButtonsLayout)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)

        self.addtotravelButton = QtWidgets.QPushButton(self.controlPanel)
        self.addtotravelButton.setMinimumSize(QtCore.QSize(120, 25))
        self.addtotravelButton.setObjectName("addtotravelButton")
        self.verticalLayout_3.addWidget(self.addtotravelButton, 0, QtCore.Qt.AlignHCenter)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)

        self.exitButton = QtWidgets.QPushButton(self.controlPanel)
        self.exitButton.setMinimumSize(QtCore.QSize(120, 25))
        self.exitButton.clicked.connect(self.exitClicked)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout_3.addWidget(self.exitButton, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.controlPanel)

        self.retranslateUi(destinationManagerWindow)
        QtCore.QMetaObject.connectSlotsByName(destinationManagerWindow)

    def retranslateUi(self, destinationManagerWindow):
        _translate = QtCore.QCoreApplication.translate
        destinationManagerWindow.setWindowTitle(_translate("destinationManagerWindow", "Destination Manager"))
        self.destinationLabel.setText(_translate("destinationManagerWindow", "Destination List"))
        self.searchLabel.setText(_translate("destinationManagerWindow", "Search:"))
        self.newButton.setText(_translate("destinationManagerWindow", "New"))
        self.previewButton.setText(_translate("destinationManagerWindow", "Preview"))
        self.editButton.setText(_translate("destinationManagerWindow", "Edit"))
        self.deleteButton.setText(_translate("destinationManagerWindow", "Delete"))
        self.addtotravelButton.setText(_translate("destinationManagerWindow", "Add to Travel"))
        self.exitButton.setText(_translate("destinationManagerWindow", "Exit"))
    
    def loadDestinationWidget(self, searchingText=""):
        self.cur.execute(f"SELECT name FROM destinations WHERE name LIKE '%{searchingText}%';")
        names = self.cur.fetchall()

        self.destinationList.clear()

        for n in names:
            self.destinationList.addItem(n[0])
    
    def searching(self):
        searchingText = self.searchPlainTextEdit.toPlainText().strip()
        self.loadDestinationWidget(searchingText)

    def newClicked(self):
        from DestinationAdd import Ui_destinationAddWindow

        def addClicked():

            # TODO check if all data is correct then:
            name = self.addUi.namePlainTextEdit.toPlainText().strip()
            country = self.addUi.countryPlainTextEdit.toPlainText().strip()
            town = self.addUi.townPlainTextEdit.toPlainText().strip()
            desc = self.addUi.descPlainTextEdit.toPlainText()

            self.cur.execute("INSERT INTO destinations (name,country,town,description,costs,profitability,attractions,transport,gastronomy,landscapes) VALUES (?,?,?,?,?,?,?,?,?)", (name, country, town, desc,0,0,0,0,0,0))
            self.conn.commit()
            
            self.loadDestinationWidget()

            self.addWindow.close()

        def cancelClicked():
            msg = QMessageBox()
            msg.setWindowTitle("Confirm cancel")
            msg.setText("Do you really want to cancel?")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
            msg.setDefaultButton(QMessageBox.No)
            msg.setInformativeText("Changes will not be saved!")
            choice = msg.exec_()

            if choice == QMessageBox.Yes:
                self.addWindow.close()
            else:
                return False

        self.addWindow = QtWidgets.QMainWindow()
        self.addUi = Ui_destinationAddWindow()
        self.addUi.setupUi(self.addWindow)

        screen = QtWidgets.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.addWindow.width()) // 2
        y = (screen.height() - self.addWindow.height()) // 2
        self.addWindow.move(x,y)

        self.addWindow.show()

        self.addUi.addButton.clicked.connect(addClicked)
        self.addUi.cancelButton.clicked.connect(cancelClicked)
    
    def previewClicked(self):
        from DestinationPreview import Ui_destinationPreviewWindow

        selectedItem = self.destinationList.selectedItems()[0].text()

        self.previewWindow = QtWidgets.QMainWindow()
        self.previewUi = Ui_destinationPreviewWindow()
        self.previewUi.setupUi(self.previewWindow, selectedItem)

        screen = QtWidgets.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.previewWindow.width()) // 2
        y = (screen.height() - self.previewWindow.height()) // 2
        self.previewWindow.move(x,y)

        self.previewWindow.show()
    
    def editClicked(self):
        from DestinationEdit import Ui_destinationPreviewWindow

        selectedItem = self.destinationList.selectedItems()[0].text()

        self.editWindow = QtWidgets.QMainWindow()
        self.editUi = Ui_destinationPreviewWindow()
        self.editUi.setupUi(self.editWindow, selectedItem)

        screen = QtWidgets.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.editWindow.width()) // 2
        y = (screen.height() - self.editWindow.height()) // 2
        self.editWindow.move(x,y)

        self.editWindow.show()

    def deleteClicked(self):
        # TODO for sure?
        selectedItem = self.destinationList.selectedItems()[0].text()

        self.cur.execute("DELETE FROM destinations WHERE name=?", (selectedItem,))
        self.conn.commit()

        self.loadDestinationWidget()

    def exitClicked(self):
        self.destinationManagerWindow.close()