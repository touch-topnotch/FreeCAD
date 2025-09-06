# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SketcherSettings.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SketcherGui_SketcherSettings(object):
    def setupUi(self, SketcherGui__SketcherSettings):
        if not SketcherGui__SketcherSettings.objectName():
            SketcherGui__SketcherSettings.setObjectName(u"SketcherGui__SketcherSettings")
        SketcherGui__SketcherSettings.resize(500, 592)
        self.gridLayout = QGridLayout(SketcherGui__SketcherSettings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(SketcherGui__SketcherSettings)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.checkBoxAdvancedSolverTaskBox = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBoxAdvancedSolverTaskBox.setObjectName(u"checkBoxAdvancedSolverTaskBox")
        self.checkBoxAdvancedSolverTaskBox.setProperty(u"prefEntry", u"ShowSolverAdvancedWidget")
        self.checkBoxAdvancedSolverTaskBox.setProperty(u"prefPath", u"Mod/Sketcher")

        self.gridLayout_4.addWidget(self.checkBoxAdvancedSolverTaskBox, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(SketcherGui__SketcherSettings)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.checkBoxRecalculateInitialSolutionWhileDragging = Gui_PrefCheckBox(self.groupBox_4)
        self.checkBoxRecalculateInitialSolutionWhileDragging.setObjectName(u"checkBoxRecalculateInitialSolutionWhileDragging")
        self.checkBoxRecalculateInitialSolutionWhileDragging.setChecked(True)
        self.checkBoxRecalculateInitialSolutionWhileDragging.setProperty(u"prefEntry", u"RecalculateInitialSolutionWhileDragging")
        self.checkBoxRecalculateInitialSolutionWhileDragging.setProperty(u"prefPath", u"Mod/Sketcher")

        self.gridLayout_5.addWidget(self.checkBoxRecalculateInitialSolutionWhileDragging, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(SketcherGui__SketcherSettings)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QSize(0, 0))
        self.groupBox_5.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_5.setBaseSize(QSize(0, 0))
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.checkBoxAutoRemoveRedundants = Gui_PrefCheckBox(self.groupBox_5)
        self.checkBoxAutoRemoveRedundants.setObjectName(u"checkBoxAutoRemoveRedundants")
        self.checkBoxAutoRemoveRedundants.setChecked(False)
        self.checkBoxAutoRemoveRedundants.setProperty(u"prefEntry", u"AutoRemoveRedundants")
        self.checkBoxAutoRemoveRedundants.setProperty(u"prefPath", u"Mod/Sketcher")

        self.verticalLayout_22.addWidget(self.checkBoxAutoRemoveRedundants)

        self.checkBoxEnableEscape = Gui_PrefCheckBox(self.groupBox_5)
        self.checkBoxEnableEscape.setObjectName(u"checkBoxEnableEscape")
        self.checkBoxEnableEscape.setChecked(True)
        self.checkBoxEnableEscape.setProperty(u"prefEntry", u"LeaveSketchWithEscape")
        self.checkBoxEnableEscape.setProperty(u"prefPath", u"Mod/Sketcher")

        self.verticalLayout_22.addWidget(self.checkBoxEnableEscape)

        self.checkBoxNotifyConstraintSubstitutions = Gui_PrefCheckBox(self.groupBox_5)
        self.checkBoxNotifyConstraintSubstitutions.setObjectName(u"checkBoxNotifyConstraintSubstitutions")
        self.checkBoxNotifyConstraintSubstitutions.setChecked(True)
        self.checkBoxNotifyConstraintSubstitutions.setProperty(u"prefEntry", u"NotifyConstraintSubstitutions")
        self.checkBoxNotifyConstraintSubstitutions.setProperty(u"prefPath", u"Mod/Sketcher/General")

        self.verticalLayout_22.addWidget(self.checkBoxNotifyConstraintSubstitutions)

        self.checkBoxUnifiedCoincident = Gui_PrefCheckBox(self.groupBox_5)
        self.checkBoxUnifiedCoincident.setObjectName(u"checkBoxUnifiedCoincident")
        self.checkBoxUnifiedCoincident.setChecked(True)
        self.checkBoxUnifiedCoincident.setProperty(u"prefEntry", u"UnifiedCoincident")
        self.checkBoxUnifiedCoincident.setProperty(u"prefPath", u"Mod/Sketcher/Constraints")

        self.verticalLayout_22.addWidget(self.checkBoxUnifiedCoincident)

        self.checkBoxHorVerAuto = Gui_PrefCheckBox(self.groupBox_5)
        self.checkBoxHorVerAuto.setObjectName(u"checkBoxHorVerAuto")
        self.checkBoxHorVerAuto.setChecked(True)
        self.checkBoxHorVerAuto.setProperty(u"prefEntry", u"AutoHorVer")
        self.checkBoxHorVerAuto.setProperty(u"prefPath", u"Mod/Sketcher/Constraints")

        self.verticalLayout_22.addWidget(self.checkBoxHorVerAuto)

        self.checkBoxLineGroup = Gui_PrefCheckBox(self.groupBox_5)
        self.checkBoxLineGroup.setObjectName(u"checkBoxLineGroup")
        self.checkBoxLineGroup.setChecked(False)
        self.checkBoxLineGroup.setProperty(u"prefEntry", u"UnifiedLineCommands")
        self.checkBoxLineGroup.setProperty(u"prefPath", u"Mod/Sketcher/Commands")

        self.verticalLayout_22.addWidget(self.checkBoxLineGroup)

        self.checkBoxAddExtGeo = Gui_PrefCheckBox(self.groupBox_5)
        self.checkBoxAddExtGeo.setObjectName(u"checkBoxAddExtGeo")
        self.checkBoxAddExtGeo.setChecked(False)
        self.checkBoxAddExtGeo.setProperty(u"prefEntry", u"AlwaysExtGeoReference")
        self.checkBoxAddExtGeo.setProperty(u"prefPath", u"Mod/Sketcher/General")

        self.verticalLayout_22.addWidget(self.checkBoxAddExtGeo)

        self.checkBoxMakeInternals = Gui_PrefCheckBox(self.groupBox_5)
        self.checkBoxMakeInternals.setObjectName(u"checkBoxMakeInternals")
        self.checkBoxMakeInternals.setProperty(u"prefPath", u"Mod/Sketcher")
        self.checkBoxMakeInternals.setProperty(u"prefEntry", u"MakeInternals")

        self.verticalLayout_22.addWidget(self.checkBoxMakeInternals)


        self.gridLayout.addWidget(self.groupBox_5, 2, 0, 1, 1)

        self.groupBox_6 = QGroupBox(SketcherGui__SketcherSettings)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.gridLayout_general = QGridLayout(self.groupBox_6)
        self.gridLayout_general.setObjectName(u"gridLayout_general")
        self.radiusDiameterMode = QComboBox(self.groupBox_6)
        self.radiusDiameterMode.setObjectName(u"radiusDiameterMode")

        self.gridLayout_general.addWidget(self.radiusDiameterMode, 1, 1, 1, 1)

        self.dimensioningMode = QComboBox(self.groupBox_6)
        self.dimensioningMode.setObjectName(u"dimensioningMode")

        self.gridLayout_general.addWidget(self.dimensioningMode, 0, 1, 1, 1)

        self.radiusDiameterLabel = QLabel(self.groupBox_6)
        self.radiusDiameterLabel.setObjectName(u"radiusDiameterLabel")

        self.gridLayout_general.addWidget(self.radiusDiameterLabel, 1, 0, 1, 1)

        self.dimensioningLabel = QLabel(self.groupBox_6)
        self.dimensioningLabel.setObjectName(u"dimensioningLabel")

        self.gridLayout_general.addWidget(self.dimensioningLabel, 0, 0, 1, 1)

        self.autoScaleModeLabel = QLabel(self.groupBox_6)
        self.autoScaleModeLabel.setObjectName(u"autoScaleModeLabel")

        self.gridLayout_general.addWidget(self.autoScaleModeLabel, 2, 0, 1, 1)

        self.autoScaleMode = QComboBox(self.groupBox_6)
        self.autoScaleMode.setObjectName(u"autoScaleMode")

        self.gridLayout_general.addWidget(self.autoScaleMode, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_6, 3, 0, 1, 1)

        self.groupBox_7 = QGroupBox(SketcherGui__SketcherSettings)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.gridLayout_vis = QGridLayout(self.groupBox_7)
        self.gridLayout_vis.setObjectName(u"gridLayout_vis")
        self.ovpVisibilityLabel = QLabel(self.groupBox_7)
        self.ovpVisibilityLabel.setObjectName(u"ovpVisibilityLabel")

        self.gridLayout_vis.addWidget(self.ovpVisibilityLabel, 0, 0, 1, 1)

        self.ovpVisibility = QComboBox(self.groupBox_7)
        self.ovpVisibility.setObjectName(u"ovpVisibility")

        self.gridLayout_vis.addWidget(self.ovpVisibility, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_7, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        QWidget.setTabOrder(self.checkBoxAdvancedSolverTaskBox, self.checkBoxRecalculateInitialSolutionWhileDragging)
        QWidget.setTabOrder(self.checkBoxRecalculateInitialSolutionWhileDragging, self.checkBoxAutoRemoveRedundants)
        QWidget.setTabOrder(self.checkBoxAutoRemoveRedundants, self.checkBoxEnableEscape)
        QWidget.setTabOrder(self.checkBoxEnableEscape, self.checkBoxNotifyConstraintSubstitutions)

        self.retranslateUi(SketcherGui__SketcherSettings)

        QMetaObject.connectSlotsByName(SketcherGui__SketcherSettings)
    # setupUi

    def retranslateUi(self, SketcherGui__SketcherSettings):
        SketcherGui__SketcherSettings.setWindowTitle(QCoreApplication.translate("SketcherGui::SketcherSettings", u"General", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Task Panel Widgets", None))
#if QT_CONFIG(tooltip)
        self.checkBoxAdvancedSolverTaskBox.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Displays the additional section 'Advanced solver control' to adjust solver settings in the task view", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxAdvancedSolverTaskBox.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Show section 'Advanced solver control'", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Dragging Performance", None))
#if QT_CONFIG(tooltip)
        self.checkBoxRecalculateInitialSolutionWhileDragging.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Special solver algorithm will be used while dragging sketch elements.\n"
"Requires to re-enter edit mode to take effect.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxRecalculateInitialSolutionWhileDragging.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Improve solving while dragging", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("SketcherGui::SketcherSettings", u"General", None))
#if QT_CONFIG(tooltip)
        self.checkBoxAutoRemoveRedundants.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Automatically removes newly added redundant constraints", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxAutoRemoveRedundants.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Auto remove redundant constraints", None))
#if QT_CONFIG(tooltip)
        self.checkBoxEnableEscape.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Allows to leave the sketch edit mode by pressing the Esc key", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxEnableEscape.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Esc key can leave sketch edit mode", None))
#if QT_CONFIG(tooltip)
        self.checkBoxNotifyConstraintSubstitutions.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Notifies about automatic constraint substitutions", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxNotifyConstraintSubstitutions.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Notify about automatic constraint substitutions", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUnifiedCoincident.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Unifies the coincident and point-on-object constraints in a single tool", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUnifiedCoincident.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Unify coincident and point-on-object constraints", None))
#if QT_CONFIG(tooltip)
        self.checkBoxHorVerAuto.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Unifies the horizontal and vertical constraints to an automatic command", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxHorVerAuto.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Unified tool for automatic horizontal/vertical constraints", None))
#if QT_CONFIG(tooltip)
        self.checkBoxLineGroup.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Shows a command group button that contains both the polyline and line commands. Otherwise, each command has its own separate button.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxLineGroup.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Group the polyline and line commands", None))
#if QT_CONFIG(tooltip)
        self.checkBoxAddExtGeo.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Always adds external geometry as construction geometry. Otherwise, it is added according to the current construction mode.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxAddExtGeo.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Always add external geometry as construction", None))
#if QT_CONFIG(tooltip)
        self.checkBoxMakeInternals.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Closed loops will automatically generate internal faces which are selectable to be used with other tools", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxMakeInternals.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Generate internal faces", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Dimension Constraint", None))
#if QT_CONFIG(tooltip)
        self.radiusDiameterMode.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"While using the Dimension tool you may choose how to handle circles and arcs:\n"
"'Auto': The tool will apply radius to arcs and diameter to circles.\n"
"'Diameter': The tool will apply diameter to both arcs and circles.\n"
"'Radius': The tool will apply radius to both arcs and circles.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dimensioningMode.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Select the type of dimensioning constraints for your toolbar:\n"
"'Single tool': A single tool for all dimensioning constraints in the toolbar: Distance, Distance X / Y, Angle, Radius. (Others in dropdown)\n"
"'Separated tools': Individual tools for each dimensioning constraint.\n"
"'Both': You will have both the 'Dimension' tool and the separated tools.\n"
"This setting is only for the toolbar. Whichever you choose, all tools are always available in the menu and through shortcuts.", None))
#endif // QT_CONFIG(tooltip)
        self.radiusDiameterLabel.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Dimension tool diameter/radius mode", None))
        self.dimensioningLabel.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Dimensioning constraints", None))
        self.autoScaleModeLabel.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Scale upon first constraint", None))
#if QT_CONFIG(tooltip)
        self.autoScaleMode.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Select the mode of automatic geometry scaling upon first dimension:\n"
"'Always': Automatic scaling upon first dimension is always performed.\n"
"'Never': Automatic scaling upon first dimension is never performed.\n"
"'When no scale feature is visible': Automatic scaling upon first dimension is only performed if there are no visible objects in the 3D view.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_7.setTitle(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Tool Parameters", None))
        self.ovpVisibilityLabel.setText(QCoreApplication.translate("SketcherGui::SketcherSettings", u"On-view-parameters (OVP)", None))
#if QT_CONFIG(tooltip)
        self.ovpVisibility.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettings", u"Choose a visibility mode for the On-View-Parameters:\n"
"'Disabled': On-View-Parameters are completely disabled.\n"
"'Only dimensional': Only dimensional On-View-Parameters are visible. They are the most useful. For example the radius of a circle.\n"
"'All': Both dimensional and positional On-View-Parameters. Positionals are the (x,y) position of the cursor. For example for the center of a circle.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

