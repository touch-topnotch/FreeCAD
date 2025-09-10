# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsNavigation.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsNavigation(object):
    def setupUi(self, Gui__Dialog__DlgSettingsNavigation):
        if not Gui__Dialog__DlgSettingsNavigation.objectName():
            Gui__Dialog__DlgSettingsNavigation.setObjectName(u"Gui__Dialog__DlgSettingsNavigation")
        Gui__Dialog__DlgSettingsNavigation.resize(548, 795)
        self.verticalLayout = QVBoxLayout(Gui__Dialog__DlgSettingsNavigation)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxNaviCube = QGroupBox(Gui__Dialog__DlgSettingsNavigation)
        self.groupBoxNaviCube.setObjectName(u"groupBoxNaviCube")
        self.groupBoxNaviCube.setCheckable(True)
        self.gridLayout_2 = QGridLayout(self.groupBoxNaviCube)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stepLabel = QLabel(self.groupBoxNaviCube)
        self.stepLabel.setObjectName(u"stepLabel")

        self.gridLayout_2.addWidget(self.stepLabel, 0, 0, 1, 1)

        self.prefStepByTurn = Gui_PrefSpinBox(self.groupBoxNaviCube)
        self.prefStepByTurn.setObjectName(u"prefStepByTurn")
        self.prefStepByTurn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.prefStepByTurn.setMinimum(4)
        self.prefStepByTurn.setMaximum(36)
        self.prefStepByTurn.setValue(8)
        self.prefStepByTurn.setProperty(u"prefEntry", u"NaviStepByTurn")
        self.prefStepByTurn.setProperty(u"prefPath", u"NaviCube")

        self.gridLayout_2.addWidget(self.prefStepByTurn, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.cornerLabel = QLabel(self.groupBoxNaviCube)
        self.cornerLabel.setObjectName(u"cornerLabel")

        self.gridLayout_2.addWidget(self.cornerLabel, 0, 3, 1, 1)

        self.naviCubeCorner = Gui_PrefComboBox(self.groupBoxNaviCube)
        self.naviCubeCorner.addItem("")
        self.naviCubeCorner.addItem("")
        self.naviCubeCorner.addItem("")
        self.naviCubeCorner.addItem("")
        self.naviCubeCorner.setObjectName(u"naviCubeCorner")
        self.naviCubeCorner.setProperty(u"prefEntry", u"CornerNaviCube")
        self.naviCubeCorner.setProperty(u"prefPath", u"NaviCube")

        self.gridLayout_2.addWidget(self.naviCubeCorner, 0, 4, 1, 1)

        self.naviCubeToNearest = Gui_PrefCheckBox(self.groupBoxNaviCube)
        self.naviCubeToNearest.setObjectName(u"naviCubeToNearest")
        self.naviCubeToNearest.setChecked(True)
        self.naviCubeToNearest.setProperty(u"prefEntry", u"NaviRotateToNearest")
        self.naviCubeToNearest.setProperty(u"prefPath", u"NaviCube")

        self.gridLayout_2.addWidget(self.naviCubeToNearest, 1, 0, 1, 2)

        self.FontNameLabel = QLabel(self.groupBoxNaviCube)
        self.FontNameLabel.setObjectName(u"FontNameLabel")

        self.gridLayout_2.addWidget(self.FontNameLabel, 1, 3, 1, 1)

        self.naviCubeFontName = Gui_PrefComboBox(self.groupBoxNaviCube)
        self.naviCubeFontName.addItem("")
        self.naviCubeFontName.setObjectName(u"naviCubeFontName")
        self.naviCubeFontName.setMaximumSize(QSize(240, 16777215))
        self.naviCubeFontName.setProperty(u"prefEntry", u"FontString")
        self.naviCubeFontName.setProperty(u"prefPath", u"NaviCube")

        self.gridLayout_2.addWidget(self.naviCubeFontName, 1, 4, 1, 1)

        self.CubeSizeLabel = QLabel(self.groupBoxNaviCube)
        self.CubeSizeLabel.setObjectName(u"CubeSizeLabel")

        self.gridLayout_2.addWidget(self.CubeSizeLabel, 2, 0, 1, 1)

        self.prefCubeSize = Gui_PrefSpinBox(self.groupBoxNaviCube)
        self.prefCubeSize.setObjectName(u"prefCubeSize")
        self.prefCubeSize.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.prefCubeSize.setSuffix(u" px")
        self.prefCubeSize.setMinimum(10)
        self.prefCubeSize.setMaximum(1024)
        self.prefCubeSize.setSingleStep(10)
        self.prefCubeSize.setValue(132)
        self.prefCubeSize.setProperty(u"prefEntry", u"CubeSize")
        self.prefCubeSize.setProperty(u"prefPath", u"NaviCube")

        self.gridLayout_2.addWidget(self.prefCubeSize, 2, 1, 1, 1)

        self.inactiveOpacityLabel = QLabel(self.groupBoxNaviCube)
        self.inactiveOpacityLabel.setObjectName(u"inactiveOpacityLabel")
        self.inactiveOpacityLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.inactiveOpacityLabel, 2, 3, 1, 1)

        self.naviCubeInactiveOpacity = Gui_PrefSpinBox(self.groupBoxNaviCube)
        self.naviCubeInactiveOpacity.setObjectName(u"naviCubeInactiveOpacity")
        self.naviCubeInactiveOpacity.setMaximumSize(QSize(60, 16777215))
        self.naviCubeInactiveOpacity.setSuffix(u"%")
        self.naviCubeInactiveOpacity.setMinimum(1)
        self.naviCubeInactiveOpacity.setMaximum(100)
        self.naviCubeInactiveOpacity.setValue(50)
        self.naviCubeInactiveOpacity.setProperty(u"prefEntry", u"InactiveOpacity")
        self.naviCubeInactiveOpacity.setProperty(u"prefPath", u"NaviCube")

        self.gridLayout_2.addWidget(self.naviCubeInactiveOpacity, 2, 4, 1, 1)

        self.BaseColorLabel = QLabel(self.groupBoxNaviCube)
        self.BaseColorLabel.setObjectName(u"BaseColorLabel")

        self.gridLayout_2.addWidget(self.BaseColorLabel, 3, 0, 1, 1)

        self.naviCubeBaseColor = Gui_PrefColorButton(self.groupBoxNaviCube)
        self.naviCubeBaseColor.setObjectName(u"naviCubeBaseColor")
        self.naviCubeBaseColor.setColor(QColor(226, 232, 239, 128))
        self.naviCubeBaseColor.setProperty(u"prefEntry", u"BaseColor")
        self.naviCubeBaseColor.setProperty(u"prefPath", u"NaviCube")

        self.gridLayout_2.addWidget(self.naviCubeBaseColor, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBoxNaviCube)

        self.groupBoxRotationCenter = QGroupBox(Gui__Dialog__DlgSettingsNavigation)
        self.groupBoxRotationCenter.setObjectName(u"groupBoxRotationCenter")
        self.groupBoxRotationCenter.setCheckable(True)
        self.gridLayout_3 = QGridLayout(self.groupBoxRotationCenter)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sizeLabelRotationCenter = QLabel(self.groupBoxRotationCenter)
        self.sizeLabelRotationCenter.setObjectName(u"sizeLabelRotationCenter")

        self.gridLayout_3.addWidget(self.sizeLabelRotationCenter, 0, 0, 1, 1)

        self.colorLabelRotationCenter = QLabel(self.groupBoxRotationCenter)
        self.colorLabelRotationCenter.setObjectName(u"colorLabelRotationCenter")

        self.gridLayout_3.addWidget(self.colorLabelRotationCenter, 1, 0, 1, 1)

        self.rotationCenterSize = Gui_PrefDoubleSpinBox(self.groupBoxRotationCenter)
        self.rotationCenterSize.setObjectName(u"rotationCenterSize")
        self.rotationCenterSize.setMaximumSize(QSize(60, 16777215))
        self.rotationCenterSize.setDecimals(1)
        self.rotationCenterSize.setMinimum(1.000000000000000)
        self.rotationCenterSize.setMaximum(100.000000000000000)
        self.rotationCenterSize.setSingleStep(0.500000000000000)
        self.rotationCenterSize.setValue(5.000000000000000)
        self.rotationCenterSize.setProperty(u"prefEntry", u"RotationCenterSize")
        self.rotationCenterSize.setProperty(u"prefPath", u"View")

        self.gridLayout_3.addWidget(self.rotationCenterSize, 0, 1, 1, 1)

        self.rotationCenterColor = Gui_PrefColorButton(self.groupBoxRotationCenter)
        self.rotationCenterColor.setObjectName(u"rotationCenterColor")
        self.rotationCenterColor.setColor(QColor(255, 0, 0, 51))
        self.rotationCenterColor.setProperty(u"prefEntry", u"RotationCenterColor")
        self.rotationCenterColor.setProperty(u"prefPath", u"View")

        self.gridLayout_3.addWidget(self.rotationCenterColor, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBoxRotationCenter)

        self.GroupBox12 = QGroupBox(Gui__Dialog__DlgSettingsNavigation)
        self.GroupBox12.setObjectName(u"GroupBox12")
        self.GroupBox12.setEnabled(True)
        self.gridLayout = QGridLayout(self.GroupBox12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.navigationLabel = QLabel(self.GroupBox12)
        self.navigationLabel.setObjectName(u"navigationLabel")

        self.gridLayout.addWidget(self.navigationLabel, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.mouseButton = QPushButton(self.GroupBox12)
        self.mouseButton.setObjectName(u"mouseButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mouseButton.sizePolicy().hasHeightForWidth())
        self.mouseButton.setSizePolicy(sizePolicy)
        self.mouseButton.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_2.addWidget(self.mouseButton)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.comboNavigationStyle = QComboBox(self.GroupBox12)
        self.comboNavigationStyle.setObjectName(u"comboNavigationStyle")
        self.comboNavigationStyle.setMinimumSize(QSize(120, 0))
        self.comboNavigationStyle.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.comboNavigationStyle, 0, 2, 1, 1)

        self.orbitLabel = QLabel(self.GroupBox12)
        self.orbitLabel.setObjectName(u"orbitLabel")

        self.gridLayout.addWidget(self.orbitLabel, 1, 0, 1, 1)

        self.comboOrbitStyle = QComboBox(self.GroupBox12)
        self.comboOrbitStyle.addItem("")
        self.comboOrbitStyle.addItem("")
        self.comboOrbitStyle.addItem("")
        self.comboOrbitStyle.addItem("")
        self.comboOrbitStyle.addItem("")
        self.comboOrbitStyle.setObjectName(u"comboOrbitStyle")
        self.comboOrbitStyle.setMinimumSize(QSize(120, 0))
        self.comboOrbitStyle.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.comboOrbitStyle, 1, 2, 1, 1)

        self.labelRotationMode = QLabel(self.GroupBox12)
        self.labelRotationMode.setObjectName(u"labelRotationMode")

        self.gridLayout.addWidget(self.labelRotationMode, 2, 0, 1, 1)

        self.comboRotationMode = QComboBox(self.GroupBox12)
        self.comboRotationMode.addItem("")
        self.comboRotationMode.addItem("")
        self.comboRotationMode.addItem("")
        self.comboRotationMode.setObjectName(u"comboRotationMode")
        self.comboRotationMode.setMinimumSize(QSize(120, 0))
        self.comboRotationMode.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.comboRotationMode, 2, 2, 1, 1)

        self.newDocViewLabel = QLabel(self.GroupBox12)
        self.newDocViewLabel.setObjectName(u"newDocViewLabel")

        self.gridLayout.addWidget(self.newDocViewLabel, 3, 0, 1, 1)

        self.comboNewDocView = QComboBox(self.GroupBox12)
        self.comboNewDocView.setObjectName(u"comboNewDocView")
        self.comboNewDocView.setMinimumSize(QSize(120, 0))
        self.comboNewDocView.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.comboNewDocView, 3, 2, 1, 1)

        self.label_2 = QLabel(self.GroupBox12)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.qspinNewDocScale = Gui_PrefUnitSpinBox(self.GroupBox12)
        self.qspinNewDocScale.setObjectName(u"qspinNewDocScale")
        self.qspinNewDocScale.setProperty(u"unit", u"mm")
        self.qspinNewDocScale.setMinimum(0.000010000000000)
        self.qspinNewDocScale.setMaximum(10000000.000000000000000)
        self.qspinNewDocScale.setProperty(u"rawValue", 100.000000000000000)
        self.qspinNewDocScale.setProperty(u"prefEntry", u"NewDocumentCameraScale")
        self.qspinNewDocScale.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.qspinNewDocScale, 4, 2, 1, 1)

        self.checkBoxZoomAtCursor = Gui_PrefCheckBox(self.GroupBox12)
        self.checkBoxZoomAtCursor.setObjectName(u"checkBoxZoomAtCursor")
        self.checkBoxZoomAtCursor.setChecked(True)
        self.checkBoxZoomAtCursor.setProperty(u"prefEntry", u"ZoomAtCursor")
        self.checkBoxZoomAtCursor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.checkBoxZoomAtCursor, 6, 0, 1, 1)

        self.label = QLabel(self.GroupBox12)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 6, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spinBoxZoomStep = Gui_PrefDoubleSpinBox(self.GroupBox12)
        self.spinBoxZoomStep.setObjectName(u"spinBoxZoomStep")
        self.spinBoxZoomStep.setMaximumSize(QSize(60, 16777215))
        self.spinBoxZoomStep.setMinimum(0.010000000000000)
        self.spinBoxZoomStep.setMaximum(1.000000000000000)
        self.spinBoxZoomStep.setSingleStep(0.050000000000000)
        self.spinBoxZoomStep.setValue(0.200000000000000)
        self.spinBoxZoomStep.setProperty(u"prefEntry", u"ZoomStep")
        self.spinBoxZoomStep.setProperty(u"prefPath", u"View")

        self.horizontalLayout.addWidget(self.spinBoxZoomStep)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 2, 1, 1)

        self.checkBoxInvertZoom = Gui_PrefCheckBox(self.GroupBox12)
        self.checkBoxInvertZoom.setObjectName(u"checkBoxInvertZoom")
        self.checkBoxInvertZoom.setChecked(True)
        self.checkBoxInvertZoom.setProperty(u"prefEntry", u"InvertZoom")
        self.checkBoxInvertZoom.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.checkBoxInvertZoom, 7, 0, 1, 1)

        self.checkBoxDisableTilt = Gui_PrefCheckBox(self.GroupBox12)
        self.checkBoxDisableTilt.setObjectName(u"checkBoxDisableTilt")
        self.checkBoxDisableTilt.setChecked(True)
        self.checkBoxDisableTilt.setProperty(u"prefEntry", u"DisableTouchTilt")
        self.checkBoxDisableTilt.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.checkBoxDisableTilt, 8, 0, 1, 1)


        self.verticalLayout.addWidget(self.GroupBox12)

        self.spaceMouseDevice = QGroupBox(Gui__Dialog__DlgSettingsNavigation)
        self.spaceMouseDevice.setObjectName(u"spaceMouseDevice")
        self.gridLayout_5 = QGridLayout(self.spaceMouseDevice)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.legacySpaceMouseDevices = Gui_PrefCheckBox(self.spaceMouseDevice)
        self.legacySpaceMouseDevices.setObjectName(u"legacySpaceMouseDevices")
        self.legacySpaceMouseDevices.setProperty(u"prefEntry", u"LegacySpaceMouseDevices")
        self.legacySpaceMouseDevices.setProperty(u"prefPath", u"View")

        self.gridLayout_5.addWidget(self.legacySpaceMouseDevices, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.spaceMouseDevice)

        self.groupBoxAnimations = QGroupBox(Gui__Dialog__DlgSettingsNavigation)
        self.groupBoxAnimations.setObjectName(u"groupBoxAnimations")
        self.groupBoxAnimations.setCheckable(True)
        self.gridLayout_4 = QGridLayout(self.groupBoxAnimations)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.animationDurationLabel = QLabel(self.groupBoxAnimations)
        self.animationDurationLabel.setObjectName(u"animationDurationLabel")
        self.animationDurationLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.animationDurationLabel, 1, 0, 1, 1)

        self.checkBoxSpinningAnimations = Gui_PrefCheckBox(self.groupBoxAnimations)
        self.checkBoxSpinningAnimations.setObjectName(u"checkBoxSpinningAnimations")
        self.checkBoxSpinningAnimations.setChecked(False)
        self.checkBoxSpinningAnimations.setProperty(u"prefEntry", u"UseSpinningAnimations")
        self.checkBoxSpinningAnimations.setProperty(u"prefPath", u"View")

        self.gridLayout_4.addWidget(self.checkBoxSpinningAnimations, 2, 0, 1, 1)

        self.spinBoxAnimationDuration = Gui_PrefSpinBox(self.groupBoxAnimations)
        self.spinBoxAnimationDuration.setObjectName(u"spinBoxAnimationDuration")
        self.spinBoxAnimationDuration.setMaximumSize(QSize(60, 16777215))
        self.spinBoxAnimationDuration.setSuffix(u" ms")
        self.spinBoxAnimationDuration.setMinimum(100)
        self.spinBoxAnimationDuration.setMaximum(10000)
        self.spinBoxAnimationDuration.setSingleStep(50)
        self.spinBoxAnimationDuration.setValue(500)
        self.spinBoxAnimationDuration.setProperty(u"prefEntry", u"AnimationDuration")
        self.spinBoxAnimationDuration.setProperty(u"prefPath", u"View")

        self.gridLayout_4.addWidget(self.spinBoxAnimationDuration, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBoxAnimations)

        self.verticalSpacer = QSpacerItem(20, 96, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Gui__Dialog__DlgSettingsNavigation)

        self.naviCubeCorner.setCurrentIndex(1)
        self.naviCubeFontName.setCurrentIndex(-1)
        self.comboNavigationStyle.setCurrentIndex(-1)
        self.comboOrbitStyle.setCurrentIndex(4)
        self.comboRotationMode.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsNavigation)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsNavigation):
        Gui__Dialog__DlgSettingsNavigation.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Navigation", None))
        self.groupBoxNaviCube.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Navigation cube", None))
        self.stepLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Steps by turn", None))
#if QT_CONFIG(tooltip)
        self.prefStepByTurn.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Number of steps by turn when using arrows (default = 8 : step angle = 360/8 = 45 deg)", None))
#endif // QT_CONFIG(tooltip)
        self.cornerLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Corner", None))
        self.naviCubeCorner.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Top left", None))
        self.naviCubeCorner.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Top right", None))
        self.naviCubeCorner.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Bottom left", None))
        self.naviCubeCorner.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Bottom right", None))

#if QT_CONFIG(tooltip)
        self.naviCubeCorner.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Corner where navigation cube is shown", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.naviCubeToNearest.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Rotates to nearest possible state when clicking a cube face", None))
#endif // QT_CONFIG(tooltip)
        self.naviCubeToNearest.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Rotate to nearest", None))
        self.FontNameLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Font name", None))
        self.naviCubeFontName.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Default", None))

#if QT_CONFIG(tooltip)
        self.naviCubeFontName.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Font name of the navigation cube", None))
#endif // QT_CONFIG(tooltip)
        self.CubeSizeLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Cube size", None))
#if QT_CONFIG(tooltip)
        self.prefCubeSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Size of the navigation cube", None))
#endif // QT_CONFIG(tooltip)
        self.inactiveOpacityLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Opacity when inactive", None))
#if QT_CONFIG(tooltip)
        self.naviCubeInactiveOpacity.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Opacity of the navigation cube when not focused", None))
#endif // QT_CONFIG(tooltip)
        self.BaseColorLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Color", None))
#if QT_CONFIG(tooltip)
        self.naviCubeBaseColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Base color for all elements", None))
#endif // QT_CONFIG(tooltip)
        self.groupBoxRotationCenter.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Rotation center indicator", None))
        self.sizeLabelRotationCenter.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Sphere size", None))
        self.colorLabelRotationCenter.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Color and transparency", None))
#if QT_CONFIG(tooltip)
        self.rotationCenterSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"The size of the rotation center indicator", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.rotationCenterColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"The color of the rotation center indicator", None))
#endif // QT_CONFIG(tooltip)
        self.GroupBox12.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Navigation", None))
        self.navigationLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"3D Navigation", None))
#if QT_CONFIG(tooltip)
        self.mouseButton.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"List the mouse button configs for each chosen navigation setting.\n"
"Select a set and then press the button to view said configurations.", None))
#endif // QT_CONFIG(tooltip)
        self.mouseButton.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Mouse...", None))
#if QT_CONFIG(tooltip)
        self.comboNavigationStyle.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Navigation settings set", None))
#endif // QT_CONFIG(tooltip)
        self.orbitLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Orbit style", None))
        self.comboOrbitStyle.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Turntable", None))
        self.comboOrbitStyle.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Trackball", None))
        self.comboOrbitStyle.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Free Turntable", None))
        self.comboOrbitStyle.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Trackball Classic", None))
        self.comboOrbitStyle.setItemText(4, QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Rounded Arcball", None))

#if QT_CONFIG(tooltip)
        self.comboOrbitStyle.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Rotation orbit style.\n"
"Rounded Arcball: moving the mouse in the corners of the screen will only roll the part.\n"
"Trackball: moving the mouse horizontally will rotate the part around the y-axis.\n"
"Trackball Classic: moving the mouse will rotate the part allowing precession.\n"
"Turntable: the part will be rotated around the z-axis (with constrained axes).\n"
"Free Turntable: the part will be rotated around the z-axis.\n"
"         ", None))
#endif // QT_CONFIG(tooltip)
        self.labelRotationMode.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Rotation mode", None))
        self.comboRotationMode.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Window center", None))
        self.comboRotationMode.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Drag at cursor", None))
        self.comboRotationMode.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Object center", None))

#if QT_CONFIG(tooltip)
        self.comboRotationMode.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Rotations in 3D will use current cursor position as center for rotation", None))
#endif // QT_CONFIG(tooltip)
        self.newDocViewLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Default camera orientation", None))
#if QT_CONFIG(tooltip)
        self.comboNewDocView.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Default camera orientation when creating a new document or selecting the home view", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Camera zoom", None))
#if QT_CONFIG(tooltip)
        self.qspinNewDocScale.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Sets camera zoom for new documents.\n"
"The value is the diameter of the sphere to fit on the screen.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBoxZoomAtCursor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Zoom operations will be performed at position of mouse pointer", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxZoomAtCursor.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Zoom at cursor", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Zoom step", None))
#if QT_CONFIG(tooltip)
        self.spinBoxZoomStep.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"How much will be zoomed.\n"
"Zoom step of '1' means a factor of 7.5 for every zoom step.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBoxInvertZoom.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Direction of zoom operations will be inverted", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxInvertZoom.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Invert zoom", None))
#if QT_CONFIG(tooltip)
        self.checkBoxDisableTilt.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Prevents view tilting when pinch-zooming.\n"
"Affects only gesture navigation style.\n"
"Mouse tilting is not disabled by this setting.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxDisableTilt.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Disable touchscreen tilt gesture", None))
        self.spaceMouseDevice.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Space mouse", None))
        self.legacySpaceMouseDevices.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Enable support of legacy space mouse devices", None))
        self.groupBoxAnimations.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Animations", None))
#if QT_CONFIG(tooltip)
        self.animationDurationLabel.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Duration of navigation animations that have a fixed duration", None))
#endif // QT_CONFIG(tooltip)
        self.animationDurationLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Animation duration", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSpinningAnimations.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Enable spinning animations that are used in some navigation styles after dragging", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSpinningAnimations.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"Enable spinning animations", None))
#if QT_CONFIG(tooltip)
        self.spinBoxAnimationDuration.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNavigation", u"The duration of navigation animations in milliseconds", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

