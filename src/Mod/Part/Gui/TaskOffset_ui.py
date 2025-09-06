# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskOffset.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_PartGui_TaskOffset(object):
    def setupUi(self, PartGui__TaskOffset):
        if not PartGui__TaskOffset.objectName():
            PartGui__TaskOffset.setObjectName(u"PartGui__TaskOffset")
        PartGui__TaskOffset.resize(264, 244)
        self.gridLayout = QGridLayout(PartGui__TaskOffset)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelOffset = QLabel(PartGui__TaskOffset)
        self.labelOffset.setObjectName(u"labelOffset")

        self.gridLayout.addWidget(self.labelOffset, 0, 0, 1, 1)

        self.spinOffset = Gui_QuantitySpinBox(PartGui__TaskOffset)
        self.spinOffset.setObjectName(u"spinOffset")
        self.spinOffset.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.spinOffset, 0, 2, 1, 1)

        self.label_2 = QLabel(PartGui__TaskOffset)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.modeType = QComboBox(PartGui__TaskOffset)
        self.modeType.addItem("")
        self.modeType.addItem("")
        self.modeType.addItem("")
        self.modeType.setObjectName(u"modeType")

        self.gridLayout.addWidget(self.modeType, 1, 2, 1, 1)

        self.label_3 = QLabel(PartGui__TaskOffset)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.joinType = QComboBox(PartGui__TaskOffset)
        self.joinType.addItem("")
        self.joinType.addItem("")
        self.joinType.addItem("")
        self.joinType.setObjectName(u"joinType")

        self.gridLayout.addWidget(self.joinType, 2, 2, 1, 1)

        self.intersection = QCheckBox(PartGui__TaskOffset)
        self.intersection.setObjectName(u"intersection")

        self.gridLayout.addWidget(self.intersection, 3, 0, 1, 1)

        self.selfIntersection = QCheckBox(PartGui__TaskOffset)
        self.selfIntersection.setObjectName(u"selfIntersection")

        self.gridLayout.addWidget(self.selfIntersection, 4, 0, 1, 2)

        self.fillOffset = QCheckBox(PartGui__TaskOffset)
        self.fillOffset.setObjectName(u"fillOffset")

        self.gridLayout.addWidget(self.fillOffset, 5, 0, 1, 1)

        self.labelFaces = QLabel(PartGui__TaskOffset)
        self.labelFaces.setObjectName(u"labelFaces")
        self.labelFaces.setText(u"")

        self.gridLayout.addWidget(self.labelFaces, 6, 0, 1, 3)

        self.facesButton = QPushButton(PartGui__TaskOffset)
        self.facesButton.setObjectName(u"facesButton")
        self.facesButton.setCheckable(True)

        self.gridLayout.addWidget(self.facesButton, 7, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(152, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 7, 1, 1, 2)

        self.line = QFrame(PartGui__TaskOffset)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 8, 0, 1, 3)

        self.updateView = QCheckBox(PartGui__TaskOffset)
        self.updateView.setObjectName(u"updateView")
        self.updateView.setChecked(True)

        self.gridLayout.addWidget(self.updateView, 9, 0, 1, 1)

        QWidget.setTabOrder(self.spinOffset, self.modeType)
        QWidget.setTabOrder(self.modeType, self.joinType)
        QWidget.setTabOrder(self.joinType, self.intersection)
        QWidget.setTabOrder(self.intersection, self.selfIntersection)

        self.retranslateUi(PartGui__TaskOffset)

        QMetaObject.connectSlotsByName(PartGui__TaskOffset)
    # setupUi

    def retranslateUi(self, PartGui__TaskOffset):
        PartGui__TaskOffset.setWindowTitle(QCoreApplication.translate("PartGui::TaskOffset", u"Offset", None))
        self.labelOffset.setText(QCoreApplication.translate("PartGui::TaskOffset", u"Offset", None))
        self.label_2.setText(QCoreApplication.translate("PartGui::TaskOffset", u"Mode", None))
        self.modeType.setItemText(0, QCoreApplication.translate("PartGui::TaskOffset", u"Skin", None))
        self.modeType.setItemText(1, QCoreApplication.translate("PartGui::TaskOffset", u"Pipe", None))
        self.modeType.setItemText(2, QCoreApplication.translate("PartGui::TaskOffset", u"Recto verso", None))

        self.label_3.setText(QCoreApplication.translate("PartGui::TaskOffset", u"Join type", None))
        self.joinType.setItemText(0, QCoreApplication.translate("PartGui::TaskOffset", u"Arc", None))
        self.joinType.setItemText(1, QCoreApplication.translate("PartGui::TaskOffset", u"Tangent", None))
        self.joinType.setItemText(2, QCoreApplication.translate("PartGui::TaskOffset", u"Intersection", None))

        self.intersection.setText(QCoreApplication.translate("PartGui::TaskOffset", u"Intersection", None))
        self.selfIntersection.setText(QCoreApplication.translate("PartGui::TaskOffset", u"Self-intersection", None))
        self.fillOffset.setText(QCoreApplication.translate("PartGui::TaskOffset", u"Fill offset", None))
        self.facesButton.setText(QCoreApplication.translate("PartGui::TaskOffset", u"Faces", None))
        self.updateView.setText(QCoreApplication.translate("PartGui::TaskOffset", u"Update view", None))
    # retranslateUi

