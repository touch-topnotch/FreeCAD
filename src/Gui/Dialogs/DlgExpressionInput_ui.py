# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgExpressionInput.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_DlgExpressionInput(object):
    def setupUi(self, DlgExpressionInput):
        if not DlgExpressionInput.objectName():
            DlgExpressionInput.setObjectName(u"DlgExpressionInput")
        DlgExpressionInput.resize(414, 272)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DlgExpressionInput.sizePolicy().hasHeightForWidth())
        DlgExpressionInput.setSizePolicy(sizePolicy)
        DlgExpressionInput.setMinimumSize(QSize(300, 0))
        self.verticalLayout = QVBoxLayout(DlgExpressionInput)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxVarSets = QGroupBox(DlgExpressionInput)
        self.groupBoxVarSets.setObjectName(u"groupBoxVarSets")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBoxVarSets)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.gridLayoutVarSets = QGridLayout()
        self.gridLayoutVarSets.setObjectName(u"gridLayoutVarSets")
        self.lineEditGroup = QLineEdit(self.groupBoxVarSets)
        self.lineEditGroup.setObjectName(u"lineEditGroup")

        self.gridLayoutVarSets.addWidget(self.lineEditGroup, 1, 2, 1, 1)

        self.labelGroup = QLabel(self.groupBoxVarSets)
        self.labelGroup.setObjectName(u"labelGroup")

        self.gridLayoutVarSets.addWidget(self.labelGroup, 1, 0, 1, 1)

        self.labelInfoActive = QLabel(self.groupBoxVarSets)
        self.labelInfoActive.setObjectName(u"labelInfoActive")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelInfoActive.sizePolicy().hasHeightForWidth())
        self.labelInfoActive.setSizePolicy(sizePolicy1)
        self.labelInfoActive.setMinimumSize(QSize(0, 70))

        self.gridLayoutVarSets.addWidget(self.labelInfoActive, 3, 2, 1, 1)

        self.labelVarSet = QLabel(self.groupBoxVarSets)
        self.labelVarSet.setObjectName(u"labelVarSet")

        self.gridLayoutVarSets.addWidget(self.labelVarSet, 0, 0, 1, 1)

        self.comboBoxVarSet = QComboBox(self.groupBoxVarSets)
        self.comboBoxVarSet.setObjectName(u"comboBoxVarSet")

        self.gridLayoutVarSets.addWidget(self.comboBoxVarSet, 0, 2, 1, 1)

        self.labelInfo = QLabel(self.groupBoxVarSets)
        self.labelInfo.setObjectName(u"labelInfo")

        self.gridLayoutVarSets.addWidget(self.labelInfo, 3, 0, 1, 1)

        self.LabelPropNew = QLabel(self.groupBoxVarSets)
        self.LabelPropNew.setObjectName(u"LabelPropNew")

        self.gridLayoutVarSets.addWidget(self.LabelPropNew, 2, 0, 1, 1)

        self.lineEditPropNew = QLineEdit(self.groupBoxVarSets)
        self.lineEditPropNew.setObjectName(u"lineEditPropNew")
        sizePolicy.setHeightForWidth(self.lineEditPropNew.sizePolicy().hasHeightForWidth())
        self.lineEditPropNew.setSizePolicy(sizePolicy)

        self.gridLayoutVarSets.addWidget(self.lineEditPropNew, 2, 2, 1, 1)


        self.horizontalLayout_8.addLayout(self.gridLayoutVarSets)


        self.verticalLayout.addWidget(self.groupBoxVarSets)

        self.checkBoxVarSets = QCheckBox(DlgExpressionInput)
        self.checkBoxVarSets.setObjectName(u"checkBoxVarSets")

        self.verticalLayout.addWidget(self.checkBoxVarSets)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
#ifndef Q_OS_MAC
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
#endif
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ctrlArea = QFrame(DlgExpressionInput)
        self.ctrlArea.setObjectName(u"ctrlArea")
        self.ctrlArea.setAutoFillBackground(True)
        self.ctrlArea.setFrameShape(QFrame.StyledPanel)
        self.ctrlArea.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.ctrlArea)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.ctrlArea)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.msg = QLabel(self.ctrlArea)
        self.msg.setObjectName(u"msg")
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush1 = QBrush(QColor(190, 190, 190, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        self.msg.setPalette(palette)

        self.horizontalLayout_4.addWidget(self.msg)


        self.verticalLayout_2.addWidget(self.ctrlArea)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.expression = Gui_ExpressionLineEdit(DlgExpressionInput)
        self.expression.setObjectName(u"expression")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.expression.sizePolicy().hasHeightForWidth())
        self.expression.setSizePolicy(sizePolicy2)
        self.expression.setMinimumSize(QSize(10, 10))

        self.horizontalLayout_5.addWidget(self.expression)

        self.horizontalSpacer_3 = QSpacerItem(0, 2, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.discardBtn = QPushButton(DlgExpressionInput)
        self.discardBtn.setObjectName(u"discardBtn")
        self.discardBtn.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.discardBtn)

        self.okBtn = QPushButton(DlgExpressionInput)
        self.okBtn.setObjectName(u"okBtn")
        self.okBtn.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.okBtn)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        QWidget.setTabOrder(self.expression, self.okBtn)
        QWidget.setTabOrder(self.okBtn, self.discardBtn)
        QWidget.setTabOrder(self.discardBtn, self.checkBoxVarSets)

        self.retranslateUi(DlgExpressionInput)
        self.okBtn.clicked.connect(DlgExpressionInput.accept)

        self.discardBtn.setDefault(False)
        self.okBtn.setDefault(True)


        QMetaObject.connectSlotsByName(DlgExpressionInput)
    # setupUi

    def retranslateUi(self, DlgExpressionInput):
        DlgExpressionInput.setWindowTitle(QCoreApplication.translate("DlgExpressionInput", u"Expression editor", None))
        self.groupBoxVarSets.setTitle(QCoreApplication.translate("DlgExpressionInput", u"Variable Sets", None))
        self.labelGroup.setText(QCoreApplication.translate("DlgExpressionInput", u"Group:", None))
        self.labelInfoActive.setText("")
        self.labelVarSet.setText(QCoreApplication.translate("DlgExpressionInput", u"Variable Set:", None))
        self.labelInfo.setText(QCoreApplication.translate("DlgExpressionInput", u"Info:", None))
        self.LabelPropNew.setText(QCoreApplication.translate("DlgExpressionInput", u"New Property:", None))
        self.checkBoxVarSets.setText(QCoreApplication.translate("DlgExpressionInput", u"Show variable sets", None))
        self.label.setText(QCoreApplication.translate("DlgExpressionInput", u"Result:", None))
        self.msg.setText("")
#if QT_CONFIG(tooltip)
        self.discardBtn.setToolTip(QCoreApplication.translate("DlgExpressionInput", u"Revert to last calculated value (as constant)", None))
#endif // QT_CONFIG(tooltip)
        self.discardBtn.setText(QCoreApplication.translate("DlgExpressionInput", u"&Clear", None))
        self.okBtn.setText(QCoreApplication.translate("DlgExpressionInput", u"&OK", None))
    # retranslateUi

