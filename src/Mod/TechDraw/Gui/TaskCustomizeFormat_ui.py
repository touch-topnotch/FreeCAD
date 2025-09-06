# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskCustomizeFormat.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskCustomizeFormat(object):
    def setupUi(self, TechDrawGui__TaskCustomizeFormat):
        if not TechDrawGui__TaskCustomizeFormat.objectName():
            TechDrawGui__TaskCustomizeFormat.setObjectName(u"TechDrawGui__TaskCustomizeFormat")
        TechDrawGui__TaskCustomizeFormat.resize(200, 622)
        TechDrawGui__TaskCustomizeFormat.setMinimumSize(QSize(200, 0))
        TechDrawGui__TaskCustomizeFormat.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(TechDrawGui__TaskCustomizeFormat)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_GDT = QLabel(TechDrawGui__TaskCustomizeFormat)
        self.label_GDT.setObjectName(u"label_GDT")

        self.verticalLayout.addWidget(self.label_GDT)

        self.grid_GDT = QGridLayout()
        self.grid_GDT.setObjectName(u"grid_GDT")
        self.pbA01 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA01.setObjectName(u"pbA01")
        self.pbA01.setText(u"\u23e4")

        self.grid_GDT.addWidget(self.pbA01, 1, 0, 1, 1)

        self.pbA02 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA02.setObjectName(u"pbA02")
        self.pbA02.setText(u"\u23e5")

        self.grid_GDT.addWidget(self.pbA02, 1, 1, 1, 1)

        self.pbA03 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA03.setObjectName(u"pbA03")
        self.pbA03.setText(u"\u25cb")

        self.grid_GDT.addWidget(self.pbA03, 1, 2, 1, 1)

        self.pbA04 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA04.setObjectName(u"pbA04")
        self.pbA04.setText(u"\u232d")

        self.grid_GDT.addWidget(self.pbA04, 1, 3, 1, 1)

        self.pbA05 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA05.setObjectName(u"pbA05")
        self.pbA05.setText(u"\u2225")

        self.grid_GDT.addWidget(self.pbA05, 1, 4, 1, 1)

        self.pbA06 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA06.setObjectName(u"pbA06")
        self.pbA06.setText(u"\u27c2")

        self.grid_GDT.addWidget(self.pbA06, 2, 0, 1, 1)

        self.pbA07 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA07.setObjectName(u"pbA07")
        self.pbA07.setText(u"\u2220")

        self.grid_GDT.addWidget(self.pbA07, 2, 1, 1, 1)

        self.pbA08 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA08.setObjectName(u"pbA08")
        font = QFont()
        font.setPointSize(9)
        self.pbA08.setFont(font)
        self.pbA08.setText(u"\u2312")

        self.grid_GDT.addWidget(self.pbA08, 2, 2, 1, 1)

        self.pbA09 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA09.setObjectName(u"pbA09")
        self.pbA09.setText(u"\u2313")

        self.grid_GDT.addWidget(self.pbA09, 2, 3, 1, 1)

        self.pbA10 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA10.setObjectName(u"pbA10")
        self.pbA10.setText(u"\u2197")

        self.grid_GDT.addWidget(self.pbA10, 2, 4, 1, 1)

        self.pbA11 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA11.setObjectName(u"pbA11")
        self.pbA11.setText(u"\u2330")

        self.grid_GDT.addWidget(self.pbA11, 3, 0, 1, 1)

        self.pbA12 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA12.setObjectName(u"pbA12")
        self.pbA12.setText(u"\u2316")

        self.grid_GDT.addWidget(self.pbA12, 3, 1, 1, 1)

        self.pbA13 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA13.setObjectName(u"pbA13")
        self.pbA13.setText(u"\u25ce")

        self.grid_GDT.addWidget(self.pbA13, 3, 2, 1, 1)

        self.pbA14 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbA14.setObjectName(u"pbA14")
        self.pbA14.setText(u"\u232f")

        self.grid_GDT.addWidget(self.pbA14, 3, 3, 1, 1)


        self.verticalLayout.addLayout(self.grid_GDT)

        self.label_3 = QLabel(TechDrawGui__TaskCustomizeFormat)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.grid_Modifiers = QGridLayout()
        self.grid_Modifiers.setObjectName(u"grid_Modifiers")
        self.pbB01 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB01.setObjectName(u"pbB01")
        self.pbB01.setFont(font)
        self.pbB01.setText(u"\u24b6")

        self.grid_Modifiers.addWidget(self.pbB01, 0, 0, 1, 1)

        self.pbB02 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB02.setObjectName(u"pbB02")
        self.pbB02.setFont(font)
        self.pbB02.setText(u"\u24b8")

        self.grid_Modifiers.addWidget(self.pbB02, 0, 1, 1, 1)

        self.pbB03 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB03.setObjectName(u"pbB03")
        self.pbB03.setFont(font)
        self.pbB03.setText(u"\u24ba")

        self.grid_Modifiers.addWidget(self.pbB03, 0, 2, 1, 1)

        self.pbB04 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB04.setObjectName(u"pbB04")
        self.pbB04.setFont(font)
        self.pbB04.setText(u"\u24bb")

        self.grid_Modifiers.addWidget(self.pbB04, 0, 3, 1, 1)

        self.pbB05 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB05.setObjectName(u"pbB05")
        self.pbB05.setFont(font)
        self.pbB05.setText(u"\u24bc")

        self.grid_Modifiers.addWidget(self.pbB05, 0, 4, 1, 1)

        self.pbB06 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB06.setObjectName(u"pbB06")
        self.pbB06.setFont(font)
        self.pbB06.setText(u"\u24c1")

        self.grid_Modifiers.addWidget(self.pbB06, 1, 0, 1, 1)

        self.pbB07 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB07.setObjectName(u"pbB07")
        self.pbB07.setFont(font)
        self.pbB07.setText(u"\u24c2")

        self.grid_Modifiers.addWidget(self.pbB07, 1, 1, 1, 1)

        self.pbB08 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB08.setObjectName(u"pbB08")
        self.pbB08.setFont(font)
        self.pbB08.setText(u"\u24c3")

        self.grid_Modifiers.addWidget(self.pbB08, 1, 2, 1, 1)

        self.pbB09 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB09.setObjectName(u"pbB09")
        self.pbB09.setFont(font)
        self.pbB09.setText(u"\u24c5")

        self.grid_Modifiers.addWidget(self.pbB09, 1, 3, 1, 1)

        self.pbB10 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB10.setObjectName(u"pbB10")
        self.pbB10.setFont(font)
        self.pbB10.setText(u"\u24c7")

        self.grid_Modifiers.addWidget(self.pbB10, 1, 4, 1, 1)

        self.pbB11 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB11.setObjectName(u"pbB11")
        self.pbB11.setFont(font)
        self.pbB11.setText(u"\u24c8")

        self.grid_Modifiers.addWidget(self.pbB11, 2, 0, 1, 1)

        self.pbB12 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB12.setObjectName(u"pbB12")
        self.pbB12.setFont(font)
        self.pbB12.setText(u"\u24c9")

        self.grid_Modifiers.addWidget(self.pbB12, 2, 1, 1, 1)

        self.pbB13 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB13.setObjectName(u"pbB13")
        self.pbB13.setFont(font)
        self.pbB13.setText(u"\u24ca")

        self.grid_Modifiers.addWidget(self.pbB13, 2, 2, 1, 1)

        self.pbB14 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbB14.setObjectName(u"pbB14")
        self.pbB14.setFont(font)
        self.pbB14.setText(u"\u24cd")

        self.grid_Modifiers.addWidget(self.pbB14, 2, 3, 1, 1)


        self.verticalLayout.addLayout(self.grid_Modifiers)

        self.label_4 = QLabel(TechDrawGui__TaskCustomizeFormat)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.grid_RadiusDiameter = QGridLayout()
        self.grid_RadiusDiameter.setObjectName(u"grid_RadiusDiameter")
        self.pbC01 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbC01.setObjectName(u"pbC01")
        self.pbC01.setText(u"R")

        self.grid_RadiusDiameter.addWidget(self.pbC01, 4, 0, 1, 1)

        self.pbC02 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbC02.setObjectName(u"pbC02")
        self.pbC02.setText(u"\u2300")

        self.grid_RadiusDiameter.addWidget(self.pbC02, 4, 1, 1, 1)

        self.pbC03 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbC03.setObjectName(u"pbC03")
        self.pbC03.setText(u"SR")

        self.grid_RadiusDiameter.addWidget(self.pbC03, 4, 2, 1, 1)

        self.pbC04 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbC04.setObjectName(u"pbC04")
        self.pbC04.setText(u"S\u2300")

        self.grid_RadiusDiameter.addWidget(self.pbC04, 4, 3, 1, 1)

        self.pbC05 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbC05.setObjectName(u"pbC05")
        self.pbC05.setText(u"\u25a1")

        self.grid_RadiusDiameter.addWidget(self.pbC05, 4, 4, 1, 1)


        self.verticalLayout.addLayout(self.grid_RadiusDiameter)

        self.label_5 = QLabel(TechDrawGui__TaskCustomizeFormat)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.grid_Angles = QGridLayout()
        self.grid_Angles.setObjectName(u"grid_Angles")
        self.pbD01 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbD01.setObjectName(u"pbD01")
        self.pbD01.setText(u"\u00b0")

        self.grid_Angles.addWidget(self.pbD01, 0, 0, 1, 1)

        self.pbD02 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbD02.setObjectName(u"pbD02")
        self.pbD02.setText(u"\u2032")

        self.grid_Angles.addWidget(self.pbD02, 0, 1, 1, 1)

        self.pbD03 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbD03.setObjectName(u"pbD03")
        self.pbD03.setText(u"\u2033")

        self.grid_Angles.addWidget(self.pbD03, 0, 2, 1, 1)

        self.pbD04 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbD04.setObjectName(u"pbD04")
        self.pbD04.setText(u"\u2034")

        self.grid_Angles.addWidget(self.pbD04, 0, 3, 1, 1)


        self.verticalLayout.addLayout(self.grid_Angles)

        self.label = QLabel(TechDrawGui__TaskCustomizeFormat)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.grid_Other = QGridLayout()
        self.grid_Other.setObjectName(u"grid_Other")
        self.grid_Other.setContentsMargins(0, -1, -1, -1)
        self.pbE01 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbE01.setObjectName(u"pbE01")
        self.pbE01.setText(u"\u2332")

        self.grid_Other.addWidget(self.pbE01, 0, 0, 1, 1)

        self.pbE02 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbE02.setObjectName(u"pbE02")
        self.pbE02.setText(u"\u2333")

        self.grid_Other.addWidget(self.pbE02, 0, 1, 1, 1)

        self.pbE03 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbE03.setObjectName(u"pbE03")
        self.pbE03.setText(u"\u2334")

        self.grid_Other.addWidget(self.pbE03, 0, 2, 1, 1)

        self.pbE04 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbE04.setObjectName(u"pbE04")
        self.pbE04.setText(u"\u2335")

        self.grid_Other.addWidget(self.pbE04, 0, 3, 1, 1)

        self.pbE05 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbE05.setObjectName(u"pbE05")
        self.pbE05.setText(u"\u00b1")

        self.grid_Other.addWidget(self.pbE05, 0, 4, 1, 1)

        self.pbE06 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbE06.setObjectName(u"pbE06")
        self.pbE06.setText(u"\u2104")

        self.grid_Other.addWidget(self.pbE06, 1, 0, 1, 1)

        self.pbE07 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbE07.setObjectName(u"pbE07")
        self.pbE07.setText(u"\u2194")

        self.grid_Other.addWidget(self.pbE07, 1, 1, 1, 1)

        self.pbE08 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbE08.setObjectName(u"pbE08")
        self.pbE08.setText(u"\u21a7")

        self.grid_Other.addWidget(self.pbE08, 1, 2, 1, 1)

        self.pbE09 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbE09.setObjectName(u"pbE09")
        self.pbE09.setText(u"\u00d7")

        self.grid_Other.addWidget(self.pbE09, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.grid_Other)

        self.label_6 = QLabel(TechDrawGui__TaskCustomizeFormat)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.grid_Greec = QGridLayout()
        self.grid_Greec.setObjectName(u"grid_Greec")
        self.pbF01 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbF01.setObjectName(u"pbF01")
        self.pbF01.setText(u"\u0394")

        self.grid_Greec.addWidget(self.pbF01, 0, 0, 1, 1)

        self.pbF02 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbF02.setObjectName(u"pbF02")
        self.pbF02.setText(u"\u03a3")

        self.grid_Greec.addWidget(self.pbF02, 0, 1, 1, 1)

        self.pbF03 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbF03.setObjectName(u"pbF03")
        self.pbF03.setText(u"\u03a9")

        self.grid_Greec.addWidget(self.pbF03, 0, 2, 1, 1)

        self.pbF04 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbF04.setObjectName(u"pbF04")
        self.pbF04.setText(u"\u03bc")

        self.grid_Greec.addWidget(self.pbF04, 0, 3, 1, 1)

        self.pbF05 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbF05.setObjectName(u"pbF05")
        self.pbF05.setText(u"\u03c3")

        self.grid_Greec.addWidget(self.pbF05, 0, 4, 1, 1)

        self.pbF06 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbF06.setObjectName(u"pbF06")
        self.pbF06.setText(u"\u03c6")

        self.grid_Greec.addWidget(self.pbF06, 1, 0, 1, 1)

        self.pbF07 = QPushButton(TechDrawGui__TaskCustomizeFormat)
        self.pbF07.setObjectName(u"pbF07")
        self.pbF07.setText(u"\u2375")

        self.grid_Greec.addWidget(self.pbF07, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.grid_Greec)

        self.grid_Format = QGridLayout()
        self.grid_Format.setObjectName(u"grid_Format")
        self.lbFormat = QLabel(TechDrawGui__TaskCustomizeFormat)
        self.lbFormat.setObjectName(u"lbFormat")

        self.grid_Format.addWidget(self.lbFormat, 0, 0, 1, 1)

        self.leFormat = QLineEdit(TechDrawGui__TaskCustomizeFormat)
        self.leFormat.setObjectName(u"leFormat")

        self.grid_Format.addWidget(self.leFormat, 0, 1, 1, 1)

        self.lbPreview = QLabel(TechDrawGui__TaskCustomizeFormat)
        self.lbPreview.setObjectName(u"lbPreview")

        self.grid_Format.addWidget(self.lbPreview, 1, 0, 1, 1)

        self.lbShowPreview = QLabel(TechDrawGui__TaskCustomizeFormat)
        self.lbShowPreview.setObjectName(u"lbShowPreview")

        self.grid_Format.addWidget(self.lbShowPreview, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.grid_Format)


        self.retranslateUi(TechDrawGui__TaskCustomizeFormat)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskCustomizeFormat)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskCustomizeFormat):
        TechDrawGui__TaskCustomizeFormat.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Format Symbols", None))
        self.label_GDT.setText(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"GD&T", None))
#if QT_CONFIG(tooltip)
        self.pbA01.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Straightness", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbA02.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Flatness", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbA03.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Circularity", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbA04.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Cylindricity", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbA05.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Parallelism", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbA06.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Perpendicularity", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbA07.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Angularity", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbA08.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Profile of a line", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbA09.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Profile of a surface", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbA10.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Circular run-out", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbA11.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Total run-out", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbA12.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Position", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbA13.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Concentricity", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbA14.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Symmetry", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Modifiers", None))
#if QT_CONFIG(tooltip)
        self.pbB01.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Derived geometry element", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbB02.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Minimax (Chebychev)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbB03.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Hull condition", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbB04.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Free state", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbB05.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Least square geometry element", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbB06.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Least material condition (LMC)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbB07.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Maximum material condition (MMC)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbB08.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Least inscribed geometry element", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbB09.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Projected tolerance zone", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbB10.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Reciprocity condition", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbB11.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Regardless of feature size (RFS)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbB12.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Tangent plane", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbB13.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Unequal bilateral", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbB14.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Most inscribed geometry element", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Radius & Diameter", None))
#if QT_CONFIG(tooltip)
        self.pbC01.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Radius", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbC02.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Diameter", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbC03.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Radius of sphere", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbC04.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Diameter of sphere", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbC05.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Square", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Angles", None))
#if QT_CONFIG(tooltip)
        self.pbD01.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Degree", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbD02.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"(Arc) minute", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbD03.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"(Arc) second", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbD04.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"(Arc) tertie", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Other", None))
#if QT_CONFIG(tooltip)
        self.pbE01.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Taper", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbE02.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Slope", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbE03.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Counterbore", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbE04.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Countersink", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbE05.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Plus - minus", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbE06.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Centerline", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbE07.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Left/right arrow", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbE08.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Downward arrow", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbE09.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Multiplication sign", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Greek letters", None))
#if QT_CONFIG(tooltip)
        self.pbF01.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Capital delta", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbF02.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Capital sigma", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbF03.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Capital omega", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbF04.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Small mu", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbF05.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Small sigma", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbF06.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Small phi", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbF07.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Small omega", None))
#endif // QT_CONFIG(tooltip)
        self.lbFormat.setText(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Format", None))
        self.lbPreview.setText(QCoreApplication.translate("TechDrawGui::TaskCustomizeFormat", u"Preview", None))
        self.lbShowPreview.setText("")
    # retranslateUi

