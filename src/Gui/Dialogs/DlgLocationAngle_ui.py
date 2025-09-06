# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgLocationAngle.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Angle(object):
    def setupUi(self, Angle):
        if not Angle.objectName():
            Angle.setObjectName(u"Angle")
        Angle.resize(145, 147)
        Angle.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(Angle)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Angle)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.vectorA = QDoubleSpinBox(Angle)
        self.vectorA.setObjectName(u"vectorA")
        self.vectorA.setMinimum(-2147480000.000000000000000)
        self.vectorA.setMaximum(2147480000.000000000000000)

        self.horizontalLayout.addWidget(self.vectorA)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Angle)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.vectorB = QDoubleSpinBox(Angle)
        self.vectorB.setObjectName(u"vectorB")
        self.vectorB.setMinimum(-2147480000.000000000000000)
        self.vectorB.setMaximum(2147480000.000000000000000)

        self.horizontalLayout_2.addWidget(self.vectorB)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Angle)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.vectorC = QDoubleSpinBox(Angle)
        self.vectorC.setObjectName(u"vectorC")
        self.vectorC.setMinimum(-2147480000.000000000000000)
        self.vectorC.setMaximum(2147480000.000000000000000)
        self.vectorC.setValue(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.vectorC)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.checkBoxSnap = QCheckBox(Angle)
        self.checkBoxSnap.setObjectName(u"checkBoxSnap")

        self.verticalLayout.addWidget(self.checkBoxSnap)

        self.comboGridSize = QComboBox(Angle)
        self.comboGridSize.addItem(u"1 \u00b0")
        self.comboGridSize.addItem(u"2 \u00b0")
        self.comboGridSize.addItem(u"5 \u00b0")
        self.comboGridSize.addItem(u"10 \u00b0")
        self.comboGridSize.addItem(u"20 \u00b0")
        self.comboGridSize.addItem(u"45 \u00b0")
        self.comboGridSize.addItem(u"90 \u00b0")
        self.comboGridSize.addItem(u"180 \u00b0")
        self.comboGridSize.setObjectName(u"comboGridSize")
        self.comboGridSize.setEditable(True)

        self.verticalLayout.addWidget(self.comboGridSize)


        self.retranslateUi(Angle)

        QMetaObject.connectSlotsByName(Angle)
    # setupUi

    def retranslateUi(self, Angle):
        self.label.setText(QCoreApplication.translate("Angle", u"A", None))
        self.label_2.setText(QCoreApplication.translate("Angle", u"B", None))
        self.label_3.setText(QCoreApplication.translate("Angle", u"C", None))
        self.checkBoxSnap.setText(QCoreApplication.translate("Angle", u"Angle snap", None))

        pass
    # retranslateUi

