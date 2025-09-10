# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgObjectSelection.ui'
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
    QDialog, QDialogButtonBox, QHBoxLayout, QHeaderView,
    QLabel, QSizePolicy, QSplitter, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Gui_DlgObjectSelection(object):
    def setupUi(self, Gui__DlgObjectSelection):
        if not Gui__DlgObjectSelection.objectName():
            Gui__DlgObjectSelection.setObjectName(u"Gui__DlgObjectSelection")
        Gui__DlgObjectSelection.resize(795, 375)
        Gui__DlgObjectSelection.setSizeGripEnabled(True)
        Gui__DlgObjectSelection.setModal(True)
        self.verticalLayout = QVBoxLayout(Gui__DlgObjectSelection)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Gui__DlgObjectSelection)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.vsplitter = QSplitter(Gui__DlgObjectSelection)
        self.vsplitter.setObjectName(u"vsplitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vsplitter.sizePolicy().hasHeightForWidth())
        self.vsplitter.setSizePolicy(sizePolicy1)
        self.vsplitter.setOrientation(Qt.Horizontal)
        self.treeWidget = QTreeWidget(self.vsplitter)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy1.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy1)
        self.treeWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.vsplitter.addWidget(self.treeWidget)
        self.treeWidget.header().setVisible(False)
        self.splitter = QSplitter(self.vsplitter)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.depList = QTreeWidget(self.splitter)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(2, u"3");
        __qtreewidgetitem1.setText(1, u"2");
        __qtreewidgetitem1.setText(0, u"1");
        self.depList.setHeaderItem(__qtreewidgetitem1)
        self.depList.setObjectName(u"depList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.depList.sizePolicy().hasHeightForWidth())
        self.depList.setSizePolicy(sizePolicy2)
        self.depList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.depList.setRootIsDecorated(False)
        self.depList.setSortingEnabled(True)
        self.depList.setColumnCount(3)
        self.splitter.addWidget(self.depList)
        self.depList.header().setProperty(u"showSortIndicator", True)
        self.inList = QTreeWidget(self.splitter)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(2, u"3");
        __qtreewidgetitem2.setText(1, u"2");
        __qtreewidgetitem2.setText(0, u"1");
        self.inList.setHeaderItem(__qtreewidgetitem2)
        self.inList.setObjectName(u"inList")
        sizePolicy2.setHeightForWidth(self.inList.sizePolicy().hasHeightForWidth())
        self.inList.setSizePolicy(sizePolicy2)
        self.inList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.inList.setRootIsDecorated(False)
        self.inList.setSortingEnabled(True)
        self.inList.setColumnCount(3)
        self.splitter.addWidget(self.inList)
        self.inList.header().setProperty(u"showSortIndicator", True)
        self.vsplitter.addWidget(self.splitter)

        self.verticalLayout.addWidget(self.vsplitter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBoxAutoDeps = QCheckBox(Gui__DlgObjectSelection)
        self.checkBoxAutoDeps.setObjectName(u"checkBoxAutoDeps")

        self.horizontalLayout.addWidget(self.checkBoxAutoDeps)

        self.checkBoxShowDeps = QCheckBox(Gui__DlgObjectSelection)
        self.checkBoxShowDeps.setObjectName(u"checkBoxShowDeps")
        self.checkBoxShowDeps.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxShowDeps)

        self.buttonBox = QDialogButtonBox(Gui__DlgObjectSelection)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy3)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Gui__DlgObjectSelection)

        QMetaObject.connectSlotsByName(Gui__DlgObjectSelection)
    # setupUi

    def retranslateUi(self, Gui__DlgObjectSelection):
        Gui__DlgObjectSelection.setWindowTitle(QCoreApplication.translate("Gui::DlgObjectSelection", u"Object selection", None))
        self.label.setText(QCoreApplication.translate("Gui::DlgObjectSelection", u"The selected objects contain other dependencies. Please select which objects to export. All dependencies are auto selected by default.", None))
        self.checkBoxAutoDeps.setText(QCoreApplication.translate("Gui::DlgObjectSelection", u"Auto select depending objects", None))
        self.checkBoxShowDeps.setText(QCoreApplication.translate("Gui::DlgObjectSelection", u"Show dependencies", None))
    # retranslateUi

