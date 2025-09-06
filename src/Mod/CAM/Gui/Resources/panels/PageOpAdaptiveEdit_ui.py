# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpAdaptiveEdit.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(437, 764)
        Form.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.toolController = QComboBox(self.frame_2)
        self.toolController.setObjectName(u"toolController")

        self.gridLayout.addWidget(self.toolController, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.coolantController = QComboBox(self.frame_2)
        self.coolantController.setObjectName(u"coolantController")

        self.gridLayout.addWidget(self.coolantController, 1, 1, 1, 1)

        self.editToolController = QCheckBox(self.frame_2)
        self.editToolController.setObjectName(u"editToolController")

        self.gridLayout.addWidget(self.editToolController, 2, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.threadFitLabel = QLabel(self.frame_3)
        self.threadFitLabel.setObjectName(u"threadFitLabel")

        self.horizontalLayout.addWidget(self.threadFitLabel)

        self.Tolerance = QSlider(self.frame_3)
        self.Tolerance.setObjectName(u"Tolerance")
        self.Tolerance.setMinimum(5)
        self.Tolerance.setMaximum(15)
        self.Tolerance.setValue(10)
        self.Tolerance.setSliderPosition(10)
        self.Tolerance.setOrientation(Qt.Orientation.Horizontal)
        self.Tolerance.setTickInterval(1)

        self.horizontalLayout.addWidget(self.Tolerance)


        self.gridLayout_2.addWidget(self.frame_3, 9, 0, 1, 2)

        self.ForceInsideOut = QCheckBox(self.frame)
        self.ForceInsideOut.setObjectName(u"ForceInsideOut")

        self.gridLayout_2.addWidget(self.ForceInsideOut, 23, 0, 1, 1)

        self.Side = QComboBox(self.frame)
        self.Side.setObjectName(u"Side")

        self.gridLayout_2.addWidget(self.Side, 0, 1, 1, 1)

        self.OperationType = QComboBox(self.frame)
        self.OperationType.setObjectName(u"OperationType")

        self.gridLayout_2.addWidget(self.OperationType, 2, 1, 1, 1)

        self.FinishingProfile = QCheckBox(self.frame)
        self.FinishingProfile.setObjectName(u"FinishingProfile")

        self.gridLayout_2.addWidget(self.FinishingProfile, 24, 0, 1, 1)

        self.StockToLeave = Gui_QuantitySpinBox(self.frame)
        self.StockToLeave.setObjectName(u"StockToLeave")
        self.StockToLeave.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.StockToLeave, 20, 1, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 20, 0, 1, 1)

        self.stepOverPercent = QSpinBox(self.frame)
        self.stepOverPercent.setObjectName(u"stepOverPercent")
        self.stepOverPercent.setMinimum(1)
        self.stepOverPercent.setMaximum(100)
        self.stepOverPercent.setSingleStep(10)
        self.stepOverPercent.setValue(100)

        self.gridLayout_2.addWidget(self.stepOverPercent, 4, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.HelixConeAngle = Gui_InputField(self.frame)
        self.HelixConeAngle.setObjectName(u"HelixConeAngle")
        self.HelixConeAngle.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.HelixConeAngle, 12, 1, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 10, 0, 1, 1)

        self.useOutline = QCheckBox(self.frame)
        self.useOutline.setObjectName(u"useOutline")

        self.gridLayout_2.addWidget(self.useOutline, 25, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.LiftDistance = Gui_QuantitySpinBox(self.frame)
        self.LiftDistance.setObjectName(u"LiftDistance")
        self.LiftDistance.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.LiftDistance, 16, 1, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 18, 0, 1, 1)

        self.HelixDiameterLimit = Gui_QuantitySpinBox(self.frame)
        self.HelixDiameterLimit.setObjectName(u"HelixDiameterLimit")
        self.HelixDiameterLimit.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.HelixDiameterLimit, 14, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 12, 0, 1, 1)

        self.HelixAngle = Gui_InputField(self.frame)
        self.HelixAngle.setObjectName(u"HelixAngle")
        self.HelixAngle.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.HelixAngle, 10, 1, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 16, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.KeepToolDownRatio = Gui_QuantitySpinBox(self.frame)
        self.KeepToolDownRatio.setObjectName(u"KeepToolDownRatio")
        self.KeepToolDownRatio.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.KeepToolDownRatio, 18, 1, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 14, 0, 1, 1)

        self.orderCutsByRegion = QCheckBox(self.frame)
        self.orderCutsByRegion.setObjectName(u"orderCutsByRegion")

        self.gridLayout_2.addWidget(self.orderCutsByRegion, 26, 0, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 21, 0, 1, 1)

        self.ZStockToLeave = Gui_QuantitySpinBox(self.frame)
        self.ZStockToLeave.setObjectName(u"ZStockToLeave")

        self.gridLayout_2.addWidget(self.ZStockToLeave, 21, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.StopButton = QPushButton(Form)
        self.StopButton.setObjectName(u"StopButton")

        self.verticalLayout.addWidget(self.StopButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.label_5.setText(QCoreApplication.translate("Form", u"Tool controller", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Coolant", None))
        self.editToolController.setText(QCoreApplication.translate("Form", u"Edit Tool Controller", None))
        self.threadFitLabel.setText(QCoreApplication.translate("Form", u"Accuracy vs performance", None))
#if QT_CONFIG(tooltip)
        self.Tolerance.setToolTip(QCoreApplication.translate("Form", u"Influences calculation performance vs stability and accuracy.\n"
"\n"
"Larger values (further to the right) will calculate faster; smaller values (further to the left) will result in more accurate toolpaths.", None))
#endif // QT_CONFIG(tooltip)
        self.ForceInsideOut.setText(QCoreApplication.translate("Form", u"Force clearing inside-out", None))
#if QT_CONFIG(tooltip)
        self.Side.setToolTip(QCoreApplication.translate("Form", u"Cut inside or outside of the selected shapes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.OperationType.setToolTip(QCoreApplication.translate("Form", u"Type of adaptive operation", None))
#endif // QT_CONFIG(tooltip)
        self.FinishingProfile.setText(QCoreApplication.translate("Form", u"Finishing profile", None))
#if QT_CONFIG(tooltip)
        self.StockToLeave.setToolTip(QCoreApplication.translate("Form", u"How much material to leave in the XY-plane (i.e. for finishing operation)", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("Form", u"XY stock to leave", None))
#if QT_CONFIG(tooltip)
        self.stepOverPercent.setToolTip(QCoreApplication.translate("Form", u"The amount by which the tool is laterally displaced on each cycle of the pattern, specified in percent of the tool diameter. A step over of 100% results in no overlap between two different cycles.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"Step over percent", None))
#if QT_CONFIG(tooltip)
        self.HelixConeAngle.setToolTip(QCoreApplication.translate("Form", u"Angle of the helix entry cone", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("Form", u"Helix ramp angle", None))
        self.useOutline.setText(QCoreApplication.translate("Form", u"Use outline", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Operation type", None))
#if QT_CONFIG(tooltip)
        self.LiftDistance.setToolTip(QCoreApplication.translate("Form", u"How much to lift the tool up during the rapid linking moves over cleared regions. If linking path is not clear tool is raised to clearance height.", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("Form", u"Keep tool down ratio", None))
#if QT_CONFIG(tooltip)
        self.HelixDiameterLimit.setToolTip(QCoreApplication.translate("Form", u"If greater than zero it limits the helix ramp diameter, otherwise 75 percent of tool diameter is used", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Form", u"Helix cone angle", None))
#if QT_CONFIG(tooltip)
        self.HelixAngle.setToolTip(QCoreApplication.translate("Form", u"Angle of the helix ramp entry", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("Form", u"Lift distance", None))
        self.label.setText(QCoreApplication.translate("Form", u"Cut region", None))
#if QT_CONFIG(tooltip)
        self.KeepToolDownRatio.setToolTip(QCoreApplication.translate("Form", u"Max length of keep-tool-down linking path compared to direct distance between points. If exceeded link will be done by raising the tool to clearance height.", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("Form", u"Helix max diameter", None))
#if QT_CONFIG(tooltip)
        self.orderCutsByRegion.setToolTip(QCoreApplication.translate("Form", u"After calculating toolpaths, the default cut order is by depth- all regions at a given stepdown are cleared before moving to the next stepdown.\n"
"\n"
"This option changes that behavior to cut each discrete area to its full depth before moving on to the next.", None))
#endif // QT_CONFIG(tooltip)
        self.orderCutsByRegion.setText(QCoreApplication.translate("Form", u"Order cuts by region", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Z stock to leave", None))
#if QT_CONFIG(tooltip)
        self.ZStockToLeave.setToolTip(QCoreApplication.translate("Form", u"How much material to leave along the Z axis (i.e. for finishing operation)", None))
#endif // QT_CONFIG(tooltip)
        self.StopButton.setText(QCoreApplication.translate("Form", u"Stop", None))
        pass
    # retranslateUi

