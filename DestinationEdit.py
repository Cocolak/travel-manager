import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_destinationPreviewWindow(object):
    def setupUi(self, destinationPreviewWindow, selectedItem):
        self.destinationPreviewWindow = destinationPreviewWindow
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()
        self.selectedItem = selectedItem

        destinationPreviewWindow.setObjectName("destinationPreviewWindow")
        destinationPreviewWindow.setFixedSize(350, 480)
        self.mainWidget = QtWidgets.QWidget(destinationPreviewWindow)
        self.mainWidget.setGeometry(QtCore.QRect(0, 0, 350, 480))
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

            # Name
        self.nameLayout = QtWidgets.QHBoxLayout()
        self.nameLayout.setObjectName("nameLayout")
        self.nameLabel = QtWidgets.QLabel(self.mainWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLayout.addWidget(self.nameLabel)
        self.namePlainTextEdit = QtWidgets.QPlainTextEdit(self.mainWidget)
        self.namePlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.namePlainTextEdit.setObjectName("namePlainTextEdit")
        self.nameLayout.addWidget(self.namePlainTextEdit)
        self.verticalLayout.addLayout(self.nameLayout)

            # Country
        self.countryLayout = QtWidgets.QHBoxLayout()
        self.countryLayout.setObjectName("countryLayout")
        self.countryLabel = QtWidgets.QLabel(self.mainWidget)
        self.countryLabel.setObjectName("countryLabel")
        self.countryLayout.addWidget(self.countryLabel)
        self.countryPlainTextEdit = QtWidgets.QPlainTextEdit(self.mainWidget)
        self.countryPlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.countryPlainTextEdit.setObjectName("countryPlainTextEdit")
        self.countryLayout.addWidget(self.countryPlainTextEdit)
        self.verticalLayout.addLayout(self.countryLayout)

            # Town
        self.townLayout = QtWidgets.QHBoxLayout()
        self.townLayout.setObjectName("townLayout")
        self.townLabel = QtWidgets.QLabel(self.mainWidget)
        self.townLabel.setObjectName("townLabel")
        self.townLayout.addWidget(self.townLabel)
        self.townPlainTextEdit = QtWidgets.QPlainTextEdit(self.mainWidget)
        self.townPlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.townPlainTextEdit.setObjectName("townPlainTextEdit")
        self.townLayout.addWidget(self.townPlainTextEdit)
        self.verticalLayout.addLayout(self.townLayout)

            # Description
        self.descLayout = QtWidgets.QHBoxLayout()
        self.descLayout.setObjectName("descLayout")
        self.descLabel = QtWidgets.QLabel(self.mainWidget)
        self.descLabel.setObjectName("descLabel")
        self.descLayout.addWidget(self.descLabel)
        self.descPlainTextEdit = QtWidgets.QPlainTextEdit(self.mainWidget)
        self.descPlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 80))
        self.descPlainTextEdit.setObjectName("descPlainTextEdit")
        self.descLayout.addWidget(self.descPlainTextEdit)
        self.verticalLayout.addLayout(self.descLayout)

        self.max_stars = 5

            # Costs
        self.costsLayout = QtWidgets.QHBoxLayout()
        self.costsLayout.setObjectName("costsLayout")
        self.costsLabel = QtWidgets.QLabel(self.mainWidget)
        self.costsLabel.setObjectName("costsLabel")
        self.costsLayout.addWidget(self.costsLabel, 0, QtCore.Qt.AlignHCenter)
        self.costsStarsLayout = QtWidgets.QHBoxLayout()
        self.costsStarsLayout.setSpacing(3)
        self.costsStarsLayout.setObjectName("costsStarsLayout")
        
        self.costsStarButtons = []
        for s in range(self.max_stars):
            starButton = QtWidgets.QPushButton("★", self.mainWidget)
            starButton.setMinimumSize(QtCore.QSize(30, 30))
            starButton.setMaximumSize(QtCore.QSize(30, 30))
            starButton.clicked.connect(lambda: self.onStarClicked(self.costsStarButtons))
            self.costsStarButtons.append(starButton)
            self.costsStarsLayout.addWidget(starButton)

        self.costsLayout.addLayout(self.costsStarsLayout)
        self.verticalLayout.addLayout(self.costsLayout)

            # Profitability
        self.profitabilityLayout = QtWidgets.QHBoxLayout()
        self.profitabilityLayout.setObjectName("profitabilityLayout")
        self.profitabilityLabel = QtWidgets.QLabel(self.mainWidget)
        self.profitabilityLabel.setObjectName("profitabilityLabel")
        self.profitabilityLayout.addWidget(self.profitabilityLabel, 0, QtCore.Qt.AlignHCenter)
        self.profitabilityStarsLayout = QtWidgets.QHBoxLayout()
        self.profitabilityStarsLayout.setSpacing(3)
        self.profitabilityStarsLayout.setObjectName("profitabilityStarsLayout")
        
        self.profitabilityStarButtons = []
        for s in range(self.max_stars):
            starButton = QtWidgets.QPushButton("★", self.mainWidget)
            starButton.setMinimumSize(QtCore.QSize(30, 30))
            starButton.setMaximumSize(QtCore.QSize(30, 30))
            starButton.clicked.connect(lambda: self.onStarClicked(self.profitabilityStarButtons))
            self.profitabilityStarButtons.append(starButton)
            self.profitabilityStarsLayout.addWidget(starButton)

        self.profitabilityLayout.addLayout(self.profitabilityStarsLayout)
        self.verticalLayout.addLayout(self.profitabilityLayout)

            # Attractions
        self.attractionsLayout = QtWidgets.QHBoxLayout()
        self.attractionsLayout.setObjectName("attractionsLayout")
        self.attractionsLabel = QtWidgets.QLabel(self.mainWidget)
        self.attractionsLabel.setObjectName("attractionsLabel")
        self.attractionsLayout.addWidget(self.attractionsLabel, 0, QtCore.Qt.AlignHCenter)
        self.attractionsStarsLayout = QtWidgets.QHBoxLayout()
        self.attractionsStarsLayout.setSpacing(3)
        self.attractionsStarsLayout.setObjectName("attractionsStarsLayout")
        
        self.attractionsStarButtons = []
        for s in range(self.max_stars):
            starButton = QtWidgets.QPushButton("★", self.mainWidget)
            starButton.setMinimumSize(QtCore.QSize(30, 30))
            starButton.setMaximumSize(QtCore.QSize(30, 30))
            starButton.clicked.connect(lambda: self.onStarClicked(self.attractionsStarButtons))
            self.attractionsStarButtons.append(starButton)
            self.attractionsStarsLayout.addWidget(starButton)

        self.attractionsLayout.addLayout(self.attractionsStarsLayout)
        self.verticalLayout.addLayout(self.attractionsLayout)

            # Transport
        self.transportLayout = QtWidgets.QHBoxLayout()
        self.transportLayout.setObjectName("transportLayout")
        self.transportLabel = QtWidgets.QLabel(self.mainWidget)
        self.transportLabel.setObjectName("transportLabel")
        self.transportLayout.addWidget(self.transportLabel, 0, QtCore.Qt.AlignHCenter)
        self.transportStarsLayout = QtWidgets.QHBoxLayout()
        self.transportStarsLayout.setSpacing(3)
        self.transportStarsLayout.setObjectName("transportStarsLayout")
        
        self.transportStarButtons = []
        for s in range(self.max_stars):
            starButton = QtWidgets.QPushButton("★", self.mainWidget)
            starButton.setMinimumSize(QtCore.QSize(30, 30))
            starButton.setMaximumSize(QtCore.QSize(30, 30))
            starButton.clicked.connect(lambda: self.onStarClicked(self.transportStarButtons))
            self.transportStarButtons.append(starButton)
            self.transportStarsLayout.addWidget(starButton)

        self.transportLayout.addLayout(self.transportStarsLayout)
        self.verticalLayout.addLayout(self.transportLayout)

            # Gastronomy
        self.gastronomyLayout = QtWidgets.QHBoxLayout()
        self.gastronomyLayout.setObjectName("gastronomyLayout")
        self.gastronomyLabel = QtWidgets.QLabel(self.mainWidget)
        self.gastronomyLabel.setObjectName("gastronomyLabel")
        self.gastronomyLayout.addWidget(self.gastronomyLabel, 0, QtCore.Qt.AlignHCenter)
        self.gastronomyStarsLayout = QtWidgets.QHBoxLayout()
        self.gastronomyStarsLayout.setSpacing(3)
        self.gastronomyStarsLayout.setObjectName("gastronomyStarsLayout")
        
        self.gastronomyStarButtons = []
        for s in range(self.max_stars):
            starButton = QtWidgets.QPushButton("★", self.mainWidget)
            starButton.setMinimumSize(QtCore.QSize(30, 30))
            starButton.setMaximumSize(QtCore.QSize(30, 30))
            starButton.clicked.connect(lambda: self.onStarClicked(self.gastronomyStarButtons))
            self.gastronomyStarButtons.append(starButton)
            self.gastronomyStarsLayout.addWidget(starButton)

        self.gastronomyLayout.addLayout(self.gastronomyStarsLayout)
        self.verticalLayout.addLayout(self.gastronomyLayout)

            # Landscapes
        self.landscapesLayout = QtWidgets.QHBoxLayout()
        self.landscapesLayout.setObjectName("landscapesLayout")
        self.lanscapesLabel = QtWidgets.QLabel(self.mainWidget)
        self.lanscapesLabel.setObjectName("lanscapesLabel")
        self.landscapesLayout.addWidget(self.lanscapesLabel, 0, QtCore.Qt.AlignHCenter)
        self.landscapesStarsLayout = QtWidgets.QHBoxLayout()
        self.landscapesStarsLayout.setSpacing(3)
        self.landscapesStarsLayout.setObjectName("landscapesStarsLayout")
        
        self.landscapesStarButtons = []
        for s in range(self.max_stars):
            starButton = QtWidgets.QPushButton("★", self.mainWidget)
            starButton.setMinimumSize(QtCore.QSize(30, 30))
            starButton.setMaximumSize(QtCore.QSize(30, 30))
            starButton.clicked.connect(lambda: self.onStarClicked(self.landscapesStarButtons))
            self.landscapesStarButtons.append(starButton)
            self.landscapesStarsLayout.addWidget(starButton)

        self.landscapesLayout.addLayout(self.landscapesStarsLayout)
        self.verticalLayout.addLayout(self.landscapesLayout)

            # Avarge score
        self.avarge_scoreLabel = QtWidgets.QLabel(self.mainWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.avarge_scoreLabel.setFont(font)
        self.avarge_scoreLabel.setObjectName("avarge_scoreLabel")
        self.verticalLayout.addWidget(self.avarge_scoreLabel)

        self.loadData()

        self.retranslateUi(destinationPreviewWindow)
        QtCore.QMetaObject.connectSlotsByName(destinationPreviewWindow)

    def retranslateUi(self, destinationPreviewWindow):
        _translate = QtCore.QCoreApplication.translate
        destinationPreviewWindow.setWindowTitle(_translate("destinationPreviewWindow", "Destination Preview"))
        self.nameLabel.setText(_translate("destinationPreviewWindow", "Name:"))
        self.countryLabel.setText(_translate("destinationPreviewWindow", "Country:"))
        self.townLabel.setText(_translate("destinationPreviewWindow", "Town:"))
        self.descLabel.setText(_translate("destinationPreviewWindow", "Description:"))
        self.costsLabel.setText(_translate("destinationPreviewWindow", "Costs: "))
        self.profitabilityLabel.setText(_translate("destinationPreviewWindow", "Profitability:"))
        self.attractionsLabel.setText(_translate("destinationPreviewWindow", "Attracions:"))
        self.transportLabel.setText(_translate("destinationPreviewWindow", "Transport:"))
        self.gastronomyLabel.setText(_translate("destinationPreviewWindow", "Gastronomy:"))
        self.lanscapesLabel.setText(_translate("destinationPreviewWindow", "Landscapes:"))
        self.avarge_scoreLabel.setText(_translate("destinationPreviewWindow", "Avarge score: "))

    def loadData(self):
        self.cur.execute("SELECT name,country,town,description,costs,profitability,attractions,transport,gastronomy,landscapes FROM destinations WHERE name=?", (self.selectedItem,))
        data = self.cur.fetchall()[0]

        self.namePlainTextEdit.setPlainText(data[0])
        self.countryPlainTextEdit.setPlainText(data[1])
        self.townPlainTextEdit.setPlainText(data[2])
        self.descPlainTextEdit.setPlainText(data[3])

        allStarButtons = [self.costsStarButtons, 
                          self.profitabilityStarButtons,
                          self.attractionsStarButtons,
                          self.transportStarButtons,
                          self.gastronomyStarButtons,
                          self.landscapesStarButtons]
        
        allStarsCount = [data[4], data[5], data[6], data[7], data[8], data[9]] 

        for i in range(6):
            self.updateStars(allStarButtons[i], allStarsCount[i])

    def onStarClicked(self, starButtons):
        sender = self.destinationPreviewWindow.sender()
        stars = starButtons.index(sender) + 1
        self.updateStars(starButtons, stars)

    def updateStars(self, starButtons, stars):
        for i, star_button in enumerate(starButtons):
            if i < stars:
                star_button.setStyleSheet("color: yellow;")
            else:
                star_button.setStyleSheet("color: gray;")