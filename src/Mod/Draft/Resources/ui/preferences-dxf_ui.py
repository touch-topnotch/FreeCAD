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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsDraft(object):
    def setupUi(self, Gui__Dialog__DlgSettingsDraft):
        if not Gui__Dialog__DlgSettingsDraft.objectName():
            Gui__Dialog__DlgSettingsDraft.setObjectName(u"Gui__Dialog__DlgSettingsDraft")
        Gui__Dialog__DlgSettingsDraft.resize(649, 773)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsDraft)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(9, 9, 9, 9)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.checkBox_dxfShowDialog = Gui_PrefCheckBox(Gui__Dialog__DlgSettingsDraft)
        self.checkBox_dxfShowDialog.setObjectName(u"checkBox_dxfShowDialog")
        self.checkBox_dxfShowDialog.setChecked(True)
        self.checkBox_dxfShowDialog.setProperty(u"prefEntry", u"dxfShowDialog")
        self.checkBox_dxfShowDialog.setProperty(u"prefPath", u"Mod/Draft")

        self.vboxLayout.addWidget(self.checkBox_dxfShowDialog)

        self.checkBox_dxfUseLegacyImporter = Gui_PrefCheckBox(Gui__Dialog__DlgSettingsDraft)
        self.checkBox_dxfUseLegacyImporter.setObjectName(u"checkBox_dxfUseLegacyImporter")
        self.checkBox_dxfUseLegacyImporter.setChecked(False)
        self.checkBox_dxfUseLegacyImporter.setProperty(u"prefEntry", u"dxfUseLegacyImporter")
        self.checkBox_dxfUseLegacyImporter.setProperty(u"prefPath", u"Mod/Draft")

        self.vboxLayout.addWidget(self.checkBox_dxfUseLegacyImporter)

        self.checkBox_dxfUseLegacyExporter = Gui_PrefCheckBox(Gui__Dialog__DlgSettingsDraft)
        self.checkBox_dxfUseLegacyExporter.setObjectName(u"checkBox_dxfUseLegacyExporter")
        self.checkBox_dxfUseLegacyExporter.setProperty(u"prefEntry", u"dxfUseLegacyExporter")
        self.checkBox_dxfUseLegacyExporter.setProperty(u"prefPath", u"Mod/Draft")

        self.vboxLayout.addWidget(self.checkBox_dxfUseLegacyExporter)

        self.groupBox_1 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.verticalLayout_1 = QVBoxLayout(self.groupBox_1)
        self.verticalLayout_1.setSpacing(6)
        self.verticalLayout_1.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setSpacing(6)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.checkBox_dxfAllowDownload = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_dxfAllowDownload.setObjectName(u"checkBox_dxfAllowDownload")
        self.checkBox_dxfAllowDownload.setProperty(u"prefEntry", u"dxfAllowDownload")
        self.checkBox_dxfAllowDownload.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_1.addWidget(self.checkBox_dxfAllowDownload)


        self.verticalLayout_1.addLayout(self.horizontalLayout_1)


        self.vboxLayout.addWidget(self.groupBox_1)

        self.GroupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.GroupBox_2.setObjectName(u"GroupBox_2")
        self.vboxLayout1 = QVBoxLayout(self.GroupBox_2)
        self.vboxLayout1.setSpacing(6)
        self.vboxLayout1.setContentsMargins(11, 11, 11, 11)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.vboxLayout1.setContentsMargins(9, 9, 9, 9)
        self.label_ImporterMissing = QLabel(self.GroupBox_2)
        self.label_ImporterMissing.setObjectName(u"label_ImporterMissing")
        font = QFont()
        font.setItalic(True)
        self.label_ImporterMissing.setFont(font)

        self.vboxLayout1.addWidget(self.label_ImporterMissing)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_Import = QLabel(self.GroupBox_2)
        self.label_Import.setObjectName(u"label_Import")

        self.horizontalLayout_2.addWidget(self.label_Import)

        self.checkBox_dxftext = Gui_PrefCheckBox(self.GroupBox_2)
        self.checkBox_dxftext.setObjectName(u"checkBox_dxftext")
        self.checkBox_dxftext.setProperty(u"prefEntry", u"dxftext")
        self.checkBox_dxftext.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_2.addWidget(self.checkBox_dxftext)

        self.checkBox_dxfImportPoints = Gui_PrefCheckBox(self.GroupBox_2)
        self.checkBox_dxfImportPoints.setObjectName(u"checkBox_dxfImportPoints")
        self.checkBox_dxfImportPoints.setProperty(u"prefEntry", u"dxfImportPoints")
        self.checkBox_dxfImportPoints.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_2.addWidget(self.checkBox_dxfImportPoints)

        self.checkBox_dxflayout = Gui_PrefCheckBox(self.GroupBox_2)
        self.checkBox_dxflayout.setObjectName(u"checkBox_dxflayout")
        self.checkBox_dxflayout.setProperty(u"prefEntry", u"dxflayout")
        self.checkBox_dxflayout.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_2.addWidget(self.checkBox_dxflayout)

        self.checkBox_dxfstarblocks = Gui_PrefCheckBox(self.GroupBox_2)
        self.checkBox_dxfstarblocks.setObjectName(u"checkBox_dxfstarblocks")
        self.checkBox_dxfstarblocks.setProperty(u"prefEntry", u"dxfstarblocks")
        self.checkBox_dxfstarblocks.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_2.addWidget(self.checkBox_dxfstarblocks)


        self.vboxLayout1.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_Create = QLabel(self.GroupBox_2)
        self.label_Create.setObjectName(u"label_Create")
        self.label_Create.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.label_Create)

        self.radioButton_dxfCreatePart = Gui_PrefRadioButton(self.GroupBox_2)
        self.radioButton_dxfCreatePart.setObjectName(u"radioButton_dxfCreatePart")
        self.radioButton_dxfCreatePart.setEnabled(False)
        self.radioButton_dxfCreatePart.setChecked(True)
        self.radioButton_dxfCreatePart.setProperty(u"prefEntry", u"dxfCreatePart")
        self.radioButton_dxfCreatePart.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_3.addWidget(self.radioButton_dxfCreatePart)

        self.radioButton_dxfCreateDraft = Gui_PrefRadioButton(self.GroupBox_2)
        self.radioButton_dxfCreateDraft.setObjectName(u"radioButton_dxfCreateDraft")
        self.radioButton_dxfCreateDraft.setEnabled(False)
        self.radioButton_dxfCreateDraft.setProperty(u"prefEntry", u"dxfCreateDraft")
        self.radioButton_dxfCreateDraft.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_3.addWidget(self.radioButton_dxfCreateDraft)

        self.radioButton_dxfCreateSketch = Gui_PrefRadioButton(self.GroupBox_2)
        self.radioButton_dxfCreateSketch.setObjectName(u"radioButton_dxfCreateSketch")
        self.radioButton_dxfCreateSketch.setEnabled(False)
        self.radioButton_dxfCreateSketch.setProperty(u"prefEntry", u"dxfCreateSketch")
        self.radioButton_dxfCreateSketch.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_3.addWidget(self.radioButton_dxfCreateSketch)


        self.vboxLayout1.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_dxfScaling = QLabel(self.GroupBox_2)
        self.label_dxfScaling.setObjectName(u"label_dxfScaling")

        self.horizontalLayout_4.addWidget(self.label_dxfScaling)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_1)

        self.spinBox_dxfScaling = Gui_PrefDoubleSpinBox(self.GroupBox_2)
        self.spinBox_dxfScaling.setObjectName(u"spinBox_dxfScaling")
        self.spinBox_dxfScaling.setDecimals(12)
        self.spinBox_dxfScaling.setMaximum(999999.999998999992386)
        self.spinBox_dxfScaling.setValue(1.000000000000000)
        self.spinBox_dxfScaling.setProperty(u"prefEntry", u"dxfScaling")
        self.spinBox_dxfScaling.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_4.addWidget(self.spinBox_dxfScaling)


        self.vboxLayout1.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_dxfGetOriginalColors = Gui_PrefCheckBox(self.GroupBox_2)
        self.checkBox_dxfGetOriginalColors.setObjectName(u"checkBox_dxfGetOriginalColors")
        self.checkBox_dxfGetOriginalColors.setProperty(u"prefEntry", u"dxfGetOriginalColors")
        self.checkBox_dxfGetOriginalColors.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_5.addWidget(self.checkBox_dxfGetOriginalColors)


        self.vboxLayout1.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox_joingeometry = Gui_PrefCheckBox(self.GroupBox_2)
        self.checkBox_joingeometry.setObjectName(u"checkBox_joingeometry")
        self.checkBox_joingeometry.setEnabled(False)
        self.checkBox_joingeometry.setProperty(u"prefEntry", u"joingeometry")
        self.checkBox_joingeometry.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_6.addWidget(self.checkBox_joingeometry)


        self.vboxLayout1.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_groupLayers = Gui_PrefCheckBox(self.GroupBox_2)
        self.checkBox_groupLayers.setObjectName(u"checkBox_groupLayers")
        self.checkBox_groupLayers.setProperty(u"prefEntry", u"groupLayers")
        self.checkBox_groupLayers.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_7.addWidget(self.checkBox_groupLayers)


        self.vboxLayout1.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox_dxfStdSize = Gui_PrefCheckBox(self.GroupBox_2)
        self.checkBox_dxfStdSize.setObjectName(u"checkBox_dxfStdSize")
        self.checkBox_dxfStdSize.setEnabled(False)
        self.checkBox_dxfStdSize.setProperty(u"prefEntry", u"dxfStdSize")
        self.checkBox_dxfStdSize.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_8.addWidget(self.checkBox_dxfStdSize)


        self.vboxLayout1.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBox_dxfUseDraftVisGroups = Gui_PrefCheckBox(self.GroupBox_2)
        self.checkBox_dxfUseDraftVisGroups.setObjectName(u"checkBox_dxfUseDraftVisGroups")
        self.checkBox_dxfUseDraftVisGroups.setChecked(True)
        self.checkBox_dxfUseDraftVisGroups.setProperty(u"prefEntry", u"dxfUseDraftVisGroups")
        self.checkBox_dxfUseDraftVisGroups.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_9.addWidget(self.checkBox_dxfUseDraftVisGroups)


        self.vboxLayout1.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.checkBox_importDxfHatches = Gui_PrefCheckBox(self.GroupBox_2)
        self.checkBox_importDxfHatches.setObjectName(u"checkBox_importDxfHatches")
        self.checkBox_importDxfHatches.setEnabled(False)
        self.checkBox_importDxfHatches.setProperty(u"prefEntry", u"importDxfHatches")
        self.checkBox_importDxfHatches.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_10.addWidget(self.checkBox_importDxfHatches)


        self.vboxLayout1.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.checkBox_renderPolylineWidth = Gui_PrefCheckBox(self.GroupBox_2)
        self.checkBox_renderPolylineWidth.setObjectName(u"checkBox_renderPolylineWidth")
        self.checkBox_renderPolylineWidth.setEnabled(False)
        self.checkBox_renderPolylineWidth.setProperty(u"prefEntry", u"renderPolylineWidth")
        self.checkBox_renderPolylineWidth.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_11.addWidget(self.checkBox_renderPolylineWidth)


        self.vboxLayout1.addLayout(self.horizontalLayout_11)


        self.vboxLayout.addWidget(self.GroupBox_2)

        self.groupBox_3 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_ExporterMissing = QLabel(self.groupBox_3)
        self.label_ExporterMissing.setObjectName(u"label_ExporterMissing")
        self.label_ExporterMissing.setFont(font)

        self.verticalLayout_2.addWidget(self.label_ExporterMissing)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.checkBox_DiscretizeEllipses = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBox_DiscretizeEllipses.setObjectName(u"checkBox_DiscretizeEllipses")
        self.checkBox_DiscretizeEllipses.setChecked(True)
        self.checkBox_DiscretizeEllipses.setProperty(u"prefEntry", u"DiscretizeEllipses")
        self.checkBox_DiscretizeEllipses.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_12.addWidget(self.checkBox_DiscretizeEllipses)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.label_maxsegmentlength = QLabel(self.groupBox_3)
        self.label_maxsegmentlength.setObjectName(u"label_maxsegmentlength")
        self.label_maxsegmentlength.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_maxsegmentlength)

        self.spinBox_maxsegmentlength = Gui_PrefDoubleSpinBox(self.groupBox_3)
        self.spinBox_maxsegmentlength.setObjectName(u"spinBox_maxsegmentlength")
        self.spinBox_maxsegmentlength.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_maxsegmentlength.setMaximum(9999.989999999999782)
        self.spinBox_maxsegmentlength.setValue(5.000000000000000)
        self.spinBox_maxsegmentlength.setProperty(u"prefEntry", u"maxsegmentlength")
        self.spinBox_maxsegmentlength.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_12.addWidget(self.spinBox_maxsegmentlength)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.checkBox_dxfmesh = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBox_dxfmesh.setObjectName(u"checkBox_dxfmesh")
        self.checkBox_dxfmesh.setEnabled(False)
        self.checkBox_dxfmesh.setProperty(u"prefEntry", u"dxfmesh")
        self.checkBox_dxfmesh.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_13.addWidget(self.checkBox_dxfmesh)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.checkBox_dxfExportBlocks = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBox_dxfExportBlocks.setObjectName(u"checkBox_dxfExportBlocks")
        self.checkBox_dxfExportBlocks.setChecked(True)
        self.checkBox_dxfExportBlocks.setProperty(u"prefEntry", u"dxfExportBlocks")
        self.checkBox_dxfExportBlocks.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_14.addWidget(self.checkBox_dxfExportBlocks)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.checkBox_dxfproject = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBox_dxfproject.setObjectName(u"checkBox_dxfproject")
        self.checkBox_dxfproject.setEnabled(False)
        self.checkBox_dxfproject.setProperty(u"prefEntry", u"dxfproject")
        self.checkBox_dxfproject.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_15.addWidget(self.checkBox_dxfproject)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)


        self.vboxLayout.addWidget(self.groupBox_3)

        self.verticalSpacer_1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer_1)


        self.retranslateUi(Gui__Dialog__DlgSettingsDraft)
        self.checkBox_dxfUseLegacyImporter.toggled.connect(self.label_Create.setEnabled)
        self.checkBox_dxfUseLegacyImporter.toggled.connect(self.radioButton_dxfCreatePart.setEnabled)
        self.checkBox_dxfUseLegacyImporter.toggled.connect(self.radioButton_dxfCreateDraft.setEnabled)
        self.checkBox_dxfUseLegacyImporter.toggled.connect(self.radioButton_dxfCreateSketch.setEnabled)
        self.checkBox_dxfUseLegacyImporter.toggled.connect(self.checkBox_joingeometry.setEnabled)
        self.checkBox_dxfUseLegacyImporter.toggled.connect(self.checkBox_dxfStdSize.setEnabled)
        self.checkBox_dxfUseLegacyImporter.toggled.connect(self.checkBox_importDxfHatches.setEnabled)
        self.checkBox_dxfUseLegacyImporter.toggled.connect(self.checkBox_renderPolylineWidth.setEnabled)
        self.checkBox_dxfUseLegacyExporter.toggled.connect(self.checkBox_dxfmesh.setEnabled)
        self.checkBox_dxfUseLegacyExporter.toggled.connect(self.checkBox_dxfproject.setEnabled)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsDraft)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsDraft):
        Gui__Dialog__DlgSettingsDraft.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"DXF", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfShowDialog.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"This preferences dialog will be shown when importing/ exporting DXF files", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfShowDialog.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Show this dialog when importing and exporting", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfUseLegacyImporter.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Python importer is used, otherwise the newer C++ is used.\n"
"Note: C++ importer is faster, but is not as featureful yet", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfUseLegacyImporter.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use legacy Python importer", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfUseLegacyExporter.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Python exporter is used, otherwise the newer C++ is used.\n"
"Note: C++ exporter is faster, but is not as featureful yet", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfUseLegacyExporter.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use legacy Python exporter", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Automatic update (legacy importer/exporter only)", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfAllowDownload.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Allow FreeCAD to download the Python converter for DXF import and export.\n"
"You can also do this manually by installing the \"dxf_library\" workbench\n"
"from the Addon Manager.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfAllowDownload.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Allow FreeCAD to automatically download and update the DXF libraries", None))
        self.GroupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Import options", None))
        self.label_ImporterMissing.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Some options are not yet available for the new importer", None))
        self.label_Import.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Import", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxftext.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If unchecked, texts and mtexts won't be imported", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxftext.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Texts and dimensions", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfImportPoints.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If unchecked, points won't be imported", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfImportPoints.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"points", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxflayout.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, paper space objects will be imported too", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxflayout.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Layouts", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfstarblocks.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If you want the non-named blocks (beginning with a *) to be imported too", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfstarblocks.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"*blocks", None))
        self.label_Create.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Create", None))
#if QT_CONFIG(tooltip)
        self.radioButton_dxfCreatePart.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Only standard Part objects will be created (fastest)", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_dxfCreatePart.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Simple Part shapes", None))
#if QT_CONFIG(tooltip)
        self.radioButton_dxfCreateDraft.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Parametric Draft objects will be created whenever possible", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_dxfCreateDraft.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Draft objects", None))
#if QT_CONFIG(tooltip)
        self.radioButton_dxfCreateSketch.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Sketches will be created whenever possible", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_dxfCreateSketch.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Sketches", None))
#if QT_CONFIG(tooltip)
        self.label_dxfScaling.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_dxfScaling.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Scale factor to apply to imported files", None))
#if QT_CONFIG(tooltip)
        self.spinBox_dxfScaling.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Scale factor to apply to DXF files on import.\n"
"The factor is the conversion between the unit of your DXF file and millimeters.\n"
"Example: for files in millimeters: 1, in centimeters: 10,\n"
"                             in meters: 1000, in inches: 25.4, in feet: 304.8", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_dxfGetOriginalColors.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Colors will set as specified in the DXF file whenever possible.\n"
"Otherwise default colors will be applied.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfGetOriginalColors.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use colors from the DXF file", None))
#if QT_CONFIG(tooltip)
        self.checkBox_joingeometry.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"FreeCAD will try to join coincident objects into wires.\n"
"Note that this can take a while!", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_joingeometry.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Join geometry", None))
#if QT_CONFIG(tooltip)
        self.checkBox_groupLayers.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Objects from the same layers will be joined into Draft Blocks,\n"
"turning the display faster, but making them less easily editable.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_groupLayers.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Group layers into blocks", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfStdSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Imported texts will get the standard Draft Text size,\n"
"instead of the size they have in the DXF document", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfStdSize.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use standard font size for texts", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfUseDraftVisGroups.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If this is checked, DXF layers will be imported as Draft Layers", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_dxfUseDraftVisGroups.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use layers", None))
#if QT_CONFIG(tooltip)
        self.checkBox_importDxfHatches.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Hatches will be converted into simple wires", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_importDxfHatches.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Import hatch boundaries as wires", None))
#if QT_CONFIG(tooltip)
        self.checkBox_renderPolylineWidth.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If polylines have a width defined, they will be rendered\n"
"as closed wires with correct width", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_renderPolylineWidth.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Render polylines with width", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Export options", None))
        self.label_ExporterMissing.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Some options are not yet available for the new exporter", None))
#if QT_CONFIG(tooltip)
        self.checkBox_DiscretizeEllipses.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Ellipse export is poorly supported. Use this to export them as polylines instead.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_DiscretizeEllipses.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Treat ellipses and splines as polylines", None))
        self.label_maxsegmentlength.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Max Spline Segment:", None))
#if QT_CONFIG(tooltip)
        self.spinBox_maxsegmentlength.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Maximum length of each of the polyline segments.\n"
"If it is set to '0' the whole spline is treated as a straight segment.", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_maxsegmentlength.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"mm", None))
#if QT_CONFIG(tooltip)
        self.checkBox_dxfmesh.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"All objects containing faces will be exported as 3D polyfaces", None))
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

