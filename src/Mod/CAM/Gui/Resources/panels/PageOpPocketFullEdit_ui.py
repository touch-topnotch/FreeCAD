# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpPocketFullEdit.ui'
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
    QSpacerItem, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(398, 513)
        Form.setWindowTitle(u"Form")
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.toolController_label = QLabel(self.frame)
        self.toolController_label.setObjectName(u"toolController_label")

        self.gridLayout_3.addWidget(self.toolController_label, 0, 0, 1, 1)

        self.toolController = QComboBox(self.frame)
        self.toolController.setObjectName(u"toolController")

        self.gridLayout_3.addWidget(self.toolController, 0, 1, 1, 1)

        self.coolantController_label = QLabel(self.frame)
        self.coolantController_label.setObjectName(u"coolantController_label")

        self.gridLayout_3.addWidget(self.coolantController_label, 1, 0, 1, 1)

        self.coolantController = QComboBox(self.frame)
        self.coolantController.setObjectName(u"coolantController")

        self.gridLayout_3.addWidget(self.coolantController, 1, 1, 1, 1)

        self.editToolController = QCheckBox(self.frame)
        self.editToolController.setObjectName(u"editToolController")

        self.gridLayout_3.addWidget(self.editToolController, 2, 0, 1, 2)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        self.facingWidget = QWidget(Form)
        self.facingWidget.setObjectName(u"facingWidget")
        self.gridLayout_2 = QGridLayout(self.facingWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.boundaryShape_label = QLabel(self.facingWidget)
        self.boundaryShape_label.setObjectName(u"boundaryShape_label")

        self.gridLayout_2.addWidget(self.boundaryShape_label, 0, 0, 1, 1)

        self.boundaryShape = QComboBox(self.facingWidget)
        self.boundaryShape.setObjectName(u"boundaryShape")

        self.gridLayout_2.addWidget(self.boundaryShape, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.facingWidget, 1, 0, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.cutMode_label = QLabel(self.widget)
        self.cutMode_label.setObjectName(u"cutMode_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.cutMode_label)

        self.cutMode = QComboBox(self.widget)
        self.cutMode.addItem("")
        self.cutMode.addItem("")
        self.cutMode.setObjectName(u"cutMode")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cutMode)

        self.offsetPattern_label = QLabel(self.widget)
        self.offsetPattern_label.setObjectName(u"offsetPattern_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.offsetPattern_label)

        self.offsetPattern = QComboBox(self.widget)
        self.offsetPattern.addItem("")
        self.offsetPattern.addItem(u"Offset")
        self.offsetPattern.addItem("")
        self.offsetPattern.addItem("")
        self.offsetPattern.addItem("")
        self.offsetPattern.addItem("")
        self.offsetPattern.addItem("")
        self.offsetPattern.setObjectName(u"offsetPattern")
        self.offsetPattern.setCurrentText(u"ZigZag")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.offsetPattern)

        self.zigZagAngle_label = QLabel(self.widget)
        self.zigZagAngle_label.setObjectName(u"zigZagAngle_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.zigZagAngle_label)

        self.zigZagAngle = Gui_InputField(self.widget)
        self.zigZagAngle.setObjectName(u"zigZagAngle")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.zigZagAngle)

        self.stepOverPercent_label = QLabel(self.widget)
        self.stepOverPercent_label.setObjectName(u"stepOverPercent_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.stepOverPercent_label)

        self.stepOverPercent = QSpinBox(self.widget)
        self.stepOverPercent.setObjectName(u"stepOverPercent")
        self.stepOverPercent.setMinimum(1)
        self.stepOverPercent.setMaximum(100)
        self.stepOverPercent.setSingleStep(10)
        self.stepOverPercent.setValue(100)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.stepOverPercent)

        self.extraOffset_label = QLabel(self.widget)
        self.extraOffset_label.setObjectName(u"extraOffset_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.extraOffset_label)

        self.extraOffset = Gui_InputField(self.widget)
        self.extraOffset.setObjectName(u"extraOffset")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.extraOffset)


        self.gridLayout_4.addWidget(self.widget, 2, 0, 1, 1)

        self.pocketWidget = QWidget(Form)
        self.pocketWidget.setObjectName(u"pocketWidget")
        self.gridLayout = QGridLayout(self.pocketWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.useStartPoint = QCheckBox(self.pocketWidget)
        self.useStartPoint.setObjectName(u"useStartPoint")

        self.gridLayout.addWidget(self.useStartPoint, 1, 0, 1, 1)

        self.useOutline = QCheckBox(self.pocketWidget)
        self.useOutline.setObjectName(u"useOutline")

        self.gridLayout.addWidget(self.useOutline, 1, 1, 1, 1)

        self.clearEdges = QCheckBox(self.pocketWidget)
        self.clearEdges.setObjectName(u"clearEdges")

        self.gridLayout.addWidget(self.clearEdges, 2, 0, 1, 1)

        self.minTravel = QCheckBox(self.pocketWidget)
        self.minTravel.setObjectName(u"minTravel")

        self.gridLayout.addWidget(self.minTravel, 2, 1, 1, 1)

        self.useRestMachining = QCheckBox(self.pocketWidget)
        self.useRestMachining.setObjectName(u"useRestMachining")

        self.gridLayout.addWidget(self.useRestMachining, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.pocketWidget, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 4, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.toolController_label.setText(QCoreApplication.translate("Form", u"Tool controller", None))
#if QT_CONFIG(tooltip)
        self.toolController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation", None))
#endif // QT_CONFIG(tooltip)
        self.coolantController_label.setText(QCoreApplication.translate("Form", u"Coolant Mode", None))
#if QT_CONFIG(tooltip)
        self.coolantController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation", None))
#endif // QT_CONFIG(tooltip)
        self.editToolController.setText(QCoreApplication.translate("Form", u"Edit Tool Controller", None))
        self.boundaryShape_label.setText(QCoreApplication.translate("Form", u"Boundary Shape", None))
#if QT_CONFIG(tooltip)
        self.boundaryShape.setToolTip(QCoreApplication.translate("Form", u"Specify if the facing should be restricted by the actual shape of the selected face (or the part if no face is selected), or if the bounding box should be faced off.\n"
"\n"
"The latter can be used to face of the entire stock area to ensure uniform heights for the following operations.", None))
#endif // QT_CONFIG(tooltip)
        self.cutMode_label.setText(QCoreApplication.translate("Form", u"Cut Mode", None))
        self.cutMode.setItemText(0, QCoreApplication.translate("Form", u"Climb", None))
        self.cutMode.setItemText(1, QCoreApplication.translate("Form", u"Conventional", None))

#if QT_CONFIG(tooltip)
        self.cutMode.setToolTip(QCoreApplication.translate("Form", u"The cutting mode assumes that the cut on one side of the tool bit represents the resulting part and the other side is either already milled away or will be removed later on. Climb mode is when the tool bit is moved into the cut on each rotation, whereas in conventional mode the tool bit's rotation and the tool's lateral movement are in the same direction", None))
#endif // QT_CONFIG(tooltip)
        self.offsetPattern_label.setText(QCoreApplication.translate("Form", u"Pattern", None))
        self.offsetPattern.setItemText(0, QCoreApplication.translate("Form", u"ZigZag", None))
        self.offsetPattern.setItemText(2, QCoreApplication.translate("Form", u"Spiral", None))
        self.offsetPattern.setItemText(3, QCoreApplication.translate("Form", u"ZigZagOffset", None))
        self.offsetPattern.setItemText(4, QCoreApplication.translate("Form", u"Line", None))
        self.offsetPattern.setItemText(5, QCoreApplication.translate("Form", u"Grid", None))
        self.offsetPattern.setItemText(6, QCoreApplication.translate("Form", u"Triangle", None))

#if QT_CONFIG(tooltip)
        self.offsetPattern.setToolTip(QCoreApplication.translate("Form", u"Pattern the tool bit is moved in to clear the material", None))
#endif // QT_CONFIG(tooltip)
        self.zigZagAngle_label.setText(QCoreApplication.translate("Form", u"Angle", None))
#if QT_CONFIG(tooltip)
        self.zigZagAngle.setToolTip(QCoreApplication.translate("Form", u"Angle in which the pattern is applied", None))
#endif // QT_CONFIG(tooltip)
        self.stepOverPercent_label.setText(QCoreApplication.translate("Form", u"Step over percent", None))
#if QT_CONFIG(tooltip)
        self.stepOverPercent.setToolTip(QCoreApplication.translate("Form", u"The amount by which the tool is laterally displaced on each cycle of the pattern, specified in percent of the tool diameter. A step over of 100% results in no overlap between two different cycles", None))
#endif // QT_CONFIG(tooltip)
        self.extraOffset_label.setText(QCoreApplication.translate("Form", u"Material allowance", None))
#if QT_CONFIG(tooltip)
        self.extraOffset.setToolTip(QCoreApplication.translate("Form", u"The amount of material that should be left by this operation in relation to the target shape", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.useStartPoint.setToolTip(QCoreApplication.translate("Form", u"Specify if this operation uses a starting point", None))
#endif // QT_CONFIG(tooltip)
        self.useStartPoint.setText(QCoreApplication.translate("Form", u"Use start point", None))
#if QT_CONFIG(tooltip)
        self.useOutline.setToolTip(QCoreApplication.translate("Form", u"If selected the operation uses the outline of the selected base geometry and ignores all holes and islands", None))
#endif // QT_CONFIG(tooltip)
        self.useOutline.setText(QCoreApplication.translate("Form", u"Use outline", None))
        self.clearEdges.setText(QCoreApplication.translate("Form", u"Clear edges", None))
        self.minTravel.setText(QCoreApplication.translate("Form", u"Min travel", None))
#if QT_CONFIG(tooltip)
        self.useRestMachining.setToolTip(QCoreApplication.translate("Form", u"Check to skip machining regions that have already been cleared by previous operations", None))
#endif // QT_CONFIG(tooltip)
        self.useRestMachining.setText(QCoreApplication.translate("Form", u"Use rest machining", None))
        pass
    # retranslateUi

