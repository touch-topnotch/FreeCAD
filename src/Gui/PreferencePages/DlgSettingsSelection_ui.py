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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Gui_Dialog_DlgSettingsSelection(object):
    def setupUi(self, Gui__Dialog__DlgSettingsSelection):
        if not Gui__Dialog__DlgSettingsSelection.objectName():
            Gui__Dialog__DlgSettingsSelection.setObjectName(u"Gui__Dialog__DlgSettingsSelection")
        Gui__Dialog__DlgSettingsSelection.resize(670, 411)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgSettingsSelection)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.checkBoxPreselection = Gui_PrefCheckBox(Gui__Dialog__DlgSettingsSelection)
        self.checkBoxPreselection.setObjectName(u"checkBoxPreselection")
        self.checkBoxPreselection.setMinimumSize(QSize(240, 0))
        self.checkBoxPreselection.setChecked(True)
        self.checkBoxPreselection.setProperty(u"prefEntry", u"EnablePreselection")
        self.checkBoxPreselection.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.checkBoxPreselection, 0, 0, 1, 1)

        self.HighlightColor = Gui_PrefColorButton(Gui__Dialog__DlgSettingsSelection)
        self.HighlightColor.setObjectName(u"HighlightColor")
        self.HighlightColor.setColor(QColor(225, 225, 20))
        self.HighlightColor.setProperty(u"prefEntry", u"HighlightColor")
        self.HighlightColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.HighlightColor, 0, 1, 1, 1)

        self.checkBoxSelection = Gui_PrefCheckBox(Gui__Dialog__DlgSettingsSelection)
        self.checkBoxSelection.setObjectName(u"checkBoxSelection")
        self.checkBoxSelection.setChecked(True)
        self.checkBoxSelection.setProperty(u"prefEntry", u"EnableSelection")
        self.checkBoxSelection.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.checkBoxSelection, 1, 0, 1, 1)

        self.SelectionColor = Gui_PrefColorButton(Gui__Dialog__DlgSettingsSelection)
        self.SelectionColor.setObjectName(u"SelectionColor")
        self.SelectionColor.setColor(QColor(28, 173, 28))
        self.SelectionColor.setProperty(u"prefEntry", u"SelectionColor")
        self.SelectionColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.SelectionColor, 1, 1, 1, 1)

        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.spinPickRadiusLabel = QLabel(Gui__Dialog__DlgSettingsSelection)
        self.spinPickRadiusLabel.setObjectName(u"spinPickRadiusLabel")

        self.horizontalLayout_1.addWidget(self.spinPickRadiusLabel)

        self.horizSpacer_1 = QSpacerItem(250, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_1.addItem(self.horizSpacer_1)


        self.gridLayout.addLayout(self.horizontalLayout_1, 2, 0, 1, 1)

        self.spinPickRadius = Gui_PrefDoubleSpinBox(Gui__Dialog__DlgSettingsSelection)
        self.spinPickRadius.setObjectName(u"spinPickRadius")
        self.spinPickRadius.setMinimumSize(QSize(120, 0))
        self.spinPickRadius.setInputMethodHints(Qt.ImhPreferNumbers)
        self.spinPickRadius.setSuffix(u" px")
        self.spinPickRadius.setDecimals(1)
        self.spinPickRadius.setMinimum(0.500000000000000)
        self.spinPickRadius.setMaximum(200.000000000000000)
        self.spinPickRadius.setValue(5.000000000000000)
        self.spinPickRadius.setProperty(u"prefEntry", u"PickRadius")
        self.spinPickRadius.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.spinPickRadius, 2, 1, 1, 1)

        self.checkBoxAutoSwitch = Gui_PrefCheckBox(Gui__Dialog__DlgSettingsSelection)
        self.checkBoxAutoSwitch.setObjectName(u"checkBoxAutoSwitch")
        self.checkBoxAutoSwitch.setProperty(u"prefEntry", u"SyncView")
        self.checkBoxAutoSwitch.setProperty(u"prefPath", u"TreeView")

        self.gridLayout.addWidget(self.checkBoxAutoSwitch, 3, 0, 1, 2)

        self.checkBoxAutoExpand = Gui_PrefCheckBox(Gui__Dialog__DlgSettingsSelection)
        self.checkBoxAutoExpand.setObjectName(u"checkBoxAutoExpand")
        self.checkBoxAutoExpand.setProperty(u"prefEntry", u"SyncSelection")
        self.checkBoxAutoExpand.setProperty(u"prefPath", u"TreeView")

        self.gridLayout.addWidget(self.checkBoxAutoExpand, 4, 0, 1, 2)

        self.checkBoxPreselect = Gui_PrefCheckBox(Gui__Dialog__DlgSettingsSelection)
        self.checkBoxPreselect.setObjectName(u"checkBoxPreselect")
        self.checkBoxPreselect.setProperty(u"prefEntry", u"PreSelection")
        self.checkBoxPreselect.setProperty(u"prefPath", u"TreeView")

        self.gridLayout.addWidget(self.checkBoxPreselect, 5, 0, 1, 2)

        self.checkBoxRecord = Gui_PrefCheckBox(Gui__Dialog__DlgSettingsSelection)
        self.checkBoxRecord.setObjectName(u"checkBoxRecord")
        self.checkBoxRecord.setProperty(u"prefEntry", u"RecordSelection")
        self.checkBoxRecord.setProperty(u"prefPath", u"TreeView")

        self.gridLayout.addWidget(self.checkBoxRecord, 6, 0, 1, 2)

        self.checkBoxSelectionCheckBoxes = Gui_PrefCheckBox(Gui__Dialog__DlgSettingsSelection)
        self.checkBoxSelectionCheckBoxes.setObjectName(u"checkBoxSelectionCheckBoxes")
        self.checkBoxSelectionCheckBoxes.setProperty(u"prefEntry", u"CheckBoxesSelection")
        self.checkBoxSelectionCheckBoxes.setProperty(u"prefPath", u"TreeView")

        self.gridLayout.addWidget(self.checkBoxSelectionCheckBoxes, 7, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 245, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 0, 1, 2)


        self.retranslateUi(Gui__Dialog__DlgSettingsSelection)
        self.checkBoxPreselection.toggled.connect(self.HighlightColor.setEnabled)
        self.checkBoxSelection.toggled.connect(self.SelectionColor.setEnabled)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsSelection)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsSelection):
        Gui__Dialog__DlgSettingsSelection.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Selection", None))
#if QT_CONFIG(tooltip)
        self.checkBoxPreselection.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Enable preselection, highlighted with specified color", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxPreselection.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Enable preselection", None))
        self.HighlightColor.setText("")
#if QT_CONFIG(tooltip)
        self.checkBoxSelection.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Enable selection, highlighted with specified color", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSelection.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Enable selection", None))
        self.SelectionColor.setText("")
        self.spinPickRadiusLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Pick radius:", None))
#if QT_CONFIG(tooltip)
        self.spinPickRadius.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Area for picking elements in 3D view.\n"
"Larger value eases to pick things, but can make small features impossible to select.\n"
"      ", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxAutoSwitch.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Auto switch to the 3D view containing the selected item", None))
        self.checkBoxAutoExpand.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Auto expand tree item when the corresponding object is selected in 3D view", None))
        self.checkBoxPreselect.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Preselect the object in 3D view when hovering the cursor over the tree item", None))
        self.checkBoxRecord.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Record selection in tree view in order to go back/forward using navigation button", None))
        self.checkBoxSelectionCheckBoxes.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsSelection", u"Add checkboxes for selection in document tree", None))
    # retranslateUi

