# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InvoluteGearFeature.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QLabel, QSizePolicy, QSpinBox, QWidget)

class Ui_InvoluteGearParameter(object):
    def setupUi(self, InvoluteGearParameter):
        if not InvoluteGearParameter.objectName():
            InvoluteGearParameter.setObjectName(u"InvoluteGearParameter")
        InvoluteGearParameter.resize(253, 301)
        self.formLayout = QFormLayout(InvoluteGearParameter)
        self.formLayout.setObjectName(u"formLayout")
        self.label_NumberOfTeeth = QLabel(InvoluteGearParameter)
        self.label_NumberOfTeeth.setObjectName(u"label_NumberOfTeeth")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_NumberOfTeeth)

        self.spinBox_NumberOfTeeth = QSpinBox(InvoluteGearParameter)
        self.spinBox_NumberOfTeeth.setObjectName(u"spinBox_NumberOfTeeth")
        self.spinBox_NumberOfTeeth.setMinimum(3)
        self.spinBox_NumberOfTeeth.setMaximum(9999)
        self.spinBox_NumberOfTeeth.setValue(26)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBox_NumberOfTeeth)

        self.label_Modules = QLabel(InvoluteGearParameter)
        self.label_Modules.setObjectName(u"label_Modules")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_Modules)

        self.Quantity_Modules = Gui_InputField(InvoluteGearParameter)
        self.Quantity_Modules.setObjectName(u"Quantity_Modules")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Quantity_Modules.sizePolicy().hasHeightForWidth())
        self.Quantity_Modules.setSizePolicy(sizePolicy)
        self.Quantity_Modules.setMinimumSize(QSize(80, 20))
        self.Quantity_Modules.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Quantity_Modules.setProperty(u"unit", u"mm")
        self.Quantity_Modules.setProperty(u"decimals", 3)
        self.Quantity_Modules.setProperty(u"maximum", 2000.000000000000000)
        self.Quantity_Modules.setProperty(u"singleStep", 2.000000000000000)
        self.Quantity_Modules.setProperty(u"value", 2.500000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Quantity_Modules)

        self.label_PressureAngle = QLabel(InvoluteGearParameter)
        self.label_PressureAngle.setObjectName(u"label_PressureAngle")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_PressureAngle)

        self.Quantity_PressureAngle = Gui_InputField(InvoluteGearParameter)
        self.Quantity_PressureAngle.setObjectName(u"Quantity_PressureAngle")
        sizePolicy.setHeightForWidth(self.Quantity_PressureAngle.sizePolicy().hasHeightForWidth())
        self.Quantity_PressureAngle.setSizePolicy(sizePolicy)
        self.Quantity_PressureAngle.setMinimumSize(QSize(80, 20))
        self.Quantity_PressureAngle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Quantity_PressureAngle.setProperty(u"unit", u"deg")
        self.Quantity_PressureAngle.setProperty(u"decimals", 3)
        self.Quantity_PressureAngle.setProperty(u"maximum", 90.000000000000000)
        self.Quantity_PressureAngle.setProperty(u"singleStep", 2.000000000000000)
        self.Quantity_PressureAngle.setProperty(u"value", 20.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Quantity_PressureAngle)

        self.label_HighPrecision = QLabel(InvoluteGearParameter)
        self.label_HighPrecision.setObjectName(u"label_HighPrecision")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_HighPrecision)

        self.comboBox_HighPrecision = QComboBox(InvoluteGearParameter)
        self.comboBox_HighPrecision.addItem("")
        self.comboBox_HighPrecision.addItem("")
        self.comboBox_HighPrecision.setObjectName(u"comboBox_HighPrecision")
        self.comboBox_HighPrecision.setEnabled(True)
        self.comboBox_HighPrecision.setEditable(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox_HighPrecision)

        self.label_ExternalGear = QLabel(InvoluteGearParameter)
        self.label_ExternalGear.setObjectName(u"label_ExternalGear")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_ExternalGear)

        self.comboBox_ExternalGear = QComboBox(InvoluteGearParameter)
        self.comboBox_ExternalGear.addItem("")
        self.comboBox_ExternalGear.addItem("")
        self.comboBox_ExternalGear.setObjectName(u"comboBox_ExternalGear")
        self.comboBox_ExternalGear.setEnabled(True)
        self.comboBox_ExternalGear.setEditable(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBox_ExternalGear)

        self.label_Addendum = QLabel(InvoluteGearParameter)
        self.label_Addendum.setObjectName(u"label_Addendum")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_Addendum)

        self.doubleSpinBox_Addendum = QDoubleSpinBox(InvoluteGearParameter)
        self.doubleSpinBox_Addendum.setObjectName(u"doubleSpinBox_Addendum")
        self.doubleSpinBox_Addendum.setMaximum(5.000000000000000)
        self.doubleSpinBox_Addendum.setSingleStep(0.050000000000000)
        self.doubleSpinBox_Addendum.setValue(1.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.doubleSpinBox_Addendum)

        self.label_Dedendum = QLabel(InvoluteGearParameter)
        self.label_Dedendum.setObjectName(u"label_Dedendum")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_Dedendum)

        self.doubleSpinBox_Dedendum = QDoubleSpinBox(InvoluteGearParameter)
        self.doubleSpinBox_Dedendum.setObjectName(u"doubleSpinBox_Dedendum")
        self.doubleSpinBox_Dedendum.setMaximum(5.000000000000000)
        self.doubleSpinBox_Dedendum.setSingleStep(0.050000000000000)
        self.doubleSpinBox_Dedendum.setValue(1.250000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.doubleSpinBox_Dedendum)

        self.label_RootFillet = QLabel(InvoluteGearParameter)
        self.label_RootFillet.setObjectName(u"label_RootFillet")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_RootFillet)

        self.doubleSpinBox_RootFillet = QDoubleSpinBox(InvoluteGearParameter)
        self.doubleSpinBox_RootFillet.setObjectName(u"doubleSpinBox_RootFillet")
        self.doubleSpinBox_RootFillet.setMaximum(2.000000000000000)
        self.doubleSpinBox_RootFillet.setSingleStep(0.020000000000000)
        self.doubleSpinBox_RootFillet.setValue(0.380000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.doubleSpinBox_RootFillet)

        self.label_ProfileShift = QLabel(InvoluteGearParameter)
        self.label_ProfileShift.setObjectName(u"label_ProfileShift")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_ProfileShift)

        self.doubleSpinBox_ProfileShift = QDoubleSpinBox(InvoluteGearParameter)
        self.doubleSpinBox_ProfileShift.setObjectName(u"doubleSpinBox_ProfileShift")
        self.doubleSpinBox_ProfileShift.setMinimum(-3.000000000000000)
        self.doubleSpinBox_ProfileShift.setMaximum(3.000000000000000)
        self.doubleSpinBox_ProfileShift.setSingleStep(0.100000000000000)
        self.doubleSpinBox_ProfileShift.setValue(0.000000000000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.doubleSpinBox_ProfileShift)


        self.retranslateUi(InvoluteGearParameter)

        QMetaObject.connectSlotsByName(InvoluteGearParameter)
    # setupUi

    def retranslateUi(self, InvoluteGearParameter):
        InvoluteGearParameter.setWindowTitle(QCoreApplication.translate("InvoluteGearParameter", u"Involute Parameter", None))
        self.label_NumberOfTeeth.setText(QCoreApplication.translate("InvoluteGearParameter", u"Number of teeth", None))
        self.label_Modules.setText(QCoreApplication.translate("InvoluteGearParameter", u"Module", None))
        self.Quantity_Modules.setText("")
        self.label_PressureAngle.setText(QCoreApplication.translate("InvoluteGearParameter", u"Pressure angle", None))
        self.label_HighPrecision.setText(QCoreApplication.translate("InvoluteGearParameter", u"High precision", None))
        self.comboBox_HighPrecision.setItemText(0, QCoreApplication.translate("InvoluteGearParameter", u"True", None))
        self.comboBox_HighPrecision.setItemText(1, QCoreApplication.translate("InvoluteGearParameter", u"False", None))

        self.label_ExternalGear.setText(QCoreApplication.translate("InvoluteGearParameter", u"External gear", None))
        self.comboBox_ExternalGear.setItemText(0, QCoreApplication.translate("InvoluteGearParameter", u"True", None))
        self.comboBox_ExternalGear.setItemText(1, QCoreApplication.translate("InvoluteGearParameter", u"False", None))

        self.label_Addendum.setText(QCoreApplication.translate("InvoluteGearParameter", u"Addendum coefficient", None))
        self.label_Dedendum.setText(QCoreApplication.translate("InvoluteGearParameter", u"Dedendum coefficient", None))
        self.label_RootFillet.setText(QCoreApplication.translate("InvoluteGearParameter", u"Root fillet coefficient", None))
        self.label_ProfileShift.setText(QCoreApplication.translate("InvoluteGearParameter", u"Profile shift coefficient", None))
    # retranslateUi

