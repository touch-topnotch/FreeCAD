# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgMaterialProperties.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_Gui_Dialog_DlgMaterialProperties(object):
    def setupUi(self, Gui__Dialog__DlgMaterialProperties):
        if not Gui__Dialog__DlgMaterialProperties.objectName():
            Gui__Dialog__DlgMaterialProperties.setObjectName(u"Gui__Dialog__DlgMaterialProperties")
        Gui__Dialog__DlgMaterialProperties.resize(292, 296)
        Gui__Dialog__DlgMaterialProperties.setSizeGripEnabled(True)
        Gui__Dialog__DlgMaterialProperties.setModal(True)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgMaterialProperties)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox4 = QGroupBox(Gui__Dialog__DlgMaterialProperties)
        self.groupBox4.setObjectName(u"groupBox4")
        self.gridLayout1 = QGridLayout(self.groupBox4)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
        self.textLabel1 = QLabel(self.groupBox4)
        self.textLabel1.setObjectName(u"textLabel1")

        self.gridLayout1.addWidget(self.textLabel1, 1, 0, 1, 1)

        self.textLabel4 = QLabel(self.groupBox4)
        self.textLabel4.setObjectName(u"textLabel4")

        self.gridLayout1.addWidget(self.textLabel4, 4, 0, 1, 1)

        self.ambientColor = Gui_ColorButton(self.groupBox4)
        self.ambientColor.setObjectName(u"ambientColor")
        self.ambientColor.setAllowTransparency(True)

        self.gridLayout1.addWidget(self.ambientColor, 0, 1, 1, 1)

        self.buttonReset = QPushButton(self.groupBox4)
        self.buttonReset.setObjectName(u"buttonReset")

        self.gridLayout1.addWidget(self.buttonReset, 6, 0, 1, 1)

        self.textLabel2 = QLabel(self.groupBox4)
        self.textLabel2.setObjectName(u"textLabel2")

        self.gridLayout1.addWidget(self.textLabel2, 0, 0, 1, 1)

        self.shininess = QSpinBox(self.groupBox4)
        self.shininess.setObjectName(u"shininess")
        self.shininess.setMinimumSize(QSize(122, 0))
        self.shininess.setSuffix(u"%")
        self.shininess.setMaximum(100)
        self.shininess.setSingleStep(5)

        self.gridLayout1.addWidget(self.shininess, 4, 1, 1, 1)

        self.emissiveColor = Gui_ColorButton(self.groupBox4)
        self.emissiveColor.setObjectName(u"emissiveColor")
        self.emissiveColor.setAllowTransparency(True)

        self.gridLayout1.addWidget(self.emissiveColor, 2, 1, 1, 1)

        self.textLabel3 = QLabel(self.groupBox4)
        self.textLabel3.setObjectName(u"textLabel3")

        self.gridLayout1.addWidget(self.textLabel3, 3, 0, 1, 1)

        self.specularColor = Gui_ColorButton(self.groupBox4)
        self.specularColor.setObjectName(u"specularColor")
        self.specularColor.setAllowTransparency(True)

        self.gridLayout1.addWidget(self.specularColor, 3, 1, 1, 1)

        self.buttonDefault = QPushButton(self.groupBox4)
        self.buttonDefault.setObjectName(u"buttonDefault")

        self.gridLayout1.addWidget(self.buttonDefault, 6, 1, 1, 1)

        self.diffuseColor = Gui_ColorButton(self.groupBox4)
        self.diffuseColor.setObjectName(u"diffuseColor")
        self.diffuseColor.setAllowTransparency(True)

        self.gridLayout1.addWidget(self.diffuseColor, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox4)
        self.label.setObjectName(u"label")

        self.gridLayout1.addWidget(self.label, 2, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout1.addWidget(self.label_2, 5, 0, 1, 1)

        self.transparency = QSpinBox(self.groupBox4)
        self.transparency.setObjectName(u"transparency")
        self.transparency.setMinimumSize(QSize(122, 0))
        self.transparency.setMaximum(100)

        self.gridLayout1.addWidget(self.transparency, 5, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox4, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__DlgMaterialProperties)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.ambientColor, self.diffuseColor)
        QWidget.setTabOrder(self.diffuseColor, self.emissiveColor)
        QWidget.setTabOrder(self.emissiveColor, self.specularColor)

        self.retranslateUi(Gui__Dialog__DlgMaterialProperties)
        self.buttonBox.rejected.connect(Gui__Dialog__DlgMaterialProperties.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgMaterialProperties)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgMaterialProperties):
        Gui__Dialog__DlgMaterialProperties.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgMaterialProperties", u"Material Properties", None))
        self.groupBox4.setTitle(QCoreApplication.translate("Gui::Dialog::DlgMaterialProperties", u"Material", None))
        self.textLabel1.setText(QCoreApplication.translate("Gui::Dialog::DlgMaterialProperties", u"Diffuse color", None))
        self.textLabel4.setText(QCoreApplication.translate("Gui::Dialog::DlgMaterialProperties", u"Shininess", None))
        self.ambientColor.setText("")
        self.buttonReset.setText(QCoreApplication.translate("Gui::Dialog::DlgMaterialProperties", u"Reset", None))
        self.textLabel2.setText(QCoreApplication.translate("Gui::Dialog::DlgMaterialProperties", u"Ambient color", None))
        self.emissiveColor.setText("")
        self.textLabel3.setText(QCoreApplication.translate("Gui::Dialog::DlgMaterialProperties", u"Specular color", None))
        self.specularColor.setText("")
        self.buttonDefault.setText(QCoreApplication.translate("Gui::Dialog::DlgMaterialProperties", u"Default", None))
        self.diffuseColor.setText("")
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgMaterialProperties", u"Emissive color", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgMaterialProperties", u"Transparency", None))
        self.transparency.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgMaterialProperties", u"%", None))
    # retranslateUi

