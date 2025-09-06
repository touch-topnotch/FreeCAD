# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskHoleParameters.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)
import PartDesign_rc

class Ui_TaskHoleParameters(object):
    def setupUi(self, TaskHoleParameters):
        if not TaskHoleParameters.objectName():
            TaskHoleParameters.setObjectName(u"TaskHoleParameters")
        TaskHoleParameters.resize(366, 924)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TaskHoleParameters.sizePolicy().hasHeightForWidth())
        TaskHoleParameters.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(TaskHoleParameters)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 6, 3, 6)
        self.TopLayout = QGridLayout()
        self.TopLayout.setObjectName(u"TopLayout")
        self.TopLayout.setContentsMargins(-1, 10, -1, -1)
        self.labelProfileType = Gui_ElideLabel(TaskHoleParameters)
        self.labelProfileType.setObjectName(u"labelProfileType")

        self.TopLayout.addWidget(self.labelProfileType, 0, 0, 1, 1)

        self.BaseProfileType = QComboBox(TaskHoleParameters)
        self.BaseProfileType.addItem("")
        self.BaseProfileType.addItem("")
        self.BaseProfileType.addItem("")
        self.BaseProfileType.setObjectName(u"BaseProfileType")

        self.TopLayout.addWidget(self.BaseProfileType, 0, 1, 1, 1)

        self.labelHeadType = Gui_ElideLabel(TaskHoleParameters)
        self.labelHeadType.setObjectName(u"labelHeadType")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelHeadType.sizePolicy().hasHeightForWidth())
        self.labelHeadType.setSizePolicy(sizePolicy1)
        self.labelHeadType.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.TopLayout.addWidget(self.labelHeadType, 1, 0, 1, 1)

        self.DepthType = QComboBox(TaskHoleParameters)
        self.DepthType.addItem("")
        self.DepthType.addItem("")
        self.DepthType.setObjectName(u"DepthType")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.DepthType.sizePolicy().hasHeightForWidth())
        self.DepthType.setSizePolicy(sizePolicy2)
        self.DepthType.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.TopLayout.addWidget(self.DepthType, 3, 1, 1, 1)

        self.labelDepthType = Gui_ElideLabel(TaskHoleParameters)
        self.labelDepthType.setObjectName(u"labelDepthType")
        sizePolicy1.setHeightForWidth(self.labelDepthType.sizePolicy().hasHeightForWidth())
        self.labelDepthType.setSizePolicy(sizePolicy1)
        self.labelDepthType.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.TopLayout.addWidget(self.labelDepthType, 3, 0, 1, 1)

        self.HoleCutType = QComboBox(TaskHoleParameters)
        self.HoleCutType.setObjectName(u"HoleCutType")
        sizePolicy2.setHeightForWidth(self.HoleCutType.sizePolicy().hasHeightForWidth())
        self.HoleCutType.setSizePolicy(sizePolicy2)

        self.TopLayout.addWidget(self.HoleCutType, 1, 1, 1, 1)

        self.TopLayout.setColumnStretch(0, 2)
        self.TopLayout.setColumnStretch(1, 5)

        self.verticalLayout_2.addLayout(self.TopLayout)

        self.HoleCutCustomValues = Gui_ElideCheckBox(TaskHoleParameters)
        self.HoleCutCustomValues.setObjectName(u"HoleCutCustomValues")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.HoleCutCustomValues.sizePolicy().hasHeightForWidth())
        self.HoleCutCustomValues.setSizePolicy(sizePolicy3)
        self.HoleCutCustomValues.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_2.addWidget(self.HoleCutCustomValues)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(14)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, -1, 3)
        self.labelHoleCutDiameter = Gui_ElideLabel(TaskHoleParameters)
        self.labelHoleCutDiameter.setObjectName(u"labelHoleCutDiameter")
        sizePolicy2.setHeightForWidth(self.labelHoleCutDiameter.sizePolicy().hasHeightForWidth())
        self.labelHoleCutDiameter.setSizePolicy(sizePolicy2)

        self.verticalLayout_13.addWidget(self.labelHoleCutDiameter)

        self.HoleCutDiameter = Gui_PrefQuantitySpinBox(TaskHoleParameters)
        self.HoleCutDiameter.setObjectName(u"HoleCutDiameter")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.HoleCutDiameter.sizePolicy().hasHeightForWidth())
        self.HoleCutDiameter.setSizePolicy(sizePolicy4)
        self.HoleCutDiameter.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.HoleCutDiameter.setKeyboardTracking(False)
        self.HoleCutDiameter.setMinimum(0.000000000000000)
        self.HoleCutDiameter.setSingleStep(0.100000000000000)
        self.HoleCutDiameter.setProperty(u"unit", u"mm")

        self.verticalLayout_13.addWidget(self.HoleCutDiameter)


        self.verticalLayout_4.addLayout(self.verticalLayout_13)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 3)
        self.labelHoleCutDepth = Gui_ElideLabel(TaskHoleParameters)
        self.labelHoleCutDepth.setObjectName(u"labelHoleCutDepth")
        sizePolicy2.setHeightForWidth(self.labelHoleCutDepth.sizePolicy().hasHeightForWidth())
        self.labelHoleCutDepth.setSizePolicy(sizePolicy2)

        self.verticalLayout_12.addWidget(self.labelHoleCutDepth)

        self.HoleCutDepth = Gui_PrefQuantitySpinBox(TaskHoleParameters)
        self.HoleCutDepth.setObjectName(u"HoleCutDepth")
        sizePolicy4.setHeightForWidth(self.HoleCutDepth.sizePolicy().hasHeightForWidth())
        self.HoleCutDepth.setSizePolicy(sizePolicy4)
        self.HoleCutDepth.setKeyboardTracking(False)
        self.HoleCutDepth.setMinimum(0.000000000000000)
        self.HoleCutDepth.setSingleStep(0.100000000000000)
        self.HoleCutDepth.setProperty(u"unit", u"mm")

        self.verticalLayout_12.addWidget(self.HoleCutDepth)


        self.verticalLayout_4.addLayout(self.verticalLayout_12)

        self.DrillFrame = QFrame(TaskHoleParameters)
        self.DrillFrame.setObjectName(u"DrillFrame")
        self.DrillFrame.setEnabled(True)
        sizePolicy.setHeightForWidth(self.DrillFrame.sizePolicy().hasHeightForWidth())
        self.DrillFrame.setSizePolicy(sizePolicy)
        self.DrillFrame.setStyleSheet(u"QFrame {background-color: none; border-width: 0px;}")
        self.DrillFrame.setLineWidth(0)
        self.verticalLayout_5 = QVBoxLayout(self.DrillFrame)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 6, 0, 0)
        self.DrillPointAngled = Gui_ElideCheckBox(self.DrillFrame)
        self.DrillPointAngled.setObjectName(u"DrillPointAngled")
        sizePolicy2.setHeightForWidth(self.DrillPointAngled.sizePolicy().hasHeightForWidth())
        self.DrillPointAngled.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.DrillPointAngled)

        self.DrillPointAngle = Gui_PrefQuantitySpinBox(self.DrillFrame)
        self.DrillPointAngle.setObjectName(u"DrillPointAngle")
        sizePolicy4.setHeightForWidth(self.DrillPointAngle.sizePolicy().hasHeightForWidth())
        self.DrillPointAngle.setSizePolicy(sizePolicy4)
        self.DrillPointAngle.setKeyboardTracking(False)
        self.DrillPointAngle.setMinimum(0.000000000000000)
        self.DrillPointAngle.setProperty(u"unit", u"deg")

        self.verticalLayout_5.addWidget(self.DrillPointAngle)

        self.DrillForDepth = Gui_ElideCheckBox(self.DrillFrame)
        self.DrillForDepth.setObjectName(u"DrillForDepth")
        sizePolicy2.setHeightForWidth(self.DrillForDepth.sizePolicy().hasHeightForWidth())
        self.DrillForDepth.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.DrillForDepth)


        self.verticalLayout_4.addWidget(self.DrillFrame)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.cutDiagram = Gui_FontScaledSVG(TaskHoleParameters)
        self.cutDiagram.setObjectName(u"cutDiagram")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cutDiagram.sizePolicy().hasHeightForWidth())
        self.cutDiagram.setSizePolicy(sizePolicy5)
        self.cutDiagram.setMinimumSize(QSize(20, 40))
        self.cutDiagram.setBaseSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.cutDiagram)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(14)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 3)
        self.labelHoleCutCountersinkAngle = Gui_ElideLabel(TaskHoleParameters)
        self.labelHoleCutCountersinkAngle.setObjectName(u"labelHoleCutCountersinkAngle")
        sizePolicy2.setHeightForWidth(self.labelHoleCutCountersinkAngle.sizePolicy().hasHeightForWidth())
        self.labelHoleCutCountersinkAngle.setSizePolicy(sizePolicy2)
        self.labelHoleCutCountersinkAngle.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_9.addWidget(self.labelHoleCutCountersinkAngle)

        self.HoleCutCountersinkAngle = Gui_PrefQuantitySpinBox(TaskHoleParameters)
        self.HoleCutCountersinkAngle.setObjectName(u"HoleCutCountersinkAngle")
        sizePolicy4.setHeightForWidth(self.HoleCutCountersinkAngle.sizePolicy().hasHeightForWidth())
        self.HoleCutCountersinkAngle.setSizePolicy(sizePolicy4)
        self.HoleCutCountersinkAngle.setKeyboardTracking(False)
        self.HoleCutCountersinkAngle.setMinimum(0.000000000000000)
        self.HoleCutCountersinkAngle.setProperty(u"unit", u"deg")

        self.verticalLayout_9.addWidget(self.HoleCutCountersinkAngle)


        self.verticalLayout_6.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 3)
        self.labelDepth = Gui_ElideLabel(TaskHoleParameters)
        self.labelDepth.setObjectName(u"labelDepth")
        sizePolicy2.setHeightForWidth(self.labelDepth.sizePolicy().hasHeightForWidth())
        self.labelDepth.setSizePolicy(sizePolicy2)
        self.labelDepth.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_10.addWidget(self.labelDepth)

        self.Depth = Gui_PrefQuantitySpinBox(TaskHoleParameters)
        self.Depth.setObjectName(u"Depth")
        sizePolicy4.setHeightForWidth(self.Depth.sizePolicy().hasHeightForWidth())
        self.Depth.setSizePolicy(sizePolicy4)
        self.Depth.setKeyboardTracking(False)
        self.Depth.setProperty(u"unit", u"mm")

        self.verticalLayout_10.addWidget(self.Depth)


        self.verticalLayout_6.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 3, -1, 0)
        self.labelDiameter = Gui_ElideLabel(TaskHoleParameters)
        self.labelDiameter.setObjectName(u"labelDiameter")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.labelDiameter.sizePolicy().hasHeightForWidth())
        self.labelDiameter.setSizePolicy(sizePolicy6)
        self.labelDiameter.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_11.addWidget(self.labelDiameter)

        self.Diameter = Gui_PrefQuantitySpinBox(TaskHoleParameters)
        self.Diameter.setObjectName(u"Diameter")
        sizePolicy4.setHeightForWidth(self.Diameter.sizePolicy().hasHeightForWidth())
        self.Diameter.setSizePolicy(sizePolicy4)
        self.Diameter.setBaseSize(QSize(0, 0))
        self.Diameter.setKeyboardTracking(False)
        self.Diameter.setMinimum(0.000000000000000)
        self.Diameter.setProperty(u"unit", u"mm")

        self.verticalLayout_11.addWidget(self.Diameter)


        self.verticalLayout_6.addLayout(self.verticalLayout_11)


        self.horizontalLayout.addLayout(self.verticalLayout_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.Reversed = Gui_ElideCheckBox(TaskHoleParameters)
        self.Reversed.setObjectName(u"Reversed")
        sizePolicy3.setHeightForWidth(self.Reversed.sizePolicy().hasHeightForWidth())
        self.Reversed.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.Reversed)

        self.Tapered = QCheckBox(TaskHoleParameters)
        self.Tapered.setObjectName(u"Tapered")
        sizePolicy4.setHeightForWidth(self.Tapered.sizePolicy().hasHeightForWidth())
        self.Tapered.setSizePolicy(sizePolicy4)
        self.Tapered.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_7.addWidget(self.Tapered)

        self.TaperedAngle = Gui_PrefQuantitySpinBox(TaskHoleParameters)
        self.TaperedAngle.setObjectName(u"TaperedAngle")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.TaperedAngle.sizePolicy().hasHeightForWidth())
        self.TaperedAngle.setSizePolicy(sizePolicy7)
        self.TaperedAngle.setKeyboardTracking(False)
        self.TaperedAngle.setMinimum(0.000000000000000)
        self.TaperedAngle.setProperty(u"unit", u"deg")

        self.horizontalLayout_7.addWidget(self.TaperedAngle)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout_8)

        self.profileLayout = QGridLayout()
        self.profileLayout.setObjectName(u"profileLayout")
        self.profileLayout.setContentsMargins(-1, 0, -1, -1)
        self.labelThreadType = Gui_ElideLabel(TaskHoleParameters)
        self.labelThreadType.setObjectName(u"labelThreadType")
        sizePolicy1.setHeightForWidth(self.labelThreadType.sizePolicy().hasHeightForWidth())
        self.labelThreadType.setSizePolicy(sizePolicy1)

        self.profileLayout.addWidget(self.labelThreadType, 0, 0, 1, 1)

        self.ThreadType = QComboBox(TaskHoleParameters)
        self.ThreadType.setObjectName(u"ThreadType")
        sizePolicy2.setHeightForWidth(self.ThreadType.sizePolicy().hasHeightForWidth())
        self.ThreadType.setSizePolicy(sizePolicy2)

        self.profileLayout.addWidget(self.ThreadType, 0, 1, 1, 1)

        self.labelSize = Gui_ElideLabel(TaskHoleParameters)
        self.labelSize.setObjectName(u"labelSize")
        sizePolicy1.setHeightForWidth(self.labelSize.sizePolicy().hasHeightForWidth())
        self.labelSize.setSizePolicy(sizePolicy1)

        self.profileLayout.addWidget(self.labelSize, 1, 0, 1, 1)

        self.ThreadSize = QComboBox(TaskHoleParameters)
        self.ThreadSize.setObjectName(u"ThreadSize")
        sizePolicy2.setHeightForWidth(self.ThreadSize.sizePolicy().hasHeightForWidth())
        self.ThreadSize.setSizePolicy(sizePolicy2)

        self.profileLayout.addWidget(self.ThreadSize, 1, 1, 1, 1)

        self.HoleType = QComboBox(TaskHoleParameters)
        self.HoleType.addItem("")
        self.HoleType.addItem("")
        self.HoleType.addItem("")
        self.HoleType.setObjectName(u"HoleType")

        self.profileLayout.addWidget(self.HoleType, 2, 1, 1, 1)

        self.labelHoleType = Gui_ElideLabel(TaskHoleParameters)
        self.labelHoleType.setObjectName(u"labelHoleType")

        self.profileLayout.addWidget(self.labelHoleType, 2, 0, 1, 1)

        self.profileLayout.setColumnStretch(0, 2)
        self.profileLayout.setColumnStretch(1, 5)

        self.verticalLayout_2.addLayout(self.profileLayout)

        self.ClearanceWidget = QWidget(TaskHoleParameters)
        self.ClearanceWidget.setObjectName(u"ClearanceWidget")
        sizePolicy6.setHeightForWidth(self.ClearanceWidget.sizePolicy().hasHeightForWidth())
        self.ClearanceWidget.setSizePolicy(sizePolicy6)
        self.horizontalLayout_6 = QHBoxLayout(self.ClearanceWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.labelThreadClearance = Gui_ElideLabel(self.ClearanceWidget)
        self.labelThreadClearance.setObjectName(u"labelThreadClearance")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.labelThreadClearance.sizePolicy().hasHeightForWidth())
        self.labelThreadClearance.setSizePolicy(sizePolicy8)

        self.horizontalLayout_6.addWidget(self.labelThreadClearance)

        self.ThreadFit = QComboBox(self.ClearanceWidget)
        self.ThreadFit.addItem("")
        self.ThreadFit.addItem("")
        self.ThreadFit.addItem("")
        self.ThreadFit.setObjectName(u"ThreadFit")
        sizePolicy6.setHeightForWidth(self.ThreadFit.sizePolicy().hasHeightForWidth())
        self.ThreadFit.setSizePolicy(sizePolicy6)

        self.horizontalLayout_6.addWidget(self.ThreadFit)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 5)

        self.verticalLayout_2.addWidget(self.ClearanceWidget)

        self.ThreadGroupBox = QGroupBox(TaskHoleParameters)
        self.ThreadGroupBox.setObjectName(u"ThreadGroupBox")
        sizePolicy8.setHeightForWidth(self.ThreadGroupBox.sizePolicy().hasHeightForWidth())
        self.ThreadGroupBox.setSizePolicy(sizePolicy8)
        self.ThreadGroupBox.setAutoFillBackground(False)
        self.ThreadGroupBox.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.ThreadGroupBox)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.UpdateView = Gui_ElideCheckBox(self.ThreadGroupBox)
        self.UpdateView.setObjectName(u"UpdateView")
        self.UpdateView.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.UpdateView.sizePolicy().hasHeightForWidth())
        self.UpdateView.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.UpdateView)

        self.classLayout = QGridLayout()
        self.classLayout.setObjectName(u"classLayout")
        self.classLayout.setContentsMargins(-1, 0, -1, -1)
        self.ThreadClass = QComboBox(self.ThreadGroupBox)
        self.ThreadClass.setObjectName(u"ThreadClass")
        sizePolicy2.setHeightForWidth(self.ThreadClass.sizePolicy().hasHeightForWidth())
        self.ThreadClass.setSizePolicy(sizePolicy2)

        self.classLayout.addWidget(self.ThreadClass, 0, 1, 1, 1)

        self.labelThreadClass = Gui_ElideLabel(self.ThreadGroupBox)
        self.labelThreadClass.setObjectName(u"labelThreadClass")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.labelThreadClass.sizePolicy().hasHeightForWidth())
        self.labelThreadClass.setSizePolicy(sizePolicy9)

        self.classLayout.addWidget(self.labelThreadClass, 0, 0, 1, 1)

        self.classLayout.setColumnStretch(0, 2)
        self.classLayout.setColumnStretch(1, 5)

        self.verticalLayout_3.addLayout(self.classLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.labelThreadDirection = QLabel(self.ThreadGroupBox)
        self.labelThreadDirection.setObjectName(u"labelThreadDirection")
        sizePolicy9.setHeightForWidth(self.labelThreadDirection.sizePolicy().hasHeightForWidth())
        self.labelThreadDirection.setSizePolicy(sizePolicy9)
        self.labelThreadDirection.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.labelThreadDirection)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.directionRightHand = QRadioButton(self.ThreadGroupBox)
        self.directionButtonGroup = QButtonGroup(TaskHoleParameters)
        self.directionButtonGroup.setObjectName(u"directionButtonGroup")
        self.directionButtonGroup.addButton(self.directionRightHand)
        self.directionRightHand.setObjectName(u"directionRightHand")
        sizePolicy2.setHeightForWidth(self.directionRightHand.sizePolicy().hasHeightForWidth())
        self.directionRightHand.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.directionRightHand)

        self.directionLeftHand = QRadioButton(self.ThreadGroupBox)
        self.directionButtonGroup.addButton(self.directionLeftHand)
        self.directionLeftHand.setObjectName(u"directionLeftHand")
        sizePolicy2.setHeightForWidth(self.directionLeftHand.sizePolicy().hasHeightForWidth())
        self.directionLeftHand.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.directionLeftHand)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.ThreadDepthWidget = QWidget(self.ThreadGroupBox)
        self.ThreadDepthWidget.setObjectName(u"ThreadDepthWidget")
        sizePolicy8.setHeightForWidth(self.ThreadDepthWidget.sizePolicy().hasHeightForWidth())
        self.ThreadDepthWidget.setSizePolicy(sizePolicy8)
        self.verticalLayout_7 = QVBoxLayout(self.ThreadDepthWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.depthTypeLayout = QHBoxLayout()
        self.depthTypeLayout.setSpacing(6)
        self.depthTypeLayout.setObjectName(u"depthTypeLayout")
        self.depthTypeLayout.setContentsMargins(-1, 0, -1, -1)
        self.labelThreadDepthType = Gui_ElideLabel(self.ThreadDepthWidget)
        self.labelThreadDepthType.setObjectName(u"labelThreadDepthType")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.labelThreadDepthType.sizePolicy().hasHeightForWidth())
        self.labelThreadDepthType.setSizePolicy(sizePolicy10)

        self.depthTypeLayout.addWidget(self.labelThreadDepthType)

        self.ThreadDepthType = QComboBox(self.ThreadDepthWidget)
        self.ThreadDepthType.addItem("")
        self.ThreadDepthType.addItem("")
        self.ThreadDepthType.addItem("")
        self.ThreadDepthType.setObjectName(u"ThreadDepthType")
        sizePolicy2.setHeightForWidth(self.ThreadDepthType.sizePolicy().hasHeightForWidth())
        self.ThreadDepthType.setSizePolicy(sizePolicy2)

        self.depthTypeLayout.addWidget(self.ThreadDepthType)


        self.verticalLayout_7.addLayout(self.depthTypeLayout)

        self.ThreadDepthDimensionWidget = QWidget(self.ThreadDepthWidget)
        self.ThreadDepthDimensionWidget.setObjectName(u"ThreadDepthDimensionWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.ThreadDepthDimensionWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelThreadDepth = QLabel(self.ThreadDepthDimensionWidget)
        self.labelThreadDepth.setObjectName(u"labelThreadDepth")

        self.horizontalLayout_3.addWidget(self.labelThreadDepth)

        self.ThreadDepth = Gui_PrefQuantitySpinBox(self.ThreadDepthDimensionWidget)
        self.ThreadDepth.setObjectName(u"ThreadDepth")
        sizePolicy6.setHeightForWidth(self.ThreadDepth.sizePolicy().hasHeightForWidth())
        self.ThreadDepth.setSizePolicy(sizePolicy6)
        self.ThreadDepth.setKeyboardTracking(False)
        self.ThreadDepth.setProperty(u"unit", u"mm")

        self.horizontalLayout_3.addWidget(self.ThreadDepth)


        self.verticalLayout_7.addWidget(self.ThreadDepthDimensionWidget)


        self.verticalLayout_3.addWidget(self.ThreadDepthWidget)

        self.CustomClearanceWidget = QWidget(self.ThreadGroupBox)
        self.CustomClearanceWidget.setObjectName(u"CustomClearanceWidget")
        self.horizontalLayout_13 = QHBoxLayout(self.CustomClearanceWidget)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.UseCustomThreadClearance = Gui_ElideCheckBox(self.CustomClearanceWidget)
        self.UseCustomThreadClearance.setObjectName(u"UseCustomThreadClearance")
        sizePolicy2.setHeightForWidth(self.UseCustomThreadClearance.sizePolicy().hasHeightForWidth())
        self.UseCustomThreadClearance.setSizePolicy(sizePolicy2)
        self.UseCustomThreadClearance.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_13.addWidget(self.UseCustomThreadClearance)

        self.CustomThreadClearance = Gui_PrefQuantitySpinBox(self.CustomClearanceWidget)
        self.CustomThreadClearance.setObjectName(u"CustomThreadClearance")
        sizePolicy4.setHeightForWidth(self.CustomThreadClearance.sizePolicy().hasHeightForWidth())
        self.CustomThreadClearance.setSizePolicy(sizePolicy4)
        self.CustomThreadClearance.setKeyboardTracking(False)
        self.CustomThreadClearance.setSingleStep(0.100000000000000)
        self.CustomThreadClearance.setProperty(u"unit", u"mm")

        self.horizontalLayout_13.addWidget(self.CustomThreadClearance)


        self.verticalLayout_3.addWidget(self.CustomClearanceWidget)


        self.verticalLayout_2.addWidget(self.ThreadGroupBox)


        self.retranslateUi(TaskHoleParameters)

        QMetaObject.connectSlotsByName(TaskHoleParameters)
    # setupUi

    def retranslateUi(self, TaskHoleParameters):
        TaskHoleParameters.setWindowTitle(QCoreApplication.translate("TaskHoleParameters", u"Hole Parameters", None))
        self.labelProfileType.setText(QCoreApplication.translate("TaskHoleParameters", u"Base profile types", None))
        self.BaseProfileType.setItemText(0, QCoreApplication.translate("TaskHoleParameters", u"Circles and arcs", None))
        self.BaseProfileType.setItemText(1, QCoreApplication.translate("TaskHoleParameters", u"Points, circles and arcs", None))
        self.BaseProfileType.setItemText(2, QCoreApplication.translate("TaskHoleParameters", u"Points", None))

        self.labelHeadType.setText(QCoreApplication.translate("TaskHoleParameters", u"Head type", None))
        self.DepthType.setItemText(0, QCoreApplication.translate("TaskHoleParameters", u"Dimension", None))
        self.DepthType.setItemText(1, QCoreApplication.translate("TaskHoleParameters", u"Through all", None))

        self.labelDepthType.setText(QCoreApplication.translate("TaskHoleParameters", u"Depth type", None))
#if QT_CONFIG(tooltip)
        self.HoleCutType.setToolTip(QCoreApplication.translate("TaskHoleParameters", u"Cut type for screw heads", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.HoleCutCustomValues.setToolTip(QCoreApplication.translate("TaskHoleParameters", u"Check to override the values predefined by the 'Type'", None))
#endif // QT_CONFIG(tooltip)
        self.HoleCutCustomValues.setText(QCoreApplication.translate("TaskHoleParameters", u"Custom head values", None))
        self.labelHoleCutDiameter.setText(QCoreApplication.translate("TaskHoleParameters", u"Head diameter", None))
        self.labelHoleCutDepth.setText(QCoreApplication.translate("TaskHoleParameters", u"Head depth", None))
#if QT_CONFIG(tooltip)
        self.HoleCutDepth.setToolTip(QCoreApplication.translate("TaskHoleParameters", u"For countersinks this is the depth of\n"
"the screw's top below the surface", None))
#endif // QT_CONFIG(tooltip)
        self.DrillPointAngled.setText(QCoreApplication.translate("TaskHoleParameters", u"Drill angle", None))
#if QT_CONFIG(tooltip)
        self.DrillForDepth.setToolTip(QCoreApplication.translate("TaskHoleParameters", u"The size of the drill point will be taken into\n"
"account for the depth of blind holes", None))
#endif // QT_CONFIG(tooltip)
        self.DrillForDepth.setText(QCoreApplication.translate("TaskHoleParameters", u"Include in depth", None))
        self.labelHoleCutCountersinkAngle.setText(QCoreApplication.translate("TaskHoleParameters", u"Countersink angle", None))
        self.labelDepth.setText(QCoreApplication.translate("TaskHoleParameters", u"Depth", None))
        self.labelDiameter.setText(QCoreApplication.translate("TaskHoleParameters", u"Diameter", None))
#if QT_CONFIG(tooltip)
        self.Diameter.setToolTip(QCoreApplication.translate("TaskHoleParameters", u"Hole diameter", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Reversed.setToolTip(QCoreApplication.translate("TaskHoleParameters", u"Reverses the hole direction", None))
#endif // QT_CONFIG(tooltip)
        self.Reversed.setText(QCoreApplication.translate("TaskHoleParameters", u"Switch direction", None))
        self.Tapered.setText(QCoreApplication.translate("TaskHoleParameters", u"Tapered", None))
#if QT_CONFIG(tooltip)
        self.TaperedAngle.setToolTip(QCoreApplication.translate("TaskHoleParameters", u"Taper angle for the hole\n"
"90 degree: straight hole\n"
"under 90: smaller hole radius at the bottom\n"
"over 90: larger hole radius at the bottom", None))
#endif // QT_CONFIG(tooltip)
        self.labelThreadType.setText(QCoreApplication.translate("TaskHoleParameters", u"Standard", None))
        self.labelSize.setText(QCoreApplication.translate("TaskHoleParameters", u"Size", None))
        self.HoleType.setItemText(0, QCoreApplication.translate("TaskHoleParameters", u"Clearance / Passthrough", None))
        self.HoleType.setItemText(1, QCoreApplication.translate("TaskHoleParameters", u"Tap drill (to be threaded)", None))
        self.HoleType.setItemText(2, QCoreApplication.translate("TaskHoleParameters", u"Modeled thread", None))

        self.labelHoleType.setText(QCoreApplication.translate("TaskHoleParameters", u"Hole type", None))
        self.labelThreadClearance.setText(QCoreApplication.translate("TaskHoleParameters", u"Clearance", None))
        self.ThreadFit.setItemText(0, QCoreApplication.translate("TaskHoleParameters", u"Standard", None))
        self.ThreadFit.setItemText(1, QCoreApplication.translate("TaskHoleParameters", u"Close", None))
        self.ThreadFit.setItemText(2, QCoreApplication.translate("TaskHoleParameters", u"Wide", None))

#if QT_CONFIG(tooltip)
        self.ThreadFit.setToolTip(QCoreApplication.translate("TaskHoleParameters", u"Hole clearance\n"
"Only available for holes without thread", None))
#endif // QT_CONFIG(tooltip)
        self.ThreadGroupBox.setTitle("")
#if QT_CONFIG(tooltip)
        self.UpdateView.setToolTip(QCoreApplication.translate("TaskHoleParameters", u"Live update of changes to the thread\n"
"Note that the calculation can take some time", None))
#endif // QT_CONFIG(tooltip)
        self.UpdateView.setText(QCoreApplication.translate("TaskHoleParameters", u"Update thread view", None))
#if QT_CONFIG(tooltip)
        self.ThreadClass.setToolTip(QCoreApplication.translate("TaskHoleParameters", u"Tolerance class for threaded holes according to hole profile", None))
#endif // QT_CONFIG(tooltip)
        self.labelThreadClass.setText(QCoreApplication.translate("TaskHoleParameters", u"Class", None))
        self.labelThreadDirection.setText(QCoreApplication.translate("TaskHoleParameters", u"Direction", None))
#if QT_CONFIG(tooltip)
        self.directionRightHand.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.directionRightHand.setText(QCoreApplication.translate("TaskHoleParameters", u"&Right hand", None))
        self.directionLeftHand.setText(QCoreApplication.translate("TaskHoleParameters", u"&Left hand", None))
        self.labelThreadDepthType.setText(QCoreApplication.translate("TaskHoleParameters", u"Thread Depth Type", None))
        self.ThreadDepthType.setItemText(0, QCoreApplication.translate("TaskHoleParameters", u"Hole depth", None))
        self.ThreadDepthType.setItemText(1, QCoreApplication.translate("TaskHoleParameters", u"Dimension", None))
        self.ThreadDepthType.setItemText(2, QCoreApplication.translate("TaskHoleParameters", u"Tapped (DIN76)", None))

        self.labelThreadDepth.setText(QCoreApplication.translate("TaskHoleParameters", u"Thread Depth", None))
#if QT_CONFIG(tooltip)
        self.UseCustomThreadClearance.setToolTip(QCoreApplication.translate("TaskHoleParameters", u"Customize thread clearance", None))
#endif // QT_CONFIG(tooltip)
        self.UseCustomThreadClearance.setText(QCoreApplication.translate("TaskHoleParameters", u"Custom Clearance", None))
#if QT_CONFIG(tooltip)
        self.CustomThreadClearance.setToolTip(QCoreApplication.translate("TaskHoleParameters", u"Custom Thread clearance value", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

