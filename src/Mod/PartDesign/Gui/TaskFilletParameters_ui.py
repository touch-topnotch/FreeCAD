# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskFilletParameters.ui'
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
    QLabel, QListWidget, QListWidgetItem, QSizePolicy,
    QToolButton, QVBoxLayout, QWidget)

class Ui_PartDesignGui_TaskFilletParameters(object):
    def setupUi(self, PartDesignGui__TaskFilletParameters):
        if not PartDesignGui__TaskFilletParameters.objectName():
            PartDesignGui__TaskFilletParameters.setObjectName(u"PartDesignGui__TaskFilletParameters")
        PartDesignGui__TaskFilletParameters.resize(232, 181)
        PartDesignGui__TaskFilletParameters.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(PartDesignGui__TaskFilletParameters)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonRefSel = QToolButton(PartDesignGui__TaskFilletParameters)
        self.buttonRefSel.setObjectName(u"buttonRefSel")
        self.buttonRefSel.setCheckable(True)

        self.verticalLayout.addWidget(self.buttonRefSel)

        self.listWidgetReferences = QListWidget(PartDesignGui__TaskFilletParameters)
        self.listWidgetReferences.setObjectName(u"listWidgetReferences")
        self.listWidgetReferences.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.listWidgetReferences)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(PartDesignGui__TaskFilletParameters)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.filletRadius = Gui_QuantitySpinBox(PartDesignGui__TaskFilletParameters)
        self.filletRadius.setObjectName(u"filletRadius")
        self.filletRadius.setKeyboardTracking(False)

        self.horizontalLayout_2.addWidget(self.filletRadius)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.checkBoxUseAllEdges = QCheckBox(PartDesignGui__TaskFilletParameters)
        self.checkBoxUseAllEdges.setObjectName(u"checkBoxUseAllEdges")

        self.verticalLayout.addWidget(self.checkBoxUseAllEdges)

        QWidget.setTabOrder(self.buttonRefSel, self.listWidgetReferences)
        QWidget.setTabOrder(self.listWidgetReferences, self.filletRadius)
        QWidget.setTabOrder(self.filletRadius, self.checkBoxUseAllEdges)

        self.retranslateUi(PartDesignGui__TaskFilletParameters)

        QMetaObject.connectSlotsByName(PartDesignGui__TaskFilletParameters)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskFilletParameters):
#if QT_CONFIG(tooltip)
        self.buttonRefSel.setToolTip(QCoreApplication.translate("PartDesignGui::TaskFilletParameters", u"Toggles between selection and preview mode", None))
#endif // QT_CONFIG(tooltip)
        self.buttonRefSel.setText(QCoreApplication.translate("PartDesignGui::TaskFilletParameters", u"Select", None))
#if QT_CONFIG(tooltip)
        self.listWidgetReferences.setToolTip(QCoreApplication.translate("PartDesignGui::TaskFilletParameters", u"- select an item to highlight it\n"
"- double-click on an item to see the fillets", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("PartDesignGui::TaskFilletParameters", u"Radius", None))
        self.checkBoxUseAllEdges.setText(QCoreApplication.translate("PartDesignGui::TaskFilletParameters", u"Use all edges", None))
        pass
    # retranslateUi

