# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createTravel.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_createTravelWindow(object):
    def setupUi(self, createTravelWindow):
        if not createTravelWindow.objectName():
            createTravelWindow.setObjectName(u"createTravelWindow")
        createTravelWindow.resize(500, 500)
        self.mainWidget = QWidget(createTravelWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setGeometry(QRect(0, 0, 500, 500))
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
"}\n"
"QDateEdit {\n"
"border: 1px solid rgb(128,128,128);\n"
"}\n"
"QSpinBox {\n"
"border: 1px solid rgb(128,128,128);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.mainWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_1 = QWidget(self.mainWidget)
        self.widget_1.setObjectName(u"widget_1")
        self.verticalLayout = QVBoxLayout(self.widget_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.destinationLabel = QLabel(self.widget_1)
        self.destinationLabel.setObjectName(u"destinationLabel")
        font = QFont()
        font.setPointSize(14)
        self.destinationLabel.setFont(font)

        self.verticalLayout.addWidget(self.destinationLabel, 0, Qt.AlignHCenter)

        self.destinationList = QListWidget(self.widget_1)
        self.destinationList.setObjectName(u"destinationList")
        font1 = QFont()
        font1.setPointSize(12)
        self.destinationList.setFont(font1)

        self.verticalLayout.addWidget(self.destinationList)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addButton = QPushButton(self.widget_1)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_2.addWidget(self.addButton)

        self.previewButton = QPushButton(self.widget_1)
        self.previewButton.setObjectName(u"previewButton")
        self.previewButton.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_2.addWidget(self.previewButton)

        self.removeButton = QPushButton(self.widget_1)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_2.addWidget(self.removeButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.widget_1)

        self.widget_2 = QWidget(self.mainWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.nameLabel = QLabel(self.widget_2)
        self.nameLabel.setObjectName(u"nameLabel")
        font2 = QFont()
        font2.setPointSize(10)
        self.nameLabel.setFont(font2)

        self.verticalLayout_5.addWidget(self.nameLabel, 0, Qt.AlignHCenter)

        self.namePlainTextEdit = QPlainTextEdit(self.widget_2)
        self.namePlainTextEdit.setObjectName(u"namePlainTextEdit")
        self.namePlainTextEdit.setMinimumSize(QSize(0, 30))
        self.namePlainTextEdit.setMaximumSize(QSize(200, 30))

        self.verticalLayout_5.addWidget(self.namePlainTextEdit, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.fromLabel = QLabel(self.widget_2)
        self.fromLabel.setObjectName(u"fromLabel")
        font3 = QFont()
        font3.setPointSize(9)
        self.fromLabel.setFont(font3)

        self.verticalLayout_3.addWidget(self.fromLabel, 0, Qt.AlignHCenter)

        self.fromDateEdit = QDateEdit(self.widget_2)
        self.fromDateEdit.setObjectName(u"fromDateEdit")
        self.fromDateEdit.setMinimumSize(QSize(130, 25))
        self.fromDateEdit.setAlignment(Qt.AlignCenter)
        self.fromDateEdit.setCalendarPopup(True)
        self.fromDateEdit.setDate(QDate(2000, 12, 27))

        self.verticalLayout_3.addWidget(self.fromDateEdit, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.toLabel = QLabel(self.widget_2)
        self.toLabel.setObjectName(u"toLabel")
        self.toLabel.setFont(font3)

        self.verticalLayout_4.addWidget(self.toLabel, 0, Qt.AlignHCenter)

        self.toDateEdit = QDateEdit(self.widget_2)
        self.toDateEdit.setObjectName(u"toDateEdit")
        self.toDateEdit.setMinimumSize(QSize(130, 25))
        self.toDateEdit.setAlignment(Qt.AlignCenter)
        self.toDateEdit.setReadOnly(False)
        self.toDateEdit.setCalendarPopup(True)
        self.toDateEdit.setTimeSpec(Qt.LocalTime)

        self.verticalLayout_4.addWidget(self.toDateEdit, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.budgetLabel = QLabel(self.widget_2)
        self.budgetLabel.setObjectName(u"budgetLabel")
        self.budgetLabel.setFont(font3)

        self.verticalLayout_6.addWidget(self.budgetLabel, 0, Qt.AlignHCenter)

        self.budgetSpinBox = QSpinBox(self.widget_2)
        self.budgetSpinBox.setObjectName(u"budgetSpinBox")
        self.budgetSpinBox.setMinimumSize(QSize(130, 25))
        self.budgetSpinBox.setStyleSheet(u"")
        self.budgetSpinBox.setAlignment(Qt.AlignCenter)
        self.budgetSpinBox.setMaximum(999999999)
        self.budgetSpinBox.setSingleStep(10)

        self.verticalLayout_6.addWidget(self.budgetSpinBox, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.saveButton = QPushButton(self.widget_2)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(130, 30))

        self.verticalLayout_2.addWidget(self.saveButton, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget_2)


        self.retranslateUi(createTravelWindow)

        QMetaObject.connectSlotsByName(createTravelWindow)
    # setupUi

    def retranslateUi(self, createTravelWindow):
        createTravelWindow.setWindowTitle(QCoreApplication.translate("createTravelWindow", u"Creating Travel", None))
        self.destinationLabel.setText(QCoreApplication.translate("createTravelWindow", u"Destination List", None))
        self.addButton.setText(QCoreApplication.translate("createTravelWindow", u"Add", None))
        self.previewButton.setText(QCoreApplication.translate("createTravelWindow", u"Preview", None))
        self.removeButton.setText(QCoreApplication.translate("createTravelWindow", u"Delete", None))
        self.nameLabel.setText(QCoreApplication.translate("createTravelWindow", u"Travel Name : ", None))
        self.fromLabel.setText(QCoreApplication.translate("createTravelWindow", u"From:", None))
        self.fromDateEdit.setDisplayFormat(QCoreApplication.translate("createTravelWindow", u"d/MM/yyyy", None))
        self.toLabel.setText(QCoreApplication.translate("createTravelWindow", u"To:", None))
        self.toDateEdit.setDisplayFormat(QCoreApplication.translate("createTravelWindow", u"d/MM/yyyy", None))
        self.budgetLabel.setText(QCoreApplication.translate("createTravelWindow", u"Budget: ", None))
        self.budgetSpinBox.setSuffix("")
        self.budgetSpinBox.setPrefix("")
        self.saveButton.setText(QCoreApplication.translate("createTravelWindow", u"Save", None))
    # retranslateUi

