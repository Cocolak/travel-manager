import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_destinationPreviewWindow(object):
    def setupUi(self, destinationPreviewWindow, selectedItem):
        self.destinationPreviewWindow = destinationPreviewWindow
        destinationPreviewWindow.setObjectName("destinationPreviewWindow")
        destinationPreviewWindow.resize(350, 480)
        self.mainWidget = QtWidgets.QWidget(destinationPreviewWindow)
        self.mainWidget.setGeometry(QtCore.QRect(0, 0, 350, 480))
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
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

        # Costs stars
        self.costsLayout = QtWidgets.QHBoxLayout()
        self.costsLayout.setObjectName("costsLayout")
        self.costsLabel = QtWidgets.QLabel(self.mainWidget)
        self.costsLabel.setObjectName("costsLabel")
        self.costsLayout.addWidget(self.costsLabel, 0, QtCore.Qt.AlignHCenter)
        self.costsStarsLayout = QtWidgets.QHBoxLayout()
        self.costsStarsLayout.setSpacing(0)
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

        # Profitability stars
        self.profitabilityLayout = QtWidgets.QHBoxLayout()
        self.profitabilityLayout.setObjectName("profitabilityLayout")
        self.profitabilityLabel = QtWidgets.QLabel(self.mainWidget)
        self.profitabilityLabel.setObjectName("profitabilityLabel")
        self.profitabilityLayout.addWidget(self.profitabilityLabel, 0, QtCore.Qt.AlignHCenter)
        self.profitabilityStarsLayout = QtWidgets.QHBoxLayout()
        self.profitabilityStarsLayout.setSpacing(0)
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

        # Attractions stars
        self.attractionsLayout = QtWidgets.QHBoxLayout()
        self.attractionsLayout.setObjectName("attractionsLayout")
        self.attractionsLabel = QtWidgets.QLabel(self.mainWidget)
        self.attractionsLabel.setObjectName("attractionsLabel")
        self.attractionsLayout.addWidget(self.attractionsLabel, 0, QtCore.Qt.AlignHCenter)
        self.attractionsStarsLayout = QtWidgets.QHBoxLayout()
        self.attractionsStarsLayout.setSpacing(0)
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

        # Transport stars
        self.transportLayout = QtWidgets.QHBoxLayout()
        self.transportLayout.setObjectName("transportLayout")
        self.transportLabel = QtWidgets.QLabel(self.mainWidget)
        self.transportLabel.setObjectName("transportLabel")
        self.transportLayout.addWidget(self.transportLabel, 0, QtCore.Qt.AlignHCenter)
        self.transportStarsLayout = QtWidgets.QHBoxLayout()
        self.transportStarsLayout.setSpacing(0)
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

        # Gastronomy stars
        self.gastronomyLayout = QtWidgets.QHBoxLayout()
        self.gastronomyLayout.setObjectName("gastronomyLayout")
        self.gastronomyLabel = QtWidgets.QLabel(self.mainWidget)
        self.gastronomyLabel.setObjectName("gastronomyLabel")
        self.gastronomyLayout.addWidget(self.gastronomyLabel, 0, QtCore.Qt.AlignHCenter)
        self.gastronomyStarsLayout = QtWidgets.QHBoxLayout()
        self.gastronomyStarsLayout.setSpacing(0)
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

        # Landscapes stars
        self.landscapesLayout = QtWidgets.QHBoxLayout()
        self.landscapesLayout.setObjectName("landscapesLayout")
        self.lanscapesLabel = QtWidgets.QLabel(self.mainWidget)
        self.lanscapesLabel.setObjectName("lanscapesLabel")
        self.landscapesLayout.addWidget(self.lanscapesLabel, 0, QtCore.Qt.AlignHCenter)
        self.landscapesStarsLayout = QtWidgets.QHBoxLayout()
        self.landscapesStarsLayout.setSpacing(0)
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

        # Avarger score
        self.avarge_scoreLabel = QtWidgets.QLabel(self.mainWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.avarge_scoreLabel.setFont(font)
        self.avarge_scoreLabel.setObjectName("avarge_scoreLabel")
        self.verticalLayout.addWidget(self.avarge_scoreLabel)

        #Edited
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()
        self.selectedItem = selectedItem
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
        self.cur.execute("SELECT * FROM destinations WHERE name=?", (self.selectedItem,))
        data = self.cur.fetchall()[0]

        self.namePlainTextEdit.setPlainText(data[1])
        self.countryPlainTextEdit.setPlainText(data[2])
        self.townPlainTextEdit.setPlainText(data[3])
        self.descPlainTextEdit.setPlainText(data[4])

        costsStars = data[5]
        attractionsStars = data[6]
        transportStars = data[7]
        gastronomyStars = data[8]
        landscapesStars = data[9]
        score_avarge = data[10]

    def onStarClicked(self, starButtons):
        sender = self.destinationPreviewWindow.sender()
        print(sender.text())
        stars = starButtons.index(sender) + 1
        self.updateStars(starButtons, stars)

    def updateStars(self, starButtons, stars):
        for i, star_button in enumerate(starButtons):
            if i < stars:
                star_button.setStyleSheet("color: yellow;")
            else:
                star_button.setStyleSheet("color: gray;")