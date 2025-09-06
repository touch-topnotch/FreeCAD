# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgChooseIcon.ui'
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
    QGridLayout, QHBoxLayout, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Gui_Dialog_DlgChooseIcon(object):
    def setupUi(self, Gui__Dialog__DlgChooseIcon):
        if not Gui__Dialog__DlgChooseIcon.objectName():
            Gui__Dialog__DlgChooseIcon.setObjectName(u"Gui__Dialog__DlgChooseIcon")
        Gui__Dialog__DlgChooseIcon.resize(430, 370)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgChooseIcon)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget = QListWidget(Gui__Dialog__DlgChooseIcon)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGridSize(QSize(50, 50))
        self.listWidget.setViewMode(QListView.IconMode)
        self.listWidget.setUniformItemSizes(False)

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addButton = QPushButton(Gui__Dialog__DlgChooseIcon)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout.addWidget(self.addButton)

        self.spacerItem = QSpacerItem(38, 31, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.spacerItem)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__DlgChooseIcon)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgChooseIcon)
        self.buttonBox.accepted.connect(Gui__Dialog__DlgChooseIcon.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__DlgChooseIcon.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgChooseIcon)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgChooseIcon):
        Gui__Dialog__DlgChooseIcon.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgChooseIcon", u"Choose Icon", None))
        self.addButton.setText(QCoreApplication.translate("Gui::Dialog::DlgChooseIcon", u"Icon Folders", None))
    # retranslateUi

