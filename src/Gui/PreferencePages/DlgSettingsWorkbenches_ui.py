# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsWorkbenches.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QListWidgetItem, QSizePolicy, QWidget)

from ListWidgetDragBugFix import ListWidgetDragBugFix

class Ui_Gui_Dialog_DlgSettingsWorkbenches(object):
    def setupUi(self, Gui__Dialog__DlgSettingsWorkbenches):
        if not Gui__Dialog__DlgSettingsWorkbenches.objectName():
            Gui__Dialog__DlgSettingsWorkbenches.setObjectName(u"Gui__Dialog__DlgSettingsWorkbenches")
        Gui__Dialog__DlgSettingsWorkbenches.resize(607, 859)
        self.gridLayout_3 = QGridLayout(Gui__Dialog__DlgSettingsWorkbenches)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.WorkbenchSelectorItemLabel = QLabel(Gui__Dialog__DlgSettingsWorkbenches)
        self.WorkbenchSelectorItemLabel.setObjectName(u"WorkbenchSelectorItemLabel")

        self.hboxLayout.addWidget(self.WorkbenchSelectorItemLabel)

        self.WorkbenchSelectorItem = QComboBox(Gui__Dialog__DlgSettingsWorkbenches)
        self.WorkbenchSelectorItem.setObjectName(u"WorkbenchSelectorItem")

        self.hboxLayout.addWidget(self.WorkbenchSelectorItem)


        self.gridLayout_3.addLayout(self.hboxLayout, 4, 0, 1, 1)

        self.wbList = ListWidgetDragBugFix(Gui__Dialog__DlgSettingsWorkbenches)
        self.wbList.setObjectName(u"wbList")

        self.gridLayout_3.addWidget(self.wbList, 1, 0, 1, 1)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setSpacing(6)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.hboxLayout1.setContentsMargins(0, 0, 0, 0)
        self.WorkbenchSelectorTypeLabel = QLabel(Gui__Dialog__DlgSettingsWorkbenches)
        self.WorkbenchSelectorTypeLabel.setObjectName(u"WorkbenchSelectorTypeLabel")

        self.hboxLayout1.addWidget(self.WorkbenchSelectorTypeLabel)

        self.WorkbenchSelectorType = QComboBox(Gui__Dialog__DlgSettingsWorkbenches)
        self.WorkbenchSelectorType.setObjectName(u"WorkbenchSelectorType")

        self.hboxLayout1.addWidget(self.WorkbenchSelectorType)


        self.gridLayout_3.addLayout(self.hboxLayout1, 3, 0, 1, 1)

        self.noteLabel = QLabel(Gui__Dialog__DlgSettingsWorkbenches)
        self.noteLabel.setObjectName(u"noteLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noteLabel.sizePolicy().hasHeightForWidth())
        self.noteLabel.setSizePolicy(sizePolicy)
        self.noteLabel.setMinimumSize(QSize(0, 50))
        self.noteLabel.setWordWrap(True)

        self.gridLayout_3.addWidget(self.noteLabel, 0, 0, 1, 1)

        self.CheckBox_WbByTab = Gui_PrefCheckBox(Gui__Dialog__DlgSettingsWorkbenches)
        self.CheckBox_WbByTab.setObjectName(u"CheckBox_WbByTab")
        self.CheckBox_WbByTab.setChecked(False)
        self.CheckBox_WbByTab.setProperty(u"prefEntry", u"SaveWBbyTab")
        self.CheckBox_WbByTab.setProperty(u"prefPath", u"View")

        self.gridLayout_3.addWidget(self.CheckBox_WbByTab, 5, 0, 1, 1)

        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setSpacing(6)
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.hboxLayout2.setContentsMargins(0, 0, 0, 0)
        self.autoModuleLabel = QLabel(Gui__Dialog__DlgSettingsWorkbenches)
        self.autoModuleLabel.setObjectName(u"autoModuleLabel")

        self.hboxLayout2.addWidget(self.autoModuleLabel)

        self.AutoloadModuleCombo = QComboBox(Gui__Dialog__DlgSettingsWorkbenches)
        self.AutoloadModuleCombo.setObjectName(u"AutoloadModuleCombo")

        self.hboxLayout2.addWidget(self.AutoloadModuleCombo)


        self.gridLayout_3.addLayout(self.hboxLayout2, 2, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgSettingsWorkbenches)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsWorkbenches)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsWorkbenches):
        Gui__Dialog__DlgSettingsWorkbenches.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Available Workbenches", None))
        self.WorkbenchSelectorItemLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Workbench selector items style:", None))
#if QT_CONFIG(tooltip)
        self.WorkbenchSelectorItem.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Customize how the items are displayed.", None))
#endif // QT_CONFIG(tooltip)
        self.WorkbenchSelectorTypeLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Workbench selector type:", None))
#if QT_CONFIG(tooltip)
        self.WorkbenchSelectorType.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Choose the workbench selector widget type (restart required).", None))
#endif // QT_CONFIG(tooltip)
        self.noteLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"<html><head/><body><p>You can reorder workbenches by drag and drop or sort them by right-clicking on any workbench and select <span style=\"  font-weight:600; font-style:italic;\">Sort alphabetically</span>. Additional workbenches can be installed through the addon manager.</p><p>\n"
"Currently, your system has the following workbenches:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.CheckBox_WbByTab.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"If checked, application will remember which workbench is active for each tab of the viewport", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox_WbByTab.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Remember active workbench by tab", None))
        self.autoModuleLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Start up workbench:", None))
#if QT_CONFIG(tooltip)
        self.AutoloadModuleCombo.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Choose which workbench will be activated and shown\n"
"after FreeCAD launches", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

