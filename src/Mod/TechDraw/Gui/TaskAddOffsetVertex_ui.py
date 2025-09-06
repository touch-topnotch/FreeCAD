# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskAddOffsetVertex.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskAddOffsetVertex(object):
    def setupUi(self, TechDrawGui__TaskAddOffsetVertex):
        if not TechDrawGui__TaskAddOffsetVertex.objectName():
            TechDrawGui__TaskAddOffsetVertex.setObjectName(u"TechDrawGui__TaskAddOffsetVertex")
        TechDrawGui__TaskAddOffsetVertex.resize(250, 182)
        icon = QIcon()
        icon.addFile(u":/icons/actions/TechDraw_CosmeticVertex.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        TechDrawGui__TaskAddOffsetVertex.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(TechDrawGui__TaskAddOffsetVertex)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line = QFrame(TechDrawGui__TaskAddOffsetVertex)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.groupBox = QGroupBox(TechDrawGui__TaskAddOffsetVertex)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setVerticalSpacing(2)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.dSpinBoxY = QDoubleSpinBox(self.groupBox)
        self.dSpinBoxY.setObjectName(u"dSpinBoxY")
        self.dSpinBoxY.setMinimum(-900.000000000000000)
        self.dSpinBoxY.setMaximum(900.000000000000000)

        self.gridLayout_2.addWidget(self.dSpinBoxY, 1, 1, 1, 2)

        self.dSpinBoxX = QDoubleSpinBox(self.groupBox)
        self.dSpinBoxX.setObjectName(u"dSpinBoxX")
        self.dSpinBoxX.setMinimum(-900.000000000000000)
        self.dSpinBoxX.setMaximum(900.000000000000000)

        self.gridLayout_2.addWidget(self.dSpinBoxX, 0, 1, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(TechDrawGui__TaskAddOffsetVertex)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskAddOffsetVertex)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskAddOffsetVertex):
        TechDrawGui__TaskAddOffsetVertex.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskAddOffsetVertex", u"Cosmetic Vertex", None))
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("TechDrawGui::TaskAddOffsetVertex", u"Position from the view center", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("TechDrawGui::TaskAddOffsetVertex", u"Position", None))
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::TaskAddOffsetVertex", u"X-offset", None))
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::TaskAddOffsetVertex", u"Y-offset", None))
#if QT_CONFIG(tooltip)
        self.dSpinBoxX.setToolTip(QCoreApplication.translate("TechDrawGui::TaskAddOffsetVertex", u"Enter X offset value", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

