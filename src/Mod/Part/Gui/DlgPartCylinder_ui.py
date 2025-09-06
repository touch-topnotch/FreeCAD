# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPartCylinder.ui'
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

class Ui_PartGui_DlgPartCylinder(object):
    def setupUi(self, PartGui__DlgPartCylinder):
        if not PartGui__DlgPartCylinder.objectName():
            PartGui__DlgPartCylinder.setObjectName(u"PartGui__DlgPartCylinder")
        PartGui__DlgPartCylinder.resize(275, 279)
        self.gridLayout = QGridLayout(PartGui__DlgPartCylinder)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.GroupBox5 = QGroupBox(PartGui__DlgPartCylinder)
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

        self.groupBox = QGroupBox(PartGui__DlgPartCylinder)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout2 = QGridLayout(self.groupBox)
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.TextLabel1_2 = QLabel(self.groupBox)
        self.TextLabel1_2.setObjectName(u"TextLabel1_2")

        self.gridLayout2.addWidget(self.TextLabel1_2, 0, 0, 1, 1)

        self.radius = Gui_QuantitySpinBox(self.groupBox)
        self.radius.setObjectName(u"radius")
        self.radius.setProperty(u"unit", u"mm")
        self.radius.setMaximum(2147480000.000000000000000)
        self.radius.setValue(10.000000000000000)

        self.gridLayout2.addWidget(self.radius, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout2.addWidget(self.label, 1, 0, 1, 1)

        self.length = Gui_QuantitySpinBox(self.groupBox)
        self.length.setObjectName(u"length")
        self.length.setProperty(u"unit", u"mm")
        self.length.setMaximum(2147480000.000000000000000)
        self.length.setValue(100.000000000000000)

        self.gridLayout2.addWidget(self.length, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(PartGui__DlgPartCylinder)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        QWidget.setTabOrder(self.xPos, self.yPos)
        QWidget.setTabOrder(self.yPos, self.zPos)
        QWidget.setTabOrder(self.zPos, self.direction)
        QWidget.setTabOrder(self.direction, self.radius)
        QWidget.setTabOrder(self.radius, self.length)

        self.retranslateUi(PartGui__DlgPartCylinder)
        self.buttonBox.accepted.connect(PartGui__DlgPartCylinder.accept)
        self.buttonBox.rejected.connect(PartGui__DlgPartCylinder.reject)

        self.direction.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(PartGui__DlgPartCylinder)
    # setupUi

    def retranslateUi(self, PartGui__DlgPartCylinder):
        PartGui__DlgPartCylinder.setWindowTitle(QCoreApplication.translate("PartGui::DlgPartCylinder", u"Cylinder Definition", None))
        self.GroupBox5.setTitle(QCoreApplication.translate("PartGui::DlgPartCylinder", u"Position", None))
        self.TextLabel1.setText(QCoreApplication.translate("PartGui::DlgPartCylinder", u"X", None))
        self.TextLabel2.setText(QCoreApplication.translate("PartGui::DlgPartCylinder", u"Y", None))
        self.TextLabel3.setText(QCoreApplication.translate("PartGui::DlgPartCylinder", u"Z", None))
        self.TextLabel1_3.setText(QCoreApplication.translate("PartGui::DlgPartCylinder", u"Direction", None))
        self.groupBox.setTitle(QCoreApplication.translate("PartGui::DlgPartCylinder", u"Parameter", None))
        self.TextLabel1_2.setText(QCoreApplication.translate("PartGui::DlgPartCylinder", u"Radius", None))
        self.label.setText(QCoreApplication.translate("PartGui::DlgPartCylinder", u"Height", None))
    # retranslateUi

