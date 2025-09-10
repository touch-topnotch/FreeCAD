# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgProjectUtility.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Gui_Dialog_DlgProjectUtility(object):
    def setupUi(self, Gui__Dialog__DlgProjectUtility):
        if not Gui__Dialog__DlgProjectUtility.objectName():
            Gui__Dialog__DlgProjectUtility.setObjectName(u"Gui__Dialog__DlgProjectUtility")
        Gui__Dialog__DlgProjectUtility.resize(445, 262)
        self.gridLayout_4 = QGridLayout(Gui__Dialog__DlgProjectUtility)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(Gui__Dialog__DlgProjectUtility)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.extractSource = Gui_FileChooser(self.groupBox)
        self.extractSource.setObjectName(u"extractSource")
        self.extractSource.setFilter(u"Document file (*.FCStd)")

        self.gridLayout.addWidget(self.extractSource, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.extractDest = Gui_FileChooser(self.groupBox)
        self.extractDest.setObjectName(u"extractDest")
        self.extractDest.setMode(Gui.FileChooser.Directory)

        self.gridLayout.addWidget(self.extractDest, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.extractButton = QPushButton(Gui__Dialog__DlgProjectUtility)
        self.extractButton.setObjectName(u"extractButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extractButton.sizePolicy().hasHeightForWidth())
        self.extractButton.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.extractButton, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgProjectUtility)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.createSource = Gui_FileChooser(self.groupBox_2)
        self.createSource.setObjectName(u"createSource")
        self.createSource.setFilter(u"Document.xml")

        self.gridLayout_2.addWidget(self.createSource, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.createDest = Gui_FileChooser(self.groupBox_2)
        self.createDest.setObjectName(u"createDest")
        self.createDest.setMode(Gui.FileChooser.Directory)

        self.gridLayout_2.addWidget(self.createDest, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.createButton = QPushButton(Gui__Dialog__DlgProjectUtility)
        self.createButton.setObjectName(u"createButton")
        sizePolicy.setHeightForWidth(self.createButton.sizePolicy().hasHeightForWidth())
        self.createButton.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.createButton, 1, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.checkLoadProject = QCheckBox(Gui__Dialog__DlgProjectUtility)
        self.checkLoadProject.setObjectName(u"checkLoadProject")

        self.gridLayout_4.addWidget(self.checkLoadProject, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__DlgProjectUtility)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.gridLayout_4.addWidget(self.buttonBox, 2, 1, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgProjectUtility)
        self.buttonBox.accepted.connect(Gui__Dialog__DlgProjectUtility.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__DlgProjectUtility.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgProjectUtility)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgProjectUtility):
        Gui__Dialog__DlgProjectUtility.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgProjectUtility", u"Document utility", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgProjectUtility", u"Extract document", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectUtility", u"Source", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectUtility", u"Destination", None))
        self.extractButton.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectUtility", u"Extract", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgProjectUtility", u"Create document", None))
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectUtility", u"Source", None))
        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectUtility", u"Destination", None))
        self.createButton.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectUtility", u"Create", None))
        self.checkLoadProject.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectUtility", u"Load document file after creation", None))
    # retranslateUi

