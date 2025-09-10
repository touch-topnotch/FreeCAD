# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgMacroRecord.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgMacroRecord(object):
    def setupUi(self, Gui__Dialog__DlgMacroRecord):
        if not Gui__Dialog__DlgMacroRecord.objectName():
            Gui__Dialog__DlgMacroRecord.setObjectName(u"Gui__Dialog__DlgMacroRecord")
        Gui__Dialog__DlgMacroRecord.resize(302, 229)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgMacroRecord)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(11, 11, 11, 11)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(11, 11, 11, 11)
        self.groupBox = QGroupBox(Gui__Dialog__DlgMacroRecord)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.lineEditPath = QLineEdit(self.groupBox)
        self.lineEditPath.setObjectName(u"lineEditPath")

        self.gridLayout.addWidget(self.lineEditPath, 0, 0, 1, 1)


        self.vboxLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgMacroRecord)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.hboxLayout = QHBoxLayout(self.groupBox_2)
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setContentsMargins(11, 11, 11, 11)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(11, 11, 11, 11)
        self.lineEditMacroPath = QLineEdit(self.groupBox_2)
        self.lineEditMacroPath.setObjectName(u"lineEditMacroPath")
        self.lineEditMacroPath.setEnabled(False)

        self.hboxLayout.addWidget(self.lineEditMacroPath)

        self.pushButtonChooseDir = QPushButton(self.groupBox_2)
        self.pushButtonChooseDir.setObjectName(u"pushButtonChooseDir")
        self.pushButtonChooseDir.setMaximumSize(QSize(35, 16777215))
        self.pushButtonChooseDir.setText(u"...")

        self.hboxLayout.addWidget(self.pushButtonChooseDir)


        self.vboxLayout.addWidget(self.groupBox_2)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setSpacing(6)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.hboxLayout1.setContentsMargins(11, 11, 11, 11)
        self.buttonStart = QPushButton(Gui__Dialog__DlgMacroRecord)
        self.buttonStart.setObjectName(u"buttonStart")

        self.hboxLayout1.addWidget(self.buttonStart)

        self.spacerItem = QSpacerItem(16, 27, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout1.addItem(self.spacerItem)

        self.buttonStop = QPushButton(Gui__Dialog__DlgMacroRecord)
        self.buttonStop.setObjectName(u"buttonStop")

        self.hboxLayout1.addWidget(self.buttonStop)

        self.buttonClose = QPushButton(Gui__Dialog__DlgMacroRecord)
        self.buttonClose.setObjectName(u"buttonClose")

        self.hboxLayout1.addWidget(self.buttonClose)


        self.vboxLayout.addLayout(self.hboxLayout1)

        QWidget.setTabOrder(self.lineEditPath, self.buttonStart)
        QWidget.setTabOrder(self.buttonStart, self.buttonStop)
        QWidget.setTabOrder(self.buttonStop, self.buttonClose)

        self.retranslateUi(Gui__Dialog__DlgMacroRecord)

        self.buttonStart.setDefault(True)
        self.buttonStop.setDefault(True)


        QMetaObject.connectSlotsByName(Gui__Dialog__DlgMacroRecord)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgMacroRecord):
        Gui__Dialog__DlgMacroRecord.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgMacroRecord", u"Macro recording", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgMacroRecord", u"Macro name:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgMacroRecord", u"Macro path:", None))
        self.buttonStart.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroRecord", u"Record", None))
        self.buttonStop.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroRecord", u"Stop", None))
        self.buttonClose.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroRecord", u"Close", None))
    # retranslateUi

