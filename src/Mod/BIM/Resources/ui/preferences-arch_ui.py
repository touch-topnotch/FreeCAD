# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-arch.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsArch(object):
    def setupUi(self, Gui__Dialog__DlgSettingsArch):
        if not Gui__Dialog__DlgSettingsArch.objectName():
            Gui__Dialog__DlgSettingsArch.setObjectName(u"Gui__Dialog__DlgSettingsArch")
        Gui__Dialog__DlgSettingsArch.resize(519, 954)
        self.verticalLayout_1 = QVBoxLayout(Gui__Dialog__DlgSettingsArch)
        self.verticalLayout_1.setSpacing(6)
        self.verticalLayout_1.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.groupBox_1 = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.gridLayout_1 = QGridLayout(self.groupBox_1)
        self.gridLayout_1.setSpacing(6)
        self.gridLayout_1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.checkBox_autoJoinWalls = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_autoJoinWalls.setObjectName(u"checkBox_autoJoinWalls")
        self.checkBox_autoJoinWalls.setChecked(False)
        self.checkBox_autoJoinWalls.setProperty(u"prefEntry", u"autoJoinWalls")
        self.checkBox_autoJoinWalls.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_1.addWidget(self.checkBox_autoJoinWalls, 0, 0, 1, 3)

        self.checkBox_joinWallSketches = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_joinWallSketches.setObjectName(u"checkBox_joinWallSketches")
        self.checkBox_joinWallSketches.setProperty(u"prefEntry", u"joinWallSketches")
        self.checkBox_joinWallSketches.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_1.addWidget(self.checkBox_joinWallSketches, 1, 0, 1, 3)

        self.checkBox_archRemoveExternal = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_archRemoveExternal.setObjectName(u"checkBox_archRemoveExternal")
        self.checkBox_archRemoveExternal.setProperty(u"prefEntry", u"archRemoveExternal")
        self.checkBox_archRemoveExternal.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_1.addWidget(self.checkBox_archRemoveExternal, 2, 0, 1, 3)

        self.checkBox_UseMaterialColor = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_UseMaterialColor.setObjectName(u"checkBox_UseMaterialColor")
        self.checkBox_UseMaterialColor.setChecked(True)
        self.checkBox_UseMaterialColor.setProperty(u"prefEntry", u"UseMaterialColor")
        self.checkBox_UseMaterialColor.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_1.addWidget(self.checkBox_UseMaterialColor, 3, 0, 1, 3)

        self.checkBox_applyconstructionStyle = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_applyconstructionStyle.setObjectName(u"checkBox_applyconstructionStyle")
        self.checkBox_applyconstructionStyle.setProperty(u"prefEntry", u"applyconstructionStyle")
        self.checkBox_applyconstructionStyle.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_1.addWidget(self.checkBox_applyconstructionStyle, 4, 0, 1, 3)

        self.checkBox_MoveWithHost = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_MoveWithHost.setObjectName(u"checkBox_MoveWithHost")
        self.checkBox_MoveWithHost.setChecked(False)
        self.checkBox_MoveWithHost.setProperty(u"prefEntry", u"MoveWithHost")
        self.checkBox_MoveWithHost.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_1.addWidget(self.checkBox_MoveWithHost, 5, 0, 1, 3)

        self.checkBox_MoveBase = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_MoveBase.setObjectName(u"checkBox_MoveBase")
        self.checkBox_MoveBase.setChecked(False)
        self.checkBox_MoveBase.setProperty(u"prefEntry", u"MoveBase")
        self.checkBox_MoveBase.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_1.addWidget(self.checkBox_MoveBase, 6, 0, 1, 3)

        self.label_MaxComputeAreas = QLabel(self.groupBox_1)
        self.label_MaxComputeAreas.setObjectName(u"label_MaxComputeAreas")

        self.gridLayout_1.addWidget(self.label_MaxComputeAreas, 7, 0, 1, 1)

        self.spinBox_MaxComputeAreas = Gui_PrefSpinBox(self.groupBox_1)
        self.spinBox_MaxComputeAreas.setObjectName(u"spinBox_MaxComputeAreas")
        self.spinBox_MaxComputeAreas.setMinimumSize(QSize(140, 0))
        self.spinBox_MaxComputeAreas.setValue(20)
        self.spinBox_MaxComputeAreas.setProperty(u"prefEntry", u"MaxComputeAreas")
        self.spinBox_MaxComputeAreas.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_1.addWidget(self.spinBox_MaxComputeAreas, 7, 1, 1, 1)

        self.horizontalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_1.addItem(self.horizontalSpacer_1, 7, 2, 1, 1)

        self.label_ReferenceCheckInterval = QLabel(self.groupBox_1)
        self.label_ReferenceCheckInterval.setObjectName(u"label_ReferenceCheckInterval")

        self.gridLayout_1.addWidget(self.label_ReferenceCheckInterval, 8, 0, 1, 1)

        self.spinBox_ReferenceCheckInterval = Gui_PrefSpinBox(self.groupBox_1)
        self.spinBox_ReferenceCheckInterval.setObjectName(u"spinBox_ReferenceCheckInterval")
        self.spinBox_ReferenceCheckInterval.setMinimum(1)
        self.spinBox_ReferenceCheckInterval.setMaximum(9999)
        self.spinBox_ReferenceCheckInterval.setValue(60)
        self.spinBox_ReferenceCheckInterval.setProperty(u"prefEntry", u"ReferenceCheckInterval")
        self.spinBox_ReferenceCheckInterval.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_1.addWidget(self.spinBox_ReferenceCheckInterval, 8, 1, 1, 1)

        self.label_IfcVersion = QLabel(self.groupBox_1)
        self.label_IfcVersion.setObjectName(u"label_IfcVersion")

        self.gridLayout_1.addWidget(self.label_IfcVersion, 9, 0, 1, 1)

        self.comboBox_IfcVersion = Gui_PrefComboBox(self.groupBox_1)
        self.comboBox_IfcVersion.addItem("")
        self.comboBox_IfcVersion.addItem("")
        self.comboBox_IfcVersion.setObjectName(u"comboBox_IfcVersion")
        self.comboBox_IfcVersion.setProperty(u"prefEntry", u"IfcVersion")
        self.comboBox_IfcVersion.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_1.addWidget(self.comboBox_IfcVersion, 9, 1, 1, 1)


        self.verticalLayout_1.addWidget(self.groupBox_1)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_ConversionFast = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_ConversionFast.setObjectName(u"checkBox_ConversionFast")
        self.checkBox_ConversionFast.setChecked(True)
        self.checkBox_ConversionFast.setProperty(u"prefEntry", u"ConversionFast")
        self.checkBox_ConversionFast.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_2.addWidget(self.checkBox_ConversionFast, 0, 0, 1, 3)

        self.checkBox_ConversionFlat = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_ConversionFlat.setObjectName(u"checkBox_ConversionFlat")
        self.checkBox_ConversionFlat.setEnabled(False)
        self.checkBox_ConversionFlat.setProperty(u"prefEntry", u"ConversionFlat")
        self.checkBox_ConversionFlat.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_2.addWidget(self.checkBox_ConversionFlat, 1, 0, 1, 3)

        self.checkBox_ConversionCut = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_ConversionCut.setObjectName(u"checkBox_ConversionCut")
        self.checkBox_ConversionCut.setEnabled(False)
        self.checkBox_ConversionCut.setChecked(True)
        self.checkBox_ConversionCut.setProperty(u"prefEntry", u"ConversionCut")
        self.checkBox_ConversionCut.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_2.addWidget(self.checkBox_ConversionCut, 2, 0, 1, 3)

        self.label_ConversionTolerance = QLabel(self.groupBox_2)
        self.label_ConversionTolerance.setObjectName(u"label_ConversionTolerance")
        self.label_ConversionTolerance.setEnabled(False)

        self.gridLayout_2.addWidget(self.label_ConversionTolerance, 3, 0, 1, 1)

        self.spinBox_ConversionTolerance = Gui_PrefDoubleSpinBox(self.groupBox_2)
        self.spinBox_ConversionTolerance.setObjectName(u"spinBox_ConversionTolerance")
        self.spinBox_ConversionTolerance.setEnabled(False)
        self.spinBox_ConversionTolerance.setMinimumSize(QSize(140, 0))
        self.spinBox_ConversionTolerance.setDecimals(4)
        self.spinBox_ConversionTolerance.setSingleStep(0.000100000000000)
        self.spinBox_ConversionTolerance.setValue(0.001000000000000)
        self.spinBox_ConversionTolerance.setProperty(u"prefEntry", u"ConversionTolerance")
        self.spinBox_ConversionTolerance.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_2.addWidget(self.spinBox_ConversionTolerance, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)


        self.verticalLayout_1.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_ShowVRMDebug = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBox_ShowVRMDebug.setObjectName(u"checkBox_ShowVRMDebug")
        self.checkBox_ShowVRMDebug.setProperty(u"prefEntry", u"ShowVRMDebug")
        self.checkBox_ShowVRMDebug.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_3.addWidget(self.checkBox_ShowVRMDebug, 0, 0, 1, 3)

        self.label_CutLineThickness = QLabel(self.groupBox_3)
        self.label_CutLineThickness.setObjectName(u"label_CutLineThickness")

        self.gridLayout_3.addWidget(self.label_CutLineThickness, 1, 0, 1, 1)

        self.spinBox_CutLineThickness = Gui_PrefDoubleSpinBox(self.groupBox_3)
        self.spinBox_CutLineThickness.setObjectName(u"spinBox_CutLineThickness")
        self.spinBox_CutLineThickness.setValue(2.000000000000000)
        self.spinBox_CutLineThickness.setProperty(u"prefEntry", u"CutLineThickness")
        self.spinBox_CutLineThickness.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_3.addWidget(self.spinBox_CutLineThickness, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.label_SymbolLineThickness = QLabel(self.groupBox_3)
        self.label_SymbolLineThickness.setObjectName(u"label_SymbolLineThickness")

        self.gridLayout_3.addWidget(self.label_SymbolLineThickness, 2, 0, 1, 1)

        self.spinBox_SymbolLineThickness = Gui_PrefDoubleSpinBox(self.groupBox_3)
        self.spinBox_SymbolLineThickness.setObjectName(u"spinBox_SymbolLineThickness")
        self.spinBox_SymbolLineThickness.setValue(0.600000000000000)
        self.spinBox_SymbolLineThickness.setProperty(u"prefEntry", u"SymbolLineThickness")
        self.spinBox_SymbolLineThickness.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_3.addWidget(self.spinBox_SymbolLineThickness, 2, 1, 1, 1)

        self.label_archHiddenPattern = QLabel(self.groupBox_3)
        self.label_archHiddenPattern.setObjectName(u"label_archHiddenPattern")

        self.gridLayout_3.addWidget(self.label_archHiddenPattern, 3, 0, 1, 1)

        self.lineEdit_archHiddenPattern = Gui_PrefLineEdit(self.groupBox_3)
        self.lineEdit_archHiddenPattern.setObjectName(u"lineEdit_archHiddenPattern")
        self.lineEdit_archHiddenPattern.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_archHiddenPattern.setText(u"30, 10")
        self.lineEdit_archHiddenPattern.setProperty(u"prefEntry", u"archHiddenPattern")
        self.lineEdit_archHiddenPattern.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_3.addWidget(self.lineEdit_archHiddenPattern, 3, 1, 1, 1)

        self.label_patternScale = QLabel(self.groupBox_3)
        self.label_patternScale.setObjectName(u"label_patternScale")

        self.gridLayout_3.addWidget(self.label_patternScale, 4, 0, 1, 1)

        self.spinBox_patternScale = Gui_PrefDoubleSpinBox(self.groupBox_3)
        self.spinBox_patternScale.setObjectName(u"spinBox_patternScale")
        self.spinBox_patternScale.setDecimals(4)
        self.spinBox_patternScale.setMaximum(9999.989999999999782)
        self.spinBox_patternScale.setSingleStep(0.001000000000000)
        self.spinBox_patternScale.setValue(0.010000000000000)
        self.spinBox_patternScale.setProperty(u"prefEntry", u"patternScale")
        self.spinBox_patternScale.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_3.addWidget(self.spinBox_patternScale, 4, 1, 1, 1)


        self.verticalLayout_1.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_BimServerUrl = QLabel(self.groupBox_4)
        self.label_BimServerUrl.setObjectName(u"label_BimServerUrl")

        self.gridLayout_4.addWidget(self.label_BimServerUrl, 0, 0, 1, 1)

        self.lineEdit_BimServerUrl = Gui_PrefLineEdit(self.groupBox_4)
        self.lineEdit_BimServerUrl.setObjectName(u"lineEdit_BimServerUrl")
        self.lineEdit_BimServerUrl.setText(u"http://localhost:8082")
        self.lineEdit_BimServerUrl.setProperty(u"prefEntry", u"BimServerUrl")
        self.lineEdit_BimServerUrl.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_4.addWidget(self.lineEdit_BimServerUrl, 0, 1, 1, 1)

        self.checkBox_BimServerBrowser = Gui_PrefCheckBox(self.groupBox_4)
        self.checkBox_BimServerBrowser.setObjectName(u"checkBox_BimServerBrowser")
        self.checkBox_BimServerBrowser.setProperty(u"prefEntry", u"BimServerBrowser")
        self.checkBox_BimServerBrowser.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout_4.addWidget(self.checkBox_BimServerBrowser, 1, 0, 1, 2)


        self.verticalLayout_1.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_surveyUnits = Gui_PrefCheckBox(self.groupBox_5)
        self.checkBox_surveyUnits.setObjectName(u"checkBox_surveyUnits")
        self.checkBox_surveyUnits.setChecked(True)
        self.checkBox_surveyUnits.setProperty(u"prefEntry", u"surveyUnits")
        self.checkBox_surveyUnits.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_2.addWidget(self.checkBox_surveyUnits)


        self.verticalLayout_1.addWidget(self.groupBox_5)

        self.verticalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_1.addItem(self.verticalSpacer_1)


        self.retranslateUi(Gui__Dialog__DlgSettingsArch)
        self.checkBox_ConversionFast.toggled.connect(self.checkBox_ConversionFlat.setDisabled)
        self.checkBox_ConversionFast.toggled.connect(self.checkBox_ConversionCut.setDisabled)
        self.checkBox_ConversionFast.toggled.connect(self.label_ConversionTolerance.setDisabled)
        self.checkBox_ConversionFast.toggled.connect(self.spinBox_ConversionTolerance.setDisabled)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsArch)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsArch):
        Gui__Dialog__DlgSettingsArch.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"General settings", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Object creation", None))
        self.checkBox_autoJoinWalls.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Auto-join walls", None))
#if QT_CONFIG(tooltip)
        self.checkBox_joinWallSketches.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"If this is checked, when 2 similar walls are being connected, their underlying sketches will be joined into one, and the two walls will become one", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_joinWallSketches.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Join base sketches of walls if possible", None))
#if QT_CONFIG(tooltip)
        self.checkBox_archRemoveExternal.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Two possible strategies to avoid circular dependencies: Create one more object (unchecked) or remove external geometry of base sketch (checked)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_archRemoveExternal.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Remove external geometry of base sketches if needed", None))
#if QT_CONFIG(tooltip)
        self.checkBox_UseMaterialColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"If this is checked, when an Arch object has a material, the object will take the color of the material. This can be overridden for each object.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_UseMaterialColor.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Use material color as shape color", None))
#if QT_CONFIG(tooltip)
        self.checkBox_applyconstructionStyle.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"If this is checked, when an object becomes Subtraction or Addition of an Arch object, it will receive the Draft Construction color.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_applyconstructionStyle.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Apply Draft construction style to subcomponents", None))
#if QT_CONFIG(tooltip)
        self.checkBox_MoveWithHost.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"By default, new objects will have their \"Move with host\" property set to False, which means they won't move when their host object is moved.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_MoveWithHost.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Set \"Move with host\" property to True by default", None))
        self.checkBox_MoveBase.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Set \"Move base\" property to True by default", None))
        self.label_MaxComputeAreas.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Do not compute areas for objects with more than", None))
        self.spinBox_MaxComputeAreas.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u" faces", None))
        self.label_ReferenceCheckInterval.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Interval between file checks for references", None))
        self.spinBox_ReferenceCheckInterval.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u" seconds", None))
        self.label_IfcVersion.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"IFC version", None))
        self.comboBox_IfcVersion.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"IFC4", None))
        self.comboBox_IfcVersion.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"IFC2X3", None))

#if QT_CONFIG(tooltip)
        self.comboBox_IfcVersion.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"The IFC version will change which attributes and products are supported", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Mesh to Shape Conversion", None))
#if QT_CONFIG(tooltip)
        self.checkBox_ConversionFast.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"If this is checked, conversion is faster but the result might still contain triangulated faces", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_ConversionFast.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Fast conversion", None))
#if QT_CONFIG(tooltip)
        self.checkBox_ConversionFlat.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"If this is checked, flat groups of faces will be force-flattened, resulting in possible gaps and non-solid results", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_ConversionFlat.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Force flat faces", None))
#if QT_CONFIG(tooltip)
        self.checkBox_ConversionCut.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"If this is checked, holes in faces will be performed by subtraction rather than using wires orientation", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_ConversionCut.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Cut method", None))
        self.label_ConversionTolerance.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Tolerance", None))
#if QT_CONFIG(tooltip)
        self.spinBox_ConversionTolerance.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Tolerance value to use when checking if 2 adjacent faces as planar", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"2D rendering", None))
#if QT_CONFIG(tooltip)
        self.checkBox_ShowVRMDebug.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Show debug information during 2D rendering", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_ShowVRMDebug.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Show renderer debug messages", None))
        self.label_CutLineThickness.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Cut areas line thickness ratio", None))
#if QT_CONFIG(tooltip)
        self.spinBox_CutLineThickness.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Specifies how many times the viewed line thickness must be applied to cut lines", None))
#endif // QT_CONFIG(tooltip)
        self.label_SymbolLineThickness.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Symbol line thickness ratio", None))
        self.label_archHiddenPattern.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Hidden geometry pattern", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_archHiddenPattern.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"This is the SVG stroke-dasharray property to apply\n"
"to projections of hidden objects.", None))
#endif // QT_CONFIG(tooltip)
        self.label_patternScale.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Pattern scale", None))
#if QT_CONFIG(tooltip)
        self.spinBox_patternScale.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Scaling factor for patterns used by objects that have\n"
"a Footprint display mode", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_4.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"BIM server", None))
        self.label_BimServerUrl.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Address", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_BimServerUrl.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"The URL of a BIM server instance (www.bimserver.org) to connect to.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_BimServerBrowser.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"If this is selected, the \"Open BIM Server in browser\"\n"
"button will open the BIM Server interface in an external browser\n"
"instead of the FreeCAD web workbench", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_BimServerBrowser.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Open in external browser", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Survey", None))
#if QT_CONFIG(tooltip)
        self.checkBox_surveyUnits.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"If this is checked, the text that gets placed in the clipboard will include the unit. Otherwise, it will be a simple number expressed in internal units (millimeters)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_surveyUnits.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Include unit when sending measurements to clipboard", None))
    # retranslateUi

