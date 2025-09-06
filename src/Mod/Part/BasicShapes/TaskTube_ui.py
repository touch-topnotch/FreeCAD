# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskTube.ui'
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
    QSizePolicy, QWidget)
import Part_rc

class Ui_PartGui_TaskTube(object):
    def setupUi(self, PartGui__TaskTube):
        if not PartGui__TaskTube.objectName():
            PartGui__TaskTube.setObjectName(u"PartGui__TaskTube")
        PartGui__TaskTube.resize(367, 125)
        PartGui__TaskTube.setProperty(u"sizeGripEnabled", True)
        self.gridLayout = QGridLayout(PartGui__TaskTube)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(PartGui__TaskTube)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout1 = QGridLayout()
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.textLabel1 = QLabel(self.groupBox)
        self.textLabel1.setObjectName(u"textLabel1")

        self.gridLayout1.addWidget(self.textLabel1, 0, 0, 1, 1)

        self.tubeOuterRadius = Gui_QuantitySpinBox(self.groupBox)
        self.tubeOuterRadius.setObjectName(u"tubeOuterRadius")
        self.tubeOuterRadius.setKeyboardTracking(False)
        self.tubeOuterRadius.setProperty(u"unit", u"mm")
        self.tubeOuterRadius.setMinimum(0.000000000000000)
        self.tubeOuterRadius.setValue(4.000000000000000)

        self.gridLayout1.addWidget(self.tubeOuterRadius, 0, 2, 1, 1)

        self.textLabel2 = QLabel(self.groupBox)
        self.textLabel2.setObjectName(u"textLabel2")

        self.gridLayout1.addWidget(self.textLabel2, 1, 0, 1, 1)

        self.tubeInnerRadius = Gui_QuantitySpinBox(self.groupBox)
        self.tubeInnerRadius.setObjectName(u"tubeInnerRadius")
        self.tubeInnerRadius.setKeyboardTracking(False)
        self.tubeInnerRadius.setProperty(u"unit", u"mm")
        self.tubeInnerRadius.setMinimum(0.000000000000000)
        self.tubeInnerRadius.setValue(2.000000000000000)

        self.gridLayout1.addWidget(self.tubeInnerRadius, 1, 2, 1, 1)

        self.textLabel3 = QLabel(self.groupBox)
        self.textLabel3.setObjectName(u"textLabel3")

        self.gridLayout1.addWidget(self.textLabel3, 2, 0, 1, 1)

        self.tubeHeight = Gui_QuantitySpinBox(self.groupBox)
        self.tubeHeight.setObjectName(u"tubeHeight")
        self.tubeHeight.setKeyboardTracking(False)
        self.tubeHeight.setProperty(u"unit", u"mm")
        self.tubeHeight.setMinimum(0.000000000000000)
        self.tubeHeight.setValue(10.000000000000000)

        self.gridLayout1.addWidget(self.tubeHeight, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout1, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        QWidget.setTabOrder(self.tubeOuterRadius, self.tubeInnerRadius)
        QWidget.setTabOrder(self.tubeInnerRadius, self.tubeHeight)

        self.retranslateUi(PartGui__TaskTube)

        QMetaObject.connectSlotsByName(PartGui__TaskTube)
    # setupUi

    def retranslateUi(self, PartGui__TaskTube):
        PartGui__TaskTube.setWindowTitle(QCoreApplication.translate("PartGui::TaskTube", u"Tube", None))
        self.groupBox.setTitle(QCoreApplication.translate("PartGui::TaskTube", u"Parameter", None))
        self.textLabel1.setText(QCoreApplication.translate("PartGui::TaskTube", u"Outer radius", None))
        self.textLabel2.setText(QCoreApplication.translate("PartGui::TaskTube", u"Inner radius", None))
        self.textLabel3.setText(QCoreApplication.translate("PartGui::TaskTube", u"Height", None))
    # retranslateUi

