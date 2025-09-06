# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskChamferParameters.ui'
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
    QFormLayout, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_PartDesignGui_TaskChamferParameters(object):
    def setupUi(self, PartDesignGui__TaskChamferParameters):
        if not PartDesignGui__TaskChamferParameters.objectName():
            PartDesignGui__TaskChamferParameters.setObjectName(u"PartDesignGui__TaskChamferParameters")
        PartDesignGui__TaskChamferParameters.resize(263, 254)
        PartDesignGui__TaskChamferParameters.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(PartDesignGui__TaskChamferParameters)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonRefSel = QToolButton(PartDesignGui__TaskChamferParameters)
        self.buttonRefSel.setObjectName(u"buttonRefSel")
        self.buttonRefSel.setCheckable(True)

        self.verticalLayout.addWidget(self.buttonRefSel)

        self.listWidgetReferences = QListWidget(PartDesignGui__TaskChamferParameters)
        self.listWidgetReferences.setObjectName(u"listWidgetReferences")
        self.listWidgetReferences.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.listWidgetReferences)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.typeLabel = QLabel(PartDesignGui__TaskChamferParameters)
        self.typeLabel.setObjectName(u"typeLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.typeLabel)

        self.chamferType = QComboBox(PartDesignGui__TaskChamferParameters)
        self.chamferType.addItem("")
        self.chamferType.addItem("")
        self.chamferType.addItem("")
        self.chamferType.setObjectName(u"chamferType")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.chamferType)


        self.horizontalLayout_2.addLayout(self.formLayout)

        self.flipDirection = QToolButton(PartDesignGui__TaskChamferParameters)
        self.flipDirection.setObjectName(u"flipDirection")
        self.flipDirection.setEnabled(False)
        icon = QIcon()
        icon.addFile(u":/icons/PartDesign_Flip_Direction.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.flipDirection.setIcon(icon)
        self.flipDirection.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.flipDirection)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.sizeLabel = QLabel(PartDesignGui__TaskChamferParameters)
        self.sizeLabel.setObjectName(u"sizeLabel")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.sizeLabel)

        self.chamferSize = Gui_QuantitySpinBox(PartDesignGui__TaskChamferParameters)
        self.chamferSize.setObjectName(u"chamferSize")
        self.chamferSize.setKeyboardTracking(False)
        self.chamferSize.setValue(1.000000000000000)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.chamferSize)


        self.verticalLayout.addLayout(self.formLayout_4)

        self.checkBoxUseAllEdges = QCheckBox(PartDesignGui__TaskChamferParameters)
        self.checkBoxUseAllEdges.setObjectName(u"checkBoxUseAllEdges")

        self.verticalLayout.addWidget(self.checkBoxUseAllEdges)

        self.stackedWidget = QStackedWidget(PartDesignGui__TaskChamferParameters)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.formLayout_2 = QFormLayout(self.page_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.size2Label = QLabel(self.page_2)
        self.size2Label.setObjectName(u"size2Label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.size2Label)

        self.chamferSize2 = Gui_QuantitySpinBox(self.page_2)
        self.chamferSize2.setObjectName(u"chamferSize2")
        self.chamferSize2.setKeyboardTracking(False)
        self.chamferSize2.setValue(1.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.chamferSize2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.formLayout_3 = QFormLayout(self.page_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.angleLabel = QLabel(self.page_3)
        self.angleLabel.setObjectName(u"angleLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.angleLabel)

        self.chamferAngle = Gui_QuantitySpinBox(self.page_3)
        self.chamferAngle.setObjectName(u"chamferAngle")
        self.chamferAngle.setKeyboardTracking(False)
        self.chamferAngle.setMinimum(0.000000000000000)
        self.chamferAngle.setMaximum(180.000000000000000)
        self.chamferAngle.setSingleStep(1.000000000000000)
        self.chamferAngle.setValue(45.000000000000000)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.chamferAngle)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget)

        QWidget.setTabOrder(self.buttonRefSel, self.listWidgetReferences)
        QWidget.setTabOrder(self.listWidgetReferences, self.chamferType)
        QWidget.setTabOrder(self.chamferType, self.flipDirection)
        QWidget.setTabOrder(self.flipDirection, self.chamferSize)
        QWidget.setTabOrder(self.chamferSize, self.checkBoxUseAllEdges)
        QWidget.setTabOrder(self.checkBoxUseAllEdges, self.chamferSize2)
        QWidget.setTabOrder(self.chamferSize2, self.chamferAngle)

        self.retranslateUi(PartDesignGui__TaskChamferParameters)
        self.chamferType.currentIndexChanged.connect(self.stackedWidget.setCurrentIndex)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PartDesignGui__TaskChamferParameters)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskChamferParameters):
#if QT_CONFIG(tooltip)
        self.buttonRefSel.setToolTip(QCoreApplication.translate("PartDesignGui::TaskChamferParameters", u"Toggles between selection and preview mode", None))
#endif // QT_CONFIG(tooltip)
        self.buttonRefSel.setText(QCoreApplication.translate("PartDesignGui::TaskChamferParameters", u"Select", None))
#if QT_CONFIG(tooltip)
        self.listWidgetReferences.setToolTip(QCoreApplication.translate("PartDesignGui::TaskChamferParameters", u"- select an item to highlight it\n"
"- double-click on an item to see the chamfers", None))
#endif // QT_CONFIG(tooltip)
        self.typeLabel.setText(QCoreApplication.translate("PartDesignGui::TaskChamferParameters", u"Type", None))
        self.chamferType.setItemText(0, QCoreApplication.translate("PartDesignGui::TaskChamferParameters", u"Equal distance", None))
        self.chamferType.setItemText(1, QCoreApplication.translate("PartDesignGui::TaskChamferParameters", u"Two distances", None))
        self.chamferType.setItemText(2, QCoreApplication.translate("PartDesignGui::TaskChamferParameters", u"Distance and angle", None))

#if QT_CONFIG(tooltip)
        self.flipDirection.setToolTip(QCoreApplication.translate("PartDesignGui::TaskChamferParameters", u"Flips the direction", None))
#endif // QT_CONFIG(tooltip)
        self.flipDirection.setText("")
        self.sizeLabel.setText(QCoreApplication.translate("PartDesignGui::TaskChamferParameters", u"Size", None))
        self.checkBoxUseAllEdges.setText(QCoreApplication.translate("PartDesignGui::TaskChamferParameters", u"Use all edges", None))
        self.size2Label.setText(QCoreApplication.translate("PartDesignGui::TaskChamferParameters", u"Size 2", None))
        self.angleLabel.setText(QCoreApplication.translate("PartDesignGui::TaskChamferParameters", u"Angle", None))
        pass
    # retranslateUi

