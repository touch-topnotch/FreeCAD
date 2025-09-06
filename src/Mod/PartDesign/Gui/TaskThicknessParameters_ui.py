# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskThicknessParameters.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QLabel, QListWidget, QListWidgetItem,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_PartDesignGui_TaskThicknessParameters(object):
    def setupUi(self, PartDesignGui__TaskThicknessParameters):
        if not PartDesignGui__TaskThicknessParameters.objectName():
            PartDesignGui__TaskThicknessParameters.setObjectName(u"PartDesignGui__TaskThicknessParameters")
        PartDesignGui__TaskThicknessParameters.resize(321, 509)
        PartDesignGui__TaskThicknessParameters.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(PartDesignGui__TaskThicknessParameters)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonRefSel = QToolButton(PartDesignGui__TaskThicknessParameters)
        self.buttonRefSel.setObjectName(u"buttonRefSel")
        self.buttonRefSel.setCheckable(True)

        self.verticalLayout.addWidget(self.buttonRefSel)

        self.listWidgetReferences = QListWidget(PartDesignGui__TaskThicknessParameters)
        self.listWidgetReferences.setObjectName(u"listWidgetReferences")
        self.listWidgetReferences.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout.addWidget(self.listWidgetReferences)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(PartDesignGui__TaskThicknessParameters)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.Value = Gui_QuantitySpinBox(PartDesignGui__TaskThicknessParameters)
        self.Value.setObjectName(u"Value")
        self.Value.setKeyboardTracking(False)
        self.Value.setProperty(u"unit", u"mm")
        self.Value.setMinimum(0.000000000000000)
        self.Value.setMaximum(999999999.000000000000000)
        self.Value.setSingleStep(0.100000000000000)
        self.Value.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.Value, 0, 1, 1, 1)

        self.label_2 = QLabel(PartDesignGui__TaskThicknessParameters)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.modeComboBox = QComboBox(PartDesignGui__TaskThicknessParameters)
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.modeComboBox.setObjectName(u"modeComboBox")

        self.gridLayout_2.addWidget(self.modeComboBox, 1, 1, 1, 1)

        self.label_3 = QLabel(PartDesignGui__TaskThicknessParameters)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.joinComboBox = QComboBox(PartDesignGui__TaskThicknessParameters)
        self.joinComboBox.addItem("")
        self.joinComboBox.addItem("")
        self.joinComboBox.setObjectName(u"joinComboBox")

        self.gridLayout_2.addWidget(self.joinComboBox, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.checkIntersection = QCheckBox(PartDesignGui__TaskThicknessParameters)
        self.checkIntersection.setObjectName(u"checkIntersection")

        self.verticalLayout.addWidget(self.checkIntersection)

        self.checkReverse = QCheckBox(PartDesignGui__TaskThicknessParameters)
        self.checkReverse.setObjectName(u"checkReverse")

        self.verticalLayout.addWidget(self.checkReverse)

        QWidget.setTabOrder(self.buttonRefSel, self.listWidgetReferences)
        QWidget.setTabOrder(self.listWidgetReferences, self.Value)
        QWidget.setTabOrder(self.Value, self.modeComboBox)
        QWidget.setTabOrder(self.modeComboBox, self.joinComboBox)
        QWidget.setTabOrder(self.joinComboBox, self.checkIntersection)
        QWidget.setTabOrder(self.checkIntersection, self.checkReverse)

        self.retranslateUi(PartDesignGui__TaskThicknessParameters)

        QMetaObject.connectSlotsByName(PartDesignGui__TaskThicknessParameters)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskThicknessParameters):
#if QT_CONFIG(tooltip)
        self.buttonRefSel.setToolTip(QCoreApplication.translate("PartDesignGui::TaskThicknessParameters", u"Toggles between selection and preview mode", None))
#endif // QT_CONFIG(tooltip)
        self.buttonRefSel.setText(QCoreApplication.translate("PartDesignGui::TaskThicknessParameters", u"Select", None))
#if QT_CONFIG(tooltip)
        self.listWidgetReferences.setToolTip(QCoreApplication.translate("PartDesignGui::TaskThicknessParameters", u"- select an item to highlight it\n"
"- double-click on an item to see the features", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("PartDesignGui::TaskThicknessParameters", u"Thickness", None))
        self.label_2.setText(QCoreApplication.translate("PartDesignGui::TaskThicknessParameters", u"Mode", None))
        self.modeComboBox.setItemText(0, QCoreApplication.translate("PartDesignGui::TaskThicknessParameters", u"Skin", None))
        self.modeComboBox.setItemText(1, QCoreApplication.translate("PartDesignGui::TaskThicknessParameters", u"Pipe", None))
        self.modeComboBox.setItemText(2, QCoreApplication.translate("PartDesignGui::TaskThicknessParameters", u"Recto verso", None))

        self.label_3.setText(QCoreApplication.translate("PartDesignGui::TaskThicknessParameters", u"Join type", None))
        self.joinComboBox.setItemText(0, QCoreApplication.translate("PartDesignGui::TaskThicknessParameters", u"Arc", None))
        self.joinComboBox.setItemText(1, QCoreApplication.translate("PartDesignGui::TaskThicknessParameters", u"Intersection", None))

        self.checkIntersection.setText(QCoreApplication.translate("PartDesignGui::TaskThicknessParameters", u"Intersection", None))
        self.checkReverse.setText(QCoreApplication.translate("PartDesignGui::TaskThicknessParameters", u"Make thickness inwards", None))
        pass
    # retranslateUi

