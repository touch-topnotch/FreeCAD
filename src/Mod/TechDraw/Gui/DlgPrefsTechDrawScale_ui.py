# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPrefsTechDrawScale.ui'
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

class Ui_TechDrawGui_DlgPrefsTechDrawScaleImp(object):
    def setupUi(self, TechDrawGui__DlgPrefsTechDrawScaleImp):
        if not TechDrawGui__DlgPrefsTechDrawScaleImp.objectName():
            TechDrawGui__DlgPrefsTechDrawScaleImp.setObjectName(u"TechDrawGui__DlgPrefsTechDrawScaleImp")
        TechDrawGui__DlgPrefsTechDrawScaleImp.resize(457, 481)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__DlgPrefsTechDrawScaleImp.sizePolicy().hasHeightForWidth())
        TechDrawGui__DlgPrefsTechDrawScaleImp.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(TechDrawGui__DlgPrefsTechDrawScaleImp)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gbScale = QGroupBox(TechDrawGui__DlgPrefsTechDrawScaleImp)
        self.gbScale.setObjectName(u"gbScale")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gbScale.sizePolicy().hasHeightForWidth())
        self.gbScale.setSizePolicy(sizePolicy1)
        self.gbScale.setMinimumSize(QSize(0, 113))
        self.gbScale.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.gbScale)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.label_13 = QLabel(self.gbScale)
        self.label_13.setObjectName(u"label_13")
        font = QFont()
        font.setItalic(True)
        self.label_13.setFont(font)

        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_15 = QLabel(self.gbScale)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)

        self.cbViewScaleType = Gui_PrefComboBox(self.gbScale)
        self.cbViewScaleType.addItem("")
        self.cbViewScaleType.addItem("")
        self.cbViewScaleType.addItem("")
        self.cbViewScaleType.setObjectName(u"cbViewScaleType")
        self.cbViewScaleType.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.cbViewScaleType.sizePolicy().hasHeightForWidth())
        self.cbViewScaleType.setSizePolicy(sizePolicy1)
        self.cbViewScaleType.setMinimumSize(QSize(174, 0))
        self.cbViewScaleType.setProperty(u"prefEntry", u"DefaultScaleType")
        self.cbViewScaleType.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout.addWidget(self.cbViewScaleType, 1, 2, 1, 1)

        self.pdsbPageScale = Gui_PrefDoubleSpinBox(self.gbScale)
        self.pdsbPageScale.setObjectName(u"pdsbPageScale")
        sizePolicy1.setHeightForWidth(self.pdsbPageScale.sizePolicy().hasHeightForWidth())
        self.pdsbPageScale.setSizePolicy(sizePolicy1)
        self.pdsbPageScale.setMinimumSize(QSize(174, 0))
        self.pdsbPageScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pdsbPageScale.setDecimals(2)
        self.pdsbPageScale.setValue(1.000000000000000)
        self.pdsbPageScale.setProperty(u"prefEntry", u"DefaultScale")
        self.pdsbPageScale.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout.addWidget(self.pdsbPageScale, 0, 2, 1, 1)

        self.pdsbViewScale = Gui_PrefDoubleSpinBox(self.gbScale)
        self.pdsbViewScale.setObjectName(u"pdsbViewScale")
        self.pdsbViewScale.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pdsbViewScale.sizePolicy().hasHeightForWidth())
        self.pdsbViewScale.setSizePolicy(sizePolicy1)
        self.pdsbViewScale.setMinimumSize(QSize(174, 0))
        self.pdsbViewScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pdsbViewScale.setDecimals(2)
        self.pdsbViewScale.setValue(1.000000000000000)
        self.pdsbViewScale.setProperty(u"prefEntry", u"DefaultViewScale")
        self.pdsbViewScale.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout.addWidget(self.pdsbViewScale, 2, 2, 1, 1)

        self.label_14 = QLabel(self.gbScale)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)

        self.cbLegacyScale = Gui_PrefCheckBox(self.gbScale)
        self.cbLegacyScale.setObjectName(u"cbLegacyScale")
        self.cbLegacyScale.setFont(font)
        self.cbLegacyScale.setProperty(u"prefEntry", u"LegacySvgScaling")
        self.cbLegacyScale.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout.addWidget(self.cbLegacyScale, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.gbScale)

        self.gb_SizeAdj = QGroupBox(TechDrawGui__DlgPrefsTechDrawScaleImp)
        self.gb_SizeAdj.setObjectName(u"gb_SizeAdj")
        sizePolicy1.setHeightForWidth(self.gb_SizeAdj.sizePolicy().hasHeightForWidth())
        self.gb_SizeAdj.setSizePolicy(sizePolicy1)
        self.gb_SizeAdj.setMinimumSize(QSize(0, 141))
        self.verticalLayout_3 = QVBoxLayout(self.gb_SizeAdj)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.gb_SizeAdj)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.pdsbVertexScale = Gui_PrefDoubleSpinBox(self.gb_SizeAdj)
        self.pdsbVertexScale.setObjectName(u"pdsbVertexScale")
        sizePolicy1.setHeightForWidth(self.pdsbVertexScale.sizePolicy().hasHeightForWidth())
        self.pdsbVertexScale.setSizePolicy(sizePolicy1)
        self.pdsbVertexScale.setMinimumSize(QSize(174, 0))
        self.pdsbVertexScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pdsbVertexScale.setValue(5.000000000000000)
        self.pdsbVertexScale.setProperty(u"prefEntry", u"VertexScale")
        self.pdsbVertexScale.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout_3.addWidget(self.pdsbVertexScale, 0, 2, 1, 1)

        self.label_2 = QLabel(self.gb_SizeAdj)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.pdsbCenterScale = Gui_PrefDoubleSpinBox(self.gb_SizeAdj)
        self.pdsbCenterScale.setObjectName(u"pdsbCenterScale")
        sizePolicy1.setHeightForWidth(self.pdsbCenterScale.sizePolicy().hasHeightForWidth())
        self.pdsbCenterScale.setSizePolicy(sizePolicy1)
        self.pdsbCenterScale.setMinimumSize(QSize(174, 0))
        self.pdsbCenterScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pdsbCenterScale.setSingleStep(0.100000000000000)
        self.pdsbCenterScale.setValue(0.500000000000000)
        self.pdsbCenterScale.setProperty(u"prefEntry", u"CenterMarkScale")
        self.pdsbCenterScale.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout_3.addWidget(self.pdsbCenterScale, 1, 2, 1, 1)

        self.label_7 = QLabel(self.gb_SizeAdj)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.pdsbTemplateMark = Gui_PrefUnitSpinBox(self.gb_SizeAdj)
        self.pdsbTemplateMark.setObjectName(u"pdsbTemplateMark")
        sizePolicy1.setHeightForWidth(self.pdsbTemplateMark.sizePolicy().hasHeightForWidth())
        self.pdsbTemplateMark.setSizePolicy(sizePolicy1)
        self.pdsbTemplateMark.setMinimumSize(QSize(174, 0))
        self.pdsbTemplateMark.setProperty(u"value", 3.000000000000000)
        self.pdsbTemplateMark.setProperty(u"prefEntry", u"TemplateDotSize")
        self.pdsbTemplateMark.setProperty(u"prefPath", u"Mod/TechDraw/General")

        self.gridLayout_3.addWidget(self.pdsbTemplateMark, 2, 2, 1, 1)

        self.label_5 = QLabel(self.gb_SizeAdj)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)

        self.pdsbSymbolScale = Gui_PrefDoubleSpinBox(self.gb_SizeAdj)
        self.pdsbSymbolScale.setObjectName(u"pdsbSymbolScale")
        self.pdsbSymbolScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pdsbSymbolScale.setSingleStep(0.100000000000000)
        self.pdsbSymbolScale.setValue(1.250000000000000)
        self.pdsbSymbolScale.setProperty(u"prefEntry", u"SymbolFactor")
        self.pdsbSymbolScale.setProperty(u"prefPath", u"Mod/TechDraw/Decorations")

        self.gridLayout_3.addWidget(self.pdsbSymbolScale, 3, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.verticalLayout_4.addWidget(self.gb_SizeAdj)

        self.label_12 = QLabel(TechDrawGui__DlgPrefsTechDrawScaleImp)
        self.label_12.setObjectName(u"label_12")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setItalic(False)
        self.label_12.setFont(font1)
        self.label_12.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_12)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.retranslateUi(TechDrawGui__DlgPrefsTechDrawScaleImp)

        QMetaObject.connectSlotsByName(TechDrawGui__DlgPrefsTechDrawScaleImp)
    # setupUi

    def retranslateUi(self, TechDrawGui__DlgPrefsTechDrawScaleImp):
        TechDrawGui__DlgPrefsTechDrawScaleImp.setWindowTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Scale", None))
#if QT_CONFIG(tooltip)
        TechDrawGui__DlgPrefsTechDrawScaleImp.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.gbScale.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Scale", None))
        self.label_13.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Page scale", None))
        self.label_15.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"View custom scale", None))
        self.cbViewScaleType.setItemText(0, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Page", None))
        self.cbViewScaleType.setItemText(1, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Auto", None))
        self.cbViewScaleType.setItemText(2, QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Custom", None))

#if QT_CONFIG(tooltip)
        self.cbViewScaleType.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Default scale for new views", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pdsbPageScale.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Default scale for new pages", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pdsbViewScale.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Default scale for views if 'View scale type' is 'Custom'", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pdsbViewScale.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_14.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"View scale type", None))
#if QT_CONFIG(tooltip)
        self.cbLegacyScale.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Uses the original (incorrect) scaling method for SVG symbols, Spreadsheet views and Draft views as used in v1.0 and earlier. Otherwise, a more accurate method will be used.", None))
#endif // QT_CONFIG(tooltip)
        self.cbLegacyScale.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Legacy symbol scaling", None))
        self.gb_SizeAdj.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Size adjustments", None))
        self.label.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Vertex scale", None))
#if QT_CONFIG(tooltip)
        self.pdsbVertexScale.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Scale of vertex dots. Multiplier of line width.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.pdsbVertexScale.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Center mark scale", None))
#if QT_CONFIG(tooltip)
        self.pdsbCenterScale.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Size of center marks. Multiplier of vertex size.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.pdsbCenterScale.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_7.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Template edit mark", None))
#if QT_CONFIG(tooltip)
        self.pdsbTemplateMark.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Size of template field click handles", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Welding symbol scale", None))
#if QT_CONFIG(tooltip)
        self.pdsbSymbolScale.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"Multiplier for size of welding symbols", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawScaleImp", u"<html><head/><body><p><span style=\" font-weight:600;\">Note:</span> Items in <span style=\" font-style:italic;\">italics</span> are default values for new objects. They have no effect on existing objects.</p></body></html>", None))
    # retranslateUi

