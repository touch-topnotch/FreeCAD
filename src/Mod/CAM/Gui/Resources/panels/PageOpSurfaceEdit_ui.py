# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpSurfaceEdit.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(498, 541)
        Form.setWindowTitle(u"Form")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolController_label = QLabel(self.frame_2)
        self.toolController_label.setObjectName(u"toolController_label")

        self.gridLayout.addWidget(self.toolController_label, 0, 0, 1, 1)

        self.toolController = QComboBox(self.frame_2)
        self.toolController.setObjectName(u"toolController")

        self.gridLayout.addWidget(self.toolController, 0, 1, 1, 1)

        self.coolantController_label = QLabel(self.frame_2)
        self.coolantController_label.setObjectName(u"coolantController_label")

        self.gridLayout.addWidget(self.coolantController_label, 1, 0, 1, 1)

        self.coolantController = QComboBox(self.frame_2)
        self.coolantController.setObjectName(u"coolantController")

        self.gridLayout.addWidget(self.coolantController, 1, 1, 1, 1)

        self.editToolController = QCheckBox(self.frame_2)
        self.editToolController.setObjectName(u"editToolController")

        self.gridLayout.addWidget(self.editToolController, 2, 0, 1, 2)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout1 = QGridLayout(self.widget)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.boundBoxSelect_label = QLabel(self.widget)
        self.boundBoxSelect_label.setObjectName(u"boundBoxSelect_label")

        self.gridLayout1.addWidget(self.boundBoxSelect_label, 0, 0, 1, 1)

        self.boundBoxSelect = QComboBox(self.widget)
        self.boundBoxSelect.setObjectName(u"boundBoxSelect")

        self.gridLayout1.addWidget(self.boundBoxSelect, 0, 1, 1, 2)

        self.scanType_label = QLabel(self.widget)
        self.scanType_label.setObjectName(u"scanType_label")

        self.gridLayout1.addWidget(self.scanType_label, 1, 0, 1, 1)

        self.scanType = QComboBox(self.widget)
        self.scanType.setObjectName(u"scanType")

        self.gridLayout1.addWidget(self.scanType, 1, 1, 1, 2)

        self.layerMode_label = QLabel(self.widget)
        self.layerMode_label.setObjectName(u"layerMode_label")

        self.gridLayout1.addWidget(self.layerMode_label, 2, 0, 1, 1)

        self.layerMode = QComboBox(self.widget)
        self.layerMode.setObjectName(u"layerMode")

        self.gridLayout1.addWidget(self.layerMode, 2, 1, 1, 2)

        self.cutPattern_label = QLabel(self.widget)
        self.cutPattern_label.setObjectName(u"cutPattern_label")

        self.gridLayout1.addWidget(self.cutPattern_label, 3, 0, 1, 1)

        self.cutPattern = QComboBox(self.widget)
        self.cutPattern.setObjectName(u"cutPattern")

        self.gridLayout1.addWidget(self.cutPattern, 3, 1, 1, 2)

        self.profileEdges_label = QLabel(self.widget)
        self.profileEdges_label.setObjectName(u"profileEdges_label")

        self.gridLayout1.addWidget(self.profileEdges_label, 4, 0, 1, 1)

        self.profileEdges = QComboBox(self.widget)
        self.profileEdges.setObjectName(u"profileEdges")

        self.gridLayout1.addWidget(self.profileEdges, 4, 1, 1, 2)

        self.avoidLastX_Faces_label = QLabel(self.widget)
        self.avoidLastX_Faces_label.setObjectName(u"avoidLastX_Faces_label")

        self.gridLayout1.addWidget(self.avoidLastX_Faces_label, 5, 0, 1, 1)

        self.avoidLastX_Faces = QSpinBox(self.widget)
        self.avoidLastX_Faces.setObjectName(u"avoidLastX_Faces")

        self.gridLayout1.addWidget(self.avoidLastX_Faces, 5, 1, 1, 2)

        self.boundBoxExtraOffset_label = QLabel(self.widget)
        self.boundBoxExtraOffset_label.setObjectName(u"boundBoxExtraOffset_label")

        self.gridLayout1.addWidget(self.boundBoxExtraOffset_label, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.boundBoxExtraOffsetX = Gui_InputField(self.widget)
        self.boundBoxExtraOffsetX.setObjectName(u"boundBoxExtraOffsetX")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boundBoxExtraOffsetX.sizePolicy().hasHeightForWidth())
        self.boundBoxExtraOffsetX.setSizePolicy(sizePolicy)
        self.boundBoxExtraOffsetX.setProperty(u"unit", u"mm")

        self.horizontalLayout.addWidget(self.boundBoxExtraOffsetX)

        self.boundBoxExtraOffsetY = Gui_InputField(self.widget)
        self.boundBoxExtraOffsetY.setObjectName(u"boundBoxExtraOffsetY")
        self.boundBoxExtraOffsetY.setProperty(u"unit", u"mm")

        self.horizontalLayout.addWidget(self.boundBoxExtraOffsetY)


        self.gridLayout1.addLayout(self.horizontalLayout, 6, 1, 1, 2)

        self.dropCutterDirSelect_label = QLabel(self.widget)
        self.dropCutterDirSelect_label.setObjectName(u"dropCutterDirSelect_label")

        self.gridLayout1.addWidget(self.dropCutterDirSelect_label, 8, 0, 1, 1)

        self.dropCutterDirSelect = QComboBox(self.widget)
        self.dropCutterDirSelect.setObjectName(u"dropCutterDirSelect")

        self.gridLayout1.addWidget(self.dropCutterDirSelect, 8, 1, 1, 2)

        self.depthOffset_label = QLabel(self.widget)
        self.depthOffset_label.setObjectName(u"depthOffset_label")

        self.gridLayout1.addWidget(self.depthOffset_label, 9, 0, 1, 1)

        self.depthOffset = Gui_InputField(self.widget)
        self.depthOffset.setObjectName(u"depthOffset")
        self.depthOffset.setProperty(u"unit", u"mm")

        self.gridLayout1.addWidget(self.depthOffset, 9, 1, 1, 2)

        self.stepOver_label = QLabel(self.widget)
        self.stepOver_label.setObjectName(u"stepOver_label")

        self.gridLayout1.addWidget(self.stepOver_label, 10, 0, 1, 1)

        self.stepOver = QSpinBox(self.widget)
        self.stepOver.setObjectName(u"stepOver")
        self.stepOver.setMinimum(1)
        self.stepOver.setMaximum(100)

        self.gridLayout1.addWidget(self.stepOver, 10, 1, 1, 2)

        self.sampleInterval_label = QLabel(self.widget)
        self.sampleInterval_label.setObjectName(u"sampleInterval_label")

        self.gridLayout1.addWidget(self.sampleInterval_label, 12, 0, 1, 1)

        self.sampleInterval = Gui_InputField(self.widget)
        self.sampleInterval.setObjectName(u"sampleInterval")
        self.sampleInterval.setProperty(u"unit", u"mm")

        self.gridLayout1.addWidget(self.sampleInterval, 12, 1, 1, 2)

        self.useStartPoint = QCheckBox(self.widget)
        self.useStartPoint.setObjectName(u"useStartPoint")

        self.gridLayout1.addWidget(self.useStartPoint, 14, 0, 1, 1)

        self.optimizeEnabled = QCheckBox(self.widget)
        self.optimizeEnabled.setObjectName(u"optimizeEnabled")

        self.gridLayout1.addWidget(self.optimizeEnabled, 14, 1, 1, 1)

        self.boundaryEnforcement = QCheckBox(self.widget)
        self.boundaryEnforcement.setObjectName(u"boundaryEnforcement")
        self.boundaryEnforcement.setChecked(True)

        self.gridLayout1.addWidget(self.boundaryEnforcement, 15, 0, 1, 1)

        self.optimizeStepOverTransitions = QCheckBox(self.widget)
        self.optimizeStepOverTransitions.setObjectName(u"optimizeStepOverTransitions")

        self.gridLayout1.addWidget(self.optimizeStepOverTransitions, 15, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.toolController_label.setText(QCoreApplication.translate("Form", u"Tool Controller", None))
#if QT_CONFIG(tooltip)
        self.toolController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation", None))
#endif // QT_CONFIG(tooltip)
        self.coolantController_label.setText(QCoreApplication.translate("Form", u"Coolant mode", None))
#if QT_CONFIG(tooltip)
        self.coolantController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation", None))
#endif // QT_CONFIG(tooltip)
        self.editToolController.setText(QCoreApplication.translate("Form", u"Edit Tool Controller", None))
        self.boundBoxSelect_label.setText(QCoreApplication.translate("Form", u"Bounding box", None))
#if QT_CONFIG(tooltip)
        self.boundBoxSelect.setToolTip(QCoreApplication.translate("Form", u"Select the overall boundary for the operation", None))
#endif // QT_CONFIG(tooltip)
        self.scanType_label.setText(QCoreApplication.translate("Form", u"Scan type", None))
#if QT_CONFIG(tooltip)
        self.scanType.setToolTip(QCoreApplication.translate("Form", u"Planar: flat, 3D surface scan. Rotational: 4th-axis rotational scan.", None))
#endif // QT_CONFIG(tooltip)
        self.layerMode_label.setText(QCoreApplication.translate("Form", u"Layer mode", None))
#if QT_CONFIG(tooltip)
        self.layerMode.setToolTip(QCoreApplication.translate("Form", u"Complete the operation in a single pass at depth, or multiple passes to final depth", None))
#endif // QT_CONFIG(tooltip)
        self.cutPattern_label.setText(QCoreApplication.translate("Form", u"Cut pattern", None))
#if QT_CONFIG(tooltip)
        self.cutPattern.setToolTip(QCoreApplication.translate("Form", u"Set the geometric clearing pattern to use for the operation", None))
#endif // QT_CONFIG(tooltip)
        self.profileEdges_label.setText(QCoreApplication.translate("Form", u"Profile edges", None))
#if QT_CONFIG(tooltip)
        self.profileEdges.setToolTip(QCoreApplication.translate("Form", u"Profile the edges of the selection", None))
#endif // QT_CONFIG(tooltip)
        self.avoidLastX_Faces_label.setText(QCoreApplication.translate("Form", u"Avoid last X faces", None))
#if QT_CONFIG(tooltip)
        self.avoidLastX_Faces.setToolTip(QCoreApplication.translate("Form", u"Avoid cutting the last 'n' faces in the base geometry list of selected faces", None))
#endif // QT_CONFIG(tooltip)
        self.boundBoxExtraOffset_label.setText(QCoreApplication.translate("Form", u"Bounding box extra offset X, Y", None))
#if QT_CONFIG(tooltip)
        self.boundBoxExtraOffsetX.setToolTip(QCoreApplication.translate("Form", u"Additional offset to the selected bounding box along the X axis", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.boundBoxExtraOffsetY.setToolTip(QCoreApplication.translate("Form", u"Additional offset to the selected bounding box along the Y axis", None))
#endif // QT_CONFIG(tooltip)
        self.dropCutterDirSelect_label.setText(QCoreApplication.translate("Form", u"Drop cutter direction", None))
#if QT_CONFIG(tooltip)
        self.dropCutterDirSelect.setToolTip(QCoreApplication.translate("Form", u"Dropcutter lines are created parallel to this axis.", None))
#endif // QT_CONFIG(tooltip)
        self.depthOffset_label.setText(QCoreApplication.translate("Form", u"Depth offset", None))
#if QT_CONFIG(tooltip)
        self.depthOffset.setToolTip(QCoreApplication.translate("Form", u"Set the Z-axis depth offset from the target surface", None))
#endif // QT_CONFIG(tooltip)
        self.stepOver_label.setText(QCoreApplication.translate("Form", u"Stepover", None))
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
        self.useStartPoint.setToolTip(QCoreApplication.translate("Form", u"Set to true if specifying a start point", None))
#endif // QT_CONFIG(tooltip)
        self.useStartPoint.setText(QCoreApplication.translate("Form", u"Use start point", None))
#if QT_CONFIG(tooltip)
        self.optimizeEnabled.setToolTip(QCoreApplication.translate("Form", u"Enable optimization of linear paths (co-linear points). Removes unnecessary co-linear points from G-code output.", None))
#endif // QT_CONFIG(tooltip)
        self.optimizeEnabled.setText(QCoreApplication.translate("Form", u"Optimize linear paths", None))
#if QT_CONFIG(tooltip)
        self.boundaryEnforcement.setToolTip(QCoreApplication.translate("Form", u"If true, the cutter will remain inside the boundaries of the model or selected faces", None))
#endif // QT_CONFIG(tooltip)
        self.boundaryEnforcement.setText(QCoreApplication.translate("Form", u"Boundary enforcement", None))
#if QT_CONFIG(tooltip)
        self.optimizeStepOverTransitions.setToolTip(QCoreApplication.translate("Form", u"Enable separate optimization of transitions between, and breaks within, each step over path.", None))
#endif // QT_CONFIG(tooltip)
        self.optimizeStepOverTransitions.setText(QCoreApplication.translate("Form", u"Optimize stepover transitions", None))
        pass
    # retranslateUi

