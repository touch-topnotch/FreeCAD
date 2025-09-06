# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-dxf.ui'
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

class Ui_Gui_Dialog_DlgSettingsDraft(object):
    def setupUi(self, Gui__Dialog__DlgSettingsDraft):
        if not Gui__Dialog__DlgSettingsDraft.objectName():
            Gui__Dialog__DlgSettingsDraft.setObjectName(u"Gui__Dialog__DlgSettingsDraft")
        Gui__Dialog__DlgSettingsDraft.resize(600, 880)
        self.verticalLayout_Main = QVBoxLayout(Gui__Dialog__DlgSettingsDraft)
        self.verticalLayout_Main.setObjectName(u"verticalLayout_Main")
        self.groupBox_General = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_General.setObjectName(u"groupBox_General")
        self.verticalLayout_General = QVBoxLayout(self.groupBox_General)
        self.verticalLayout_General.setObjectName(u"verticalLayout_General")
        self.checkBox_dxfShowDialog = Gui_PrefCheckBox(self.groupBox_General)
        self.checkBox_dxfShowDialog.setObjectName(u"checkBox_dxfShowDialog")
        self.checkBox_dxfShowDialog.setChecked(True)
        self.checkBox_dxfShowDialog.setProperty(u"prefEntry", u"dxfShowDialog")
        self.checkBox_dxfShowDialog.setProperty(u"prefPath", u"Mod/Draft")

        self.verticalLayout_General.addWidget(self.checkBox_dxfShowDialog)

        self.checkBox_dxfUseLegacyImporter = Gui_PrefCheckBox(self.groupBox_General)
        self.checkBox_dxfUseLegacyImporter.setObjectName(u"checkBox_dxfUseLegacyImporter")
        self.checkBox_dxfUseLegacyImporter.setProperty(u"prefEntry", u"dxfUseLegacyImporter")
        self.checkBox_dxfUseLegacyImporter.setProperty(u"prefPath", u"Mod/Draft")

        self.verticalLayout_General.addWidget(self.checkBox_dxfUseLegacyImporter)

        self.checkBox_dxfUseLegacyExporter = Gui_PrefCheckBox(self.groupBox_General)
        self.checkBox_dxfUseLegacyExporter.setObjectName(u"checkBox_dxfUseLegacyExporter")
        self.checkBox_dxfUseLegacyExporter.setProperty(u"prefEntry", u"dxfUseLegacyExporter")
        self.checkBox_dxfUseLegacyExporter.setProperty(u"prefPath", u"Mod/Draft")

        self.verticalLayout_General.addWidget(self.checkBox_dxfUseLegacyExporter)


        self.verticalLayout_Main.addWidget(self.groupBox_General)

        self.groupBox_AutoUpdate = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_AutoUpdate.setObjectName(u"groupBox_AutoUpdate")
        self.verticalLayout_AutoUpdate = QVBoxLayout(self.groupBox_AutoUpdate)
        self.verticalLayout_AutoUpdate.setObjectName(u"verticalLayout_AutoUpdate")
        self.checkBox_dxfAllowDownload = Gui_PrefCheckBox(self.groupBox_AutoUpdate)
        self.checkBox_dxfAllowDownload.setObjectName(u"checkBox_dxfAllowDownload")
        self.checkBox_dxfAllowDownload.setProperty(u"prefEntry", u"dxfAllowDownload")
        self.checkBox_dxfAllowDownload.setProperty(u"prefPath", u"Mod/Draft")

        self.verticalLayout_AutoUpdate.addWidget(self.checkBox_dxfAllowDownload)


        self.verticalLayout_Main.addWidget(self.groupBox_AutoUpdate)

        self.groupBox_ImportAs = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_ImportAs.setObjectName(u"groupBox_ImportAs")
        self.verticalLayout_ImportAs = QVBoxLayout(self.groupBox_ImportAs)
        self.verticalLayout_ImportAs.setObjectName(u"verticalLayout_ImportAs")
        self.radio_ImportAs_Draft = Gui_PrefRadioButton(self.groupBox_ImportAs)
        self.radio_ImportAs_Draft.setObjectName(u"radio_ImportAs_Draft")
        self.radio_ImportAs_Draft.setEnabled(True)
        self.radio_ImportAs_Draft.setProperty(u"prefEntry", u"dxfImportAsDraft")
        self.radio_ImportAs_Draft.setProperty(u"prefPath", u"Mod/Draft")
        self.radio_ImportAs_Draft.setProperty(u"prefRadioButtonValue", 0)

        self.verticalLayout_ImportAs.addWidget(self.radio_ImportAs_Draft)

        self.radio_ImportAs_Primitives = Gui_PrefRadioButton(self.groupBox_ImportAs)
        self.radio_ImportAs_Primitives.setObjectName(u"radio_ImportAs_Primitives")
        self.radio_ImportAs_Primitives.setEnabled(True)
        self.radio_ImportAs_Primitives.setProperty(u"prefEntry", u"dxfImportAsPrimitives")
        self.radio_ImportAs_Primitives.setProperty(u"prefPath", u"Mod/Draft")
        self.radio_ImportAs_Primitives.setProperty(u"prefRadioButtonValue", 1)

        self.verticalLayout_ImportAs.addWidget(self.radio_ImportAs_Primitives)

        self.radio_ImportAs_Shapes = Gui_PrefRadioButton(self.groupBox_ImportAs)
        self.radio_ImportAs_Shapes.setObjectName(u"radio_ImportAs_Shapes")
        self.radio_ImportAs_Shapes.setChecked(True)
        self.radio_ImportAs_Shapes.setProperty(u"prefEntry", u"dxfImportAsShapes")
        self.radio_ImportAs_Shapes.setProperty(u"prefPath", u"Mod/Draft")
        self.radio_ImportAs_Shapes.setProperty(u"prefRadioButtonValue", 2)

        self.verticalLayout_ImportAs.addWidget(self.radio_ImportAs_Shapes)

        self.radio_ImportAs_Fused = Gui_PrefRadioButton(self.groupBox_ImportAs)
        self.radio_ImportAs_Fused.setObjectName(u"radio_ImportAs_Fused")
        self.radio_ImportAs_Fused.setProperty(u"prefEntry", u"dxfImportAsFused")
        self.radio_ImportAs_Fused.setProperty(u"prefPath", u"Mod/Draft")
        self.radio_ImportAs_Fused.setProperty(u"prefRadioButtonValue", 3)

        self.verticalLayout_ImportAs.addWidget(self.radio_ImportAs_Fused)


        self.verticalLayout_Main.addWidget(self.groupBox_ImportAs)

        self.groupBox_ImportSettings = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_ImportSettings.setObjectName(u"groupBox_ImportSettings")
        self.verticalLayout_ImportSettings = QVBoxLayout(self.groupBox_ImportSettings)
        self.verticalLayout_ImportSettings.setObjectName(u"verticalLayout_ImportSettings")
        self.horizontalLayout_Scaling = QHBoxLayout()
        self.horizontalLayout_Scaling.setObjectName(u"horizontalLayout_Scaling")
        self.label_dxfScaling = QLabel(self.groupBox_ImportSettings)
        self.label_dxfScaling.setObjectName(u"label_dxfScaling")

        self.horizontalLayout_Scaling.addWidget(self.label_dxfScaling)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Scaling.addItem(self.horizontalSpacer_1)

        self.spinBox_dxfScaling = Gui_PrefDoubleSpinBox(self.groupBox_ImportSettings)
        self.spinBox_dxfScaling.setObjectName(u"spinBox_dxfScaling")
        self.spinBox_dxfScaling.setDecimals(6)
        self.spinBox_dxfScaling.setMaximum(999999.999998999992386)
        self.spinBox_dxfScaling.setValue(1.000000000000000)
        self.spinBox_dxfScaling.setProperty(u"prefEntry", u"dxfScaling")
        self.spinBox_dxfScaling.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_Scaling.addWidget(self.spinBox_dxfScaling)


        self.verticalLayout_ImportSettings.addLayout(self.horizontalLayout_Scaling)

        self.label_ImportContent = QLabel(self.groupBox_ImportSettings)
        self.label_ImportContent.setObjectName(u"label_ImportContent")

        self.verticalLayout_ImportSettings.addWidget(self.label_ImportContent)

        self.gridLayout_Import = QGridLayout()
        self.gridLayout_Import.setObjectName(u"gridLayout_Import")
        self.checkBox_dxftext = Gui_PrefCheckBox(self.groupBox_ImportSettings)
        self.checkBox_dxftext.setObjectName(u"checkBox_dxftext")
        self.checkBox_dxftext.setProperty(u"prefEntry", u"dxftext")
        self.checkBox_dxftext.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_Import.addWidget(self.checkBox_dxftext, 0, 0, 1, 1)

        self.checkBox_dxfImportPoints = Gui_PrefCheckBox(self.groupBox_ImportSettings)
        self.checkBox_dxfImportPoints.setObjectName(u"checkBox_dxfImportPoints")
        self.checkBox_dxfImportPoints.setChecked(True)
        self.checkBox_dxfImportPoints.setProperty(u"prefEntry", u"dxfImportPoints")
        self.checkBox_dxfImportPoints.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_Import.addWidget(self.checkBox_dxfImportPoints, 0, 1, 1, 1)

        self.checkBox_dxflayout = Gui_PrefCheckBox(self.groupBox_ImportSettings)
        self.checkBox_dxflayout.setObjectName(u"checkBox_dxflayout")
        self.checkBox_dxflayout.setProperty(u"prefEntry", u"dxflayout")
        self.checkBox_dxflayout.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_Import.addWidget(self.checkBox_dxflayout, 1, 0, 1, 1)

        self.checkBox_dxfstarblocks = Gui_PrefCheckBox(self.groupBox_ImportSettings)
        self.checkBox_dxfstarblocks.setObjectName(u"checkBox_dxfstarblocks")
        self.checkBox_dxfstarblocks.setProperty(u"prefEntry", u"dxfstarblocks")
        self.checkBox_dxfstarblocks.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_Import.addWidget(self.checkBox_dxfstarblocks, 1, 1, 1, 1)

        self.checkBox_importDxfHatches = Gui_PrefCheckBox(self.groupBox_ImportSettings)
        self.checkBox_importDxfHatches.setObjectName(u"checkBox_importDxfHatches")
        self.checkBox_importDxfHatches.setEnabled(False)
        self.checkBox_importDxfHatches.setProperty(u"prefEntry", u"importDxfHatches")
        self.checkBox_importDxfHatches.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_Import.addWidget(self.checkBox_importDxfHatches, 2, 0, 1, 1)


        self.verticalLayout_ImportSettings.addLayout(self.gridLayout_Import)

        self.label_Appearance = QLabel(self.groupBox_ImportSettings)
        self.label_Appearance.setObjectName(u"label_Appearance")

        self.verticalLayout_ImportSettings.addWidget(self.label_Appearance)

        self.gridLayout_Appearance = QGridLayout()
        self.gridLayout_Appearance.setObjectName(u"gridLayout_Appearance")
        self.checkBox_dxfGetOriginalColors = Gui_PrefCheckBox(self.groupBox_ImportSettings)
        self.checkBox_dxfGetOriginalColors.setObjectName(u"checkBox_dxfGetOriginalColors")
        self.checkBox_dxfGetOriginalColors.setChecked(True)
        self.checkBox_dxfGetOriginalColors.setProperty(u"prefEntry", u"dxfGetOriginalColors")
        self.checkBox_dxfGetOriginalColors.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_Appearance.addWidget(self.checkBox_dxfGetOriginalColors, 0, 0, 1, 1)

        self.checkBox_dxfStdSize = Gui_PrefCheckBox(self.groupBox_ImportSettings)
        self.checkBox_dxfStdSize.setObjectName(u"checkBox_dxfStdSize")
        self.checkBox_dxfStdSize.setEnabled(False)
        self.checkBox_dxfStdSize.setProperty(u"prefEntry", u"dxfStdSize")
        self.checkBox_dxfStdSize.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_Appearance.addWidget(self.checkBox_dxfStdSize, 0, 1, 1, 1)


        self.verticalLayout_ImportSettings.addLayout(self.gridLayout_Appearance)

        self.label_AdvancedProcessing = QLabel(self.groupBox_ImportSettings)
        self.label_AdvancedProcessing.setObjectName(u"label_AdvancedProcessing")

        self.verticalLayout_ImportSettings.addWidget(self.label_AdvancedProcessing)

        self.gridLayout_Advanced = QGridLayout()
        self.gridLayout_Advanced.setObjectName(u"gridLayout_Advanced")
        self.checkBox_joingeometry = Gui_PrefCheckBox(self.groupBox_ImportSettings)
        self.checkBox_joingeometry.setObjectName(u"checkBox_joingeometry")
        self.checkBox_joingeometry.setEnabled(False)
        self.checkBox_joingeometry.setProperty(u"prefEntry", u"joingeometry")
        self.checkBox_joingeometry.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_Advanced.addWidget(self.checkBox_joingeometry, 0, 0, 1, 1)

        self.checkBox_renderPolylineWidth = Gui_PrefCheckBox(self.groupBox_ImportSettings)
        self.checkBox_renderPolylineWidth.setObjectName(u"checkBox_renderPolylineWidth")
        self.checkBox_renderPolylineWidth.setEnabled(False)
        self.checkBox_renderPolylineWidth.setProperty(u"prefEntry", u"renderPolylineWidth")
        self.checkBox_renderPolylineWidth.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_Advanced.addWidget(self.checkBox_renderPolylineWidth, 0, 1, 1, 1)

        self.checkBox_dxfCreateSketch = Gui_PrefCheckBox(self.groupBox_ImportSettings)
        self.checkBox_dxfCreateSketch.setObjectName(u"checkBox_dxfCreateSketch")
        self.checkBox_dxfCreateSketch.setEnabled(False)
        self.checkBox_dxfCreateSketch.setProperty(u"prefEntry", u"dxfCreateSketch")
        self.checkBox_dxfCreateSketch.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_Advanced.addWidget(self.checkBox_dxfCreateSketch, 1, 0, 1, 1)


        self.verticalLayout_ImportSettings.addLayout(self.gridLayout_Advanced)


        self.verticalLayout_Main.addWidget(self.groupBox_ImportSettings)

        self.groupBox_ExportOptions = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_ExportOptions.setObjectName(u"groupBox_ExportOptions")
        self.verticalLayout_Export = QVBoxLayout(self.groupBox_ExportOptions)
        self.verticalLayout_Export.setObjectName(u"verticalLayout_Export")
        self.horizontalLayout_Discretize = QHBoxLayout()
        self.horizontalLayout_Discretize.setObjectName(u"horizontalLayout_Discretize")
        self.checkBox_DiscretizeEllipses = Gui_PrefCheckBox(self.groupBox_ExportOptions)
        self.checkBox_DiscretizeEllipses.setObjectName(u"checkBox_DiscretizeEllipses")
        self.checkBox_DiscretizeEllipses.setChecked(True)
        self.checkBox_DiscretizeEllipses.setProperty(u"prefEntry", u"DiscretizeEllipses")
        self.checkBox_DiscretizeEllipses.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_Discretize.addWidget(self.checkBox_DiscretizeEllipses)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Discretize.addItem(self.horizontalSpacer_2)

        self.label_maxsegmentlength = QLabel(self.groupBox_ExportOptions)
        self.label_maxsegmentlength.setObjectName(u"label_maxsegmentlength")
        self.label_maxsegmentlength.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_Discretize.addWidget(self.label_maxsegmentlength)

        self.spinBox_maxsegmentlength = Gui_PrefDoubleSpinBox(self.groupBox_ExportOptions)
        self.spinBox_maxsegmentlength.setObjectName(u"spinBox_maxsegmentlength")
        self.spinBox_maxsegmentlength.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_maxsegmentlength.setMaximum(9999.989999999999782)
        self.spinBox_maxsegmentlength.setValue(5.000000000000000)
        self.spinBox_maxsegmentlength.setProperty(u"prefEntry", u"maxsegmentlength")
        self.spinBox_maxsegmentlength.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_Discretize.addWidget(self.spinBox_maxsegmentlength)


        self.verticalLayout_Export.addLayout(self.horizontalLayout_Discretize)

        self.horizontalLayout_Export3D = QHBoxLayout()
        self.horizontalLayout_Export3D.setObjectName(u"horizontalLayout_Export3D")
        self.checkBox_dxfmesh = Gui_PrefCheckBox(self.groupBox_ExportOptions)
        self.checkBox_dxfmesh.setObjectName(u"checkBox_dxfmesh")
        self.checkBox_dxfmesh.setEnabled(False)
        self.checkBox_dxfmesh.setProperty(u"prefEntry", u"dxfmesh")
        self.checkBox_dxfmesh.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_Export3D.addWidget(self.checkBox_dxfmesh)


        self.verticalLayout_Export.addLayout(self.horizontalLayout_Export3D)

        self.horizontalLayout_ExportTechDraw = QHBoxLayout()
        self.horizontalLayout_ExportTechDraw.setObjectName(u"horizontalLayout_ExportTechDraw")
        self.checkBox_dxfExportBlocks = Gui_PrefCheckBox(self.groupBox_ExportOptions)
        self.checkBox_dxfExportBlocks.setObjectName(u"checkBox_dxfExportBlocks")
        self.checkBox_dxfExportBlocks.setChecked(True)
        self.checkBox_dxfExportBlocks.setProperty(u"prefEntry", u"dxfExportBlocks")
        self.checkBox_dxfExportBlocks.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_ExportTechDraw.addWidget(self.checkBox_dxfExportBlocks)


        self.verticalLayout_Export.addLayout(self.horizontalLayout_ExportTechDraw)

        self.horizontalLayout_Project = QHBoxLayout()
        self.horizontalLayout_Project.setObjectName(u"horizontalLayout_Project")
        self.checkBox_dxfproject = Gui_PrefCheckBox(self.groupBox_ExportOptions)
        self.checkBox_dxfproject.setObjectName(u"checkBox_dxfproject")
        self.checkBox_dxfproject.setEnabled(False)
        self.checkBox_dxfproject.setProperty(u"prefEntry", u"dxfproject")
        self.checkBox_dxfproject.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_Project.addWidget(self.checkBox_dxfproject)


        self.verticalLayout_Export.addLayout(self.horizontalLayout_Project)


        self.verticalLayout_Main.addWidget(self.groupBox_ExportOptions)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_Main.addItem(self.verticalSpacer)


        self.retranslateUi(Gui__Dialog__DlgSettingsDraft)
        self.checkBox_dxfUseLegacyImporter.toggled.connect(self.checkBox_joingeometry.setEnabled)
        self.checkBox_dxfUseLegacyImporter.toggled.connect(self.checkBox_renderPolylineWidth.setEnabled)
        self.checkBox_dxfUseLegacyImporter.toggled.connect(self.checkBox_dxfStdSize.setEnabled)
        self.checkBox_dxfUseLegacyImporter.toggled.connect(self.checkBox_importDxfHatches.setEnabled)
        self.checkBox_dxfUseLegacyImporter.toggled.connect(self.checkBox_dxfCreateSketch.setEnabled)
        self.checkBox_dxfCreateSketch.toggled.connect(self.groupBox_ImportAs.setDisabled)
        self.checkBox_dxfUseLegacyExporter.toggled.connect(self.checkBox_dxfmesh.setEnabled)
        self.checkBox_dxfUseLegacyExporter.toggled.connect(self.checkBox_dxfproject.setEnabled)
        self.checkBox_dxfUseLegacyExporter.toggled.connect(self.checkBox_dxfmesh.setEnabled)
        self.checkBox_dxfUseLegacyExporter.toggled.connect(self.checkBox_dxfproject.setEnabled)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsDraft)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsDraft):
        Gui__Dialog__DlgSettingsDraft.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"DXF", None))
        self.groupBox_General.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"General", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfShowDialog.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, this preferences dialog will be shown each time you import or export\n"
"a DXF file.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfShowDialog.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Show the importer dialog when importing a file", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfUseLegacyImporter.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use the legacy Python importer. This importer is more feature-complete but slower and requires an external library.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfUseLegacyImporter.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use legacy importer", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfUseLegacyExporter.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use the legacy Python exporter. This exporter is more feature-complete but slower and requires an external library.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfUseLegacyExporter.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use legacy exporter", None))
        self.groupBox_AutoUpdate.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Automatic Update (Legacy Only)", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfAllowDownload.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, FreeCAD is allowed to download and update the Python libraries\n"
"required by the legacy importer. This can also be done manually by installing\n"
"the 'dxf_library' addon from the Addon Manager.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfAllowDownload.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Allow FreeCAD to automatically download and update the DXF libraries", None))
        self.groupBox_ImportAs.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Import As", None))
#if QT_CONFIG(tooltip)
        self.radio_ImportAs_Draft.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Creates fully parametric Draft objects. Block definitions are imported as\n"
"reusable objects (Part Compounds) and instances become `App::Link` objects,\n"
"maintaining the block structure. Best for full integration with the Draft\n"
"workbench. ", None))
#endif // QT_CONFIG(tooltip)
        self.radio_ImportAs_Draft.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Editable Draft objects (highest fidelity, slowest)", None))
        self.radio_ImportAs_Draft.setProperty(u"prefRadioButtonGroup", QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"DxfImportMode", None))
#if QT_CONFIG(tooltip)
        self.radio_ImportAs_Primitives.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Creates parametric Part objects (e.g., Part::Line, Part::Circle). Block\n"
"definitions are imported as reusable objects (Part Compounds) and instances\n"
"become `App::Link` objects, maintaining the block structure. Best for\n"
"script-based post-processing and Part workbench integration.", None))
#endif // QT_CONFIG(tooltip)
        self.radio_ImportAs_Primitives.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Editable Part primitives (high fidelity, slower)", None))
        self.radio_ImportAs_Primitives.setProperty(u"prefRadioButtonGroup", QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"DxfImportMode", None))
#if QT_CONFIG(tooltip)
        self.radio_ImportAs_Shapes.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Creates a non-parametric shape for each DXF entity. Block definitions are\n"
"imported as reusable objects (Part Compounds) and instances become `App::Link`\n"
"objects, maintaining the block structure. Good for referencing and measuring.", None))
#endif // QT_CONFIG(tooltip)
        self.radio_ImportAs_Shapes.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Individual Part shapes (balanced, recommended)", None))
        self.radio_ImportAs_Shapes.setProperty(u"prefRadioButtonGroup", QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"DxfImportMode", None))
#if QT_CONFIG(tooltip)
        self.radio_ImportAs_Fused.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Merges all geometry per layer into a single, non-editable shape. Block\n"
"structures are not preserved; their geometry becomes part of the layer's\n"
"shape. Best for importing and viewing very large files with maximum performance.", None))
#endif // QT_CONFIG(tooltip)
        self.radio_ImportAs_Fused.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Fused Part shapes (lowest fidelity, fastest)", None))
        self.radio_ImportAs_Fused.setProperty(u"prefRadioButtonGroup", QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"DxfImportMode", None))
        self.groupBox_ImportSettings.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Import Settings", None))
        self.label_dxfScaling.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Global scaling factor", None))
#if QT_CONFIG(tooltip)
        self.spinBox_dxfScaling.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Scale factor to apply to DXF files on import. The factor is the conversion\n"
"between the DXF file's unit and millimeters. Example: for files in\n"
"millimeters: 1, in centimeters: 10, in meters: 1000, in inches: 25.4,\n"
"in feet: 304.8", None))
#endif // QT_CONFIG(tooltip)
        self.label_ImportContent.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Import", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxftext.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, text, mtext, and dimension entities will be imported as Draft objects", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxftext.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Texts and dimensions", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfImportPoints.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, point entities will be imported", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfImportPoints.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Points", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxflayout.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, entities from the paper space will also be imported. By default,\n"
"only model space is imported", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxflayout.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Paper space objects", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfstarblocks.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, anonymous blocks (whose names begin with *) will also be imported.\n"
"These are often used for hatches and dimensions", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfstarblocks.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Anonymous blocks (*-blocks)", None))
#if QT_CONFIG(tooltip)
        self.checkBox_importDxfHatches.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, the boundaries of hatch objects will be imported as closed wires.\n"
"(Legacy importer only)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_importDxfHatches.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Hatch boundaries", None))
        self.label_Appearance.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Appearance", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfGetOriginalColors.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, colors will be set as specified in the DXF file whenever\n"
"possible. Otherwise, default FreeCAD colors are applied", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfGetOriginalColors.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use colors from the DXF file", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfStdSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, imported texts will get the standard Draft text size, instead of\n"
"the size defined in the DXF document. (Legacy importer only)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfStdSize.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use standard font size for texts", None))
        self.label_AdvancedProcessing.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Advanced processing", None))
#if QT_CONFIG(tooltip)
        self.checkBox_joingeometry.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, the legacy importer will attempt to join coincident geometric\n"
"objects into wires. This can be slow for large files. (Legacy importer only)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_joingeometry.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Join geometry", None))
#if QT_CONFIG(tooltip)
        self.checkBox_renderPolylineWidth.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, polylines that have a width property will be rendered as faces\n"
"representing that width. (Legacy importer only)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_renderPolylineWidth.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Render polylines with width", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfCreateSketch.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, the legacy importer will attempt to create Sketcher objects\n"
"instead of Draft or Part objects. This overrides the 'Import As' setting", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfCreateSketch.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Create sketches", None))
        self.groupBox_ExportOptions.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Export Options", None))
#if QT_CONFIG(tooltip)
        self.checkBox_DiscretizeEllipses.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Ellipse export is poorly supported. Use this to export them as polylines instead.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_DiscretizeEllipses.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Treat ellipses and splines as polylines", None))
        self.label_maxsegmentlength.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Maximum spline segment", None))
#if QT_CONFIG(tooltip)
        self.spinBox_maxsegmentlength.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Maximum length of each of the polyline segments. '0' treats the whole spline as a straight segment.", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_maxsegmentlength.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"mm", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfmesh.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"All objects containing faces will be exported as 3D polyface meshes", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfmesh.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Export 3D objects as polyface meshes", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfExportBlocks.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"TechDraw Views will be exported as blocks.\n"
"This might fail for post DXF R12 templates.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfExportBlocks.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Export TechDraw Views as blocks", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfproject.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Exported objects will be projected to reflect the current view direction", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfproject.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Project exported objects along current view direction", None))
    # retranslateUi

