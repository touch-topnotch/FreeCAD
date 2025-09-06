# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-svg.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsDraft(object):
    def setupUi(self, Gui__Dialog__DlgSettingsDraft):
        if not Gui__Dialog__DlgSettingsDraft.objectName():
            Gui__Dialog__DlgSettingsDraft.setObjectName(u"Gui__Dialog__DlgSettingsDraft")
        Gui__Dialog__DlgSettingsDraft.resize(425, 362)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsDraft)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(9, 9, 9, 9)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self._4 = QHBoxLayout()
        self._4.setSpacing(6)
        self._4.setContentsMargins(0, 0, 0, 0)
        self._4.setObjectName(u"_4")
        self.textLabel1_5 = QLabel(self.groupBox)
        self.textLabel1_5.setObjectName(u"textLabel1_5")

        self._4.addWidget(self.textLabel1_5)

        self.gui__prefcombobox_3 = Gui_PrefComboBox(self.groupBox)
        self.gui__prefcombobox_3.addItem("")
        self.gui__prefcombobox_3.addItem("")
        self.gui__prefcombobox_3.setObjectName(u"gui__prefcombobox_3")
        self.gui__prefcombobox_3.setProperty(u"prefEntry", u"svgstyle")
        self.gui__prefcombobox_3.setProperty(u"prefPath", u"Mod/Draft")

        self._4.addWidget(self.gui__prefcombobox_3)


        self.verticalLayout.addLayout(self._4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox = Gui_PrefCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(False)
        self.checkBox.setProperty(u"prefEntry", u"svgDisableUnitScaling")
        self.checkBox.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox1 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox1.setObjectName(u"checkBox1")
        self.checkBox1.setChecked(False)
        self.checkBox1.setProperty(u"prefEntry", u"svgAddWireForInvalidFace")
        self.checkBox1.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout.addWidget(self.checkBox1)

        self.checkBox2 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox2.setObjectName(u"checkBox2")
        self.checkBox2.setChecked(True)
        self.checkBox2.setProperty(u"prefEntry", u"svgMakeCuts")
        self.checkBox2.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout.addWidget(self.checkBox2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.spinBox_precisionSVG = Gui_PrefSpinBox(self.groupBox)
        self.spinBox_precisionSVG.setObjectName(u"spinBox_precisionSVG")
        self.spinBox_precisionSVG.setMinimumSize(QSize(140, 0))
        self.spinBox_precisionSVG.setMaximum(10)
        self.spinBox_precisionSVG.setValue(3)
        self.spinBox_precisionSVG.setProperty(u"prefEntry", u"svgPrecision")
        self.spinBox_precisionSVG.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_5.addWidget(self.spinBox_precisionSVG)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.vboxLayout.addWidget(self.groupBox)

        self.GroupBox12_2 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.GroupBox12_2.setObjectName(u"GroupBox12_2")
        self._3 = QVBoxLayout(self.GroupBox12_2)
        self._3.setSpacing(6)
        self._3.setContentsMargins(9, 9, 9, 9)
        self._3.setObjectName(u"_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_2 = QLabel(self.GroupBox12_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_9.addWidget(self.label_2)

        self.svg_export_style_combobox = Gui_PrefComboBox(self.GroupBox12_2)
        self.svg_export_style_combobox.addItem("")
        self.svg_export_style_combobox.addItem("")
        self.svg_export_style_combobox.setObjectName(u"svg_export_style_combobox")
        self.svg_export_style_combobox.setProperty(u"prefEntry", u"svg_export_style")
        self.svg_export_style_combobox.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_9.addWidget(self.svg_export_style_combobox)


        self._3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gui__prefcheckbox_6 = Gui_PrefCheckBox(self.GroupBox12_2)
        self.gui__prefcheckbox_6.setObjectName(u"gui__prefcheckbox_6")
        self.gui__prefcheckbox_6.setChecked(True)
        self.gui__prefcheckbox_6.setProperty(u"prefEntry", u"SvgLinesBlack")
        self.gui__prefcheckbox_6.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_10.addWidget(self.gui__prefcheckbox_6)


        self._3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.GroupBox12_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.doubleSpinBox = Gui_PrefDoubleSpinBox(self.GroupBox12_2)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setSuffix(u" mm")
        self.doubleSpinBox.setMaximum(9999.989999999999782)
        self.doubleSpinBox.setProperty(u"prefEntry", u"svgDiscretization")
        self.doubleSpinBox.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_2.addWidget(self.doubleSpinBox)


        self._3.addLayout(self.horizontalLayout_2)


        self.vboxLayout.addWidget(self.GroupBox12_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Gui__Dialog__DlgSettingsDraft)

        self.gui__prefcombobox_3.setCurrentIndex(0)
        self.svg_export_style_combobox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsDraft)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsDraft):
        Gui__Dialog__DlgSettingsDraft.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"SVG", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Import Options", None))
        self.textLabel1_5.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Import style", None))
        self.gui__prefcombobox_3.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use default style from Part/PartDesign", None))
        self.gui__prefcombobox_3.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use original SVG style", None))

#if QT_CONFIG(tooltip)
        self.gui__prefcombobox_3.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Method for importing SVG object colors", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, no unit conversion will occur.\n"
"One unit in the SVG file will be interpreted as one millimeter.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Disable unit scaling", None))
#if QT_CONFIG(tooltip)
        self.checkBox1.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If face generation results in a degenerated face,\n"
"a raw wire from the original shape is added", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox1.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Add wires for invalid faces", None))
#if QT_CONFIG(tooltip)
        self.checkBox2.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Check to cut shapes according to the even/odd SVG fill rule", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Apply Cuts", None))
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Coordinate precision (crucial for detecting closed paths)", None))
#if QT_CONFIG(tooltip)
        self.spinBox_precisionSVG.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The number of decimal places used in internal coordinate operations (for example 3 = 0.001).\n"
"	The optimal value depends on the absolute size of the import. Typical values are between 1 and 5.", None))
#endif // QT_CONFIG(tooltip)
        self.GroupBox12_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Export Options", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Export style", None))
        self.svg_export_style_combobox.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Translated (for print & display)", None))
        self.svg_export_style_combobox.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Raw (for CAM)", None))

#if QT_CONFIG(tooltip)
        self.svg_export_style_combobox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Style of SVG file to write when exporting a sketch", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.gui__prefcheckbox_6.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"All white lines will appear in black in the SVG for better readability against white backgrounds", None))
#endif // QT_CONFIG(tooltip)
        self.gui__prefcheckbox_6.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Convert white line color to black", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Maximum segment length for discretized arcs", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Versions of OpenCASCADE older than version 6.8 don't support arc projection.\n"
"In this case arcs will be discretized into small line segments.\n"
"This value is the maximum segment length.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

