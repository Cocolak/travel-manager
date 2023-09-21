# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectTravel.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import res_rc

class Ui_selectTravelWindow(object):
    def setupUi(self, selectTravelWindow):
        if not selectTravelWindow.objectName():
            selectTravelWindow.setObjectName(u"selectTravelWindow")
        selectTravelWindow.resize(400, 550)
        self.mainWidget = QWidget(selectTravelWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setGeometry(QRect(0, 0, 400, 550))
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
"QPushButton#githubButton {\n"
"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"margin:0px 10px 10px 0px;\n"
"}\n"
"QListWidget{\n"
"border:1px solid rgb(72, 168, 96);;\n"
"}\n"
"QListWidget::item{\n"
"background-color:rgb(72, 168, 96);\n"
"color:black;\n"
"border:1px solid black;\n"
"height:20px;\n"
"}\n"
"QListWidget::item:hover{\n"
"background-color:rgb(52, 138, 76);\n"
"}\n"
"QListWidget::item:selected{\n"
"background-color:rgb(32, 118, 56);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.mainWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.mainWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(30)
        self.titleLabel.setFont(font)

        self.verticalLayout_3.addWidget(self.titleLabel, 0, Qt.AlignHCenter)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 10, -1, -1)
        self.selectLabel = QLabel(self.mainWidget)
        self.selectLabel.setObjectName(u"selectLabel")
        font1 = QFont()
        font1.setPointSize(13)
        self.selectLabel.setFont(font1)

        self.verticalLayout.addWidget(self.selectLabel, 0, Qt.AlignHCenter)

        self.travelList = QListWidget(self.mainWidget)
        __qlistwidgetitem = QListWidgetItem(self.travelList)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        self.travelList.setObjectName(u"travelList")
        self.travelList.setStyleSheet(u"")
        self.travelList.setMovement(QListView.Free)

        self.verticalLayout.addWidget(self.travelList, 0, Qt.AlignHCenter)

        self.orLabel = QLabel(self.mainWidget)
        self.orLabel.setObjectName(u"orLabel")

        self.verticalLayout.addWidget(self.orLabel, 0, Qt.AlignHCenter)

        self.createButton = QPushButton(self.mainWidget)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setMinimumSize(QSize(130, 25))
        self.createButton.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.createButton, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.githubButton = QPushButton(self.mainWidget)
        self.githubButton.setObjectName(u"githubButton")
        self.githubButton.setMinimumSize(QSize(60, 50))
        icon = QIcon()
        icon.addFile(u":/Images/github-mark-white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.githubButton.setIcon(icon)
        self.githubButton.setIconSize(QSize(46, 46))

        self.verticalLayout_3.addWidget(self.githubButton, 0, Qt.AlignRight)


        self.retranslateUi(selectTravelWindow)

        QMetaObject.connectSlotsByName(selectTravelWindow)
    # setupUi

    def retranslateUi(self, selectTravelWindow):
        selectTravelWindow.setWindowTitle(QCoreApplication.translate("selectTravelWindow", u"Selecting Travel", None))
        self.titleLabel.setText(QCoreApplication.translate("selectTravelWindow", u"Travel Manager", None))
        self.selectLabel.setText(QCoreApplication.translate("selectTravelWindow", u"Select Travel from list:", None))

        __sortingEnabled = self.travelList.isSortingEnabled()
        self.travelList.setSortingEnabled(False)
        ___qlistwidgetitem = self.travelList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("selectTravelWindow", u"Aligment test", None));
        self.travelList.setSortingEnabled(__sortingEnabled)

        self.orLabel.setText(QCoreApplication.translate("selectTravelWindow", u"or", None))
        self.createButton.setText(QCoreApplication.translate("selectTravelWindow", u"Create New Travel", None))
        self.githubButton.setText("")
    # retranslateUi

