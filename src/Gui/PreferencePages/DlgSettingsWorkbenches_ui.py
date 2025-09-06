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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QListWidgetItem, QSizePolicy, QVBoxLayout,
    QWidget)

from ListWidgetDragBugFix import ListWidgetDragBugFix

class Ui_Gui_Dialog_DlgSettingsWorkbenches(object):
    def setupUi(self, Gui__Dialog__DlgSettingsWorkbenches):
        if not Gui__Dialog__DlgSettingsWorkbenches.objectName():
            Gui__Dialog__DlgSettingsWorkbenches.setObjectName(u"Gui__Dialog__DlgSettingsWorkbenches")
        Gui__Dialog__DlgSettingsWorkbenches.resize(980, 859)
        self.verticalLayout_3 = QVBoxLayout(Gui__Dialog__DlgSettingsWorkbenches)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsWorkbenches)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.noteLabel = QLabel(self.groupBox)
        self.noteLabel.setObjectName(u"noteLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noteLabel.sizePolicy().hasHeightForWidth())
        self.noteLabel.setSizePolicy(sizePolicy)
        self.noteLabel.setMinimumSize(QSize(0, 50))
        self.noteLabel.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.noteLabel)

        self.wbList = ListWidgetDragBugFix(self.groupBox)
        self.wbList.setObjectName(u"wbList")

        self.verticalLayout_4.addWidget(self.wbList)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(Gui__Dialog__DlgSettingsWorkbenches)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.WorkbenchSelectorItemLabel = QLabel(self.groupBox_3)
        self.WorkbenchSelectorItemLabel.setObjectName(u"WorkbenchSelectorItemLabel")

        self.hboxLayout.addWidget(self.WorkbenchSelectorItemLabel)

        self.WorkbenchSelectorItem = QComboBox(self.groupBox_3)
        self.WorkbenchSelectorItem.setObjectName(u"WorkbenchSelectorItem")

        self.hboxLayout.addWidget(self.WorkbenchSelectorItem)


        self.verticalLayout.addLayout(self.hboxLayout)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setSpacing(6)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.hboxLayout1.setContentsMargins(0, 0, 0, 0)
        self.WorkbenchSelectorTypeLabel = QLabel(self.groupBox_3)
        self.WorkbenchSelectorTypeLabel.setObjectName(u"WorkbenchSelectorTypeLabel")

        self.hboxLayout1.addWidget(self.WorkbenchSelectorTypeLabel)

        self.WorkbenchSelectorType = QComboBox(self.groupBox_3)
        self.WorkbenchSelectorType.setObjectName(u"WorkbenchSelectorType")

        self.hboxLayout1.addWidget(self.WorkbenchSelectorType)


        self.verticalLayout.addLayout(self.hboxLayout1)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsWorkbenches)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setSpacing(6)
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.hboxLayout2.setContentsMargins(0, 0, 0, 0)
        self.autoModuleLabel = QLabel(self.groupBox_2)
        self.autoModuleLabel.setObjectName(u"autoModuleLabel")

        self.hboxLayout2.addWidget(self.autoModuleLabel)

        self.AutoloadModuleCombo = QComboBox(self.groupBox_2)
        self.AutoloadModuleCombo.setObjectName(u"AutoloadModuleCombo")

        self.hboxLayout2.addWidget(self.AutoloadModuleCombo)


        self.verticalLayout_2.addLayout(self.hboxLayout2)

        self.CheckBox_WbByTab = Gui_PrefCheckBox(self.groupBox_2)
        self.CheckBox_WbByTab.setObjectName(u"CheckBox_WbByTab")
        self.CheckBox_WbByTab.setChecked(False)
        self.CheckBox_WbByTab.setProperty(u"prefEntry", u"SaveWBbyTab")
        self.CheckBox_WbByTab.setProperty(u"prefPath", u"View")

        self.verticalLayout_2.addWidget(self.CheckBox_WbByTab)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.retranslateUi(Gui__Dialog__DlgSettingsWorkbenches)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsWorkbenches)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsWorkbenches):
        Gui__Dialog__DlgSettingsWorkbenches.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Available Workbenches", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Workbenches", None))
        self.noteLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"<html><head/><body><p>You can reorder workbenches by drag and drop or sort them by right-clicking on any workbench and select <span style=\"  font-weight:600; font-style:italic;\">Sort alphabetically</span>. Additional workbenches can be installed through the addon manager.</p><p>\n"
"Currently installed workbenches:</p></body></html>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Selectors", None))
        self.WorkbenchSelectorItemLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Workbench selector items style", None))
#if QT_CONFIG(tooltip)
        self.WorkbenchSelectorItem.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Customizes how the items are displayed", None))
#endif // QT_CONFIG(tooltip)
        self.WorkbenchSelectorTypeLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Workbench selector type", None))
#if QT_CONFIG(tooltip)
        self.WorkbenchSelectorType.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Choose the workbench selector widget type (restart required)", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Startup", None))
        self.autoModuleLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Default workbench", None))
#if QT_CONFIG(tooltip)
        self.AutoloadModuleCombo.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Changes which workbench will be activated and shown\n"
"after FreeCAD launches", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.CheckBox_WbByTab.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Remembers which workbench is active for each tab of the viewport", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox_WbByTab.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsWorkbenches", u"Remember active workbench by tab", None))
    # retranslateUi

