# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgParameter.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QWidget)

class Ui_Gui_Dialog_DlgParameter(object):
    def setupUi(self, Gui__Dialog__DlgParameter):
        if not Gui__Dialog__DlgParameter.objectName():
            Gui__Dialog__DlgParameter.setObjectName(u"Gui__Dialog__DlgParameter")
        Gui__Dialog__DlgParameter.resize(657, 558)
        Gui__Dialog__DlgParameter.setSizeGripEnabled(True)
        Gui__Dialog__DlgParameter.setModal(True)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgParameter)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.parameterSet = QComboBox(Gui__Dialog__DlgParameter)
        self.parameterSet.setObjectName(u"parameterSet")

        self.gridLayout.addWidget(self.parameterSet, 0, 0, 1, 1)

        self.splitter3 = QSplitter(Gui__Dialog__DlgParameter)
        self.splitter3.setObjectName(u"splitter3")
        self.splitter3.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.splitter3, 1, 0, 1, 1)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.checkSort = QCheckBox(Gui__Dialog__DlgParameter)
        self.checkSort.setObjectName(u"checkSort")
        self.checkSort.setChecked(True)

        self.hboxLayout.addWidget(self.checkSort)

        self.quickSearch = QLabel(Gui__Dialog__DlgParameter)
        self.quickSearch.setObjectName(u"quickSearch")

        self.hboxLayout.addWidget(self.quickSearch)

        self.findGroupLE = QLineEdit(Gui__Dialog__DlgParameter)
        self.findGroupLE.setObjectName(u"findGroupLE")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findGroupLE.sizePolicy().hasHeightForWidth())
        self.findGroupLE.setSizePolicy(sizePolicy)

        self.hboxLayout.addWidget(self.findGroupLE)

        self.buttonFind = QPushButton(Gui__Dialog__DlgParameter)
        self.buttonFind.setObjectName(u"buttonFind")

        self.hboxLayout.addWidget(self.buttonFind)

        self.spacerItem = QSpacerItem(351, 27, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.spacerItem)

        self.buttonSaveToDisk = QPushButton(Gui__Dialog__DlgParameter)
        self.buttonSaveToDisk.setObjectName(u"buttonSaveToDisk")
        self.buttonSaveToDisk.setAutoDefault(True)

        self.hboxLayout.addWidget(self.buttonSaveToDisk)

        self.closeButton = QPushButton(Gui__Dialog__DlgParameter)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setAutoDefault(True)

        self.hboxLayout.addWidget(self.closeButton)


        self.gridLayout.addLayout(self.hboxLayout, 2, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgParameter)

        self.buttonSaveToDisk.setDefault(True)
        self.closeButton.setDefault(True)


        QMetaObject.connectSlotsByName(Gui__Dialog__DlgParameter)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgParameter):
        Gui__Dialog__DlgParameter.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgParameter", u"Parameter Editor", None))
        self.checkSort.setText(QCoreApplication.translate("Gui::Dialog::DlgParameter", u"Sorted", None))
        self.quickSearch.setText(QCoreApplication.translate("Gui::Dialog::DlgParameter", u"Search", None))
#if QT_CONFIG(tooltip)
        self.findGroupLE.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgParameter", u"Enter a group name to search", None))
#endif // QT_CONFIG(tooltip)
        self.findGroupLE.setPlaceholderText(QCoreApplication.translate("Gui::Dialog::DlgParameter", u"Search group", None))
        self.buttonFind.setText(QCoreApplication.translate("Gui::Dialog::DlgParameter", u"Find", None))
        self.buttonSaveToDisk.setText(QCoreApplication.translate("Gui::Dialog::DlgParameter", u"Save", None))
#if QT_CONFIG(shortcut)
        self.buttonSaveToDisk.setShortcut(QCoreApplication.translate("Gui::Dialog::DlgParameter", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.closeButton.setText(QCoreApplication.translate("Gui::Dialog::DlgParameter", u"&Close", None))
#if QT_CONFIG(shortcut)
        self.closeButton.setShortcut(QCoreApplication.translate("Gui::Dialog::DlgParameter", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

