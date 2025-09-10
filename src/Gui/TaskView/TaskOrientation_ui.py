# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskOrientation.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Gui_TaskOrientation(object):
    def setupUi(self, Gui__TaskOrientation):
        if not Gui__TaskOrientation.objectName():
            Gui__TaskOrientation.setObjectName(u"Gui__TaskOrientation")
        Gui__TaskOrientation.resize(194, 200)
        self.gridLayout = QGridLayout(Gui__TaskOrientation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Gui__TaskOrientation)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.XY_radioButton = QRadioButton(self.groupBox)
        self.XY_radioButton.setObjectName(u"XY_radioButton")
        self.XY_radioButton.setChecked(True)

        self.verticalLayout.addWidget(self.XY_radioButton)

        self.XZ_radioButton = QRadioButton(self.groupBox)
        self.XZ_radioButton.setObjectName(u"XZ_radioButton")

        self.verticalLayout.addWidget(self.XZ_radioButton)

        self.YZ_radioButton = QRadioButton(self.groupBox)
        self.YZ_radioButton.setObjectName(u"YZ_radioButton")

        self.verticalLayout.addWidget(self.YZ_radioButton)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.Reverse_checkBox = QCheckBox(Gui__TaskOrientation)
        self.Reverse_checkBox.setObjectName(u"Reverse_checkBox")

        self.gridLayout.addWidget(self.Reverse_checkBox, 1, 0, 1, 2)

        self.previewLabel = QLabel(Gui__TaskOrientation)
        self.previewLabel.setObjectName(u"previewLabel")
        self.previewLabel.setMinimumSize(QSize(48, 48))
        self.previewLabel.setMaximumSize(QSize(48, 48))
        self.previewLabel.setText(u"Preview")

        self.gridLayout.addWidget(self.previewLabel, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Gui__TaskOrientation)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.Offset_doubleSpinBox = Gui_QuantitySpinBox(Gui__TaskOrientation)
        self.Offset_doubleSpinBox.setObjectName(u"Offset_doubleSpinBox")
        self.Offset_doubleSpinBox.setProperty(u"unit", u"mm")
        self.Offset_doubleSpinBox.setProperty(u"minimum", -999999999.000000000000000)
        self.Offset_doubleSpinBox.setProperty(u"maximum", 999999999.000000000000000)
        self.Offset_doubleSpinBox.setProperty(u"singleStep", 1.000000000000000)

        self.horizontalLayout.addWidget(self.Offset_doubleSpinBox)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)


        self.retranslateUi(Gui__TaskOrientation)

        QMetaObject.connectSlotsByName(Gui__TaskOrientation)
    # setupUi

    def retranslateUi(self, Gui__TaskOrientation):
        Gui__TaskOrientation.setWindowTitle(QCoreApplication.translate("Gui::TaskOrientation", u"Choose orientation", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::TaskOrientation", u"Planes", None))
        self.XY_radioButton.setText(QCoreApplication.translate("Gui::TaskOrientation", u"XY-Plane", None))
        self.XZ_radioButton.setText(QCoreApplication.translate("Gui::TaskOrientation", u"XZ-Plane", None))
        self.YZ_radioButton.setText(QCoreApplication.translate("Gui::TaskOrientation", u"YZ-Plane", None))
        self.Reverse_checkBox.setText(QCoreApplication.translate("Gui::TaskOrientation", u"Reverse direction", None))
        self.label.setText(QCoreApplication.translate("Gui::TaskOrientation", u"Offset:", None))
    # retranslateUi

