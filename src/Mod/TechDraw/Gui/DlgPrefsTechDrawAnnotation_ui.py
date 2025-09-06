# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPrefsTechDrawAnnotation.ui'
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

class Ui_TechDrawGui_DlgPrefsTechDrawAnnotationImp(object):
    def setupUi(self, TechDrawGui__DlgPrefsTechDrawAnnotationImp):
        if not TechDrawGui__DlgPrefsTechDrawAnnotationImp.objectName():
            TechDrawGui__DlgPrefsTechDrawAnnotationImp.setObjectName(u"TechDrawGui__DlgPrefsTechDrawAnnotationImp")
        TechDrawGui__DlgPrefsTechDrawAnnotationImp.resize(835, 956)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__DlgPrefsTechDrawAnnotationImp.sizePolicy().hasHeightForWidth())
        TechDrawGui__DlgPrefsTechDrawAnnotationImp.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(TechDrawGui__DlgPrefsTechDrawAnnotationImp)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(TechDrawGui__DlgPrefsTechDrawAnnotationImp)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cbPrintCenterMarks = Gui_PrefCheckBox(self.groupBox)
        self.cbPrintCenterMarks.setObjectName(u"cbPrintCenterMarks")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbPrintCenterMarks.sizePolicy().hasHeightForWidth())
        self.cbPrintCenterMarks.setSizePolicy(sizePolicy1)
        self.cbPrintCenterMarks.setProperty(u"prefEntry", u"PrintCenterMarks")
        self.cbPrintCenterMarks.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout_2.addWidget(self.cbPrintCenterMarks, 12, 2, 1, 1)

        self.cbShowCenterMarks = Gui_PrefCheckBox(self.groupBox)
        self.cbShowCenterMarks.setObjectName(u"cbShowCenterMarks")
        sizePolicy1.setHeightForWidth(self.cbShowCenterMarks.sizePolicy().hasHeightForWidth())
        self.cbShowCenterMarks.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setItalic(True)
        self.cbShowCenterMarks.setFont(font)
        self.cbShowCenterMarks.setChecked(True)
        self.cbShowCenterMarks.setProperty(u"prefEntry", u"ShowCenterMarks")
        self.cbShowCenterMarks.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout_2.addWidget(self.cbShowCenterMarks, 12, 0, 1, 1)

        self.cb_ShowSectionLine = Gui_PrefCheckBox(self.groupBox)
        self.cb_ShowSectionLine.setObjectName(u"cb_ShowSectionLine")
        self.cb_ShowSectionLine.setFont(font)
        self.cb_ShowSectionLine.setChecked(True)
        self.cb_ShowSectionLine.setProperty(u"prefEntry", u"ShowSectionLine")
        self.cb_ShowSectionLine.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout_2.addWidget(self.cb_ShowSectionLine, 1, 0, 1, 1)

        self.pcbBalloonShape = Gui_PrefComboBox(self.groupBox)
        self.pcbBalloonShape.setObjectName(u"pcbBalloonShape")
        sizePolicy1.setHeightForWidth(self.pcbBalloonShape.sizePolicy().hasHeightForWidth())
        self.pcbBalloonShape.setSizePolicy(sizePolicy1)
        self.pcbBalloonShape.setProperty(u"prefEntry", u"BalloonShape")
        self.pcbBalloonShape.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout_2.addWidget(self.pcbBalloonShape, 7, 2, 1, 1)

        self.cb_IncludeCutLine = Gui_PrefCheckBox(self.groupBox)
        self.cb_IncludeCutLine.setObjectName(u"cb_IncludeCutLine")
        self.cb_IncludeCutLine.setFont(font)
        self.cb_IncludeCutLine.setChecked(True)
        self.cb_IncludeCutLine.setProperty(u"prefEntry", u"IncludeCutLine")
        self.cb_IncludeCutLine.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout_2.addWidget(self.cb_IncludeCutLine, 2, 0, 1, 1)

        self.pcbBalloonArrow = Gui_PrefComboBox(self.groupBox)
        self.pcbBalloonArrow.setObjectName(u"pcbBalloonArrow")
        sizePolicy1.setHeightForWidth(self.pcbBalloonArrow.sizePolicy().hasHeightForWidth())
        self.pcbBalloonArrow.setSizePolicy(sizePolicy1)
        self.pcbBalloonArrow.setProperty(u"prefEntry", u"BalloonArrow")
        self.pcbBalloonArrow.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout_2.addWidget(self.pcbBalloonArrow, 8, 2, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.gridLayout_2.addWidget(self.label_18, 9, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_2.addWidget(self.label_11, 11, 0, 1, 1)

        self.cbPyramidOrtho = Gui_PrefCheckBox(self.groupBox)
        self.cbPyramidOrtho.setObjectName(u"cbPyramidOrtho")
        sizePolicy1.setHeightForWidth(self.cbPyramidOrtho.sizePolicy().hasHeightForWidth())
        self.cbPyramidOrtho.setSizePolicy(sizePolicy1)
        self.cbPyramidOrtho.setChecked(True)
        self.cbPyramidOrtho.setProperty(u"prefEntry", u"PyramidOrtho")
        self.cbPyramidOrtho.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout_2.addWidget(self.cbPyramidOrtho, 10, 0, 1, 1)

        self.cbCutSurface = Gui_PrefComboBox(self.groupBox)
        self.cbCutSurface.addItem("")
        self.cbCutSurface.addItem("")
        self.cbCutSurface.addItem("")
        self.cbCutSurface.addItem("")
        self.cbCutSurface.setObjectName(u"cbCutSurface")
        self.cbCutSurface.setProperty(u"prefEntry", u"CutSurfaceDisplay")
        self.cbCutSurface.setProperty(u"prefPath", u"/Mod/TechDraw/Decorations")

        self.gridLayout_2.addWidget(self.cbCutSurface, 0, 2, 1, 1)

        self.pcbDetailMatting = Gui_PrefCheckBox(self.groupBox)
        self.pcbDetailMatting.setObjectName(u"pcbDetailMatting")
        self.pcbDetailMatting.setChecked(True)
        self.pcbDetailMatting.setProperty(u"prefEntry", u"ShowDetailMatting")
        self.pcbDetailMatting.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.gridLayout_2.addWidget(self.pcbDetailMatting, 5, 0, 1, 1)

        self.pcbDetailHighlight = Gui_PrefCheckBox(self.groupBox)
        self.pcbDetailHighlight.setObjectName(u"pcbDetailHighlight")
        self.pcbDetailHighlight.setChecked(True)
        self.pcbDetailHighlight.setProperty(u"prefEntry", u"ShowDetailHighlight")
        self.pcbDetailHighlight.setProperty(u"prefPath", u"/Mod/TechDraw/General")

        self.gridLayout_2.addWidget(self.pcbDetailHighlight, 6, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setItalic(False)
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)

        self.cbAutoHoriz = Gui_PrefCheckBox(self.groupBox)
        self.cbAutoHoriz.setObjectName(u"cbAutoHoriz")
        sizePolicy1.setHeightForWidth(self.cbAutoHoriz.sizePolicy().hasHeightForWidth())
        self.cbAutoHoriz.setSizePolicy(sizePolicy1)
        self.cbAutoHoriz.setFont(font)
        self.cbAutoHoriz.setChecked(True)
        self.cbAutoHoriz.setProperty(u"prefEntry", u"AutoHorizontal")
        self.cbAutoHoriz.setProperty(u"prefPath", u"Mod/TechDraw/LeaderLine")

        self.gridLayout_2.addWidget(self.cbAutoHoriz, 10, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 4, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 8, 0, 1, 1)

        self.pcbBreakType = Gui_PrefComboBox(self.groupBox)
        self.pcbBreakType.addItem("")
        self.pcbBreakType.addItem("")
        self.pcbBreakType.addItem("")
        self.pcbBreakType.setObjectName(u"pcbBreakType")
        self.pcbBreakType.setProperty(u"prefEntry", u"BreakType")
        self.pcbBreakType.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout_2.addWidget(self.pcbBreakType, 11, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 7, 0, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.gridLayout_2.addWidget(self.label_19, 0, 0, 1, 1)

        self.pcbMatting = Gui_PrefComboBox(self.groupBox)
        self.pcbMatting.setObjectName(u"pcbMatting")
        sizePolicy1.setHeightForWidth(self.pcbMatting.sizePolicy().hasHeightForWidth())
        self.pcbMatting.setSizePolicy(sizePolicy1)
        self.pcbMatting.setProperty(u"prefEntry", u"MattingStyle")
        self.pcbMatting.setProperty(u"prefPath", u"/Mod/TechDraw/Decorations")

        self.gridLayout_2.addWidget(self.pcbMatting, 4, 2, 1, 1)

        self.cbComplexMarks = Gui_PrefCheckBox(self.groupBox)
        self.cbComplexMarks.setObjectName(u"cbComplexMarks")
        self.cbComplexMarks.setFont(font)
        self.cbComplexMarks.setChecked(True)
        self.cbComplexMarks.setProperty(u"prefEntry", u"SectionLineMarks")
        self.cbComplexMarks.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout_2.addWidget(self.cbComplexMarks, 3, 0, 1, 1)

        self.pdsbBalloonKink = Gui_PrefUnitSpinBox(self.groupBox)
        self.pdsbBalloonKink.setObjectName(u"pdsbBalloonKink")
        sizePolicy1.setHeightForWidth(self.pdsbBalloonKink.sizePolicy().hasHeightForWidth())
        self.pdsbBalloonKink.setSizePolicy(sizePolicy1)
        self.pdsbBalloonKink.setProperty(u"value", 5.000000000000000)
        self.pdsbBalloonKink.setProperty(u"prefEntry", u"BalloonKink")
        self.pdsbBalloonKink.setProperty(u"prefPath", u"Mod/TechDraw/Dimensions")

        self.gridLayout_2.addWidget(self.pdsbBalloonKink, 9, 2, 1, 1)

        self.cbISODates = Gui_PrefCheckBox(self.groupBox)
        self.cbISODates.setObjectName(u"cbISODates")
        self.cbISODates.setProperty(u"prefEntry", u"EnforceISODate")
        self.cbISODates.setProperty(u"prefPath", u"Mod/TechDraw/Standards")

        self.gridLayout_2.addWidget(self.cbISODates, 13, 0, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.gbLines = QGroupBox(TechDrawGui__DlgPrefsTechDrawAnnotationImp)
        self.gbLines.setObjectName(u"gbLines")
        sizePolicy1.setHeightForWidth(self.gbLines.sizePolicy().hasHeightForWidth())
        self.gbLines.setSizePolicy(sizePolicy1)
        self.gridLayout_5 = QGridLayout(self.gbLines)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pcbHiddenStyle = Gui_PrefComboBox(self.gbLines)
        self.pcbHiddenStyle.setObjectName(u"pcbHiddenStyle")
        sizePolicy1.setHeightForWidth(self.pcbHiddenStyle.sizePolicy().hasHeightForWidth())
        self.pcbHiddenStyle.setSizePolicy(sizePolicy1)
        self.pcbHiddenStyle.setMaxVisibleItems(6)
        self.pcbHiddenStyle.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.pcbHiddenStyle.setIconSize(QSize(32, 32))
        self.pcbHiddenStyle.setProperty(u"prefEntry", u"LineStyleHidden")
        self.pcbHiddenStyle.setProperty(u"prefPath", u"/Mod/TechDraw/Decorations")

        self.gridLayout_4.addWidget(self.pcbHiddenStyle, 2, 2, 1, 1)

        self.label_4 = QLabel(self.gbLines)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_4.addWidget(self.label_4, 5, 0, 1, 1)

        self.pcbLineStandard = Gui_PrefComboBox(self.gbLines)
        self.pcbLineStandard.setObjectName(u"pcbLineStandard")
        sizePolicy1.setHeightForWidth(self.pcbLineStandard.sizePolicy().hasHeightForWidth())
        self.pcbLineStandard.setSizePolicy(sizePolicy1)
        self.pcbLineStandard.setProperty(u"prefEntry", u"LineStandard")
        self.pcbLineStandard.setProperty(u"prefPath", u"Mod/TechDraw/Standards")

        self.gridLayout_4.addWidget(self.pcbLineStandard, 0, 2, 1, 1)

        self.pcbLineGroup = Gui_PrefComboBox(self.gbLines)
        self.pcbLineGroup.setObjectName(u"pcbLineGroup")
        sizePolicy1.setHeightForWidth(self.pcbLineGroup.sizePolicy().hasHeightForWidth())
        self.pcbLineGroup.setSizePolicy(sizePolicy1)
        self.pcbLineGroup.setProperty(u"prefEntry", u"LineGroup")
        self.pcbLineGroup.setProperty(u"prefPath", u"/Mod/TechDraw/Decorations")

        self.gridLayout_4.addWidget(self.pcbLineGroup, 1, 2, 1, 1)

        self.pcbHighlightStyle = Gui_PrefComboBox(self.gbLines)
        self.pcbHighlightStyle.setObjectName(u"pcbHighlightStyle")
        sizePolicy1.setHeightForWidth(self.pcbHighlightStyle.sizePolicy().hasHeightForWidth())
        self.pcbHighlightStyle.setSizePolicy(sizePolicy1)
        self.pcbHighlightStyle.setMaxVisibleItems(6)
        self.pcbHighlightStyle.setIconSize(QSize(32, 32))
        self.pcbHighlightStyle.setProperty(u"prefEntry", u"LineStyleHighlight")
        self.pcbHighlightStyle.setProperty(u"prefPath", u"/Mod/TechDraw/Decorations")

        self.gridLayout_4.addWidget(self.pcbHighlightStyle, 4, 2, 1, 1)

        self.label_20 = QLabel(self.gbLines)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.gridLayout_4.addWidget(self.label_20, 4, 0, 1, 1)

        self.label_6 = QLabel(self.gbLines)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)

        self.pcbSectionStyle = Gui_PrefComboBox(self.gbLines)
        self.pcbSectionStyle.setObjectName(u"pcbSectionStyle")
        sizePolicy1.setHeightForWidth(self.pcbSectionStyle.sizePolicy().hasHeightForWidth())
        self.pcbSectionStyle.setSizePolicy(sizePolicy1)
        self.pcbSectionStyle.setMaxVisibleItems(6)
        self.pcbSectionStyle.setIconSize(QSize(32, 32))
        self.pcbSectionStyle.setProperty(u"prefEntry", u"LineStyleSection")
        self.pcbSectionStyle.setProperty(u"prefPath", u"/Mod/TechDraw/Decorations")

        self.gridLayout_4.addWidget(self.pcbSectionStyle, 3, 2, 1, 1)

        self.label_2 = QLabel(self.gbLines)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.cbEndCap = Gui_PrefComboBox(self.gbLines)
        self.cbEndCap.addItem("")
        self.cbEndCap.addItem("")
        self.cbEndCap.addItem("")
        self.cbEndCap.setObjectName(u"cbEndCap")
        sizePolicy1.setHeightForWidth(self.cbEndCap.sizePolicy().hasHeightForWidth())
        self.cbEndCap.setSizePolicy(sizePolicy1)
        self.cbEndCap.setFont(font1)
        self.cbEndCap.setProperty(u"prefEntry", u"EdgeCapStyle")
        self.cbEndCap.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout_4.addWidget(self.cbEndCap, 7, 2, 1, 1)

        self.pcbCenterStyle = Gui_PrefComboBox(self.gbLines)
        self.pcbCenterStyle.setObjectName(u"pcbCenterStyle")
        sizePolicy1.setHeightForWidth(self.pcbCenterStyle.sizePolicy().hasHeightForWidth())
        self.pcbCenterStyle.setSizePolicy(sizePolicy1)
        self.pcbCenterStyle.setMaxVisibleItems(6)
        self.pcbCenterStyle.setIconSize(QSize(32, 32))
        self.pcbCenterStyle.setProperty(u"prefEntry", u"LineStyleCenter")
        self.pcbCenterStyle.setProperty(u"prefPath", u"/Mod/TechDraw/Decorations")

        self.gridLayout_4.addWidget(self.pcbCenterStyle, 5, 2, 1, 1)

        self.label_13 = QLabel(self.gbLines)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setFont(font)

        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_9 = QLabel(self.gbLines)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_4.addWidget(self.label_9, 7, 0, 1, 1)

        self.label_7 = QLabel(self.gbLines)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label_10 = QLabel(self.gbLines)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_4.addWidget(self.label_10, 6, 0, 1, 1)

        self.pcbBreakStyle = Gui_PrefComboBox(self.gbLines)
        self.pcbBreakStyle.setObjectName(u"pcbBreakStyle")
        self.pcbBreakStyle.setIconSize(QSize(32, 32))
        self.pcbBreakStyle.setProperty(u"prefEntry", u"LineStyleBreak")
        self.pcbBreakStyle.setProperty(u"prefPath", u"/Mod/TechDraw/Decorations")

        self.gridLayout_4.addWidget(self.pcbBreakStyle, 6, 2, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(2, 2)

        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.gbLines)

        self.label_8 = QLabel(TechDrawGui__DlgPrefsTechDrawAnnotationImp)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TechDrawGui__DlgPrefsTechDrawAnnotationImp)

        self.cbCutSurface.setCurrentIndex(2)
        self.pcbBreakType.setCurrentIndex(2)
        self.pcbLineStandard.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(TechDrawGui__DlgPrefsTechDrawAnnotationImp)
    # setupUi

    def retranslateUi(self, TechDrawGui__DlgPrefsTechDrawAnnotationImp):
        TechDrawGui__DlgPrefsTechDrawAnnotationImp.setWindowTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Annotation", None))
        self.groupBox.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Annotation", None))
#if QT_CONFIG(tooltip)
        self.cbPrintCenterMarks.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Show arc centers in printed output", None))
#endif // QT_CONFIG(tooltip)
        self.cbPrintCenterMarks.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Print center marks", None))
#if QT_CONFIG(tooltip)
        self.cbShowCenterMarks.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Show arc center marks in views", None))
#endif // QT_CONFIG(tooltip)
        self.cbShowCenterMarks.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Show center marks", None))
#if QT_CONFIG(tooltip)
        self.cb_ShowSectionLine.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Draws the section annotation on the source view. Otherwise, no section line, arrows or symbol will be shown in the source view.", None))
#endif // QT_CONFIG(tooltip)
        self.cb_ShowSectionLine.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Show section line in source view", None))
#if QT_CONFIG(tooltip)
        self.pcbBalloonShape.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Shape of balloon annotations", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cb_IncludeCutLine.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Draws a cut line on the source view. Otherwise, only the change marks, arrows and symbols will be displayed.", None))
#endif // QT_CONFIG(tooltip)
        self.cb_IncludeCutLine.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Include cut line in section annotation", None))
#if QT_CONFIG(tooltip)
        self.pcbBalloonArrow.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Style for balloon leader line ends", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Length of horizontal portion of balloon leader", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Balloon leader kink length", None))
        self.label_11.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Broken view break type", None))
#if QT_CONFIG(tooltip)
        self.cbPyramidOrtho.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Restrict filled triangle line end to vertical or horizontal directions", None))
#endif // QT_CONFIG(tooltip)
        self.cbPyramidOrtho.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Balloon orthogonal triangle", None))
        self.cbCutSurface.setItemText(0, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Hide", None))
        self.cbCutSurface.setItemText(1, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Solid color", None))
        self.cbCutSurface.setItemText(2, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"SVG hatch", None))
        self.cbCutSurface.setItemText(3, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"PAT hatch", None))

#if QT_CONFIG(tooltip)
        self.cbCutSurface.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Default appearance of cut surface in section view", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pcbDetailMatting.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Displays the outline around a detail view", None))
#endif // QT_CONFIG(tooltip)
        self.pcbDetailMatting.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Detail view show matting", None))
#if QT_CONFIG(tooltip)
        self.pcbDetailHighlight.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Highlights the detail area in the source view of the detail", None))
#endif // QT_CONFIG(tooltip)
        self.pcbDetailHighlight.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Detail source show highlight", None))
        self.label.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Detail view outline shape", None))
#if QT_CONFIG(tooltip)
        self.cbAutoHoriz.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Forces last leader line segment to be horizontal", None))
#endif // QT_CONFIG(tooltip)
        self.cbAutoHoriz.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Leader line auto horizontal", None))
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Balloon leader end", None))
        self.pcbBreakType.setItemText(0, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"No break lines", None))
        self.pcbBreakType.setItemText(1, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Zigzag lines", None))
        self.pcbBreakType.setItemText(2, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Simple lines", None))

        self.label_5.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Balloon shape", None))
        self.label_19.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Section cut surface", None))
#if QT_CONFIG(tooltip)
        self.pcbMatting.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Outline shape for detail views", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cbComplexMarks.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Shows markers at direction changes on complex section lines", None))
#endif // QT_CONFIG(tooltip)
        self.cbComplexMarks.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Complex section line marks", None))
#if QT_CONFIG(tooltip)
        self.pdsbBalloonKink.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Length of balloon leader line kink", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cbISODates.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Fills out template date fields using ccyy-mm-dd format automatically, even if that is not the standard format for the current locale.", None))
#endif // QT_CONFIG(tooltip)
        self.cbISODates.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Enforce ISO 8601 date format", None))
        self.gbLines.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Lines", None))
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Center line style", None))
#if QT_CONFIG(tooltip)
        self.pcbLineStandard.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Standard to be used to draw non-continuous lines.", None))
#endif // QT_CONFIG(tooltip)
        self.pcbLineGroup.setProperty(u"text", "")
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Line style of detail highlight on base view", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Detail highlight style", None))
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Section line style", None))
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Line standard", None))
        self.cbEndCap.setItemText(0, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Round", None))
        self.cbEndCap.setItemText(1, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Square", None))
        self.cbEndCap.setItemText(2, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Flat", None))

#if QT_CONFIG(tooltip)
        self.cbEndCap.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Shape of line end caps. The default (round) should almost\n"
"always be the right choice.  Flat or square caps are useful\n"
"for using drawings a 1:1 cutting guide.\n"
"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Line group used to set line widths", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Line width group", None))
        self.label_9.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Line end cap shape", None))
        self.label_7.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Hidden line style", None))
        self.label_10.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Break line style", None))
#if QT_CONFIG(tooltip)
        self.pcbBreakStyle.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"Style of line to be used in broken view.", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawAnnotationImp", u"<html><head/><body><p><span style=\" font-weight:600;\">Note:</span> Items in <span style=\" font-style:italic;\">italics</span> are default values for new objects. They have no effect on existing objects.</p></body></html>", None))
    # retranslateUi

