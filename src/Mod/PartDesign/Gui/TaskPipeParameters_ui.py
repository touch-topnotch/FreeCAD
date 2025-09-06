# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskPipeParameters.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_PartDesignGui_TaskPipeParameters(object):
    def setupUi(self, PartDesignGui__TaskPipeParameters):
        if not PartDesignGui__TaskPipeParameters.objectName():
            PartDesignGui__TaskPipeParameters.setObjectName(u"PartDesignGui__TaskPipeParameters")
        PartDesignGui__TaskPipeParameters.resize(306, 421)
        PartDesignGui__TaskPipeParameters.setWindowTitle(u"Form")
        self.verticalLayout_2 = QVBoxLayout(PartDesignGui__TaskPipeParameters)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupprofile = QGroupBox(PartDesignGui__TaskPipeParameters)
        self.groupprofile.setObjectName(u"groupprofile")
        self.vboxLayout = QVBoxLayout(self.groupprofile)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.buttonProfileBase = QToolButton(self.groupprofile)
        self.buttonProfileBase.setObjectName(u"buttonProfileBase")
        self.buttonProfileBase.setCheckable(True)

        self.hboxLayout.addWidget(self.buttonProfileBase)

        self.profileBaseEdit = QLineEdit(self.groupprofile)
        self.profileBaseEdit.setObjectName(u"profileBaseEdit")

        self.hboxLayout.addWidget(self.profileBaseEdit)


        self.vboxLayout.addLayout(self.hboxLayout)


        self.verticalLayout_2.addWidget(self.groupprofile)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.label_2 = QLabel(PartDesignGui__TaskPipeParameters)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.comboBoxTransition = QComboBox(PartDesignGui__TaskPipeParameters)
        self.comboBoxTransition.addItem("")
        self.comboBoxTransition.addItem("")
        self.comboBoxTransition.addItem("")
        self.comboBoxTransition.setObjectName(u"comboBoxTransition")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxTransition.sizePolicy().hasHeightForWidth())
        self.comboBoxTransition.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBoxTransition)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.groupBox = QGroupBox(PartDesignGui__TaskPipeParameters)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonSpineBase = QToolButton(self.groupBox)
        self.buttonSpineBase.setObjectName(u"buttonSpineBase")
        self.buttonSpineBase.setCheckable(True)

        self.horizontalLayout.addWidget(self.buttonSpineBase)

        self.spineBaseEdit = QLineEdit(self.groupBox)
        self.spineBaseEdit.setObjectName(u"spineBaseEdit")

        self.horizontalLayout.addWidget(self.spineBaseEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttonRefAdd = QToolButton(self.groupBox)
        self.buttonRefAdd.setObjectName(u"buttonRefAdd")
        self.buttonRefAdd.setEnabled(True)
        sizePolicy.setHeightForWidth(self.buttonRefAdd.sizePolicy().hasHeightForWidth())
        self.buttonRefAdd.setSizePolicy(sizePolicy)
        self.buttonRefAdd.setCheckable(True)
        self.buttonRefAdd.setChecked(False)

        self.horizontalLayout_4.addWidget(self.buttonRefAdd)

        self.buttonRefRemove = QToolButton(self.groupBox)
        self.buttonRefRemove.setObjectName(u"buttonRefRemove")
        sizePolicy.setHeightForWidth(self.buttonRefRemove.sizePolicy().hasHeightForWidth())
        self.buttonRefRemove.setSizePolicy(sizePolicy)
        self.buttonRefRemove.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.buttonRefRemove)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.listWidgetReferences = QListWidget(self.groupBox)
        self.listWidgetReferences.setObjectName(u"listWidgetReferences")

        self.verticalLayout.addWidget(self.listWidgetReferences)


        self.verticalLayout_2.addWidget(self.groupBox)

        QWidget.setTabOrder(self.buttonProfileBase, self.profileBaseEdit)
        QWidget.setTabOrder(self.profileBaseEdit, self.comboBoxTransition)
        QWidget.setTabOrder(self.comboBoxTransition, self.buttonSpineBase)
        QWidget.setTabOrder(self.buttonSpineBase, self.spineBaseEdit)
        QWidget.setTabOrder(self.spineBaseEdit, self.buttonRefAdd)
        QWidget.setTabOrder(self.buttonRefAdd, self.buttonRefRemove)
        QWidget.setTabOrder(self.buttonRefRemove, self.listWidgetReferences)

        self.retranslateUi(PartDesignGui__TaskPipeParameters)

        QMetaObject.connectSlotsByName(PartDesignGui__TaskPipeParameters)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskPipeParameters):
        self.groupprofile.setTitle(QCoreApplication.translate("PartDesignGui::TaskPipeParameters", u"Profile", None))
        self.buttonProfileBase.setText(QCoreApplication.translate("PartDesignGui::TaskPipeParameters", u"Object", None))
        self.label_2.setText(QCoreApplication.translate("PartDesignGui::TaskPipeParameters", u"Corner transition", None))
        self.comboBoxTransition.setItemText(0, QCoreApplication.translate("PartDesignGui::TaskPipeParameters", u"Transformed", None))
        self.comboBoxTransition.setItemText(1, QCoreApplication.translate("PartDesignGui::TaskPipeParameters", u"Right corner", None))
        self.comboBoxTransition.setItemText(2, QCoreApplication.translate("PartDesignGui::TaskPipeParameters", u"Round corner", None))

        self.groupBox.setTitle(QCoreApplication.translate("PartDesignGui::TaskPipeParameters", u"Path to Sweep Along", None))
        self.buttonSpineBase.setText(QCoreApplication.translate("PartDesignGui::TaskPipeParameters", u"Object", None))
        self.buttonRefAdd.setText(QCoreApplication.translate("PartDesignGui::TaskPipeParameters", u"Add edge", None))
        self.buttonRefRemove.setText(QCoreApplication.translate("PartDesignGui::TaskPipeParameters", u"Remove edge", None))
        pass
    # retranslateUi

