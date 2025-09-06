# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsGeneral.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsGeneral(object):
    def setupUi(self, Gui__Dialog__DlgSettingsGeneral):
        if not Gui__Dialog__DlgSettingsGeneral.objectName():
            Gui__Dialog__DlgSettingsGeneral.setObjectName(u"Gui__Dialog__DlgSettingsGeneral")
        Gui__Dialog__DlgSettingsGeneral.resize(660, 930)
        self.verticalLayout = QVBoxLayout(Gui__Dialog__DlgSettingsGeneral)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.GroupBox7 = QGroupBox(Gui__Dialog__DlgSettingsGeneral)
        self.GroupBox7.setObjectName(u"GroupBox7")
        self.gridLayout = QGridLayout(self.GroupBox7)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.TextLabel1_4 = QLabel(self.GroupBox7)
        self.TextLabel1_4.setObjectName(u"TextLabel1_4")

        self.gridLayout.addWidget(self.TextLabel1_4, 0, 0, 1, 1)

        self.Languages = QComboBox(self.GroupBox7)
        self.Languages.setObjectName(u"Languages")

        self.gridLayout.addWidget(self.Languages, 0, 1, 1, 1)

        self.unitSystemLabel = QLabel(self.GroupBox7)
        self.unitSystemLabel.setObjectName(u"unitSystemLabel")

        self.gridLayout.addWidget(self.unitSystemLabel, 1, 0, 1, 1)

        self.comboBox_UnitSystem = QComboBox(self.GroupBox7)
        self.comboBox_UnitSystem.setObjectName(u"comboBox_UnitSystem")

        self.gridLayout.addWidget(self.comboBox_UnitSystem, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.decimalsLabel = QLabel(self.GroupBox7)
        self.decimalsLabel.setObjectName(u"decimalsLabel")

        self.horizontalLayout_3.addWidget(self.decimalsLabel)

        self.spinBoxDecimals = QSpinBox(self.GroupBox7)
        self.spinBoxDecimals.setObjectName(u"spinBoxDecimals")
        self.spinBoxDecimals.setMinimum(1)
        self.spinBoxDecimals.setMaximum(12)

        self.horizontalLayout_3.addWidget(self.spinBoxDecimals)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)

        self.checkBox_projectUnitSystemIgnore = QCheckBox(self.GroupBox7)
        self.checkBox_projectUnitSystemIgnore.setObjectName(u"checkBox_projectUnitSystemIgnore")

        self.gridLayout.addWidget(self.checkBox_projectUnitSystemIgnore, 2, 0, 1, 3)

        self.fractionalInchLabel = QLabel(self.GroupBox7)
        self.fractionalInchLabel.setObjectName(u"fractionalInchLabel")

        self.gridLayout.addWidget(self.fractionalInchLabel, 3, 0, 1, 1)

        self.comboBox_FracInch = QComboBox(self.GroupBox7)
        self.comboBox_FracInch.addItem(u"1/2\"")
        self.comboBox_FracInch.addItem(u"1/4\"")
        self.comboBox_FracInch.addItem(u"1/8\"")
        self.comboBox_FracInch.addItem(u"1/16\"")
        self.comboBox_FracInch.addItem(u"1/32\"")
        self.comboBox_FracInch.addItem(u"1/64\"")
        self.comboBox_FracInch.addItem(u"1/128\"")
        self.comboBox_FracInch.setObjectName(u"comboBox_FracInch")

        self.gridLayout.addWidget(self.comboBox_FracInch, 3, 1, 1, 1)

        self.TextLabel1_5 = QLabel(self.GroupBox7)
        self.TextLabel1_5.setObjectName(u"TextLabel1_5")

        self.gridLayout.addWidget(self.TextLabel1_5, 4, 0, 1, 1)

        self.UseLocaleFormatting = Gui_PrefComboBox(self.GroupBox7)
        self.UseLocaleFormatting.setObjectName(u"UseLocaleFormatting")
        self.UseLocaleFormatting.setProperty(u"prefEntry", u"UseLocaleFormatting")
        self.UseLocaleFormatting.setProperty(u"prefPath", u"General")

        self.gridLayout.addWidget(self.UseLocaleFormatting, 4, 1, 1, 1)

        self.SubstituteDecimal = Gui_PrefCheckBox(self.GroupBox7)
        self.SubstituteDecimal.setObjectName(u"SubstituteDecimal")
        self.SubstituteDecimal.setProperty(u"prefEntry", u"SubstituteDecimalSeparator")
        self.SubstituteDecimal.setProperty(u"prefPath", u"General")

        self.gridLayout.addWidget(self.SubstituteDecimal, 4, 2, 1, 1)


        self.verticalLayout.addWidget(self.GroupBox7)

        self.GroupBox3 = QGroupBox(Gui__Dialog__DlgSettingsGeneral)
        self.GroupBox3.setObjectName(u"GroupBox3")
        self.gridLayout1 = QGridLayout(self.GroupBox3)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.themesLabel = QLabel(self.GroupBox3)
        self.themesLabel.setObjectName(u"themesLabel")

        self.gridLayout1.addWidget(self.themesLabel, 0, 0, 1, 1)

        self.themesCombobox = QComboBox(self.GroupBox3)
        self.themesCombobox.setObjectName(u"themesCombobox")

        self.gridLayout1.addWidget(self.themesCombobox, 0, 1, 1, 1)

        self.moreThemesLabel = QLabel(self.GroupBox3)
        self.moreThemesLabel.setObjectName(u"moreThemesLabel")
        font = QFont()
        font.setPointSize(8)
        self.moreThemesLabel.setFont(font)
        self.moreThemesLabel.setTextFormat(Qt.RichText)

        self.gridLayout1.addWidget(self.moreThemesLabel, 1, 0, 1, 2)

        self.iconSizeLabel = QLabel(self.GroupBox3)
        self.iconSizeLabel.setObjectName(u"iconSizeLabel")

        self.gridLayout1.addWidget(self.iconSizeLabel, 2, 0, 1, 1)

        self.toolbarIconSize = QComboBox(self.GroupBox3)
        self.toolbarIconSize.setObjectName(u"toolbarIconSize")

        self.gridLayout1.addWidget(self.toolbarIconSize, 2, 1, 1, 1)

        self.treeModeLabel = QLabel(self.GroupBox3)
        self.treeModeLabel.setObjectName(u"treeModeLabel")

        self.gridLayout1.addWidget(self.treeModeLabel, 3, 0, 1, 1)

        self.treeMode = QComboBox(self.GroupBox3)
        self.treeMode.setObjectName(u"treeMode")

        self.gridLayout1.addWidget(self.treeMode, 3, 1, 1, 1)

        self.recentFileListLabel = QLabel(self.GroupBox3)
        self.recentFileListLabel.setObjectName(u"recentFileListLabel")

        self.gridLayout1.addWidget(self.recentFileListLabel, 4, 0, 1, 1)

        self.RecentFiles = Gui_PrefSpinBox(self.GroupBox3)
        self.RecentFiles.setObjectName(u"RecentFiles")
        self.RecentFiles.setValue(4)
        self.RecentFiles.setProperty(u"prefEntry", u"RecentFiles")
        self.RecentFiles.setProperty(u"prefPath", u"RecentFiles")

        self.gridLayout1.addWidget(self.RecentFiles, 4, 1, 1, 1)

        self.tiledBackground = QCheckBox(self.GroupBox3)
        self.tiledBackground.setObjectName(u"tiledBackground")

        self.gridLayout1.addWidget(self.tiledBackground, 5, 0, 1, 1)

        self.EnableCursorBlinking = Gui_PrefCheckBox(self.GroupBox3)
        self.EnableCursorBlinking.setObjectName(u"EnableCursorBlinking")
        self.EnableCursorBlinking.setChecked(True)
        self.EnableCursorBlinking.setProperty(u"prefEntry", u"EnableCursorBlinking")
        self.EnableCursorBlinking.setProperty(u"prefPath", u"General")

        self.gridLayout1.addWidget(self.EnableCursorBlinking, 5, 1, 1, 1)

        self.SplashScreen = Gui_PrefCheckBox(self.GroupBox3)
        self.SplashScreen.setObjectName(u"SplashScreen")
        self.SplashScreen.setChecked(True)
        self.SplashScreen.setProperty(u"prefEntry", u"ShowSplasher")
        self.SplashScreen.setProperty(u"prefPath", u"General")

        self.gridLayout1.addWidget(self.SplashScreen, 6, 0, 1, 1)

        self.ActivateOverlay = Gui_PrefCheckBox(self.GroupBox3)
        self.ActivateOverlay.setObjectName(u"ActivateOverlay")
        self.ActivateOverlay.setChecked(True)
        self.ActivateOverlay.setProperty(u"prefEntry", u"ActivateOverlay")
        self.ActivateOverlay.setProperty(u"prefPath", u"DockWindows")

        self.gridLayout1.addWidget(self.ActivateOverlay, 6, 1, 1, 1)


        self.verticalLayout.addWidget(self.GroupBox3)

        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsGeneral)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.PreferencePacks = QTableWidget(self.groupBox)
        if (self.PreferencePacks.columnCount() < 3):
            self.PreferencePacks.setColumnCount(3)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.PreferencePacks.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.PreferencePacks.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.PreferencePacks.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.PreferencePacks.setObjectName(u"PreferencePacks")
        self.PreferencePacks.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.PreferencePacks.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.PreferencePacks.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.PreferencePacks.setProperty(u"showDropIndicator", False)
        self.PreferencePacks.setDragDropOverwriteMode(False)
        self.PreferencePacks.setSelectionMode(QAbstractItemView.NoSelection)
        self.PreferencePacks.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.PreferencePacks.setShowGrid(False)
        self.PreferencePacks.setSortingEnabled(True)
        self.PreferencePacks.setWordWrap(False)
        self.PreferencePacks.setCornerButtonEnabled(False)
        self.PreferencePacks.horizontalHeader().setVisible(True)
        self.PreferencePacks.horizontalHeader().setCascadingSectionResizes(True)
        self.PreferencePacks.horizontalHeader().setMinimumSectionSize(30)
        self.PreferencePacks.horizontalHeader().setDefaultSectionSize(100)
        self.PreferencePacks.horizontalHeader().setStretchLastSection(True)
        self.PreferencePacks.verticalHeader().setVisible(False)
        self.PreferencePacks.verticalHeader().setMinimumSectionSize(16)
        self.PreferencePacks.verticalHeader().setDefaultSectionSize(24)

        self.verticalLayout_3.addWidget(self.PreferencePacks)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.ImportConfig = QPushButton(self.groupBox)
        self.ImportConfig.setObjectName(u"ImportConfig")

        self.horizontalLayout_2.addWidget(self.ImportConfig)

        self.SaveNewPreferencePack = QPushButton(self.groupBox)
        self.SaveNewPreferencePack.setObjectName(u"SaveNewPreferencePack")

        self.horizontalLayout_2.addWidget(self.SaveNewPreferencePack)

        self.ManagePreferencePacks = QPushButton(self.groupBox)
        self.ManagePreferencePacks.setObjectName(u"ManagePreferencePacks")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ManagePreferencePacks.sizePolicy().hasHeightForWidth())
        self.ManagePreferencePacks.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.ManagePreferencePacks)

        self.RevertToSavedConfig = QPushButton(self.groupBox)
        self.RevertToSavedConfig.setObjectName(u"RevertToSavedConfig")

        self.horizontalLayout_2.addWidget(self.RevertToSavedConfig)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.groupBox)

        QWidget.setTabOrder(self.Languages, self.RecentFiles)
        QWidget.setTabOrder(self.RecentFiles, self.EnableCursorBlinking)
        QWidget.setTabOrder(self.EnableCursorBlinking, self.SplashScreen)

        self.retranslateUi(Gui__Dialog__DlgSettingsGeneral)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsGeneral)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsGeneral):
        Gui__Dialog__DlgSettingsGeneral.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"General", None))
        self.GroupBox7.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Language and Number Format", None))
        self.TextLabel1_4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Language", None))
#if QT_CONFIG(tooltip)
        self.Languages.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Language of the application's user interface", None))
#endif // QT_CONFIG(tooltip)
        self.unitSystemLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Default unit system", None))
#if QT_CONFIG(tooltip)
        self.comboBox_UnitSystem.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Unit system for all parts of the application. Can be overridden by specifying a document unit system.", None))
#endif // QT_CONFIG(tooltip)
        self.decimalsLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Number of decimals", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDecimals.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Number of decimals that should be shown for numbers and dimensions", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_projectUnitSystemIgnore.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Ignores document unit systems", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_projectUnitSystemIgnore.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Ignore project unit system and use default", None))
        self.fractionalInchLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Minimum fractional inch", None))

#if QT_CONFIG(tooltip)
        self.comboBox_FracInch.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Minimum fractional inch to be displayed", None))
#endif // QT_CONFIG(tooltip)
        self.TextLabel1_5.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Number format", None))
#if QT_CONFIG(tooltip)
        self.SubstituteDecimal.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Substitutes numerical keypad decimal separator with locale separator, except\n"
"in the Python console and the macro editor where a\n"
"dot/period will always be printed", None))
#endif // QT_CONFIG(tooltip)
        self.SubstituteDecimal.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Substitute decimal separator", None))
        self.GroupBox3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Application", None))
        self.themesLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Theme", None))
#if QT_CONFIG(tooltip)
        self.themesCombobox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Customize the appearance of the user interface", None))
#endif // QT_CONFIG(tooltip)
        self.moreThemesLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Looking for more themes? You can obtain them using the <a href=\"freecad:Std_AddonMgr\">Addon Manager</a>.", None))
        self.iconSizeLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Size of toolbar icons", None))
#if QT_CONFIG(tooltip)
        self.toolbarIconSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Icon size in the toolbar", None))
#endif // QT_CONFIG(tooltip)
        self.treeModeLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Tree View and Property View mode", None))
#if QT_CONFIG(tooltip)
        self.treeMode.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Customize how the tree view is shown in the panel (restart required).\n"
"\n"
"'Combined': combine tree and property view into one panel.\n"
"'Independent': split tree and property view into separate panels.", None))
#endif // QT_CONFIG(tooltip)
        self.recentFileListLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Size of recent file list", None))
#if QT_CONFIG(tooltip)
        self.RecentFiles.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"How many files should be listed in recent files list", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tiledBackground.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Background of the main window (when no document is opened) will consist of tiles of an image.", None))
#endif // QT_CONFIG(tooltip)
        self.tiledBackground.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Enable tiled background", None))
#if QT_CONFIG(tooltip)
        self.EnableCursorBlinking.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"The text cursor will be blinking", None))
#endif // QT_CONFIG(tooltip)
        self.EnableCursorBlinking.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Enable cursor blinking", None))
#if QT_CONFIG(tooltip)
        self.SplashScreen.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"A splash screen is a small loading window that is shown\n"
"when FreeCAD is launching. If this option is checked, FreeCAD will\n"
"display the splash screen.", None))
#endif // QT_CONFIG(tooltip)
        self.SplashScreen.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Enable splash screen at start-up", None))
#if QT_CONFIG(tooltip)
        self.ActivateOverlay.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Activate overlay handling of docked panels", None))
#endif // QT_CONFIG(tooltip)
        self.ActivateOverlay.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Activate overlay panels", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Preference Packs", None))
        ___qtablewidgetitem = self.PreferencePacks.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Name", None));
        ___qtablewidgetitem1 = self.PreferencePacks.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Type", None));
        ___qtablewidgetitem2 = self.PreferencePacks.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Load", None));
        self.ImportConfig.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Import Configuration", None))
        self.SaveNewPreferencePack.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Save as New", None))
        self.ManagePreferencePacks.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Manage", None))
        self.RevertToSavedConfig.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsGeneral", u"Revert", None))
    # retranslateUi

