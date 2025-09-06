# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogIfcElements.ui'
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
    QComboBox, QDialog, QDialogButtonBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QSizePolicy,
    QTreeView, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 488)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.onlyVisible = QCheckBox(Dialog)
        self.onlyVisible.setObjectName(u"onlyVisible")

        self.verticalLayout.addWidget(self.onlyVisible)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.groupMode = QComboBox(Dialog)
        icon = QIcon()
        iconThemeName = u"format-text-direction-ltr"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.groupMode.addItem(icon, "")
        icon1 = QIcon()
        iconThemeName = u"application-drawing"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.groupMode.addItem(icon1, "")
        self.groupMode.addItem("")
        self.groupMode.addItem("")
        self.groupMode.setObjectName(u"groupMode")

        self.horizontalLayout.addWidget(self.groupMode)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tree = QTreeView(Dialog)
        self.tree.setObjectName(u"tree")
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree.header().setDefaultSectionSize(250)
        self.tree.header().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tree)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.globalMaterial = QComboBox(Dialog)
        self.globalMaterial.setObjectName(u"globalMaterial")

        self.gridLayout.addWidget(self.globalMaterial, 1, 1, 1, 1)

        self.globalMode = QComboBox(Dialog)
        self.globalMode.setObjectName(u"globalMode")

        self.gridLayout.addWidget(self.globalMode, 0, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"IFC Elements Manager", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>This dialog lets you change the IFC type and material associated with any BIM object in this document. Double-click the IFC type to change, or use the drop-down menu below the list.</p></body></html>", None))
        self.onlyVisible.setText(QCoreApplication.translate("Dialog", u"Only visible BIM objects", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Order by", None))
        self.groupMode.setItemText(0, QCoreApplication.translate("Dialog", u"Alphabetical", None))
        self.groupMode.setItemText(1, QCoreApplication.translate("Dialog", u"IFC type", None))
        self.groupMode.setItemText(2, QCoreApplication.translate("Dialog", u"Material", None))
        self.groupMode.setItemText(3, QCoreApplication.translate("Dialog", u"Model structure", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"Change type", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Change material", None))
    # retranslateUi

