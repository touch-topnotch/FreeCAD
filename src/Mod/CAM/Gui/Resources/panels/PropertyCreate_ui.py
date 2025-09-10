# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PropertyCreate.ui'
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
    QDialog, QDialogButtonBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(480, 452)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.labelName = QLabel(Dialog)
        self.labelName.setObjectName(u"labelName")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelName)

        self.propertyName = QLineEdit(Dialog)
        self.propertyName.setObjectName(u"propertyName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.propertyName)

        self.propertyGroup = QComboBox(Dialog)
        self.propertyGroup.setObjectName(u"propertyGroup")
        self.propertyGroup.setEditable(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.propertyGroup)

        self.labelGroup = QLabel(Dialog)
        self.labelGroup.setObjectName(u"labelGroup")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelGroup)

        self.propertyType = QComboBox(Dialog)
        self.propertyType.setObjectName(u"propertyType")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.propertyType)

        self.labelType = QLabel(Dialog)
        self.labelType.setObjectName(u"labelType")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelType)

        self.propertyEnum = QLineEdit(Dialog)
        self.propertyEnum.setObjectName(u"propertyEnum")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.propertyEnum)

        self.propertyInfo = QTextEdit(Dialog)
        self.propertyInfo.setObjectName(u"propertyInfo")
        self.propertyInfo.setTabChangesFocus(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.propertyInfo)

        self.labelEnum = QLabel(Dialog)
        self.labelEnum.setObjectName(u"labelEnum")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelEnum)

        self.labelInfo = QLabel(Dialog)
        self.labelInfo.setObjectName(u"labelInfo")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelInfo)

        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.createAnother = QCheckBox(self.widget_2)
        self.createAnother.setObjectName(u"createAnother")

        self.horizontalLayout_2.addWidget(self.createAnother)

        self.buttonBox = QDialogButtonBox(self.widget_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_2.addWidget(self.buttonBox)


        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.widget_2)

        QWidget.setTabOrder(self.propertyName, self.propertyGroup)
        QWidget.setTabOrder(self.propertyGroup, self.propertyType)
        QWidget.setTabOrder(self.propertyType, self.propertyEnum)
        QWidget.setTabOrder(self.propertyEnum, self.propertyInfo)
        QWidget.setTabOrder(self.propertyInfo, self.createAnother)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Create Property", None))
        self.labelName.setText(QCoreApplication.translate("Dialog", u"Name", None))
#if QT_CONFIG(tooltip)
        self.propertyName.setToolTip(QCoreApplication.translate("Dialog", u"Name of property. Can only contain letters, numbers, and underscores. MixedCase names will display with spaces \"Mixed Case\"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.propertyGroup.setToolTip(QCoreApplication.translate("Dialog", u"The category group the property belongs to.", None))
#endif // QT_CONFIG(tooltip)
        self.labelGroup.setText(QCoreApplication.translate("Dialog", u"Group", None))
#if QT_CONFIG(tooltip)
        self.propertyType.setToolTip(QCoreApplication.translate("Dialog", u"The type of the property value.", None))
#endif // QT_CONFIG(tooltip)
        self.labelType.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.propertyEnum.setPlaceholderText(QCoreApplication.translate("Dialog", u"val1,val2,val3,...", None))
#if QT_CONFIG(tooltip)
        self.propertyInfo.setToolTip(QCoreApplication.translate("Dialog", u"ToolTip to be displayed when user hovers mouse over property.", None))
#endif // QT_CONFIG(tooltip)
        self.labelEnum.setText(QCoreApplication.translate("Dialog", u"Enums", None))
        self.labelInfo.setText(QCoreApplication.translate("Dialog", u"ToolTip", None))
#if QT_CONFIG(tooltip)
        self.createAnother.setToolTip(QCoreApplication.translate("Dialog", u"Check if you want to create several properties in a batch.", None))
#endif // QT_CONFIG(tooltip)
        self.createAnother.setText(QCoreApplication.translate("Dialog", u"Create another", None))
    # retranslateUi

