# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgLocationPos.ui'
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

class Ui_Position(object):
    def setupUi(self, Position):
        if not Position.objectName():
            Position.setObjectName(u"Position")
        Position.resize(171, 178)
        Position.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(Position)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Position)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.vectorX = QDoubleSpinBox(Position)
        self.vectorX.setObjectName(u"vectorX")
        self.vectorX.setMinimum(-2147480000.000000000000000)
        self.vectorX.setMaximum(2147480000.000000000000000)

        self.horizontalLayout.addWidget(self.vectorX)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Position)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.vectorY = QDoubleSpinBox(Position)
        self.vectorY.setObjectName(u"vectorY")
        self.vectorY.setMinimum(-2147480000.000000000000000)
        self.vectorY.setMaximum(2147480000.000000000000000)

        self.horizontalLayout_2.addWidget(self.vectorY)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Position)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.vectorZ = QDoubleSpinBox(Position)
        self.vectorZ.setObjectName(u"vectorZ")
        self.vectorZ.setMinimum(-2147480000.000000000000000)
        self.vectorZ.setMaximum(2147480000.000000000000000)
        self.vectorZ.setValue(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.vectorZ)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.checkBox = QCheckBox(Position)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.comboBoxGridSize = QComboBox(Position)
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.addItem("")
        self.comboBoxGridSize.setObjectName(u"comboBoxGridSize")
        self.comboBoxGridSize.setEditable(True)

        self.verticalLayout.addWidget(self.comboBoxGridSize)


        self.retranslateUi(Position)

        QMetaObject.connectSlotsByName(Position)
    # setupUi

    def retranslateUi(self, Position):
        self.label.setText(QCoreApplication.translate("Position", u"X", None))
        self.label_2.setText(QCoreApplication.translate("Position", u"Y", None))
        self.label_3.setText(QCoreApplication.translate("Position", u"Z", None))
        self.checkBox.setText(QCoreApplication.translate("Position", u"Grid snap in", None))
        self.comboBoxGridSize.setItemText(0, QCoreApplication.translate("Position", u"0.1 mm", None))
        self.comboBoxGridSize.setItemText(1, QCoreApplication.translate("Position", u"0.5 mm", None))
        self.comboBoxGridSize.setItemText(2, QCoreApplication.translate("Position", u"1 mm", None))
        self.comboBoxGridSize.setItemText(3, QCoreApplication.translate("Position", u"2 mm", None))
        self.comboBoxGridSize.setItemText(4, QCoreApplication.translate("Position", u"5 mm", None))
        self.comboBoxGridSize.setItemText(5, QCoreApplication.translate("Position", u"10 mm", None))
        self.comboBoxGridSize.setItemText(6, QCoreApplication.translate("Position", u"20 mm", None))
        self.comboBoxGridSize.setItemText(7, QCoreApplication.translate("Position", u"50 mm", None))
        self.comboBoxGridSize.setItemText(8, QCoreApplication.translate("Position", u"100 mm", None))
        self.comboBoxGridSize.setItemText(9, QCoreApplication.translate("Position", u"200 mm", None))
        self.comboBoxGridSize.setItemText(10, QCoreApplication.translate("Position", u"500 mm", None))
        self.comboBoxGridSize.setItemText(11, QCoreApplication.translate("Position", u"1 m", None))
        self.comboBoxGridSize.setItemText(12, QCoreApplication.translate("Position", u"2 m", None))
        self.comboBoxGridSize.setItemText(13, QCoreApplication.translate("Position", u"5 m", None))

        pass
    # retranslateUi

