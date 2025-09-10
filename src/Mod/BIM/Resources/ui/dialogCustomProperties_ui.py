# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogCustomProperties.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(206, 367)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        iconThemeName = u"gtk-add"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.pushButton.setIcon(icon)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        iconThemeName = u"gtk-remove"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.pushButton_2.setIcon(icon1)

        self.verticalLayout.addWidget(self.pushButton_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Custom properties", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Name", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("Form", u"Can only contain alphanumerical characters and no spaces. Use CamelCase typing to define spaces automatically", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Description", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip(QCoreApplication.translate("Form", u"A description for this property, can be in any language.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.radioButton_2.setToolTip(QCoreApplication.translate("Form", u"The property will be hidden in the interface, and can only be modified via Python script", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"Hidden", None))
#if QT_CONFIG(tooltip)
        self.radioButton.setToolTip(QCoreApplication.translate("Form", u"The property is visible but cannot be modified by the user", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton.setText(QCoreApplication.translate("Form", u"Read-only", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

