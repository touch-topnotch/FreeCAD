# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpWaterlineEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(389, 400)
        Form.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.toolController_label = QLabel(self.frame_2)
        self.toolController_label.setObjectName(u"toolController_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.toolController_label)

        self.toolController = QComboBox(self.frame_2)
        self.toolController.setObjectName(u"toolController")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.toolController)

        self.coolantController = QComboBox(self.frame_2)
        self.coolantController.setObjectName(u"coolantController")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.coolantController)

        self.coolantController_label = QLabel(self.frame_2)
        self.coolantController_label.setObjectName(u"coolantController_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.coolantController_label)


        self.verticalLayout.addWidget(self.frame_2)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.algorithmSelect_label = QLabel(self.widget)
        self.algorithmSelect_label.setObjectName(u"algorithmSelect_label")

        self.gridLayout.addWidget(self.algorithmSelect_label, 0, 0, 1, 1)

        self.algorithmSelect = QComboBox(self.widget)
        self.algorithmSelect.setObjectName(u"algorithmSelect")

        self.gridLayout.addWidget(self.algorithmSelect, 0, 1, 1, 1)

        self.boundBoxSelect_label = QLabel(self.widget)
        self.boundBoxSelect_label.setObjectName(u"boundBoxSelect_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boundBoxSelect_label.sizePolicy().hasHeightForWidth())
        self.boundBoxSelect_label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.boundBoxSelect_label, 1, 0, 1, 1)

        self.boundBoxSelect = QComboBox(self.widget)
        self.boundBoxSelect.setObjectName(u"boundBoxSelect")
        font = QFont()
        font.setPointSize(12)
        self.boundBoxSelect.setFont(font)

        self.gridLayout.addWidget(self.boundBoxSelect, 1, 1, 1, 1)

        self.layerMode_label = QLabel(self.widget)
        self.layerMode_label.setObjectName(u"layerMode_label")

        self.gridLayout.addWidget(self.layerMode_label, 2, 0, 1, 1)

        self.layerMode = QComboBox(self.widget)
        self.layerMode.setObjectName(u"layerMode")
        self.layerMode.setFont(font)

        self.gridLayout.addWidget(self.layerMode, 2, 1, 1, 1)

        self.cutPattern_label = QLabel(self.widget)
        self.cutPattern_label.setObjectName(u"cutPattern_label")

        self.gridLayout.addWidget(self.cutPattern_label, 3, 0, 1, 1)

        self.cutPattern = QComboBox(self.widget)
        self.cutPattern.setObjectName(u"cutPattern")
        self.cutPattern.setFont(font)

        self.gridLayout.addWidget(self.cutPattern, 3, 1, 1, 1)

        self.boundaryAdjustment_label = QLabel(self.widget)
        self.boundaryAdjustment_label.setObjectName(u"boundaryAdjustment_label")
        sizePolicy.setHeightForWidth(self.boundaryAdjustment_label.sizePolicy().hasHeightForWidth())
        self.boundaryAdjustment_label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.boundaryAdjustment_label, 4, 0, 1, 1)

        self.boundaryAdjustment = Gui_InputField(self.widget)
        self.boundaryAdjustment.setObjectName(u"boundaryAdjustment")
        self.boundaryAdjustment.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.boundaryAdjustment, 4, 1, 1, 1)

        self.stepOver_label = QLabel(self.widget)
        self.stepOver_label.setObjectName(u"stepOver_label")

        self.gridLayout.addWidget(self.stepOver_label, 5, 0, 1, 1)

        self.stepOver = QSpinBox(self.widget)
        self.stepOver.setObjectName(u"stepOver")
        sizePolicy.setHeightForWidth(self.stepOver.sizePolicy().hasHeightForWidth())
        self.stepOver.setSizePolicy(sizePolicy)
        self.stepOver.setMinimum(1)
        self.stepOver.setMaximum(100)

        self.gridLayout.addWidget(self.stepOver, 5, 1, 1, 1)

        self.sampleInterval_label = QLabel(self.widget)
        self.sampleInterval_label.setObjectName(u"sampleInterval_label")

        self.gridLayout.addWidget(self.sampleInterval_label, 6, 0, 1, 1)

        self.sampleInterval = Gui_InputField(self.widget)
        self.sampleInterval.setObjectName(u"sampleInterval")
        self.sampleInterval.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.sampleInterval, 6, 1, 1, 1)

        self.optimizeEnabled = QCheckBox(self.widget)
        self.optimizeEnabled.setObjectName(u"optimizeEnabled")

        self.gridLayout.addWidget(self.optimizeEnabled, 7, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        QWidget.setTabOrder(self.toolController, self.coolantController)
        QWidget.setTabOrder(self.coolantController, self.algorithmSelect)
        QWidget.setTabOrder(self.algorithmSelect, self.boundBoxSelect)
        QWidget.setTabOrder(self.boundBoxSelect, self.layerMode)
        QWidget.setTabOrder(self.layerMode, self.cutPattern)
        QWidget.setTabOrder(self.cutPattern, self.stepOver)
        QWidget.setTabOrder(self.stepOver, self.sampleInterval)
        QWidget.setTabOrder(self.sampleInterval, self.optimizeEnabled)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.toolController_label.setText(QCoreApplication.translate("Form", u"Tool Controller", None))
#if QT_CONFIG(tooltip)
        self.toolController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation.", None))
#endif // QT_CONFIG(tooltip)
        self.coolantController_label.setText(QCoreApplication.translate("Form", u"Coolant Mode", None))
        self.algorithmSelect_label.setText(QCoreApplication.translate("Form", u"Algorithm", None))
#if QT_CONFIG(tooltip)
        self.algorithmSelect.setToolTip(QCoreApplication.translate("Form", u"Select the algorithm to use: OCL Dropcutter*, or Experimental (Not OCL based).", None))
#endif // QT_CONFIG(tooltip)
        self.boundBoxSelect_label.setText(QCoreApplication.translate("Form", u"Bounding Box", None))
#if QT_CONFIG(tooltip)
        self.boundBoxSelect.setToolTip(QCoreApplication.translate("Form", u"Select the overall boundary for the operation.", None))
#endif // QT_CONFIG(tooltip)
        self.layerMode_label.setText(QCoreApplication.translate("Form", u"Layer Mode", None))
#if QT_CONFIG(tooltip)
        self.layerMode.setToolTip(QCoreApplication.translate("Form", u"Complete the operation in a single pass at depth, or multiple passes to final depth.", None))
#endif // QT_CONFIG(tooltip)
        self.cutPattern_label.setText(QCoreApplication.translate("Form", u"Cut Pattern", None))
#if QT_CONFIG(tooltip)
        self.cutPattern.setToolTip(QCoreApplication.translate("Form", u"Set the geometric clearing pattern to use for the operation.", None))
#endif // QT_CONFIG(tooltip)
        self.boundaryAdjustment_label.setText(QCoreApplication.translate("Form", u"Boundary Adjustment", None))
#if QT_CONFIG(tooltip)
        self.boundaryAdjustment.setToolTip(QCoreApplication.translate("Form", u"Set the Z-axis depth offset from the target surface.", None))
#endif // QT_CONFIG(tooltip)
        self.stepOver_label.setText(QCoreApplication.translate("Form", u"Step over", None))
#if QT_CONFIG(tooltip)
        self.stepOver.setToolTip(QCoreApplication.translate("Form", u"The amount by which the tool is laterally displaced on each cycle of the pattern, specified in percent of the tool diameter.\n"
"\n"
"A step over of 100% results in no overlap between two different cycles.", None))
#endif // QT_CONFIG(tooltip)
        self.sampleInterval_label.setText(QCoreApplication.translate("Form", u"Sample interval", None))
#if QT_CONFIG(tooltip)
        self.sampleInterval.setToolTip(QCoreApplication.translate("Form", u"Set the sampling resolution. Smaller values quickly increase processing time.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.optimizeEnabled.setToolTip(QCoreApplication.translate("Form", u"Enable optimization of linear paths (co-linear points). Removes unnecessary co-linear points from G-code output.", None))
#endif // QT_CONFIG(tooltip)
        self.optimizeEnabled.setText(QCoreApplication.translate("Form", u"Optimize Linear Paths", None))
        pass
    # retranslateUi

