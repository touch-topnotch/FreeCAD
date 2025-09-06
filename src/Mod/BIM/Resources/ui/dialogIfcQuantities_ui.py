# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogIfcQuantities.ui'
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
    QComboBox, QDialog, QDialogButtonBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTreeView, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(680, 512)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_5)

        self.onlyVisible = QCheckBox(Dialog)
        self.onlyVisible.setObjectName(u"onlyVisible")

        self.verticalLayout.addWidget(self.onlyVisible)

        self.quantities = QTreeView(Dialog)
        self.quantities.setObjectName(u"quantities")
        self.quantities.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.quantities)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.comboQto = QComboBox(Dialog)
        self.comboQto.setObjectName(u"comboQto")

        self.horizontalLayout_6.addWidget(self.comboQto)

        self.buttonApply = QPushButton(Dialog)
        self.buttonApply.setObjectName(u"buttonApply")

        self.horizontalLayout_6.addWidget(self.buttonApply)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.buttonRefresh = QPushButton(Dialog)
        self.buttonRefresh.setObjectName(u"buttonRefresh")
        icon = QIcon()
        iconThemeName = u"reload"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonRefresh.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.buttonRefresh)

        self.buttonSelectAll = QPushButton(Dialog)
        self.buttonSelectAll.setObjectName(u"buttonSelectAll")
        icon1 = QIcon()
        iconThemeName = u"edit-select-all"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonSelectAll.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.buttonSelectAll)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonSelectAll.clicked.connect(self.quantities.selectAll)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"IFC Quantities Manager", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Checked quantities will be exported to IFC. Quantities marked with a warning sign indicate a zero value that you might need to check. Clicking a column header will apply to all selected items.</p><p><span style=\" font-weight:600;\">Warning</span>: Horizontal area is the area obtained when projecting the object on the ground (X,Y) plane, but vertical area is the sum of all areas of the faces that are vertical (orthogonal to the ground plane), so a wall will have its both faces counted.</p><p>Length, width and height values can be changed here, but beware, it might change the geometry!</p></body></html>", None))
        self.onlyVisible.setText(QCoreApplication.translate("Dialog", u"Only visible BIM objects", None))
        self.buttonApply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.buttonRefresh.setText(QCoreApplication.translate("Dialog", u"Refresh", None))
        self.buttonSelectAll.setText(QCoreApplication.translate("Dialog", u"Select All", None))
    # retranslateUi

