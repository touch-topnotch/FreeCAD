# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskDraftParameters.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_PartDesignGui_TaskDraftParameters(object):
    def setupUi(self, PartDesignGui__TaskDraftParameters):
        if not PartDesignGui__TaskDraftParameters.objectName():
            PartDesignGui__TaskDraftParameters.setObjectName(u"PartDesignGui__TaskDraftParameters")
        PartDesignGui__TaskDraftParameters.resize(257, 285)
        PartDesignGui__TaskDraftParameters.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(PartDesignGui__TaskDraftParameters)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonRefSel = QToolButton(PartDesignGui__TaskDraftParameters)
        self.buttonRefSel.setObjectName(u"buttonRefSel")
        self.buttonRefSel.setCheckable(True)

        self.verticalLayout.addWidget(self.buttonRefSel)

        self.listWidgetReferences = QListWidget(PartDesignGui__TaskDraftParameters)
        self.listWidgetReferences.setObjectName(u"listWidgetReferences")
        self.listWidgetReferences.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.listWidgetReferences)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(PartDesignGui__TaskDraftParameters)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.draftAngle = Gui_QuantitySpinBox(PartDesignGui__TaskDraftParameters)
        self.draftAngle.setObjectName(u"draftAngle")
        self.draftAngle.setKeyboardTracking(False)
        self.draftAngle.setProperty(u"unit", u"deg")
        self.draftAngle.setMinimum(0.000000000000000)
        self.draftAngle.setMaximum(89.999999999999986)
        self.draftAngle.setSingleStep(1.000000000000000)
        self.draftAngle.setValue(10.000000000000000)

        self.horizontalLayout_2.addWidget(self.draftAngle)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buttonPlane = QToolButton(PartDesignGui__TaskDraftParameters)
        self.buttonPlane.setObjectName(u"buttonPlane")
        self.buttonPlane.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.buttonPlane)

        self.linePlane = QLineEdit(PartDesignGui__TaskDraftParameters)
        self.linePlane.setObjectName(u"linePlane")

        self.horizontalLayout_3.addWidget(self.linePlane)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttonLine = QToolButton(PartDesignGui__TaskDraftParameters)
        self.buttonLine.setObjectName(u"buttonLine")
        self.buttonLine.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.buttonLine)

        self.lineLine = QLineEdit(PartDesignGui__TaskDraftParameters)
        self.lineLine.setObjectName(u"lineLine")

        self.horizontalLayout_4.addWidget(self.lineLine)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.checkReverse = QCheckBox(PartDesignGui__TaskDraftParameters)
        self.checkReverse.setObjectName(u"checkReverse")

        self.verticalLayout.addWidget(self.checkReverse)

        self.buttonRefSel.raise_()
        self.checkReverse.raise_()
        self.listWidgetReferences.raise_()
        QWidget.setTabOrder(self.buttonRefSel, self.listWidgetReferences)
        QWidget.setTabOrder(self.listWidgetReferences, self.draftAngle)
        QWidget.setTabOrder(self.draftAngle, self.buttonPlane)
        QWidget.setTabOrder(self.buttonPlane, self.linePlane)
        QWidget.setTabOrder(self.linePlane, self.buttonLine)
        QWidget.setTabOrder(self.buttonLine, self.lineLine)
        QWidget.setTabOrder(self.lineLine, self.checkReverse)

        self.retranslateUi(PartDesignGui__TaskDraftParameters)

        QMetaObject.connectSlotsByName(PartDesignGui__TaskDraftParameters)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskDraftParameters):
#if QT_CONFIG(tooltip)
        self.buttonRefSel.setToolTip(QCoreApplication.translate("PartDesignGui::TaskDraftParameters", u"Toggles between selection and preview mode", None))
#endif // QT_CONFIG(tooltip)
        self.buttonRefSel.setText(QCoreApplication.translate("PartDesignGui::TaskDraftParameters", u"Select", None))
#if QT_CONFIG(tooltip)
        self.listWidgetReferences.setToolTip(QCoreApplication.translate("PartDesignGui::TaskDraftParameters", u"- select an item to highlight it\n"
"- double-click on an item to see the drafts", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("PartDesignGui::TaskDraftParameters", u"Draft angle", None))
        self.buttonPlane.setText(QCoreApplication.translate("PartDesignGui::TaskDraftParameters", u"Neutral Plane", None))
        self.buttonLine.setText(QCoreApplication.translate("PartDesignGui::TaskDraftParameters", u"Pull Direction", None))
        self.checkReverse.setText(QCoreApplication.translate("PartDesignGui::TaskDraftParameters", u"Reverse pull direction", None))
        pass
    # retranslateUi

