# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ToolControllerEdit.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Frame(object):
    def setupUi(self, toolControllerEditor):
        if not toolControllerEditor.objectName():
            toolControllerEditor.setObjectName(u"toolControllerEditor")
        toolControllerEditor.resize(561, 739)
        toolControllerEditor.setFrameShape(QFrame.NoFrame)
        toolControllerEditor.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(toolControllerEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tcOperationCountLabel = QLabel(toolControllerEditor)
        self.tcOperationCountLabel.setObjectName(u"tcOperationCountLabel")

        self.verticalLayout.addWidget(self.tcOperationCountLabel)

        self.groupBox_4 = QGroupBox(toolControllerEditor)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tcName = QLineEdit(self.groupBox_4)
        self.tcName.setObjectName(u"tcName")
        self.tcName.setReadOnly(False)

        self.horizontalLayout.addWidget(self.tcName)

        self.tcNumber = QSpinBox(self.groupBox_4)
        self.tcNumber.setObjectName(u"tcNumber")
        self.tcNumber.setFocusPolicy(Qt.StrongFocus)
        self.tcNumber.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.tcNumber.setMaximum(99999)

        self.horizontalLayout.addWidget(self.tcNumber)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.frame = QFrame(toolControllerEditor)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizFeed = Gui_QuantitySpinBox(self.frame)
        self.horizFeed.setObjectName(u"horizFeed")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizFeed.sizePolicy().hasHeightForWidth())
        self.horizFeed.setSizePolicy(sizePolicy)
        self.horizFeed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.horizFeed.setMinimum(0.000000000000000)
        self.horizFeed.setMaximum(9999999.000000000000000)
        self.horizFeed.setProperty(u"unit", u"mm/s")

        self.gridLayout.addWidget(self.horizFeed, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.vertFeed = Gui_QuantitySpinBox(self.frame)
        self.vertFeed.setObjectName(u"vertFeed")
        sizePolicy.setHeightForWidth(self.vertFeed.sizePolicy().hasHeightForWidth())
        self.vertFeed.setSizePolicy(sizePolicy)
        self.vertFeed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.vertFeed.setMinimum(0.000000000000000)
        self.vertFeed.setMaximum(9999999.000000000000000)
        self.vertFeed.setProperty(u"unit", u"mm/s")

        self.gridLayout.addWidget(self.vertFeed, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.horizRapid = Gui_QuantitySpinBox(self.frame)
        self.horizRapid.setObjectName(u"horizRapid")
        sizePolicy.setHeightForWidth(self.horizRapid.sizePolicy().hasHeightForWidth())
        self.horizRapid.setSizePolicy(sizePolicy)
        self.horizRapid.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.horizRapid.setMinimum(0.000000000000000)
        self.horizRapid.setMaximum(9999999.000000000000000)
        self.horizRapid.setProperty(u"unit", u"mm/s")

        self.gridLayout.addWidget(self.horizRapid, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.vertRapid = Gui_QuantitySpinBox(self.frame)
        self.vertRapid.setObjectName(u"vertRapid")
        sizePolicy.setHeightForWidth(self.vertRapid.sizePolicy().hasHeightForWidth())
        self.vertRapid.setSizePolicy(sizePolicy)
        self.vertRapid.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.vertRapid.setMinimum(0.000000000000000)
        self.vertRapid.setMaximum(9999999.000000000000000)
        self.vertRapid.setProperty(u"unit", u"mm/s")

        self.gridLayout.addWidget(self.vertRapid, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.groupBox_3 = QGroupBox(toolControllerEditor)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_2 = QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.spindleDirection = QComboBox(self.groupBox_3)
        self.spindleDirection.addItem("")
        self.spindleDirection.addItem("")
        self.spindleDirection.setObjectName(u"spindleDirection")
        self.spindleDirection.setFocusPolicy(Qt.StrongFocus)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spindleDirection)

        self.spindleSpeed = QDoubleSpinBox(self.groupBox_3)
        self.spindleSpeed.setObjectName(u"spindleSpeed")
        self.spindleSpeed.setMinimum(0.000000000000000)
        self.spindleSpeed.setMaximum(100000.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.spindleSpeed)


        self.verticalLayout.addWidget(self.groupBox_3)

        QWidget.setTabOrder(self.tcName, self.tcNumber)
        QWidget.setTabOrder(self.tcNumber, self.horizFeed)
        QWidget.setTabOrder(self.horizFeed, self.vertFeed)
        QWidget.setTabOrder(self.vertFeed, self.horizRapid)
        QWidget.setTabOrder(self.horizRapid, self.vertRapid)
        QWidget.setTabOrder(self.vertRapid, self.spindleSpeed)
        QWidget.setTabOrder(self.spindleSpeed, self.spindleDirection)

        self.retranslateUi(toolControllerEditor)

        QMetaObject.connectSlotsByName(toolControllerEditor)
    # setupUi

    def retranslateUi(self, toolControllerEditor):
        self.groupBox_4.setTitle(QCoreApplication.translate("Frame", u"Controller Name / Tool Number", None))
        self.label.setText(QCoreApplication.translate("Frame", u"Horizontal feed", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"Vertical feed", None))
        self.label_5.setText(QCoreApplication.translate("Frame", u"Horizontal rapid", None))
        self.label_4.setText(QCoreApplication.translate("Frame", u"Vertical rapid", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Frame", u"Spindle", None))
        self.spindleDirection.setItemText(0, QCoreApplication.translate("Frame", u"Forward", None))
        self.spindleDirection.setItemText(1, QCoreApplication.translate("Frame", u"Reverse", None))

        pass
    # retranslateUi

