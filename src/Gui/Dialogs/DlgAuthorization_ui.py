# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgAuthorization.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Gui_Dialog_DlgAuthorization(object):
    def setupUi(self, Gui__Dialog__DlgAuthorization):
        if not Gui__Dialog__DlgAuthorization.objectName():
            Gui__Dialog__DlgAuthorization.setObjectName(u"Gui__Dialog__DlgAuthorization")
        Gui__Dialog__DlgAuthorization.resize(284, 128)
        Gui__Dialog__DlgAuthorization.setSizeGripEnabled(True)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgAuthorization)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(Gui__Dialog__DlgAuthorization)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.siteDescription = QLabel(Gui__Dialog__DlgAuthorization)
        self.siteDescription.setObjectName(u"siteDescription")
        font = QFont()
        font.setBold(True)
        self.siteDescription.setFont(font)
        self.siteDescription.setWordWrap(True)

        self.gridLayout.addWidget(self.siteDescription, 0, 1, 1, 1)

        self.textLabel1 = QLabel(Gui__Dialog__DlgAuthorization)
        self.textLabel1.setObjectName(u"textLabel1")

        self.gridLayout.addWidget(self.textLabel1, 1, 0, 1, 1)

        self.username = QLineEdit(Gui__Dialog__DlgAuthorization)
        self.username.setObjectName(u"username")

        self.gridLayout.addWidget(self.username, 1, 1, 1, 1)

        self.textLabel2 = QLabel(Gui__Dialog__DlgAuthorization)
        self.textLabel2.setObjectName(u"textLabel2")

        self.gridLayout.addWidget(self.textLabel2, 2, 0, 1, 1)

        self.password = QLineEdit(Gui__Dialog__DlgAuthorization)
        self.password.setObjectName(u"password")
        self.password.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.password, 2, 1, 1, 1)

        self.spacerItem = QSpacerItem(21, 41, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.spacerItem, 3, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__DlgAuthorization)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)

        QWidget.setTabOrder(self.username, self.password)

        self.retranslateUi(Gui__Dialog__DlgAuthorization)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgAuthorization)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgAuthorization):
        Gui__Dialog__DlgAuthorization.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgAuthorization", u"Authorization", None))
        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::DlgAuthorization", u"Site:", None))
        self.siteDescription.setText(QCoreApplication.translate("Gui::Dialog::DlgAuthorization", u"%1 at %2", None))
        self.textLabel1.setText(QCoreApplication.translate("Gui::Dialog::DlgAuthorization", u"Username:", None))
        self.textLabel2.setText(QCoreApplication.translate("Gui::Dialog::DlgAuthorization", u"Password:", None))
    # retranslateUi

