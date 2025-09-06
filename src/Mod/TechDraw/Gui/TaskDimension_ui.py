# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskDimension.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskDimension(object):
    def setupUi(self, TechDrawGui__TaskDimension):
        if not TechDrawGui__TaskDimension.objectName():
            TechDrawGui__TaskDimension.setObjectName(u"TechDrawGui__TaskDimension")
        TechDrawGui__TaskDimension.resize(371, 698)
        self.verticalLayout_4 = QVBoxLayout(TechDrawGui__TaskDimension)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gbTolerancing = QGroupBox(TechDrawGui__TaskDimension)
        self.gbTolerancing.setObjectName(u"gbTolerancing")
        self.verticalLayout_2 = QVBoxLayout(self.gbTolerancing)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cbTheoreticallyExact = QCheckBox(self.gbTolerancing)
        self.cbTheoreticallyExact.setObjectName(u"cbTheoreticallyExact")

        self.gridLayout_2.addWidget(self.cbTheoreticallyExact, 0, 0, 1, 1)

        self.cbEqualTolerance = QCheckBox(self.gbTolerancing)
        self.cbEqualTolerance.setObjectName(u"cbEqualTolerance")

        self.gridLayout_2.addWidget(self.cbEqualTolerance, 1, 0, 1, 1)

        self.label_2 = QLabel(self.gbTolerancing)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.qsbOvertolerance = Gui_QuantitySpinBox(self.gbTolerancing)
        self.qsbOvertolerance.setObjectName(u"qsbOvertolerance")
        self.qsbOvertolerance.setMinimumSize(QSize(0, 20))
        self.qsbOvertolerance.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbOvertolerance.setSingleStep(0.100000000000000)
        self.qsbOvertolerance.setValue(0.000000000000000)

        self.gridLayout_2.addWidget(self.qsbOvertolerance, 2, 1, 1, 1)

        self.label_8 = QLabel(self.gbTolerancing)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.qsbUndertolerance = Gui_QuantitySpinBox(self.gbTolerancing)
        self.qsbUndertolerance.setObjectName(u"qsbUndertolerance")
        self.qsbUndertolerance.setMinimumSize(QSize(0, 20))
        self.qsbUndertolerance.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbUndertolerance.setSingleStep(0.100000000000000)
        self.qsbUndertolerance.setValue(0.000000000000000)

        self.gridLayout_2.addWidget(self.qsbUndertolerance, 3, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_4.addWidget(self.gbTolerancing)

        self.gbFormatting = QGroupBox(TechDrawGui__TaskDimension)
        self.gbFormatting.setObjectName(u"gbFormatting")
        self.verticalLayout = QVBoxLayout(self.gbFormatting)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_11 = QLabel(self.gbFormatting)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.leFormatSpecifier = QLineEdit(self.gbFormatting)
        self.leFormatSpecifier.setObjectName(u"leFormatSpecifier")

        self.gridLayout.addWidget(self.leFormatSpecifier, 0, 1, 1, 1)

        self.cbArbitrary = QCheckBox(self.gbFormatting)
        self.cbArbitrary.setObjectName(u"cbArbitrary")

        self.gridLayout.addWidget(self.cbArbitrary, 1, 0, 1, 1)

        self.label = QLabel(self.gbFormatting)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.leFormatSpecifierOverTolerance = QLineEdit(self.gbFormatting)
        self.leFormatSpecifierOverTolerance.setObjectName(u"leFormatSpecifierOverTolerance")

        self.gridLayout.addWidget(self.leFormatSpecifierOverTolerance, 2, 1, 1, 1)

        self.label_12 = QLabel(self.gbFormatting)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)

        self.leFormatSpecifierUnderTolerance = QLineEdit(self.gbFormatting)
        self.leFormatSpecifierUnderTolerance.setObjectName(u"leFormatSpecifierUnderTolerance")

        self.gridLayout.addWidget(self.leFormatSpecifierUnderTolerance, 3, 1, 1, 1)

        self.cbArbitraryTolerances = QCheckBox(self.gbFormatting)
        self.cbArbitraryTolerances.setObjectName(u"cbArbitraryTolerances")

        self.gridLayout.addWidget(self.cbArbitraryTolerances, 4, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.gbFormatting)

        self.gbDisplayStyle = QGroupBox(TechDrawGui__TaskDimension)
        self.gbDisplayStyle.setObjectName(u"gbDisplayStyle")
        self.verticalLayout_3 = QVBoxLayout(self.gbDisplayStyle)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cbArrowheads = QCheckBox(self.gbDisplayStyle)
        self.cbArrowheads.setObjectName(u"cbArrowheads")

        self.gridLayout_3.addWidget(self.cbArrowheads, 0, 0, 1, 1)

        self.label_5 = QLabel(self.gbDisplayStyle)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.dimensionColor = Gui_ColorButton(self.gbDisplayStyle)
        self.dimensionColor.setObjectName(u"dimensionColor")
        self.dimensionColor.setColor(QColor(0, 0, 0))

        self.gridLayout_3.addWidget(self.dimensionColor, 1, 1, 1, 1)

        self.label_7 = QLabel(self.gbDisplayStyle)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.qsbFontSize = Gui_QuantitySpinBox(self.gbDisplayStyle)
        self.qsbFontSize.setObjectName(u"qsbFontSize")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbFontSize.sizePolicy().hasHeightForWidth())
        self.qsbFontSize.setSizePolicy(sizePolicy)
        self.qsbFontSize.setMinimumSize(QSize(0, 20))
        self.qsbFontSize.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbFontSize.setMinimum(0.000000000000000)
        self.qsbFontSize.setValue(4.000000000000000)
        self.qsbFontSize.setProperty(u"prefEntry", u"Font size")
        self.qsbFontSize.setProperty(u"prefPath", u"/Mod/TechDraw/Dimensions")

        self.gridLayout_3.addWidget(self.qsbFontSize, 2, 1, 1, 1)

        self.label_4 = QLabel(self.gbDisplayStyle)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.comboDrawingStyle = QComboBox(self.gbDisplayStyle)
        self.comboDrawingStyle.addItem("")
        self.comboDrawingStyle.addItem("")
        self.comboDrawingStyle.addItem("")
        self.comboDrawingStyle.addItem("")
        self.comboDrawingStyle.setObjectName(u"comboDrawingStyle")

        self.gridLayout_3.addWidget(self.comboDrawingStyle, 3, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.verticalLayout_4.addWidget(self.gbDisplayStyle)

        self.gbLines = QGroupBox(TechDrawGui__TaskDimension)
        self.gbLines.setObjectName(u"gbLines")
        self.verticalLayout_5 = QVBoxLayout(self.gbLines)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.rbOverride = QRadioButton(self.gbLines)
        self.rbOverride.setObjectName(u"rbOverride")

        self.gridLayout_4.addWidget(self.rbOverride, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gbLines)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.dsbDimAngle = QDoubleSpinBox(self.gbLines)
        self.dsbDimAngle.setObjectName(u"dsbDimAngle")
        self.dsbDimAngle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbDimAngle.setMinimum(-360.000000000000000)
        self.dsbDimAngle.setMaximum(360.000000000000000)

        self.gridLayout_4.addWidget(self.dsbDimAngle, 1, 1, 1, 1)

        self.pbDimUseDefault = QPushButton(self.gbLines)
        self.pbDimUseDefault.setObjectName(u"pbDimUseDefault")

        self.gridLayout_4.addWidget(self.pbDimUseDefault, 2, 0, 1, 1)

        self.pbDimUseSelection = QPushButton(self.gbLines)
        self.pbDimUseSelection.setObjectName(u"pbDimUseSelection")

        self.gridLayout_4.addWidget(self.pbDimUseSelection, 2, 1, 1, 1)

        self.label_6 = QLabel(self.gbLines)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)

        self.dsbExtAngle = QDoubleSpinBox(self.gbLines)
        self.dsbExtAngle.setObjectName(u"dsbExtAngle")
        self.dsbExtAngle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbExtAngle.setMinimum(-360.000000000000000)
        self.dsbExtAngle.setMaximum(360.000000000000000)

        self.gridLayout_4.addWidget(self.dsbExtAngle, 3, 1, 1, 1)

        self.pbExtUseDefault = QPushButton(self.gbLines)
        self.pbExtUseDefault.setObjectName(u"pbExtUseDefault")

        self.gridLayout_4.addWidget(self.pbExtUseDefault, 4, 0, 1, 1)

        self.pbExtUseSelection = QPushButton(self.gbLines)
        self.pbExtUseSelection.setObjectName(u"pbExtUseSelection")

        self.gridLayout_4.addWidget(self.pbExtUseSelection, 4, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)


        self.verticalLayout_4.addWidget(self.gbLines)


        self.retranslateUi(TechDrawGui__TaskDimension)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskDimension)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskDimension):
        TechDrawGui__TaskDimension.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Dimension", None))
        self.gbTolerancing.setTitle(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Tolerancing", None))
#if QT_CONFIG(tooltip)
        self.cbTheoreticallyExact.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"If theoretically exact (basic) dimension", None))
#endif // QT_CONFIG(tooltip)
        self.cbTheoreticallyExact.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Theoretically exact", None))
#if QT_CONFIG(tooltip)
        self.cbEqualTolerance.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Assign same value to over and under tolerance", None))
#endif // QT_CONFIG(tooltip)
        self.cbEqualTolerance.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Equal tolerance", None))
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Overtolerance", None))
#if QT_CONFIG(tooltip)
        self.qsbOvertolerance.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Overtolerance value\n"
"If 'Equal tolerance' is checked this is also\n"
"the negated value for 'Undertolerance'.", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Undertolerance", None))
#if QT_CONFIG(tooltip)
        self.qsbUndertolerance.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Undertolerance value\n"
"If 'Equal tolerance' is checked it will be replaced\n"
"by negative value of 'Overtolerance'.", None))
#endif // QT_CONFIG(tooltip)
        self.gbFormatting.setTitle(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Formatting", None))
        self.label_11.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Format specifier", None))
#if QT_CONFIG(tooltip)
        self.leFormatSpecifier.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Text to be displayed", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cbArbitrary.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Sets use of 'Format spec' instead of the dimension value", None))
#endif // QT_CONFIG(tooltip)
        self.cbArbitrary.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Arbitrary text", None))
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Overtolerance format specifier", None))
#if QT_CONFIG(tooltip)
        self.leFormatSpecifierOverTolerance.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Specifies the overtolerance format in printf() style, or arbitrary text", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Undertolerance format specifier", None))
#if QT_CONFIG(tooltip)
        self.leFormatSpecifierUnderTolerance.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Specifies the undertolerance format in printf() style, or arbitrary text", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cbArbitraryTolerances.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"<html><head/><body><p>Uses the tolerance format spec</p><p>instead of the tolerance value</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cbArbitraryTolerances.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Arbitrary tolerance text", None))
        self.gbDisplayStyle.setTitle(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Display Style", None))
#if QT_CONFIG(tooltip)
        self.cbArrowheads.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Reverses usual direction of dimension line terminators", None))
#endif // QT_CONFIG(tooltip)
        self.cbArrowheads.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Flip arrowheads", None))
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Color", None))
#if QT_CONFIG(tooltip)
        self.dimensionColor.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Color of the dimension", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Font size", None))
#if QT_CONFIG(tooltip)
        self.qsbFontSize.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Font size for text", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Drawing style", None))
        self.comboDrawingStyle.setItemText(0, QCoreApplication.translate("TechDrawGui::TaskDimension", u"ISO oriented", None))
        self.comboDrawingStyle.setItemText(1, QCoreApplication.translate("TechDrawGui::TaskDimension", u"ISO referencing", None))
        self.comboDrawingStyle.setItemText(2, QCoreApplication.translate("TechDrawGui::TaskDimension", u"ASME inlined", None))
        self.comboDrawingStyle.setItemText(3, QCoreApplication.translate("TechDrawGui::TaskDimension", u"ASME referencing", None))

#if QT_CONFIG(tooltip)
        self.comboDrawingStyle.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Standard and style according to which dimension is drawn", None))
#endif // QT_CONFIG(tooltip)
        self.gbLines.setTitle(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Lines", None))
#if QT_CONFIG(tooltip)
        self.rbOverride.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Use override angles if checked. Use default angles if unchecked.", None))
#endif // QT_CONFIG(tooltip)
        self.rbOverride.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Override angles", None))
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Dimension line angle", None))
#if QT_CONFIG(tooltip)
        self.dsbDimAngle.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Angle of dimension line with drawing X axis (degrees)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbDimUseDefault.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Set dimension line angle to default (orthographic view)", None))
#endif // QT_CONFIG(tooltip)
        self.pbDimUseDefault.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Use Default", None))
#if QT_CONFIG(tooltip)
        self.pbDimUseSelection.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Set dimension line angle to match selected edge or vertices", None))
#endif // QT_CONFIG(tooltip)
        self.pbDimUseSelection.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Use Selection", None))
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Extension line angle", None))
#if QT_CONFIG(tooltip)
        self.dsbExtAngle.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Angle of extension lines with drawing X axis (degrees)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbExtUseDefault.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Set extension line angle to default (orthographic)", None))
#endif // QT_CONFIG(tooltip)
        self.pbExtUseDefault.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Use Default", None))
#if QT_CONFIG(tooltip)
        self.pbExtUseSelection.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Set extension line angle to match selected edge or vertices", None))
#endif // QT_CONFIG(tooltip)
        self.pbExtUseSelection.setText(QCoreApplication.translate("TechDrawGui::TaskDimension", u"Use Selection", None))
    # retranslateUi

