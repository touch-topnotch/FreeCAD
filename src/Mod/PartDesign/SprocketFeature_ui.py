# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SprocketFeature.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QSizePolicy, QSpinBox, QWidget)

class Ui_SprocketParameter(object):
    def setupUi(self, SprocketParameter):
        if not SprocketParameter.objectName():
            SprocketParameter.setObjectName(u"SprocketParameter")
        SprocketParameter.resize(344, 160)
        self.gridLayout = QGridLayout(SprocketParameter)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(SprocketParameter)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.spinBox_NumberOfTeeth = QSpinBox(SprocketParameter)
        self.spinBox_NumberOfTeeth.setObjectName(u"spinBox_NumberOfTeeth")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spinBox_NumberOfTeeth.sizePolicy().hasHeightForWidth())
        self.spinBox_NumberOfTeeth.setSizePolicy(sizePolicy1)
        self.spinBox_NumberOfTeeth.setMinimum(3)
        self.spinBox_NumberOfTeeth.setMaximum(9999)
        self.spinBox_NumberOfTeeth.setValue(50)

        self.gridLayout.addWidget(self.spinBox_NumberOfTeeth, 0, 1, 1, 1)

        self.label_10 = QLabel(SprocketParameter)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.comboBox_SprocketReference = QComboBox(SprocketParameter)
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.addItem("")
        self.comboBox_SprocketReference.setObjectName(u"comboBox_SprocketReference")
        sizePolicy1.setHeightForWidth(self.comboBox_SprocketReference.sizePolicy().hasHeightForWidth())
        self.comboBox_SprocketReference.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBox_SprocketReference, 1, 1, 1, 1)

        self.label_8 = QLabel(SprocketParameter)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.Quantity_Pitch = Gui_InputField(SprocketParameter)
        self.Quantity_Pitch.setObjectName(u"Quantity_Pitch")
        sizePolicy1.setHeightForWidth(self.Quantity_Pitch.sizePolicy().hasHeightForWidth())
        self.Quantity_Pitch.setSizePolicy(sizePolicy1)
        self.Quantity_Pitch.setMinimumSize(QSize(80, 20))
        self.Quantity_Pitch.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Quantity_Pitch.setSingleStep(0.001000000000000)
        self.Quantity_Pitch.setMaximum(2000.000000000000000)
        self.Quantity_Pitch.setMinimum(0.010000000000000)
        self.Quantity_Pitch.setProperty(u"unit", u"in")
        self.Quantity_Pitch.setProperty(u"decimals", 3)
        self.Quantity_Pitch.setProperty(u"value", 0.375000000000000)

        self.gridLayout.addWidget(self.Quantity_Pitch, 2, 1, 1, 1)

        self.label_6 = QLabel(SprocketParameter)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.Quantity_RollerDiameter = Gui_InputField(SprocketParameter)
        self.Quantity_RollerDiameter.setObjectName(u"Quantity_RollerDiameter")
        sizePolicy1.setHeightForWidth(self.Quantity_RollerDiameter.sizePolicy().hasHeightForWidth())
        self.Quantity_RollerDiameter.setSizePolicy(sizePolicy1)
        self.Quantity_RollerDiameter.setMinimumSize(QSize(80, 20))
        self.Quantity_RollerDiameter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Quantity_RollerDiameter.setSingleStep(0.010000000000000)
        self.Quantity_RollerDiameter.setMaximum(50.000000000000000)
        self.Quantity_RollerDiameter.setMinimum(0.010000000000000)
        self.Quantity_RollerDiameter.setProperty(u"unit", u"in")
        self.Quantity_RollerDiameter.setProperty(u"decimals", 3)
        self.Quantity_RollerDiameter.setProperty(u"value", 0.200000000000000)

        self.gridLayout.addWidget(self.Quantity_RollerDiameter, 3, 1, 1, 1)

        self.label_7 = QLabel(SprocketParameter)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.Quantity_Thickness = Gui_InputField(SprocketParameter)
        self.Quantity_Thickness.setObjectName(u"Quantity_Thickness")
        sizePolicy1.setHeightForWidth(self.Quantity_Thickness.sizePolicy().hasHeightForWidth())
        self.Quantity_Thickness.setSizePolicy(sizePolicy1)
        self.Quantity_Thickness.setMinimumSize(QSize(80, 20))
        self.Quantity_Thickness.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Quantity_Thickness.setSingleStep(0.010000000000000)
        self.Quantity_Thickness.setMaximum(50.000000000000000)
        self.Quantity_Thickness.setMinimum(0.010000000000000)
        self.Quantity_Thickness.setProperty(u"unit", u"in")
        self.Quantity_Thickness.setProperty(u"decimals", 3)
        self.Quantity_Thickness.setProperty(u"value", 0.200000000000000)

        self.gridLayout.addWidget(self.Quantity_Thickness, 4, 1, 1, 1)


        self.retranslateUi(SprocketParameter)

        QMetaObject.connectSlotsByName(SprocketParameter)
    # setupUi

    def retranslateUi(self, SprocketParameter):
        SprocketParameter.setWindowTitle(QCoreApplication.translate("SprocketParameter", u"Sprocket Parameters", None))
        self.label_9.setText(QCoreApplication.translate("SprocketParameter", u"Number of teeth", None))
        self.label_10.setText(QCoreApplication.translate("SprocketParameter", u"Sprocket reference", None))
        self.comboBox_SprocketReference.setItemText(0, QCoreApplication.translate("SprocketParameter", u"ANSI 25", None))
        self.comboBox_SprocketReference.setItemText(1, QCoreApplication.translate("SprocketParameter", u"ANSI 35", None))
        self.comboBox_SprocketReference.setItemText(2, QCoreApplication.translate("SprocketParameter", u"ANSI 41", None))
        self.comboBox_SprocketReference.setItemText(3, QCoreApplication.translate("SprocketParameter", u"ANSI 40", None))
        self.comboBox_SprocketReference.setItemText(4, QCoreApplication.translate("SprocketParameter", u"ANSI 50", None))
        self.comboBox_SprocketReference.setItemText(5, QCoreApplication.translate("SprocketParameter", u"ANSI 60", None))
        self.comboBox_SprocketReference.setItemText(6, QCoreApplication.translate("SprocketParameter", u"ANSI 80", None))
        self.comboBox_SprocketReference.setItemText(7, QCoreApplication.translate("SprocketParameter", u"ANSI 100", None))
        self.comboBox_SprocketReference.setItemText(8, QCoreApplication.translate("SprocketParameter", u"ANSI 120", None))
        self.comboBox_SprocketReference.setItemText(9, QCoreApplication.translate("SprocketParameter", u"ANSI 140", None))
        self.comboBox_SprocketReference.setItemText(10, QCoreApplication.translate("SprocketParameter", u"ANSI 160", None))
        self.comboBox_SprocketReference.setItemText(11, QCoreApplication.translate("SprocketParameter", u"ANSI 180", None))
        self.comboBox_SprocketReference.setItemText(12, QCoreApplication.translate("SprocketParameter", u"ANSI 200", None))
        self.comboBox_SprocketReference.setItemText(13, QCoreApplication.translate("SprocketParameter", u"ANSI 240", None))
        self.comboBox_SprocketReference.setItemText(14, QCoreApplication.translate("SprocketParameter", u"Bicycle with derailleur", None))
        self.comboBox_SprocketReference.setItemText(15, QCoreApplication.translate("SprocketParameter", u"Bicycle without derailleur", None))
        self.comboBox_SprocketReference.setItemText(16, QCoreApplication.translate("SprocketParameter", u"ISO 606 06B", None))
        self.comboBox_SprocketReference.setItemText(17, QCoreApplication.translate("SprocketParameter", u"ISO 606 08B", None))
        self.comboBox_SprocketReference.setItemText(18, QCoreApplication.translate("SprocketParameter", u"ISO 606 10B", None))
        self.comboBox_SprocketReference.setItemText(19, QCoreApplication.translate("SprocketParameter", u"ISO 606 12B", None))
        self.comboBox_SprocketReference.setItemText(20, QCoreApplication.translate("SprocketParameter", u"ISO 606 16B", None))
        self.comboBox_SprocketReference.setItemText(21, QCoreApplication.translate("SprocketParameter", u"ISO 606 20B", None))
        self.comboBox_SprocketReference.setItemText(22, QCoreApplication.translate("SprocketParameter", u"ISO 606 24B", None))
        self.comboBox_SprocketReference.setItemText(23, QCoreApplication.translate("SprocketParameter", u"Motorcycle 420", None))
        self.comboBox_SprocketReference.setItemText(24, QCoreApplication.translate("SprocketParameter", u"Motorcycle 425", None))
        self.comboBox_SprocketReference.setItemText(25, QCoreApplication.translate("SprocketParameter", u"Motorcycle 428", None))
        self.comboBox_SprocketReference.setItemText(26, QCoreApplication.translate("SprocketParameter", u"Motorcycle 520", None))
        self.comboBox_SprocketReference.setItemText(27, QCoreApplication.translate("SprocketParameter", u"Motorcycle 525", None))
        self.comboBox_SprocketReference.setItemText(28, QCoreApplication.translate("SprocketParameter", u"Motorcycle 530", None))
        self.comboBox_SprocketReference.setItemText(29, QCoreApplication.translate("SprocketParameter", u"Motorcycle 630", None))

        self.label_8.setText(QCoreApplication.translate("SprocketParameter", u"Chain pitch", None))
        self.Quantity_Pitch.setText(QCoreApplication.translate("SprocketParameter", u"0 in", None))
        self.label_6.setText(QCoreApplication.translate("SprocketParameter", u"Chain roller diameter", None))
        self.label_7.setText(QCoreApplication.translate("SprocketParameter", u"Tooth width", None))
    # retranslateUi

