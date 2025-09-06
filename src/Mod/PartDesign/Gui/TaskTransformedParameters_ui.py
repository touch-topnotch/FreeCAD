# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskTransformedParameters.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QCheckBox,
    QHBoxLayout, QListWidget, QListWidgetItem, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_PartDesignGui_TaskTransformedParameters(object):
    def setupUi(self, PartDesignGui__TaskTransformedParameters):
        if not PartDesignGui__TaskTransformedParameters.objectName():
            PartDesignGui__TaskTransformedParameters.setObjectName(u"PartDesignGui__TaskTransformedParameters")
        PartDesignGui__TaskTransformedParameters.resize(297, 248)
        PartDesignGui__TaskTransformedParameters.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(PartDesignGui__TaskTransformedParameters)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(PartDesignGui__TaskTransformedParameters)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.radioTransformBody = QRadioButton(self.widget)
        self.buttonGroupMode = QButtonGroup(PartDesignGui__TaskTransformedParameters)
        self.buttonGroupMode.setObjectName(u"buttonGroupMode")
        self.buttonGroupMode.addButton(self.radioTransformBody)
        self.radioTransformBody.setObjectName(u"radioTransformBody")
        self.radioTransformBody.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioTransformBody)

        self.radioTransformToolShapes = QRadioButton(self.widget)
        self.buttonGroupMode.addButton(self.radioTransformToolShapes)
        self.radioTransformToolShapes.setObjectName(u"radioTransformToolShapes")

        self.verticalLayout_3.addWidget(self.radioTransformToolShapes)


        self.verticalLayout.addWidget(self.widget)

        self.groupFeatureList = QWidget(PartDesignGui__TaskTransformedParameters)
        self.groupFeatureList.setObjectName(u"groupFeatureList")
        self.verticalLayout_2 = QVBoxLayout(self.groupFeatureList)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonAddFeature = QPushButton(self.groupFeatureList)
        self.buttonAddFeature.setObjectName(u"buttonAddFeature")
        self.buttonAddFeature.setCheckable(True)

        self.horizontalLayout.addWidget(self.buttonAddFeature)

        self.buttonRemoveFeature = QPushButton(self.groupFeatureList)
        self.buttonRemoveFeature.setObjectName(u"buttonRemoveFeature")
        self.buttonRemoveFeature.setCheckable(True)

        self.horizontalLayout.addWidget(self.buttonRemoveFeature)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.listWidgetFeatures = QListWidget(self.groupFeatureList)
        self.listWidgetFeatures.setObjectName(u"listWidgetFeatures")
        self.listWidgetFeatures.setMaximumSize(QSize(16777215, 120))
        self.listWidgetFeatures.setDragDropMode(QAbstractItemView.InternalMove)

        self.verticalLayout_2.addWidget(self.listWidgetFeatures)


        self.verticalLayout.addWidget(self.groupFeatureList)

        self.featureUI = QWidget(PartDesignGui__TaskTransformedParameters)
        self.featureUI.setObjectName(u"featureUI")

        self.verticalLayout.addWidget(self.featureUI)

        self.checkBoxUpdateView = QCheckBox(PartDesignGui__TaskTransformedParameters)
        self.checkBoxUpdateView.setObjectName(u"checkBoxUpdateView")
        self.checkBoxUpdateView.setChecked(True)

        self.verticalLayout.addWidget(self.checkBoxUpdateView)

        QWidget.setTabOrder(self.radioTransformBody, self.radioTransformToolShapes)
        QWidget.setTabOrder(self.radioTransformToolShapes, self.buttonAddFeature)
        QWidget.setTabOrder(self.buttonAddFeature, self.buttonRemoveFeature)
        QWidget.setTabOrder(self.buttonRemoveFeature, self.listWidgetFeatures)
        QWidget.setTabOrder(self.listWidgetFeatures, self.checkBoxUpdateView)

        self.retranslateUi(PartDesignGui__TaskTransformedParameters)

        QMetaObject.connectSlotsByName(PartDesignGui__TaskTransformedParameters)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskTransformedParameters):
        self.radioTransformBody.setText(QCoreApplication.translate("PartDesignGui::TaskTransformedParameters", u"Transform body", None))
        self.radioTransformToolShapes.setText(QCoreApplication.translate("PartDesignGui::TaskTransformedParameters", u"Transform tool shapes", None))
        self.buttonAddFeature.setText(QCoreApplication.translate("PartDesignGui::TaskTransformedParameters", u"Add Feature", None))
        self.buttonRemoveFeature.setText(QCoreApplication.translate("PartDesignGui::TaskTransformedParameters", u"Remove Feature", None))
#if QT_CONFIG(tooltip)
        self.listWidgetFeatures.setToolTip(QCoreApplication.translate("PartDesignGui::TaskTransformedParameters", u"List can be reordered by dragging", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUpdateView.setText(QCoreApplication.translate("PartDesignGui::TaskTransformedParameters", u"Recompute on change", None))
        pass
    # retranslateUi

