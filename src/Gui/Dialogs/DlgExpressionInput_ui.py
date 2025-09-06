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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_DlgExpressionInput(object):
    def setupUi(self, DlgExpressionInput):
        if not DlgExpressionInput.objectName():
            DlgExpressionInput.setObjectName(u"DlgExpressionInput")
        DlgExpressionInput.resize(414, 298)
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
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ctrlArea.sizePolicy().hasHeightForWidth())
        self.ctrlArea.setSizePolicy(sizePolicy1)
        self.ctrlArea.setAutoFillBackground(True)
        self.ctrlArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.ctrlArea.setFrameShadow(QFrame.Shadow.Raised)
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
        self.checkBoxVarSets = QCheckBox(DlgExpressionInput)
        self.checkBoxVarSets.setObjectName(u"checkBoxVarSets")

        self.horizontalLayout_3.addWidget(self.checkBoxVarSets)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBoxVarSets = QGroupBox(DlgExpressionInput)
        self.groupBoxVarSets.setObjectName(u"groupBoxVarSets")
        self.verticalLayout_3 = QVBoxLayout(self.groupBoxVarSets)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.errorFrame = QFrame(self.groupBoxVarSets)
        self.errorFrame.setObjectName(u"errorFrame")
        self.errorFrame.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.errorFrame.sizePolicy().hasHeightForWidth())
        self.errorFrame.setSizePolicy(sizePolicy3)
        self.errorFrame.setMinimumSize(QSize(0, 0))
        self.errorFrame.setStyleSheet(u"#errorFrame { border: 1px solid red; border-radius: 5px; background-color: #f8d7da; color: #721c24; } #errorTextLabel { color: #721c24; }")
        self.errorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.errorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.errorFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.errorIconLabel = QLabel(self.errorFrame)
        self.errorIconLabel.setObjectName(u"errorIconLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.errorIconLabel.sizePolicy().hasHeightForWidth())
        self.errorIconLabel.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.errorIconLabel)

        self.errorTextLabel = QLabel(self.errorFrame)
        self.errorTextLabel.setObjectName(u"errorTextLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.errorTextLabel.sizePolicy().hasHeightForWidth())
        self.errorTextLabel.setSizePolicy(sizePolicy5)
        self.errorTextLabel.setTextFormat(Qt.TextFormat.PlainText)
        self.errorTextLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.errorTextLabel.setWordWrap(True)
        self.errorTextLabel.setMargin(0)

        self.horizontalLayout.addWidget(self.errorTextLabel)


        self.verticalLayout_3.addWidget(self.errorFrame)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelVarSet = QLabel(self.groupBoxVarSets)
        self.labelVarSet.setObjectName(u"labelVarSet")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelVarSet)

        self.comboBoxVarSet = QComboBox(self.groupBoxVarSets)
        self.comboBoxVarSet.setObjectName(u"comboBoxVarSet")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBoxVarSet)

        self.labelGroup = QLabel(self.groupBoxVarSets)
        self.labelGroup.setObjectName(u"labelGroup")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelGroup)

        self.LabelPropNew = QLabel(self.groupBoxVarSets)
        self.LabelPropNew.setObjectName(u"LabelPropNew")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.LabelPropNew)

        self.lineEditPropNew = QLineEdit(self.groupBoxVarSets)
        self.lineEditPropNew.setObjectName(u"lineEditPropNew")
        sizePolicy1.setHeightForWidth(self.lineEditPropNew.sizePolicy().hasHeightForWidth())
        self.lineEditPropNew.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditPropNew)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.groupBoxVarSets)

        self.buttonBox = QDialogButtonBox(DlgExpressionInput)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy6)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok|QDialogButtonBox.StandardButton.Reset)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DlgExpressionInput)
        self.buttonBox.accepted.connect(DlgExpressionInput.accept)

        QMetaObject.connectSlotsByName(DlgExpressionInput)
    # setupUi

    def retranslateUi(self, DlgExpressionInput):
        DlgExpressionInput.setWindowTitle(QCoreApplication.translate("DlgExpressionInput", u"Expression Editor", None))
        self.label.setText(QCoreApplication.translate("DlgExpressionInput", u"Result", None))
        self.msg.setText("")
        self.checkBoxVarSets.setText(QCoreApplication.translate("DlgExpressionInput", u"Store in VarSet...", None))
        self.groupBoxVarSets.setTitle("")
        self.errorIconLabel.setText("")
        self.errorTextLabel.setText(QCoreApplication.translate("DlgExpressionInput", u"Error", None))
        self.labelVarSet.setText(QCoreApplication.translate("DlgExpressionInput", u"Variable Set", None))
        self.labelGroup.setText(QCoreApplication.translate("DlgExpressionInput", u"Group", None))
        self.LabelPropNew.setText(QCoreApplication.translate("DlgExpressionInput", u"Name", None))
    # retranslateUi

