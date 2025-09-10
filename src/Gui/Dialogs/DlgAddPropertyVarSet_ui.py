# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgAddPropertyVarSet.ui'
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
    QDialog, QDialogButtonBox, QFormLayout, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_Gui_Dialog_DlgAddPropertyVarSet(object):
    def setupUi(self, Gui__Dialog__DlgAddPropertyVarSet):
        if not Gui__Dialog__DlgAddPropertyVarSet.objectName():
            Gui__Dialog__DlgAddPropertyVarSet.setObjectName(u"Gui__Dialog__DlgAddPropertyVarSet")
        Gui__Dialog__DlgAddPropertyVarSet.resize(418, 223)
        self.formLayout = QFormLayout(Gui__Dialog__DlgAddPropertyVarSet)
        self.formLayout.setObjectName(u"formLayout")
        self.labelName = QLabel(Gui__Dialog__DlgAddPropertyVarSet)
        self.labelName.setObjectName(u"labelName")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelName)

        self.lineEditName = QLineEdit(Gui__Dialog__DlgAddPropertyVarSet)
        self.lineEditName.setObjectName(u"lineEditName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditName)

        self.labelGroup = QLabel(Gui__Dialog__DlgAddPropertyVarSet)
        self.labelGroup.setObjectName(u"labelGroup")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelGroup)

        self.labelType = QLabel(Gui__Dialog__DlgAddPropertyVarSet)
        self.labelType.setObjectName(u"labelType")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelType)

        self.comboBoxType = QComboBox(Gui__Dialog__DlgAddPropertyVarSet)
        self.comboBoxType.setObjectName(u"comboBoxType")
        self.comboBoxType.setEditable(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxType)

        self.labelValue = QLabel(Gui__Dialog__DlgAddPropertyVarSet)
        self.labelValue.setObjectName(u"labelValue")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelValue)

        self.checkBoxAdd = QCheckBox(Gui__Dialog__DlgAddPropertyVarSet)
        self.checkBoxAdd.setObjectName(u"checkBoxAdd")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.checkBoxAdd)

        self.labelToolTip = QLabel(Gui__Dialog__DlgAddPropertyVarSet)
        self.labelToolTip.setObjectName(u"labelToolTip")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelToolTip)

        self.lineEditToolTip = QLineEdit(Gui__Dialog__DlgAddPropertyVarSet)
        self.lineEditToolTip.setObjectName(u"lineEditToolTip")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEditToolTip)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__DlgAddPropertyVarSet)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.buttonBox)


        self.retranslateUi(Gui__Dialog__DlgAddPropertyVarSet)
        self.buttonBox.accepted.connect(Gui__Dialog__DlgAddPropertyVarSet.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__DlgAddPropertyVarSet.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgAddPropertyVarSet)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgAddPropertyVarSet):
        Gui__Dialog__DlgAddPropertyVarSet.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgAddPropertyVarSet", u"Add property", None))
        self.labelName.setText(QCoreApplication.translate("Gui::Dialog::DlgAddPropertyVarSet", u"Name", None))
        self.labelGroup.setText(QCoreApplication.translate("Gui::Dialog::DlgAddPropertyVarSet", u"Group", None))
        self.labelType.setText(QCoreApplication.translate("Gui::Dialog::DlgAddPropertyVarSet", u"Type", None))
        self.labelValue.setText(QCoreApplication.translate("Gui::Dialog::DlgAddPropertyVarSet", u"Value", None))
        self.checkBoxAdd.setText(QCoreApplication.translate("Gui::Dialog::DlgAddPropertyVarSet", u"Add another", None))
        self.labelToolTip.setText(QCoreApplication.translate("Gui::Dialog::DlgAddPropertyVarSet", u"Tooltip", None))
    # retranslateUi

