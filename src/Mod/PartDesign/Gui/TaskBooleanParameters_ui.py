# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskBooleanParameters.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QListWidget,
    QListWidgetItem, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_PartDesignGui_TaskBooleanParameters(object):
    def setupUi(self, PartDesignGui__TaskBooleanParameters):
        if not PartDesignGui__TaskBooleanParameters.objectName():
            PartDesignGui__TaskBooleanParameters.setObjectName(u"PartDesignGui__TaskBooleanParameters")
        PartDesignGui__TaskBooleanParameters.resize(209, 185)
        PartDesignGui__TaskBooleanParameters.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(PartDesignGui__TaskBooleanParameters)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonBodyAdd = QToolButton(PartDesignGui__TaskBooleanParameters)
        self.buttonBodyAdd.setObjectName(u"buttonBodyAdd")
        self.buttonBodyAdd.setCheckable(True)

        self.horizontalLayout.addWidget(self.buttonBodyAdd)

        self.buttonBodyRemove = QToolButton(PartDesignGui__TaskBooleanParameters)
        self.buttonBodyRemove.setObjectName(u"buttonBodyRemove")
        self.buttonBodyRemove.setCheckable(True)

        self.horizontalLayout.addWidget(self.buttonBodyRemove)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidgetBodies = QListWidget(PartDesignGui__TaskBooleanParameters)
        self.listWidgetBodies.setObjectName(u"listWidgetBodies")

        self.verticalLayout.addWidget(self.listWidgetBodies)

        self.comboType = QComboBox(PartDesignGui__TaskBooleanParameters)
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.addItem("")
        self.comboType.setObjectName(u"comboType")

        self.verticalLayout.addWidget(self.comboType)

        QWidget.setTabOrder(self.buttonBodyAdd, self.buttonBodyRemove)
        QWidget.setTabOrder(self.buttonBodyRemove, self.listWidgetBodies)
        QWidget.setTabOrder(self.listWidgetBodies, self.comboType)

        self.retranslateUi(PartDesignGui__TaskBooleanParameters)

        QMetaObject.connectSlotsByName(PartDesignGui__TaskBooleanParameters)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskBooleanParameters):
        self.buttonBodyAdd.setText(QCoreApplication.translate("PartDesignGui::TaskBooleanParameters", u"Add Body", None))
        self.buttonBodyRemove.setText(QCoreApplication.translate("PartDesignGui::TaskBooleanParameters", u"Remove Body", None))
        self.comboType.setItemText(0, QCoreApplication.translate("PartDesignGui::TaskBooleanParameters", u"Fuse", None))
        self.comboType.setItemText(1, QCoreApplication.translate("PartDesignGui::TaskBooleanParameters", u"Cut", None))
        self.comboType.setItemText(2, QCoreApplication.translate("PartDesignGui::TaskBooleanParameters", u"Common", None))

        pass
    # retranslateUi

