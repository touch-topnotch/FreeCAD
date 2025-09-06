# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgTemplateField.ui'
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
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_TechDrawGui_dlgTemplateField(object):
    def setupUi(self, TechDrawGui__dlgTemplateField):
        if not TechDrawGui__dlgTemplateField.objectName():
            TechDrawGui__dlgTemplateField.setObjectName(u"TechDrawGui__dlgTemplateField")
        TechDrawGui__dlgTemplateField.setWindowModality(Qt.ApplicationModal)
        TechDrawGui__dlgTemplateField.resize(340, 132)
        TechDrawGui__dlgTemplateField.setModal(True)
        self.verticalLayout = QVBoxLayout(TechDrawGui__dlgTemplateField)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName(u"formLayout")
        self.lblMsg = QLabel(TechDrawGui__dlgTemplateField)
        self.lblMsg.setObjectName(u"lblMsg")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblMsg)

        self.lblName = QLabel(TechDrawGui__dlgTemplateField)
        self.lblName.setObjectName(u"lblName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lblName)

        self.label = QLabel(TechDrawGui__dlgTemplateField)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.leInput = QLineEdit(TechDrawGui__dlgTemplateField)
        self.leInput.setObjectName(u"leInput")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.leInput)

        self.cbAutofill = QCheckBox(TechDrawGui__dlgTemplateField)
        self.cbAutofill.setObjectName(u"cbAutofill")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.cbAutofill)

        self.leAutofill = QLineEdit(TechDrawGui__dlgTemplateField)
        self.leAutofill.setObjectName(u"leAutofill")
        self.leAutofill.setEnabled(False)
        self.leAutofill.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.leAutofill)


        self.verticalLayout.addLayout(self.formLayout)

        self.bbButtons = QDialogButtonBox(TechDrawGui__dlgTemplateField)
        self.bbButtons.setObjectName(u"bbButtons")
        self.bbButtons.setOrientation(Qt.Horizontal)
        self.bbButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.bbButtons.setCenterButtons(False)

        self.verticalLayout.addWidget(self.bbButtons)


        self.retranslateUi(TechDrawGui__dlgTemplateField)
        self.bbButtons.accepted.connect(TechDrawGui__dlgTemplateField.accept)
        self.bbButtons.rejected.connect(TechDrawGui__dlgTemplateField.reject)

        QMetaObject.connectSlotsByName(TechDrawGui__dlgTemplateField)
    # setupUi

    def retranslateUi(self, TechDrawGui__dlgTemplateField):
        TechDrawGui__dlgTemplateField.setWindowTitle(QCoreApplication.translate("TechDrawGui::dlgTemplateField", u"Change Editable Field", None))
        self.lblMsg.setText(QCoreApplication.translate("TechDrawGui::dlgTemplateField", u"Text name", None))
        self.lblName.setText(QCoreApplication.translate("TechDrawGui::dlgTemplateField", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("TechDrawGui::dlgTemplateField", u"Value", None))
#if QT_CONFIG(tooltip)
        self.cbAutofill.setToolTip(QCoreApplication.translate("TechDrawGui::dlgTemplateField", u"Reapplies auto-fill to this field", None))
#endif // QT_CONFIG(tooltip)
        self.cbAutofill.setText(QCoreApplication.translate("TechDrawGui::dlgTemplateField", u"Autofill", None))
#if QT_CONFIG(tooltip)
        self.leAutofill.setToolTip(QCoreApplication.translate("TechDrawGui::dlgTemplateField", u"The autofill replacement value", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

