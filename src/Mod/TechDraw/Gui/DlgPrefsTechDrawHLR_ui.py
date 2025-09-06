# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPrefsTechDrawHLR.ui'
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

class Ui_TechDrawGui_DlgPrefsTechDrawHLRImp(object):
    def setupUi(self, TechDrawGui__DlgPrefsTechDrawHLRImp):
        if not TechDrawGui__DlgPrefsTechDrawHLRImp.objectName():
            TechDrawGui__DlgPrefsTechDrawHLRImp.setObjectName(u"TechDrawGui__DlgPrefsTechDrawHLRImp")
        TechDrawGui__DlgPrefsTechDrawHLRImp.resize(440, 307)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__DlgPrefsTechDrawHLRImp.sizePolicy().hasHeightForWidth())
        TechDrawGui__DlgPrefsTechDrawHLRImp.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(TechDrawGui__DlgPrefsTechDrawHLRImp)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gbMisc = QGroupBox(TechDrawGui__DlgPrefsTechDrawHLRImp)
        self.gbMisc.setObjectName(u"gbMisc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gbMisc.sizePolicy().hasHeightForWidth())
        self.gbMisc.setSizePolicy(sizePolicy1)
        self.gbMisc.setMinimumSize(QSize(0, 225))
        self.gbMisc.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.gbMisc)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pcbPolygon = Gui_PrefCheckBox(self.gbMisc)
        self.pcbPolygon.setObjectName(u"pcbPolygon")
        sizePolicy1.setHeightForWidth(self.pcbPolygon.sizePolicy().hasHeightForWidth())
        self.pcbPolygon.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setItalic(True)
        self.pcbPolygon.setFont(font)
        self.pcbPolygon.setProperty(u"prefEntry", u"UsePolygon")
        self.pcbPolygon.setProperty(u"prefPath", u"Mod/TechDraw/HLR")

        self.gridLayout_6.addWidget(self.pcbPolygon, 0, 0, 1, 1)

        self.label_17 = QLabel(self.gbMisc)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_6.addWidget(self.label_17, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.label_18 = QLabel(self.gbMisc)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.pcbHardViz = Gui_PrefCheckBox(self.gbMisc)
        self.pcbHardViz.setObjectName(u"pcbHardViz")
        self.pcbHardViz.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pcbHardViz.sizePolicy().hasHeightForWidth())
        self.pcbHardViz.setSizePolicy(sizePolicy1)
        self.pcbHardViz.setFont(font)
        self.pcbHardViz.setFocusPolicy(Qt.NoFocus)
        self.pcbHardViz.setCheckable(True)
        self.pcbHardViz.setChecked(True)
        self.pcbHardViz.setProperty(u"prefEntry", u"HardViz")
        self.pcbHardViz.setProperty(u"prefPath", u"Mod/TechDraw/HLR")

        self.gridLayout_6.addWidget(self.pcbHardViz, 2, 0, 1, 1)

        self.pcbHardHid = Gui_PrefCheckBox(self.gbMisc)
        self.pcbHardHid.setObjectName(u"pcbHardHid")
        sizePolicy1.setHeightForWidth(self.pcbHardHid.sizePolicy().hasHeightForWidth())
        self.pcbHardHid.setSizePolicy(sizePolicy1)
        self.pcbHardHid.setFont(font)
        self.pcbHardHid.setProperty(u"prefEntry", u"HardHid")
        self.pcbHardHid.setProperty(u"prefPath", u"Mod/TechDraw/HLR")

        self.gridLayout_6.addWidget(self.pcbHardHid, 2, 2, 1, 1)

        self.pcbSmoothViz = Gui_PrefCheckBox(self.gbMisc)
        self.pcbSmoothViz.setObjectName(u"pcbSmoothViz")
        sizePolicy1.setHeightForWidth(self.pcbSmoothViz.sizePolicy().hasHeightForWidth())
        self.pcbSmoothViz.setSizePolicy(sizePolicy1)
        self.pcbSmoothViz.setFont(font)
        self.pcbSmoothViz.setChecked(True)
        self.pcbSmoothViz.setProperty(u"prefEntry", u"SmoothViz")
        self.pcbSmoothViz.setProperty(u"prefPath", u"Mod/TechDraw/HLR")

        self.gridLayout_6.addWidget(self.pcbSmoothViz, 3, 0, 1, 1)

        self.pcbSmoothHid = Gui_PrefCheckBox(self.gbMisc)
        self.pcbSmoothHid.setObjectName(u"pcbSmoothHid")
        sizePolicy1.setHeightForWidth(self.pcbSmoothHid.sizePolicy().hasHeightForWidth())
        self.pcbSmoothHid.setSizePolicy(sizePolicy1)
        self.pcbSmoothHid.setFont(font)
        self.pcbSmoothHid.setProperty(u"prefEntry", u"SmoothHid")
        self.pcbSmoothHid.setProperty(u"prefPath", u"Mod/TechDraw/HLR")

        self.gridLayout_6.addWidget(self.pcbSmoothHid, 3, 2, 1, 1)

        self.pcbSeamViz = Gui_PrefCheckBox(self.gbMisc)
        self.pcbSeamViz.setObjectName(u"pcbSeamViz")
        sizePolicy1.setHeightForWidth(self.pcbSeamViz.sizePolicy().hasHeightForWidth())
        self.pcbSeamViz.setSizePolicy(sizePolicy1)
        self.pcbSeamViz.setFont(font)
        self.pcbSeamViz.setChecked(False)
        self.pcbSeamViz.setProperty(u"prefEntry", u"SeamViz")
        self.pcbSeamViz.setProperty(u"prefPath", u"Mod/TechDraw/HLR")

        self.gridLayout_6.addWidget(self.pcbSeamViz, 4, 0, 1, 1)

        self.pcbSeamHid = Gui_PrefCheckBox(self.gbMisc)
        self.pcbSeamHid.setObjectName(u"pcbSeamHid")
        sizePolicy1.setHeightForWidth(self.pcbSeamHid.sizePolicy().hasHeightForWidth())
        self.pcbSeamHid.setSizePolicy(sizePolicy1)
        self.pcbSeamHid.setFont(font)
        self.pcbSeamHid.setProperty(u"prefEntry", u"SeamHid")
        self.pcbSeamHid.setProperty(u"prefPath", u"Mod/TechDraw/HLR")

        self.gridLayout_6.addWidget(self.pcbSeamHid, 4, 2, 1, 1)

        self.pcbIsoViz = Gui_PrefCheckBox(self.gbMisc)
        self.pcbIsoViz.setObjectName(u"pcbIsoViz")
        sizePolicy1.setHeightForWidth(self.pcbIsoViz.sizePolicy().hasHeightForWidth())
        self.pcbIsoViz.setSizePolicy(sizePolicy1)
        self.pcbIsoViz.setFont(font)
        self.pcbIsoViz.setProperty(u"prefEntry", u"IsoViz")
        self.pcbIsoViz.setProperty(u"prefPath", u"Mod/TechDraw/HLR")

        self.gridLayout_6.addWidget(self.pcbIsoViz, 5, 0, 1, 1)

        self.pcbIsoHid = Gui_PrefCheckBox(self.gbMisc)
        self.pcbIsoHid.setObjectName(u"pcbIsoHid")
        sizePolicy1.setHeightForWidth(self.pcbIsoHid.sizePolicy().hasHeightForWidth())
        self.pcbIsoHid.setSizePolicy(sizePolicy1)
        self.pcbIsoHid.setFont(font)
        self.pcbIsoHid.setProperty(u"prefEntry", u"IsoHid")
        self.pcbIsoHid.setProperty(u"prefPath", u"Mod/TechDraw/HLR")

        self.gridLayout_6.addWidget(self.pcbIsoHid, 5, 2, 1, 1)

        self.label_19 = QLabel(self.gbMisc)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 0))
        self.label_19.setFont(font)

        self.gridLayout_6.addWidget(self.label_19, 6, 0, 1, 1)

        self.psbIsoCount = Gui_PrefSpinBox(self.gbMisc)
        self.psbIsoCount.setObjectName(u"psbIsoCount")
        sizePolicy1.setHeightForWidth(self.psbIsoCount.sizePolicy().hasHeightForWidth())
        self.psbIsoCount.setSizePolicy(sizePolicy1)
        self.psbIsoCount.setMaximumSize(QSize(140, 16777215))
        self.psbIsoCount.setAlignment(Qt.AlignRight)
        self.psbIsoCount.setProperty(u"prefEntry", u"IsoCount")
        self.psbIsoCount.setProperty(u"prefPath", u"Mod/TechDraw/HLR")

        self.gridLayout_6.addWidget(self.psbIsoCount, 6, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_6)


        self.verticalLayout_2.addWidget(self.gbMisc)

        self.label_20 = QLabel(TechDrawGui__DlgPrefsTechDrawHLRImp)
        self.label_20.setObjectName(u"label_20")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setItalic(False)
        self.label_20.setFont(font1)
        self.label_20.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_20)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(TechDrawGui__DlgPrefsTechDrawHLRImp)

        QMetaObject.connectSlotsByName(TechDrawGui__DlgPrefsTechDrawHLRImp)
    # setupUi

    def retranslateUi(self, TechDrawGui__DlgPrefsTechDrawHLRImp):
        TechDrawGui__DlgPrefsTechDrawHLRImp.setWindowTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"HLR", None))
#if QT_CONFIG(tooltip)
        TechDrawGui__DlgPrefsTechDrawHLRImp.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.gbMisc.setTitle(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Hidden Line Removal", None))
#if QT_CONFIG(tooltip)
        self.pcbPolygon.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Use an approximation to find hidden lines.\n"
"Fast, but result is a collection of short straight lines.", None))
#endif // QT_CONFIG(tooltip)
        self.pcbPolygon.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Use polygon approximation", None))
        self.label_17.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Visible", None))
        self.label_18.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Hidden", None))
#if QT_CONFIG(tooltip)
        self.pcbHardViz.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Shows hard and outline edges (always shown)", None))
#endif // QT_CONFIG(tooltip)
        self.pcbHardViz.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Show hard lines", None))
#if QT_CONFIG(tooltip)
        self.pcbHardHid.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Shows hidden hard and outline edges", None))
#endif // QT_CONFIG(tooltip)
        self.pcbHardHid.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Show hard lines", None))
#if QT_CONFIG(tooltip)
        self.pcbSmoothViz.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Shows smooth lines", None))
#endif // QT_CONFIG(tooltip)
        self.pcbSmoothViz.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Show smooth lines", None))
#if QT_CONFIG(tooltip)
        self.pcbSmoothHid.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Shows hidden smooth edges", None))
#endif // QT_CONFIG(tooltip)
        self.pcbSmoothHid.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Show smooth lines", None))
#if QT_CONFIG(tooltip)
        self.pcbSeamViz.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Shows seam lines", None))
#endif // QT_CONFIG(tooltip)
        self.pcbSeamViz.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Show seam lines", None))
#if QT_CONFIG(tooltip)
        self.pcbSeamHid.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Shows hidden seam lines", None))
#endif // QT_CONFIG(tooltip)
        self.pcbSeamHid.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Show seam lines", None))
#if QT_CONFIG(tooltip)
        self.pcbIsoViz.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Makes lines of equal parameterization", None))
#endif // QT_CONFIG(tooltip)
        self.pcbIsoViz.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Show UV ISO lines", None))
#if QT_CONFIG(tooltip)
        self.pcbIsoHid.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Shows hidden equal parameterization lines", None))
#endif // QT_CONFIG(tooltip)
        self.pcbIsoHid.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Show UV ISO lines", None))
        self.label_19.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"ISO count", None))
#if QT_CONFIG(tooltip)
        self.psbIsoCount.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"Number of ISO lines per face edge", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("TechDrawGui::DlgPrefsTechDrawHLRImp", u"<html><head/><body><p><span style=\" font-weight:600;\">Note:</span> Items in <span style=\" font-style:italic;\">italics</span> are default values for new objects. They have no effect on existing objects.</p></body></html>", None))
    # retranslateUi

