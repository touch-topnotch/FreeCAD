# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPrefsTechDrawGeneral.ui'
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

class Ui_TechDrawGui_DlgPrefsTechDrawGeneralImp(object):
    def setupUi(self, TechDrawGui__DlgPrefsTechDrawGeneralImp):
        if not TechDrawGui__DlgPrefsTechDrawGeneralImp.objectName():
            TechDrawGui__DlgPrefsTechDrawGeneralImp.setObjectName(u"TechDrawGui__DlgPrefsTechDrawGeneralImp")
        TechDrawGui__DlgPrefsTechDrawGeneralImp.resize(676, 1200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__DlgPrefsTechDrawGeneralImp.sizePolicy().hasHeightForWidth())
        TechDrawGui__DlgPrefsTechDrawGeneralImp.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(TechDrawGui__DlgPrefsTechDrawGeneralImp)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gbMisc = QGroupBox(TechDrawGui__DlgPrefsTechDrawGeneralImp)
        self.gbMisc.setObjectName(u"gbMisc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gbMisc.sizePolicy().hasHeightForWidth())
        self.gbMisc.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.gbMisc)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cb_Global = Gui_PrefCheckBox(self.gbMisc)
        self.cb_Global.setObjectName(u"cb_Global")
        sizePolicy1.setHeightForWidth(self.cb_Global.sizePolicy().hasHeightForWidth())
        self.cb_Global.setSizePolicy(sizePolicy1)
        self.cb_Global.setChecked(True)
        self.cb_Global.setProperty(u"prefEntry", u"GlobalUpdateDrawings")
        self.cb_Global.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout_5.addWidget(self.cb_Global, 0, 0, 1, 1)

        self.cb_Override = Gui_PrefCheckBox(self.gbMisc)
        self.cb_Override.setObjectName(u"cb_Override")
        sizePolicy1.setHeightForWidth(self.cb_Override.sizePolicy().hasHeightForWidth())
        self.cb_Override.setSizePolicy(sizePolicy1)
        self.cb_Override.setChecked(True)
        self.cb_Override.setProperty(u"prefEntry", u"AllowPageOverride")
        self.cb_Override.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout_5.addWidget(self.cb_Override, 0, 1, 1, 1)

        self.cb_PageUpdate = Gui_PrefCheckBox(self.gbMisc)
        self.cb_PageUpdate.setObjectName(u"cb_PageUpdate")
        sizePolicy1.setHeightForWidth(self.cb_PageUpdate.sizePolicy().hasHeightForWidth())
        self.cb_PageUpdate.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setItalic(True)
        self.cb_PageUpdate.setFont(font)
        self.cb_PageUpdate.setChecked(True)
        self.cb_PageUpdate.setProperty(u"prefEntry", u"KeepPagesUpToDate")
        self.cb_PageUpdate.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout_5.addWidget(self.cb_PageUpdate, 1, 0, 1, 1)

        self.cb_AutoDist = Gui_PrefCheckBox(self.gbMisc)
        self.cb_AutoDist.setObjectName(u"cb_AutoDist")
        sizePolicy1.setHeightForWidth(self.cb_AutoDist.sizePolicy().hasHeightForWidth())
        self.cb_AutoDist.setSizePolicy(sizePolicy1)
        self.cb_AutoDist.setFont(font)
        self.cb_AutoDist.setChecked(True)
        self.cb_AutoDist.setProperty(u"prefEntry", u"AutoDist")
        self.cb_AutoDist.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.gridLayout_5.addWidget(self.cb_AutoDist, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_5)


        self.verticalLayout_3.addWidget(self.gbMisc)

        self.gb_Font = QGroupBox(TechDrawGui__DlgPrefsTechDrawGeneralImp)
        self.gb_Font.setObjectName(u"gb_Font")
        sizePolicy1.setHeightForWidth(self.gb_Font.sizePolicy().hasHeightForWidth())
        self.gb_Font.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.gb_Font)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_LabelFont = QLabel(self.gb_Font)
        self.lbl_LabelFont.setObjectName(u"lbl_LabelFont")
        self.lbl_LabelFont.setBaseSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.lbl_LabelFont, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.pfb_LabelFont = Gui_PrefFontBox(self.gb_Font)
        self.pfb_LabelFont.setObjectName(u"pfb_LabelFont")
        sizePolicy1.setHeightForWidth(self.pfb_LabelFont.sizePolicy().hasHeightForWidth())
        self.pfb_LabelFont.setSizePolicy(sizePolicy1)
        self.pfb_LabelFont.setBaseSize(QSize(0, 0))
        self.pfb_LabelFont.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        font1 = QFont()
        self.pfb_LabelFont.setCurrentFont(font1)
        self.pfb_LabelFont.setProperty(u"prefEntry", u"LabelFont")
        self.pfb_LabelFont.setProperty(u"prefPath", u"/Mod/TechDraw/Labels")

        self.gridLayout_2.addWidget(self.pfb_LabelFont, 0, 2, 1, 1)

        self.label_6 = QLabel(self.gb_Font)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 1, 1, 1, 1)

        self.plsb_LabelSize = Gui_PrefUnitSpinBox(self.gb_Font)
        self.plsb_LabelSize.setObjectName(u"plsb_LabelSize")
        sizePolicy1.setHeightForWidth(self.plsb_LabelSize.sizePolicy().hasHeightForWidth())
        self.plsb_LabelSize.setSizePolicy(sizePolicy1)
        self.plsb_LabelSize.setProperty(u"value", 8.000000000000000)
        self.plsb_LabelSize.setProperty(u"prefEntry", u"LabelSize")
        self.plsb_LabelSize.setProperty(u"prefPath", u"/Mod/TechDraw/Labels")

        self.gridLayout_2.addWidget(self.plsb_LabelSize, 1, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addWidget(self.gb_Font)

        self.groupBox_2 = QGroupBox(TechDrawGui__DlgPrefsTechDrawGeneralImp)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setBaseSize(QSize(0, 500))
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1)

        self.cbProjAngle = Gui_PrefComboBox(self.groupBox_2)
        self.cbProjAngle.addItem("")
        self.cbProjAngle.addItem("")
        self.cbProjAngle.addItem("")
        self.cbProjAngle.setObjectName(u"cbProjAngle")
        sizePolicy1.setHeightForWidth(self.cbProjAngle.sizePolicy().hasHeightForWidth())
        self.cbProjAngle.setSizePolicy(sizePolicy1)
        self.cbProjAngle.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.cbProjAngle.setProperty(u"prefEntry", u"ProjectionAngle")
        self.cbProjAngle.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout_6.addWidget(self.cbProjAngle, 0, 2, 1, 1)

        self.cbSectionLineStd = Gui_PrefComboBox(self.groupBox_2)
        self.cbSectionLineStd.addItem(u"ANSI")
        self.cbSectionLineStd.addItem(u"ISO")
        self.cbSectionLineStd.setObjectName(u"cbSectionLineStd")
        sizePolicy1.setHeightForWidth(self.cbSectionLineStd.sizePolicy().hasHeightForWidth())
        self.cbSectionLineStd.setSizePolicy(sizePolicy1)
        self.cbSectionLineStd.setProperty(u"prefEntry", u"SectionLineStandard")
        self.cbSectionLineStd.setProperty(u"prefPath", u"Mod/TechDraw/Standards")

        self.gridLayout_6.addWidget(self.cbSectionLineStd, 1, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        font2 = QFont()
        font2.setItalic(False)
        self.label_13.setFont(font2)

        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 1)

        self.verticalLayout.addLayout(self.gridLayout_6)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.gb_Templates = QGroupBox(TechDrawGui__DlgPrefsTechDrawGeneralImp)
        self.gb_Templates.setObjectName(u"gb_Templates")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gb_Templates.sizePolicy().hasHeightForWidth())
        self.gb_Templates.setSizePolicy(sizePolicy2)
        self.gridLayout_4 = QGridLayout(self.gb_Templates)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_7 = QSpacerItem(40, 22, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 1, 1, 2, 1)

        self.label_9 = QLabel(self.gb_Templates)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)

        self.pfc_HatchFile = Gui_PrefFileChooser(self.gb_Templates)
        self.pfc_HatchFile.setObjectName(u"pfc_HatchFile")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pfc_HatchFile.sizePolicy().hasHeightForWidth())
        self.pfc_HatchFile.setSizePolicy(sizePolicy3)
        self.pfc_HatchFile.setProperty(u"prefEntry", u"FileHatch")
        self.pfc_HatchFile.setProperty(u"prefPath", u"/Mod/TechDraw/Files")

        self.gridLayout_3.addWidget(self.pfc_HatchFile, 2, 2, 1, 1)

        self.pfc_LineGroup = Gui_PrefFileChooser(self.gb_Templates)
        self.pfc_LineGroup.setObjectName(u"pfc_LineGroup")
        sizePolicy3.setHeightForWidth(self.pfc_LineGroup.sizePolicy().hasHeightForWidth())
        self.pfc_LineGroup.setSizePolicy(sizePolicy3)
        self.pfc_LineGroup.setProperty(u"prefEntry", u"LineGroupFile")
        self.pfc_LineGroup.setProperty(u"prefPath", u"/Mod/TechDraw/Files")

        self.gridLayout_3.addWidget(self.pfc_LineGroup, 3, 2, 1, 1)

        self.pfc_DefTemp = Gui_PrefFileChooser(self.gb_Templates)
        self.pfc_DefTemp.setObjectName(u"pfc_DefTemp")
        sizePolicy3.setHeightForWidth(self.pfc_DefTemp.sizePolicy().hasHeightForWidth())
        self.pfc_DefTemp.setSizePolicy(sizePolicy3)
        self.pfc_DefTemp.setProperty(u"prefEntry", u"TemplateFile")
        self.pfc_DefTemp.setProperty(u"prefPath", u"/Mod/TechDraw/Files")

        self.gridLayout_3.addWidget(self.pfc_DefTemp, 0, 2, 1, 1)

        self.label_11 = QLabel(self.gb_Templates)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_3.addWidget(self.label_11, 4, 0, 1, 1)

        self.pfc_FilePattern = Gui_PrefFileChooser(self.gb_Templates)
        self.pfc_FilePattern.setObjectName(u"pfc_FilePattern")
        sizePolicy3.setHeightForWidth(self.pfc_FilePattern.sizePolicy().hasHeightForWidth())
        self.pfc_FilePattern.setSizePolicy(sizePolicy3)
        self.pfc_FilePattern.setProperty(u"prefEntry", u"FilePattern")
        self.pfc_FilePattern.setProperty(u"prefPath", u"/Mod/TechDraw/PAT")

        self.gridLayout_3.addWidget(self.pfc_FilePattern, 5, 2, 1, 1)

        self.pfc_Welding = Gui_PrefFileChooser(self.gb_Templates)
        self.pfc_Welding.setObjectName(u"pfc_Welding")
        sizePolicy3.setHeightForWidth(self.pfc_Welding.sizePolicy().hasHeightForWidth())
        self.pfc_Welding.setSizePolicy(sizePolicy3)
        self.pfc_Welding.setProperty(u"prefEntry", u"WeldingDir")
        self.pfc_Welding.setProperty(u"prefPath", u"/Mod/TechDraw/Files")

        self.gridLayout_3.addWidget(self.pfc_Welding, 4, 2, 1, 1)

        self.pfc_DefDir = Gui_PrefFileChooser(self.gb_Templates)
        self.pfc_DefDir.setObjectName(u"pfc_DefDir")
        sizePolicy3.setHeightForWidth(self.pfc_DefDir.sizePolicy().hasHeightForWidth())
        self.pfc_DefDir.setSizePolicy(sizePolicy3)
        self.pfc_DefDir.setProperty(u"prefEntry", u"TemplateDir")
        self.pfc_DefDir.setProperty(u"prefPath", u"/Mod/TechDraw/Files")

        self.gridLayout_3.addWidget(self.pfc_DefDir, 1, 2, 1, 1)

        self.label_2 = QLabel(self.gb_Templates)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.fcSymbolDir = Gui_PrefFileChooser(self.gb_Templates)
        self.fcSymbolDir.setObjectName(u"fcSymbolDir")
        sizePolicy3.setHeightForWidth(self.fcSymbolDir.sizePolicy().hasHeightForWidth())
        self.fcSymbolDir.setSizePolicy(sizePolicy3)
        self.fcSymbolDir.setProperty(u"prefEntry", u"DirSymbol")
        self.fcSymbolDir.setProperty(u"prefPath", u"/Mod/TechDraw/Files")

        self.gridLayout_3.addWidget(self.fcSymbolDir, 7, 2, 1, 1)

        self.lbl_Hatch = QLabel(self.gb_Templates)
        self.lbl_Hatch.setObjectName(u"lbl_Hatch")
        self.lbl_Hatch.setFont(font)

        self.gridLayout_3.addWidget(self.lbl_Hatch, 2, 0, 1, 1)

        self.label = QLabel(self.gb_Templates)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.gb_Templates)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_3.addWidget(self.label_5, 7, 0, 1, 1)

        self.le_NamePattern = Gui_PrefLineEdit(self.gb_Templates)
        self.le_NamePattern.setObjectName(u"le_NamePattern")
        sizePolicy3.setHeightForWidth(self.le_NamePattern.sizePolicy().hasHeightForWidth())
        self.le_NamePattern.setSizePolicy(sizePolicy3)
        self.le_NamePattern.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_NamePattern.setProperty(u"prefEntry", u"NamePattern")
        self.le_NamePattern.setProperty(u"prefPath", u"/Mod/TechDraw/PAT")

        self.gridLayout_3.addWidget(self.le_NamePattern, 6, 2, 1, 1)

        self.label_10 = QLabel(self.gb_Templates)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_8 = QLabel(self.gb_Templates)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_3.addWidget(self.label_8, 6, 0, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(2, 2)

        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.gb_Templates)

        self.gbGrid = QGroupBox(TechDrawGui__DlgPrefsTechDrawGeneralImp)
        self.gbGrid.setObjectName(u"gbGrid")
        self.verticalLayout_5 = QVBoxLayout(self.gbGrid)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.cb_ShowGrid = Gui_PrefCheckBox(self.gbGrid)
        self.cb_ShowGrid.setObjectName(u"cb_ShowGrid")
        self.cb_ShowGrid.setFont(font)
        self.cb_ShowGrid.setChecked(True)
        self.cb_ShowGrid.setProperty(u"prefEntry", u"showGrid")
        self.cb_ShowGrid.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.gridLayout.addWidget(self.cb_ShowGrid, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gbGrid)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.psb_GridSpacing = Gui_PrefUnitSpinBox(self.gbGrid)
        self.psb_GridSpacing.setObjectName(u"psb_GridSpacing")
        self.psb_GridSpacing.setProperty(u"value", 10.000000000000000)
        self.psb_GridSpacing.setProperty(u"prefEntry", u"gridSpacing")
        self.psb_GridSpacing.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.gridLayout.addWidget(self.psb_GridSpacing, 1, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)

        self.verticalLayout_5.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.gbGrid)

        self.gbSelection = QGroupBox(TechDrawGui__DlgPrefsTechDrawGeneralImp)
        self.gbSelection.setObjectName(u"gbSelection")
        sizePolicy1.setHeightForWidth(self.gbSelection.sizePolicy().hasHeightForWidth())
        self.gbSelection.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.gbSelection)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.cbMultiSelection = Gui_PrefCheckBox(self.gbSelection)
        self.cbMultiSelection.setObjectName(u"cbMultiSelection")
        sizePolicy1.setHeightForWidth(self.cbMultiSelection.sizePolicy().hasHeightForWidth())
        self.cbMultiSelection.setSizePolicy(sizePolicy1)
        self.cbMultiSelection.setChecked(False)
        self.cbMultiSelection.setProperty(u"prefEntry", u"multiSelection")
        self.cbMultiSelection.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout_7.addWidget(self.cbMultiSelection, 0, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_7)


        self.verticalLayout_3.addWidget(self.gbSelection)

        self.gbViewDefaut = QGroupBox(TechDrawGui__DlgPrefsTechDrawGeneralImp)
        self.gbViewDefaut.setObjectName(u"gbViewDefaut")
        sizePolicy2.setHeightForWidth(self.gbViewDefaut.sizePolicy().hasHeightForWidth())
        self.gbViewDefaut.setSizePolicy(sizePolicy2)
        self.verticalLayout_8 = QVBoxLayout(self.gbViewDefaut)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.cb_useCameraDirection = Gui_PrefCheckBox(self.gbViewDefaut)
        self.cb_useCameraDirection.setObjectName(u"cb_useCameraDirection")
        sizePolicy1.setHeightForWidth(self.cb_useCameraDirection.sizePolicy().hasHeightForWidth())
        self.cb_useCameraDirection.setSizePolicy(sizePolicy1)
        self.cb_useCameraDirection.setFont(font)
        self.cb_useCameraDirection.setProperty(u"prefEntry", u"UseCameraDirection")
        self.cb_useCameraDirection.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.verticalLayout_7.addWidget(self.cb_useCameraDirection)

        self.cb_alwaysShowLabel = Gui_PrefCheckBox(self.gbViewDefaut)
        self.cb_alwaysShowLabel.setObjectName(u"cb_alwaysShowLabel")
        self.cb_alwaysShowLabel.setFont(font)
        self.cb_alwaysShowLabel.setProperty(u"prefEntry", u"AlwaysShowLabel")
        self.cb_alwaysShowLabel.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.verticalLayout_7.addWidget(self.cb_alwaysShowLabel)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.verticalLayout_3.addWidget(self.gbViewDefaut)

        self.groupBox = QGroupBox(TechDrawGui__DlgPrefsTechDrawGeneralImp)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy4)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.cb_SnapViews = Gui_PrefCheckBox(self.groupBox)
        self.cb_SnapViews.setObjectName(u"cb_SnapViews")
        self.cb_SnapViews.setChecked(True)
        self.cb_SnapViews.setProperty(u"prefEntry", u"SnapViews")
        self.cb_SnapViews.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.gridLayout_8.addWidget(self.cb_SnapViews, 0, 0, 1, 1)

        self.cb_SnapHighlights = Gui_PrefCheckBox(self.groupBox)
        self.cb_SnapHighlights.setObjectName(u"cb_SnapHighlights")
        self.cb_SnapHighlights.setChecked(True)
        self.cb_SnapHighlights.setProperty(u"prefEntry", u"SnapHighlights")
        self.cb_SnapHighlights.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.gridLayout_8.addWidget(self.cb_SnapHighlights, 2, 0, 1, 1)

        self.psb_SnapFactor = Gui_PrefDoubleSpinBox(self.groupBox)
        self.psb_SnapFactor.setObjectName(u"psb_SnapFactor")
        self.psb_SnapFactor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.psb_SnapFactor.setValue(0.050000000000000)
        self.psb_SnapFactor.setProperty(u"prefEntry", u"SnapLimitFactor")
        self.psb_SnapFactor.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.gridLayout_8.addWidget(self.psb_SnapFactor, 1, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_8.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_8.addWidget(self.label_14, 3, 0, 1, 1)

        self.psb_HighlightSnapFactor = Gui_PrefDoubleSpinBox(self.groupBox)
        self.psb_HighlightSnapFactor.setObjectName(u"psb_HighlightSnapFactor")
        self.psb_HighlightSnapFactor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.psb_HighlightSnapFactor.setValue(0.600000000000000)
        self.psb_HighlightSnapFactor.setProperty(u"prefEntry", u"DetailSnapRadius")
        self.psb_HighlightSnapFactor.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.gridLayout_8.addWidget(self.psb_HighlightSnapFactor, 3, 2, 1, 1)

        self.gridLayout_8.setColumnStretch(0, 1)
        self.gridLayout_8.setColumnStretch(2, 2)

        self.verticalLayout_9.addLayout(self.gridLayout_8)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.label_12 = QLabel(TechDrawGui__DlgPrefsTechDrawGeneralImp)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(0, 64))
        self.label_12.setBaseSize(QSize(0, 64))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setItalic(False)
        self.label_12.setFont(font3)
        self.label_12.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_12)


        self.retranslateUi(TechDrawGui__DlgPrefsTechDrawGeneralImp)

        self.cbSectionLineStd.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TechDrawGui__DlgPrefsTechDrawGeneralImp)
    # setupUi

    def retranslateUi(self, TechDrawGui__DlgPrefsTechDrawGeneralImp):
        TechDrawGui__DlgPrefsTechDrawGeneralImp.setWindowTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"General", None))
#if QT_CONFIG(tooltip)
        TechDrawGui__DlgPrefsTechDrawGeneralImp.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.gbMisc.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Drawing Update", None))
#if QT_CONFIG(tooltip)
        self.cb_Global.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Whether or not pages are updated every time the 3D model is changed", None))
#endif // QT_CONFIG(tooltip)
        self.cb_Global.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Update with 3D (global policy)", None))
#if QT_CONFIG(tooltip)
        self.cb_Override.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Controls whether or not a page's 'Keep Updated' property\n"
"can override the global 'Update with 3D' parameter", None))
#endif // QT_CONFIG(tooltip)
        self.cb_Override.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Allow page override (global policy)", None))
#if QT_CONFIG(tooltip)
        self.cb_PageUpdate.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Keep drawing pages in sync with changes of 3D model in real time.\n"
"This can slow down the response time.", None))
#endif // QT_CONFIG(tooltip)
        self.cb_PageUpdate.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Keep page up to date", None))
#if QT_CONFIG(tooltip)
        self.cb_AutoDist.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Automatically distribute secondary views\n"
"for ProjectionGroups", None))
#endif // QT_CONFIG(tooltip)
        self.cb_AutoDist.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Auto-distribute secondary views", None))
        self.gb_Font.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Labels", None))
#if QT_CONFIG(tooltip)
        self.lbl_LabelFont.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"* This font is also used for dimensions.\n"
"   Changes have no effect on existing dimensions.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_LabelFont.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Label font*", None))
#if QT_CONFIG(tooltip)
        self.pfb_LabelFont.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Font for labels", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Label size", None))
#if QT_CONFIG(tooltip)
        self.plsb_LabelSize.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Label size", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Conventions", None))
        self.label_7.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Projection group angle", None))
        self.cbProjAngle.setItemText(0, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"First-angle", None))
        self.cbProjAngle.setItemText(1, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Third-angle", None))
        self.cbProjAngle.setItemText(2, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Page", None))

#if QT_CONFIG(tooltip)
        self.cbProjAngle.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Use first or third-angle multiview projection convention", None))
#endif // QT_CONFIG(tooltip)

#if QT_CONFIG(tooltip)
        self.cbSectionLineStd.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Standard to be used to draw section lines. This affects the position of arrows and symbol.", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Section line convention", None))
        self.gb_Templates.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Files", None))
        self.label_9.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"PAT file", None))
#if QT_CONFIG(tooltip)
        self.pfc_HatchFile.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Preferred SVG or bitmap file for hatching. This value will also control the initial directory for choosing hatch patterns. You can use this to get hatch files from a local directory.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pfc_LineGroup.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Alternate file for personal LineGroup definition", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pfc_DefTemp.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Default template file for new pages", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Welding directory", None))
#if QT_CONFIG(tooltip)
        self.pfc_FilePattern.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Default PAT pattern definition file for geometric hatching", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pfc_Welding.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Default directory for welding symbols", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pfc_DefDir.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Starting directory for 'Insert Page From Template' tool", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Template directory", None))
#if QT_CONFIG(tooltip)
        self.fcSymbolDir.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Alternate directory to search for SVG symbol files.", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_Hatch.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Hatch pattern file", None))
        self.label.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Default template", None))
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Symbol directory", None))
#if QT_CONFIG(tooltip)
        self.le_NamePattern.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Name of the default PAT pattern", None))
#endif // QT_CONFIG(tooltip)
        self.le_NamePattern.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Diamond", None))
        self.label_10.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Line group file", None))
        self.label_8.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Pattern name", None))
        self.gbGrid.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Grid", None))
#if QT_CONFIG(tooltip)
        self.cb_ShowGrid.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Set 'Show grid' property to true on new pages", None))
#endif // QT_CONFIG(tooltip)
        self.cb_ShowGrid.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Show grid", None))
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Grid spacing", None))
#if QT_CONFIG(tooltip)
        self.psb_GridSpacing.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Distance between page grid lines", None))
#endif // QT_CONFIG(tooltip)
        self.gbSelection.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Selection", None))
#if QT_CONFIG(tooltip)
        self.cbMultiSelection.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"If enabled, clicking without Ctrl does not clear existing vertex/edge/face selection", None))
#endif // QT_CONFIG(tooltip)
        self.cbMultiSelection.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Enable multi-selection mode", None))
        self.gbViewDefaut.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"View Defaults", None))
#if QT_CONFIG(tooltip)
        self.cb_useCameraDirection.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Uses the 3D camera direction (or normal of a selected face) as the view direction. Otherwise, views will be created as front views.", None))
#endif // QT_CONFIG(tooltip)
        self.cb_useCameraDirection.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Use 3D camera direction", None))
#if QT_CONFIG(tooltip)
        self.cb_alwaysShowLabel.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Displays view labels even when frames are suppressed", None))
#endif // QT_CONFIG(tooltip)
        self.cb_alwaysShowLabel.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Always Show Label", None))
        self.groupBox.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Snapping", None))
#if QT_CONFIG(tooltip)
        self.cb_SnapViews.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Snaps views into alignment when being dragged", None))
#endif // QT_CONFIG(tooltip)
        self.cb_SnapViews.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Snap view alignment", None))
#if QT_CONFIG(tooltip)
        self.cb_SnapHighlights.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Check this box if you want detail view highlights to snap to the nearest vertex when dragging in TaskDetail.", None))
#endif // QT_CONFIG(tooltip)
        self.cb_SnapHighlights.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Snap detail highlights", None))
#if QT_CONFIG(tooltip)
        self.psb_SnapFactor.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"When dragging a view, if it is within this fraction of view size of the correct alignment, it will snap into alignment.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"View snapping factor", None))
        self.label_14.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Highlight snapping factor", None))
#if QT_CONFIG(tooltip)
        self.psb_HighlightSnapFactor.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"Controls the snap radius for highlights. Vertex must be within this factor times the highlight size to be a snap target.", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawGeneralImp", u"<html><head/><body><p><span style=\" font-weight:600;\">Note:</span> Items in <span style=\" font-style:italic;\">italics</span> are default values for new objects. They have no effect on existing objects.</p></body></html>", None))
    # retranslateUi

