# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsUI.ui'
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

class Ui_Gui_Dialog_DlgSettingsUI(object):
    def setupUi(self, Gui__Dialog__DlgSettingsUI):
        if not Gui__Dialog__DlgSettingsUI.objectName():
            Gui__Dialog__DlgSettingsUI.setObjectName(u"Gui__Dialog__DlgSettingsUI")
        Gui__Dialog__DlgSettingsUI.resize(405, 1065)
        self.verticalLayout = QVBoxLayout(Gui__Dialog__DlgSettingsUI)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsUI)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")

        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)

        self.ThemeAccentColor1 = Gui_PrefColorButton(self.groupBox)
        self.ThemeAccentColor1.setObjectName(u"ThemeAccentColor1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ThemeAccentColor1.sizePolicy().hasHeightForWidth())
        self.ThemeAccentColor1.setSizePolicy(sizePolicy)
        self.ThemeAccentColor1.setProperty(u"color", QColor(85, 123, 182))
        self.ThemeAccentColor1.setProperty(u"prefEntry", u"ThemeAccentColor1")
        self.ThemeAccentColor1.setProperty(u"prefPath", u"Themes")

        self.gridLayout.addWidget(self.ThemeAccentColor1, 0, 1, 1, 1)

        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")

        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)

        self.label3 = QLabel(self.groupBox)
        self.label3.setObjectName(u"label3")

        self.gridLayout.addWidget(self.label3, 2, 0, 1, 1)

        self.styleSheetLabel = QLabel(self.groupBox)
        self.styleSheetLabel.setObjectName(u"styleSheetLabel")

        self.gridLayout.addWidget(self.styleSheetLabel, 3, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.ThemeAccentColor2 = Gui_PrefColorButton(self.groupBox)
        self.ThemeAccentColor2.setObjectName(u"ThemeAccentColor2")
        sizePolicy.setHeightForWidth(self.ThemeAccentColor2.sizePolicy().hasHeightForWidth())
        self.ThemeAccentColor2.setSizePolicy(sizePolicy)
        self.ThemeAccentColor2.setProperty(u"color", QColor(85, 123, 182))
        self.ThemeAccentColor2.setProperty(u"prefEntry", u"ThemeAccentColor2")
        self.ThemeAccentColor2.setProperty(u"prefPath", u"Themes")

        self.gridLayout.addWidget(self.ThemeAccentColor2, 1, 1, 1, 1)

        self.ThemeAccentColor3 = Gui_PrefColorButton(self.groupBox)
        self.ThemeAccentColor3.setObjectName(u"ThemeAccentColor3")
        sizePolicy.setHeightForWidth(self.ThemeAccentColor3.sizePolicy().hasHeightForWidth())
        self.ThemeAccentColor3.setSizePolicy(sizePolicy)
        self.ThemeAccentColor3.setProperty(u"color", QColor(85, 123, 182))
        self.ThemeAccentColor3.setProperty(u"prefEntry", u"ThemeAccentColor3")
        self.ThemeAccentColor3.setProperty(u"prefPath", u"Themes")

        self.gridLayout.addWidget(self.ThemeAccentColor3, 2, 1, 1, 1)

        self.StyleSheets = Gui_PrefComboBox(self.groupBox)
        self.StyleSheets.setObjectName(u"StyleSheets")
        self.StyleSheets.setProperty(u"prefPath", u"MainWindow")
        self.StyleSheets.setProperty(u"prefEntry", u"StyleSheet")
        self.StyleSheets.setProperty(u"prefType", u"")

        self.gridLayout.addWidget(self.StyleSheets, 3, 1, 1, 1)

        self.OverlayStyleSheets = Gui_PrefComboBox(self.groupBox)
        self.OverlayStyleSheets.setObjectName(u"OverlayStyleSheets")
        self.OverlayStyleSheets.setProperty(u"prefPath", u"MainWindow")
        self.OverlayStyleSheets.setProperty(u"prefEntry", u"OverlayActiveStyleSheet")
        self.OverlayStyleSheets.setProperty(u"prefType", u"")

        self.gridLayout.addWidget(self.OverlayStyleSheets, 4, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsUI)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout1 = QGridLayout(self.groupBox_2)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.hideInternalNamesCheckBox = Gui_PrefCheckBox(self.groupBox_2)
        self.hideInternalNamesCheckBox.setObjectName(u"hideInternalNamesCheckBox")
        self.hideInternalNamesCheckBox.setChecked(True)
        self.hideInternalNamesCheckBox.setProperty(u"prefEntry", u"HideInternalNames")
        self.hideInternalNamesCheckBox.setProperty(u"prefPath", u"TreeView")

        self.gridLayout1.addWidget(self.hideInternalNamesCheckBox, 5, 0, 1, 2)

        self.iconSizeSpinBox = Gui_PrefSpinBox(self.groupBox_2)
        self.iconSizeSpinBox.setObjectName(u"iconSizeSpinBox")
        self.iconSizeSpinBox.setSingleStep(1)
        self.iconSizeSpinBox.setValue(16)
        self.iconSizeSpinBox.setProperty(u"prefPath", u"TreeView")
        self.iconSizeSpinBox.setProperty(u"prefEntry", u"IconSize")

        self.gridLayout1.addWidget(self.iconSizeSpinBox, 0, 1, 1, 1)

        self.rowSpacingLabel = QLabel(self.groupBox_2)
        self.rowSpacingLabel.setObjectName(u"rowSpacingLabel")

        self.gridLayout1.addWidget(self.rowSpacingLabel, 1, 0, 1, 1)

        self.resizableColumnsCheckBox = Gui_PrefCheckBox(self.groupBox_2)
        self.resizableColumnsCheckBox.setObjectName(u"resizableColumnsCheckBox")
        self.resizableColumnsCheckBox.setProperty(u"prefEntry", u"ResizableColumn")
        self.resizableColumnsCheckBox.setProperty(u"prefPath", u"TreeView")

        self.gridLayout1.addWidget(self.resizableColumnsCheckBox, 2, 0, 1, 2)

        self.iconSizeLabel = QLabel(self.groupBox_2)
        self.iconSizeLabel.setObjectName(u"iconSizeLabel")

        self.gridLayout1.addWidget(self.iconSizeLabel, 0, 0, 1, 1)

        self.rowSpacingSpinBox = Gui_PrefSpinBox(self.groupBox_2)
        self.rowSpacingSpinBox.setObjectName(u"rowSpacingSpinBox")
        self.rowSpacingSpinBox.setSingleStep(1)
        self.rowSpacingSpinBox.setValue(0)
        self.rowSpacingSpinBox.setProperty(u"prefPath", u"TreeView")
        self.rowSpacingSpinBox.setProperty(u"prefEntry", u"ItemSpacing")

        self.gridLayout1.addWidget(self.rowSpacingSpinBox, 1, 1, 1, 1)

        self.showVisibilityIconCheckBox = Gui_PrefCheckBox(self.groupBox_2)
        self.showVisibilityIconCheckBox.setObjectName(u"showVisibilityIconCheckBox")
        self.showVisibilityIconCheckBox.setChecked(True)
        self.showVisibilityIconCheckBox.setProperty(u"prefEntry", u"VisibilityIcon")
        self.showVisibilityIconCheckBox.setProperty(u"prefPath", u"TreeView")

        self.gridLayout1.addWidget(self.showVisibilityIconCheckBox, 3, 0, 1, 2)

        self.hideHeaderCheckBox = Gui_PrefCheckBox(self.groupBox_2)
        self.hideHeaderCheckBox.setObjectName(u"hideHeaderCheckBox")
        self.hideHeaderCheckBox.setChecked(True)
        self.hideHeaderCheckBox.setProperty(u"prefEntry", u"HideHeaderView")
        self.hideHeaderCheckBox.setProperty(u"prefPath", u"TreeView")

        self.gridLayout1.addWidget(self.hideHeaderCheckBox, 7, 0, 1, 2)

        self.hideTreeViewScrollBarCheckBox = Gui_PrefCheckBox(self.groupBox_2)
        self.hideTreeViewScrollBarCheckBox.setObjectName(u"hideTreeViewScrollBarCheckBox")
        self.hideTreeViewScrollBarCheckBox.setChecked(True)
        self.hideTreeViewScrollBarCheckBox.setProperty(u"prefEntry", u"HideScrollBar")
        self.hideTreeViewScrollBarCheckBox.setProperty(u"prefPath", u"TreeView")

        self.gridLayout1.addWidget(self.hideTreeViewScrollBarCheckBox, 6, 0, 1, 2)

        self.hideDescriptionCheckBox = Gui_PrefCheckBox(self.groupBox_2)
        self.hideDescriptionCheckBox.setObjectName(u"hideDescriptionCheckBox")
        self.hideDescriptionCheckBox.setChecked(True)
        self.hideDescriptionCheckBox.setProperty(u"prefEntry", u"HideColumn")
        self.hideDescriptionCheckBox.setProperty(u"prefPath", u"TreeView")

        self.gridLayout1.addWidget(self.hideDescriptionCheckBox, 4, 0, 1, 2)

        self.gridLayout1.setColumnStretch(0, 2)
        self.gridLayout1.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Gui__Dialog__DlgSettingsUI)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.hideTabBarCheckBox = Gui_PrefCheckBox(self.groupBox_3)
        self.hideTabBarCheckBox.setObjectName(u"hideTabBarCheckBox")
        self.hideTabBarCheckBox.setChecked(True)
        self.hideTabBarCheckBox.setProperty(u"prefEntry", u"DockOverlayHideTabBar")
        self.hideTabBarCheckBox.setProperty(u"prefPath", u"View")

        self.gridLayout_2.addWidget(self.hideTabBarCheckBox, 0, 0, 1, 1)

        self.hintShowTabBarCheckBox = Gui_PrefCheckBox(self.groupBox_3)
        self.hintShowTabBarCheckBox.setObjectName(u"hintShowTabBarCheckBox")
        self.hintShowTabBarCheckBox.setProperty(u"prefEntry", u"DockOverlayHintTabBar")
        self.hintShowTabBarCheckBox.setProperty(u"prefPath", u"View")

        self.gridLayout_2.addWidget(self.hintShowTabBarCheckBox, 1, 0, 1, 1)

        self.hidePropertyViewScrollBarCheckBox = Gui_PrefCheckBox(self.groupBox_3)
        self.hidePropertyViewScrollBarCheckBox.setObjectName(u"hidePropertyViewScrollBarCheckBox")
        self.hidePropertyViewScrollBarCheckBox.setProperty(u"prefEntry", u"DockOverlayHidePropertyViewScrollBar")
        self.hidePropertyViewScrollBarCheckBox.setProperty(u"prefPath", u"View")

        self.gridLayout_2.addWidget(self.hidePropertyViewScrollBarCheckBox, 2, 0, 1, 1)

        self.overlayAutoHideCheckBox = Gui_PrefCheckBox(self.groupBox_3)
        self.overlayAutoHideCheckBox.setObjectName(u"overlayAutoHideCheckBox")
        self.overlayAutoHideCheckBox.setChecked(True)
        self.overlayAutoHideCheckBox.setProperty(u"prefEntry", u"DockOverlayAutoView")
        self.overlayAutoHideCheckBox.setProperty(u"prefPath", u"View")

        self.gridLayout_2.addWidget(self.overlayAutoHideCheckBox, 3, 0, 1, 1)

        self.mouseClickPassThroughCheckBox = Gui_PrefCheckBox(self.groupBox_3)
        self.mouseClickPassThroughCheckBox.setObjectName(u"mouseClickPassThroughCheckBox")
        self.mouseClickPassThroughCheckBox.setChecked(True)
        self.mouseClickPassThroughCheckBox.setProperty(u"prefEntry", u"DockOverlayAutoMouseThrough")
        self.mouseClickPassThroughCheckBox.setProperty(u"prefPath", u"View")

        self.gridLayout_2.addWidget(self.mouseClickPassThroughCheckBox, 4, 0, 1, 1)

        self.mouseWheelPassThroughCheckBox = Gui_PrefCheckBox(self.groupBox_3)
        self.mouseWheelPassThroughCheckBox.setObjectName(u"mouseWheelPassThroughCheckBox")
        self.mouseWheelPassThroughCheckBox.setChecked(True)
        self.mouseWheelPassThroughCheckBox.setProperty(u"prefEntry", u"DockOverlayWheelPassThrough")
        self.mouseWheelPassThroughCheckBox.setProperty(u"prefPath", u"View")

        self.gridLayout_2.addWidget(self.mouseWheelPassThroughCheckBox, 5, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.spacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.spacer_3)

#if QT_CONFIG(shortcut)
        self.label1.setBuddy(self.ThemeAccentColor1)
        self.label2.setBuddy(self.ThemeAccentColor2)
        self.label3.setBuddy(self.ThemeAccentColor3)
        self.styleSheetLabel.setBuddy(self.StyleSheets)
        self.label_2.setBuddy(self.OverlayStyleSheets)
        self.rowSpacingLabel.setBuddy(self.rowSpacingSpinBox)
        self.iconSizeLabel.setBuddy(self.iconSizeSpinBox)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.ThemeAccentColor1, self.ThemeAccentColor2)
        QWidget.setTabOrder(self.ThemeAccentColor2, self.ThemeAccentColor3)
        QWidget.setTabOrder(self.ThemeAccentColor3, self.StyleSheets)
        QWidget.setTabOrder(self.StyleSheets, self.OverlayStyleSheets)
        QWidget.setTabOrder(self.OverlayStyleSheets, self.iconSizeSpinBox)
        QWidget.setTabOrder(self.iconSizeSpinBox, self.rowSpacingSpinBox)
        QWidget.setTabOrder(self.rowSpacingSpinBox, self.resizableColumnsCheckBox)
        QWidget.setTabOrder(self.resizableColumnsCheckBox, self.showVisibilityIconCheckBox)
        QWidget.setTabOrder(self.showVisibilityIconCheckBox, self.hideDescriptionCheckBox)
        QWidget.setTabOrder(self.hideDescriptionCheckBox, self.hideInternalNamesCheckBox)
        QWidget.setTabOrder(self.hideInternalNamesCheckBox, self.hideTreeViewScrollBarCheckBox)
        QWidget.setTabOrder(self.hideTreeViewScrollBarCheckBox, self.hideHeaderCheckBox)
        QWidget.setTabOrder(self.hideHeaderCheckBox, self.hideTabBarCheckBox)
        QWidget.setTabOrder(self.hideTabBarCheckBox, self.hintShowTabBarCheckBox)
        QWidget.setTabOrder(self.hintShowTabBarCheckBox, self.hidePropertyViewScrollBarCheckBox)
        QWidget.setTabOrder(self.hidePropertyViewScrollBarCheckBox, self.overlayAutoHideCheckBox)
        QWidget.setTabOrder(self.overlayAutoHideCheckBox, self.mouseClickPassThroughCheckBox)
        QWidget.setTabOrder(self.mouseClickPassThroughCheckBox, self.mouseWheelPassThroughCheckBox)

        self.retranslateUi(Gui__Dialog__DlgSettingsUI)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsUI)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsUI):
        Gui__Dialog__DlgSettingsUI.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"UI", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Theme customization", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"This section lets you customize your current theme. The offered settings are optional for theme developers so they may or may not have an effect in your current theme.", None))
        self.label1.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Accent color 1", None))
#if QT_CONFIG(tooltip)
        self.ThemeAccentColor1.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"This color might be used by your theme to let you customize it.", None))
#endif // QT_CONFIG(tooltip)
        self.label2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Accent color 2", None))
        self.label3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Accent color 3", None))
        self.styleSheetLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Style sheet (advanced):", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Overlay style sheet:", None))
#if QT_CONFIG(tooltip)
        self.ThemeAccentColor2.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"This color might be used by your theme to let you customize it.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ThemeAccentColor3.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"This color might be used by your theme to let you customize it.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.StyleSheets.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Style sheet how user interface will look like", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Tree view", None))
#if QT_CONFIG(tooltip)
        self.hideInternalNamesCheckBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Hide extra tree view column - Internal Names.", None))
#endif // QT_CONFIG(tooltip)
        self.hideInternalNamesCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Hide Internal Names", None))
#if QT_CONFIG(tooltip)
        self.iconSizeSpinBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Icon size override, set to 0 for the default value.", None))
#endif // QT_CONFIG(tooltip)
        self.rowSpacingLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Additional row spacing", None))
#if QT_CONFIG(tooltip)
        self.resizableColumnsCheckBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Allow tree view columns to be manually resized.", None))
#endif // QT_CONFIG(tooltip)
        self.resizableColumnsCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Resizable columns", None))
        self.iconSizeLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Icon size", None))
#if QT_CONFIG(tooltip)
        self.rowSpacingSpinBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Additional spacing for tree view rows. Bigger values will increase row item heights.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.showVisibilityIconCheckBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"If enabled, show an eye icon before the tree view items, showing their visibility status. When clicked the visibility is toggled.", None))
#endif // QT_CONFIG(tooltip)
        self.showVisibilityIconCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Show visibility icon", None))
#if QT_CONFIG(tooltip)
        self.hideHeaderCheckBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Hide header with column names from the tree view.", None))
#endif // QT_CONFIG(tooltip)
        self.hideHeaderCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Hide header", None))
#if QT_CONFIG(tooltip)
        self.hideTreeViewScrollBarCheckBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Hide scroll bar from the tree view, scrolling will still be possible using mouse wheel.", None))
#endif // QT_CONFIG(tooltip)
        self.hideTreeViewScrollBarCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Hide scroll bar", None))
#if QT_CONFIG(tooltip)
        self.hideDescriptionCheckBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Hide column with object description in tree view.", None))
#endif // QT_CONFIG(tooltip)
        self.hideDescriptionCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Hide description", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Overlay", None))
#if QT_CONFIG(tooltip)
        self.hideTabBarCheckBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Hide tab bar in dock overlay", None))
#endif // QT_CONFIG(tooltip)
        self.hideTabBarCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Hide tab bar", None))
#if QT_CONFIG(tooltip)
        self.hintShowTabBarCheckBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Show tab bar on mouse over when auto hide", None))
#endif // QT_CONFIG(tooltip)
        self.hintShowTabBarCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Hint show tab bar", None))
#if QT_CONFIG(tooltip)
        self.hidePropertyViewScrollBarCheckBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Hide property view scroll bar in dock overlay", None))
#endif // QT_CONFIG(tooltip)
        self.hidePropertyViewScrollBarCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Hide property view scroll bar", None))
#if QT_CONFIG(tooltip)
        self.overlayAutoHideCheckBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Automatically hide overlaid dock panels when in non 3D view (like TechDraw or Spreadsheet).", None))
#endif // QT_CONFIG(tooltip)
        self.overlayAutoHideCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Auto hide in non 3D view", None))
#if QT_CONFIG(tooltip)
        self.mouseClickPassThroughCheckBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Auto mouse click through transparent part of dock overlay.", None))
#endif // QT_CONFIG(tooltip)
        self.mouseClickPassThroughCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Auto mouse pass through", None))
#if QT_CONFIG(tooltip)
        self.mouseWheelPassThroughCheckBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Auto pass through mouse wheel event on transparent dock overlay.", None))
#endif // QT_CONFIG(tooltip)
        self.mouseWheelPassThroughCheckBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsUI", u"Auto mouse wheel pass through", None))
    # retranslateUi

