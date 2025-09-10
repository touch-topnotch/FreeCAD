# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsMacro.ui'
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

class Ui_Gui_Dialog_DlgSettingsMacro(object):
    def setupUi(self, Gui__Dialog__DlgSettingsMacro):
        if not Gui__Dialog__DlgSettingsMacro.objectName():
            Gui__Dialog__DlgSettingsMacro.setObjectName(u"Gui__Dialog__DlgSettingsMacro")
        Gui__Dialog__DlgSettingsMacro.resize(391, 407)
        self.gridLayout_2 = QGridLayout(Gui__Dialog__DlgSettingsMacro)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsMacro)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.PrefCheckBox_LocalEnv = Gui_PrefCheckBox(self.groupBox)
        self.PrefCheckBox_LocalEnv.setObjectName(u"PrefCheckBox_LocalEnv")
        self.PrefCheckBox_LocalEnv.setChecked(True)
        self.PrefCheckBox_LocalEnv.setProperty(u"prefEntry", u"LocalEnvironment")
        self.PrefCheckBox_LocalEnv.setProperty(u"prefPath", u"Macro")

        self.gridLayout.addWidget(self.PrefCheckBox_LocalEnv, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.GroupBox6 = QGroupBox(Gui__Dialog__DlgSettingsMacro)
        self.GroupBox6.setObjectName(u"GroupBox6")
        self.gridLayout1 = QGridLayout(self.GroupBox6)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
        self.GroupBox8 = QGroupBox(self.GroupBox6)
        self.GroupBox8.setObjectName(u"GroupBox8")
        self.gridLayout2 = QGridLayout(self.GroupBox8)
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayout2.setContentsMargins(11, 11, 11, 11)
        self.MacroPath = Gui_PrefFileChooser(self.GroupBox8)
        self.MacroPath.setObjectName(u"MacroPath")
        self.MacroPath.setMode(Gui.FileChooser.Directory)
        self.MacroPath.setProperty(u"prefEntry", u"MacroPath")
        self.MacroPath.setProperty(u"prefPath", u"Macro")

        self.gridLayout2.addWidget(self.MacroPath, 0, 0, 1, 1)


        self.gridLayout1.addWidget(self.GroupBox8, 0, 0, 1, 1)

        self.GroupBox7 = QGroupBox(self.GroupBox6)
        self.GroupBox7.setObjectName(u"GroupBox7")
        self.gridLayout3 = QGridLayout(self.GroupBox7)
        self.gridLayout3.setSpacing(6)
        self.gridLayout3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.gridLayout3.setContentsMargins(11, 11, 11, 11)
        self.PrefCheckBox_RecordGui = Gui_PrefCheckBox(self.GroupBox7)
        self.PrefCheckBox_RecordGui.setObjectName(u"PrefCheckBox_RecordGui")
        self.PrefCheckBox_RecordGui.setChecked(True)
        self.PrefCheckBox_RecordGui.setProperty(u"prefEntry", u"RecordGui")
        self.PrefCheckBox_RecordGui.setProperty(u"prefPath", u"Macro")

        self.gridLayout3.addWidget(self.PrefCheckBox_RecordGui, 0, 0, 1, 1)

        self.PrefCheckBox_GuiAsComment = Gui_PrefCheckBox(self.GroupBox7)
        self.PrefCheckBox_GuiAsComment.setObjectName(u"PrefCheckBox_GuiAsComment")
        self.PrefCheckBox_GuiAsComment.setChecked(True)
        self.PrefCheckBox_GuiAsComment.setProperty(u"prefEntry", u"GuiAsComment")
        self.PrefCheckBox_GuiAsComment.setProperty(u"prefPath", u"Macro")

        self.gridLayout3.addWidget(self.PrefCheckBox_GuiAsComment, 1, 0, 1, 1)


        self.gridLayout1.addWidget(self.GroupBox7, 1, 0, 1, 1)

        self.groupBox4 = QGroupBox(self.GroupBox6)
        self.groupBox4.setObjectName(u"groupBox4")
        self.vboxLayout = QVBoxLayout(self.groupBox4)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(11, 11, 11, 11)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(11, 11, 11, 11)
        self.PConsoleCheckBox = Gui_PrefCheckBox(self.groupBox4)
        self.PConsoleCheckBox.setObjectName(u"PConsoleCheckBox")
        self.PConsoleCheckBox.setChecked(True)
        self.PConsoleCheckBox.setProperty(u"prefEntry", u"ScriptToPyConsole")
        self.PConsoleCheckBox.setProperty(u"prefPath", u"Macro")

        self.vboxLayout.addWidget(self.PConsoleCheckBox)

        self.FileLogCheckBox = Gui_PrefCheckBox(self.groupBox4)
        self.FileLogCheckBox.setObjectName(u"FileLogCheckBox")
        self.FileLogCheckBox.setProperty(u"prefEntry", u"ScriptToFile")
        self.FileLogCheckBox.setProperty(u"prefPath", u"Macro")

        self.vboxLayout.addWidget(self.FileLogCheckBox)

        self.MacroPath_2 = Gui_PrefFileChooser(self.groupBox4)
        self.MacroPath_2.setObjectName(u"MacroPath_2")
        self.MacroPath_2.setProperty(u"prefEntry", u"ScriptFile")
        self.MacroPath_2.setProperty(u"prefPath", u"Macro")

        self.vboxLayout.addWidget(self.MacroPath_2)


        self.gridLayout1.addWidget(self.groupBox4, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.GroupBox6, 1, 0, 1, 1)

        self.recentmacrosgroupBox = QGroupBox(Gui__Dialog__DlgSettingsMacro)
        self.recentmacrosgroupBox.setObjectName(u"recentmacrosgroupBox")
        self.recentmacrosgridLayout = QGridLayout(self.recentmacrosgroupBox)
        self.recentmacrosgridLayout.setSpacing(6)
        self.recentmacrosgridLayout.setContentsMargins(11, 11, 11, 11)
        self.recentmacrosgridLayout.setObjectName(u"recentmacrosgridLayout")
        self.recentMacroListLabel = QLabel(self.recentmacrosgroupBox)
        self.recentMacroListLabel.setObjectName(u"recentMacroListLabel")

        self.recentmacrosgridLayout.addWidget(self.recentMacroListLabel, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.recentmacrosgridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.RecentMacros = Gui_PrefSpinBox(self.recentmacrosgroupBox)
        self.RecentMacros.setObjectName(u"RecentMacros")
        self.RecentMacros.setValue(12)
        self.RecentMacros.setProperty(u"prefEntry", u"RecentMacros")
        self.RecentMacros.setProperty(u"prefPath", u"RecentMacros")

        self.recentmacrosgridLayout.addWidget(self.RecentMacros, 0, 5, 1, 1)

        self.recentMacroListShortcutCountLabel = QLabel(self.recentmacrosgroupBox)
        self.recentMacroListShortcutCountLabel.setObjectName(u"recentMacroListShortcutCountLabel")

        self.recentmacrosgridLayout.addWidget(self.recentMacroListShortcutCountLabel, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.recentmacrosgridLayout.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.ShortcutCount = Gui_PrefSpinBox(self.recentmacrosgroupBox)
        self.ShortcutCount.setObjectName(u"ShortcutCount")
        self.ShortcutCount.setValue(3)
        self.ShortcutCount.setProperty(u"prefEntry", u"ShortcutCount")
        self.ShortcutCount.setProperty(u"prefPath", u"RecentMacros")

        self.recentmacrosgridLayout.addWidget(self.ShortcutCount, 1, 5, 1, 1)

        self.ShorcutModifiersLabel = QLabel(self.recentmacrosgroupBox)
        self.ShorcutModifiersLabel.setObjectName(u"ShorcutModifiersLabel")

        self.recentmacrosgridLayout.addWidget(self.ShorcutModifiersLabel, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.recentmacrosgridLayout.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.ShortcutModifiers = Gui_ModifierLineEdit(self.recentmacrosgroupBox)
        self.ShortcutModifiers.setObjectName(u"ShortcutModifiers")

        self.recentmacrosgridLayout.addWidget(self.ShortcutModifiers, 2, 5, 1, 3)


        self.gridLayout_2.addWidget(self.recentmacrosgroupBox, 2, 0, 1, 1)

        self.spacerItem = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.spacerItem, 3, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgSettingsMacro)
        self.PrefCheckBox_RecordGui.toggled.connect(self.PrefCheckBox_GuiAsComment.setEnabled)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsMacro)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsMacro):
        Gui__Dialog__DlgSettingsMacro.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Macro", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"General macro settings", None))
#if QT_CONFIG(tooltip)
        self.PrefCheckBox_LocalEnv.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Variables defined by macros are created as local variables", None))
#endif // QT_CONFIG(tooltip)
        self.PrefCheckBox_LocalEnv.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Run macros in local environment", None))
        self.GroupBox6.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Macro recording settings", None))
        self.GroupBox8.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Macro path", None))
#if QT_CONFIG(tooltip)
        self.MacroPath.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"The directory in which the application will search for macros", None))
#endif // QT_CONFIG(tooltip)
        self.GroupBox7.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Gui commands", None))
#if QT_CONFIG(tooltip)
        self.PrefCheckBox_RecordGui.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Recorded macros will also contain user interface commands", None))
#endif // QT_CONFIG(tooltip)
        self.PrefCheckBox_RecordGui.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Record GUI commands", None))
#if QT_CONFIG(tooltip)
        self.PrefCheckBox_GuiAsComment.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Recorded macros will also contain user interface commands as comments", None))
#endif // QT_CONFIG(tooltip)
        self.PrefCheckBox_GuiAsComment.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Record as comment", None))
        self.groupBox4.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Logging Commands", None))
#if QT_CONFIG(tooltip)
        self.PConsoleCheckBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Commands executed by macro scripts are shown in Python console", None))
#endif // QT_CONFIG(tooltip)
        self.PConsoleCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Show script commands in Python console", None))
        self.FileLogCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Log all commands issued by menus to file:", None))
        self.MacroPath_2.setProperty(u"fileName", QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"FullScript.FCScript", None))
        self.recentmacrosgroupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Recent macros menu", None))
        self.recentMacroListLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Size of recent macro list", None))
#if QT_CONFIG(tooltip)
        self.RecentMacros.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"How many macros should be listed in recent macros list", None))
#endif // QT_CONFIG(tooltip)
        self.recentMacroListShortcutCountLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Keyboard shortcut count", None))
#if QT_CONFIG(tooltip)
        self.ShortcutCount.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"How many recent macros should have shortcuts", None))
#endif // QT_CONFIG(tooltip)
        self.ShorcutModifiersLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Keyboard Modifiers", None))
#if QT_CONFIG(tooltip)
        self.ShortcutModifiers.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsMacro", u"Keyboard modifiers, default = Ctrl+Shift+", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

