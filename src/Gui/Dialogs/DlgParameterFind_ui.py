# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgParameterFind.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QWidget)

class Ui_Gui_Dialog_DlgParameterFind(object):
    def setupUi(self, Gui__Dialog__DlgParameterFind):
        if not Gui__Dialog__DlgParameterFind.objectName():
            Gui__Dialog__DlgParameterFind.setObjectName(u"Gui__Dialog__DlgParameterFind")
        Gui__Dialog__DlgParameterFind.resize(443, 212)
        self.gridLayout_3 = QGridLayout(Gui__Dialog__DlgParameterFind)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgParameterFind)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkGroups = QCheckBox(self.groupBox)
        self.checkGroups.setObjectName(u"checkGroups")
        self.checkGroups.setChecked(True)

        self.gridLayout.addWidget(self.checkGroups, 0, 0, 1, 1)

        self.checkNames = QCheckBox(self.groupBox)
        self.checkNames.setObjectName(u"checkNames")
        self.checkNames.setChecked(True)

        self.gridLayout.addWidget(self.checkNames, 1, 0, 1, 1)

        self.checkValues = QCheckBox(self.groupBox)
        self.checkValues.setObjectName(u"checkValues")
        self.checkValues.setChecked(True)

        self.gridLayout.addWidget(self.checkValues, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 3)

        self.checkMatch = QCheckBox(self.groupBox_2)
        self.checkMatch.setObjectName(u"checkMatch")
        self.checkMatch.setChecked(True)

        self.gridLayout_2.addWidget(self.checkMatch, 3, 0, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__DlgParameterFind)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_3.addWidget(self.buttonBox, 0, 1, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgParameterFind)
        self.buttonBox.accepted.connect(Gui__Dialog__DlgParameterFind.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__DlgParameterFind.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgParameterFind)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgParameterFind):
        Gui__Dialog__DlgParameterFind.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgParameterFind", u"Find", None))
        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgParameterFind", u"Find what:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgParameterFind", u"Look at", None))
        self.checkGroups.setText(QCoreApplication.translate("Gui::Dialog::DlgParameterFind", u"Groups", None))
        self.checkNames.setText(QCoreApplication.translate("Gui::Dialog::DlgParameterFind", u"Names", None))
        self.checkValues.setText(QCoreApplication.translate("Gui::Dialog::DlgParameterFind", u"Values", None))
        self.checkMatch.setText(QCoreApplication.translate("Gui::Dialog::DlgParameterFind", u"Match whole string only", None))
    # retranslateUi

