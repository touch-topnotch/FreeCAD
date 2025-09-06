# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPrefsTechDrawColors.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_TechDrawGui_DlgPrefsTechDrawColorsImp(object):
    def setupUi(self, TechDrawGui__DlgPrefsTechDrawColorsImp):
        if not TechDrawGui__DlgPrefsTechDrawColorsImp.objectName():
            TechDrawGui__DlgPrefsTechDrawColorsImp.setObjectName(u"TechDrawGui__DlgPrefsTechDrawColorsImp")
        TechDrawGui__DlgPrefsTechDrawColorsImp.resize(440, 448)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__DlgPrefsTechDrawColorsImp.sizePolicy().hasHeightForWidth())
        TechDrawGui__DlgPrefsTechDrawColorsImp.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(TechDrawGui__DlgPrefsTechDrawColorsImp)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gb_Colors = QGroupBox(TechDrawGui__DlgPrefsTechDrawColorsImp)
        self.gb_Colors.setObjectName(u"gb_Colors")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gb_Colors.sizePolicy().hasHeightForWidth())
        self.gb_Colors.setSizePolicy(sizePolicy1)
        self.gb_Colors.setMinimumSize(QSize(0, 225))
        self.gb_Colors.setBaseSize(QSize(0, 200))
        self.verticalLayout = QVBoxLayout(self.gb_Colors)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.gb_Colors)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setItalic(True)
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 4, 3, 1, 1)

        self.pcbHighlight = Gui_PrefColorButton(self.gb_Colors)
        self.pcbHighlight.setObjectName(u"pcbHighlight")
        self.pcbHighlight.setColor(QColor(0, 0, 0))
        self.pcbHighlight.setProperty(u"prefEntry", u"HighlightColor")
        self.pcbHighlight.setProperty(u"prefPath", u"/Mod/TechDraw/Decorations")

        self.gridLayout.addWidget(self.pcbHighlight, 6, 1, 1, 1)

        self.pcbMonochrome = Gui_PrefCheckBox(self.gb_Colors)
        self.pcbMonochrome.setObjectName(u"pcbMonochrome")
        self.pcbMonochrome.setProperty(u"prefEntry", u"Monochrome")
        self.pcbMonochrome.setProperty(u"prefPath", u"/Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcbMonochrome, 11, 0, 1, 1)

        self.lbl_Select = QLabel(self.gb_Colors)
        self.lbl_Select.setObjectName(u"lbl_Select")
        self.lbl_Select.setFont(font)

        self.gridLayout.addWidget(self.lbl_Select, 2, 0, 1, 1)

        self.pcb_Background = Gui_PrefColorButton(self.gb_Colors)
        self.pcb_Background.setObjectName(u"pcb_Background")
        self.pcb_Background.setColor(QColor(211, 211, 211))
        self.pcb_Background.setProperty(u"prefEntry", u"Background")
        self.pcb_Background.setProperty(u"prefPath", u"/Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcb_Background, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.pcbCenterColor = Gui_PrefColorButton(self.gb_Colors)
        self.pcbCenterColor.setObjectName(u"pcbCenterColor")
        self.pcbCenterColor.setColor(QColor(0, 0, 0))
        self.pcbCenterColor.setProperty(u"prefEntry", u"CenterColor")
        self.pcbCenterColor.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout.addWidget(self.pcbCenterColor, 5, 1, 1, 1)

        self.label_3 = QLabel(self.gb_Colors)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)

        self.label_15 = QLabel(self.gb_Colors)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 1)

        self.pcb_PreSelect = Gui_PrefColorButton(self.gb_Colors)
        self.pcb_PreSelect.setObjectName(u"pcb_PreSelect")
        self.pcb_PreSelect.setColor(QColor(255, 255, 0))
        self.pcb_PreSelect.setProperty(u"prefEntry", u"PreSelectColor")
        self.pcb_PreSelect.setProperty(u"prefPath", u"Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcb_PreSelect, 1, 1, 1, 1)

        self.label_16 = QLabel(self.gb_Colors)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 5, 3, 1, 1)

        self.label_4 = QLabel(self.gb_Colors)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.pcb_Face = Gui_PrefColorButton(self.gb_Colors)
        self.pcb_Face.setObjectName(u"pcb_Face")
        self.pcb_Face.setColor(QColor(255, 255, 255))
        self.pcb_Face.setProperty(u"prefEntry", u"FaceColor")
        self.pcb_Face.setProperty(u"prefPath", u"/Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcb_Face, 7, 4, 1, 1)

        self.lbl_PreSelect = QLabel(self.gb_Colors)
        self.lbl_PreSelect.setObjectName(u"lbl_PreSelect")
        self.lbl_PreSelect.setFont(font)

        self.gridLayout.addWidget(self.lbl_PreSelect, 1, 0, 1, 1)

        self.label_17 = QLabel(self.gb_Colors)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout.addWidget(self.label_17, 6, 3, 1, 1)

        self.pcbLightTextColor = Gui_PrefColorButton(self.gb_Colors)
        self.pcbLightTextColor.setObjectName(u"pcbLightTextColor")
        self.pcbLightTextColor.setProperty(u"prefEntry", u"LightTextColor")
        self.pcbLightTextColor.setProperty(u"prefPath", u"Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcbLightTextColor, 11, 1, 1, 1)

        self.pcbDimColor = Gui_PrefColorButton(self.gb_Colors)
        self.pcbDimColor.setObjectName(u"pcbDimColor")
        self.pcbDimColor.setColor(QColor(0, 0, 0))
        self.pcbDimColor.setProperty(u"prefEntry", u"Color")
        self.pcbDimColor.setProperty(u"prefPath", u"Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.pcbDimColor, 4, 1, 1, 1)

        self.pcbPageColor = Gui_PrefColorButton(self.gb_Colors)
        self.pcbPageColor.setObjectName(u"pcbPageColor")
        self.pcbPageColor.setColor(QColor(255, 255, 255))
        self.pcbPageColor.setProperty(u"prefEntry", u"PageColor")
        self.pcbPageColor.setProperty(u"prefPath", u"Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcbPageColor, 11, 4, 1, 1)

        self.label_6 = QLabel(self.gb_Colors)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)

        self.pcb_Hatch = Gui_PrefColorButton(self.gb_Colors)
        self.pcb_Hatch.setObjectName(u"pcb_Hatch")
        self.pcb_Hatch.setColor(QColor(0, 0, 0))
        self.pcb_Hatch.setProperty(u"prefEntry", u"Hatch")
        self.pcb_Hatch.setProperty(u"prefPath", u"/Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcb_Hatch, 3, 4, 1, 1)

        self.pcbSectionLine = Gui_PrefColorButton(self.gb_Colors)
        self.pcbSectionLine.setObjectName(u"pcbSectionLine")
        self.pcbSectionLine.setColor(QColor(0, 0, 0))
        self.pcbSectionLine.setProperty(u"prefEntry", u"SectionColor")
        self.pcbSectionLine.setProperty(u"prefPath", u"/Mod/TechDraw/Decorations")

        self.gridLayout.addWidget(self.pcbSectionLine, 2, 4, 1, 1)

        self.pcb_GeomHatch = Gui_PrefColorButton(self.gb_Colors)
        self.pcb_GeomHatch.setObjectName(u"pcb_GeomHatch")
        self.pcb_GeomHatch.setColor(QColor(0, 0, 0))
        self.pcb_GeomHatch.setProperty(u"prefEntry", u"GeomHatch")
        self.pcb_GeomHatch.setProperty(u"prefPath", u"/Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcb_GeomHatch, 4, 4, 1, 1)

        self.label_18 = QLabel(self.gb_Colors)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.gridLayout.addWidget(self.label_18, 6, 0, 1, 1)

        self.label_5 = QLabel(self.gb_Colors)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 3, 3, 1, 1)

        self.label_2 = QLabel(self.gb_Colors)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 11, 3, 1, 1)

        self.label_14 = QLabel(self.gb_Colors)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 2, 3, 1, 1)

        self.pcbLightOnDark = Gui_PrefCheckBox(self.gb_Colors)
        self.pcbLightOnDark.setObjectName(u"pcbLightOnDark")
        self.pcbLightOnDark.setProperty(u"prefEntry", u"LightOnDark")
        self.pcbLightOnDark.setProperty(u"prefPath", u"/Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcbLightOnDark, 10, 0, 1, 1)

        self.pcb_Select = Gui_PrefColorButton(self.gb_Colors)
        self.pcb_Select.setObjectName(u"pcb_Select")
        self.pcb_Select.setColor(QColor(0, 255, 0))
        self.pcb_Select.setProperty(u"prefEntry", u"SelectColor")
        self.pcb_Select.setProperty(u"prefPath", u"Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcb_Select, 2, 1, 1, 1)

        self.pcbMarkup = Gui_PrefColorButton(self.gb_Colors)
        self.pcbMarkup.setObjectName(u"pcbMarkup")
        self.pcbMarkup.setColor(QColor(0, 0, 0))
        self.pcbMarkup.setProperty(u"prefEntry", u"Color")
        self.pcbMarkup.setProperty(u"prefPath", u"Mod/TechDraw/Markups")

        self.gridLayout.addWidget(self.pcbMarkup, 6, 4, 1, 1)

        self.pcb_PaintFaces = Gui_PrefCheckBox(self.gb_Colors)
        self.pcb_PaintFaces.setObjectName(u"pcb_PaintFaces")
        self.pcb_PaintFaces.setMinimumSize(QSize(0, 20))
        self.pcb_PaintFaces.setFont(font)
        self.pcb_PaintFaces.setProperty(u"prefEntry", u"ClearFace")
        self.pcb_PaintFaces.setProperty(u"prefPath", u"/Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcb_PaintFaces, 7, 3, 1, 1)

        self.pcb_Normal = Gui_PrefColorButton(self.gb_Colors)
        self.pcb_Normal.setObjectName(u"pcb_Normal")
        self.pcb_Normal.setColor(QColor(0, 0, 0))
        self.pcb_Normal.setProperty(u"prefEntry", u"NormalColor")
        self.pcb_Normal.setProperty(u"prefPath", u"Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcb_Normal, 0, 1, 1, 1)

        self.pcb_Hidden = Gui_PrefColorButton(self.gb_Colors)
        self.pcb_Hidden.setObjectName(u"pcb_Hidden")
        self.pcb_Hidden.setColor(QColor(0, 0, 0))
        self.pcb_Hidden.setProperty(u"prefEntry", u"HiddenColor")
        self.pcb_Hidden.setProperty(u"prefPath", u"Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcb_Hidden, 0, 4, 1, 1)

        self.pcb_Grid = Gui_PrefColorButton(self.gb_Colors)
        self.pcb_Grid.setObjectName(u"pcb_Grid")
        self.pcb_Grid.setColor(QColor(0, 0, 0))
        self.pcb_Grid.setProperty(u"prefEntry", u"gridColor")
        self.pcb_Grid.setProperty(u"prefPath", u"/Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcb_Grid, 7, 1, 1, 1)

        self.label_13 = QLabel(self.gb_Colors)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)

        self.pcbVertexColor = Gui_PrefColorButton(self.gb_Colors)
        self.pcbVertexColor.setObjectName(u"pcbVertexColor")
        self.pcbVertexColor.setColor(QColor(0, 0, 0))
        self.pcbVertexColor.setProperty(u"prefEntry", u"VertexColor")
        self.pcbVertexColor.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout.addWidget(self.pcbVertexColor, 5, 4, 1, 1)

        self.label = QLabel(self.gb_Colors)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)

        self.lbl_Hidden = QLabel(self.gb_Colors)
        self.lbl_Hidden.setObjectName(u"lbl_Hidden")
        self.lbl_Hidden.setFont(font)

        self.gridLayout.addWidget(self.lbl_Hidden, 0, 3, 1, 1)

        self.lbl_Normal = QLabel(self.gb_Colors)
        self.lbl_Normal.setObjectName(u"lbl_Normal")
        self.lbl_Normal.setFont(font)

        self.gridLayout.addWidget(self.lbl_Normal, 0, 0, 1, 1)

        self.pcb_Surface = Gui_PrefColorButton(self.gb_Colors)
        self.pcb_Surface.setObjectName(u"pcb_Surface")
        self.pcb_Surface.setColor(QColor(211, 211, 211))
        self.pcb_Surface.setProperty(u"prefEntry", u"CutSurfaceColor")
        self.pcb_Surface.setProperty(u"prefPath", u"Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcb_Surface, 1, 4, 1, 1)

        self.label_8 = QLabel(self.gb_Colors)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)

        self.pcbUnderline = Gui_PrefColorButton(self.gb_Colors)
        self.pcbUnderline.setObjectName(u"pcbUnderline")
        self.pcbUnderline.setColor(QColor(0, 0, 255))
        self.pcbUnderline.setProperty(u"prefEntry", u"TemplateUnderlineColor")
        self.pcbUnderline.setProperty(u"prefPath", u"/Mod/TechDraw/Colors")

        self.gridLayout.addWidget(self.pcbUnderline, 8, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.gb_Colors)

        self.label_12 = QLabel(TechDrawGui__DlgPrefsTechDrawColorsImp)
        self.label_12.setObjectName(u"label_12")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setItalic(False)
        self.label_12.setFont(font1)
        self.label_12.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_12)

        self.verticalSpacer = QSpacerItem(20, 19, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(TechDrawGui__DlgPrefsTechDrawColorsImp)

        QMetaObject.connectSlotsByName(TechDrawGui__DlgPrefsTechDrawColorsImp)
    # setupUi

    def retranslateUi(self, TechDrawGui__DlgPrefsTechDrawColorsImp):
        TechDrawGui__DlgPrefsTechDrawColorsImp.setWindowTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Colors", None))
#if QT_CONFIG(tooltip)
        TechDrawGui__DlgPrefsTechDrawColorsImp.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.gb_Colors.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Colors", None))
        self.label_7.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Geometric hatch", None))
#if QT_CONFIG(tooltip)
        self.pcbMonochrome.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Use a single colour for all text and lines", None))
#endif // QT_CONFIG(tooltip)
        self.pcbMonochrome.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Monochrome", None))
        self.lbl_Select.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Selected", None))
#if QT_CONFIG(tooltip)
        self.pcb_Background.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Background color around pages", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pcbCenterColor.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Centerline color", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Section face", None))
        self.label_15.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Centerline", None))
#if QT_CONFIG(tooltip)
        self.pcb_PreSelect.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Preselection color", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Vertex", None))
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Background", None))
#if QT_CONFIG(tooltip)
        self.pcb_Face.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Face color (if not transparent)", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_PreSelect.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Preselected", None))
        self.label_17.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Leader line", None))
#if QT_CONFIG(tooltip)
        self.pcbLightTextColor.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Monochrome text color", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pcbDimColor.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Color of dimension lines and text", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pcbPageColor.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Use a light color for dark text and dark color for light text", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText("")
#if QT_CONFIG(tooltip)
        self.pcb_Hatch.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Hatch image color", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pcbSectionLine.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Section line color", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pcb_GeomHatch.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Geometric hatch pattern color", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Detail highlight", None))
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Hatch", None))
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Page color", None))
        self.label_14.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Section line", None))
#if QT_CONFIG(tooltip)
        self.pcbLightOnDark.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Uses light text and lines on dark backgrounds and sets page color to a dark color. Transparent or light color faces are recommended with this option.", None))
#endif // QT_CONFIG(tooltip)
        self.pcbLightOnDark.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Light on dark", None))
#if QT_CONFIG(tooltip)
        self.pcb_Select.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Selected item color", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pcbMarkup.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Default color for leader lines", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pcb_PaintFaces.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Object faces will be transparent", None))
#endif // QT_CONFIG(tooltip)
        self.pcb_PaintFaces.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Transparent faces", None))
#if QT_CONFIG(tooltip)
        self.pcb_Normal.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Normal line color", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pcb_Hidden.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Hidden line color", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Dimension", None))
#if QT_CONFIG(tooltip)
        self.pcbVertexColor.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Color of vertices in views", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Grid color", None))
        self.lbl_Hidden.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Hidden line", None))
        self.lbl_Normal.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Normal", None))
#if QT_CONFIG(tooltip)
        self.pcb_Surface.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Section face color", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"Template underline", None))
        self.label_12.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawColorsImp", u"<html><head/><body><p><span style=\" font-weight:600;\">Note:</span> Items in <span style=\" font-style:italic;\">italics</span> are default values for new objects. They have no effect on existing objects.</p></body></html>", None))
    # retranslateUi

