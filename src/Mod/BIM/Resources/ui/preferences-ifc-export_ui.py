# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-ifc-export.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsArch(object):
    def setupUi(self, Gui__Dialog__DlgSettingsArch):
        if not Gui__Dialog__DlgSettingsArch.objectName():
            Gui__Dialog__DlgSettingsArch.setObjectName(u"Gui__Dialog__DlgSettingsArch")
        Gui__Dialog__DlgSettingsArch.resize(534, 718)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsArch)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(9, 9, 9, 9)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.group_box_0 = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.group_box_0.setObjectName(u"group_box_0")
        self.verticalLayout = QVBoxLayout(self.group_box_0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_7 = Gui_PrefCheckBox(self.group_box_0)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setProperty(u"prefEntry", u"ifcShowDialog")
        self.checkBox_7.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_7)


        self.vboxLayout.addWidget(self.group_box_0)

        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox = Gui_PrefComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setProperty(u"prefEntry", u"ifcExportModel")
        self.comboBox.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.checkBox = Gui_PrefCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setProperty(u"prefEntry", u"ifcExportAsBrep")
        self.checkBox.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_4 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setProperty(u"prefEntry", u"ifcUseDaeOptions")
        self.checkBox_4.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.checkBox_5 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setProperty(u"prefEntry", u"ifcJoinCoplanarFacets")
        self.checkBox_5.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_2.addWidget(self.checkBox_5)

        self.checkBox_9 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setChecked(True)
        self.checkBox_9.setProperty(u"prefEntry", u"ifcStoreUid")
        self.checkBox_9.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_2.addWidget(self.checkBox_9)

        self.checkBox_10 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setProperty(u"prefEntry", u"ifcSerialize")
        self.checkBox_10.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_2.addWidget(self.checkBox_10)

        self.checkBox_12 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setChecked(True)
        self.checkBox_12.setProperty(u"prefEntry", u"ifcExport2D")
        self.checkBox_12.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_2.addWidget(self.checkBox_12)

        self.checkBox_13 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setProperty(u"prefEntry", u"IfcExportFreeCADProperties")
        self.checkBox_13.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_2.addWidget(self.checkBox_13)

        self.checkBox_15 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setChecked(True)
        self.checkBox_15.setProperty(u"prefEntry", u"ifcCompress")
        self.checkBox_15.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_2.addWidget(self.checkBox_15)

        self.checkBox_16 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_16.setObjectName(u"checkBox_16")
        self.checkBox_16.setProperty(u"prefEntry", u"DisableIfcRectangleProfileDef")
        self.checkBox_16.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_2.addWidget(self.checkBox_16)

        self.checkBox_17 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_17.setObjectName(u"checkBox_17")
        self.checkBox_17.setProperty(u"prefEntry", u"getStandardCase")
        self.checkBox_17.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_2.addWidget(self.checkBox_17)

        self.checkBox_19 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_19.setObjectName(u"checkBox_19")
        self.checkBox_19.setProperty(u"prefEntry", u"IfcAddDefaultSite")
        self.checkBox_19.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_2.addWidget(self.checkBox_19)

        self.checkBox_20 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_20.setObjectName(u"checkBox_20")
        self.checkBox_20.setProperty(u"prefEntry", u"IfcAddDefaultStorey")
        self.checkBox_20.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_2.addWidget(self.checkBox_20)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_3 = Gui_PrefComboBox(self.groupBox)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setProperty(u"prefEntry", u"ifcUnit")
        self.comboBox_3.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout.addWidget(self.comboBox_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)


        self.vboxLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_21 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_21.setObjectName(u"checkBox_21")
        self.checkBox_21.setChecked(True)
        self.checkBox_21.setProperty(u"prefEntry", u"IfcAddDefaultBuilding")
        self.checkBox_21.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_3.addWidget(self.checkBox_21)

        self.checkBox_2 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setProperty(u"prefEntry", u"IfcGroupsAsAssemblies")
        self.checkBox_2.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_3.addWidget(self.checkBox_2)


        self.vboxLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Gui__Dialog__DlgSettingsArch)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsArch)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsArch):
        Gui__Dialog__DlgSettingsArch.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"IFC export", None))
        self.group_box_0.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"General options", None))
        self.checkBox_7.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Show this dialog when exporting", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Export options", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"The type of objects that you wish to export:\n"
"- Standard model: solid objects.\n"
"- Structural analysis: wireframe model for structural calculations.\n"
"- Standard + structural: both types of models.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Export type", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Standard model", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Structural analysis", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Standard + structural", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"The type of objects that you wish to export:\n"
"- Standard model: solid objects.\n"
"- Structural analysis: wireframe model for structural calculations.\n"
"- Standard + structural: both types of models.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Some IFC viewers don't like objects exported as extrusions.\n"
"Use this to force all objects to be exported as BREP geometry.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Force export as Brep", None))
#if QT_CONFIG(tooltip)
        self.checkBox_4.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Use triangulation options set in the DAE options page", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Use DAE triangulation options", None))
#if QT_CONFIG(tooltip)
        self.checkBox_5.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Curved shapes that cannot be represented as curves in IFC\n"
"are decomposed into flat facets.\n"
"If this is checked, an additional calculation is done to join coplanar facets.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_5.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Join coplanar facets when triangulating", None))
#if QT_CONFIG(tooltip)
        self.checkBox_9.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"When exporting objects without unique ID (UID), the generated UID\n"
"will be stored inside the FreeCAD object for reuse next time that object\n"
"is exported. This leads to smaller differences between file versions.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_9.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Store IFC unique ID in FreeCAD objects", None))
#if QT_CONFIG(tooltip)
        self.checkBox_10.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"IFCOpenShell is a library that enables importing IFC files.\n"
"Its serializer functionality allows giving it an OCC shape and it will\n"
"produce adequate IFC geometry: NURBS, faceted, or anything else.\n"
"Note: The serializer is still an experimental feature!", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_10.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Use IfcOpenShell serializer if available", None))
#if QT_CONFIG(tooltip)
        self.checkBox_12.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"2D objects will be exported as IfcAnnotation", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_12.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Export 2D objects as IfcAnnotations", None))
#if QT_CONFIG(tooltip)
        self.checkBox_13.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"All FreeCAD object properties will be stored inside the exported objects,\n"
"allowing to recreate a full parametric model on reimport.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_13.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Export full FreeCAD parametric model", None))
#if QT_CONFIG(tooltip)
        self.checkBox_15.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"When possible, similar entities will be used only once in the file if possible.\n"
"This can reduce the file size a lot, but will make it less easily readable.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_15.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Reuse similar entities", None))
#if QT_CONFIG(tooltip)
        self.checkBox_16.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"When possible, IFC objects that are extruded rectangles will be\n"
"exported as IfcRectangleProfileDef.\n"
"However, some other applications might have problems importing that entity.\n"
"If this is your case, you can disable this and then all profiles will be exported as IfcArbitraryClosedProfileDef.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_16.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Disable IfcRectangleProfileDef", None))
#if QT_CONFIG(tooltip)
        self.checkBox_17.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Some IFC types such as IfcWall or IfcBeam have special standard versions like IfcWallStandardCase or IfcBeamStandardCase. If this option is turned on, FreeCAD will automatically export such objects\n"
"as standard cases when the necessary conditions are met.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_17.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Auto-detect and export as standard cases when applicable", None))
#if QT_CONFIG(tooltip)
        self.checkBox_19.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"If no site is found in the FreeCAD document, a default one will be added.\n"
"A site is not mandatory but a common practice is to have at least one in the file.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_19.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Add default site if one is not found in the document", None))
#if QT_CONFIG(tooltip)
        self.checkBox_20.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"If no building storey is found in the FreeCAD document, a default one will be added.\n"
"A building storey is not mandatory but a common practice to have at least one in the file.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_20.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Add default building storey if one is not found in the document", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"The units you want your IFC file to be exported to.\n"
"\n"
"Note that IFC files are ALWAYS written in metric units; imperial units\n"
"are only a conversion factor applied on top of them.\n"
"However, some BIM applications will use this factor to choose which\n"
"unit to work with when opening the file.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"IFC file units", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Metric", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Imperial", None))

#if QT_CONFIG(tooltip)
        self.comboBox_3.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"The units you want your IFC file to be exported to.\n"
"\n"
"Note that IFC files are ALWAYS written in metric units; imperial units\n"
"are only a conversion factor applied on top of them.\n"
"However, some BIM applications will use this factor to choose which\n"
"unit to work with when opening the file.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Check also native-IFC-specific preferences under BIM -> Native IFC", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"IFC standard compliance", None))
#if QT_CONFIG(tooltip)
        self.checkBox_21.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"If no building is found in the FreeCAD document, a default one will be added.\n"
"Warning: The IFC standard asks for at least one building in each file. By turning this option off, you will produce a non-standard IFC file.\n"
"However, at FreeCAD, we believe having a building should not be mandatory, and this option is there to have a chance to demonstrate our point of view.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_21.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Add default building if one is not found in the document", None))
#if QT_CONFIG(tooltip)
        self.checkBox_2.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"In FreeCAD, it is possible to nest groups inside buildings or storeys. If this option is disabled, FreeCAD groups will be saved as IfcGroups and aggregated to the building structure. Aggregating non-building elements such as IfcGroups is however not recommended by the IFC standards. It is therefore also possible to export these groups as IfcElementAssemblies, which produces an IFC-compliant file. However, at FreeCAD, we believe nesting groups inside structures should be possible, and this option is there to have a chance to demonstrate our point of view.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Export nested groups as assemblies", None))
    # retranslateUi

