# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskRevolutionParameters.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_PartDesignGui_TaskRevolutionParameters(object):
    def setupUi(self, PartDesignGui__TaskRevolutionParameters):
        if not PartDesignGui__TaskRevolutionParameters.objectName():
            PartDesignGui__TaskRevolutionParameters.setObjectName(u"PartDesignGui__TaskRevolutionParameters")
        PartDesignGui__TaskRevolutionParameters.resize(278, 193)
        PartDesignGui__TaskRevolutionParameters.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(PartDesignGui__TaskRevolutionParameters)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayoutMode = QHBoxLayout()
        self.horizontalLayoutMode.setObjectName(u"horizontalLayoutMode")
        self.textLabelMode = QLabel(PartDesignGui__TaskRevolutionParameters)
        self.textLabelMode.setObjectName(u"textLabelMode")

        self.horizontalLayoutMode.addWidget(self.textLabelMode)

        self.changeMode = QComboBox(PartDesignGui__TaskRevolutionParameters)
        self.changeMode.addItem("")
        self.changeMode.setObjectName(u"changeMode")

        self.horizontalLayoutMode.addWidget(self.changeMode)


        self.verticalLayout.addLayout(self.horizontalLayoutMode)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textLabel1 = QLabel(PartDesignGui__TaskRevolutionParameters)
        self.textLabel1.setObjectName(u"textLabel1")

        self.horizontalLayout.addWidget(self.textLabel1)

        self.axis = QComboBox(PartDesignGui__TaskRevolutionParameters)
        self.axis.addItem("")
        self.axis.addItem("")
        self.axis.addItem("")
        self.axis.addItem("")
        self.axis.addItem("")
        self.axis.addItem("")
        self.axis.setObjectName(u"axis")

        self.horizontalLayout.addWidget(self.axis)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelAngle = QLabel(PartDesignGui__TaskRevolutionParameters)
        self.labelAngle.setObjectName(u"labelAngle")

        self.horizontalLayout_3.addWidget(self.labelAngle)

        self.revolveAngle = Gui_QuantitySpinBox(PartDesignGui__TaskRevolutionParameters)
        self.revolveAngle.setObjectName(u"revolveAngle")
        self.revolveAngle.setKeyboardTracking(False)
        self.revolveAngle.setProperty(u"unit", u"deg")
        self.revolveAngle.setMinimum(0.000000000000000)
        self.revolveAngle.setMaximum(360.000000000000000)
        self.revolveAngle.setSingleStep(10.000000000000000)
        self.revolveAngle.setValue(360.000000000000000)

        self.horizontalLayout_3.addWidget(self.revolveAngle)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelAngle2 = QLabel(PartDesignGui__TaskRevolutionParameters)
        self.labelAngle2.setObjectName(u"labelAngle2")

        self.horizontalLayout_4.addWidget(self.labelAngle2)

        self.revolveAngle2 = Gui_QuantitySpinBox(PartDesignGui__TaskRevolutionParameters)
        self.revolveAngle2.setObjectName(u"revolveAngle2")
        self.revolveAngle2.setKeyboardTracking(False)
        self.revolveAngle2.setProperty(u"unit", u"deg")
        self.revolveAngle2.setMinimum(0.000000000000000)
        self.revolveAngle2.setMaximum(360.000000000000000)
        self.revolveAngle2.setSingleStep(10.000000000000000)
        self.revolveAngle2.setValue(60.000000000000000)

        self.horizontalLayout_4.addWidget(self.revolveAngle2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.checkBoxMidplane = QCheckBox(PartDesignGui__TaskRevolutionParameters)
        self.checkBoxMidplane.setObjectName(u"checkBoxMidplane")
        self.checkBoxMidplane.setEnabled(True)

        self.verticalLayout.addWidget(self.checkBoxMidplane)

        self.checkBoxReversed = QCheckBox(PartDesignGui__TaskRevolutionParameters)
        self.checkBoxReversed.setObjectName(u"checkBoxReversed")

        self.verticalLayout.addWidget(self.checkBoxReversed)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.buttonFace = QPushButton(PartDesignGui__TaskRevolutionParameters)
        self.buttonFace.setObjectName(u"buttonFace")
        self.buttonFace.setCheckable(True)

        self.gridLayout_5.addWidget(self.buttonFace, 0, 0, 1, 1)

        self.lineFaceName = QLineEdit(PartDesignGui__TaskRevolutionParameters)
        self.lineFaceName.setObjectName(u"lineFaceName")

        self.gridLayout_5.addWidget(self.lineFaceName, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_5)

        self.line = QFrame(PartDesignGui__TaskRevolutionParameters)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.checkBoxUpdateView = QCheckBox(PartDesignGui__TaskRevolutionParameters)
        self.checkBoxUpdateView.setObjectName(u"checkBoxUpdateView")
        self.checkBoxUpdateView.setChecked(True)

        self.verticalLayout.addWidget(self.checkBoxUpdateView)

        QWidget.setTabOrder(self.axis, self.revolveAngle)
        QWidget.setTabOrder(self.revolveAngle, self.checkBoxMidplane)
        QWidget.setTabOrder(self.checkBoxMidplane, self.checkBoxReversed)
        QWidget.setTabOrder(self.checkBoxReversed, self.checkBoxUpdateView)

        self.retranslateUi(PartDesignGui__TaskRevolutionParameters)

        QMetaObject.connectSlotsByName(PartDesignGui__TaskRevolutionParameters)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskRevolutionParameters):
        self.textLabelMode.setText(QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Type", None))
        self.changeMode.setItemText(0, QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Dimension", None))

        self.textLabel1.setText(QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Axis", None))
        self.axis.setItemText(0, QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Base X-axis", None))
        self.axis.setItemText(1, QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Base Y-axis", None))
        self.axis.setItemText(2, QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Base Z-axis", None))
        self.axis.setItemText(3, QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Horizontal sketch axis", None))
        self.axis.setItemText(4, QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Vertical sketch axis", None))
        self.axis.setItemText(5, QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Select reference\u2026", None))

        self.labelAngle.setText(QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Angle", None))
        self.labelAngle2.setText(QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"2nd angle", None))
        self.checkBoxMidplane.setText(QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Symmetric to plane", None))
        self.checkBoxReversed.setText(QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Reversed", None))
        self.buttonFace.setText(QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Face", None))
        self.checkBoxUpdateView.setText(QCoreApplication.translate("PartDesignGui::TaskRevolutionParameters", u"Recompute on change", None))
        pass
    # retranslateUi

