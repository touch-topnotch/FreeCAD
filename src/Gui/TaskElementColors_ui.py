# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskElementColors.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Gui_TaskElementColors(object):
    def setupUi(self, Gui__TaskElementColors):
        if not Gui__TaskElementColors.objectName():
            Gui__TaskElementColors.setObjectName(u"Gui__TaskElementColors")
        Gui__TaskElementColors.resize(483, 406)
        self.gridLayout_2 = QGridLayout(Gui__TaskElementColors)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.objectLabel = QLabel(Gui__TaskElementColors)
        self.objectLabel.setObjectName(u"objectLabel")

        self.verticalLayout.addWidget(self.objectLabel)

        self.elementList = QListWidget(Gui__TaskElementColors)
        self.elementList.setObjectName(u"elementList")
        self.elementList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.elementList)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.addSelection = QPushButton(Gui__TaskElementColors)
        self.addSelection.setObjectName(u"addSelection")

        self.gridLayout_6.addWidget(self.addSelection, 0, 0, 1, 1)

        self.hideSelection = QPushButton(Gui__TaskElementColors)
        self.hideSelection.setObjectName(u"hideSelection")

        self.gridLayout_6.addWidget(self.hideSelection, 0, 1, 1, 1)

        self.removeSelection = QPushButton(Gui__TaskElementColors)
        self.removeSelection.setObjectName(u"removeSelection")

        self.gridLayout_6.addWidget(self.removeSelection, 0, 2, 1, 1)

        self.removeAll = QPushButton(Gui__TaskElementColors)
        self.removeAll.setObjectName(u"removeAll")

        self.gridLayout_6.addWidget(self.removeAll, 0, 3, 1, 1)

        self.boxSelect = QPushButton(Gui__TaskElementColors)
        self.boxSelect.setObjectName(u"boxSelect")

        self.gridLayout_6.addWidget(self.boxSelect, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_6, 3, 0, 1, 1)

        self.recompute = QCheckBox(Gui__TaskElementColors)
        self.recompute.setObjectName(u"recompute")

        self.gridLayout_2.addWidget(self.recompute, 4, 0, 1, 1)

        self.onTop = QCheckBox(Gui__TaskElementColors)
        self.onTop.setObjectName(u"onTop")

        self.gridLayout_2.addWidget(self.onTop, 5, 0, 1, 1)


        self.retranslateUi(Gui__TaskElementColors)

        QMetaObject.connectSlotsByName(Gui__TaskElementColors)
    # setupUi

    def retranslateUi(self, Gui__TaskElementColors):
        Gui__TaskElementColors.setWindowTitle(QCoreApplication.translate("Gui::TaskElementColors", u"Set Element Color", None))
        self.objectLabel.setText(QCoreApplication.translate("Gui::TaskElementColors", u"TextLabel", None))
        self.addSelection.setText(QCoreApplication.translate("Gui::TaskElementColors", u"Edit", None))
        self.hideSelection.setText(QCoreApplication.translate("Gui::TaskElementColors", u"Hide", None))
        self.removeSelection.setText(QCoreApplication.translate("Gui::TaskElementColors", u"Remove", None))
        self.removeAll.setText(QCoreApplication.translate("Gui::TaskElementColors", u"Remove All", None))
        self.boxSelect.setText(QCoreApplication.translate("Gui::TaskElementColors", u"Box Select", None))
        self.recompute.setText(QCoreApplication.translate("Gui::TaskElementColors", u"Recompute after commit", None))
        self.onTop.setText(QCoreApplication.translate("Gui::TaskElementColors", u"On top when selected", None))
    # retranslateUi

