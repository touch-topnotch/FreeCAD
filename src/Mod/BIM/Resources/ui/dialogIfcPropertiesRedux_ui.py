# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogIfcPropertiesRedux.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTreeView, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(289, 548)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.labelUUID = QLineEdit(Dialog)
        self.labelUUID.setObjectName(u"labelUUID")

        self.horizontalLayout_4.addWidget(self.labelUUID)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.treeProperties = QTreeView(Dialog)
        self.treeProperties.setObjectName(u"treeProperties")

        self.verticalLayout.addWidget(self.treeProperties)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboPset = QComboBox(Dialog)
        self.comboPset.setObjectName(u"comboPset")

        self.gridLayout.addWidget(self.comboPset, 0, 0, 1, 1)

        self.comboProperty = QComboBox(Dialog)
        self.comboProperty.setObjectName(u"comboProperty")

        self.gridLayout.addWidget(self.comboProperty, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonDelete = QPushButton(Dialog)
        self.buttonDelete.setObjectName(u"buttonDelete")
        icon = QIcon()
        iconThemeName = u"gtk-delete"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../../../../../../.FreeCAD/Mod/BIM", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonDelete.setIcon(icon)

        self.horizontalLayout.addWidget(self.buttonDelete)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.checkBrep = QCheckBox(Dialog)
        self.checkBrep.setObjectName(u"checkBrep")

        self.verticalLayout.addWidget(self.checkBrep)

        self.checkParametric = QCheckBox(Dialog)
        self.checkParametric.setObjectName(u"checkParametric")

        self.verticalLayout.addWidget(self.checkParametric)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"IFC Properties Editor", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"IFC UUID", None))
        self.labelUUID.setPlaceholderText(QCoreApplication.translate("Dialog", u"Leave this empty to generate one at export", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"List of IFC properties for this object. Double-click to edit. Drag and drop to reorganize.", None))
        self.buttonDelete.setText(QCoreApplication.translate("Dialog", u"Delete Selected Property/Property Set", None))
        self.checkBrep.setText(QCoreApplication.translate("Dialog", u"Force exporting geometry as BREP", None))
        self.checkParametric.setText(QCoreApplication.translate("Dialog", u"Force export of full FreeCAD parametric data", None))
    # retranslateUi

