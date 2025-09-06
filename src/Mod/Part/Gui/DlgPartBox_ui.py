# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPartBox.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QWidget)

class Ui_PartGui_DlgPartBox(object):
    def setupUi(self, PartGui__DlgPartBox):
        if not PartGui__DlgPartBox.objectName():
            PartGui__DlgPartBox.setObjectName(u"PartGui__DlgPartBox")
        PartGui__DlgPartBox.resize(257, 305)
        self.gridLayout = QGridLayout(PartGui__DlgPartBox)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.GroupBox5 = QGroupBox(PartGui__DlgPartBox)
        self.GroupBox5.setObjectName(u"GroupBox5")
        self.gridLayout1 = QGridLayout(self.GroupBox5)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.TextLabel1 = QLabel(self.GroupBox5)
        self.TextLabel1.setObjectName(u"TextLabel1")

        self.gridLayout1.addWidget(self.TextLabel1, 0, 0, 1, 1)

        self.xPos = Gui_QuantitySpinBox(self.GroupBox5)
        self.xPos.setObjectName(u"xPos")
        self.xPos.setProperty(u"unit", u"mm")
        self.xPos.setMinimum(-2147480000.000000000000000)
        self.xPos.setMaximum(2147480000.000000000000000)

        self.gridLayout1.addWidget(self.xPos, 0, 1, 1, 1)

        self.TextLabel2 = QLabel(self.GroupBox5)
        self.TextLabel2.setObjectName(u"TextLabel2")

        self.gridLayout1.addWidget(self.TextLabel2, 1, 0, 1, 1)

        self.yPos = Gui_QuantitySpinBox(self.GroupBox5)
        self.yPos.setObjectName(u"yPos")
        self.yPos.setProperty(u"unit", u"mm")
        self.yPos.setMinimum(-2147480000.000000000000000)
        self.yPos.setMaximum(2147480000.000000000000000)

        self.gridLayout1.addWidget(self.yPos, 1, 1, 1, 1)

        self.TextLabel3 = QLabel(self.GroupBox5)
        self.TextLabel3.setObjectName(u"TextLabel3")

        self.gridLayout1.addWidget(self.TextLabel3, 2, 0, 1, 1)

        self.zPos = Gui_QuantitySpinBox(self.GroupBox5)
        self.zPos.setObjectName(u"zPos")
        self.zPos.setProperty(u"unit", u"mm")
        self.zPos.setMinimum(-2147480000.000000000000000)
        self.zPos.setMaximum(2147480000.000000000000000)

        self.gridLayout1.addWidget(self.zPos, 2, 1, 1, 1)

        self.TextLabel1_3 = QLabel(self.GroupBox5)
        self.TextLabel1_3.setObjectName(u"TextLabel1_3")

        self.gridLayout1.addWidget(self.TextLabel1_3, 3, 0, 1, 1)

        self.direction = QComboBox(self.GroupBox5)
        self.direction.setObjectName(u"direction")

        self.gridLayout1.addWidget(self.direction, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.GroupBox5, 0, 0, 1, 1)

        self.GroupBox5_2 = QGroupBox(PartGui__DlgPartBox)
        self.GroupBox5_2.setObjectName(u"GroupBox5_2")
        self.gridLayout2 = QGridLayout(self.GroupBox5_2)
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.TextLabel1_2 = QLabel(self.GroupBox5_2)
        self.TextLabel1_2.setObjectName(u"TextLabel1_2")

        self.gridLayout2.addWidget(self.TextLabel1_2, 0, 0, 1, 1)

        self.uLength = Gui_QuantitySpinBox(self.GroupBox5_2)
        self.uLength.setObjectName(u"uLength")
        self.uLength.setProperty(u"unit", u"mm")
        self.uLength.setMaximum(2147480000.000000000000000)
        self.uLength.setValue(100.000000000000000)

        self.gridLayout2.addWidget(self.uLength, 0, 1, 1, 1)

        self.TextLabel2_2 = QLabel(self.GroupBox5_2)
        self.TextLabel2_2.setObjectName(u"TextLabel2_2")

        self.gridLayout2.addWidget(self.TextLabel2_2, 1, 0, 1, 1)

        self.vLength = Gui_QuantitySpinBox(self.GroupBox5_2)
        self.vLength.setObjectName(u"vLength")
        self.vLength.setProperty(u"unit", u"mm")
        self.vLength.setMaximum(2147480000.000000000000000)
        self.vLength.setValue(100.000000000000000)

        self.gridLayout2.addWidget(self.vLength, 1, 1, 1, 1)

        self.TextLabel3_2 = QLabel(self.GroupBox5_2)
        self.TextLabel3_2.setObjectName(u"TextLabel3_2")

        self.gridLayout2.addWidget(self.TextLabel3_2, 2, 0, 1, 1)

        self.wLength = Gui_QuantitySpinBox(self.GroupBox5_2)
        self.wLength.setObjectName(u"wLength")
        self.wLength.setProperty(u"unit", u"mm")
        self.wLength.setMaximum(2147480000.000000000000000)
        self.wLength.setValue(100.000000000000000)

        self.gridLayout2.addWidget(self.wLength, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.GroupBox5_2, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(PartGui__DlgPartBox)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        QWidget.setTabOrder(self.xPos, self.yPos)
        QWidget.setTabOrder(self.yPos, self.zPos)
        QWidget.setTabOrder(self.zPos, self.direction)
        QWidget.setTabOrder(self.direction, self.uLength)
        QWidget.setTabOrder(self.uLength, self.vLength)
        QWidget.setTabOrder(self.vLength, self.wLength)

        self.retranslateUi(PartGui__DlgPartBox)
        self.buttonBox.accepted.connect(PartGui__DlgPartBox.accept)
        self.buttonBox.rejected.connect(PartGui__DlgPartBox.reject)

        self.direction.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(PartGui__DlgPartBox)
    # setupUi

    def retranslateUi(self, PartGui__DlgPartBox):
        PartGui__DlgPartBox.setWindowTitle(QCoreApplication.translate("PartGui::DlgPartBox", u"Box Definition", None))
        self.GroupBox5.setTitle(QCoreApplication.translate("PartGui::DlgPartBox", u"Position", None))
        self.TextLabel1.setText(QCoreApplication.translate("PartGui::DlgPartBox", u"X", None))
        self.TextLabel2.setText(QCoreApplication.translate("PartGui::DlgPartBox", u"Y", None))
        self.TextLabel3.setText(QCoreApplication.translate("PartGui::DlgPartBox", u"Z", None))
        self.TextLabel1_3.setText(QCoreApplication.translate("PartGui::DlgPartBox", u"Direction", None))
        self.GroupBox5_2.setTitle(QCoreApplication.translate("PartGui::DlgPartBox", u"Size", None))
        self.TextLabel1_2.setText(QCoreApplication.translate("PartGui::DlgPartBox", u"Length", None))
        self.TextLabel2_2.setText(QCoreApplication.translate("PartGui::DlgPartBox", u"Width", None))
        self.TextLabel3_2.setText(QCoreApplication.translate("PartGui::DlgPartBox", u"Height", None))
    # retranslateUi

