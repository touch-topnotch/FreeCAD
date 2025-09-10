# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-draftsnap.ui'
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
        Gui__Dialog__DlgSettingsDraft.resize(518, 719)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsDraft)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(11, 11, 11, 11)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.groupBox_1 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.gridLayout_1 = QGridLayout(self.groupBox_1)
        self.gridLayout_1.setSpacing(6)
        self.gridLayout_1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.checkBox_alwaysShowGrid = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_alwaysShowGrid.setObjectName(u"checkBox_alwaysShowGrid")
        self.checkBox_alwaysShowGrid.setChecked(True)
        self.checkBox_alwaysShowGrid.setProperty(u"prefEntry", u"alwaysShowGrid")
        self.checkBox_alwaysShowGrid.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.checkBox_alwaysShowGrid, 0, 0, 1, 3)

        self.checkBox_grid = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_grid.setObjectName(u"checkBox_grid")
        self.checkBox_grid.setEnabled(False)
        self.checkBox_grid.setChecked(True)
        self.checkBox_grid.setProperty(u"prefEntry", u"grid")
        self.checkBox_grid.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.checkBox_grid, 1, 0, 1, 3)

        self.checkBox_gridBorder = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_gridBorder.setObjectName(u"checkBox_gridBorder")
        self.checkBox_gridBorder.setChecked(True)
        self.checkBox_gridBorder.setProperty(u"prefEntry", u"gridBorder")
        self.checkBox_gridBorder.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.checkBox_gridBorder, 2, 0, 1, 3)

        self.checkBox_gridShowHuman = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_gridShowHuman.setObjectName(u"checkBox_gridShowHuman")
        self.checkBox_gridShowHuman.setEnabled(True)
        self.checkBox_gridShowHuman.setChecked(False)
        self.checkBox_gridShowHuman.setProperty(u"prefEntry", u"gridShowHuman")
        self.checkBox_gridShowHuman.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.checkBox_gridShowHuman, 3, 0, 1, 3)

        self.checkBox_coloredGridAxes = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_coloredGridAxes.setObjectName(u"checkBox_coloredGridAxes")
        self.checkBox_coloredGridAxes.setChecked(True)
        self.checkBox_coloredGridAxes.setProperty(u"prefEntry", u"coloredGridAxes")
        self.checkBox_coloredGridAxes.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.checkBox_coloredGridAxes, 4, 0, 1, 3)

        self.label_gridEvery = QLabel(self.groupBox_1)
        self.label_gridEvery.setObjectName(u"label_gridEvery")

        self.gridLayout_1.addWidget(self.label_gridEvery, 5, 0, 1, 1)

        self.spinBox_gridEvery = Gui_PrefSpinBox(self.groupBox_1)
        self.spinBox_gridEvery.setObjectName(u"spinBox_gridEvery")
        self.spinBox_gridEvery.setMinimumSize(QSize(140, 0))
        self.spinBox_gridEvery.setMaximum(1000)
        self.spinBox_gridEvery.setValue(10)
        self.spinBox_gridEvery.setProperty(u"prefEntry", u"gridEvery")
        self.spinBox_gridEvery.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.spinBox_gridEvery, 5, 1, 1, 1)

        self.horizontalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_1.addItem(self.horizontalSpacer_1, 5, 2, 1, 1)

        self.label_gridSpacing = QLabel(self.groupBox_1)
        self.label_gridSpacing.setObjectName(u"label_gridSpacing")

        self.gridLayout_1.addWidget(self.label_gridSpacing, 6, 0, 1, 1)

        self.spinBox_gridSpacing = Gui_PrefQuantitySpinBox(self.groupBox_1)
        self.spinBox_gridSpacing.setObjectName(u"spinBox_gridSpacing")
        self.spinBox_gridSpacing.setProperty(u"unit", u"mm")
        self.spinBox_gridSpacing.setMaximum(9999.989999999999782)
        self.spinBox_gridSpacing.setProperty(u"rawValue", 1.000000000000000)
        self.spinBox_gridSpacing.setProperty(u"prefEntry", u"gridSpacing")
        self.spinBox_gridSpacing.setProperty(u"prefPath", u"Mod/Draft")
        self.spinBox_gridSpacing.setProperty(u"decimals", 4)

        self.gridLayout_1.addWidget(self.spinBox_gridSpacing, 6, 1, 1, 1)

        self.label_gridSize = QLabel(self.groupBox_1)
        self.label_gridSize.setObjectName(u"label_gridSize")

        self.gridLayout_1.addWidget(self.label_gridSize, 7, 0, 1, 1)

        self.spinBox_gridSize = Gui_PrefSpinBox(self.groupBox_1)
        self.spinBox_gridSize.setObjectName(u"spinBox_gridSize")
        self.spinBox_gridSize.setMaximum(10000)
        self.spinBox_gridSize.setValue(100)
        self.spinBox_gridSize.setProperty(u"prefEntry", u"gridSize")
        self.spinBox_gridSize.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.spinBox_gridSize, 7, 1, 1, 1)

        self.label_gridTransparency = QLabel(self.groupBox_1)
        self.label_gridTransparency.setObjectName(u"label_gridTransparency")

        self.gridLayout_1.addWidget(self.label_gridTransparency, 8, 0, 1, 1)

        self.spinBox_gridTransparency = Gui_PrefSpinBox(self.groupBox_1)
        self.spinBox_gridTransparency.setObjectName(u"spinBox_gridTransparency")
        self.spinBox_gridTransparency.setMaximum(100)
        self.spinBox_gridTransparency.setProperty(u"prefEntry", u"gridTransparency")
        self.spinBox_gridTransparency.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.spinBox_gridTransparency, 8, 1, 1, 1)

        self.label_gridColor = QLabel(self.groupBox_1)
        self.label_gridColor.setObjectName(u"label_gridColor")

        self.gridLayout_1.addWidget(self.label_gridColor, 9, 0, 1, 1)

        self.colorButton_gridColor = Gui_PrefColorButton(self.groupBox_1)
        self.colorButton_gridColor.setObjectName(u"colorButton_gridColor")
        self.colorButton_gridColor.setColor(QColor(50, 50, 75))
        self.colorButton_gridColor.setProperty(u"prefEntry", u"gridColor")
        self.colorButton_gridColor.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.colorButton_gridColor, 9, 1, 1, 1)


        self.vboxLayout.addWidget(self.groupBox_1)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_snapStyle = QLabel(self.groupBox_2)
        self.label_snapStyle.setObjectName(u"label_snapStyle")

        self.gridLayout_2.addWidget(self.label_snapStyle, 0, 0, 1, 1)

        self.comboBox_snapStyle = Gui_PrefComboBox(self.groupBox_2)
        self.comboBox_snapStyle.addItem("")
        self.comboBox_snapStyle.addItem("")
        self.comboBox_snapStyle.setObjectName(u"comboBox_snapStyle")
        self.comboBox_snapStyle.setProperty(u"prefEntry", u"snapStyle")
        self.comboBox_snapStyle.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.comboBox_snapStyle, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.label_snapcolor = QLabel(self.groupBox_2)
        self.label_snapcolor.setObjectName(u"label_snapcolor")

        self.gridLayout_2.addWidget(self.label_snapcolor, 1, 0, 1, 1)

        self.colorButton_snapcolor = Gui_PrefColorButton(self.groupBox_2)
        self.colorButton_snapcolor.setObjectName(u"colorButton_snapcolor")
        self.colorButton_snapcolor.setColor(QColor(255, 170, 0))
        self.colorButton_snapcolor.setProperty(u"prefEntry", u"snapcolor")
        self.colorButton_snapcolor.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.colorButton_snapcolor, 1, 1, 1, 1)

        self.checkBox_alwaysSnap = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_alwaysSnap.setObjectName(u"checkBox_alwaysSnap")
        self.checkBox_alwaysSnap.setChecked(True)
        self.checkBox_alwaysSnap.setProperty(u"prefEntry", u"alwaysSnap")
        self.checkBox_alwaysSnap.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.checkBox_alwaysSnap, 2, 0, 1, 3)

        self.label_modsnap = QLabel(self.groupBox_2)
        self.label_modsnap.setObjectName(u"label_modsnap")
        self.label_modsnap.setEnabled(False)

        self.gridLayout_2.addWidget(self.label_modsnap, 3, 0, 1, 1)

        self.comboBox_modsnap = Gui_PrefComboBox(self.groupBox_2)
        self.comboBox_modsnap.addItem("")
        self.comboBox_modsnap.addItem("")
        self.comboBox_modsnap.addItem("")
        self.comboBox_modsnap.setObjectName(u"comboBox_modsnap")
        self.comboBox_modsnap.setEnabled(False)
        self.comboBox_modsnap.setMinimumSize(QSize(140, 0))
        self.comboBox_modsnap.setProperty(u"prefEntry", u"modsnap")
        self.comboBox_modsnap.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.comboBox_modsnap, 3, 1, 1, 1)

        self.label_modconstrain = QLabel(self.groupBox_2)
        self.label_modconstrain.setObjectName(u"label_modconstrain")

        self.gridLayout_2.addWidget(self.label_modconstrain, 4, 0, 1, 1)

        self.comboBox_modconstrain = Gui_PrefComboBox(self.groupBox_2)
        self.comboBox_modconstrain.addItem("")
        self.comboBox_modconstrain.addItem("")
        self.comboBox_modconstrain.addItem("")
        self.comboBox_modconstrain.setObjectName(u"comboBox_modconstrain")
        self.comboBox_modconstrain.setProperty(u"prefEntry", u"modconstrain")
        self.comboBox_modconstrain.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.comboBox_modconstrain, 4, 1, 1, 1)

        self.label_modalt = QLabel(self.groupBox_2)
        self.label_modalt.setObjectName(u"label_modalt")

        self.gridLayout_2.addWidget(self.label_modalt, 5, 0, 1, 1)

        self.comboBox_modalt = Gui_PrefComboBox(self.groupBox_2)
        self.comboBox_modalt.addItem("")
        self.comboBox_modalt.addItem("")
        self.comboBox_modalt.addItem("")
        self.comboBox_modalt.setObjectName(u"comboBox_modalt")
        self.comboBox_modalt.setProperty(u"prefEntry", u"modalt")
        self.comboBox_modalt.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.comboBox_modalt, 5, 1, 1, 1)


        self.vboxLayout.addWidget(self.groupBox_2)

        self.verticalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer_1)


        self.retranslateUi(Gui__Dialog__DlgSettingsDraft)
        self.checkBox_alwaysShowGrid.toggled.connect(self.checkBox_grid.setDisabled)
        self.checkBox_gridBorder.toggled.connect(self.checkBox_gridShowHuman.setEnabled)
        self.checkBox_alwaysSnap.toggled.connect(self.label_modsnap.setDisabled)
        self.checkBox_alwaysSnap.toggled.connect(self.comboBox_modsnap.setDisabled)

        self.comboBox_modsnap.setCurrentIndex(1)
        self.comboBox_modalt.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsDraft)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsDraft):
        Gui__Dialog__DlgSettingsDraft.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Grid and snapping", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Grid", None))
#if QT_CONFIG(tooltip)
        self.checkBox_alwaysShowGrid.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, the grid will always be visible in new views.\n"
"Use Draft ToggleGrid to change this for the active view.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_alwaysShowGrid.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Always show the grid", None))
#if QT_CONFIG(tooltip)
        self.checkBox_grid.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, the grid will be visible during commands in new views.\n"
"Use Draft ToggleGrid to change this for the active view.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_grid.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Show the grid during commands", None))
#if QT_CONFIG(tooltip)
        self.checkBox_gridBorder.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, an additional border is displayed around the grid,\n"
"showing the main square size in the bottom left corner", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_gridBorder.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Show grid border", None))
#if QT_CONFIG(tooltip)
        self.checkBox_gridShowHuman.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, the outline of a human figure is displayed at the bottom left\n"
"corner of the grid. Only effective if \"Show grid border\" is enabled.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_gridShowHuman.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Show human figure", None))
#if QT_CONFIG(tooltip)
        self.checkBox_coloredGridAxes.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, the two main axes of the grid are colored red, green or blue\n"
"if they match the X, Y or Z axis of the global coordinate system", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_coloredGridAxes.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Use colored axes", None))
        self.label_gridEvery.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Major lines every", None))
#if QT_CONFIG(tooltip)
        self.spinBox_gridEvery.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The number of squares between major grid lines.\n"
"Major grid lines are thicker than minor grid lines.", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_gridEvery.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u" squares", None))
        self.label_gridSpacing.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Grid spacing", None))
#if QT_CONFIG(tooltip)
        self.spinBox_gridSpacing.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The distance between grid lines", None))
#endif // QT_CONFIG(tooltip)
        self.label_gridSize.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Grid size", None))
#if QT_CONFIG(tooltip)
        self.spinBox_gridSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The number of squares in the X and Y direction of the grid", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_gridSize.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u" squares", None))
        self.label_gridTransparency.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Grid transparency", None))
#if QT_CONFIG(tooltip)
        self.spinBox_gridTransparency.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The overall transparency of the grid", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_gridTransparency.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u" %", None))
        self.label_gridColor.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Grid color", None))
#if QT_CONFIG(tooltip)
        self.colorButton_gridColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The color of the grid", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Snapping and modifier keys", None))
        self.label_snapStyle.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Snap symbol style", None))
        self.comboBox_snapStyle.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Draft classic style", None))
        self.comboBox_snapStyle.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Bitsnpieces style", None))

#if QT_CONFIG(tooltip)
        self.comboBox_snapStyle.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The style for snap symbols", None))
#endif // QT_CONFIG(tooltip)
        self.label_snapcolor.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Snap symbol color", None))
#if QT_CONFIG(tooltip)
        self.colorButton_snapcolor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The color for snap symbols", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_alwaysSnap.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, snapping is activated without the need to press the Snap modifier key", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_alwaysSnap.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Always snap", None))
        self.label_modsnap.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Snap modifier", None))
        self.comboBox_modsnap.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Shift", None))
        self.comboBox_modsnap.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Ctrl", None))
        self.comboBox_modsnap.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Alt", None))

#if QT_CONFIG(tooltip)
        self.comboBox_modsnap.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The Snap modifier key", None))
#endif // QT_CONFIG(tooltip)
        self.label_modconstrain.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Constrain modifier", None))
        self.comboBox_modconstrain.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Shift", None))
        self.comboBox_modconstrain.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Ctrl", None))
        self.comboBox_modconstrain.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Alt", None))

#if QT_CONFIG(tooltip)
        self.comboBox_modconstrain.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The Constrain modifier key", None))
#endif // QT_CONFIG(tooltip)
        self.label_modalt.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Alt modifier", None))
        self.comboBox_modalt.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Shift", None))
        self.comboBox_modalt.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Ctrl", None))
        self.comboBox_modalt.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Alt", None))

#if QT_CONFIG(tooltip)
        self.comboBox_modalt.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The Alt modifier key. The function of this key depends on the command.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

