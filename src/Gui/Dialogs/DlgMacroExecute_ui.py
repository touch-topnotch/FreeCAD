# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgMacroExecute.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgMacroExecute(object):
    def setupUi(self, Gui__Dialog__DlgMacroExecute):
        if not Gui__Dialog__DlgMacroExecute.objectName():
            Gui__Dialog__DlgMacroExecute.setObjectName(u"Gui__Dialog__DlgMacroExecute")
        Gui__Dialog__DlgMacroExecute.resize(640, 480)
        Gui__Dialog__DlgMacroExecute.setModal(True)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgMacroExecute)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout1 = QGridLayout()
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.MacroNameGroup = QGroupBox(Gui__Dialog__DlgMacroExecute)
        self.MacroNameGroup.setObjectName(u"MacroNameGroup")
        self.gridLayout2 = QGridLayout(self.MacroNameGroup)
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayout2.setContentsMargins(9, 9, 9, 9)
        self.LineEditMacroName = QLineEdit(self.MacroNameGroup)
        self.LineEditMacroName.setObjectName(u"LineEditMacroName")
        self.LineEditMacroName.setEnabled(False)

        self.gridLayout2.addWidget(self.LineEditMacroName, 0, 0, 1, 1)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.label = QLabel(self.MacroNameGroup)
        self.label.setObjectName(u"label")

        self.hboxLayout.addWidget(self.label)

        self.LineEditFind = QLineEdit(self.MacroNameGroup)
        self.LineEditFind.setObjectName(u"LineEditFind")

        self.hboxLayout.addWidget(self.LineEditFind)

        self.label1 = QLabel(self.MacroNameGroup)
        self.label1.setObjectName(u"label1")

        self.hboxLayout.addWidget(self.label1)

        self.LineEditFindInFiles = QLineEdit(self.MacroNameGroup)
        self.LineEditFindInFiles.setObjectName(u"LineEditFindInFiles")

        self.hboxLayout.addWidget(self.LineEditFindInFiles)


        self.gridLayout2.addLayout(self.hboxLayout, 1, 0, 1, 1)

        self.tabMacroWidget = QTabWidget(self.MacroNameGroup)
        self.tabMacroWidget.setObjectName(u"tabMacroWidget")
        self.tabMacroWidget.setTabPosition(QTabWidget.North)
        self.userSpecificTab = QWidget()
        self.userSpecificTab.setObjectName(u"userSpecificTab")
        self.verticalLayout_2 = QVBoxLayout(self.userSpecificTab)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.userMacroListBox = QTreeWidget(self.userSpecificTab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.userMacroListBox.setHeaderItem(__qtreewidgetitem)
        self.userMacroListBox.setObjectName(u"userMacroListBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userMacroListBox.sizePolicy().hasHeightForWidth())
        self.userMacroListBox.setSizePolicy(sizePolicy)
        self.userMacroListBox.setRootIsDecorated(False)

        self.verticalLayout_2.addWidget(self.userMacroListBox)

        self.tabMacroWidget.addTab(self.userSpecificTab, "")
        self.systemWideTag = QWidget()
        self.systemWideTag.setObjectName(u"systemWideTag")
        self.verticalLayout = QVBoxLayout(self.systemWideTag)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.systemMacroListBox = QTreeWidget(self.systemWideTag)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.systemMacroListBox.setHeaderItem(__qtreewidgetitem1)
        self.systemMacroListBox.setObjectName(u"systemMacroListBox")
        sizePolicy.setHeightForWidth(self.systemMacroListBox.sizePolicy().hasHeightForWidth())
        self.systemMacroListBox.setSizePolicy(sizePolicy)
        self.systemMacroListBox.setRootIsDecorated(False)

        self.verticalLayout.addWidget(self.systemMacroListBox)

        self.tabMacroWidget.addTab(self.systemWideTag, "")

        self.gridLayout2.addWidget(self.tabMacroWidget, 2, 0, 1, 1)


        self.gridLayout1.addWidget(self.MacroNameGroup, 0, 0, 1, 1)

        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.executeButton = QPushButton(Gui__Dialog__DlgMacroExecute)
        self.executeButton.setObjectName(u"executeButton")
        self.executeButton.setEnabled(False)

        self.vboxLayout.addWidget(self.executeButton)

        self.closeButton = QPushButton(Gui__Dialog__DlgMacroExecute)
        self.closeButton.setObjectName(u"closeButton")

        self.vboxLayout.addWidget(self.closeButton)

        self.spacerItem = QSpacerItem(77, 34, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.spacerItem)

        self.createButton = QPushButton(Gui__Dialog__DlgMacroExecute)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setEnabled(True)

        self.vboxLayout.addWidget(self.createButton)

        self.deleteButton = QPushButton(Gui__Dialog__DlgMacroExecute)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setEnabled(False)

        self.vboxLayout.addWidget(self.deleteButton)

        self.editButton = QPushButton(Gui__Dialog__DlgMacroExecute)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setEnabled(False)

        self.vboxLayout.addWidget(self.editButton)

        self.renameButton = QPushButton(Gui__Dialog__DlgMacroExecute)
        self.renameButton.setObjectName(u"renameButton")
        self.renameButton.setEnabled(False)

        self.vboxLayout.addWidget(self.renameButton)

        self.duplicateButton = QPushButton(Gui__Dialog__DlgMacroExecute)
        self.duplicateButton.setObjectName(u"duplicateButton")
        self.duplicateButton.setEnabled(False)

        self.vboxLayout.addWidget(self.duplicateButton)

        self.toolbarButton = QPushButton(Gui__Dialog__DlgMacroExecute)
        self.toolbarButton.setObjectName(u"toolbarButton")
        self.toolbarButton.setEnabled(False)

        self.vboxLayout.addWidget(self.toolbarButton)

        self.spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.spacerItem1)

        self.addonsButton = QPushButton(Gui__Dialog__DlgMacroExecute)
        self.addonsButton.setObjectName(u"addonsButton")
        self.addonsButton.setEnabled(True)

        self.vboxLayout.addWidget(self.addonsButton)


        self.gridLayout1.addLayout(self.vboxLayout, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout1, 0, 0, 1, 1)

        self.DestinationGroup = QGroupBox(Gui__Dialog__DlgMacroExecute)
        self.DestinationGroup.setObjectName(u"DestinationGroup")
        self.gridLayout3 = QGridLayout(self.DestinationGroup)
        self.gridLayout3.setSpacing(6)
        self.gridLayout3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.gridLayout3.setContentsMargins(9, 9, 9, 9)
        self.fileChooser = Gui_FileChooser(self.DestinationGroup)
        self.fileChooser.setObjectName(u"fileChooser")
        self.fileChooser.setFocusPolicy(Qt.StrongFocus)
        self.fileChooser.setMode(Gui.FileChooser.Mode.Directory)

        self.gridLayout3.addWidget(self.fileChooser, 0, 0, 1, 1)

        self.folderButton = QPushButton(self.DestinationGroup)
        self.folderButton.setObjectName(u"folderButton")
        self.folderButton.setEnabled(True)

        self.gridLayout3.addWidget(self.folderButton, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.DestinationGroup, 1, 0, 1, 1)

        QWidget.setTabOrder(self.LineEditMacroName, self.executeButton)
        QWidget.setTabOrder(self.executeButton, self.closeButton)
        QWidget.setTabOrder(self.closeButton, self.createButton)
        QWidget.setTabOrder(self.createButton, self.deleteButton)
        QWidget.setTabOrder(self.deleteButton, self.editButton)
        QWidget.setTabOrder(self.editButton, self.renameButton)
        QWidget.setTabOrder(self.renameButton, self.duplicateButton)
        QWidget.setTabOrder(self.duplicateButton, self.toolbarButton)
        QWidget.setTabOrder(self.toolbarButton, self.addonsButton)
        QWidget.setTabOrder(self.addonsButton, self.fileChooser)
        QWidget.setTabOrder(self.fileChooser, self.folderButton)

        self.retranslateUi(Gui__Dialog__DlgMacroExecute)
        self.closeButton.clicked.connect(Gui__Dialog__DlgMacroExecute.reject)
        self.userMacroListBox.itemDoubleClicked.connect(Gui__Dialog__DlgMacroExecute.accept)
        self.systemMacroListBox.itemDoubleClicked.connect(Gui__Dialog__DlgMacroExecute.accept)
        self.executeButton.clicked.connect(Gui__Dialog__DlgMacroExecute.accept)

        self.tabMacroWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Gui__Dialog__DlgMacroExecute)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgMacroExecute):
        Gui__Dialog__DlgMacroExecute.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Execute macro", None))
        self.MacroNameGroup.setTitle(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Macro name:", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Find file:", None))
#if QT_CONFIG(tooltip)
        self.LineEditFind.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Case-insensitive search for filenames, regular expressions supported", None))
#endif // QT_CONFIG(tooltip)
        self.label1.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Find in files:", None))
#if QT_CONFIG(tooltip)
        self.LineEditFindInFiles.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Filter by case-insensitive file content, regular expressions supported", None))
#endif // QT_CONFIG(tooltip)
        self.tabMacroWidget.setTabText(self.tabMacroWidget.indexOf(self.userSpecificTab), QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"User macros", None))
        self.tabMacroWidget.setTabText(self.tabMacroWidget.indexOf(self.systemWideTag), QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"System macros", None))
        self.executeButton.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Execute", None))
        self.closeButton.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Close", None))
        self.createButton.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Create", None))
        self.deleteButton.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Delete", None))
        self.editButton.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Edit", None))
        self.renameButton.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Rename", None))
        self.duplicateButton.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Duplicate", None))
#if QT_CONFIG(tooltip)
        self.toolbarButton.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Launch a guide on how to set up a macro in a custom global toolbar.", None))
#endif // QT_CONFIG(tooltip)
        self.toolbarButton.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Toolbar", None))
#if QT_CONFIG(tooltip)
        self.addonsButton.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Open Addon Manager where macros created by the community and other addons can be downloaded.", None))
#endif // QT_CONFIG(tooltip)
        self.addonsButton.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Download", None))
        self.DestinationGroup.setTitle(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"User macros location:", None))
#if QT_CONFIG(tooltip)
        self.folderButton.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Open folder with macros in system file manager.", None))
#endif // QT_CONFIG(tooltip)
        self.folderButton.setText(QCoreApplication.translate("Gui::Dialog::DlgMacroExecute", u"Open folder", None))
    # retranslateUi

