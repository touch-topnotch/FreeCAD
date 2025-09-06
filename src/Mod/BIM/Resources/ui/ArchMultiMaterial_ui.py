# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ArchMultiMaterial.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTreeView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(495, 395)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chooseCombo = QComboBox(Form)
        self.chooseCombo.addItem("")
        self.chooseCombo.setObjectName(u"chooseCombo")

        self.verticalLayout.addWidget(self.chooseCombo)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.nameField = QLineEdit(self.groupBox_2)
        self.nameField.setObjectName(u"nameField")

        self.horizontalLayout.addWidget(self.nameField)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.tree = QTreeView(self.groupBox_2)
        self.tree.setObjectName(u"tree")

        self.verticalLayout_3.addWidget(self.tree)

        self.labelTotalThickness = QLabel(self.groupBox_2)
        self.labelTotalThickness.setObjectName(u"labelTotalThickness")

        self.verticalLayout_3.addWidget(self.labelTotalThickness)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addButton = QPushButton(self.groupBox_2)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout_2.addWidget(self.addButton)

        self.upButton = QPushButton(self.groupBox_2)
        self.upButton.setObjectName(u"upButton")

        self.horizontalLayout_2.addWidget(self.upButton)

        self.downButton = QPushButton(self.groupBox_2)
        self.downButton.setObjectName(u"downButton")

        self.horizontalLayout_2.addWidget(self.downButton)

        self.delButton = QPushButton(self.groupBox_2)
        self.delButton.setObjectName(u"delButton")

        self.horizontalLayout_2.addWidget(self.delButton)

        self.invertButton = QPushButton(self.groupBox_2)
        self.invertButton.setObjectName(u"invertButton")

        self.horizontalLayout_2.addWidget(self.invertButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Multi-Material Definition", None))
        self.chooseCombo.setItemText(0, QCoreApplication.translate("Form", u"Copy existing\u2026", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Edit definition", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Composition", None))
        self.labelTotalThickness.setText(QCoreApplication.translate("Form", u"Total thickness", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.upButton.setText(QCoreApplication.translate("Form", u"Up", None))
        self.downButton.setText(QCoreApplication.translate("Form", u"Down", None))
        self.delButton.setText(QCoreApplication.translate("Form", u"Del", None))
        self.invertButton.setText(QCoreApplication.translate("Form", u"Invert", None))
    # retranslateUi

