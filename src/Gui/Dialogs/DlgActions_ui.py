# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgActions.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QToolButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Gui_Dialog_DlgCustomActions(object):
    def setupUi(self, Gui__Dialog__DlgCustomActions):
        if not Gui__Dialog__DlgCustomActions.objectName():
            Gui__Dialog__DlgCustomActions.setObjectName(u"Gui__Dialog__DlgCustomActions")
        Gui__Dialog__DlgCustomActions.resize(564, 383)
        self.horizontalLayout_3 = QHBoxLayout(Gui__Dialog__DlgCustomActions)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.GroupBox7 = QGroupBox(Gui__Dialog__DlgCustomActions)
        self.GroupBox7.setObjectName(u"GroupBox7")
        self.verticalLayout_2 = QVBoxLayout(self.GroupBox7)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(self.GroupBox7)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.actionListWidget = QTreeWidget(self.splitter)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.actionListWidget.setHeaderItem(__qtreewidgetitem)
        self.actionListWidget.setObjectName(u"actionListWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionListWidget.sizePolicy().hasHeightForWidth())
        self.actionListWidget.setSizePolicy(sizePolicy)
        self.actionListWidget.setRootIsDecorated(False)
        self.splitter.addWidget(self.actionListWidget)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        sizePolicy.setHeightForWidth(self.layoutWidget.sizePolicy().hasHeightForWidth())
        self.layoutWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TextLabel1_3 = QLabel(self.layoutWidget)
        self.TextLabel1_3.setObjectName(u"TextLabel1_3")

        self.gridLayout.addWidget(self.TextLabel1_3, 0, 0, 1, 1)

        self.TextLabel3 = QLabel(self.layoutWidget)
        self.TextLabel3.setObjectName(u"TextLabel3")

        self.gridLayout.addWidget(self.TextLabel3, 1, 0, 1, 1)

        self.TextLabel2_2 = QLabel(self.layoutWidget)
        self.TextLabel2_2.setObjectName(u"TextLabel2_2")

        self.gridLayout.addWidget(self.TextLabel2_2, 2, 0, 1, 1)

        self.TextLabel3_2 = QLabel(self.layoutWidget)
        self.TextLabel3_2.setObjectName(u"TextLabel3_2")

        self.gridLayout.addWidget(self.TextLabel3_2, 3, 0, 1, 1)

        self.TextLabel2 = QLabel(self.layoutWidget)
        self.TextLabel2.setObjectName(u"TextLabel2")

        self.gridLayout.addWidget(self.TextLabel2, 4, 0, 1, 1)

        self.TextLabel1 = QLabel(self.layoutWidget)
        self.TextLabel1.setObjectName(u"TextLabel1")

        self.gridLayout.addWidget(self.TextLabel1, 5, 0, 1, 1)

        self.actionAccel = Gui_AccelLineEdit(self.layoutWidget)
        self.actionAccel.setObjectName(u"actionAccel")

        self.gridLayout.addWidget(self.actionAccel, 5, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 2, 1, 1)

        self.TextLabel5_2 = QLabel(self.layoutWidget)
        self.TextLabel5_2.setObjectName(u"TextLabel5_2")

        self.gridLayout.addWidget(self.TextLabel5_2, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonChoosePixmap = QToolButton(self.layoutWidget)
        self.buttonChoosePixmap.setObjectName(u"buttonChoosePixmap")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonChoosePixmap.sizePolicy().hasHeightForWidth())
        self.buttonChoosePixmap.setSizePolicy(sizePolicy1)
        self.buttonChoosePixmap.setMinimumSize(QSize(40, 30))
        self.buttonChoosePixmap.setMaximumSize(QSize(40, 30))
        self.buttonChoosePixmap.setText(u"...")

        self.horizontalLayout.addWidget(self.buttonChoosePixmap)

        self.pixmapLabel = QLabel(self.layoutWidget)
        self.pixmapLabel.setObjectName(u"pixmapLabel")
        self.pixmapLabel.setMinimumSize(QSize(40, 40))
        self.pixmapLabel.setMaximumSize(QSize(40, 40))
        self.pixmapLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.pixmapLabel)

        self.spacerItem = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.spacerItem)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 1, 1, 1)

        self.actionMacros = QComboBox(self.layoutWidget)
        self.actionMacros.setObjectName(u"actionMacros")

        self.gridLayout.addWidget(self.actionMacros, 0, 1, 1, 2)

        self.actionMenu = QLineEdit(self.layoutWidget)
        self.actionMenu.setObjectName(u"actionMenu")

        self.gridLayout.addWidget(self.actionMenu, 1, 1, 1, 2)

        self.actionToolTip = QLineEdit(self.layoutWidget)
        self.actionToolTip.setObjectName(u"actionToolTip")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.actionToolTip.sizePolicy().hasHeightForWidth())
        self.actionToolTip.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.actionToolTip, 2, 1, 1, 2)

        self.actionStatus = QLineEdit(self.layoutWidget)
        self.actionStatus.setObjectName(u"actionStatus")

        self.gridLayout.addWidget(self.actionStatus, 3, 1, 1, 2)

        self.actionWhatsThis = QLineEdit(self.layoutWidget)
        self.actionWhatsThis.setObjectName(u"actionWhatsThis")

        self.gridLayout.addWidget(self.actionWhatsThis, 4, 1, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.spacerItem1 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.spacerItem1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonAddAction = QPushButton(self.layoutWidget)
        self.buttonAddAction.setObjectName(u"buttonAddAction")

        self.horizontalLayout_2.addWidget(self.buttonAddAction)

        self.buttonRemoveAction = QPushButton(self.layoutWidget)
        self.buttonRemoveAction.setObjectName(u"buttonRemoveAction")

        self.horizontalLayout_2.addWidget(self.buttonRemoveAction)

        self.buttonReplaceAction = QPushButton(self.layoutWidget)
        self.buttonReplaceAction.setObjectName(u"buttonReplaceAction")

        self.horizontalLayout_2.addWidget(self.buttonReplaceAction)

        self.spacerItem2 = QSpacerItem(41, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.spacerItem2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.layoutWidget)

        self.verticalLayout_2.addWidget(self.splitter)


        self.horizontalLayout_3.addWidget(self.GroupBox7)

        QWidget.setTabOrder(self.actionMacros, self.actionMenu)
        QWidget.setTabOrder(self.actionMenu, self.actionToolTip)
        QWidget.setTabOrder(self.actionToolTip, self.actionStatus)
        QWidget.setTabOrder(self.actionStatus, self.actionWhatsThis)
        QWidget.setTabOrder(self.actionWhatsThis, self.actionAccel)
        QWidget.setTabOrder(self.actionAccel, self.buttonAddAction)
        QWidget.setTabOrder(self.buttonAddAction, self.buttonRemoveAction)

        self.retranslateUi(Gui__Dialog__DlgCustomActions)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgCustomActions)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgCustomActions):
        Gui__Dialog__DlgCustomActions.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgCustomActions", u"Macros", None))
        self.GroupBox7.setTitle(QCoreApplication.translate("Gui::Dialog::DlgCustomActions", u"Setup Custom Macros", None))
        self.TextLabel1_3.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomActions", u"Macro:", None))
        self.TextLabel3.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomActions", u"Menu text:", None))
        self.TextLabel2_2.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomActions", u"Tool tip:", None))
        self.TextLabel3_2.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomActions", u"Status text:", None))
        self.TextLabel2.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomActions", u"What's this:", None))
        self.TextLabel1.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomActions", u"Accelerator:", None))
        self.TextLabel5_2.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomActions", u"Pixmap", None))
        self.buttonAddAction.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomActions", u"Add", None))
        self.buttonRemoveAction.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomActions", u"Remove", None))
        self.buttonReplaceAction.setText(QCoreApplication.translate("Gui::Dialog::DlgCustomActions", u"Replace", None))
    # retranslateUi

