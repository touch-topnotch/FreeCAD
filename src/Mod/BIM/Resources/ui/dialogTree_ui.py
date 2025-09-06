# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogTree.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QHeaderView, QSizePolicy, QSplitter,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(845, 438)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.geomtree = QTreeWidget(self.splitter)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.geomtree.setHeaderItem(__qtreewidgetitem)
        self.geomtree.setObjectName(u"geomtree")
        self.geomtree.setMinimumSize(QSize(550, 0))
        self.splitter.addWidget(self.geomtree)
        self.geomtree.header().setVisible(False)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.proptree = QTableWidget(self.groupBox)
        if (self.proptree.columnCount() < 2):
            self.proptree.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.proptree.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.proptree.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.proptree.setObjectName(u"proptree")
        self.proptree.setMinimumSize(QSize(0, 0))
        self.proptree.setColumnCount(2)
        self.proptree.horizontalHeader().setStretchLastSection(True)
        self.proptree.verticalHeader().setVisible(False)
        self.proptree.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.proptree)

        self.splitter.addWidget(self.groupBox)

        self.verticalLayout.addWidget(self.splitter)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"IFC Representation", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"GroupBox", None))
        ___qtablewidgetitem = self.proptree.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Property", None));
        ___qtablewidgetitem1 = self.proptree.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Value", None));
    # retranslateUi

