# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'destinationPreview.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_destinationPreviewWindow(object):
    def setupUi(self, destinationPreviewWindow):
        if not destinationPreviewWindow.objectName():
            destinationPreviewWindow.setObjectName(u"destinationPreviewWindow")
        destinationPreviewWindow.resize(350, 480)
        self.mainWidget = QWidget(destinationPreviewWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setGeometry(QRect(0, 0, 350, 480))
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
"QPlainTextEdit {\n"
"border: 1px solid rgb(128,128,128);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.nameLayout = QHBoxLayout()
        self.nameLayout.setObjectName(u"nameLayout")
        self.nameLabel = QLabel(self.mainWidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.nameLayout.addWidget(self.nameLabel)

        self.namePlainTextEdit = QPlainTextEdit(self.mainWidget)
        self.namePlainTextEdit.setObjectName(u"namePlainTextEdit")
        self.namePlainTextEdit.setMaximumSize(QSize(16777215, 30))

        self.nameLayout.addWidget(self.namePlainTextEdit)


        self.verticalLayout.addLayout(self.nameLayout)

        self.countryLayout = QHBoxLayout()
        self.countryLayout.setObjectName(u"countryLayout")
        self.countryLabel = QLabel(self.mainWidget)
        self.countryLabel.setObjectName(u"countryLabel")

        self.countryLayout.addWidget(self.countryLabel)

        self.countryPlainTextEdit = QPlainTextEdit(self.mainWidget)
        self.countryPlainTextEdit.setObjectName(u"countryPlainTextEdit")
        self.countryPlainTextEdit.setMaximumSize(QSize(16777215, 30))

        self.countryLayout.addWidget(self.countryPlainTextEdit)


        self.verticalLayout.addLayout(self.countryLayout)

        self.townLayout = QHBoxLayout()
        self.townLayout.setObjectName(u"townLayout")
        self.townLabel = QLabel(self.mainWidget)
        self.townLabel.setObjectName(u"townLabel")

        self.townLayout.addWidget(self.townLabel)

        self.townPlainTextEdit = QPlainTextEdit(self.mainWidget)
        self.townPlainTextEdit.setObjectName(u"townPlainTextEdit")
        self.townPlainTextEdit.setMaximumSize(QSize(16777215, 30))

        self.townLayout.addWidget(self.townPlainTextEdit)


        self.verticalLayout.addLayout(self.townLayout)

        self.descLayout = QHBoxLayout()
        self.descLayout.setObjectName(u"descLayout")
        self.descLabel = QLabel(self.mainWidget)
        self.descLabel.setObjectName(u"descLabel")

        self.descLayout.addWidget(self.descLabel)

        self.descPlainTextEdit = QPlainTextEdit(self.mainWidget)
        self.descPlainTextEdit.setObjectName(u"descPlainTextEdit")
        self.descPlainTextEdit.setMaximumSize(QSize(16777215, 80))

        self.descLayout.addWidget(self.descPlainTextEdit)


        self.verticalLayout.addLayout(self.descLayout)

        self.costsLayout = QHBoxLayout()
        self.costsLayout.setObjectName(u"costsLayout")
        self.costsLabel = QLabel(self.mainWidget)
        self.costsLabel.setObjectName(u"costsLabel")

        self.costsLayout.addWidget(self.costsLabel, 0, Qt.AlignHCenter)

        self.costsStarsLayout = QHBoxLayout()
        self.costsStarsLayout.setSpacing(3)
        self.costsStarsLayout.setObjectName(u"costsStarsLayout")
        self.costsStar_1 = QPushButton(self.mainWidget)
        self.costsStar_1.setObjectName(u"costsStar_1")
        self.costsStar_1.setMinimumSize(QSize(30, 30))
        self.costsStar_1.setMaximumSize(QSize(30, 30))

        self.costsStarsLayout.addWidget(self.costsStar_1)

        self.costsStar_2 = QPushButton(self.mainWidget)
        self.costsStar_2.setObjectName(u"costsStar_2")
        self.costsStar_2.setMinimumSize(QSize(30, 30))
        self.costsStar_2.setMaximumSize(QSize(30, 30))

        self.costsStarsLayout.addWidget(self.costsStar_2)

        self.costsStar_3 = QPushButton(self.mainWidget)
        self.costsStar_3.setObjectName(u"costsStar_3")
        self.costsStar_3.setMinimumSize(QSize(30, 30))
        self.costsStar_3.setMaximumSize(QSize(30, 30))

        self.costsStarsLayout.addWidget(self.costsStar_3)

        self.costsStar_4 = QPushButton(self.mainWidget)
        self.costsStar_4.setObjectName(u"costsStar_4")
        self.costsStar_4.setMinimumSize(QSize(30, 30))
        self.costsStar_4.setMaximumSize(QSize(30, 30))

        self.costsStarsLayout.addWidget(self.costsStar_4)

        self.costsStar_5 = QPushButton(self.mainWidget)
        self.costsStar_5.setObjectName(u"costsStar_5")
        self.costsStar_5.setMinimumSize(QSize(30, 30))
        self.costsStar_5.setMaximumSize(QSize(30, 30))

        self.costsStarsLayout.addWidget(self.costsStar_5)


        self.costsLayout.addLayout(self.costsStarsLayout)


        self.verticalLayout.addLayout(self.costsLayout)

        self.profitabilityLayout = QHBoxLayout()
        self.profitabilityLayout.setObjectName(u"profitabilityLayout")
        self.profitabilityLabel = QLabel(self.mainWidget)
        self.profitabilityLabel.setObjectName(u"profitabilityLabel")

        self.profitabilityLayout.addWidget(self.profitabilityLabel, 0, Qt.AlignHCenter)

        self.profitabilityStarsLayout = QHBoxLayout()
        self.profitabilityStarsLayout.setSpacing(3)
        self.profitabilityStarsLayout.setObjectName(u"profitabilityStarsLayout")
        self.profitabilityStar_1 = QPushButton(self.mainWidget)
        self.profitabilityStar_1.setObjectName(u"profitabilityStar_1")
        self.profitabilityStar_1.setMinimumSize(QSize(30, 30))
        self.profitabilityStar_1.setMaximumSize(QSize(30, 30))

        self.profitabilityStarsLayout.addWidget(self.profitabilityStar_1)

        self.profitabilityStar_2 = QPushButton(self.mainWidget)
        self.profitabilityStar_2.setObjectName(u"profitabilityStar_2")
        self.profitabilityStar_2.setMinimumSize(QSize(30, 30))
        self.profitabilityStar_2.setMaximumSize(QSize(30, 30))

        self.profitabilityStarsLayout.addWidget(self.profitabilityStar_2)

        self.profitabilityStar_3 = QPushButton(self.mainWidget)
        self.profitabilityStar_3.setObjectName(u"profitabilityStar_3")
        self.profitabilityStar_3.setMinimumSize(QSize(30, 30))
        self.profitabilityStar_3.setMaximumSize(QSize(30, 30))

        self.profitabilityStarsLayout.addWidget(self.profitabilityStar_3)

        self.profitabilityStar_4 = QPushButton(self.mainWidget)
        self.profitabilityStar_4.setObjectName(u"profitabilityStar_4")
        self.profitabilityStar_4.setMinimumSize(QSize(30, 30))
        self.profitabilityStar_4.setMaximumSize(QSize(30, 30))

        self.profitabilityStarsLayout.addWidget(self.profitabilityStar_4)

        self.profitabilityStar_5 = QPushButton(self.mainWidget)
        self.profitabilityStar_5.setObjectName(u"profitabilityStar_5")
        self.profitabilityStar_5.setMinimumSize(QSize(30, 30))
        self.profitabilityStar_5.setMaximumSize(QSize(30, 30))

        self.profitabilityStarsLayout.addWidget(self.profitabilityStar_5)


        self.profitabilityLayout.addLayout(self.profitabilityStarsLayout)


        self.verticalLayout.addLayout(self.profitabilityLayout)

        self.attractionsLayout = QHBoxLayout()
        self.attractionsLayout.setObjectName(u"attractionsLayout")
        self.attractionsLabel = QLabel(self.mainWidget)
        self.attractionsLabel.setObjectName(u"attractionsLabel")

        self.attractionsLayout.addWidget(self.attractionsLabel, 0, Qt.AlignHCenter)

        self.attractionsStarsLayout = QHBoxLayout()
        self.attractionsStarsLayout.setSpacing(3)
        self.attractionsStarsLayout.setObjectName(u"attractionsStarsLayout")
        self.attractionsStar_1 = QPushButton(self.mainWidget)
        self.attractionsStar_1.setObjectName(u"attractionsStar_1")
        self.attractionsStar_1.setMinimumSize(QSize(30, 30))
        self.attractionsStar_1.setMaximumSize(QSize(30, 30))

        self.attractionsStarsLayout.addWidget(self.attractionsStar_1)

        self.attractionsStar_2 = QPushButton(self.mainWidget)
        self.attractionsStar_2.setObjectName(u"attractionsStar_2")
        self.attractionsStar_2.setMinimumSize(QSize(30, 30))
        self.attractionsStar_2.setMaximumSize(QSize(30, 30))

        self.attractionsStarsLayout.addWidget(self.attractionsStar_2)

        self.attractionsStar_3 = QPushButton(self.mainWidget)
        self.attractionsStar_3.setObjectName(u"attractionsStar_3")
        self.attractionsStar_3.setMinimumSize(QSize(30, 30))
        self.attractionsStar_3.setMaximumSize(QSize(30, 30))

        self.attractionsStarsLayout.addWidget(self.attractionsStar_3)

        self.attractionsStar_4 = QPushButton(self.mainWidget)
        self.attractionsStar_4.setObjectName(u"attractionsStar_4")
        self.attractionsStar_4.setMinimumSize(QSize(30, 30))
        self.attractionsStar_4.setMaximumSize(QSize(30, 30))

        self.attractionsStarsLayout.addWidget(self.attractionsStar_4)

        self.attractionsStar_5 = QPushButton(self.mainWidget)
        self.attractionsStar_5.setObjectName(u"attractionsStar_5")
        self.attractionsStar_5.setMinimumSize(QSize(30, 30))
        self.attractionsStar_5.setMaximumSize(QSize(30, 30))

        self.attractionsStarsLayout.addWidget(self.attractionsStar_5)


        self.attractionsLayout.addLayout(self.attractionsStarsLayout)


        self.verticalLayout.addLayout(self.attractionsLayout)

        self.transportLayout = QHBoxLayout()
        self.transportLayout.setObjectName(u"transportLayout")
        self.transportLabel = QLabel(self.mainWidget)
        self.transportLabel.setObjectName(u"transportLabel")

        self.transportLayout.addWidget(self.transportLabel, 0, Qt.AlignHCenter)

        self.transportStarsLayout = QHBoxLayout()
        self.transportStarsLayout.setSpacing(3)
        self.transportStarsLayout.setObjectName(u"transportStarsLayout")
        self.transportStar_1 = QPushButton(self.mainWidget)
        self.transportStar_1.setObjectName(u"transportStar_1")
        self.transportStar_1.setMinimumSize(QSize(30, 30))
        self.transportStar_1.setMaximumSize(QSize(30, 30))

        self.transportStarsLayout.addWidget(self.transportStar_1)

        self.transportStar_2 = QPushButton(self.mainWidget)
        self.transportStar_2.setObjectName(u"transportStar_2")
        self.transportStar_2.setMinimumSize(QSize(30, 30))
        self.transportStar_2.setMaximumSize(QSize(30, 30))

        self.transportStarsLayout.addWidget(self.transportStar_2)

        self.transportStar_3 = QPushButton(self.mainWidget)
        self.transportStar_3.setObjectName(u"transportStar_3")
        self.transportStar_3.setMinimumSize(QSize(30, 30))
        self.transportStar_3.setMaximumSize(QSize(30, 30))

        self.transportStarsLayout.addWidget(self.transportStar_3)

        self.transportStar_4 = QPushButton(self.mainWidget)
        self.transportStar_4.setObjectName(u"transportStar_4")
        self.transportStar_4.setMinimumSize(QSize(30, 30))
        self.transportStar_4.setMaximumSize(QSize(30, 30))

        self.transportStarsLayout.addWidget(self.transportStar_4)

        self.transportStar_5 = QPushButton(self.mainWidget)
        self.transportStar_5.setObjectName(u"transportStar_5")
        self.transportStar_5.setMinimumSize(QSize(30, 30))
        self.transportStar_5.setMaximumSize(QSize(30, 30))

        self.transportStarsLayout.addWidget(self.transportStar_5)


        self.transportLayout.addLayout(self.transportStarsLayout)


        self.verticalLayout.addLayout(self.transportLayout)

        self.gastronomyLayout = QHBoxLayout()
        self.gastronomyLayout.setObjectName(u"gastronomyLayout")
        self.gastronomyLabel = QLabel(self.mainWidget)
        self.gastronomyLabel.setObjectName(u"gastronomyLabel")

        self.gastronomyLayout.addWidget(self.gastronomyLabel, 0, Qt.AlignHCenter)

        self.gastronomyStarsLayout = QHBoxLayout()
        self.gastronomyStarsLayout.setSpacing(3)
        self.gastronomyStarsLayout.setObjectName(u"gastronomyStarsLayout")
        self.gastronomyStar_1 = QPushButton(self.mainWidget)
        self.gastronomyStar_1.setObjectName(u"gastronomyStar_1")
        self.gastronomyStar_1.setMinimumSize(QSize(30, 30))
        self.gastronomyStar_1.setMaximumSize(QSize(30, 30))

        self.gastronomyStarsLayout.addWidget(self.gastronomyStar_1)

        self.gastronomyStar_2 = QPushButton(self.mainWidget)
        self.gastronomyStar_2.setObjectName(u"gastronomyStar_2")
        self.gastronomyStar_2.setMinimumSize(QSize(30, 30))
        self.gastronomyStar_2.setMaximumSize(QSize(30, 30))

        self.gastronomyStarsLayout.addWidget(self.gastronomyStar_2)

        self.gastronomyStar_3 = QPushButton(self.mainWidget)
        self.gastronomyStar_3.setObjectName(u"gastronomyStar_3")
        self.gastronomyStar_3.setMinimumSize(QSize(30, 30))
        self.gastronomyStar_3.setMaximumSize(QSize(30, 30))

        self.gastronomyStarsLayout.addWidget(self.gastronomyStar_3)

        self.gastronomyStar_4 = QPushButton(self.mainWidget)
        self.gastronomyStar_4.setObjectName(u"gastronomyStar_4")
        self.gastronomyStar_4.setMinimumSize(QSize(30, 30))
        self.gastronomyStar_4.setMaximumSize(QSize(30, 30))

        self.gastronomyStarsLayout.addWidget(self.gastronomyStar_4)

        self.gastronomyStar_5 = QPushButton(self.mainWidget)
        self.gastronomyStar_5.setObjectName(u"gastronomyStar_5")
        self.gastronomyStar_5.setMinimumSize(QSize(30, 30))
        self.gastronomyStar_5.setMaximumSize(QSize(30, 30))

        self.gastronomyStarsLayout.addWidget(self.gastronomyStar_5)


        self.gastronomyLayout.addLayout(self.gastronomyStarsLayout)


        self.verticalLayout.addLayout(self.gastronomyLayout)

        self.landscapesLayout = QHBoxLayout()
        self.landscapesLayout.setObjectName(u"landscapesLayout")
        self.lanscapesLabel = QLabel(self.mainWidget)
        self.lanscapesLabel.setObjectName(u"lanscapesLabel")

        self.landscapesLayout.addWidget(self.lanscapesLabel, 0, Qt.AlignHCenter)

        self.landscapesStarsLayout = QHBoxLayout()
        self.landscapesStarsLayout.setSpacing(3)
        self.landscapesStarsLayout.setObjectName(u"landscapesStarsLayout")
        self.lanscapesStar_1 = QPushButton(self.mainWidget)
        self.lanscapesStar_1.setObjectName(u"lanscapesStar_1")
        self.lanscapesStar_1.setMinimumSize(QSize(30, 30))
        self.lanscapesStar_1.setMaximumSize(QSize(30, 30))

        self.landscapesStarsLayout.addWidget(self.lanscapesStar_1)

        self.lanscapesStar_2 = QPushButton(self.mainWidget)
        self.lanscapesStar_2.setObjectName(u"lanscapesStar_2")
        self.lanscapesStar_2.setMinimumSize(QSize(30, 30))
        self.lanscapesStar_2.setMaximumSize(QSize(30, 30))

        self.landscapesStarsLayout.addWidget(self.lanscapesStar_2)

        self.lanscapesStar_3 = QPushButton(self.mainWidget)
        self.lanscapesStar_3.setObjectName(u"lanscapesStar_3")
        self.lanscapesStar_3.setMinimumSize(QSize(30, 30))
        self.lanscapesStar_3.setMaximumSize(QSize(30, 30))

        self.landscapesStarsLayout.addWidget(self.lanscapesStar_3)

        self.lanscapesStar_4 = QPushButton(self.mainWidget)
        self.lanscapesStar_4.setObjectName(u"lanscapesStar_4")
        self.lanscapesStar_4.setMinimumSize(QSize(30, 30))
        self.lanscapesStar_4.setMaximumSize(QSize(30, 30))

        self.landscapesStarsLayout.addWidget(self.lanscapesStar_4)

        self.lanscapesStar_5 = QPushButton(self.mainWidget)
        self.lanscapesStar_5.setObjectName(u"lanscapesStar_5")
        self.lanscapesStar_5.setMinimumSize(QSize(30, 30))
        self.lanscapesStar_5.setMaximumSize(QSize(30, 30))

        self.landscapesStarsLayout.addWidget(self.lanscapesStar_5)


        self.landscapesLayout.addLayout(self.landscapesStarsLayout)


        self.verticalLayout.addLayout(self.landscapesLayout)

        self.avarge_scoreLabel = QLabel(self.mainWidget)
        self.avarge_scoreLabel.setObjectName(u"avarge_scoreLabel")
        font = QFont()
        font.setPointSize(13)
        self.avarge_scoreLabel.setFont(font)

        self.verticalLayout.addWidget(self.avarge_scoreLabel)


        self.retranslateUi(destinationPreviewWindow)

        QMetaObject.connectSlotsByName(destinationPreviewWindow)
    # setupUi

    def retranslateUi(self, destinationPreviewWindow):
        destinationPreviewWindow.setWindowTitle(QCoreApplication.translate("destinationPreviewWindow", u"Destination Preview", None))
        self.nameLabel.setText(QCoreApplication.translate("destinationPreviewWindow", u"Name:", None))
        self.countryLabel.setText(QCoreApplication.translate("destinationPreviewWindow", u"Country:", None))
        self.townLabel.setText(QCoreApplication.translate("destinationPreviewWindow", u"Town:", None))
        self.descLabel.setText(QCoreApplication.translate("destinationPreviewWindow", u"Description:", None))
        self.costsLabel.setText(QCoreApplication.translate("destinationPreviewWindow", u"Costs: ", None))
        self.costsStar_1.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.costsStar_2.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.costsStar_3.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.costsStar_4.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.costsStar_5.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.profitabilityLabel.setText(QCoreApplication.translate("destinationPreviewWindow", u"Profitability:", None))
        self.profitabilityStar_1.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.profitabilityStar_2.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.profitabilityStar_3.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.profitabilityStar_4.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.profitabilityStar_5.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.attractionsLabel.setText(QCoreApplication.translate("destinationPreviewWindow", u"Attracions:", None))
        self.attractionsStar_1.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.attractionsStar_2.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.attractionsStar_3.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.attractionsStar_4.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.attractionsStar_5.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.transportLabel.setText(QCoreApplication.translate("destinationPreviewWindow", u"Transport:", None))
        self.transportStar_1.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.transportStar_2.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.transportStar_3.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.transportStar_4.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.transportStar_5.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.gastronomyLabel.setText(QCoreApplication.translate("destinationPreviewWindow", u"Gastronomy:", None))
        self.gastronomyStar_1.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.gastronomyStar_2.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.gastronomyStar_3.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.gastronomyStar_4.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.gastronomyStar_5.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.lanscapesLabel.setText(QCoreApplication.translate("destinationPreviewWindow", u"Landscapes:", None))
        self.lanscapesStar_1.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.lanscapesStar_2.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.lanscapesStar_3.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.lanscapesStar_4.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.lanscapesStar_5.setText(QCoreApplication.translate("destinationPreviewWindow", u"\u2605", None))
        self.avarge_scoreLabel.setText(QCoreApplication.translate("destinationPreviewWindow", u"Avarge score: ", None))
    # retranslateUi

