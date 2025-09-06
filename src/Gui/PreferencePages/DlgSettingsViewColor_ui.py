# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsViewColor.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsViewColor(object):
    def setupUi(self, Gui__Dialog__DlgSettingsViewColor):
        if not Gui__Dialog__DlgSettingsViewColor.objectName():
            Gui__Dialog__DlgSettingsViewColor.setObjectName(u"Gui__Dialog__DlgSettingsViewColor")
        Gui__Dialog__DlgSettingsViewColor.resize(405, 400)
        self.verticalLayout = QVBoxLayout(Gui__Dialog__DlgSettingsViewColor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxColor = QGroupBox(Gui__Dialog__DlgSettingsViewColor)
        self.groupBoxColor.setObjectName(u"groupBoxColor")
        self.gridLayout = QGridLayout(self.groupBoxColor)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.spacer, 2, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButtonSimple = Gui_PrefRadioButton(self.groupBoxColor)
        self.radioButtonSimple.setObjectName(u"radioButtonSimple")
        self.radioButtonSimple.setProperty(u"prefEntry", u"Simple")
        self.radioButtonSimple.setProperty(u"prefPath", u"View")

        self.horizontalLayout_2.addWidget(self.radioButtonSimple)

        self.radioButtonGradient = Gui_PrefRadioButton(self.groupBoxColor)
        self.radioButtonGradient.setObjectName(u"radioButtonGradient")
        self.radioButtonGradient.setChecked(True)
        self.radioButtonGradient.setProperty(u"prefEntry", u"Gradient")
        self.radioButtonGradient.setProperty(u"prefPath", u"View")

        self.horizontalLayout_2.addWidget(self.radioButtonGradient)

        self.rbRadialGradient = Gui_PrefRadioButton(self.groupBoxColor)
        self.rbRadialGradient.setObjectName(u"rbRadialGradient")
        self.rbRadialGradient.setChecked(False)
        self.rbRadialGradient.setProperty(u"prefEntry", u"RadialGradient")
        self.rbRadialGradient.setProperty(u"prefPath", u"View")

        self.horizontalLayout_2.addWidget(self.rbRadialGradient)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.SelectionColor_Background = Gui_PrefColorButton(self.groupBoxColor)
        self.SelectionColor_Background.setObjectName(u"SelectionColor_Background")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectionColor_Background.sizePolicy().hasHeightForWidth())
        self.SelectionColor_Background.setSizePolicy(sizePolicy)
        self.SelectionColor_Background.setProperty(u"color", QColor(20, 20, 163))
        self.SelectionColor_Background.setProperty(u"prefEntry", u"BackgroundColor")
        self.SelectionColor_Background.setProperty(u"prefPath", u"View")

        self.verticalLayout_3.addWidget(self.SelectionColor_Background)

        self._4 = QGridLayout()
        self._4.setSpacing(6)
        self._4.setObjectName(u"_4")
        self._4.setContentsMargins(0, 0, 0, 0)
        self.SwitchGradientColors = QToolButton(self.groupBoxColor)
        self.SwitchGradientColors.setObjectName(u"SwitchGradientColors")
        icon = QIcon()
        icon.addFile(u":/icons/button_sort.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SwitchGradientColors.setIcon(icon)

        self._4.addWidget(self.SwitchGradientColors, 1, 0, 1, 1)

        self.color1Label = QLabel(self.groupBoxColor)
        self.color1Label.setObjectName(u"color1Label")

        self._4.addWidget(self.color1Label, 0, 1, 1, 1)

        self.backgroundColorFrom = Gui_PrefColorButton(self.groupBoxColor)
        self.backgroundColorFrom.setObjectName(u"backgroundColorFrom")
        self.backgroundColorFrom.setProperty(u"color", QColor(51, 51, 101))
        self.backgroundColorFrom.setProperty(u"prefEntry", u"BackgroundColor2")
        self.backgroundColorFrom.setProperty(u"prefPath", u"View")

        self._4.addWidget(self.backgroundColorFrom, 0, 2, 1, 1)

        self.color2Label = QLabel(self.groupBoxColor)
        self.color2Label.setObjectName(u"color2Label")

        self._4.addWidget(self.color2Label, 1, 1, 1, 1)

        self.backgroundColorMid = Gui_PrefColorButton(self.groupBoxColor)
        self.backgroundColorMid.setObjectName(u"backgroundColorMid")
        self.backgroundColorMid.setProperty(u"color", QColor(111, 111, 147))
        self.backgroundColorMid.setProperty(u"prefEntry", u"BackgroundColor4")
        self.backgroundColorMid.setProperty(u"prefPath", u"View")

        self._4.addWidget(self.backgroundColorMid, 1, 2, 1, 1)

        self.checkMidColor = Gui_PrefCheckBox(self.groupBoxColor)
        self.checkMidColor.setObjectName(u"checkMidColor")
        self.checkMidColor.setProperty(u"prefEntry", u"UseBackgroundColorMid")
        self.checkMidColor.setProperty(u"prefPath", u"View")

        self._4.addWidget(self.checkMidColor, 1, 3, 1, 1)

        self.color3Label = QLabel(self.groupBoxColor)
        self.color3Label.setObjectName(u"color3Label")

        self._4.addWidget(self.color3Label, 2, 1, 1, 1)

        self.backgroundColorTo = Gui_PrefColorButton(self.groupBoxColor)
        self.backgroundColorTo.setObjectName(u"backgroundColorTo")
        self.backgroundColorTo.setProperty(u"color", QColor(151, 151, 170))
        self.backgroundColorTo.setProperty(u"prefEntry", u"BackgroundColor3")
        self.backgroundColorTo.setProperty(u"prefPath", u"View")

        self._4.addWidget(self.backgroundColorTo, 2, 2, 1, 1)


        self.verticalLayout_3.addLayout(self._4)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBoxColor)

        self.groupBoxTree = QGroupBox(Gui__Dialog__DlgSettingsViewColor)
        self.groupBoxTree.setObjectName(u"groupBoxTree")
        self.gridLayout1 = QGridLayout(self.groupBoxTree)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
        self.gridLayout2 = QGridLayout()
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.groupBoxTree)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(240, 0))

        self.gridLayout2.addWidget(self.label_2, 0, 0, 1, 1)

        self.TreeEditColor = Gui_PrefColorButton(self.groupBoxTree)
        self.TreeEditColor.setObjectName(u"TreeEditColor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TreeEditColor.sizePolicy().hasHeightForWidth())
        self.TreeEditColor.setSizePolicy(sizePolicy1)
        self.TreeEditColor.setProperty(u"color", QColor(94, 170, 35))
        self.TreeEditColor.setProperty(u"prefEntry", u"TreeEditColor")
        self.TreeEditColor.setProperty(u"prefPath", u"TreeView")

        self.gridLayout2.addWidget(self.TreeEditColor, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBoxTree)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout2.addWidget(self.label_3, 1, 0, 1, 1)

        self.TreeActiveColor = Gui_PrefColorButton(self.groupBoxTree)
        self.TreeActiveColor.setObjectName(u"TreeActiveColor")
        sizePolicy1.setHeightForWidth(self.TreeActiveColor.sizePolicy().hasHeightForWidth())
        self.TreeActiveColor.setSizePolicy(sizePolicy1)
        self.TreeActiveColor.setProperty(u"color", QColor(60, 145, 252))
        self.TreeActiveColor.setProperty(u"prefEntry", u"TreeActiveColor")
        self.TreeActiveColor.setProperty(u"prefPath", u"TreeView")

        self.gridLayout2.addWidget(self.TreeActiveColor, 1, 1, 1, 1)


        self.gridLayout1.addLayout(self.gridLayout2, 0, 0, 1, 1)

        self.spacer_5 = QSpacerItem(183, 23, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout1.addItem(self.spacer_5, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBoxTree)

        self.groupColorBar = QGroupBox(Gui__Dialog__DlgSettingsViewColor)
        self.groupColorBar.setObjectName(u"groupColorBar")
        self.gridLayout3 = QGridLayout(self.groupColorBar)
        self.gridLayout3.setSpacing(6)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.gridLayout3.setContentsMargins(9, 9, 9, 9)
        self.gridLayout4 = QGridLayout()
        self.gridLayout4.setSpacing(6)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.gridLayout4.setContentsMargins(0, 0, 0, 0)
        self.label_CbLabelColor = QLabel(self.groupColorBar)
        self.label_CbLabelColor.setObjectName(u"label_CbLabelColor")
        self.label_CbLabelColor.setMinimumSize(QSize(240, 0))

        self.gridLayout4.addWidget(self.label_CbLabelColor, 0, 0, 1, 1)

        self.CbLabelColor = Gui_PrefColorButton(self.groupColorBar)
        self.CbLabelColor.setObjectName(u"CbLabelColor")
        self.CbLabelColor.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.CbLabelColor.sizePolicy().hasHeightForWidth())
        self.CbLabelColor.setSizePolicy(sizePolicy1)
        self.CbLabelColor.setProperty(u"color", QColor(255, 255, 255))
        self.CbLabelColor.setProperty(u"prefEntry", u"CbLabelColor")
        self.CbLabelColor.setProperty(u"prefPath", u"View")

        self.gridLayout4.addWidget(self.CbLabelColor, 0, 1, 1, 1)

        self.label_CbLabelTextSize = QLabel(self.groupColorBar)
        self.label_CbLabelTextSize.setObjectName(u"label_CbLabelTextSize")

        self.gridLayout4.addWidget(self.label_CbLabelTextSize, 1, 0, 1, 1)

        self.CbLabelTextSize = Gui_PrefSpinBox(self.groupColorBar)
        self.CbLabelTextSize.setObjectName(u"CbLabelTextSize")
        self.CbLabelTextSize.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.CbLabelTextSize.setMinimum(4)
        self.CbLabelTextSize.setMaximum(36)
        self.CbLabelTextSize.setValue(13)
        self.CbLabelTextSize.setProperty(u"prefEntry", u"CbLabelTextSize")
        self.CbLabelTextSize.setProperty(u"prefPath", u"View")

        self.gridLayout4.addWidget(self.CbLabelTextSize, 1, 1, 1, 1)


        self.gridLayout3.addLayout(self.gridLayout4, 0, 0, 1, 1)

        self.spacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout3.addItem(self.spacer_6, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupColorBar)

        self.spacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.spacer_7)

        QWidget.setTabOrder(self.SelectionColor_Background, self.backgroundColorFrom)
        QWidget.setTabOrder(self.backgroundColorFrom, self.backgroundColorTo)
        QWidget.setTabOrder(self.backgroundColorTo, self.checkMidColor)
        QWidget.setTabOrder(self.checkMidColor, self.backgroundColorMid)

        self.retranslateUi(Gui__Dialog__DlgSettingsViewColor)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsViewColor)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsViewColor):
        Gui__Dialog__DlgSettingsViewColor.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Colors", None))
#if QT_CONFIG(tooltip)
        self.groupBoxColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Background color for the model view", None))
#endif // QT_CONFIG(tooltip)
        self.groupBoxColor.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Background Color", None))
#if QT_CONFIG(tooltip)
        self.radioButtonSimple.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Background will have the selected color", None))
#endif // QT_CONFIG(tooltip)
        self.radioButtonSimple.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Simple color", None))
#if QT_CONFIG(tooltip)
        self.radioButtonGradient.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Background will have the selected color gradient", None))
#endif // QT_CONFIG(tooltip)
        self.radioButtonGradient.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Linear gradient", None))
#if QT_CONFIG(tooltip)
        self.rbRadialGradient.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Background will have the selected color gradient", None))
#endif // QT_CONFIG(tooltip)
        self.rbRadialGradient.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Radial gradient", None))
#if QT_CONFIG(tooltip)
        self.SelectionColor_Background.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Background will have the selected color", None))
#endif // QT_CONFIG(tooltip)
        self.SelectionColor_Background.setText("")
#if QT_CONFIG(tooltip)
        self.SwitchGradientColors.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Switches the colors of the gradient", None))
#endif // QT_CONFIG(tooltip)
        self.SwitchGradientColors.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Switch", None))
        self.color1Label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Top", None))
        self.backgroundColorFrom.setText("")
        self.color2Label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Middle", None))
        self.backgroundColorMid.setText("")
#if QT_CONFIG(tooltip)
        self.checkMidColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Color gradient will get the selected color as middle color", None))
#endif // QT_CONFIG(tooltip)
        self.checkMidColor.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Middle color", None))
        self.color3Label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Bottom", None))
        self.backgroundColorTo.setText("")
        self.groupBoxTree.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Tree View", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Object being edited", None))
#if QT_CONFIG(tooltip)
        self.TreeEditColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Background color for objects in the tree view that are currently edited", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Active container object", None))
#if QT_CONFIG(tooltip)
        self.TreeActiveColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Background color for active containers (e.g. part or body) in the tree view", None))
#endif // QT_CONFIG(tooltip)
        self.groupColorBar.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Color Bar", None))
#if QT_CONFIG(tooltip)
        self.label_CbLabelColor.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_CbLabelColor.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Label text color", None))
#if QT_CONFIG(tooltip)
        self.CbLabelColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Color bar label text color (e.g. in Mesh and FEM)", None))
#endif // QT_CONFIG(tooltip)
        self.label_CbLabelTextSize.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Label text size", None))
#if QT_CONFIG(tooltip)
        self.CbLabelTextSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u"Color bar label text size (e.g. in Mesh and FEM)", None))
#endif // QT_CONFIG(tooltip)
        self.CbLabelTextSize.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsViewColor", u" pt", None))
    # retranslateUi

