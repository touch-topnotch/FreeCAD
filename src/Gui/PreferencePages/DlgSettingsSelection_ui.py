# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsSelection.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Gui_Dialog_DlgSettingsSelection(object):
    def setupUi(self, Gui__Dialog__DlgSettingsSelection):
        if not Gui__Dialog__DlgSettingsSelection.objectName():
            Gui__Dialog__DlgSettingsSelection.setObjectName(u"Gui__Dialog__DlgSettingsSelection")
        Gui__Dialog__DlgSettingsSelection.resize(670, 641)
        self.verticalLayout_4 = QVBoxLayout(Gui__Dialog__DlgSettingsSelection)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsSelection)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.SelectionColor = Gui_PrefColorButton(self.groupBox)
        self.SelectionColor.setObjectName(u"SelectionColor")
        self.SelectionColor.setColor(QColor(28, 173, 28))
        self.SelectionColor.setProperty(u"prefEntry", u"SelectionColor")
        self.SelectionColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.SelectionColor, 4, 1, 1, 1)

        self.checkBoxSelection = Gui_PrefCheckBox(self.groupBox)
        self.checkBoxSelection.setObjectName(u"checkBoxSelection")
        self.checkBoxSelection.setChecked(True)
        self.checkBoxSelection.setProperty(u"prefEntry", u"EnableSelection")
        self.checkBoxSelection.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.checkBoxSelection, 4, 0, 1, 1)

        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.spinPickRadiusLabel = QLabel(self.groupBox)
        self.spinPickRadiusLabel.setObjectName(u"spinPickRadiusLabel")

        self.horizontalLayout_1.addWidget(self.spinPickRadiusLabel)

        self.horizSpacer_1 = QSpacerItem(250, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_1.addItem(self.horizSpacer_1)

        self.spinPickRadius = Gui_PrefDoubleSpinBox(self.groupBox)
        self.spinPickRadius.setObjectName(u"spinPickRadius")
        self.spinPickRadius.setMinimumSize(QSize(120, 0))
        self.spinPickRadius.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)
        self.spinPickRadius.setSuffix(u" px")
        self.spinPickRadius.setDecimals(1)
        self.spinPickRadius.setMinimum(0.500000000000000)
        self.spinPickRadius.setMaximum(200.000000000000000)
        self.spinPickRadius.setValue(5.000000000000000)
        self.spinPickRadius.setProperty(u"prefEntry", u"PickRadius")
        self.spinPickRadius.setProperty(u"prefPath", u"View")

        self.horizontalLayout_1.addWidget(self.spinPickRadius)


        self.gridLayout.addLayout(self.horizontalLayout_1, 7, 0, 1, 2)

        self.HighlightColor = Gui_PrefColorButton(self.groupBox)
        self.HighlightColor.setObjectName(u"HighlightColor")
        self.HighlightColor.setColor(QColor(225, 225, 20))
        self.HighlightColor.setProperty(u"prefEntry", u"HighlightColor")
        self.HighlightColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.HighlightColor, 3, 1, 1, 1)

        self.checkBoxPreselection = Gui_PrefCheckBox(self.groupBox)
        self.checkBoxPreselection.setObjectName(u"checkBoxPreselection")
        self.checkBoxPreselection.setMinimumSize(QSize(240, 0))
        self.checkBoxPreselection.setChecked(True)
        self.checkBoxPreselection.setProperty(u"prefEntry", u"EnablePreselection")
        self.checkBoxPreselection.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.checkBoxPreselection, 3, 0, 1, 1)

        self.checkBoxPreselect = Gui_PrefCheckBox(self.groupBox)
        self.checkBoxPreselect.setObjectName(u"checkBoxPreselect")
        self.checkBoxPreselect.setProperty(u"prefEntry", u"PreSelection")
        self.checkBoxPreselect.setProperty(u"prefPath", u"TreeView")

        self.gridLayout.addWidget(self.checkBoxPreselect, 8, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(Gui__Dialog__DlgSettingsSelection)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBoxAutoSwitch = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBoxAutoSwitch.setObjectName(u"checkBoxAutoSwitch")
        self.checkBoxAutoSwitch.setProperty(u"prefEntry", u"SyncView")
        self.checkBoxAutoSwitch.setProperty(u"prefPath", u"TreeView")

        self.verticalLayout_2.addWidget(self.checkBoxAutoSwitch)

        self.checkBoxAutoExpand = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBoxAutoExpand.setObjectName(u"checkBoxAutoExpand")
        self.checkBoxAutoExpand.setProperty(u"prefEntry", u"SyncSelection")
        self.checkBoxAutoExpand.setProperty(u"prefPath", u"TreeView")

        self.verticalLayout_2.addWidget(self.checkBoxAutoExpand)

        self.checkBoxRecord = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBoxRecord.setObjectName(u"checkBoxRecord")
        self.checkBoxRecord.setProperty(u"prefEntry", u"RecordSelection")
        self.checkBoxRecord.setProperty(u"prefPath", u"TreeView")

        self.verticalLayout_2.addWidget(self.checkBoxRecord)

        self.checkBoxSelectionCheckBoxes = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBoxSelectionCheckBoxes.setObjectName(u"checkBoxSelectionCheckBoxes")
        self.checkBoxSelectionCheckBoxes.setProperty(u"prefEntry", u"CheckBoxesSelection")
        self.checkBoxSelectionCheckBoxes.setProperty(u"prefPath", u"TreeView")

        self.verticalLayout_2.addWidget(self.checkBoxSelectionCheckBoxes)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 245, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.retranslateUi(Gui__Dialog__DlgSettingsSelection)
        self.checkBoxPreselection.toggled.connect(self.HighlightColor.setEnabled)
        self.checkBoxSelection.toggled.connect(self.SelectionColor.setEnabled)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsSelection)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsSelection):
        Gui__Dialog__DlgSettingsSelection.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Selection", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Viewport Selection Behavior", None))
        self.SelectionColor.setText("")
#if QT_CONFIG(tooltip)
        self.checkBoxSelection.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Enable selection, highlighted with specified color", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSelection.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Enable selection", None))
        self.spinPickRadiusLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Radius", None))
#if QT_CONFIG(tooltip)
        self.spinPickRadius.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Area for selecting elements in the 3D view.\n"
"A larger value makes it easier to select elements, but may prevent selection of small features.\n"
"      ", None))
#endif // QT_CONFIG(tooltip)
        self.HighlightColor.setText("")
#if QT_CONFIG(tooltip)
        self.checkBoxPreselection.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Enable preselection, highlighted with specified color", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxPreselection.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Enable preselection", None))
        self.checkBoxPreselect.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Preselect the object in the 3D view when hovering the cursor over the tree item", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Tree Selection Behavior", None))
        self.checkBoxAutoSwitch.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Auto switch to the 3D view containing the selected item", None))
        self.checkBoxAutoExpand.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Auto expand tree item when the corresponding object is selected in the 3D view", None))
        self.checkBoxRecord.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Record selection in tree view in order to go back/forward using navigation button", None))
        self.checkBoxSelectionCheckBoxes.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Add checkboxes for selection in document tree", None))
    # retranslateUi

