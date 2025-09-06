# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskCosVertex.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskCosVertex(object):
    def setupUi(self, TechDrawGui__TaskCosVertex):
        if not TechDrawGui__TaskCosVertex.objectName():
            TechDrawGui__TaskCosVertex.setObjectName(u"TechDrawGui__TaskCosVertex")
        TechDrawGui__TaskCosVertex.resize(250, 167)
        icon = QIcon()
        icon.addFile(u":/icons/actions/TechDraw_CosmeticVertex.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        TechDrawGui__TaskCosVertex.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(TechDrawGui__TaskCosVertex)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(TechDrawGui__TaskCosVertex)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.leBaseView = QLineEdit(TechDrawGui__TaskCosVertex)
        self.leBaseView.setObjectName(u"leBaseView")
        self.leBaseView.setEnabled(False)
        self.leBaseView.setMouseTracking(False)
        self.leBaseView.setFocusPolicy(Qt.NoFocus)
        self.leBaseView.setAcceptDrops(False)

        self.gridLayout.addWidget(self.leBaseView, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pbTracker = QPushButton(TechDrawGui__TaskCosVertex)
        self.pbTracker.setObjectName(u"pbTracker")

        self.horizontalLayout.addWidget(self.pbTracker)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line = QFrame(TechDrawGui__TaskCosVertex)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.groupBox = QGroupBox(TechDrawGui__TaskCosVertex)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"X")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.dsbX = Gui_QuantitySpinBox(self.groupBox)
        self.dsbX.setObjectName(u"dsbX")
        self.dsbX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbX.setMinimum(-2147483647.000000000000000)
        self.dsbX.setMaximum(2147483647.000000000000000)
        self.dsbX.setProperty(u"decimals", 4)

        self.gridLayout_2.addWidget(self.dsbX, 0, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"Y")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 2)

        self.dsbY = Gui_QuantitySpinBox(self.groupBox)
        self.dsbY.setObjectName(u"dsbY")
        self.dsbY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbY.setMinimum(-2147483647.000000000000000)
        self.dsbY.setMaximum(2147483647.000000000000000)
        self.dsbY.setProperty(u"decimals", 4)

        self.gridLayout_2.addWidget(self.dsbY, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(TechDrawGui__TaskCosVertex)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskCosVertex)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskCosVertex):
        TechDrawGui__TaskCosVertex.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskCosVertex", u"Cosmetic Vertex", None))
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::TaskCosVertex", u"Base view", None))
        self.pbTracker.setText(QCoreApplication.translate("TechDrawGui::TaskCosVertex", u"Point Picker", None))
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCosVertex", u"Position from the view center", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("TechDrawGui::TaskCosVertex", u"Position", None))
    # retranslateUi

