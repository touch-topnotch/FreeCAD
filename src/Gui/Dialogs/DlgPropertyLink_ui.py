# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPropertyLink.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_Gui_Dialog_DlgPropertyLink(object):
    def setupUi(self, Gui__Dialog__DlgPropertyLink):
        if not Gui__Dialog__DlgPropertyLink.objectName():
            Gui__Dialog__DlgPropertyLink.setObjectName(u"Gui__Dialog__DlgPropertyLink")
        Gui__Dialog__DlgPropertyLink.resize(436, 438)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgPropertyLink)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeWidget = QTreeWidget(Gui__Dialog__DlgPropertyLink)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeWidget.setProperty(u"showDropIndicator", False)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setExpandsOnDoubleClick(False)
        self.treeWidget.header().setVisible(False)

        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkObjectType = QCheckBox(Gui__Dialog__DlgPropertyLink)
        self.checkObjectType.setObjectName(u"checkObjectType")

        self.horizontalLayout_2.addWidget(self.checkObjectType)

        self.checkSubObject = QCheckBox(Gui__Dialog__DlgPropertyLink)
        self.checkSubObject.setObjectName(u"checkSubObject")

        self.horizontalLayout_2.addWidget(self.checkSubObject)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.typeTree = QTreeWidget(Gui__Dialog__DlgPropertyLink)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.typeTree.setHeaderItem(__qtreewidgetitem1)
        self.typeTree.setObjectName(u"typeTree")
        self.typeTree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.typeTree.setRootIsDecorated(False)
        self.typeTree.setSortingEnabled(True)
        self.typeTree.header().setVisible(False)

        self.gridLayout.addWidget(self.typeTree, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Gui__Dialog__DlgPropertyLink)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.searchBox = Gui_ExpressionLineEdit(Gui__Dialog__DlgPropertyLink)
        self.searchBox.setObjectName(u"searchBox")

        self.horizontalLayout.addWidget(self.searchBox)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__DlgPropertyLink)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 10, 0, 1, 1)

        QWidget.setTabOrder(self.treeWidget, self.typeTree)
        QWidget.setTabOrder(self.typeTree, self.searchBox)
        QWidget.setTabOrder(self.searchBox, self.buttonBox)

        self.retranslateUi(Gui__Dialog__DlgPropertyLink)
        self.buttonBox.accepted.connect(Gui__Dialog__DlgPropertyLink.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__DlgPropertyLink.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgPropertyLink)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgPropertyLink):
        Gui__Dialog__DlgPropertyLink.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgPropertyLink", u"Link", None))
        self.checkObjectType.setText(QCoreApplication.translate("Gui::Dialog::DlgPropertyLink", u"Filter by type", None))
#if QT_CONFIG(tooltip)
        self.checkSubObject.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgPropertyLink", u"Synchronizes the 3D view selection with the full object hierarchy", None))
#endif // QT_CONFIG(tooltip)
        self.checkSubObject.setText(QCoreApplication.translate("Gui::Dialog::DlgPropertyLink", u"Sync sub-object selection", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgPropertyLink", u"Search", None))
#if QT_CONFIG(tooltip)
        self.searchBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgPropertyLink", u"A search pattern to filter the results above", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

