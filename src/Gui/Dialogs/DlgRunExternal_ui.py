# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgRunExternal.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgRunExternal(object):
    def setupUi(self, Gui__Dialog__DlgRunExternal):
        if not Gui__Dialog__DlgRunExternal.objectName():
            Gui__Dialog__DlgRunExternal.setObjectName(u"Gui__Dialog__DlgRunExternal")
        Gui__Dialog__DlgRunExternal.resize(387, 363)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Gui__Dialog__DlgRunExternal.sizePolicy().hasHeightForWidth())
        Gui__Dialog__DlgRunExternal.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgRunExternal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.programName = QLabel(Gui__Dialog__DlgRunExternal)
        self.programName.setObjectName(u"programName")
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.programName.setFont(font)

        self.horizontalLayout.addWidget(self.programName)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonAdvanced = QPushButton(Gui__Dialog__DlgRunExternal)
        self.buttonAdvanced.setObjectName(u"buttonAdvanced")

        self.horizontalLayout.addWidget(self.buttonAdvanced)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.extensionWidget = QWidget(Gui__Dialog__DlgRunExternal)
        self.extensionWidget.setObjectName(u"extensionWidget")
        self.verticalLayout = QVBoxLayout(self.extensionWidget)
#ifndef Q_OS_MAC
        self.verticalLayout.setSpacing(6)
#endif
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.hboxLayout = QHBoxLayout()
#ifndef Q_OS_MAC
        self.hboxLayout.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
#endif
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.programPath = QLineEdit(self.extensionWidget)
        self.programPath.setObjectName(u"programPath")

        self.hboxLayout.addWidget(self.programPath)

        self.chooseProgram = QPushButton(self.extensionWidget)
        self.chooseProgram.setObjectName(u"chooseProgram")
        self.chooseProgram.setText(u"Choose Program")

        self.hboxLayout.addWidget(self.chooseProgram)


        self.verticalLayout.addLayout(self.hboxLayout)

        self.output = QTextEdit(self.extensionWidget)
        self.output.setObjectName(u"output")

        self.verticalLayout.addWidget(self.output)


        self.gridLayout.addWidget(self.extensionWidget, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonAccept = QPushButton(Gui__Dialog__DlgRunExternal)
        self.buttonAccept.setObjectName(u"buttonAccept")

        self.horizontalLayout_2.addWidget(self.buttonAccept)

        self.buttonDiscard = QPushButton(Gui__Dialog__DlgRunExternal)
        self.buttonDiscard.setObjectName(u"buttonDiscard")

        self.horizontalLayout_2.addWidget(self.buttonDiscard)

        self.buttonAbort = QPushButton(Gui__Dialog__DlgRunExternal)
        self.buttonAbort.setObjectName(u"buttonAbort")

        self.horizontalLayout_2.addWidget(self.buttonAbort)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.buttonHelp = QPushButton(Gui__Dialog__DlgRunExternal)
        self.buttonHelp.setObjectName(u"buttonHelp")

        self.horizontalLayout_2.addWidget(self.buttonHelp)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgRunExternal)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgRunExternal)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgRunExternal):
        Gui__Dialog__DlgRunExternal.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgRunExternal", u"Running External Program", None))
        self.programName.setText(QCoreApplication.translate("Gui::Dialog::DlgRunExternal", u"TextLabel", None))
        self.buttonAdvanced.setText(QCoreApplication.translate("Gui::Dialog::DlgRunExternal", u"Advanced >>", None))
        self.buttonAccept.setText(QCoreApplication.translate("Gui::Dialog::DlgRunExternal", u"Accept Changes", None))
        self.buttonDiscard.setText(QCoreApplication.translate("Gui::Dialog::DlgRunExternal", u"Discard Changes", None))
        self.buttonAbort.setText(QCoreApplication.translate("Gui::Dialog::DlgRunExternal", u"Abort Program", None))
        self.buttonHelp.setText(QCoreApplication.translate("Gui::Dialog::DlgRunExternal", u"Help", None))
    # retranslateUi

