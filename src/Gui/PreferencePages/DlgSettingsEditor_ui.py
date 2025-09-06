# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsEditor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QSizePolicy, QSpacerItem,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Gui_Dialog_DlgSettingsEditor(object):
    def setupUi(self, Gui__Dialog__DlgSettingsEditor):
        if not Gui__Dialog__DlgSettingsEditor.objectName():
            Gui__Dialog__DlgSettingsEditor.setObjectName(u"Gui__Dialog__DlgSettingsEditor")
        Gui__Dialog__DlgSettingsEditor.resize(494, 553)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgSettingsEditor)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.GroupBox2 = QGroupBox(Gui__Dialog__DlgSettingsEditor)
        self.GroupBox2.setObjectName(u"GroupBox2")
        self.vboxLayout = QVBoxLayout(self.GroupBox2)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(11, 11, 11, 11)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(9, 9, 9, 9)
        self.EnableLineNumber = Gui_PrefCheckBox(self.GroupBox2)
        self.EnableLineNumber.setObjectName(u"EnableLineNumber")
        self.EnableLineNumber.setFocusPolicy(Qt.TabFocus)
        self.EnableLineNumber.setChecked(True)
        self.EnableLineNumber.setProperty(u"prefEntry", u"EnableLineNumber")
        self.EnableLineNumber.setProperty(u"prefPath", u"Editor")

        self.vboxLayout.addWidget(self.EnableLineNumber)

        self.EnableBlockCursor = Gui_PrefCheckBox(self.GroupBox2)
        self.EnableBlockCursor.setObjectName(u"EnableBlockCursor")
        self.EnableBlockCursor.setFocusPolicy(Qt.TabFocus)
        self.EnableBlockCursor.setChecked(False)
        self.EnableBlockCursor.setProperty(u"prefEntry", u"EnableBlockCursor")
        self.EnableBlockCursor.setProperty(u"prefPath", u"Editor")

        self.vboxLayout.addWidget(self.EnableBlockCursor)

        self.EnableFolding = Gui_PrefCheckBox(self.GroupBox2)
        self.EnableFolding.setObjectName(u"EnableFolding")
        self.EnableFolding.setChecked(True)
        self.EnableFolding.setProperty(u"prefEntry", u"EnableFolding")
        self.EnableFolding.setProperty(u"prefPath", u"Editor")

        self.vboxLayout.addWidget(self.EnableFolding)

        self.spacerItem = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)

        self.vboxLayout.addItem(self.spacerItem)


        self.gridLayout.addWidget(self.GroupBox2, 0, 0, 1, 1)

        self.groupBoxIndent = QGroupBox(Gui__Dialog__DlgSettingsEditor)
        self.groupBoxIndent.setObjectName(u"groupBoxIndent")
        self.gridLayout1 = QGridLayout(self.groupBoxIndent)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
        self.textLabel1 = QLabel(self.groupBoxIndent)
        self.textLabel1.setObjectName(u"textLabel1")

        self.gridLayout1.addWidget(self.textLabel1, 0, 0, 1, 1)

        self.tabSize = Gui_PrefSpinBox(self.groupBoxIndent)
        self.tabSize.setObjectName(u"tabSize")
        self.tabSize.setValue(4)
        self.tabSize.setProperty(u"prefEntry", u"TabSize")
        self.tabSize.setProperty(u"prefPath", u"Editor")

        self.gridLayout1.addWidget(self.tabSize, 0, 1, 1, 1)

        self.textLabel2 = QLabel(self.groupBoxIndent)
        self.textLabel2.setObjectName(u"textLabel2")

        self.gridLayout1.addWidget(self.textLabel2, 1, 0, 1, 1)

        self.indentSize = Gui_PrefSpinBox(self.groupBoxIndent)
        self.indentSize.setObjectName(u"indentSize")
        self.indentSize.setValue(4)
        self.indentSize.setProperty(u"prefEntry", u"IndentSize")
        self.indentSize.setProperty(u"prefPath", u"Editor")

        self.gridLayout1.addWidget(self.indentSize, 1, 1, 1, 1)

        self.radioTabs = Gui_PrefRadioButton(self.groupBoxIndent)
        self.radioTabs.setObjectName(u"radioTabs")
        self.radioTabs.setChecked(False)
        self.radioTabs.setProperty(u"prefEntry", u"Tabs")
        self.radioTabs.setProperty(u"prefPath", u"Editor")

        self.gridLayout1.addWidget(self.radioTabs, 2, 0, 1, 2)

        self.radioSpaces = Gui_PrefRadioButton(self.groupBoxIndent)
        self.radioSpaces.setObjectName(u"radioSpaces")
        self.radioSpaces.setProperty(u"prefEntry", u"Spaces")
        self.radioSpaces.setChecked(True)
        self.radioSpaces.setProperty(u"prefPath", u"Editor")

        self.gridLayout1.addWidget(self.radioSpaces, 3, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBoxIndent, 0, 1, 1, 1)

        self.GroupBox5 = QGroupBox(Gui__Dialog__DlgSettingsEditor)
        self.GroupBox5.setObjectName(u"GroupBox5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GroupBox5.sizePolicy().hasHeightForWidth())
        self.GroupBox5.setSizePolicy(sizePolicy)
        self.gridLayout2 = QGridLayout(self.GroupBox5)
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayout2.setContentsMargins(9, 9, 9, 9)
        self.displayItems = QTreeWidget(self.GroupBox5)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.displayItems.setHeaderItem(__qtreewidgetitem)
        self.displayItems.setObjectName(u"displayItems")
        self.displayItems.setRootIsDecorated(False)

        self.gridLayout2.addWidget(self.displayItems, 0, 0, 7, 1)

        self.TextLabel3 = QLabel(self.GroupBox5)
        self.TextLabel3.setObjectName(u"TextLabel3")

        self.gridLayout2.addWidget(self.TextLabel3, 0, 1, 1, 1)

        self.fontFamily = QComboBox(self.GroupBox5)
        self.fontFamily.setObjectName(u"fontFamily")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fontFamily.sizePolicy().hasHeightForWidth())
        self.fontFamily.setSizePolicy(sizePolicy1)

        self.gridLayout2.addWidget(self.fontFamily, 0, 2, 1, 1)

        self.TextLabel4 = QLabel(self.GroupBox5)
        self.TextLabel4.setObjectName(u"TextLabel4")

        self.gridLayout2.addWidget(self.TextLabel4, 1, 1, 1, 1)

        self.fontSize = Gui_PrefSpinBox(self.GroupBox5)
        self.fontSize.setObjectName(u"fontSize")
        sizePolicy1.setHeightForWidth(self.fontSize.sizePolicy().hasHeightForWidth())
        self.fontSize.setSizePolicy(sizePolicy1)
        self.fontSize.setSuffix(u" pt")
        self.fontSize.setMinimum(1)
        self.fontSize.setValue(10)
        self.fontSize.setProperty(u"prefEntry", u"FontSize")
        self.fontSize.setProperty(u"prefPath", u"Editor")

        self.gridLayout2.addWidget(self.fontSize, 1, 2, 1, 1)

        self.label_2 = QLabel(self.GroupBox5)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout2.addWidget(self.label_2, 2, 1, 1, 1)

        self.colorButton = Gui_ColorButton(self.GroupBox5)
        self.colorButton.setObjectName(u"colorButton")
        self.colorButton.setMinimumSize(QSize(140, 0))
        self.colorButton.setFocusPolicy(Qt.TabFocus)

        self.gridLayout2.addWidget(self.colorButton, 2, 2, 1, 1)

        self.label = QLabel(self.GroupBox5)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.gridLayout2.addWidget(self.label, 3, 1, 1, 1)

        self.textEdit1 = QTextEdit(self.GroupBox5)
        self.textEdit1.setObjectName(u"textEdit1")

        self.gridLayout2.addWidget(self.textEdit1, 4, 1, 3, 2)


        self.gridLayout.addWidget(self.GroupBox5, 1, 0, 1, 2)

        QWidget.setTabOrder(self.fontFamily, self.EnableLineNumber)
        QWidget.setTabOrder(self.EnableLineNumber, self.EnableBlockCursor)
        QWidget.setTabOrder(self.EnableBlockCursor, self.EnableFolding)
        QWidget.setTabOrder(self.EnableFolding, self.tabSize)
        QWidget.setTabOrder(self.tabSize, self.indentSize)

        self.retranslateUi(Gui__Dialog__DlgSettingsEditor)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsEditor)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsEditor):
        Gui__Dialog__DlgSettingsEditor.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Editor", None))
        self.GroupBox2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Options", None))
#if QT_CONFIG(tooltip)
        self.EnableLineNumber.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Code lines will be numbered", None))
#endif // QT_CONFIG(tooltip)
        self.EnableLineNumber.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Enable line numbers", None))
#if QT_CONFIG(tooltip)
        self.EnableBlockCursor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"The cursor shape will be a block", None))
#endif // QT_CONFIG(tooltip)
        self.EnableBlockCursor.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Enable block cursor", None))
        self.EnableFolding.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Enable folding", None))
        self.groupBoxIndent.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Indentation", None))
        self.textLabel1.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Tab size", None))
#if QT_CONFIG(tooltip)
        self.tabSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Tabulator raster (how many spaces)", None))
#endif // QT_CONFIG(tooltip)
        self.tabSize.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u" spaces", u"Do not remove leading space"))
        self.textLabel2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Indent size", None))
#if QT_CONFIG(tooltip)
        self.indentSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"How many spaces will be inserted when pressing <Tab>", None))
#endif // QT_CONFIG(tooltip)
        self.indentSize.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u" spaces", u"Do not remove leading space"))
#if QT_CONFIG(tooltip)
        self.radioTabs.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Pressing <Tab> will insert a tabulator with defined tab size", None))
#endif // QT_CONFIG(tooltip)
        self.radioTabs.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Keep tabs", None))
#if QT_CONFIG(tooltip)
        self.radioSpaces.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Pressing <Tab> will insert amount of defined indent size", None))
#endif // QT_CONFIG(tooltip)
        self.radioSpaces.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Insert spaces", None))
        self.GroupBox5.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Display Items", None))
#if QT_CONFIG(tooltip)
        self.displayItems.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Color and font settings will be applied to selected type", None))
#endif // QT_CONFIG(tooltip)
        self.TextLabel3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Family", None))
#if QT_CONFIG(tooltip)
        self.fontFamily.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Font family to be used for selected code type", None))
#endif // QT_CONFIG(tooltip)
        self.TextLabel4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Size", None))
#if QT_CONFIG(tooltip)
        self.fontSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Font size to be used for selected code type", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Color", None))
        self.colorButton.setText("")
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsEditor", u"Preview", None))
    # retranslateUi

