# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-drafttexts.ui'
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

class Ui_Gui_Dialog_DlgSettingsDraft(object):
    def setupUi(self, Gui__Dialog__DlgSettingsDraft):
        if not Gui__Dialog__DlgSettingsDraft.objectName():
            Gui__Dialog__DlgSettingsDraft.setObjectName(u"Gui__Dialog__DlgSettingsDraft")
        Gui__Dialog__DlgSettingsDraft.resize(555, 836)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsDraft)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(30, 30, 30, 30)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.groupBox_1 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.gridLayout_1 = QGridLayout(self.groupBox_1)
        self.gridLayout_1.setSpacing(6)
        self.gridLayout_1.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.label_DefaultAnnoScaleMultiplier = QLabel(self.groupBox_1)
        self.label_DefaultAnnoScaleMultiplier.setObjectName(u"label_DefaultAnnoScaleMultiplier")

        self.gridLayout_1.addWidget(self.label_DefaultAnnoScaleMultiplier, 0, 0, 1, 1)

        self.spinBox_DefaultAnnoScaleMultiplier = Gui_PrefDoubleSpinBox(self.groupBox_1)
        self.spinBox_DefaultAnnoScaleMultiplier.setObjectName(u"spinBox_DefaultAnnoScaleMultiplier")
        self.spinBox_DefaultAnnoScaleMultiplier.setMinimumSize(QSize(140, 0))
        self.spinBox_DefaultAnnoScaleMultiplier.setMinimum(0)
        self.spinBox_DefaultAnnoScaleMultiplier.setMaximum(10000)
        self.spinBox_DefaultAnnoScaleMultiplier.setValue(1.000000000000000)
        self.spinBox_DefaultAnnoScaleMultiplier.setProperty(u"prefEntry", u"DefaultAnnoScaleMultiplier")
        self.spinBox_DefaultAnnoScaleMultiplier.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.spinBox_DefaultAnnoScaleMultiplier, 0, 1, 1, 1)

        self.horizontalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_1.addItem(self.horizontalSpacer_1, 0, 2, 1, 1)


        self.vboxLayout.addWidget(self.groupBox_1)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_textfont = QLabel(self.groupBox_2)
        self.label_textfont.setObjectName(u"label_textfont")

        self.gridLayout_2.addWidget(self.label_textfont, 0, 0, 1, 1)

        self.fontBox_textfont = Gui_PrefFontBox(self.groupBox_2)
        self.fontBox_textfont.setObjectName(u"fontBox_textfont")
        self.fontBox_textfont.setMinimumSize(QSize(280, 0))
        self.fontBox_textfont.setProperty(u"prefEntry", u"textfont")
        self.fontBox_textfont.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.fontBox_textfont, 0, 1, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.label_textheight = QLabel(self.groupBox_2)
        self.label_textheight.setObjectName(u"label_textheight")

        self.gridLayout_2.addWidget(self.label_textheight, 1, 0, 1, 1)

        self.spinBox_textheight = Gui_PrefUnitSpinBox(self.groupBox_2)
        self.spinBox_textheight.setObjectName(u"spinBox_textheight")
        self.spinBox_textheight.setMinimumSize(QSize(140, 0))
        self.spinBox_textheight.setSingleStep(0.100000000000000)
        self.spinBox_textheight.setMinimum(0.000000000000000)
        self.spinBox_textheight.setProperty(u"rawValue", 3.500000000000000)
        self.spinBox_textheight.setProperty(u"prefEntry", u"textheight")
        self.spinBox_textheight.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.spinBox_textheight, 1, 1, 1, 1)

        self.label_LineSpacing = QLabel(self.groupBox_2)
        self.label_LineSpacing.setObjectName(u"label_LineSpacing")

        self.gridLayout_2.addWidget(self.label_LineSpacing, 2, 0, 1, 1)

        self.spinBox_LineSpacing = Gui_PrefDoubleSpinBox(self.groupBox_2)
        self.spinBox_LineSpacing.setObjectName(u"spinBox_LineSpacing")
        self.spinBox_LineSpacing.setSingleStep(0.100000000000000)
        self.spinBox_LineSpacing.setValue(1.000000000000000)
        self.spinBox_LineSpacing.setProperty(u"prefEntry", u"LineSpacing")
        self.spinBox_LineSpacing.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.spinBox_LineSpacing, 2, 1, 1, 1)

        self.label_DefaultTextColor = QLabel(self.groupBox_2)
        self.label_DefaultTextColor.setObjectName(u"label_DefaultTextColor")

        self.gridLayout_2.addWidget(self.label_DefaultTextColor, 3, 0, 1, 1)

        self.colorButton_DefaultTextColor = Gui_PrefColorButton(self.groupBox_2)
        self.colorButton_DefaultTextColor.setObjectName(u"colorButton_DefaultTextColor")
        self.colorButton_DefaultTextColor.setProperty(u"color", QColor(0, 0, 0))
        self.colorButton_DefaultTextColor.setProperty(u"prefEntry", u"DefaultTextColor")
        self.colorButton_DefaultTextColor.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.colorButton_DefaultTextColor, 3, 1, 1, 1)


        self.vboxLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_DimShowLine = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBox_DimShowLine.setObjectName(u"checkBox_DimShowLine")
        self.checkBox_DimShowLine.setChecked(True)
        self.checkBox_DimShowLine.setProperty(u"prefEntry", u"DimShowLine")
        self.checkBox_DimShowLine.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_3.addWidget(self.checkBox_DimShowLine, 0, 0, 1, 3)

        self.label_DefaultAnnoLineWidth = QLabel(self.groupBox_3)
        self.label_DefaultAnnoLineWidth.setObjectName(u"label_DefaultAnnoLineWidth")

        self.gridLayout_3.addWidget(self.label_DefaultAnnoLineWidth, 1, 0, 1, 1)

        self.spinBox_DefaultAnnoLineWidth = Gui_PrefSpinBox(self.groupBox_3)
        self.spinBox_DefaultAnnoLineWidth.setObjectName(u"spinBox_DefaultAnnoLineWidth")
        self.spinBox_DefaultAnnoLineWidth.setMinimum(1)
        self.spinBox_DefaultAnnoLineWidth.setValue(2)
        self.spinBox_DefaultAnnoLineWidth.setProperty(u"prefEntry", u"DefaultAnnoLineWidth")
        self.spinBox_DefaultAnnoLineWidth.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_3.addWidget(self.spinBox_DefaultAnnoLineWidth, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.label_dimsymbolstart = QLabel(self.groupBox_3)
        self.label_dimsymbolstart.setObjectName(u"label_dimsymbolstart")

        self.gridLayout_3.addWidget(self.label_dimsymbolstart, 2, 0, 1, 1)

        self.comboBox_dimsymbolstart = Gui_PrefComboBox(self.groupBox_3)
        self.comboBox_dimsymbolstart.addItem("")
        self.comboBox_dimsymbolstart.addItem("")
        self.comboBox_dimsymbolstart.addItem("")
        self.comboBox_dimsymbolstart.addItem("")
        self.comboBox_dimsymbolstart.addItem("")
        self.comboBox_dimsymbolstart.addItem("")
        self.comboBox_dimsymbolstart.setObjectName(u"comboBox_dimsymbolstart")
        self.comboBox_dimsymbolstart.setMinimumSize(QSize(140, 0))
        self.comboBox_dimsymbolstart.setProperty(u"prefEntry", u"dimsymbolstart")
        self.comboBox_dimsymbolstart.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_3.addWidget(self.comboBox_dimsymbolstart, 2, 1, 1, 1)

        self.label_arrowsizestart = QLabel(self.groupBox_3)
        self.label_arrowsizestart.setObjectName(u"label_arrowsizestart")

        self.gridLayout_3.addWidget(self.label_arrowsizestart, 3, 0, 1, 1)

        self.spinBox_arrowsizestart = Gui_PrefUnitSpinBox(self.groupBox_3)
        self.spinBox_arrowsizestart.setObjectName(u"spinBox_arrowsizestart")
        self.spinBox_arrowsizestart.setSingleStep(0.100000000000000)
        self.spinBox_arrowsizestart.setMinimum(0.000000000000000)
        self.spinBox_arrowsizestart.setProperty(u"rawValue", 1.000000000000000)
        self.spinBox_arrowsizestart.setProperty(u"prefEntry", u"arrowsizestart")
        self.spinBox_arrowsizestart.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_3.addWidget(self.spinBox_arrowsizestart, 3, 1, 1, 1)

        self.label_dimsymbolend = QLabel(self.groupBox_3)
        self.label_dimsymbolend.setObjectName(u"label_dimsymbolend")

        self.gridLayout_3.addWidget(self.label_dimsymbolend, 4, 0, 1, 1)

        self.comboBox_dimsymbolend = Gui_PrefComboBox(self.groupBox_3)
        self.comboBox_dimsymbolend.addItem("")
        self.comboBox_dimsymbolend.addItem("")
        self.comboBox_dimsymbolend.addItem("")
        self.comboBox_dimsymbolend.addItem("")
        self.comboBox_dimsymbolend.addItem("")
        self.comboBox_dimsymbolend.addItem("")
        self.comboBox_dimsymbolend.setObjectName(u"comboBox_dimsymbolend")
        self.comboBox_dimsymbolend.setMinimumSize(QSize(140, 0))
        self.comboBox_dimsymbolend.setProperty(u"prefEntry", u"dimsymbolend")
        self.comboBox_dimsymbolend.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_3.addWidget(self.comboBox_dimsymbolend, 4, 1, 1, 1)

        self.label_arrowsizeend = QLabel(self.groupBox_3)
        self.label_arrowsizeend.setObjectName(u"label_arrowsizeend")

        self.gridLayout_3.addWidget(self.label_arrowsizeend, 5, 0, 1, 1)

        self.spinBox_arrowsizeend = Gui_PrefUnitSpinBox(self.groupBox_3)
        self.spinBox_arrowsizeend.setObjectName(u"spinBox_arrowsizeend")
        self.spinBox_arrowsizeend.setSingleStep(0.100000000000000)
        self.spinBox_arrowsizeend.setMinimum(0.000000000000000)
        self.spinBox_arrowsizeend.setProperty(u"rawValue", 1.000000000000000)
        self.spinBox_arrowsizeend.setProperty(u"prefEntry", u"arrowsizeend")
        self.spinBox_arrowsizeend.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_3.addWidget(self.spinBox_arrowsizeend, 5, 1, 1, 1)

        self.label_DefaultAnnoLineColor = QLabel(self.groupBox_3)
        self.label_DefaultAnnoLineColor.setObjectName(u"label_DefaultAnnoLineColor")

        self.gridLayout_3.addWidget(self.label_DefaultAnnoLineColor, 6, 0, 1, 1)

        self.colorButton_DefaultAnnoLineColor = Gui_PrefColorButton(self.groupBox_3)
        self.colorButton_DefaultAnnoLineColor.setObjectName(u"colorButton_DefaultAnnoLineColor")
        self.colorButton_DefaultAnnoLineColor.setProperty(u"color", QColor(0, 0, 0))
        self.colorButton_DefaultAnnoLineColor.setProperty(u"prefEntry", u"DefaultAnnoLineColor")
        self.colorButton_DefaultAnnoLineColor.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_3.addWidget(self.colorButton_DefaultAnnoLineColor, 6, 1, 1, 1)


        self.vboxLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.checkBox_showUnit = Gui_PrefCheckBox(self.groupBox_4)
        self.checkBox_showUnit.setObjectName(u"checkBox_showUnit")
        self.checkBox_showUnit.setChecked(True)
        self.checkBox_showUnit.setProperty(u"prefEntry", u"showUnit")
        self.checkBox_showUnit.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_4.addWidget(self.checkBox_showUnit, 0, 0, 1, 3)

        self.label_overrideUnit = QLabel(self.groupBox_4)
        self.label_overrideUnit.setObjectName(u"label_overrideUnit")

        self.gridLayout_4.addWidget(self.label_overrideUnit, 1, 0, 1, 1)

        self.lineEdit_overrideUnit = Gui_PrefLineEdit(self.groupBox_4)
        self.lineEdit_overrideUnit.setObjectName(u"lineEdit_overrideUnit")
        self.lineEdit_overrideUnit.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_overrideUnit.setProperty(u"prefEntry", u"overrideUnit")
        self.lineEdit_overrideUnit.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_4.addWidget(self.lineEdit_overrideUnit, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.label_dimPrecision = QLabel(self.groupBox_4)
        self.label_dimPrecision.setObjectName(u"label_dimPrecision")

        self.gridLayout_4.addWidget(self.label_dimPrecision, 2, 0, 1, 1)

        self.spinBox_dimPrecision = Gui_PrefSpinBox(self.groupBox_4)
        self.spinBox_dimPrecision.setObjectName(u"spinBox_dimPrecision")
        self.spinBox_dimPrecision.setMinimum(0)
        self.spinBox_dimPrecision.setMaximum(8)
        self.spinBox_dimPrecision.setValue(2)
        self.spinBox_dimPrecision.setProperty(u"prefEntry", u"dimPrecision")
        self.spinBox_dimPrecision.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_4.addWidget(self.spinBox_dimPrecision, 2, 1, 1, 1)

        self.label_FeetSeparator = QLabel(self.groupBox_4)
        self.label_FeetSeparator.setObjectName(u"label_FeetSeparator")

        self.gridLayout_4.addWidget(self.label_FeetSeparator, 3, 0, 1, 1)

        self.lineEdit_FeetSeparator = Gui_PrefLineEdit(self.groupBox_4)
        self.lineEdit_FeetSeparator.setObjectName(u"lineEdit_FeetSeparator")
        self.lineEdit_FeetSeparator.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_FeetSeparator.setProperty(u"prefEntry", u"FeetSeparator")
        self.lineEdit_FeetSeparator.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_4.addWidget(self.lineEdit_FeetSeparator, 3, 1, 1, 1)


        self.vboxLayout.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_dimovershoot = QLabel(self.groupBox_5)
        self.label_dimovershoot.setObjectName(u"label_dimovershoot")

        self.gridLayout_5.addWidget(self.label_dimovershoot, 0, 0, 1, 1)

        self.spinBox_dimovershoot = Gui_PrefUnitSpinBox(self.groupBox_5)
        self.spinBox_dimovershoot.setObjectName(u"spinBox_dimovershoot")
        self.spinBox_dimovershoot.setMinimumSize(QSize(140, 0))
        self.spinBox_dimovershoot.setSingleStep(0.100000000000000)
        self.spinBox_dimovershoot.setProperty(u"rawValue", 0.000000000000000)
        self.spinBox_dimovershoot.setProperty(u"prefEntry", u"dimovershoot")
        self.spinBox_dimovershoot.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_5.addWidget(self.spinBox_dimovershoot, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.label_extlines = QLabel(self.groupBox_5)
        self.label_extlines.setObjectName(u"label_extlines")

        self.gridLayout_5.addWidget(self.label_extlines, 1, 0, 1, 1)

        self.spinBox_extlines = Gui_PrefUnitSpinBox(self.groupBox_5)
        self.spinBox_extlines.setObjectName(u"spinBox_extlines")
        self.spinBox_extlines.setSingleStep(0.100000000000000)
        self.spinBox_extlines.setProperty(u"rawValue", -0.500000000000000)
        self.spinBox_extlines.setProperty(u"prefEntry", u"extlines")
        self.spinBox_extlines.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_5.addWidget(self.spinBox_extlines, 1, 1, 1, 1)

        self.label_extovershoot = QLabel(self.groupBox_5)
        self.label_extovershoot.setObjectName(u"label_extovershoot")

        self.gridLayout_5.addWidget(self.label_extovershoot, 2, 0, 1, 1)

        self.spinBox_extovershoot = Gui_PrefUnitSpinBox(self.groupBox_5)
        self.spinBox_extovershoot.setObjectName(u"spinBox_extovershoot")
        self.spinBox_extovershoot.setSingleStep(0.100000000000000)
        self.spinBox_extovershoot.setProperty(u"rawValue", 2.000000000000000)
        self.spinBox_extovershoot.setProperty(u"prefEntry", u"extovershoot")
        self.spinBox_extovershoot.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_5.addWidget(self.spinBox_extovershoot, 2, 1, 1, 1)

        self.label_dimspacing = QLabel(self.groupBox_5)
        self.label_dimspacing.setObjectName(u"label_dimspacing")

        self.gridLayout_5.addWidget(self.label_dimspacing, 3, 0, 1, 1)

        self.spinBox_dimspacing = Gui_PrefUnitSpinBox(self.groupBox_5)
        self.spinBox_dimspacing.setObjectName(u"spinBox_dimspacing")
        self.spinBox_dimspacing.setSingleStep(0.100000000000000)
        self.spinBox_dimspacing.setMinimum(0.000000000000000)
        self.spinBox_dimspacing.setProperty(u"rawValue", 1.000000000000000)
        self.spinBox_dimspacing.setProperty(u"prefEntry", u"dimspacing")
        self.spinBox_dimspacing.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_5.addWidget(self.spinBox_dimspacing, 3, 1, 1, 1)


        self.vboxLayout.addWidget(self.groupBox_5)

        self.verticalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer_1)


        self.retranslateUi(Gui__Dialog__DlgSettingsDraft)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsDraft)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsDraft):
        Gui__Dialog__DlgSettingsDraft.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Texts and Dimensions", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Annotations", None))
        self.label_DefaultAnnoScaleMultiplier.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Scale multiplier", None))
#if QT_CONFIG(tooltip)
        self.spinBox_DefaultAnnoScaleMultiplier.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default annotation scale multiplier. This is the inverse of the scale set\n"
"in the Draft Scale Widget. If the scale is 1:100 the multiplier is 100.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Texts", None))
        self.label_textfont.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Font name", None))
#if QT_CONFIG(tooltip)
        self.fontBox_textfont.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default font for texts, dimensions and labels", None))
#endif // QT_CONFIG(tooltip)
        self.label_textheight.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Font size", None))
#if QT_CONFIG(tooltip)
        self.spinBox_textheight.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default height for texts, dimension texts and label texts", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_textheight.setProperty(u"unit", QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"mm", None))
        self.label_LineSpacing.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Line spacing factor", None))
#if QT_CONFIG(tooltip)
        self.spinBox_LineSpacing.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default line spacing for multi-line texts and labels (relative to the font size)", None))
#endif // QT_CONFIG(tooltip)
        self.label_DefaultTextColor.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Text color", None))
#if QT_CONFIG(tooltip)
        self.colorButton_DefaultTextColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default color for texts, dimension texts and label texts", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Lines and Arrows", None))
#if QT_CONFIG(tooltip)
        self.checkBox_DimShowLine.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, the dimension line is displayed by default", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_DimShowLine.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Show dimension line", None))
        self.label_DefaultAnnoLineWidth.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Line width", None))
#if QT_CONFIG(tooltip)
        self.spinBox_DefaultAnnoLineWidth.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default line width", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_DefaultAnnoLineWidth.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u" px", None))
        self.label_dimsymbolstart.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Start arrow type", None))
        self.comboBox_dimsymbolstart.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Dot", None))
        self.comboBox_dimsymbolstart.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Circle", None))
        self.comboBox_dimsymbolstart.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Arrow", None))
        self.comboBox_dimsymbolstart.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Tick", None))
        self.comboBox_dimsymbolstart.setItemText(4, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Tick-2", None))
        self.comboBox_dimsymbolstart.setItemText(5, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"None", None))

#if QT_CONFIG(tooltip)
        self.comboBox_dimsymbolstart.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default symbol displayed at the start of dimension lines", None))
#endif // QT_CONFIG(tooltip)
        self.label_arrowsizestart.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Start arrow size", None))
#if QT_CONFIG(tooltip)
        self.spinBox_arrowsizestart.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default starting arrow size", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_arrowsizestart.setProperty(u"unit", QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"mm", None))
        self.label_dimsymbolend.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"End arrow type", None))
        self.comboBox_dimsymbolend.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Dot", None))
        self.comboBox_dimsymbolend.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Circle", None))
        self.comboBox_dimsymbolend.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Arrow", None))
        self.comboBox_dimsymbolend.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Tick", None))
        self.comboBox_dimsymbolend.setItemText(4, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Tick-2", None))
        self.comboBox_dimsymbolend.setItemText(5, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"None", None))

#if QT_CONFIG(tooltip)
        self.comboBox_dimsymbolend.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default symbol displayed at the end of dimension lines", None))
#endif // QT_CONFIG(tooltip)
        self.label_arrowsizeend.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"End arrow size", None))
#if QT_CONFIG(tooltip)
        self.spinBox_arrowsizeend.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default ending arrow size", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_arrowsizeend.setProperty(u"unit", QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"mm", None))
        self.label_DefaultAnnoLineColor.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Line and arrow color", None))
#if QT_CONFIG(tooltip)
        self.colorButton_DefaultAnnoLineColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default color for lines and arrows", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_4.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Units", None))
#if QT_CONFIG(tooltip)
        self.checkBox_showUnit.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, a unit symbol is added to dimension texts by default", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_showUnit.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Show unit", None))
        self.label_overrideUnit.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Unit override", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_overrideUnit.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default unit override for dimensions. Enter a unit such as m\n"
"or cm, leave blank to use the current unit defined in FreeCAD.", None))
#endif // QT_CONFIG(tooltip)
        self.label_dimPrecision.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Number of decimals", None))
#if QT_CONFIG(tooltip)
        self.spinBox_dimPrecision.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default number of decimal places for dimension texts", None))
#endif // QT_CONFIG(tooltip)
        self.label_FeetSeparator.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Feet separator", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_FeetSeparator.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The optional string inserted between the feet and inches values in dimensions", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_5.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Dimension Details", None))
        self.label_dimovershoot.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Dimension line overshoot", None))
#if QT_CONFIG(tooltip)
        self.spinBox_dimovershoot.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default distance the dimension line is extended past the extension lines", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_dimovershoot.setProperty(u"unit", QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"mm", None))
        self.label_extlines.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Extension line length", None))
#if QT_CONFIG(tooltip)
        self.spinBox_extlines.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default length of extension lines. Use 0 for full extension lines. A negative\n"
"value defines the gap between the ends of the extension lines and the measured\n"
"points. A positive value defines the maximum length of the extension lines. Only\n"
"used for linear dimensions.", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_extlines.setProperty(u"unit", QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"mm", None))
        self.label_extovershoot.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Extension line overshoot", None))
#if QT_CONFIG(tooltip)
        self.spinBox_extovershoot.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default length of extension lines above the dimension line", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_extovershoot.setProperty(u"unit", QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"mm", None))
        self.label_dimspacing.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Text spacing", None))
#if QT_CONFIG(tooltip)
        self.spinBox_dimspacing.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default space between the dimension line and the dimension text", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_dimspacing.setProperty(u"unit", QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"mm", None))
    # retranslateUi

