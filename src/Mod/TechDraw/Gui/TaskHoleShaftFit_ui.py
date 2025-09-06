# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskHoleShaftFit.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskSurfaceFinishSymbols(object):
    def setupUi(self, TechDrawGui__TaskSurfaceFinishSymbols):
        if not TechDrawGui__TaskSurfaceFinishSymbols.objectName():
            TechDrawGui__TaskSurfaceFinishSymbols.setObjectName(u"TechDrawGui__TaskSurfaceFinishSymbols")
        TechDrawGui__TaskSurfaceFinishSymbols.setEnabled(True)
        TechDrawGui__TaskSurfaceFinishSymbols.resize(274, 162)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskSurfaceFinishSymbols.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskSurfaceFinishSymbols.setSizePolicy(sizePolicy)
        TechDrawGui__TaskSurfaceFinishSymbols.setMinimumSize(QSize(250, 0))
        self.verticalLayout = QVBoxLayout(TechDrawGui__TaskSurfaceFinishSymbols)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.rbHoleBase = QRadioButton(TechDrawGui__TaskSurfaceFinishSymbols)
        self.rbHoleBase.setObjectName(u"rbHoleBase")
        self.rbHoleBase.setChecked(True)

        self.gridLayout.addWidget(self.rbHoleBase, 0, 0, 1, 1)

        self.rbShaftBase = QRadioButton(TechDrawGui__TaskSurfaceFinishSymbols)
        self.rbShaftBase.setObjectName(u"rbShaftBase")

        self.gridLayout.addWidget(self.rbShaftBase, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cbField = QComboBox(TechDrawGui__TaskSurfaceFinishSymbols)
        self.cbField.addItem(u"c11")
        self.cbField.addItem(u"f7")
        self.cbField.addItem(u"h6")
        self.cbField.addItem(u"h7")
        self.cbField.addItem(u"h9")
        self.cbField.addItem(u"h9")
        self.cbField.addItem(u"h9")
        self.cbField.addItem(u"h6")
        self.cbField.addItem(u"h6")
        self.cbField.addItem(u"h6")
        self.cbField.addItem(u"h6")
        self.cbField.addItem(u"h6")
        self.cbField.addItem(u"k6")
        self.cbField.addItem(u"n6")
        self.cbField.addItem(u"r6")
        self.cbField.addItem(u"s6")
        self.cbField.setObjectName(u"cbField")
        self.cbField.setEnabled(True)

        self.gridLayout_2.addWidget(self.cbField, 0, 2, 1, 1)

        self.lbFitType = QLabel(TechDrawGui__TaskSurfaceFinishSymbols)
        self.lbFitType.setObjectName(u"lbFitType")

        self.gridLayout_2.addWidget(self.lbFitType, 0, 3, 1, 1)

        self.lbBaseField = QLabel(TechDrawGui__TaskSurfaceFinishSymbols)
        self.lbBaseField.setObjectName(u"lbBaseField")
        self.lbBaseField.setText(u"H11/")

        self.gridLayout_2.addWidget(self.lbBaseField, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.retranslateUi(TechDrawGui__TaskSurfaceFinishSymbols)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskSurfaceFinishSymbols)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskSurfaceFinishSymbols):
        TechDrawGui__TaskSurfaceFinishSymbols.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskSurfaceFinishSymbols", u"Hole/Shaft Fit ISO 286", None))
        self.rbHoleBase.setText(QCoreApplication.translate("TechDrawGui::TaskSurfaceFinishSymbols", u"Shaft fit", None))
        self.rbShaftBase.setText(QCoreApplication.translate("TechDrawGui::TaskSurfaceFinishSymbols", u"Hole fit", None))

        self.lbFitType.setText(QCoreApplication.translate("TechDrawGui::TaskSurfaceFinishSymbols", u"Loose fit", None))
    # retranslateUi

