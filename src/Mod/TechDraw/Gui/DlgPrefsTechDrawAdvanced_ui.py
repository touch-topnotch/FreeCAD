# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPrefsTechDrawAdvanced.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_TechDrawGui_DlgPrefsTechDrawAdvancedImp(object):
    def setupUi(self, TechDrawGui__DlgPrefsTechDrawAdvancedImp):
        if not TechDrawGui__DlgPrefsTechDrawAdvancedImp.objectName():
            TechDrawGui__DlgPrefsTechDrawAdvancedImp.setObjectName(u"TechDrawGui__DlgPrefsTechDrawAdvancedImp")
        TechDrawGui__DlgPrefsTechDrawAdvancedImp.resize(700, 810)
        self.verticalLayout_2 = QVBoxLayout(TechDrawGui__DlgPrefsTechDrawAdvancedImp)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gbDim = QGroupBox(TechDrawGui__DlgPrefsTechDrawAdvancedImp)
        self.gbDim.setObjectName(u"gbDim")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbDim.sizePolicy().hasHeightForWidth())
        self.gbDim.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.gbDim)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cbSwitchWB = Gui_PrefCheckBox(self.gbDim)
        self.cbSwitchWB.setObjectName(u"cbSwitchWB")
        self.cbSwitchWB.setChecked(True)
        self.cbSwitchWB.setProperty(u"prefEntry", u"SwitchToWB")
        self.cbSwitchWB.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout.addWidget(self.cbSwitchWB, 3, 0, 1, 1)

        self.cbDebugSection = Gui_PrefCheckBox(self.gbDim)
        self.cbDebugSection.setObjectName(u"cbDebugSection")
        sizePolicy.setHeightForWidth(self.cbDebugSection.sizePolicy().hasHeightForWidth())
        self.cbDebugSection.setSizePolicy(sizePolicy)
        self.cbDebugSection.setProperty(u"prefEntry", u"debugSection")
        self.cbDebugSection.setProperty(u"prefPath", u"Mod/TechDraw/debug")

        self.gridLayout.addWidget(self.cbDebugSection, 4, 2, 1, 1)

        self.label_5 = QLabel(self.gbDim)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.cbNewFaceFinder = Gui_PrefCheckBox(self.gbDim)
        self.cbNewFaceFinder.setObjectName(u"cbNewFaceFinder")
        self.cbNewFaceFinder.setChecked(True)
        self.cbNewFaceFinder.setProperty(u"prefEntry", u"NewFaceFinder")
        self.cbNewFaceFinder.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout.addWidget(self.cbNewFaceFinder, 1, 0, 1, 1)

        self.cbDebugDetail = Gui_PrefCheckBox(self.gbDim)
        self.cbDebugDetail.setObjectName(u"cbDebugDetail")
        sizePolicy.setHeightForWidth(self.cbDebugDetail.sizePolicy().hasHeightForWidth())
        self.cbDebugDetail.setSizePolicy(sizePolicy)
        self.cbDebugDetail.setProperty(u"prefEntry", u"debugDetail")
        self.cbDebugDetail.setProperty(u"prefPath", u"Mod/TechDraw/debug")

        self.gridLayout.addWidget(self.cbDebugDetail, 5, 2, 1, 1)

        self.cbDetectFaces = Gui_PrefCheckBox(self.gbDim)
        self.cbDetectFaces.setObjectName(u"cbDetectFaces")
        sizePolicy.setHeightForWidth(self.cbDetectFaces.sizePolicy().hasHeightForWidth())
        self.cbDetectFaces.setSizePolicy(sizePolicy)
        self.cbDetectFaces.setChecked(True)
        self.cbDetectFaces.setProperty(u"prefEntry", u"HandleFaces")
        self.cbDetectFaces.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.gridLayout.addWidget(self.cbDetectFaces, 0, 0, 1, 1)

        self.cbAutoCorrectRefs = Gui_PrefCheckBox(self.gbDim)
        self.cbAutoCorrectRefs.setObjectName(u"cbAutoCorrectRefs")
        self.cbAutoCorrectRefs.setChecked(True)
        self.cbAutoCorrectRefs.setProperty(u"prefEntry", u"AutoCorrectRefs")
        self.cbAutoCorrectRefs.setProperty(u"prefPath", u"Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.cbAutoCorrectRefs, 1, 2, 1, 1)

        self.cbValidateShapes = Gui_PrefCheckBox(self.gbDim)
        self.cbValidateShapes.setObjectName(u"cbValidateShapes")
        self.cbValidateShapes.setProperty(u"prefEntry", u"CheckShapesBeforeUse")
        self.cbValidateShapes.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout.addWidget(self.cbValidateShapes, 4, 0, 1, 1)

        self.cbCrazyEdges = Gui_PrefCheckBox(self.gbDim)
        self.cbCrazyEdges.setObjectName(u"cbCrazyEdges")
        sizePolicy.setHeightForWidth(self.cbCrazyEdges.sizePolicy().hasHeightForWidth())
        self.cbCrazyEdges.setSizePolicy(sizePolicy)
        self.cbCrazyEdges.setProperty(u"prefEntry", u"allowCrazyEdge")
        self.cbCrazyEdges.setProperty(u"prefPath", u"Mod/TechDraw/debug")

        self.gridLayout.addWidget(self.cbCrazyEdges, 3, 2, 1, 1)

        self.cbReportProgress = Gui_PrefCheckBox(self.gbDim)
        self.cbReportProgress.setObjectName(u"cbReportProgress")
        self.cbReportProgress.setProperty(u"prefEntry", u"ReportProgress")
        self.cbReportProgress.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.gridLayout.addWidget(self.cbReportProgress, 0, 2, 1, 1)

        self.sbScrubCount = Gui_PrefSpinBox(self.gbDim)
        self.sbScrubCount.setObjectName(u"sbScrubCount")
        self.sbScrubCount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.sbScrubCount.setValue(1)
        self.sbScrubCount.setProperty(u"prefEntry", u"ScrubCount")
        self.sbScrubCount.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout.addWidget(self.sbScrubCount, 7, 2, 1, 1)

        self.label_3 = QLabel(self.gbDim)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setItalic(True)
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)

        self.label_4 = QLabel(self.gbDim)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)

        self.sbMaxPat = Gui_PrefSpinBox(self.gbDim)
        self.sbMaxPat.setObjectName(u"sbMaxPat")
        self.sbMaxPat.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.sbMaxPat.setMinimum(1)
        self.sbMaxPat.setMaximum(1000000)
        self.sbMaxPat.setSingleStep(100)
        self.sbMaxPat.setValue(10000)
        self.sbMaxPat.setProperty(u"prefEntry", u"MaxSeg")
        self.sbMaxPat.setProperty(u"prefPath", u"Mod/TechDraw/PAT")

        self.gridLayout.addWidget(self.sbMaxPat, 11, 2, 1, 1)

        self.label = QLabel(self.gbDim)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 10, 0, 1, 1)

        self.cbDebugBadShape = Gui_PrefCheckBox(self.gbDim)
        self.cbDebugBadShape.setObjectName(u"cbDebugBadShape")
        self.cbDebugBadShape.setProperty(u"prefEntry", u"debugBadShape")
        self.cbDebugBadShape.setProperty(u"prefPath", u"Mod/TechDraw/debug")

        self.gridLayout.addWidget(self.cbDebugBadShape, 5, 0, 1, 1)

        self.cbFuseBeforeSection = Gui_PrefCheckBox(self.gbDim)
        self.cbFuseBeforeSection.setObjectName(u"cbFuseBeforeSection")
        sizePolicy.setHeightForWidth(self.cbFuseBeforeSection.sizePolicy().hasHeightForWidth())
        self.cbFuseBeforeSection.setSizePolicy(sizePolicy)
        self.cbFuseBeforeSection.setFont(font)
        self.cbFuseBeforeSection.setProperty(u"prefEntry", u"SectionFuseFirst")
        self.cbFuseBeforeSection.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout.addWidget(self.cbFuseBeforeSection, 2, 2, 1, 1)

        self.pdsbMarkFuzz = Gui_PrefDoubleSpinBox(self.gbDim)
        self.pdsbMarkFuzz.setObjectName(u"pdsbMarkFuzz")
        sizePolicy.setHeightForWidth(self.pdsbMarkFuzz.sizePolicy().hasHeightForWidth())
        self.pdsbMarkFuzz.setSizePolicy(sizePolicy)
        self.pdsbMarkFuzz.setMinimumSize(QSize(174, 0))
        self.pdsbMarkFuzz.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.pdsbMarkFuzz.setValue(5.000000000000000)
        self.pdsbMarkFuzz.setProperty(u"prefEntry", u"MarkFuzz")
        self.pdsbMarkFuzz.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout.addWidget(self.pdsbMarkFuzz, 9, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 6, 1, 1, 1)

        self.pdsbEdgeFuzz = Gui_PrefDoubleSpinBox(self.gbDim)
        self.pdsbEdgeFuzz.setObjectName(u"pdsbEdgeFuzz")
        sizePolicy.setHeightForWidth(self.pdsbEdgeFuzz.sizePolicy().hasHeightForWidth())
        self.pdsbEdgeFuzz.setSizePolicy(sizePolicy)
        self.pdsbEdgeFuzz.setMinimumSize(QSize(174, 0))
        self.pdsbEdgeFuzz.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.pdsbEdgeFuzz.setValue(10.000000000000000)
        self.pdsbEdgeFuzz.setProperty(u"prefEntry", u"EdgeFuzz")
        self.pdsbEdgeFuzz.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout.addWidget(self.pdsbEdgeFuzz, 8, 2, 1, 1)

        self.cbShowSectionEdges = Gui_PrefCheckBox(self.gbDim)
        self.cbShowSectionEdges.setObjectName(u"cbShowSectionEdges")
        sizePolicy.setHeightForWidth(self.cbShowSectionEdges.sizePolicy().hasHeightForWidth())
        self.cbShowSectionEdges.setSizePolicy(sizePolicy)
        self.cbShowSectionEdges.setChecked(True)
        self.cbShowSectionEdges.setProperty(u"prefEntry", u"ShowSectionEdges")
        self.cbShowSectionEdges.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.gridLayout.addWidget(self.cbShowSectionEdges, 2, 0, 1, 1)

        self.label_2 = QLabel(self.gbDim)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 11, 0, 1, 1)

        self.sbMaxTiles = Gui_PrefSpinBox(self.gbDim)
        self.sbMaxTiles.setObjectName(u"sbMaxTiles")
        self.sbMaxTiles.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.sbMaxTiles.setMinimum(1)
        self.sbMaxTiles.setMaximum(1000000)
        self.sbMaxTiles.setSingleStep(100)
        self.sbMaxTiles.setValue(10000)
        self.sbMaxTiles.setProperty(u"prefEntry", u"MaxSVGTile")
        self.sbMaxTiles.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout.addWidget(self.sbMaxTiles, 10, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)

        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.gbDim)

        self.gbBehaviour = QGroupBox(TechDrawGui__DlgPrefsTechDrawAdvancedImp)
        self.gbBehaviour.setObjectName(u"gbBehaviour")
        self.verticalLayout_3 = QVBoxLayout(self.gbBehaviour)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cbBalloonDefault = QCheckBox(self.gbBehaviour)
        self.cbBalloonDefault.setObjectName(u"cbBalloonDefault")
        self.cbBalloonDefault.setChecked(True)

        self.gridLayout_2.addWidget(self.cbBalloonDefault, 1, 0, 1, 1)

        self.label_8 = QLabel(self.gbBehaviour)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_6 = QLabel(self.gbBehaviour)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.cbBalloonAlt = QCheckBox(self.gbBehaviour)
        self.cbBalloonAlt.setObjectName(u"cbBalloonAlt")

        self.gridLayout_2.addWidget(self.cbBalloonAlt, 1, 1, 1, 1)

        self.cbBalloonShift = QCheckBox(self.gbBehaviour)
        self.cbBalloonShift.setObjectName(u"cbBalloonShift")

        self.gridLayout_2.addWidget(self.cbBalloonShift, 0, 1, 1, 1)

        self.cbBalloonMeta = QCheckBox(self.gbBehaviour)
        self.cbBalloonMeta.setObjectName(u"cbBalloonMeta")

        self.gridLayout_2.addWidget(self.cbBalloonMeta, 1, 2, 1, 1)

        self.cbBalloonControl = QCheckBox(self.gbBehaviour)
        self.cbBalloonControl.setObjectName(u"cbBalloonControl")

        self.gridLayout_2.addWidget(self.cbBalloonControl, 0, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addWidget(self.gbBehaviour)

        self.label_17 = QLabel(TechDrawGui__DlgPrefsTechDrawAdvancedImp)
        self.label_17.setObjectName(u"label_17")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setItalic(False)
        self.label_17.setFont(font1)
        self.label_17.setTextFormat(Qt.TextFormat.RichText)
        self.label_17.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_17)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(TechDrawGui__DlgPrefsTechDrawAdvancedImp)

        QMetaObject.connectSlotsByName(TechDrawGui__DlgPrefsTechDrawAdvancedImp)
    # setupUi

    def retranslateUi(self, TechDrawGui__DlgPrefsTechDrawAdvancedImp):
        TechDrawGui__DlgPrefsTechDrawAdvancedImp.setWindowTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Advanced", None))
        self.gbDim.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Advanced", None))
#if QT_CONFIG(tooltip)
        self.cbSwitchWB.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"If this box is checked, double-clicking on a page in the tree will automatically switch to TechDraw and the page will be made visible.", None))
#endif // QT_CONFIG(tooltip)
        self.cbSwitchWB.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Switch workbench on click", None))
#if QT_CONFIG(tooltip)
        self.cbDebugSection.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Dump intermediate results during section view processing", None))
#endif // QT_CONFIG(tooltip)
        self.cbDebugSection.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Debug section", None))
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Edge fuzz", None))
#if QT_CONFIG(tooltip)
        self.cbNewFaceFinder.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"If checked, FreeCAD will use the new face finder algorithm. If not checked, FreeCAD will use the legacy face finder algorithm.", None))
#endif // QT_CONFIG(tooltip)
        self.cbNewFaceFinder.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Use new face finder algorithm", None))
#if QT_CONFIG(tooltip)
        self.cbDebugDetail.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Dump intermediate results during detail view processing", None))
#endif // QT_CONFIG(tooltip)
        self.cbDebugDetail.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Debug detail", None))
#if QT_CONFIG(tooltip)
        self.cbDetectFaces.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"If checked, TechDraw will attempt to build faces using the\n"
"line segments returned by the hidden line removal algorithm.\n"
"Faces must be detected in order to use hatching, but there\n"
"can be a performance penalty in complex models.", None))
#endif // QT_CONFIG(tooltip)
        self.cbDetectFaces.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Detect faces", None))
#if QT_CONFIG(tooltip)
        self.cbAutoCorrectRefs.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"If checked, the system will attempt to automatically correct dimension references when the model changes.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.cbAutoCorrectRefs.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.cbAutoCorrectRefs.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Auto-correct dimension references", None))
#if QT_CONFIG(tooltip)
        self.cbValidateShapes.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"If checked, input shapes will be checked for errors before use and invalid shapes will be skipped by the shape extractor. Checking for errors is slower, but can prevent crashes from some geometry problems.\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.cbValidateShapes.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Validate shapes", None))
#if QT_CONFIG(tooltip)
        self.cbCrazyEdges.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Include edges with unexpected geometry (zero length etc.) in results", None))
#endif // QT_CONFIG(tooltip)
        self.cbCrazyEdges.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Allow crazy edges", None))
#if QT_CONFIG(tooltip)
        self.cbReportProgress.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Issue progress messages while building view geometry", None))
#endif // QT_CONFIG(tooltip)
        self.cbReportProgress.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Report progress", None))
#if QT_CONFIG(tooltip)
        self.sbScrubCount.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"The number of times FreeCAD should try to remove overlapping edges returned by the hidden line removal algorithm. A value of 0 indicates no scrubbing, 1 indicates a single pass and 2 indicates a second pass should be performed. Values above 2 are generally not productive. Each pass adds to the time required to produce the drawing.", None))
#endif // QT_CONFIG(tooltip)
        self.sbScrubCount.setSuffix("")
        self.sbScrubCount.setPrefix("")
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Overlap edges scrub passes", None))
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Mark fuzz", None))
#if QT_CONFIG(tooltip)
        self.sbMaxPat.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Maximum hatch line segments to use\n"
"when hatching a face with a PAT pattern", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Max SVG hatch tiles", None))
#if QT_CONFIG(tooltip)
        self.cbDebugBadShape.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"If checked, shapes that fail validation will be saved as BREP files for later analysis.", None))
#endif // QT_CONFIG(tooltip)
        self.cbDebugBadShape.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Debug bad shape", None))
#if QT_CONFIG(tooltip)
        self.cbFuseBeforeSection.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Perform a fuse operation on input shapes before section view processing", None))
#endif // QT_CONFIG(tooltip)
        self.cbFuseBeforeSection.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Fuse before section", None))
#if QT_CONFIG(tooltip)
        self.pdsbMarkFuzz.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Selection area around center marks\n"
"Each unit is approx. 0.1 mm wide", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pdsbMarkFuzz.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.pdsbEdgeFuzz.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Size of selection area around edges\n"
"Each unit is approximately 0.1mm wide", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pdsbEdgeFuzz.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.cbShowSectionEdges.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Highlights border of section cut in section views", None))
#endif // QT_CONFIG(tooltip)
        self.cbShowSectionEdges.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Show section edges", None))
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Maximum PAT hatch segments", None))
#if QT_CONFIG(tooltip)
        self.sbMaxTiles.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Limits the number of 64\u00d764 pixel SVG tiles used to hatch a single face.\n"
"For large scales, errors may occur due to excessive tiling.\n"
"Increase the limit if necessary.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.gbBehaviour.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Choose non-conflicting key bindings as some combinations of OS and navigation style key bindings may conflict with the default modifier keys for balloon dragging and view snapping override.", None))
#endif // QT_CONFIG(tooltip)
        self.gbBehaviour.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Behaviour Overrides", None))
#if QT_CONFIG(tooltip)
        self.cbBalloonDefault.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Check this box to use the default modifier keys. Uncheck this box to set a different key combination.", None))
#endif // QT_CONFIG(tooltip)
        self.cbBalloonDefault.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Use default", None))
        self.label_8.setText("")
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Balloon drag", None))
#if QT_CONFIG(tooltip)
        self.cbBalloonAlt.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Check this box to include the Alt key in the modifiers.", None))
#endif // QT_CONFIG(tooltip)
        self.cbBalloonAlt.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Alt", None))
#if QT_CONFIG(tooltip)
        self.cbBalloonShift.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Check this box to include the Shift key in the modifiers.", None))
#endif // QT_CONFIG(tooltip)
        self.cbBalloonShift.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Shift", None))
#if QT_CONFIG(tooltip)
        self.cbBalloonMeta.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Check this box to include the Meta/Start/Super key in the modifiers.", None))
#endif // QT_CONFIG(tooltip)
        self.cbBalloonMeta.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Meta", None))
#if QT_CONFIG(tooltip)
        self.cbBalloonControl.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Check this box to include the Control key in the modifiers.", None))
#endif // QT_CONFIG(tooltip)
        self.cbBalloonControl.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"Control", None))
        self.label_17.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAdvancedImp", u"<html><head/><body><p><span style=\" font-weight:600;\">Note:</span> Items in <span style=\" font-style:italic;\">italics</span> are default values for new objects. They have no effect on existing objects.</p></body></html>", None))
    # retranslateUi

