# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-ifc.ui'
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
        Gui__Dialog__DlgSettingsArch.resize(555, 729)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsArch)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(9, 9, 9, 9)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.groupBox_3 = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_7 = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setProperty(u"prefEntry", u"ifcShowDialog")
        self.checkBox_7.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_3.addWidget(self.checkBox_7)

        self.gui__prefcheckbox_5 = Gui_PrefCheckBox(self.groupBox_3)
        self.gui__prefcheckbox_5.setObjectName(u"gui__prefcheckbox_5")
        self.gui__prefcheckbox_5.setProperty(u"prefEntry", u"ifcDebug")
        self.gui__prefcheckbox_5.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_3.addWidget(self.gui__prefcheckbox_5)

        self.checkBox_6 = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setProperty(u"prefEntry", u"ifcCreateClones")
        self.checkBox_6.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_3.addWidget(self.checkBox_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spinBox = Gui_PrefSpinBox(self.groupBox_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(120, 16777215))
        self.spinBox.setProperty(u"prefEntry", u"ifcMulticore")
        self.spinBox.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout.addWidget(self.spinBox)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(16, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.vboxLayout.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.comboBox = Gui_PrefComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setProperty(u"prefEntry", u"ifcImportModeArch")
        self.comboBox.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.comboBox_2 = Gui_PrefComboBox(self.groupBox_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setProperty(u"prefEntry", u"ifcImportModeStruct")
        self.comboBox_2.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout_5.addWidget(self.comboBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = Gui_PrefLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setText(u"IfcProduct")
        self.lineEdit_2.setProperty(u"prefEntry", u"ifcRootElement")
        self.lineEdit_2.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gui__prefcheckbox_6 = Gui_PrefCheckBox(self.groupBox_2)
        self.gui__prefcheckbox_6.setObjectName(u"gui__prefcheckbox_6")
        self.gui__prefcheckbox_6.setProperty(u"prefEntry", u"ifcSeparateOpenings")
        self.gui__prefcheckbox_6.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.gui__prefcheckbox_6)

        self.checkBox_2 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setProperty(u"prefEntry", u"ifcGetExtrusions")
        self.checkBox_2.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_11 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setProperty(u"prefEntry", u"ifcSplitLayers")
        self.checkBox_11.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_11)

        self.gui__prefcheckbox_7 = Gui_PrefCheckBox(self.groupBox_2)
        self.gui__prefcheckbox_7.setObjectName(u"gui__prefcheckbox_7")
        self.gui__prefcheckbox_7.setProperty(u"prefEntry", u"ifcPrefixNumbers")
        self.gui__prefcheckbox_7.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.gui__prefcheckbox_7)

        self.checkBox_3 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setProperty(u"prefEntry", u"ifcMergeMaterials")
        self.checkBox_3.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_8 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setProperty(u"prefEntry", u"ifcImportProperties")
        self.checkBox_8.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_8)

        self.checkBox_22 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_22.setObjectName(u"checkBox_22")
        self.checkBox_22.setProperty(u"prefEntry", u"ifcAllowInvalid")
        self.checkBox_22.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_22)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_13.addWidget(self.label_4)

        self.gui__preflineedit = Gui_PrefLineEdit(self.groupBox_2)
        self.gui__preflineedit.setObjectName(u"gui__preflineedit")
        self.gui__preflineedit.setProperty(u"prefEntry", u"ifcSkip")
        self.gui__preflineedit.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout_13.addWidget(self.gui__preflineedit)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.checkBox_14 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setProperty(u"prefEntry", u"ifcFitViewOnImport")
        self.checkBox_14.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_14)

        self.checkBox_18 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_18.setObjectName(u"checkBox_18")
        self.checkBox_18.setProperty(u"prefEntry", u"IfcImportFreeCADProperties")
        self.checkBox_18.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_18)

        self.checkBox = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setProperty(u"prefEntry", u"ifcReplaceProject")
        self.checkBox.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)


        self.vboxLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Gui__Dialog__DlgSettingsArch)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsArch)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsArch):
        Gui__Dialog__DlgSettingsArch.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"IFC import", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"General options", None))
        self.checkBox_7.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Show this dialog when importing", None))
#if QT_CONFIG(tooltip)
        self.gui__prefcheckbox_5.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Shows verbose debug messages during import and export\n"
"of IFC files in the Report view panel", None))
#endif // QT_CONFIG(tooltip)
        self.gui__prefcheckbox_5.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Show debug messages", None))
#if QT_CONFIG(tooltip)
        self.checkBox_6.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Clones are used when objects have shared geometry\n"
"One object is the base object, the others are clones.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_6.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Create clones when objects have shared geometry", None))
#if QT_CONFIG(tooltip)
        self.spinBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"EXPERIMENTAL\n"
"The number of cores to use in multicore mode.\n"
"Keep 0 to disable multicore mode.\n"
"The maximum value should be your number of cores minus 1,\n"
"for example, 3 if you have a 4-core CPU.\n"
"\n"
"Set it to 1 to use multicore mode in single-core mode; this is safer\n"
"if you start getting crashes when you set multiple cores.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"EXPERIMENTAL\n"
"The number of cores to use in multicore mode.\n"
"Keep 0 to disable multicore mode.\n"
"The maximum value should be your number of cores minus 1,\n"
"for example, 3 if you have a 4-core CPU.\n"
"\n"
"Set it to 1 to use multicore mode in single-core mode; this is safer\n"
"if you start getting crashes when you set multiple cores.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Number of cores to use (experimental)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Import options", None))
        self.label_5.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Import arch IFC objects as", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Parametric BIM objects", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Non-parametric BIM objects", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Simple Part shapes", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"One compound per floor", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Do not import Arch objects", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Specifies what kind of objects will be created in FreeCAD", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Import struct IFC objects as", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Non-parametric BIM objects", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Simple Part shapes", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"One compound for all", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Do not import structural objects", None))

#if QT_CONFIG(tooltip)
        self.comboBox_2.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Specifies what kind of objects will be created in FreeCAD", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Root element:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Only subtypes of the specified element will be imported.\n"
"Keep the element IfcProduct to import all building elements.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.gui__prefcheckbox_6.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Openings will be imported as subtractions, otherwise wall shapes\n"
"will already have their openings subtracted", None))
#endif // QT_CONFIG(tooltip)
        self.gui__prefcheckbox_6.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Separate openings", None))
#if QT_CONFIG(tooltip)
        self.checkBox_2.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"The importer will try to detect extrusions.\n"
"Note that this might slow things down.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Detect extrusions", None))
#if QT_CONFIG(tooltip)
        self.checkBox_11.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Split walls made of multiple layers", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_11.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Split multilayer walls", None))
#if QT_CONFIG(tooltip)
        self.gui__prefcheckbox_7.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Object names will be prefixed with the IFC ID number", None))
#endif // QT_CONFIG(tooltip)
        self.gui__prefcheckbox_7.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Prefix names with ID number", None))
#if QT_CONFIG(tooltip)
        self.checkBox_3.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"If several materials with the same name and color are found in the IFC file,\n"
"they will be treated as one.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Merge materials with same name and same color", None))
#if QT_CONFIG(tooltip)
        self.checkBox_8.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Each object will have their IFC properties stored in a spreadsheet object", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_8.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Import IFC properties in spreadsheet", None))
#if QT_CONFIG(tooltip)
        self.checkBox_22.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"IFC files can contain unclean or non-solid geometry. If this option is checked, all the geometry is imported, regardless of their validity.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_22.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Allow invalid shapes", None))
        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Exclude list:", None))
#if QT_CONFIG(tooltip)
        self.gui__preflineedit.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Comma-separated list of IFC entities to be excluded from imports", None))
#endif // QT_CONFIG(tooltip)
        self.gui__preflineedit.setText("")
        self.gui__preflineedit.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.checkBox_14.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Fit view during import on the imported objects.\n"
"This will slow down the import, but one can watch the import.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_14.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Fit view while importing", None))
#if QT_CONFIG(tooltip)
        self.checkBox_18.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Creates a full parametric model on import using stored\n"
"FreeCAD object properties", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_18.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Import full FreeCAD parametric definitions if available", None))
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"If this option is checked, the default 'Project', 'Site', 'Building', and 'Storeys'\n"
"objects that are usually found in an IFC file are not imported, and all objects\n"
"are placed in a 'Group' instead.\n"
"'Buildings' and 'Storeys' are still imported if there is more than one.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Replace 'Project', 'Site', 'Building', and 'Storey' with 'Group'", None))
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Check also native-IFC-specific preferences under BIM -> Native IFC", None))
    # retranslateUi

