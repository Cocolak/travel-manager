import res
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem


class Ui_selectTravelWindow(object):
    def setupUi(self, selectTravelWindow):
        self.selectTravelWindow = selectTravelWindow
        selectTravelWindow.setObjectName("selectTravelWindow")
        selectTravelWindow.setFixedSize(400, 550)

        self.mainWidget = QtWidgets.QWidget(selectTravelWindow)
        self.mainWidget.setGeometry(QtCore.QRect(0, 0, 400, 550))
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
"QPushButton#githubButton {\n"
"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"margin:0px 10px 10px 0px;\n"
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
"}\n")
        self.mainWidget.setObjectName("mainWidget")

        # Title
        self.titleLabel = QtWidgets.QLabel(self.mainWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLayout = QtWidgets.QVBoxLayout(self.mainWidget)
        self.titleLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLayout.setSpacing(0)
        self.titleLayout.setObjectName("verticalLayout_3")
        self.titleLayout.addWidget(self.titleLabel, 0, QtCore.Qt.AlignHCenter)

        # Select Label
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.selectLabel = QtWidgets.QLabel(self.mainWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.selectLabel.setFont(font)
        self.selectLabel.setObjectName("selectLabel")
        self.verticalLayout.addWidget(self.selectLabel, 0, QtCore.Qt.AlignHCenter)

        # Travel List
        self.travelList = QtWidgets.QListWidget(self.mainWidget)
        self.travelList.setStyleSheet("")
        self.travelList.setMovement(QtWidgets.QListView.Free)
        self.travelList.setObjectName("travelList")
        self.travelList.itemClicked.connect(self.listItemClicked)
        self.verticalLayout.addWidget(self.travelList, 0, QtCore.Qt.AlignHCenter)
        self.loadTravelList()

        # or Label
        self.orLabel = QtWidgets.QLabel(self.mainWidget)
        self.orLabel.setObjectName("orLabel")
        self.verticalLayout.addWidget(self.orLabel, 0, QtCore.Qt.AlignHCenter)

        # Create Button
        self.createButton = QtWidgets.QPushButton(self.mainWidget)
        self.createButton.setMinimumSize(QtCore.QSize(130, 25))
        self.createButton.setStyleSheet("")
        self.createButton.setObjectName("createButton")
        self.createButton.clicked.connect(self.createClicked)
        self.verticalLayout.addWidget(self.createButton, 0, QtCore.Qt.AlignHCenter)
        self.titleLayout.addLayout(self.verticalLayout)

        # GitHub Button
        self.githubButton = QtWidgets.QPushButton(self.mainWidget)
        self.githubButton.setMinimumSize(QtCore.QSize(60, 50))
        self.githubButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/github-mark-white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.githubButton.setIcon(icon)
        self.githubButton.setIconSize(QtCore.QSize(46, 46))
        self.githubButton.setObjectName("githubButton")
        self.githubButton.clicked.connect(self.githubClicked)
        self.titleLayout.addWidget(self.githubButton, 0, QtCore.Qt.AlignRight)

        self.retranslateUi(selectTravelWindow)
        QtCore.QMetaObject.connectSlotsByName(selectTravelWindow)

    def retranslateUi(self, selectTravelWindow):
        _translate = QtCore.QCoreApplication.translate
        selectTravelWindow.setWindowTitle(_translate("selectTravelWindow", "Selecting Travel"))
        self.titleLabel.setText(_translate("selectTravelWindow", "Travel Manager"))
        self.selectLabel.setText(_translate("selectTravelWindow", "Select Travel from list:"))
        self.orLabel.setText(_translate("selectTravelWindow", "or"))
        self.createButton.setText(_translate("selectTravelWindow", "Create New Travel"))

    def loadTravelList(self):
        item = QListWidgetItem("Test1")
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.travelList.addItem(item)

    def createClicked(self):
        from CreateTravel import Ui_createTravelWindow

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_createTravelWindow()
        self.ui.setupUi(self.window)

        screen = QtWidgets.QDesktopWidget().screenGeometry()
        x = (screen.width() - self.window.width()) // 2
        y = (screen.height() - self.window.height()) // 2
        self.window.move(x,y)

        self.window.show()
        self.selectTravelWindow.close()

    def listItemClicked(self):
        print("Działa")

    def githubClicked(self):
        import webbrowser
        webbrowser.open('https://github.com/Cocolak')