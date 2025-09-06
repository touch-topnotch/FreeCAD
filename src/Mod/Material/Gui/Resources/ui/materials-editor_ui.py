# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'materials-editor.ui'
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
    QDialogButtonBox, QGroupBox, QHBoxLayout, QHeaderView,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QTreeView, QVBoxLayout, QWidget)

class Ui_MaterialEditor(object):
    def setupUi(self, MaterialEditor):
        if not MaterialEditor.objectName():
            MaterialEditor.setObjectName(u"MaterialEditor")
        MaterialEditor.resize(441, 626)
        self.verticalLayout_2 = QVBoxLayout(MaterialEditor)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_3 = QGroupBox(MaterialEditor)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.topLayout = QHBoxLayout()
        self.topLayout.setObjectName(u"topLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ButtonURL = QPushButton(self.groupBox_3)
        self.ButtonURL.setObjectName(u"ButtonURL")
        self.ButtonURL.setMaximumSize(QSize(22, 22))

        self.horizontalLayout_7.addWidget(self.ButtonURL)

        self.ComboMaterial = QComboBox(self.groupBox_3)
        self.ComboMaterial.setObjectName(u"ComboMaterial")
        self.ComboMaterial.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_7.addWidget(self.ComboMaterial)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ButtonOpen = QPushButton(self.groupBox_3)
        self.ButtonOpen.setObjectName(u"ButtonOpen")

        self.horizontalLayout.addWidget(self.ButtonOpen)

        self.ButtonSave = QPushButton(self.groupBox_3)
        self.ButtonSave.setObjectName(u"ButtonSave")

        self.horizontalLayout.addWidget(self.ButtonSave)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.topLayout.addLayout(self.verticalLayout_6)


        self.verticalLayout_4.addLayout(self.topLayout)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(MaterialEditor)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.treeView = QTreeView(self.groupBox_4)
        self.treeView.setObjectName(u"treeView")

        self.horizontalLayout_3.addWidget(self.treeView)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(MaterialEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.EditProperty = QLineEdit(self.groupBox_2)
        self.EditProperty.setObjectName(u"EditProperty")

        self.horizontalLayout_6.addWidget(self.EditProperty)

        self.ButtonAddProperty = QPushButton(self.groupBox_2)
        self.ButtonAddProperty.setObjectName(u"ButtonAddProperty")

        self.horizontalLayout_6.addWidget(self.ButtonAddProperty)

        self.ButtonDeleteProperty = QPushButton(self.groupBox_2)
        self.ButtonDeleteProperty.setObjectName(u"ButtonDeleteProperty")

        self.horizontalLayout_6.addWidget(self.ButtonDeleteProperty)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.standardButtons = QDialogButtonBox(MaterialEditor)
        self.standardButtons.setObjectName(u"standardButtons")
        self.standardButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.standardButtons)


        self.retranslateUi(MaterialEditor)

        QMetaObject.connectSlotsByName(MaterialEditor)
    # setupUi

    def retranslateUi(self, MaterialEditor):
        MaterialEditor.setWindowTitle(QCoreApplication.translate("MaterialEditor", u"Material Editor", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MaterialEditor", u"Material Card", None))
#if QT_CONFIG(tooltip)
        self.ButtonURL.setToolTip(QCoreApplication.translate("MaterialEditor", u"Opens the Product URL of this material in an external browser", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonURL.setText("")
#if QT_CONFIG(tooltip)
        self.ComboMaterial.setToolTip(QCoreApplication.translate("MaterialEditor", u"Existing material cards", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ButtonOpen.setToolTip(QCoreApplication.translate("MaterialEditor", u"Opens an existing material card", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonOpen.setText(QCoreApplication.translate("MaterialEditor", u"Open\u2026", None))
#if QT_CONFIG(tooltip)
        self.ButtonSave.setToolTip(QCoreApplication.translate("MaterialEditor", u"Saves this material as a card", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonSave.setText(QCoreApplication.translate("MaterialEditor", u"Save As\u2026", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MaterialEditor", u"Material Parameter", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MaterialEditor", u"Add/Remove Parameter", None))
        self.ButtonAddProperty.setText(QCoreApplication.translate("MaterialEditor", u"Add Property", None))
        self.ButtonDeleteProperty.setText(QCoreApplication.translate("MaterialEditor", u"Delete Property", None))
    # retranslateUi

