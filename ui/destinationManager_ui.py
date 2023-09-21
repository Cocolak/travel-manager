# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'destinationManager.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_destinationManagerWindow(object):
    def setupUi(self, destinationManagerWindow):
        if not destinationManagerWindow.objectName():
            destinationManagerWindow.setObjectName(u"destinationManagerWindow")
        destinationManagerWindow.resize(400, 650)
        self.mainWidget = QWidget(destinationManagerWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setGeometry(QRect(0, 0, 400, 650))
        self.mainWidget.setStyleSheet(u"QWidget{\n"
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
        self.horizontalLayout = QHBoxLayout(self.mainWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.destinationWidget = QWidget(self.mainWidget)
        self.destinationWidget.setObjectName(u"destinationWidget")
        self.verticalLayout_4 = QVBoxLayout(self.destinationWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.destinationLabel = QLabel(self.destinationWidget)
        self.destinationLabel.setObjectName(u"destinationLabel")
        font = QFont()
        font.setPointSize(14)
        self.destinationLabel.setFont(font)

        self.verticalLayout_4.addWidget(self.destinationLabel, 0, Qt.AlignHCenter)

        self.destinationList = QListWidget(self.destinationWidget)
        self.destinationList.setObjectName(u"destinationList")

        self.verticalLayout_4.addWidget(self.destinationList)


        self.horizontalLayout.addWidget(self.destinationWidget)

        self.buttonsWidget = QWidget(self.mainWidget)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        self.buttonsWidget.setMinimumSize(QSize(180, 0))
        self.buttonsWidget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.buttonsWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.searchLayout = QVBoxLayout()
        self.searchLayout.setSpacing(6)
        self.searchLayout.setObjectName(u"searchLayout")
        self.searchLabel = QLabel(self.buttonsWidget)
        self.searchLabel.setObjectName(u"searchLabel")
        font1 = QFont()
        font1.setPointSize(13)
        self.searchLabel.setFont(font1)

        self.searchLayout.addWidget(self.searchLabel, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.searchPlainTextEdit = QPlainTextEdit(self.buttonsWidget)
        self.searchPlainTextEdit.setObjectName(u"searchPlainTextEdit")
        self.searchPlainTextEdit.setMaximumSize(QSize(150, 30))

        self.searchLayout.addWidget(self.searchPlainTextEdit, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.searchLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.manageButtonsLayout = QVBoxLayout()
        self.manageButtonsLayout.setObjectName(u"manageButtonsLayout")
        self.newButton = QPushButton(self.buttonsWidget)
        self.newButton.setObjectName(u"newButton")
        self.newButton.setMinimumSize(QSize(120, 25))

        self.manageButtonsLayout.addWidget(self.newButton, 0, Qt.AlignHCenter)

        self.previewButton = QPushButton(self.buttonsWidget)
        self.previewButton.setObjectName(u"previewButton")
        self.previewButton.setMinimumSize(QSize(120, 25))

        self.manageButtonsLayout.addWidget(self.previewButton, 0, Qt.AlignHCenter)

        self.editButton = QPushButton(self.buttonsWidget)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setMinimumSize(QSize(120, 25))

        self.manageButtonsLayout.addWidget(self.editButton, 0, Qt.AlignHCenter)

        self.deleteButton = QPushButton(self.buttonsWidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMinimumSize(QSize(120, 25))

        self.manageButtonsLayout.addWidget(self.deleteButton, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.manageButtonsLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.addtotravelButton = QPushButton(self.buttonsWidget)
        self.addtotravelButton.setObjectName(u"addtotravelButton")
        self.addtotravelButton.setMinimumSize(QSize(120, 25))

        self.verticalLayout_3.addWidget(self.addtotravelButton, 0, Qt.AlignHCenter)

        self.verticalSpacer_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_1)

        self.exitButton = QPushButton(self.buttonsWidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setMinimumSize(QSize(120, 25))

        self.verticalLayout_3.addWidget(self.exitButton, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.buttonsWidget)


        self.retranslateUi(destinationManagerWindow)

        QMetaObject.connectSlotsByName(destinationManagerWindow)
    # setupUi

    def retranslateUi(self, destinationManagerWindow):
        destinationManagerWindow.setWindowTitle(QCoreApplication.translate("destinationManagerWindow", u"Destination Manager", None))
        self.destinationLabel.setText(QCoreApplication.translate("destinationManagerWindow", u"Destination List", None))
        self.searchLabel.setText(QCoreApplication.translate("destinationManagerWindow", u"Search:", None))
        self.newButton.setText(QCoreApplication.translate("destinationManagerWindow", u"New", None))
        self.previewButton.setText(QCoreApplication.translate("destinationManagerWindow", u"Preview", None))
        self.editButton.setText(QCoreApplication.translate("destinationManagerWindow", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("destinationManagerWindow", u"Delete", None))
        self.addtotravelButton.setText(QCoreApplication.translate("destinationManagerWindow", u"Add to Travel", None))
        self.exitButton.setText(QCoreApplication.translate("destinationManagerWindow", u"Exit", None))
    # retranslateUi

