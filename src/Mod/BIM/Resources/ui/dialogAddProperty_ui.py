# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogAddProperty.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(338, 217)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.field_type = QComboBox(Dialog)
        self.field_type.addItem("")
        self.field_type.addItem("")
        self.field_type.addItem("")
        self.field_type.addItem("")
        self.field_type.addItem("")
        self.field_type.addItem("")
        self.field_type.setObjectName(u"field_type")

        self.gridLayout.addWidget(self.field_type, 2, 1, 1, 1)

        self.field_name = QLineEdit(Dialog)
        self.field_name.setObjectName(u"field_name")

        self.gridLayout.addWidget(self.field_name, 0, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.field_pset = QComboBox(Dialog)
        self.field_pset.setObjectName(u"field_pset")
        self.field_pset.setEditable(True)

        self.gridLayout.addWidget(self.field_pset, 3, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add IFC Property", None))
        self.field_type.setItemText(0, QCoreApplication.translate("Dialog", u"IfcLabel", None))
        self.field_type.setItemText(1, QCoreApplication.translate("Dialog", u"IfcBoolean", None))
        self.field_type.setItemText(2, QCoreApplication.translate("Dialog", u"IfcInteger", None))
        self.field_type.setItemText(3, QCoreApplication.translate("Dialog", u"IfcReal", None))
        self.field_type.setItemText(4, QCoreApplication.translate("Dialog", u"IfcLengthMeasure", None))
        self.field_type.setItemText(5, QCoreApplication.translate("Dialog", u"IfcAreaMeasure", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"PSet", None))
    # retranslateUi

