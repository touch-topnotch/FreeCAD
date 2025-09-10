# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgOnlineHelp.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Gui_Dialog_DlgOnlineHelp(object):
    def setupUi(self, Gui__Dialog__DlgOnlineHelp):
        if not Gui__Dialog__DlgOnlineHelp.objectName():
            Gui__Dialog__DlgOnlineHelp.setObjectName(u"Gui__Dialog__DlgOnlineHelp")
        Gui__Dialog__DlgOnlineHelp.resize(395, 440)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgOnlineHelp)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.GroupBoxOther = QGroupBox(Gui__Dialog__DlgOnlineHelp)
        self.GroupBoxOther.setObjectName(u"GroupBoxOther")
        self.gridLayout1 = QGridLayout(self.GroupBoxOther)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.TextLabelURL = QLabel(self.GroupBoxOther)
        self.TextLabelURL.setObjectName(u"TextLabelURL")

        self.gridLayout1.addWidget(self.TextLabelURL, 0, 0, 1, 1)

        self.prefStartPage = Gui_PrefFileChooser(self.GroupBoxOther)
        self.prefStartPage.setObjectName(u"prefStartPage")
        self.prefStartPage.setProperty(u"prefEntry", u"Startpage")
        self.prefStartPage.setProperty(u"prefPath", u"OnlineHelp")

        self.gridLayout1.addWidget(self.prefStartPage, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.GroupBoxOther, 0, 0, 1, 1)

        self.spacerItem = QSpacerItem(373, 291, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.spacerItem, 1, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgOnlineHelp)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgOnlineHelp)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgOnlineHelp):
        Gui__Dialog__DlgOnlineHelp.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgOnlineHelp", u"On-line help", None))
        self.GroupBoxOther.setTitle(QCoreApplication.translate("Gui::Dialog::DlgOnlineHelp", u"Help viewer", None))
        self.TextLabelURL.setText(QCoreApplication.translate("Gui::Dialog::DlgOnlineHelp", u"Location of start page", None))
    # retranslateUi

