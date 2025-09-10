# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DownloadManager.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

from DownloadItem import EditTableView

class Ui_Gui_Dialog_DownloadManager(object):
    def setupUi(self, Gui__Dialog__DownloadManager):
        if not Gui__Dialog__DownloadManager.objectName():
            Gui__Dialog__DownloadManager.setObjectName(u"Gui__Dialog__DownloadManager")
        Gui__Dialog__DownloadManager.resize(332, 252)
        self.gridLayout = QGridLayout(Gui__Dialog__DownloadManager)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.downloadsView = EditTableView(Gui__Dialog__DownloadManager)
        self.downloadsView.setObjectName(u"downloadsView")

        self.gridLayout.addWidget(self.downloadsView, 0, 0, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cleanupButton = QPushButton(Gui__Dialog__DownloadManager)
        self.cleanupButton.setObjectName(u"cleanupButton")
        self.cleanupButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.cleanupButton)

        self.spacerItem = QSpacerItem(58, 24, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.spacerItem)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.itemCount = QLabel(Gui__Dialog__DownloadManager)
        self.itemCount.setObjectName(u"itemCount")

        self.gridLayout.addWidget(self.itemCount, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)


        self.retranslateUi(Gui__Dialog__DownloadManager)

        QMetaObject.connectSlotsByName(Gui__Dialog__DownloadManager)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DownloadManager):
        Gui__Dialog__DownloadManager.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DownloadManager", u"Downloads", None))
        self.cleanupButton.setText(QCoreApplication.translate("Gui::Dialog::DownloadManager", u"Clean up", None))
        self.itemCount.setText(QCoreApplication.translate("Gui::Dialog::DownloadManager", u"0 Items", None))
    # retranslateUi

