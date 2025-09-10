# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ArchMaterial.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_ArchMaterial(object):
    def setupUi(self, ArchMaterial):
        if not ArchMaterial.objectName():
            ArchMaterial.setObjectName(u"ArchMaterial")
        ArchMaterial.resize(267, 327)
        self.verticalLayout = QVBoxLayout(ArchMaterial)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox_MaterialsInDir = QComboBox(ArchMaterial)
        self.comboBox_MaterialsInDir.addItem("")
        self.comboBox_MaterialsInDir.setObjectName(u"comboBox_MaterialsInDir")
        self.comboBox_MaterialsInDir.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout.addWidget(self.comboBox_MaterialsInDir)

        self.comboBox_FromExisting = QComboBox(ArchMaterial)
        self.comboBox_FromExisting.addItem("")
        self.comboBox_FromExisting.setObjectName(u"comboBox_FromExisting")
        self.comboBox_FromExisting.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout.addWidget(self.comboBox_FromExisting)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(ArchMaterial)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.FieldName = QLineEdit(ArchMaterial)
        self.FieldName.setObjectName(u"FieldName")

        self.horizontalLayout_3.addWidget(self.FieldName)

        self.ButtonEditor = QPushButton(ArchMaterial)
        self.ButtonEditor.setObjectName(u"ButtonEditor")
        self.ButtonEditor.setMaximumSize(QSize(30, 16777215))
        icon = QIcon()
        iconThemeName = u"edit-paste"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.ButtonEditor.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.ButtonEditor)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(ArchMaterial)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.FieldDescription = QLineEdit(ArchMaterial)
        self.FieldDescription.setObjectName(u"FieldDescription")

        self.horizontalLayout_6.addWidget(self.FieldDescription)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(ArchMaterial)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.ButtonColor = QPushButton(ArchMaterial)
        self.ButtonColor.setObjectName(u"ButtonColor")
        self.ButtonColor.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_2.addWidget(self.ButtonColor)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(ArchMaterial)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.ButtonSectionColor = QPushButton(ArchMaterial)
        self.ButtonSectionColor.setObjectName(u"ButtonSectionColor")
        self.ButtonSectionColor.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_7.addWidget(self.ButtonSectionColor)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(ArchMaterial)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.SpinBox_Transparency = QSpinBox(ArchMaterial)
        self.SpinBox_Transparency.setObjectName(u"SpinBox_Transparency")
        self.SpinBox_Transparency.setMaximum(100)

        self.horizontalLayout_8.addWidget(self.SpinBox_Transparency)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(ArchMaterial)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.FieldCode = QLineEdit(ArchMaterial)
        self.FieldCode.setObjectName(u"FieldCode")

        self.horizontalLayout_4.addWidget(self.FieldCode)

        self.ButtonCode = QPushButton(ArchMaterial)
        self.ButtonCode.setObjectName(u"ButtonCode")
        self.ButtonCode.setMaximumSize(QSize(30, 16777215))
        icon1 = QIcon()
        iconThemeName = u"web-browser"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.ButtonCode.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.ButtonCode)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(ArchMaterial)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.FieldUrl = QLineEdit(ArchMaterial)
        self.FieldUrl.setObjectName(u"FieldUrl")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FieldUrl.sizePolicy().hasHeightForWidth())
        self.FieldUrl.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.FieldUrl)

        self.ButtonUrl = QPushButton(ArchMaterial)
        self.ButtonUrl.setObjectName(u"ButtonUrl")
        self.ButtonUrl.setMaximumSize(QSize(30, 16777215))
        self.ButtonUrl.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.ButtonUrl)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(ArchMaterial)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.comboFather = QComboBox(ArchMaterial)
        self.comboFather.setObjectName(u"comboFather")
        self.comboFather.setMaximumSize(QSize(130, 16777215))
        self.comboFather.setEditable(True)

        self.horizontalLayout.addWidget(self.comboFather)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ArchMaterial)

        QMetaObject.connectSlotsByName(ArchMaterial)
    # setupUi

    def retranslateUi(self, ArchMaterial):
        ArchMaterial.setWindowTitle(QCoreApplication.translate("ArchMaterial", u"BIM material", None))
        self.comboBox_MaterialsInDir.setItemText(0, QCoreApplication.translate("ArchMaterial", u"Choose preset...", None))

#if QT_CONFIG(tooltip)
        self.comboBox_MaterialsInDir.setToolTip(QCoreApplication.translate("ArchMaterial", u"Choose a preset card", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_FromExisting.setItemText(0, QCoreApplication.translate("ArchMaterial", u"Copy existing...", None))

#if QT_CONFIG(tooltip)
        self.comboBox_FromExisting.setToolTip(QCoreApplication.translate("ArchMaterial", u"Copy values from an existing material in the document", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("ArchMaterial", u"Name", None))
#if QT_CONFIG(tooltip)
        self.FieldName.setToolTip(QCoreApplication.translate("ArchMaterial", u"The name/label of this material", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonEditor.setText("")
        self.label_5.setText(QCoreApplication.translate("ArchMaterial", u"Description", None))
#if QT_CONFIG(tooltip)
        self.FieldDescription.setToolTip(QCoreApplication.translate("ArchMaterial", u"An optional description for this material", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("ArchMaterial", u"Color", None))
#if QT_CONFIG(tooltip)
        self.ButtonColor.setToolTip(QCoreApplication.translate("ArchMaterial", u"The color of this material", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonColor.setText("")
        self.label_8.setText(QCoreApplication.translate("ArchMaterial", u"Section Color", None))
        self.ButtonSectionColor.setText("")
        self.label_6.setText(QCoreApplication.translate("ArchMaterial", u"Transparency", None))
#if QT_CONFIG(tooltip)
        self.SpinBox_Transparency.setToolTip(QCoreApplication.translate("ArchMaterial", u"A transparency value for this material", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("ArchMaterial", u"Standard code", None))
#if QT_CONFIG(tooltip)
        self.FieldCode.setToolTip(QCoreApplication.translate("ArchMaterial", u"A standard (MasterFormat, Omniclass...) code for this material", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ButtonCode.setToolTip(QCoreApplication.translate("ArchMaterial", u"Opens a browser dialog to choose a class from a BIM standard", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonCode.setText("")
        self.label_4.setText(QCoreApplication.translate("ArchMaterial", u"URL", None))
#if QT_CONFIG(tooltip)
        self.FieldUrl.setToolTip(QCoreApplication.translate("ArchMaterial", u"A URL describing this material", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ButtonUrl.setToolTip(QCoreApplication.translate("ArchMaterial", u"Opens the URL in a browser", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonUrl.setText("")
        self.label_7.setText(QCoreApplication.translate("ArchMaterial", u"Parent", None))
    # retranslateUi

