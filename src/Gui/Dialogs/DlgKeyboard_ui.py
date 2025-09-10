# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgKeyboard.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgCustomKeyboard(object):
    def setupUi(self, Gui__Dialog__DlgCustomKeyboard):
        if not Gui__Dialog__DlgCustomKeyboard.objectName():
            Gui__Dialog__DlgCustomKeyboard.setObjectName(u"Gui__Dialog__DlgCustomKeyboard")
        Gui__Dialog__DlgCustomKeyboard.resize(642, 376)
        self.verticalLayout = QVBoxLayout(Gui__Dialog__DlgCustomKeyboard)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(Gui__Dialog__DlgCustomKeyboard)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.editCommand = QLineEdit(self.layoutWidget)
        self.editCommand.setObjectName(u"editCommand")

        self.gridLayout.addWidget(self.editCommand, 1, 0, 1, 2)

        self.TextLabelCategory = QLabel(self.layoutWidget)
        self.TextLabelCategory.setObjectName(u"TextLabelCategory")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextLabelCategory.sizePolicy().hasHeightForWidth())
        self.TextLabelCategory.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.TextLabelCategory, 2, 0, 1, 1)

        self.categoryBox = QComboBox(self.layoutWidget)
        self.categoryBox.setObjectName(u"categoryBox")

        self.gridLayout.addWidget(self.categoryBox, 2, 1, 1, 1)

        self.commandTreeWidget = QTreeWidget(self.layoutWidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.commandTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.commandTreeWidget.setObjectName(u"commandTreeWidget")
        self.commandTreeWidget.setMinimumSize(QSize(220, 0))
        self.commandTreeWidget.setRootIsDecorated(False)
        self.commandTreeWidget.setSortingEnabled(True)

        self.gridLayout.addWidget(self.commandTreeWidget, 3, 0, 1, 2)

        self.splitter.addWidget(self.layoutWidget)
        self.horizontalLayoutWidget = QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textLabelShortcut = QLabel(self.horizontalLayoutWidget)
        self.textLabelShortcut.setObjectName(u"textLabelShortcut")

        self.gridLayout_2.addWidget(self.textLabelShortcut, 1, 1, 1, 1)

        self.accelLineEditShortcut = Gui_AccelLineEdit(self.horizontalLayoutWidget)
        self.accelLineEditShortcut.setObjectName(u"accelLineEditShortcut")
        self.accelLineEditShortcut.setReadOnly(True)

        self.gridLayout_2.addWidget(self.accelLineEditShortcut, 1, 2, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textLabelNewShortcut = QLabel(self.horizontalLayoutWidget)
        self.textLabelNewShortcut.setObjectName(u"textLabelNewShortcut")

        self.horizontalLayout_4.addWidget(self.textLabelNewShortcut)

        self.editShortcut = Gui_AccelLineEdit(self.horizontalLayoutWidget)
        self.editShortcut.setObjectName(u"editShortcut")

        self.horizontalLayout_4.addWidget(self.editShortcut)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 1, 1, 3)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 4, 1, 1, 2)

        self.shortcutTimeout = Gui_PrefSpinBox(self.horizontalLayoutWidget)
        self.shortcutTimeout.setObjectName(u"shortcutTimeout")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.shortcutTimeout.sizePolicy().hasHeightForWidth())
        self.shortcutTimeout.setSizePolicy(sizePolicy1)
        self.shortcutTimeout.setMinimumSize(QSize(50, 0))
        self.shortcutTimeout.setMaximum(10000)
        self.shortcutTimeout.setSingleStep(100)
        self.shortcutTimeout.setValue(300)
        self.shortcutTimeout.setProperty(u"prefPath", u"Shortcut/Settings")
        self.shortcutTimeout.setProperty(u"prefEntry", u"ShortcutTimeout")

        self.gridLayout_2.addWidget(self.shortcutTimeout, 4, 3, 1, 1)

        self.textLabelAssigned = QLabel(self.horizontalLayoutWidget)
        self.textLabelAssigned.setObjectName(u"textLabelAssigned")
        self.textLabelAssigned.setMinimumSize(QSize(0, 20))

        self.gridLayout_2.addWidget(self.textLabelAssigned, 5, 1, 1, 3)

        self.assignedTreeWidget = QTreeWidget(self.horizontalLayoutWidget)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.assignedTreeWidget.setHeaderItem(__qtreewidgetitem1)
        self.assignedTreeWidget.setObjectName(u"assignedTreeWidget")
        self.assignedTreeWidget.setMinimumSize(QSize(220, 0))
        self.assignedTreeWidget.setAlternatingRowColors(True)
        self.assignedTreeWidget.setRootIsDecorated(False)

        self.gridLayout_2.addWidget(self.assignedTreeWidget, 6, 1, 1, 3)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonAssign = QPushButton(self.horizontalLayoutWidget)
        self.buttonAssign.setObjectName(u"buttonAssign")

        self.vboxLayout.addWidget(self.buttonAssign)

        self.buttonClear = QPushButton(self.horizontalLayoutWidget)
        self.buttonClear.setObjectName(u"buttonClear")

        self.vboxLayout.addWidget(self.buttonClear)

        self.buttonReset = QPushButton(self.horizontalLayoutWidget)
        self.buttonReset.setObjectName(u"buttonReset")

        self.vboxLayout.addWidget(self.buttonReset)

        self.buttonResetAll = QPushButton(self.horizontalLayoutWidget)
        self.buttonResetAll.setObjectName(u"buttonResetAll")

        self.vboxLayout.addWidget(self.buttonResetAll)

        self.spacerItem = QSpacerItem(41, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.spacerItem)

        self.buttonUp = QPushButton(self.horizontalLayoutWidget)
        self.buttonUp.setObjectName(u"buttonUp")
        self.buttonUp.setEnabled(False)

        self.vboxLayout.addWidget(self.buttonUp)

        self.buttonDown = QPushButton(self.horizontalLayoutWidget)
        self.buttonDown.setObjectName(u"buttonDown")
        self.buttonDown.setEnabled(False)

        self.vboxLayout.addWidget(self.buttonDown)


        self.horizontalLayout.addLayout(self.vboxLayout)

        self.splitter.addWidget(self.horizontalLayoutWidget)

        self.verticalLayout.addWidget(self.splitter)

        self.verticalLayout.setStretch(0, 1)
#if QT_CONFIG(shortcut)
        self.TextLabelCategory.setBuddy(self.categoryBox)
        self.textLabelNewShortcut.setBuddy(self.editShortcut)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.editCommand, self.categoryBox)
        QWidget.setTabOrder(self.categoryBox, self.commandTreeWidget)
        QWidget.setTabOrder(self.commandTreeWidget, self.accelLineEditShortcut)
        QWidget.setTabOrder(self.accelLineEditShortcut, self.editShortcut)
        QWidget.setTabOrder(self.editShortcut, self.shortcutTimeout)
        QWidget.setTabOrder(self.shortcutTimeout, self.buttonAssign)
        QWidget.setTabOrder(self.buttonAssign, self.buttonClear)
        QWidget.setTabOrder(self.buttonClear, self.buttonReset)
        QWidget.setTabOrder(self.buttonReset, self.buttonResetAll)
        QWidget.setTabOrder(self.buttonResetAll, self.assignedTreeWidget)
        QWidget.setTabOrder(self.assignedTreeWidget, self.buttonUp)
        QWidget.setTabOrder(self.buttonUp, self.buttonDown)

        self.retranslateUi(Gui__Dialog__DlgCustomKeyboard)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgCustomKeyboard)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgCustomKeyboard):
        Gui__Dialog__DlgCustomKeyboard.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"Keyboard", None))
        self.TextLabelCategory.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"&Category:", None))
        self.textLabelShortcut.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"Current shortcut:", None))
#if QT_CONFIG(tooltip)
        self.accelLineEditShortcut.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"To change a current shortcut enter the new shortcut in the field below and press 'Assign'.", None))
#endif // QT_CONFIG(tooltip)
        self.textLabelNewShortcut.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"&New shortcut:", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"Multi-key sequence delay:", None))
#if QT_CONFIG(tooltip)
        self.shortcutTimeout.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"Time in milliseconds to wait for the next keystroke of the current key sequence.\n"
"For example, pressing 'F' twice in less than the time delay setting here will be\n"
"treated as shortcut key sequence 'F, F'.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.textLabelAssigned.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"This list shows commands having the same shortcut in the priority from high\n"
"to low. If more than one command with the same shortcut are active at the\n"
"same time. The one with the highest priority will be triggered.", None))
#endif // QT_CONFIG(tooltip)
        self.textLabelAssigned.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"Shortcut priority list:", None))
        self.buttonAssign.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"&Assign", None))
#if QT_CONFIG(shortcut)
        self.buttonAssign.setShortcut(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"Alt+A", None))
#endif // QT_CONFIG(shortcut)
        self.buttonClear.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"Clear", None))
        self.buttonReset.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"&Reset", None))
#if QT_CONFIG(shortcut)
        self.buttonReset.setShortcut(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"Alt+R", None))
#endif // QT_CONFIG(shortcut)
        self.buttonResetAll.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"Re&set All", None))
#if QT_CONFIG(shortcut)
        self.buttonResetAll.setShortcut(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.buttonUp.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"Up", None))
        self.buttonDown.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomKeyboard", u"Down", None))
    # retranslateUi

