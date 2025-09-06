# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SketcherSettingsDisplay.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SketcherGui_SketcherSettingsDisplay(object):
    def setupUi(self, SketcherGui__SketcherSettingsDisplay):
        if not SketcherGui__SketcherSettingsDisplay.objectName():
            SketcherGui__SketcherSettingsDisplay.setObjectName(u"SketcherGui__SketcherSettingsDisplay")
        SketcherGui__SketcherSettingsDisplay.resize(500, 538)
        self.verticalLayout = QVBoxLayout(SketcherGui__SketcherSettingsDisplay)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_1 = QGroupBox(SketcherGui__SketcherSettingsDisplay)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.gridLayout_1 = QGridLayout(self.groupBox_1)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.checkBoxUseConstraintSymbolSize = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBoxUseConstraintSymbolSize.setObjectName(u"checkBoxUseConstraintSymbolSize")
        self.checkBoxUseConstraintSymbolSize.setChecked(False)
        self.checkBoxUseConstraintSymbolSize.setProperty(u"prefEntry", u"UseConstraintSymbolSize")
        self.checkBoxUseConstraintSymbolSize.setProperty(u"prefPath", u"View")

        self.gridLayout_1.addWidget(self.checkBoxUseConstraintSymbolSize, 1, 0, 1, 1)

        self.ConstraintSymbolSize = Gui_PrefSpinBox(self.groupBox_1)
        self.ConstraintSymbolSize.setObjectName(u"ConstraintSymbolSize")
        self.ConstraintSymbolSize.setMinimum(6)
        self.ConstraintSymbolSize.setMaximum(96)
        self.ConstraintSymbolSize.setValue(15)
        self.ConstraintSymbolSize.setEnabled(False)
        self.ConstraintSymbolSize.setProperty(u"prefEntry", u"ConstraintSymbolSize")
        self.ConstraintSymbolSize.setProperty(u"prefPath", u"View")

        self.gridLayout_1.addWidget(self.ConstraintSymbolSize, 1, 1, 1, 1)

        self.label_1 = QLabel(self.groupBox_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(182, 0))

        self.gridLayout_1.addWidget(self.label_1, 2, 0, 1, 1)

        self.viewScalingFactor = Gui_PrefDoubleSpinBox(self.groupBox_1)
        self.viewScalingFactor.setObjectName(u"viewScalingFactor")
        self.viewScalingFactor.setInputMethodHints(Qt.ImhPreferNumbers)
        self.viewScalingFactor.setDecimals(2)
        self.viewScalingFactor.setMinimum(0.500000000000000)
        self.viewScalingFactor.setMaximum(5.000000000000000)
        self.viewScalingFactor.setSingleStep(0.050000000000000)
        self.viewScalingFactor.setValue(1.000000000000000)
        self.viewScalingFactor.setProperty(u"prefEntry", u"ViewScalingFactor")
        self.viewScalingFactor.setProperty(u"prefPath", u"View")

        self.gridLayout_1.addWidget(self.viewScalingFactor, 2, 1, 1, 1)

        self.SegmentsPerGeometry = Gui_PrefSpinBox(self.groupBox_1)
        self.SegmentsPerGeometry.setObjectName(u"SegmentsPerGeometry")
        self.SegmentsPerGeometry.setMinimum(50)
        self.SegmentsPerGeometry.setMaximum(1000)
        self.SegmentsPerGeometry.setProperty(u"prefEntry", u"SegmentsPerGeometry")
        self.SegmentsPerGeometry.setProperty(u"prefPath", u"View")

        self.gridLayout_1.addWidget(self.SegmentsPerGeometry, 3, 1, 1, 1)

        self.checkBoxShowDimensionalName = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBoxShowDimensionalName.setObjectName(u"checkBoxShowDimensionalName")
        self.checkBoxShowDimensionalName.setProperty(u"prefEntry", u"ShowDimensionalName")
        self.checkBoxShowDimensionalName.setProperty(u"prefPath", u"Mod/Sketcher")
        self.checkBoxShowDimensionalName.setChecked(True)

        self.gridLayout_1.addWidget(self.checkBoxShowDimensionalName, 10, 0, 1, 1)

        self.prefDimensionalStringFormat = Gui_PrefLineEdit(self.groupBox_1)
        self.prefDimensionalStringFormat.setObjectName(u"prefDimensionalStringFormat")
        self.prefDimensionalStringFormat.setText(u"%N = %V")
        self.prefDimensionalStringFormat.setProperty(u"prefEntry", u"DimensionalStringFormat")
        self.prefDimensionalStringFormat.setProperty(u"prefPath", u"Mod/Sketcher")

        self.gridLayout_1.addWidget(self.prefDimensionalStringFormat, 10, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_1.addWidget(self.label_3, 3, 0, 1, 1)

        self.continueMode = Gui_PrefCheckBox(self.groupBox_1)
        self.continueMode.setObjectName(u"continueMode")
        self.continueMode.setChecked(True)
        self.continueMode.setProperty(u"prefEntry", u"ContinuousCreationMode")
        self.continueMode.setProperty(u"prefPath", u"Mod/Sketcher")

        self.gridLayout_1.addWidget(self.continueMode, 5, 0, 1, 2)

        self.EditSketcherFontSize = Gui_PrefSpinBox(self.groupBox_1)
        self.EditSketcherFontSize.setObjectName(u"EditSketcherFontSize")
        self.EditSketcherFontSize.setMinimum(1)
        self.EditSketcherFontSize.setMaximum(100)
        self.EditSketcherFontSize.setValue(17)
        self.EditSketcherFontSize.setProperty(u"prefEntry", u"EditSketcherFontSize")
        self.EditSketcherFontSize.setProperty(u"prefPath", u"View")

        self.gridLayout_1.addWidget(self.EditSketcherFontSize, 0, 1, 1, 1)

        self.checkBoxHideUnits = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBoxHideUnits.setObjectName(u"checkBoxHideUnits")
        self.checkBoxHideUnits.setProperty(u"prefEntry", u"HideUnits")
        self.checkBoxHideUnits.setProperty(u"prefPath", u"Mod/Sketcher")

        self.gridLayout_1.addWidget(self.checkBoxHideUnits, 7, 0, 1, 2)

        self.label_0 = QLabel(self.groupBox_1)
        self.label_0.setObjectName(u"label_0")
        self.label_0.setMinimumSize(QSize(182, 0))

        self.gridLayout_1.addWidget(self.label_0, 0, 0, 1, 1)

        self.constraintMode = Gui_PrefCheckBox(self.groupBox_1)
        self.constraintMode.setObjectName(u"constraintMode")
        self.constraintMode.setChecked(True)
        self.constraintMode.setProperty(u"prefEntry", u"ContinuousConstraintMode")
        self.constraintMode.setProperty(u"prefPath", u"Mod/Sketcher")

        self.gridLayout_1.addWidget(self.constraintMode, 6, 0, 1, 2)

        self.checkBoxShowCursorCoords = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBoxShowCursorCoords.setObjectName(u"checkBoxShowCursorCoords")
        self.checkBoxShowCursorCoords.setChecked(True)
        self.checkBoxShowCursorCoords.setProperty(u"prefEntry", u"ShowCursorCoords")
        self.checkBoxShowCursorCoords.setProperty(u"prefPath", u"Mod/Sketcher")

        self.gridLayout_1.addWidget(self.checkBoxShowCursorCoords, 8, 0, 1, 1)

        self.dialogOnDistanceConstraint = Gui_PrefCheckBox(self.groupBox_1)
        self.dialogOnDistanceConstraint.setObjectName(u"dialogOnDistanceConstraint")
        self.dialogOnDistanceConstraint.setChecked(True)
        self.dialogOnDistanceConstraint.setProperty(u"prefEntry", u"ShowDialogOnDistanceConstraint")
        self.dialogOnDistanceConstraint.setProperty(u"prefPath", u"Mod/Sketcher")

        self.gridLayout_1.addWidget(self.dialogOnDistanceConstraint, 4, 0, 1, 2)

        self.checkBoxUseSystemDecimals = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBoxUseSystemDecimals.setObjectName(u"checkBoxUseSystemDecimals")
        self.checkBoxUseSystemDecimals.setProperty(u"prefEntry", u"UseSystemDecimals")
        self.checkBoxUseSystemDecimals.setProperty(u"prefPath", u"Mod/Sketcher")

        self.gridLayout_1.addWidget(self.checkBoxUseSystemDecimals, 9, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_1)

        self.groupBox_2 = QGroupBox(SketcherGui__SketcherSettingsDisplay)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_2.setBaseSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBoxTVHideDependent = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBoxTVHideDependent.setObjectName(u"checkBoxTVHideDependent")
        self.checkBoxTVHideDependent.setChecked(True)
        self.checkBoxTVHideDependent.setProperty(u"prefEntry", u"HideDependent")
        self.checkBoxTVHideDependent.setProperty(u"prefPath", u"Mod/Sketcher/General")

        self.verticalLayout_2.addWidget(self.checkBoxTVHideDependent)

        self.checkBoxTVShowLinks = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBoxTVShowLinks.setObjectName(u"checkBoxTVShowLinks")
        self.checkBoxTVShowLinks.setChecked(True)
        self.checkBoxTVShowLinks.setProperty(u"prefEntry", u"ShowLinks")
        self.checkBoxTVShowLinks.setProperty(u"prefPath", u"Mod/Sketcher/General")

        self.verticalLayout_2.addWidget(self.checkBoxTVShowLinks)

        self.checkBoxTVShowSupport = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBoxTVShowSupport.setObjectName(u"checkBoxTVShowSupport")
        self.checkBoxTVShowSupport.setChecked(True)
        self.checkBoxTVShowSupport.setProperty(u"prefEntry", u"ShowSupport")
        self.checkBoxTVShowSupport.setProperty(u"prefPath", u"Mod/Sketcher/General")

        self.verticalLayout_2.addWidget(self.checkBoxTVShowSupport)

        self.checkBoxTVRestoreCamera = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBoxTVRestoreCamera.setObjectName(u"checkBoxTVRestoreCamera")
        self.checkBoxTVRestoreCamera.setChecked(True)
        self.checkBoxTVRestoreCamera.setProperty(u"prefEntry", u"RestoreCamera")
        self.checkBoxTVRestoreCamera.setProperty(u"prefPath", u"Mod/Sketcher/General")

        self.verticalLayout_2.addWidget(self.checkBoxTVRestoreCamera)

        self.checkBoxTVForceOrtho = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBoxTVForceOrtho.setObjectName(u"checkBoxTVForceOrtho")
        self.checkBoxTVForceOrtho.setChecked(False)
        self.checkBoxTVForceOrtho.setProperty(u"prefEntry", u"ForceOrtho")
        self.checkBoxTVForceOrtho.setProperty(u"prefPath", u"Mod/Sketcher/General")

        self.verticalLayout_2.addWidget(self.checkBoxTVForceOrtho)

        self.checkBoxTVSectionView = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBoxTVSectionView.setObjectName(u"checkBoxTVSectionView")
        self.checkBoxTVSectionView.setChecked(False)
        self.checkBoxTVSectionView.setProperty(u"prefEntry", u"SectionView")
        self.checkBoxTVSectionView.setProperty(u"prefPath", u"Mod/Sketcher/General")

        self.verticalLayout_2.addWidget(self.checkBoxTVSectionView)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_4.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_4)

        self.btnTVApply = QPushButton(self.groupBox_2)
        self.btnTVApply.setObjectName(u"btnTVApply")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnTVApply.sizePolicy().hasHeightForWidth())
        self.btnTVApply.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.btnTVApply)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

#if QT_CONFIG(shortcut)
        self.label_1.setBuddy(self.viewScalingFactor)
        self.label_3.setBuddy(self.SegmentsPerGeometry)
        self.label_0.setBuddy(self.EditSketcherFontSize)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.EditSketcherFontSize, self.ConstraintSymbolSize)
        QWidget.setTabOrder(self.ConstraintSymbolSize, self.viewScalingFactor)
        QWidget.setTabOrder(self.viewScalingFactor, self.SegmentsPerGeometry)
        QWidget.setTabOrder(self.SegmentsPerGeometry, self.dialogOnDistanceConstraint)
        QWidget.setTabOrder(self.dialogOnDistanceConstraint, self.continueMode)
        QWidget.setTabOrder(self.continueMode, self.constraintMode)
        QWidget.setTabOrder(self.constraintMode, self.checkBoxHideUnits)
        QWidget.setTabOrder(self.checkBoxHideUnits, self.checkBoxShowCursorCoords)
        QWidget.setTabOrder(self.checkBoxShowCursorCoords, self.checkBoxUseSystemDecimals)
        QWidget.setTabOrder(self.checkBoxUseSystemDecimals, self.checkBoxShowDimensionalName)
        QWidget.setTabOrder(self.checkBoxShowDimensionalName, self.prefDimensionalStringFormat)
        QWidget.setTabOrder(self.prefDimensionalStringFormat, self.checkBoxTVHideDependent)
        QWidget.setTabOrder(self.checkBoxTVHideDependent, self.checkBoxTVShowLinks)
        QWidget.setTabOrder(self.checkBoxTVShowLinks, self.checkBoxTVShowSupport)
        QWidget.setTabOrder(self.checkBoxTVShowSupport, self.checkBoxTVRestoreCamera)
        QWidget.setTabOrder(self.checkBoxTVRestoreCamera, self.checkBoxTVForceOrtho)
        QWidget.setTabOrder(self.checkBoxTVForceOrtho, self.checkBoxTVSectionView)
        QWidget.setTabOrder(self.checkBoxTVSectionView, self.btnTVApply)

        self.retranslateUi(SketcherGui__SketcherSettingsDisplay)
        self.checkBoxTVRestoreCamera.toggled.connect(self.checkBoxTVForceOrtho.setEnabled)
        self.checkBoxUseConstraintSymbolSize.toggled.connect(self.ConstraintSymbolSize.setEnabled)

        QMetaObject.connectSlotsByName(SketcherGui__SketcherSettingsDisplay)
    # setupUi

    def retranslateUi(self, SketcherGui__SketcherSettingsDisplay):
        SketcherGui__SketcherSettingsDisplay.setWindowTitle(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Display", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Sketch Editing", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUseConstraintSymbolSize.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Enable a custom pixel size for constraint symbols (otherwise the font size is used).", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUseConstraintSymbolSize.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Use custom constraint symbol size", None))
#if QT_CONFIG(tooltip)
        self.ConstraintSymbolSize.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Pixel size used to render constraint symbols", None))
#endif // QT_CONFIG(tooltip)
        self.ConstraintSymbolSize.setSuffix(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"px", None))
        self.label_1.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"View scale ratio", None))
#if QT_CONFIG(tooltip)
        self.viewScalingFactor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Scales the 3D view based on this factor", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.SegmentsPerGeometry.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"The number of polygons used for geometry approximation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBoxShowDimensionalName.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Displays names of dimensional constraints, if they exist", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxShowDimensionalName.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Show dimensional constraint name with format", None))
#if QT_CONFIG(tooltip)
        self.prefDimensionalStringFormat.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"The format of the dimensional constraint string presentation.\n"
"Defaults to: %N = %V\n"
"\n"
"%N - name parameter\n"
"%V - dimension value", None))
#endif // QT_CONFIG(tooltip)
        self.prefDimensionalStringFormat.setPlaceholderText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"%N = %V", None))
        self.label_3.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Segments per geometry", None))
#if QT_CONFIG(tooltip)
        self.continueMode.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Keeps the current Sketcher tool active after creating geometry", None))
#endif // QT_CONFIG(tooltip)
        self.continueMode.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Geometry creation \"Continue Mode\"", None))
#if QT_CONFIG(tooltip)
        self.EditSketcherFontSize.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Font size used for labels and constraints", None))
#endif // QT_CONFIG(tooltip)
        self.EditSketcherFontSize.setSuffix(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"px", None))
#if QT_CONFIG(tooltip)
        self.checkBoxHideUnits.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Base length units will not be displayed in constraints or cursor coordinates.\n"
"Supports all unit systems except 'US customary' and 'Building US/Euro'.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxHideUnits.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Hide base length units for supported unit systems", None))
        self.label_0.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Font size", None))
#if QT_CONFIG(tooltip)
        self.constraintMode.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Keeps the current Sketcher constraint tool active after creating geometry", None))
#endif // QT_CONFIG(tooltip)
        self.constraintMode.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Constraint creation \"Continue Mode\"", None))
#if QT_CONFIG(tooltip)
        self.checkBoxShowCursorCoords.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Displays cursor position coordinates next to the cursor while editing a sketch", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxShowCursorCoords.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Displays coordinates next to the cursor while editing", None))
#if QT_CONFIG(tooltip)
        self.dialogOnDistanceConstraint.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Opens a dialog to input a value for new dimensional constraints after creation", None))
#endif // QT_CONFIG(tooltip)
        self.dialogOnDistanceConstraint.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Ask for value after creating a dimensional constraint", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUseSystemDecimals.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Cursor coordinates will use the system decimals setting instead of the short form", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUseSystemDecimals.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Use system decimals setting for cursor coordinates", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Visibility Automation", None))
#if QT_CONFIG(tooltip)
        self.checkBoxTVHideDependent.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Hides all object features that depend on the opened sketch", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxTVHideDependent.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Hide all objects that depend on the sketch", None))
#if QT_CONFIG(tooltip)
        self.checkBoxTVShowLinks.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Shows source objects which are used for external geometry in the opened sketch", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxTVShowLinks.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Show objects used for external geometry", None))
#if QT_CONFIG(tooltip)
        self.checkBoxTVShowSupport.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Shows objects the opened sketch is attached to", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxTVShowSupport.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Show objects that the sketch is attached to", None))
#if QT_CONFIG(tooltip)
        self.checkBoxTVRestoreCamera.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Restores the camera position after closing the sketch", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxTVRestoreCamera.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Restore camera position after editing", None))
#if QT_CONFIG(tooltip)
        self.checkBoxTVForceOrtho.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Forces the camera to an orthographic view when editing a sketch.\n"
"Works only when \"Restore camera position after editing\" is enabled.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxTVForceOrtho.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Force orthographic camera when entering edit", None))
#if QT_CONFIG(tooltip)
        self.checkBoxTVSectionView.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Opens a sketch in section view mode, showing only objects behind the sketch plane", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxTVSectionView.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Open sketch in section view mode", None))
        self.label_4.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Note: these settings are defaults applied to new sketches. The behavior is remembered for each sketch individually as properties on the View tab.", None))
#if QT_CONFIG(tooltip)
        self.btnTVApply.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Applies current visibility automation settings to all sketches in the open documents", None))
#endif // QT_CONFIG(tooltip)
        self.btnTVApply.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsDisplay", u"Apply to Existing Sketches", None))
    # retranslateUi

