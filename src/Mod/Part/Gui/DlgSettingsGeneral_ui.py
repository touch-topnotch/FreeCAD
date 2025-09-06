# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsGeneral.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_PartGui_DlgSettingsGeneral(object):
    def setupUi(self, PartGui__DlgSettingsGeneral):
        if not PartGui__DlgSettingsGeneral.objectName():
            PartGui__DlgSettingsGeneral.setObjectName(u"PartGui__DlgSettingsGeneral")
        PartGui__DlgSettingsGeneral.resize(550, 586)
        self.verticalLayout = QVBoxLayout(PartGui__DlgSettingsGeneral)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(PartGui__DlgSettingsGeneral)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBooleanCheck = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBooleanCheck.setObjectName(u"checkBooleanCheck")
        self.checkBooleanCheck.setChecked(True)
        self.checkBooleanCheck.setProperty(u"prefEntry", u"CheckModel")
        self.checkBooleanCheck.setProperty(u"prefPath", u"Mod/Part/Boolean")

        self.gridLayout.addWidget(self.checkBooleanCheck, 0, 0, 1, 1)

        self.checkBooleanRefine = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBooleanRefine.setObjectName(u"checkBooleanRefine")
        self.checkBooleanRefine.setChecked(True)
        self.checkBooleanRefine.setProperty(u"prefEntry", u"RefineModel")
        self.checkBooleanRefine.setProperty(u"prefPath", u"Mod/Part/Boolean")

        self.gridLayout.addWidget(self.checkBooleanRefine, 1, 0, 1, 1)

        self.checkSketchBaseRefine = Gui_PrefCheckBox(self.groupBox_2)
        self.checkSketchBaseRefine.setObjectName(u"checkSketchBaseRefine")
        self.checkSketchBaseRefine.setChecked(True)
        self.checkSketchBaseRefine.setProperty(u"prefEntry", u"RefineModel")
        self.checkSketchBaseRefine.setProperty(u"prefPath", u"Mod/PartDesign")

        self.gridLayout.addWidget(self.checkSketchBaseRefine, 2, 0, 1, 1)

        self.checkAllowCompoundBody = Gui_PrefCheckBox(self.groupBox_2)
        self.checkAllowCompoundBody.setObjectName(u"checkAllowCompoundBody")
        self.checkAllowCompoundBody.setChecked(True)
        self.checkAllowCompoundBody.setProperty(u"prefEntry", u"AllowCompoundDefault")
        self.checkAllowCompoundBody.setProperty(u"prefPath", u"Mod/PartDesign")

        self.gridLayout.addWidget(self.checkAllowCompoundBody, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(PartGui__DlgSettingsGeneral)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setVisible(False)
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkObjectNaming = Gui_PrefCheckBox(self.groupBox_3)
        self.checkObjectNaming.setObjectName(u"checkObjectNaming")
        self.checkObjectNaming.setProperty(u"prefEntry", u"AddBaseObjectName")
        self.checkObjectNaming.setProperty(u"prefPath", u"Mod/Part")

        self.gridLayout_2.addWidget(self.checkObjectNaming, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(PartGui__DlgSettingsGeneral)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.comboDefaultProfileTypeForHole = Gui_PrefComboBox(self.groupBox)
        self.comboDefaultProfileTypeForHole.addItem("")
        self.comboDefaultProfileTypeForHole.addItem("")
        self.comboDefaultProfileTypeForHole.addItem("")
        self.comboDefaultProfileTypeForHole.setObjectName(u"comboDefaultProfileTypeForHole")
        self.comboDefaultProfileTypeForHole.setProperty(u"prefEntry", u"defaultBaseTypeHole")
        self.comboDefaultProfileTypeForHole.setProperty(u"prefPath", u"Mod/PartDesign")

        self.horizontalLayout_2.addWidget(self.comboDefaultProfileTypeForHole)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.checkSwitchToTask = Gui_PrefCheckBox(self.groupBox)
        self.checkSwitchToTask.setObjectName(u"checkSwitchToTask")
        self.checkSwitchToTask.setChecked(True)
        self.checkSwitchToTask.setProperty(u"prefEntry", u"SwitchToTask")
        self.checkSwitchToTask.setProperty(u"prefPath", u"Mod/PartDesign")

        self.verticalLayout_4.addWidget(self.checkSwitchToTask)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBoxPreview = QGroupBox(PartGui__DlgSettingsGeneral)
        self.groupBoxPreview.setObjectName(u"groupBoxPreview")
        self.groupBoxPreview.setEnabled(True)
        self.groupBoxPreview.setFlat(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBoxPreview)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkShowFinalPreview = Gui_PrefCheckBox(self.groupBoxPreview)
        self.checkShowFinalPreview.setObjectName(u"checkShowFinalPreview")
        self.checkShowFinalPreview.setProperty(u"prefEntry", u"ShowFinal")
        self.checkShowFinalPreview.setProperty(u"prefPath", u"Mod/PartDesign/Preview")

        self.verticalLayout_3.addWidget(self.checkShowFinalPreview)

        self.checkShowTransparentPreview = Gui_PrefCheckBox(self.groupBoxPreview)
        self.checkShowTransparentPreview.setObjectName(u"checkShowTransparentPreview")
        self.checkShowTransparentPreview.setChecked(True)
        self.checkShowTransparentPreview.setProperty(u"prefEntry", u"ShowTransparentPreview")
        self.checkShowTransparentPreview.setProperty(u"prefPath", u"Mod/PartDesign/Preview")

        self.verticalLayout_3.addWidget(self.checkShowTransparentPreview)

        self.checkShowProfilePreview = Gui_PrefCheckBox(self.groupBoxPreview)
        self.checkShowProfilePreview.setObjectName(u"checkShowProfilePreview")
        self.checkShowProfilePreview.setChecked(True)
        self.checkShowProfilePreview.setProperty(u"prefEntry", u"ShowProfilePreview")
        self.checkShowProfilePreview.setProperty(u"prefPath", u"Mod/PartDesign/Preview")

        self.verticalLayout_3.addWidget(self.checkShowProfilePreview)


        self.verticalLayout.addWidget(self.groupBoxPreview)

        self.groupBoxExperimental = QGroupBox(PartGui__DlgSettingsGeneral)
        self.groupBoxExperimental.setObjectName(u"groupBoxExperimental")
        self.groupBoxExperimental.setEnabled(True)
        self.groupBoxExperimental.setFlat(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxExperimental)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.warningLabel = QLabel(self.groupBoxExperimental)
        self.warningLabel.setObjectName(u"warningLabel")
        self.warningLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.warningLabel)

        self.enableGizmos = Gui_PrefCheckBox(self.groupBoxExperimental)
        self.enableGizmos.setObjectName(u"enableGizmos")
        self.enableGizmos.setChecked(True)
        self.enableGizmos.setProperty(u"prefEntry", u"EnableGizmos")
        self.enableGizmos.setProperty(u"prefPath", u"Mod/PartDesign")

        self.verticalLayout_2.addWidget(self.enableGizmos)

        self.delayedGizmoUpdate = Gui_PrefCheckBox(self.groupBoxExperimental)
        self.delayedGizmoUpdate.setObjectName(u"delayedGizmoUpdate")
        self.delayedGizmoUpdate.setProperty(u"prefEntry", u"DelayedGizmoUpdate")
        self.delayedGizmoUpdate.setProperty(u"prefPath", u"Mod/PartDesign")

        self.verticalLayout_2.addWidget(self.delayedGizmoUpdate)


        self.verticalLayout.addWidget(self.groupBoxExperimental)

        self.spacerItem = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.spacerItem)


        self.retranslateUi(PartGui__DlgSettingsGeneral)

        self.comboDefaultProfileTypeForHole.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(PartGui__DlgSettingsGeneral)
    # setupUi

    def retranslateUi(self, PartGui__DlgSettingsGeneral):
        PartGui__DlgSettingsGeneral.setWindowTitle(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"General", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Model Settings", None))
        self.checkBooleanCheck.setText(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Automatically check model after boolean operation", None))
        self.checkBooleanRefine.setText(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Automatically refine model after boolean operation", None))
        self.checkSketchBaseRefine.setText(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Automatically refine model after applying operations", None))
        self.checkAllowCompoundBody.setText(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Allow multiple solids in Part Design bodies by default", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Object Naming", None))
        self.checkObjectNaming.setText(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Add name of base object", None))
        self.groupBox.setTitle(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Features Settings", None))
        self.label.setText(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Default profile type for holes", None))
        self.comboDefaultProfileTypeForHole.setItemText(0, QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Circles and arcs", None))
        self.comboDefaultProfileTypeForHole.setItemText(1, QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Points, circles and arcs", None))
        self.comboDefaultProfileTypeForHole.setItemText(2, QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Points", None))

#if QT_CONFIG(tooltip)
        self.checkSwitchToTask.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Automatically switch to the task panel when the Part Design workbench is activated", None))
#endif // QT_CONFIG(tooltip)
        self.checkSwitchToTask.setText(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Switch to task panel when entering Part Design workbench", None))
        self.groupBoxPreview.setTitle(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Preview", None))
        self.checkShowFinalPreview.setText(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Show final result by default when editing features", None))
        self.checkShowTransparentPreview.setText(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Show transparent preview overlay by default when editing features", None))
        self.checkShowProfilePreview.setText(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Highlight the profile used to create features", None))
        self.groupBoxExperimental.setTitle(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Experimental", None))
        self.warningLabel.setText(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"These settings are experimental and may result in decreased stability, problems and undefined behaviors", None))
        self.enableGizmos.setText(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Show interactive draggers when editing features", None))
        self.delayedGizmoUpdate.setText(QCoreApplication.translate("PartGui::DlgSettingsGeneral", u"Disable recompute while dragging", None))
    # retranslateUi

