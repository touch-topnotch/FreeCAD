# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgAddProperty.ui'
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
    QLineEdit, QPlainTextEdit, QSizePolicy, QWidget)

class Ui_Gui_Dialog_DlgAddProperty(object):
    def setupUi(self, Gui__Dialog__DlgAddProperty):
        if not Gui__Dialog__DlgAddProperty.objectName():
            Gui__Dialog__DlgAddProperty.setObjectName(u"Gui__Dialog__DlgAddProperty")
        Gui__Dialog__DlgAddProperty.resize(418, 258)
        self.formLayout = QFormLayout(Gui__Dialog__DlgAddProperty)
        self.formLayout.setObjectName(u"formLayout")
        self.label_type = QLabel(Gui__Dialog__DlgAddProperty)
        self.label_type.setObjectName(u"label_type")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_type)

        self.comboType = QComboBox(Gui__Dialog__DlgAddProperty)
        self.comboType.setObjectName(u"comboType")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboType)

        self.label_group = QLabel(Gui__Dialog__DlgAddProperty)
        self.label_group.setObjectName(u"label_group")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_group)

        self.edtGroup = QLineEdit(Gui__Dialog__DlgAddProperty)
        self.edtGroup.setObjectName(u"edtGroup")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edtGroup)

        self.label_name = QLabel(Gui__Dialog__DlgAddProperty)
        self.label_name.setObjectName(u"label_name")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_name)

        self.edtName = QLineEdit(Gui__Dialog__DlgAddProperty)
        self.edtName.setObjectName(u"edtName")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edtName)

        self.label_doc = QLabel(Gui__Dialog__DlgAddProperty)
        self.label_doc.setObjectName(u"label_doc")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_doc)

        self.edtDoc = QPlainTextEdit(Gui__Dialog__DlgAddProperty)
        self.edtDoc.setObjectName(u"edtDoc")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.edtDoc)

        self.chkAppend = QCheckBox(Gui__Dialog__DlgAddProperty)
        self.chkAppend.setObjectName(u"chkAppend")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.chkAppend)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__DlgAddProperty)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.buttonBox)

        QWidget.setTabOrder(self.comboType, self.edtGroup)
        QWidget.setTabOrder(self.edtGroup, self.edtName)

        self.retranslateUi(Gui__Dialog__DlgAddProperty)
        self.buttonBox.accepted.connect(Gui__Dialog__DlgAddProperty.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__DlgAddProperty.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgAddProperty)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgAddProperty):
        Gui__Dialog__DlgAddProperty.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgAddProperty", u"Add Property", None))
        self.label_type.setText(QCoreApplication.translate("Gui::Dialog::DlgAddProperty", u"Type", None))
        self.label_group.setText(QCoreApplication.translate("Gui::Dialog::DlgAddProperty", u"Group", None))
        self.label_name.setText(QCoreApplication.translate("Gui::Dialog::DlgAddProperty", u"Name", None))
#if QT_CONFIG(tooltip)
        self.label_doc.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgAddProperty", u"Verbose description of the new property", None))
#endif // QT_CONFIG(tooltip)
        self.label_doc.setText(QCoreApplication.translate("Gui::Dialog::DlgAddProperty", u"Documentation", None))
#if QT_CONFIG(tooltip)
        self.edtDoc.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgAddProperty", u"Verbose description of the new property", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.chkAppend.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgAddProperty", u"Prefix the property name with the group name in the form 'Group_Name' to avoid conflicts with an existing property.\n"
"In this case the prefix will be automatically trimmed when shown in the property editor.\n"
"However, the property is still used in a script with the full name, like 'obj.Group_Name'.\n"
"\n"
"If this is not checked, the property must be uniquely named, and it is accessed like 'obj.Name'.", None))
#endif // QT_CONFIG(tooltip)
        self.chkAppend.setText(QCoreApplication.translate("Gui::Dialog::DlgAddProperty", u"Prefix group name", None))
    # retranslateUi

