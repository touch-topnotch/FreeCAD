# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskLinkDim.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_TechDrawGui_TaskLinkDim(object):
    def setupUi(self, TechDrawGui__TaskLinkDim):
        if not TechDrawGui__TaskLinkDim.objectName():
            TechDrawGui__TaskLinkDim.setObjectName(u"TechDrawGui__TaskLinkDim")
        TechDrawGui__TaskLinkDim.resize(400, 472)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskLinkDim.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskLinkDim.setSizePolicy(sizePolicy)
        TechDrawGui__TaskLinkDim.setMinimumSize(QSize(250, 0))
        self.verticalLayout_2 = QVBoxLayout(TechDrawGui__TaskLinkDim)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(TechDrawGui__TaskLinkDim)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lblLinkThis = QLabel(self.frame)
        self.lblLinkThis.setObjectName(u"lblLinkThis")

        self.horizontalLayout_3.addWidget(self.lblLinkThis)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblFeature = QLabel(self.frame)
        self.lblFeature.setObjectName(u"lblFeature")

        self.gridLayout.addWidget(self.lblFeature, 0, 0, 1, 1)

        self.leFeature1 = QLineEdit(self.frame)
        self.leFeature1.setObjectName(u"leFeature1")
        self.leFeature1.setFocusPolicy(Qt.NoFocus)
        self.leFeature1.setStyleSheet(u"color: rgb(120, 120, 120);")
        self.leFeature1.setReadOnly(True)

        self.gridLayout.addWidget(self.leFeature1, 0, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.leGeometry1 = QLineEdit(self.frame)
        self.leGeometry1.setObjectName(u"leGeometry1")
        self.leGeometry1.setFocusPolicy(Qt.NoFocus)
        self.leGeometry1.setStyleSheet(u"color: rgb(120, 120, 120);")
        self.leGeometry1.setReadOnly(True)

        self.gridLayout.addWidget(self.leGeometry1, 1, 1, 1, 1)

        self.lblGeometry = QLabel(self.frame)
        self.lblGeometry.setObjectName(u"lblGeometry")

        self.gridLayout.addWidget(self.lblGeometry, 2, 0, 1, 1)

        self.leFeature2 = QLineEdit(self.frame)
        self.leFeature2.setObjectName(u"leFeature2")
        self.leFeature2.setFocusPolicy(Qt.NoFocus)
        self.leFeature2.setStyleSheet(u"color: rgb(120, 120, 120);")
        self.leFeature2.setReadOnly(True)

        self.gridLayout.addWidget(self.leFeature2, 2, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.leGeometry2 = QLineEdit(self.frame)
        self.leGeometry2.setObjectName(u"leGeometry2")
        self.leGeometry2.setFocusPolicy(Qt.NoFocus)
        self.leGeometry2.setStyleSheet(u"color: rgb(120, 120, 120);")
        self.leGeometry2.setReadOnly(True)

        self.gridLayout.addWidget(self.leGeometry2, 3, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lblToThese = QLabel(self.frame)
        self.lblToThese.setObjectName(u"lblToThese")

        self.verticalLayout_4.addWidget(self.lblToThese)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.selector = Gui_ActionSelector(self.frame)
        self.selector.setObjectName(u"selector")

        self.horizontalLayout_2.addWidget(self.selector)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(TechDrawGui__TaskLinkDim)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskLinkDim)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskLinkDim):
        TechDrawGui__TaskLinkDim.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskLinkDim", u"Link Dimension", None))
        self.lblLinkThis.setText(QCoreApplication.translate("TechDrawGui::TaskLinkDim", u"Link this 3D geometry", None))
        self.lblFeature.setText(QCoreApplication.translate("TechDrawGui::TaskLinkDim", u"Feature1", None))
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskLinkDim", u"Geometry1", None))
        self.lblGeometry.setText(QCoreApplication.translate("TechDrawGui::TaskLinkDim", u"Feature2", None))
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::TaskLinkDim", u"Geometry2", None))
        self.lblToThese.setText(QCoreApplication.translate("TechDrawGui::TaskLinkDim", u"To these dimensions", None))
    # retranslateUi

