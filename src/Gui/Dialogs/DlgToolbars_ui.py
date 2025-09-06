# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgToolbars.ui'
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
import resource_rc

class Ui_Gui_Dialog_DlgCustomToolbars(object):
    def setupUi(self, Gui__Dialog__DlgCustomToolbars):
        if not Gui__Dialog__DlgCustomToolbars.objectName():
            Gui__Dialog__DlgCustomToolbars.setObjectName(u"Gui__Dialog__DlgCustomToolbars")
        Gui__Dialog__DlgCustomToolbars.resize(736, 352)
        Gui__Dialog__DlgCustomToolbars.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(Gui__Dialog__DlgCustomToolbars)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(Gui__Dialog__DlgCustomToolbars)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.categoryBox = QComboBox(self.widget)
        self.categoryBox.setObjectName(u"categoryBox")

        self.gridLayout_2.addWidget(self.categoryBox, 1, 1, 1, 1)

        self.editCommand = QLineEdit(self.widget)
        self.editCommand.setObjectName(u"editCommand")

        self.gridLayout_2.addWidget(self.editCommand, 0, 0, 1, 2)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.commandTreeWidget = QTreeWidget(self.widget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.commandTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.commandTreeWidget.setObjectName(u"commandTreeWidget")
        self.commandTreeWidget.setMinimumSize(QSize(400, 0))
        self.commandTreeWidget.setRootIsDecorated(False)

        self.gridLayout_2.addWidget(self.commandTreeWidget, 2, 0, 1, 2)

        self.splitter.addWidget(self.widget)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.spacerItem = QSpacerItem(33, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.spacerItem)

        self.moveActionRightButton = QPushButton(self.layoutWidget)
        self.moveActionRightButton.setObjectName(u"moveActionRightButton")
        self.moveActionRightButton.setEnabled(True)
        self.moveActionRightButton.setMinimumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icons/button_right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.moveActionRightButton.setIcon(icon)

        self.verticalLayout_2.addWidget(self.moveActionRightButton)

        self.moveActionLeftButton = QPushButton(self.layoutWidget)
        self.moveActionLeftButton.setObjectName(u"moveActionLeftButton")
        self.moveActionLeftButton.setEnabled(True)
        self.moveActionLeftButton.setMinimumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/button_left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.moveActionLeftButton.setIcon(icon1)
        self.moveActionLeftButton.setAutoDefault(True)

        self.verticalLayout_2.addWidget(self.moveActionLeftButton)

        self.moveActionUpButton = QPushButton(self.layoutWidget)
        self.moveActionUpButton.setObjectName(u"moveActionUpButton")
        self.moveActionUpButton.setEnabled(True)
        self.moveActionUpButton.setMinimumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons/button_up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.moveActionUpButton.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.moveActionUpButton)

        self.moveActionDownButton = QPushButton(self.layoutWidget)
        self.moveActionDownButton.setObjectName(u"moveActionDownButton")
        self.moveActionDownButton.setEnabled(True)
        self.moveActionDownButton.setMinimumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icons/button_down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.moveActionDownButton.setIcon(icon3)
        self.moveActionDownButton.setAutoDefault(True)

        self.verticalLayout_2.addWidget(self.moveActionDownButton)

        self.spacerItem1 = QSpacerItem(33, 57, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.spacerItem1)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.workbenchBox = QComboBox(self.layoutWidget)
        self.workbenchBox.setObjectName(u"workbenchBox")

        self.verticalLayout.addWidget(self.workbenchBox)

        self.toolbarTreeWidget = QTreeWidget(self.layoutWidget)
        self.toolbarTreeWidget.setObjectName(u"toolbarTreeWidget")
        self.toolbarTreeWidget.setColumnCount(0)

        self.verticalLayout.addWidget(self.toolbarTreeWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.spacerItem2 = QSpacerItem(20, 21, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vboxLayout.addItem(self.spacerItem2)

        self.newButton = QPushButton(self.layoutWidget)
        self.newButton.setObjectName(u"newButton")

        self.vboxLayout.addWidget(self.newButton)

        self.renameButton = QPushButton(self.layoutWidget)
        self.renameButton.setObjectName(u"renameButton")

        self.vboxLayout.addWidget(self.renameButton)

        self.deleteButton = QPushButton(self.layoutWidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.vboxLayout.addWidget(self.deleteButton)

        self.spacerItem3 = QSpacerItem(20, 152, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.spacerItem3)


        self.horizontalLayout.addLayout(self.vboxLayout)

        self.splitter.addWidget(self.layoutWidget)

        self.verticalLayout_3.addWidget(self.splitter)

        self.label = QLabel(Gui__Dialog__DlgCustomToolbars)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.label)

        QWidget.setTabOrder(self.editCommand, self.categoryBox)
        QWidget.setTabOrder(self.categoryBox, self.commandTreeWidget)
        QWidget.setTabOrder(self.commandTreeWidget, self.moveActionRightButton)
        QWidget.setTabOrder(self.moveActionRightButton, self.moveActionLeftButton)
        QWidget.setTabOrder(self.moveActionLeftButton, self.moveActionUpButton)
        QWidget.setTabOrder(self.moveActionUpButton, self.moveActionDownButton)
        QWidget.setTabOrder(self.moveActionDownButton, self.workbenchBox)
        QWidget.setTabOrder(self.workbenchBox, self.toolbarTreeWidget)
        QWidget.setTabOrder(self.toolbarTreeWidget, self.newButton)
        QWidget.setTabOrder(self.newButton, self.renameButton)
        QWidget.setTabOrder(self.renameButton, self.deleteButton)

        self.retranslateUi(Gui__Dialog__DlgCustomToolbars)

        self.moveActionLeftButton.setDefault(False)


        QMetaObject.connectSlotsByName(Gui__Dialog__DlgCustomToolbars)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgCustomToolbars):
        Gui__Dialog__DlgCustomToolbars.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"Toolbars", None))
        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"Category", None))
#if QT_CONFIG(tooltip)
        self.moveActionRightButton.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"Move Right", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.moveActionRightButton.setWhatsThis(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"<b>Moves the selected item one level down.</b><p>This will also change the level of the parent item.</p>", None))
#endif // QT_CONFIG(whatsthis)
        self.moveActionRightButton.setText("")
#if QT_CONFIG(tooltip)
        self.moveActionLeftButton.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"Move Left", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.moveActionLeftButton.setWhatsThis(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"<b>Moves the selected item one level up.</b><p>This will also change the level of the parent item.</p>", None))
#endif // QT_CONFIG(whatsthis)
        self.moveActionLeftButton.setText("")
#if QT_CONFIG(tooltip)
        self.moveActionUpButton.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"Move Up", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.moveActionUpButton.setWhatsThis(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"<b>Moves the selected item up.</b><p>The item will be moved within the hierarchy level.</p>", None))
#endif // QT_CONFIG(whatsthis)
        self.moveActionUpButton.setText("")
#if QT_CONFIG(tooltip)
        self.moveActionDownButton.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"Move Down", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.moveActionDownButton.setWhatsThis(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"<b>Moves the selected item down.</b><p>The item will be moved within the hierarchy level.</p>", None))
#endif // QT_CONFIG(whatsthis)
        self.moveActionDownButton.setText("")
        self.newButton.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"New", None))
        self.renameButton.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"Rename", None))
        self.deleteButton.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"Delete", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomToolbars", u"<html><head><meta name=\"qrichtext\" content=\"1\" /></head><body style=\" white-space: pre-wrap; font-size:7.8pt; font-weight:400; font-style:normal; text-decoration:none;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><span style=\" font-weight:600;\">Note:</span> The changes become active the next time you load the appropriate workbench</p></body></html>", None))
    # retranslateUi

