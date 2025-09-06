# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPreferencePackManagement.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QHBoxLayout, QHeaderView, QPushButton, QSizePolicy,
    QSpacerItem, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_Gui_Dialog_DlgPreferencePackManagement(object):
    def setupUi(self, Gui__Dialog__DlgPreferencePackManagement):
        if not Gui__Dialog__DlgPreferencePackManagement.objectName():
            Gui__Dialog__DlgPreferencePackManagement.setObjectName(u"Gui__Dialog__DlgPreferencePackManagement")
        Gui__Dialog__DlgPreferencePackManagement.resize(392, 255)
        Gui__Dialog__DlgPreferencePackManagement.setSizeGripEnabled(True)
        Gui__Dialog__DlgPreferencePackManagement.setModal(False)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgPreferencePackManagement)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonOpenAddonManager = QPushButton(Gui__Dialog__DlgPreferencePackManagement)
        self.pushButtonOpenAddonManager.setObjectName(u"pushButtonOpenAddonManager")

        self.horizontalLayout.addWidget(self.pushButtonOpenAddonManager)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.treeWidget = QTreeWidget(Gui__Dialog__DlgPreferencePackManagement)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeWidget.setProperty(u"showDropIndicator", False)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.header().setStretchLastSection(False)

        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgPreferencePackManagement)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgPreferencePackManagement)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgPreferencePackManagement):
        Gui__Dialog__DlgPreferencePackManagement.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgPreferencePackManagement", u"Manage Preference Packs", None))
        self.pushButtonOpenAddonManager.setText(QCoreApplication.translate("Gui::Dialog::DlgPreferencePackManagement", u"Open Addon Manager", None))
    # retranslateUi

