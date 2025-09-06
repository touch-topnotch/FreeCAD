# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPrefsTechDrawDimensions.ui'
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

class Ui_TechDrawGui_DlgPrefsTechDrawDimensionsImp(object):
    def setupUi(self, TechDrawGui__DlgPrefsTechDrawDimensionsImp):
        if not TechDrawGui__DlgPrefsTechDrawDimensionsImp.objectName():
            TechDrawGui__DlgPrefsTechDrawDimensionsImp.setObjectName(u"TechDrawGui__DlgPrefsTechDrawDimensionsImp")
        TechDrawGui__DlgPrefsTechDrawDimensionsImp.resize(495, 692)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__DlgPrefsTechDrawDimensionsImp.sizePolicy().hasHeightForWidth())
        TechDrawGui__DlgPrefsTechDrawDimensionsImp.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(TechDrawGui__DlgPrefsTechDrawDimensionsImp)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gbDim = QGroupBox(TechDrawGui__DlgPrefsTechDrawDimensionsImp)
        self.gbDim.setObjectName(u"gbDim")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gbDim.sizePolicy().hasHeightForWidth())
        self.gbDim.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.gbDim)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.plsb_ArrowSize = Gui_PrefUnitSpinBox(self.gbDim)
        self.plsb_ArrowSize.setObjectName(u"plsb_ArrowSize")
        sizePolicy1.setHeightForWidth(self.plsb_ArrowSize.sizePolicy().hasHeightForWidth())
        self.plsb_ArrowSize.setSizePolicy(sizePolicy1)
        self.plsb_ArrowSize.setProperty(u"value", 5.000000000000000)
        self.plsb_ArrowSize.setProperty(u"prefEntry", u"ArrowSize")
        self.plsb_ArrowSize.setProperty(u"prefPath", u"Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.plsb_ArrowSize, 8, 2, 1, 1)

        self.label = QLabel(self.gbDim)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setItalic(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.pcbArrow = Gui_PrefComboBox(self.gbDim)
        self.pcbArrow.setObjectName(u"pcbArrow")
        sizePolicy1.setHeightForWidth(self.pcbArrow.sizePolicy().hasHeightForWidth())
        self.pcbArrow.setSizePolicy(sizePolicy1)
        self.pcbArrow.setProperty(u"prefEntry", u"ArrowStyle")
        self.pcbArrow.setProperty(u"prefPath", u"Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.pcbArrow, 7, 2, 1, 1)

        self.label_8 = QLabel(self.gbDim)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.pcbStandardAndStyle = Gui_PrefComboBox(self.gbDim)
        self.pcbStandardAndStyle.addItem("")
        self.pcbStandardAndStyle.addItem("")
        self.pcbStandardAndStyle.addItem("")
        self.pcbStandardAndStyle.addItem("")
        self.pcbStandardAndStyle.setObjectName(u"pcbStandardAndStyle")
        sizePolicy1.setHeightForWidth(self.pcbStandardAndStyle.sizePolicy().hasHeightForWidth())
        self.pcbStandardAndStyle.setSizePolicy(sizePolicy1)
        self.pcbStandardAndStyle.setProperty(u"prefEntry", u"StandardAndStyle")
        self.pcbStandardAndStyle.setProperty(u"prefPath", u"/Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.pcbStandardAndStyle, 0, 2, 1, 1)

        self.label_2 = QLabel(self.gbDim)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.cbShowUnits = Gui_PrefCheckBox(self.gbDim)
        self.cbShowUnits.setObjectName(u"cbShowUnits")
        sizePolicy1.setHeightForWidth(self.cbShowUnits.sizePolicy().hasHeightForWidth())
        self.cbShowUnits.setSizePolicy(sizePolicy1)
        self.cbShowUnits.setFont(font)
        self.cbShowUnits.setProperty(u"prefEntry", u"ShowUnits")
        self.cbShowUnits.setProperty(u"prefPath", u"/Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.cbShowUnits, 1, 2, 1, 1)

        self.label_16 = QLabel(self.gbDim)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout.addWidget(self.label_16, 0, 0, 1, 1)

        self.plsb_FontSize = Gui_PrefUnitSpinBox(self.gbDim)
        self.plsb_FontSize.setObjectName(u"plsb_FontSize")
        sizePolicy1.setHeightForWidth(self.plsb_FontSize.sizePolicy().hasHeightForWidth())
        self.plsb_FontSize.setSizePolicy(sizePolicy1)
        self.plsb_FontSize.setProperty(u"value", 4.000000000000000)
        self.plsb_FontSize.setProperty(u"prefEntry", u"FontSize")
        self.plsb_FontSize.setProperty(u"prefPath", u"/Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.plsb_FontSize, 4, 2, 1, 1)

        self.label_12 = QLabel(self.gbDim)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)

        self.label_9 = QLabel(self.gbDim)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.pdsbToleranceScale = Gui_PrefDoubleSpinBox(self.gbDim)
        self.pdsbToleranceScale.setObjectName(u"pdsbToleranceScale")
        sizePolicy1.setHeightForWidth(self.pdsbToleranceScale.sizePolicy().hasHeightForWidth())
        self.pdsbToleranceScale.setSizePolicy(sizePolicy1)
        self.pdsbToleranceScale.setMinimumSize(QSize(174, 0))
        self.pdsbToleranceScale.setBaseSize(QSize(0, 0))
        self.pdsbToleranceScale.setSingleStep(0.100000000000000)
        self.pdsbToleranceScale.setValue(0.800000000000000)
        self.pdsbToleranceScale.setProperty(u"prefEntry", u"TolSizeAdjust")
        self.pdsbToleranceScale.setProperty(u"prefPath", u"Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.pdsbToleranceScale, 5, 2, 1, 1)

        self.lbl_LabelFont = QLabel(self.gbDim)
        self.lbl_LabelFont.setObjectName(u"lbl_LabelFont")
        self.lbl_LabelFont.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setItalic(False)
        self.lbl_LabelFont.setFont(font1)

        self.gridLayout.addWidget(self.lbl_LabelFont, 5, 0, 1, 1)

        self.sbAltDecimals = Gui_PrefSpinBox(self.gbDim)
        self.sbAltDecimals.setObjectName(u"sbAltDecimals")
        self.sbAltDecimals.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.sbAltDecimals.sizePolicy().hasHeightForWidth())
        self.sbAltDecimals.setSizePolicy(sizePolicy1)
        self.sbAltDecimals.setValue(2)
        self.sbAltDecimals.setProperty(u"prefEntry", u"AltDecimals")
        self.sbAltDecimals.setProperty(u"prefPath", u"/Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.sbAltDecimals, 2, 2, 1, 1)

        self.leDiameter = Gui_PrefLineEdit(self.gbDim)
        self.leDiameter.setObjectName(u"leDiameter")
        sizePolicy1.setHeightForWidth(self.leDiameter.sizePolicy().hasHeightForWidth())
        self.leDiameter.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(12)
        self.leDiameter.setFont(font2)
        self.leDiameter.setText(u"\u2300")
        self.leDiameter.setProperty(u"prefEntry", u"DiameterSymbol")
        self.leDiameter.setProperty(u"prefPath", u"/Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.leDiameter, 6, 2, 1, 1)

        self.cbGlobalDecimals = Gui_PrefCheckBox(self.gbDim)
        self.cbGlobalDecimals.setObjectName(u"cbGlobalDecimals")
        sizePolicy1.setHeightForWidth(self.cbGlobalDecimals.sizePolicy().hasHeightForWidth())
        self.cbGlobalDecimals.setSizePolicy(sizePolicy1)
        self.cbGlobalDecimals.setFont(font)
        self.cbGlobalDecimals.setChecked(True)
        self.cbGlobalDecimals.setProperty(u"prefEntry", u"UseGlobalDecimals")
        self.cbGlobalDecimals.setProperty(u"prefPath", u"/Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.cbGlobalDecimals, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 1, 1, 1)

        self.label_11 = QLabel(self.gbDim)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_3 = QLabel(self.gbDim)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 9, 0, 1, 1)

        self.leFormatSpec = Gui_PrefLineEdit(self.gbDim)
        self.leFormatSpec.setObjectName(u"leFormatSpec")
        self.leFormatSpec.setProperty(u"prefEntry", u"formatSpec")
        self.leFormatSpec.setProperty(u"prefPath", u"/Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.leFormatSpec, 3, 2, 1, 1)

        self.label_4 = QLabel(self.gbDim)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)

        self.pdsbGapISO = Gui_PrefDoubleSpinBox(self.gbDim)
        self.pdsbGapISO.setObjectName(u"pdsbGapISO")
        self.pdsbGapISO.setValue(0.000000000000000)
        self.pdsbGapISO.setProperty(u"prefEntry", u"GapISO")
        self.pdsbGapISO.setProperty(u"prefPath", u"Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.pdsbGapISO, 9, 2, 1, 1)

        self.pdsbGapASME = Gui_PrefDoubleSpinBox(self.gbDim)
        self.pdsbGapASME.setObjectName(u"pdsbGapASME")
        self.pdsbGapASME.setValue(0.000000000000000)
        self.pdsbGapASME.setProperty(u"prefEntry", u"GapASME")
        self.pdsbGapASME.setProperty(u"prefPath", u"Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.pdsbGapASME, 10, 2, 1, 1)

        self.label_18 = QLabel(self.gbDim)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.gridLayout.addWidget(self.label_18, 11, 0, 1, 1)

        self.pdsbLineSpacingFactorISO = Gui_PrefDoubleSpinBox(self.gbDim)
        self.pdsbLineSpacingFactorISO.setObjectName(u"pdsbLineSpacingFactorISO")
        self.pdsbLineSpacingFactorISO.setValue(2.000000000000000)
        self.pdsbLineSpacingFactorISO.setProperty(u"prefEntry", u"LineSpacingFactorISO")
        self.pdsbLineSpacingFactorISO.setProperty(u"prefPath", u"Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.pdsbLineSpacingFactorISO, 11, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.gbDim)

        self.label_17 = QLabel(TechDrawGui__DlgPrefsTechDrawDimensionsImp)
        self.label_17.setObjectName(u"label_17")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setItalic(False)
        self.label_17.setFont(font3)
        self.label_17.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_17)

        self.groupBox_6 = QGroupBox(TechDrawGui__DlgPrefsTechDrawDimensionsImp)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy2)
        self.gridLayout_general = QGridLayout(self.groupBox_6)
        self.gridLayout_general.setObjectName(u"gridLayout_general")
        self.dimensioningLabel = QLabel(self.groupBox_6)
        self.dimensioningLabel.setObjectName(u"dimensioningLabel")

        self.gridLayout_general.addWidget(self.dimensioningLabel, 0, 0, 1, 1)

        self.dimensioningMode = QComboBox(self.groupBox_6)
        self.dimensioningMode.setObjectName(u"dimensioningMode")

        self.gridLayout_general.addWidget(self.dimensioningMode, 0, 1, 1, 1)

        self.radiusDiameterLabel = QLabel(self.groupBox_6)
        self.radiusDiameterLabel.setObjectName(u"radiusDiameterLabel")

        self.gridLayout_general.addWidget(self.radiusDiameterLabel, 1, 0, 1, 1)

        self.radiusDiameterMode = QComboBox(self.groupBox_6)
        self.radiusDiameterMode.setObjectName(u"radiusDiameterMode")

        self.gridLayout_general.addWidget(self.radiusDiameterMode, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_6)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(TechDrawGui__DlgPrefsTechDrawDimensionsImp)
        self.cbGlobalDecimals.toggled.connect(self.sbAltDecimals.setDisabled)

        self.pcbArrow.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(TechDrawGui__DlgPrefsTechDrawDimensionsImp)
    # setupUi

    def retranslateUi(self, TechDrawGui__DlgPrefsTechDrawDimensionsImp):
        TechDrawGui__DlgPrefsTechDrawDimensionsImp.setWindowTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Dimensions", None))
        self.gbDim.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Dimensions", None))
#if QT_CONFIG(tooltip)
        self.plsb_ArrowSize.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Arrowhead size", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Dimension format", None))
#if QT_CONFIG(tooltip)
        self.pcbArrow.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Arrowhead style", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Diameter symbol", None))
        self.pcbStandardAndStyle.setItemText(0, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"ISO oriented", None))
        self.pcbStandardAndStyle.setItemText(1, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"ISO referencing", None))
        self.pcbStandardAndStyle.setItemText(2, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"ASME inlined", None))
        self.pcbStandardAndStyle.setItemText(3, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"ASME referencing", None))

#if QT_CONFIG(tooltip)
        self.pcbStandardAndStyle.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Standard to be used for dimensional values", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Font size", None))
#if QT_CONFIG(tooltip)
        self.cbShowUnits.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Append unit to dimension values", None))
#endif // QT_CONFIG(tooltip)
        self.cbShowUnits.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Show units", None))
        self.label_16.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Standard and style", None))
#if QT_CONFIG(tooltip)
        self.plsb_FontSize.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Dimension text font size", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Arrow size", None))
        self.label_9.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Arrow style", None))
#if QT_CONFIG(tooltip)
        self.pdsbToleranceScale.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Tolerance text scale\n"
"Multiplier of 'Font size'", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.pdsbToleranceScale.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.lbl_LabelFont.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Tolerance text scale", None))
#if QT_CONFIG(tooltip)
        self.sbAltDecimals.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Number of decimals if 'Use global decimals' is not used", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.leDiameter.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Character used to indicate diameter dimensions", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cbGlobalDecimals.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Use system setting for number of decimals", None))
#endif // QT_CONFIG(tooltip)
        self.cbGlobalDecimals.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Use global decimals", None))
        self.label_11.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Alternate decimals", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Controls the gap size between the dimension point and the start of the extension line for ISO dimensions", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Extension gap factor - ISO", None))
#if QT_CONFIG(tooltip)
        self.leFormatSpec.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Leave blank for automatic dimension format. Use %f, %g or %w specifiers to override.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Controls the gap size between the dimension point and the start of the extension line for ASME dimensions", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Extension gap factor - ASME", None))
#if QT_CONFIG(tooltip)
        self.pdsbGapISO.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Controls the gap size between the dimension point and the start of the extension line for ISO dimensions.\n"
" Value multiplied by the line width is the gap.\n"
" Normally, no gap is used. If using a gap, the recommended value is 8.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pdsbGapASME.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Controls the gap size between the dimension point and the start of the extension line for ASME dimensions. Value multiplied by the line width is the gap.\n"
" Normally, no gap is used. If using a gap, the recommended value is 6.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Controls the gap size between dimension line and dimension text for ISO dimensions.", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Line spacing - ISO", None))
#if QT_CONFIG(tooltip)
        self.pdsbLineSpacingFactorISO.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Controls the gap size between dimension line and dimension text.\n"
" Value multiplied by the line width is the line spacing.", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"<html><head/><body><p><span style=\" font-weight:600;\">Note:</span> Items in <span style=\" font-style:italic;\">italics</span> are default values for new objects. They have no effect on existing objects.</p></body></html>", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Tools", None))
        self.dimensioningLabel.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Dimensioning tools", None))
#if QT_CONFIG(tooltip)
        self.dimensioningMode.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Choose the type of dimensioning tools shown in the toolbar:\n"
"\u2018Single tool\u2019 provides one unified tool for all dimension types (Distance, X/Y, Angle, Radius) with others in a drop-down.\n"
"\u2018Separated tools\u2019 displays individual tools for each dimension type.\n"
"\u2018Both\u2019 enables both the unified tool and the individual tools.\n"
"This affects only the toolbar; all tools remain available via the menu and shortcuts.", None))
#endif // QT_CONFIG(tooltip)
        self.radiusDiameterLabel.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"Dimension tool diameter/radius mode", None))
#if QT_CONFIG(tooltip)
        self.radiusDiameterMode.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawDimensionsImp", u"While using the dimension tool you may choose how to handle circles and arcs:\n"
"'Auto': The tool will apply radius to arcs and diameter to circles.\n"
"'Diameter': The tool will apply diameter to all.\n"
"'Radius': The tool will apply radius to all.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

