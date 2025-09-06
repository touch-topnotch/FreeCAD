# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskFeaturePick.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QListWidget, QListWidgetItem, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_PartDesignGui_TaskFeaturePick(object):
    def setupUi(self, PartDesignGui__TaskFeaturePick):
        if not PartDesignGui__TaskFeaturePick.objectName():
            PartDesignGui__TaskFeaturePick.setObjectName(u"PartDesignGui__TaskFeaturePick")
        PartDesignGui__TaskFeaturePick.resize(364, 487)
        PartDesignGui__TaskFeaturePick.setWindowTitle(u"Form")
        self.verticalLayout_4 = QVBoxLayout(PartDesignGui__TaskFeaturePick)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listWidget = QListWidget(PartDesignGui__TaskFeaturePick)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_4.addWidget(self.listWidget)

        self.checkUsed = QCheckBox(PartDesignGui__TaskFeaturePick)
        self.checkUsed.setObjectName(u"checkUsed")

        self.verticalLayout_4.addWidget(self.checkUsed)

        self.checkExternal = QGroupBox(PartDesignGui__TaskFeaturePick)
        self.checkExternal.setObjectName(u"checkExternal")
        self.checkExternal.setCheckable(False)
        self.checkExternal.setChecked(False)
        self.verticalLayout_2 = QVBoxLayout(self.checkExternal)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkOtherBody = QCheckBox(self.checkExternal)
        self.checkOtherBody.setObjectName(u"checkOtherBody")

        self.verticalLayout_2.addWidget(self.checkOtherBody)

        self.checkOtherPart = QCheckBox(self.checkExternal)
        self.checkOtherPart.setObjectName(u"checkOtherPart")

        self.verticalLayout_2.addWidget(self.checkOtherPart)

        self.line = QFrame(self.checkExternal)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.radioIndependent = QRadioButton(self.checkExternal)
        self.radioIndependent.setObjectName(u"radioIndependent")
        self.radioIndependent.setEnabled(False)
        self.radioIndependent.setChecked(True)

        self.verticalLayout_2.addWidget(self.radioIndependent)

        self.radioDependent = QRadioButton(self.checkExternal)
        self.radioDependent.setObjectName(u"radioDependent")
        self.radioDependent.setEnabled(False)

        self.verticalLayout_2.addWidget(self.radioDependent)

        self.radioXRef = QRadioButton(self.checkExternal)
        self.radioXRef.setObjectName(u"radioXRef")
        self.radioXRef.setEnabled(False)

        self.verticalLayout_2.addWidget(self.radioXRef)


        self.verticalLayout_4.addWidget(self.checkExternal)


        self.retranslateUi(PartDesignGui__TaskFeaturePick)

        QMetaObject.connectSlotsByName(PartDesignGui__TaskFeaturePick)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskFeaturePick):
        self.checkUsed.setText(QCoreApplication.translate("PartDesignGui::TaskFeaturePick", u"Allow used features", None))
        self.checkExternal.setTitle(QCoreApplication.translate("PartDesignGui::TaskFeaturePick", u"Allow External Features", None))
        self.checkOtherBody.setText(QCoreApplication.translate("PartDesignGui::TaskFeaturePick", u"From other bodies of the same part", None))
        self.checkOtherPart.setText(QCoreApplication.translate("PartDesignGui::TaskFeaturePick", u"From different parts or free features", None))
        self.radioIndependent.setText(QCoreApplication.translate("PartDesignGui::TaskFeaturePick", u"Make independent copy (recommended)", None))
        self.radioDependent.setText(QCoreApplication.translate("PartDesignGui::TaskFeaturePick", u"Make dependent copy", None))
        self.radioXRef.setText(QCoreApplication.translate("PartDesignGui::TaskFeaturePick", u"Create cross-reference", None))
        pass
    # retranslateUi

