# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpHelixEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QLabel, QSizePolicy, QSpacerItem,
    QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 365)
        Form.setWindowTitle(u"Form")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.toolController = QComboBox(self.frame)
        self.toolController.setObjectName(u"toolController")

        self.gridLayout.addWidget(self.toolController, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.coolantController = QComboBox(self.frame)
        self.coolantController.setObjectName(u"coolantController")

        self.gridLayout.addWidget(self.coolantController, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.startSide = QComboBox(self.widget)
        self.startSide.addItem("")
        self.startSide.addItem("")
        self.startSide.setObjectName(u"startSide")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.startSide)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.cutMode = QComboBox(self.widget)
        self.cutMode.addItem("")
        self.cutMode.addItem("")
        self.cutMode.setObjectName(u"cutMode")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cutMode)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.stepOverPercent = QSpinBox(self.widget)
        self.stepOverPercent.setObjectName(u"stepOverPercent")
        self.stepOverPercent.setMinimum(1)
        self.stepOverPercent.setMaximum(100)
        self.stepOverPercent.setSingleStep(10)
        self.stepOverPercent.setValue(100)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.stepOverPercent)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.extraOffset = Gui_InputField(self.widget)
        self.extraOffset.setObjectName(u"extraOffset")
        self.extraOffset.setProperty(u"unit", u"")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.extraOffset)


        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.label.setText(QCoreApplication.translate("Form", u"Tool Controller", None))
#if QT_CONFIG(tooltip)
        self.toolController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"Coolant", None))
#if QT_CONFIG(tooltip)
        self.coolantController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Start from", None))
        self.startSide.setItemText(0, QCoreApplication.translate("Form", u"Inside", None))
        self.startSide.setItemText(1, QCoreApplication.translate("Form", u"Outside", None))

#if QT_CONFIG(tooltip)
        self.startSide.setToolTip(QCoreApplication.translate("Form", u"Specify if the helix operation should start at the inside and work its way outwards, or start at the outside and work its way to the center.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Direction", None))
        self.cutMode.setItemText(0, QCoreApplication.translate("Form", u"Climb", None))
        self.cutMode.setItemText(1, QCoreApplication.translate("Form", u"Conventional", None))

#if QT_CONFIG(tooltip)
        self.cutMode.setToolTip(QCoreApplication.translate("Form", u"The direction for the helix, clockwise or counterclockwise.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"Step over percent", None))
#if QT_CONFIG(tooltip)
        self.stepOverPercent.setToolTip(QCoreApplication.translate("Form", u"Specify the percent of the tool diameter each helix will be offset to the previous one. A step over of 100% means no overlap of the individual cuts.", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Form", u"Extra Offset", None))
        pass
    # retranslateUi

