# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogIfcProperties.ui'
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
    QComboBox, QDialog, QDialogButtonBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSplitter, QTreeView, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 608)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelinfo = QLabel(Dialog)
        self.labelinfo.setObjectName(u"labelinfo")
        self.labelinfo.setWordWrap(True)

        self.verticalLayout.addWidget(self.labelinfo)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.onlySelected = QCheckBox(Dialog)
        self.onlySelected.setObjectName(u"onlySelected")

        self.horizontalLayout.addWidget(self.onlySelected)

        self.onlyVisible = QCheckBox(Dialog)
        self.onlyVisible.setObjectName(u"onlyVisible")

        self.horizontalLayout.addWidget(self.onlyVisible)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.groupMode = QComboBox(Dialog)
        icon = QIcon()
        iconThemeName = u"format-text-direction-ltr"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.groupMode.addItem(icon, "")
        icon1 = QIcon()
        iconThemeName = u"application-drawing"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.groupMode.addItem(icon1, "")
        self.groupMode.addItem("")
        self.groupMode.setObjectName(u"groupMode")

        self.horizontalLayout_2.addWidget(self.groupMode)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.widget_2 = QWidget(self.splitter)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tree = QTreeView(self.widget_2)
        self.tree.setObjectName(u"tree")
        self.tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_3.addWidget(self.tree)

        self.splitter.addWidget(self.widget_2)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.searchField = QComboBox(self.widget)
        self.searchField.setObjectName(u"searchField")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchField.sizePolicy().hasHeightForWidth())
        self.searchField.setSizePolicy(sizePolicy)
        self.searchField.setEditable(True)

        self.horizontalLayout_3.addWidget(self.searchField)

        self.onlyMatches = QCheckBox(self.widget)
        self.onlyMatches.setObjectName(u"onlyMatches")
        self.onlyMatches.setChecked(True)

        self.horizontalLayout_3.addWidget(self.onlyMatches)

        self.buttonSelectAll = QPushButton(self.widget)
        self.buttonSelectAll.setObjectName(u"buttonSelectAll")

        self.horizontalLayout_3.addWidget(self.buttonSelectAll)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.treeProperties = QTreeView(self.widget)
        self.treeProperties.setObjectName(u"treeProperties")

        self.verticalLayout_2.addWidget(self.treeProperties)

        self.splitter.addWidget(self.widget)

        self.verticalLayout.addWidget(self.splitter)

        self.GroupBoxIfcProperties = QGroupBox(Dialog)
        self.GroupBoxIfcProperties.setObjectName(u"GroupBoxIfcProperties")
        self.GroupBoxIfcProperties.setEnabled(True)
        self.horizontalLayout_5 = QHBoxLayout(self.GroupBoxIfcProperties)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.comboProperty = QComboBox(self.GroupBoxIfcProperties)
        self.comboProperty.setObjectName(u"comboProperty")

        self.horizontalLayout_5.addWidget(self.comboProperty)

        self.comboPset = QComboBox(self.GroupBoxIfcProperties)
        self.comboPset.setObjectName(u"comboPset")

        self.horizontalLayout_5.addWidget(self.comboPset)

        self.buttonIFCPropertiesDelete = QPushButton(self.GroupBoxIfcProperties)
        self.buttonIFCPropertiesDelete.setObjectName(u"buttonIFCPropertiesDelete")
        icon2 = QIcon()
        iconThemeName = u"gtk-delete"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonIFCPropertiesDelete.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.buttonIFCPropertiesDelete)


        self.verticalLayout.addWidget(self.GroupBoxIfcProperties)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonSelectAll.clicked.connect(self.tree.selectAll)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"IFC Properties Manager", None))
        self.labelinfo.setText(QCoreApplication.translate("Dialog", u"This dialog allows you to display and manage IFC properties attached to BIM objects. Only properties and sets present in all selected objects will be displayed and editable.", None))
        self.onlySelected.setText(QCoreApplication.translate("Dialog", u"Only selected objects", None))
        self.onlyVisible.setText(QCoreApplication.translate("Dialog", u"Only visible BIM objects", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Order by:", None))
        self.groupMode.setItemText(0, QCoreApplication.translate("Dialog", u"Alphabetical", None))
        self.groupMode.setItemText(1, QCoreApplication.translate("Dialog", u"IFC type", None))
        self.groupMode.setItemText(2, QCoreApplication.translate("Dialog", u"Model structure", None))

        self.label_7.setText(QCoreApplication.translate("Dialog", u"Search for a property or property set:", None))
        self.onlyMatches.setText(QCoreApplication.translate("Dialog", u"Only show matches", None))
        self.buttonSelectAll.setText(QCoreApplication.translate("Dialog", u"Select All", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"List of IFC properties for the selected objects. Double-click to edit, drag and drop to reorganize", None))
        self.GroupBoxIfcProperties.setTitle(QCoreApplication.translate("Dialog", u"IFC Properties", None))
        self.buttonIFCPropertiesDelete.setText(QCoreApplication.translate("Dialog", u"Delete selected property/set", None))
    # retranslateUi

