# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskHelixParameters.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_PartDesignGui_TaskHelixParameters(object):
    def setupUi(self, PartDesignGui__TaskHelixParameters):
        if not PartDesignGui__TaskHelixParameters.objectName():
            PartDesignGui__TaskHelixParameters.setObjectName(u"PartDesignGui__TaskHelixParameters")
        PartDesignGui__TaskHelixParameters.resize(278, 398)
        PartDesignGui__TaskHelixParameters.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(PartDesignGui__TaskHelixParameters)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayoutStatus = QHBoxLayout()
        self.horizontalLayoutStatus.setObjectName(u"horizontalLayoutStatus")
        self.labelStatus = QLabel(PartDesignGui__TaskHelixParameters)
        self.labelStatus.setObjectName(u"labelStatus")

        self.horizontalLayoutStatus.addWidget(self.labelStatus)

        self.labelMessage = QLabel(PartDesignGui__TaskHelixParameters)
        self.labelMessage.setObjectName(u"labelMessage")

        self.horizontalLayoutStatus.addWidget(self.labelMessage)


        self.verticalLayout.addLayout(self.horizontalLayoutStatus)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelAxis = QLabel(PartDesignGui__TaskHelixParameters)
        self.labelAxis.setObjectName(u"labelAxis")

        self.horizontalLayout.addWidget(self.labelAxis)

        self.axis = QComboBox(PartDesignGui__TaskHelixParameters)
        self.axis.addItem("")
        self.axis.addItem("")
        self.axis.addItem("")
        self.axis.addItem("")
        self.axis.addItem("")
        self.axis.addItem("")
        self.axis.addItem("")
        self.axis.setObjectName(u"axis")

        self.horizontalLayout.addWidget(self.axis)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayoutMode = QHBoxLayout()
        self.horizontalLayoutMode.setObjectName(u"horizontalLayoutMode")
        self.labelInputMode = QLabel(PartDesignGui__TaskHelixParameters)
        self.labelInputMode.setObjectName(u"labelInputMode")

        self.horizontalLayoutMode.addWidget(self.labelInputMode)

        self.inputMode = QComboBox(PartDesignGui__TaskHelixParameters)
        self.inputMode.addItem("")
        self.inputMode.addItem("")
        self.inputMode.addItem("")
        self.inputMode.addItem("")
        self.inputMode.setObjectName(u"inputMode")

        self.horizontalLayoutMode.addWidget(self.inputMode)


        self.verticalLayout.addLayout(self.horizontalLayoutMode)

        self.horizontalLayoutPitch = QHBoxLayout()
        self.horizontalLayoutPitch.setObjectName(u"horizontalLayoutPitch")
        self.labelPitch = QLabel(PartDesignGui__TaskHelixParameters)
        self.labelPitch.setObjectName(u"labelPitch")

        self.horizontalLayoutPitch.addWidget(self.labelPitch)

        self.pitch = Gui_QuantitySpinBox(PartDesignGui__TaskHelixParameters)
        self.pitch.setObjectName(u"pitch")
        self.pitch.setKeyboardTracking(False)
        self.pitch.setProperty(u"unit", u"mm")
        self.pitch.setMinimum(0.000000000000000)
        self.pitch.setValue(10.000000000000000)

        self.horizontalLayoutPitch.addWidget(self.pitch)


        self.verticalLayout.addLayout(self.horizontalLayoutPitch)

        self.horizontalLayoutHeight = QHBoxLayout()
        self.horizontalLayoutHeight.setObjectName(u"horizontalLayoutHeight")
        self.labelHeight = QLabel(PartDesignGui__TaskHelixParameters)
        self.labelHeight.setObjectName(u"labelHeight")

        self.horizontalLayoutHeight.addWidget(self.labelHeight)

        self.height = Gui_QuantitySpinBox(PartDesignGui__TaskHelixParameters)
        self.height.setObjectName(u"height")
        self.height.setKeyboardTracking(False)
        self.height.setProperty(u"unit", u"mm")
        self.height.setMinimum(0.000000000000000)
        self.height.setValue(30.000000000000000)

        self.horizontalLayoutHeight.addWidget(self.height)


        self.verticalLayout.addLayout(self.horizontalLayoutHeight)

        self.horizontalLayoutTurns = QHBoxLayout()
        self.horizontalLayoutTurns.setObjectName(u"horizontalLayoutTurns")
        self.labelTurns = QLabel(PartDesignGui__TaskHelixParameters)
        self.labelTurns.setObjectName(u"labelTurns")

        self.horizontalLayoutTurns.addWidget(self.labelTurns)

        self.turns = Gui_QuantitySpinBox(PartDesignGui__TaskHelixParameters)
        self.turns.setObjectName(u"turns")
        self.turns.setKeyboardTracking(False)
        self.turns.setMinimum(0.000000000000000)
        self.turns.setValue(3.000000000000000)

        self.horizontalLayoutTurns.addWidget(self.turns)


        self.verticalLayout.addLayout(self.horizontalLayoutTurns)

        self.horizontalLayoutConeAngle = QHBoxLayout()
        self.horizontalLayoutConeAngle.setObjectName(u"horizontalLayoutConeAngle")
        self.labelConeAngle = QLabel(PartDesignGui__TaskHelixParameters)
        self.labelConeAngle.setObjectName(u"labelConeAngle")

        self.horizontalLayoutConeAngle.addWidget(self.labelConeAngle)

        self.coneAngle = Gui_QuantitySpinBox(PartDesignGui__TaskHelixParameters)
        self.coneAngle.setObjectName(u"coneAngle")
        self.coneAngle.setKeyboardTracking(False)
        self.coneAngle.setProperty(u"unit", u"deg")
        self.coneAngle.setMinimum(-89.000000000000000)
        self.coneAngle.setMaximum(89.000000000000000)
        self.coneAngle.setSingleStep(1.000000000000000)

        self.horizontalLayoutConeAngle.addWidget(self.coneAngle)


        self.verticalLayout.addLayout(self.horizontalLayoutConeAngle)

        self.horizontalLayoutGrowth = QHBoxLayout()
        self.horizontalLayoutGrowth.setObjectName(u"horizontalLayoutGrowth")
        self.labelGrowth = QLabel(PartDesignGui__TaskHelixParameters)
        self.labelGrowth.setObjectName(u"labelGrowth")

        self.horizontalLayoutGrowth.addWidget(self.labelGrowth)

        self.growth = Gui_QuantitySpinBox(PartDesignGui__TaskHelixParameters)
        self.growth.setObjectName(u"growth")
        self.growth.setKeyboardTracking(False)
        self.growth.setProperty(u"unit", u"mm")

        self.horizontalLayoutGrowth.addWidget(self.growth)


        self.verticalLayout.addLayout(self.horizontalLayoutGrowth)

        self.checkBoxLeftHanded = QCheckBox(PartDesignGui__TaskHelixParameters)
        self.checkBoxLeftHanded.setObjectName(u"checkBoxLeftHanded")
        self.checkBoxLeftHanded.setEnabled(True)

        self.verticalLayout.addWidget(self.checkBoxLeftHanded)

        self.checkBoxReversed = QCheckBox(PartDesignGui__TaskHelixParameters)
        self.checkBoxReversed.setObjectName(u"checkBoxReversed")
        self.checkBoxReversed.setEnabled(True)

        self.verticalLayout.addWidget(self.checkBoxReversed)

        self.checkBoxOutside = QCheckBox(PartDesignGui__TaskHelixParameters)
        self.checkBoxOutside.setObjectName(u"checkBoxOutside")
        self.checkBoxOutside.setChecked(False)

        self.verticalLayout.addWidget(self.checkBoxOutside)

        self.line = QFrame(PartDesignGui__TaskHelixParameters)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.checkBoxUpdateView = QCheckBox(PartDesignGui__TaskHelixParameters)
        self.checkBoxUpdateView.setObjectName(u"checkBoxUpdateView")
        self.checkBoxUpdateView.setChecked(True)

        self.verticalLayout.addWidget(self.checkBoxUpdateView)

        QWidget.setTabOrder(self.axis, self.inputMode)
        QWidget.setTabOrder(self.inputMode, self.pitch)
        QWidget.setTabOrder(self.pitch, self.height)
        QWidget.setTabOrder(self.height, self.turns)
        QWidget.setTabOrder(self.turns, self.coneAngle)
        QWidget.setTabOrder(self.coneAngle, self.growth)
        QWidget.setTabOrder(self.growth, self.checkBoxLeftHanded)
        QWidget.setTabOrder(self.checkBoxLeftHanded, self.checkBoxReversed)
        QWidget.setTabOrder(self.checkBoxReversed, self.checkBoxOutside)
        QWidget.setTabOrder(self.checkBoxOutside, self.checkBoxUpdateView)

        self.retranslateUi(PartDesignGui__TaskHelixParameters)

        QMetaObject.connectSlotsByName(PartDesignGui__TaskHelixParameters)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskHelixParameters):
        self.labelStatus.setText(QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Status", None))
        self.labelMessage.setText(QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Valid", None))
        self.labelAxis.setText(QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Axis", None))
        self.axis.setItemText(0, QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Base X-axis", None))
        self.axis.setItemText(1, QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Base Y-axis", None))
        self.axis.setItemText(2, QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Base Z-axis", None))
        self.axis.setItemText(3, QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Horizontal sketch axis", None))
        self.axis.setItemText(4, QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Vertical sketch axis", None))
        self.axis.setItemText(5, QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Normal sketch axis", None))
        self.axis.setItemText(6, QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Select reference\u2026", None))

        self.labelInputMode.setText(QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Mode", None))
        self.inputMode.setItemText(0, QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Pitch-Height-Angle", None))
        self.inputMode.setItemText(1, QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Pitch-Turns-Angle", None))
        self.inputMode.setItemText(2, QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Height-Turns-Angle", None))
        self.inputMode.setItemText(3, QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Height-Turns-Growth", None))

        self.labelPitch.setText(QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Pitch", None))
        self.labelHeight.setText(QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Height", None))
        self.labelTurns.setText(QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Turns", None))
        self.labelConeAngle.setText(QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Cone angle", None))
        self.labelGrowth.setText(QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Radial growth", None))
        self.checkBoxLeftHanded.setText(QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Left handed", None))
        self.checkBoxReversed.setText(QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Reversed", None))
        self.checkBoxOutside.setText(QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Remove outside of profile", None))
        self.checkBoxUpdateView.setText(QCoreApplication.translate("PartDesignGui::TaskHelixParameters", u"Recompute on change", None))
        pass
    # retranslateUi

