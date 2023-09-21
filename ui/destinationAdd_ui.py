# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'destinationAdd.ui'
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

class Ui_destinationAddWindow(object):
    def setupUi(self, destinationAddWindow):
        if not destinationAddWindow.objectName():
            destinationAddWindow.setObjectName(u"destinationAddWindow")
        destinationAddWindow.resize(350, 250)
        self.mainWidget = QWidget(destinationAddWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setGeometry(QRect(0, 0, 350, 250))
        self.verticalLayout_3 = QVBoxLayout(self.mainWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 6)
        self.contentWidget = QWidget(self.mainWidget)
        self.contentWidget.setObjectName(u"contentWidget")
        self.verticalLayout = QVBoxLayout(self.contentWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nameLayout = QHBoxLayout()
        self.nameLayout.setObjectName(u"nameLayout")
        self.nameLabel = QLabel(self.contentWidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.nameLayout.addWidget(self.nameLabel)

        self.namePlainTextEdit = QPlainTextEdit(self.contentWidget)
        self.namePlainTextEdit.setObjectName(u"namePlainTextEdit")
        self.namePlainTextEdit.setMaximumSize(QSize(16777215, 30))

        self.nameLayout.addWidget(self.namePlainTextEdit)


        self.verticalLayout.addLayout(self.nameLayout)

        self.countryLayout = QHBoxLayout()
        self.countryLayout.setObjectName(u"countryLayout")
        self.countryLabel = QLabel(self.contentWidget)
        self.countryLabel.setObjectName(u"countryLabel")

        self.countryLayout.addWidget(self.countryLabel)

        self.countryPlainTextEdit = QPlainTextEdit(self.contentWidget)
        self.countryPlainTextEdit.setObjectName(u"countryPlainTextEdit")
        self.countryPlainTextEdit.setMaximumSize(QSize(16777215, 30))

        self.countryLayout.addWidget(self.countryPlainTextEdit)


        self.verticalLayout.addLayout(self.countryLayout)

        self.townLayout = QHBoxLayout()
        self.townLayout.setObjectName(u"townLayout")
        self.townlabel = QLabel(self.contentWidget)
        self.townlabel.setObjectName(u"townlabel")

        self.townLayout.addWidget(self.townlabel)

        self.townPlainTextEdit = QPlainTextEdit(self.contentWidget)
        self.townPlainTextEdit.setObjectName(u"townPlainTextEdit")
        self.townPlainTextEdit.setMaximumSize(QSize(16777215, 30))

        self.townLayout.addWidget(self.townPlainTextEdit)


        self.verticalLayout.addLayout(self.townLayout)

        self.descLayout = QHBoxLayout()
        self.descLayout.setObjectName(u"descLayout")
        self.descLabel = QLabel(self.contentWidget)
        self.descLabel.setObjectName(u"descLabel")

        self.descLayout.addWidget(self.descLabel)

        self.descPlainTextEdit = QPlainTextEdit(self.contentWidget)
        self.descPlainTextEdit.setObjectName(u"descPlainTextEdit")
        self.descPlainTextEdit.setMaximumSize(QSize(16777215, 80))

        self.descLayout.addWidget(self.descPlainTextEdit)


        self.verticalLayout.addLayout(self.descLayout)


        self.verticalLayout_3.addWidget(self.contentWidget)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.addButton = QPushButton(self.mainWidget)
        self.addButton.setObjectName(u"addButton")

        self.buttonsLayout.addWidget(self.addButton, 0, Qt.AlignHCenter)

        self.cancelButton = QPushButton(self.mainWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonsLayout.addWidget(self.cancelButton, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.buttonsLayout)


        self.retranslateUi(destinationAddWindow)

        QMetaObject.connectSlotsByName(destinationAddWindow)
    # setupUi

    def retranslateUi(self, destinationAddWindow):
        destinationAddWindow.setWindowTitle(QCoreApplication.translate("destinationAddWindow", u"Adding Destination", None))
        self.nameLabel.setText(QCoreApplication.translate("destinationAddWindow", u"Name:", None))
        self.countryLabel.setText(QCoreApplication.translate("destinationAddWindow", u"Country:", None))
        self.townlabel.setText(QCoreApplication.translate("destinationAddWindow", u"Town:", None))
        self.descLabel.setText(QCoreApplication.translate("destinationAddWindow", u"Description:", None))
        self.addButton.setText(QCoreApplication.translate("destinationAddWindow", u"Add", None))
        self.cancelButton.setText(QCoreApplication.translate("destinationAddWindow", u"Cancel", None))
    # retranslateUi

