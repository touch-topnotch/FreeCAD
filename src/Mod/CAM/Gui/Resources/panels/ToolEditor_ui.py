# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ToolEditor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(408, 678)
        Form.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.toolName = QLineEdit(self.groupBox_2)
        self.toolName.setObjectName(u"toolName")
        self.toolName.setMaxLength(50)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.toolName)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.toolType = QComboBox(self.groupBox_2)
        self.toolType.setObjectName(u"toolType")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.toolType)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.toolMaterial = QComboBox(self.groupBox_2)
        self.toolMaterial.setObjectName(u"toolMaterial")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.toolMaterial)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.toolLengthOffset = Gui_InputField(self.groupBox_2)
        self.toolLengthOffset.setObjectName(u"toolLengthOffset")
        self.toolLengthOffset.setText(u"0.00")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.toolLengthOffset)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.paramGeneric = QGroupBox(Form)
        self.paramGeneric.setObjectName(u"paramGeneric")
        self.formLayout_2 = QFormLayout(self.paramGeneric)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_4 = QLabel(self.paramGeneric)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.label_6 = QLabel(self.paramGeneric)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.paramGeneric)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.label_9 = QLabel(self.paramGeneric)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_9)

        self.label_8 = QLabel(self.paramGeneric)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.toolDiameter = Gui_InputField(self.paramGeneric)
        self.toolDiameter.setObjectName(u"toolDiameter")
        self.toolDiameter.setText(u"0.00")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.toolDiameter)

        self.toolFlatRadius = Gui_InputField(self.paramGeneric)
        self.toolFlatRadius.setObjectName(u"toolFlatRadius")
        self.toolFlatRadius.setText(u"0.00")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.toolFlatRadius)

        self.toolCornerRadius = Gui_InputField(self.paramGeneric)
        self.toolCornerRadius.setObjectName(u"toolCornerRadius")
        self.toolCornerRadius.setText(u"0.00")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.toolCornerRadius)

        self.toolCuttingEdgeAngle = Gui_InputField(self.paramGeneric)
        self.toolCuttingEdgeAngle.setObjectName(u"toolCuttingEdgeAngle")
        self.toolCuttingEdgeAngle.setText(u"180\u00b0")
        self.toolCuttingEdgeAngle.setProperty(u"unit", u"\u00b0")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.toolCuttingEdgeAngle)

        self.toolCuttingEdgeHeight = Gui_InputField(self.paramGeneric)
        self.toolCuttingEdgeHeight.setObjectName(u"toolCuttingEdgeHeight")
        self.toolCuttingEdgeHeight.setText(u"0.00")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.toolCuttingEdgeHeight)


        self.verticalLayout.addWidget(self.paramGeneric)

        self.paramImage = QGroupBox(Form)
        self.paramImage.setObjectName(u"paramImage")
        self.horizontalLayout = QHBoxLayout(self.paramImage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.paramImageParam = QWidget(self.paramImage)
        self.paramImageParam.setObjectName(u"paramImageParam")
        self.formLayout_3 = QFormLayout(self.paramImageParam)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_D = QLabel(self.paramImageParam)
        self.label_D.setObjectName(u"label_D")
        self.label_D.setText(u"D =")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_D)

        self.value_D = Gui_InputField(self.paramImageParam)
        self.value_D.setObjectName(u"value_D")
        self.value_D.setText(u"0.00")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.value_D)

        self.label_d = QLabel(self.paramImageParam)
        self.label_d.setObjectName(u"label_d")
        self.label_d.setText(u"d =")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_d)

        self.value_d = Gui_InputField(self.paramImageParam)
        self.value_d.setObjectName(u"value_d")
        self.value_d.setText(u"0.00")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.value_d)

        self.label_H = QLabel(self.paramImageParam)
        self.label_H.setObjectName(u"label_H")
        self.label_H.setText(u"H =")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_H)

        self.value_H = Gui_InputField(self.paramImageParam)
        self.value_H.setObjectName(u"value_H")
        self.value_H.setText(u"0.00")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.value_H)

        self.label_a = QLabel(self.paramImageParam)
        self.label_a.setObjectName(u"label_a")
        self.label_a.setText(u"\u03b1 = ")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_a)

        self.value_a = Gui_InputField(self.paramImageParam)
        self.value_a.setObjectName(u"value_a")
        self.value_a.setText(u"180\u00b0")
        self.value_a.setProperty(u"unit", u"\u00b0")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.value_a)

        self.label_S = QLabel(self.paramImageParam)
        self.label_S.setObjectName(u"label_S")
        self.label_S.setEnabled(False)
        self.label_S.setText(u"S = ")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_S)

        self.value_S = Gui_InputField(self.paramImageParam)
        self.value_S.setObjectName(u"value_S")
        self.value_S.setEnabled(False)
        self.value_S.setText(u"0.00")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.value_S)


        self.horizontalLayout.addWidget(self.paramImageParam)

        self.image = QLabel(self.paramImage)
        self.image.setObjectName(u"image")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMinimumSize(QSize(210, 297))
        self.image.setMaximumSize(QSize(210, 297))
        self.image.setScaledContents(True)
        self.image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.image)


        self.verticalLayout.addWidget(self.paramImage)


        self.retranslateUi(Form)

        self.toolType.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Tool", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.toolName.setPlaceholderText(QCoreApplication.translate("Form", u"Display Name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Type", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Material", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Length Offset", None))
        self.toolLengthOffset.setProperty(u"unit", QCoreApplication.translate("Form", u"mm", None))
        self.paramGeneric.setTitle(QCoreApplication.translate("Form", u"Tool Parameter", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Diameter", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Flat Radius", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Corner Radius", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Point/Tip Angle", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Cutting Edge Height", None))
        self.toolDiameter.setProperty(u"unit", QCoreApplication.translate("Form", u"mm", None))
        self.toolFlatRadius.setProperty(u"unit", QCoreApplication.translate("Form", u"mm", None))
        self.toolCornerRadius.setProperty(u"unit", QCoreApplication.translate("Form", u"mm", None))
        self.toolCuttingEdgeHeight.setProperty(u"unit", QCoreApplication.translate("Form", u"mm", None))
        self.paramImage.setTitle(QCoreApplication.translate("Form", u"Tool Parameter", None))
        self.value_D.setProperty(u"unit", QCoreApplication.translate("Form", u"mm", None))
        self.value_d.setProperty(u"unit", QCoreApplication.translate("Form", u"mm", None))
        self.value_H.setProperty(u"unit", QCoreApplication.translate("Form", u"mm", None))
        self.value_S.setProperty(u"unit", QCoreApplication.translate("Form", u"mm", None))
        self.image.setText(QCoreApplication.translate("Form", u"Image", None))
        pass
    # retranslateUi

