# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgProjectionOnSurface.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_PartGui_DlgProjectionOnSurface(object):
    def setupUi(self, PartGui__DlgProjectionOnSurface):
        if not PartGui__DlgProjectionOnSurface.objectName():
            PartGui__DlgProjectionOnSurface.setObjectName(u"PartGui__DlgProjectionOnSurface")
        PartGui__DlgProjectionOnSurface.resize(400, 764)
        self.verticalLayout = QVBoxLayout(PartGui__DlgProjectionOnSurface)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButtonAddProjFace = QPushButton(PartGui__DlgProjectionOnSurface)
        self.pushButtonAddProjFace.setObjectName(u"pushButtonAddProjFace")

        self.verticalLayout.addWidget(self.pushButtonAddProjFace)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonAddFace = QPushButton(PartGui__DlgProjectionOnSurface)
        self.pushButtonAddFace.setObjectName(u"pushButtonAddFace")

        self.horizontalLayout.addWidget(self.pushButtonAddFace)

        self.pushButtonAddWire = QPushButton(PartGui__DlgProjectionOnSurface)
        self.pushButtonAddWire.setObjectName(u"pushButtonAddWire")

        self.horizontalLayout.addWidget(self.pushButtonAddWire)

        self.pushButtonAddEdge = QPushButton(PartGui__DlgProjectionOnSurface)
        self.pushButtonAddEdge.setObjectName(u"pushButtonAddEdge")

        self.horizontalLayout.addWidget(self.pushButtonAddEdge)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButtonShowAll = QRadioButton(PartGui__DlgProjectionOnSurface)
        self.radioButtonShowAll.setObjectName(u"radioButtonShowAll")
        self.radioButtonShowAll.setChecked(True)

        self.horizontalLayout_5.addWidget(self.radioButtonShowAll)

        self.radioButtonFaces = QRadioButton(PartGui__DlgProjectionOnSurface)
        self.radioButtonFaces.setObjectName(u"radioButtonFaces")
        self.radioButtonFaces.setChecked(False)

        self.horizontalLayout_5.addWidget(self.radioButtonFaces)

        self.radioButtonEdges = QRadioButton(PartGui__DlgProjectionOnSurface)
        self.radioButtonEdges.setObjectName(u"radioButtonEdges")
        self.radioButtonEdges.setChecked(False)

        self.horizontalLayout_5.addWidget(self.radioButtonEdges)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelExtrudeHeigth = QLabel(PartGui__DlgProjectionOnSurface)
        self.labelExtrudeHeigth.setObjectName(u"labelExtrudeHeigth")
        self.labelExtrudeHeigth.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.labelExtrudeHeigth)

        self.doubleSpinBoxExtrudeHeight = QDoubleSpinBox(PartGui__DlgProjectionOnSurface)
        self.doubleSpinBoxExtrudeHeight.setObjectName(u"doubleSpinBoxExtrudeHeight")
        self.doubleSpinBoxExtrudeHeight.setMaximum(999.000000000000000)
        self.doubleSpinBoxExtrudeHeight.setValue(10.000000000000000)

        self.horizontalLayout_6.addWidget(self.doubleSpinBoxExtrudeHeight)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.labelDepth = QLabel(PartGui__DlgProjectionOnSurface)
        self.labelDepth.setObjectName(u"labelDepth")
        self.labelDepth.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.labelDepth)

        self.doubleSpinBoxSolidDepth = QDoubleSpinBox(PartGui__DlgProjectionOnSurface)
        self.doubleSpinBoxSolidDepth.setObjectName(u"doubleSpinBoxSolidDepth")
        self.doubleSpinBoxSolidDepth.setMinimum(-999.000000000000000)
        self.doubleSpinBoxSolidDepth.setMaximum(999.000000000000000)
        self.doubleSpinBoxSolidDepth.setValue(0.000000000000000)

        self.horizontalLayout_7.addWidget(self.doubleSpinBoxSolidDepth)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.groupBoxDir = QGroupBox(PartGui__DlgProjectionOnSurface)
        self.groupBoxDir.setObjectName(u"groupBoxDir")
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxDir)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButtonGetCurrentCamDir = QPushButton(self.groupBoxDir)
        self.pushButtonGetCurrentCamDir.setObjectName(u"pushButtonGetCurrentCamDir")

        self.verticalLayout_2.addWidget(self.pushButtonGetCurrentCamDir)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonDirX = QPushButton(self.groupBoxDir)
        self.pushButtonDirX.setObjectName(u"pushButtonDirX")

        self.horizontalLayout_2.addWidget(self.pushButtonDirX)

        self.doubleSpinBoxDirX = QDoubleSpinBox(self.groupBoxDir)
        self.doubleSpinBoxDirX.setObjectName(u"doubleSpinBoxDirX")
        self.doubleSpinBoxDirX.setEnabled(False)
        self.doubleSpinBoxDirX.setReadOnly(False)
        self.doubleSpinBoxDirX.setMinimum(-1.000000000000000)
        self.doubleSpinBoxDirX.setMaximum(1.000000000000000)
        self.doubleSpinBoxDirX.setSingleStep(0.100000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBoxDirX)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonDirY = QPushButton(self.groupBoxDir)
        self.pushButtonDirY.setObjectName(u"pushButtonDirY")

        self.horizontalLayout_3.addWidget(self.pushButtonDirY)

        self.doubleSpinBoxDirY = QDoubleSpinBox(self.groupBoxDir)
        self.doubleSpinBoxDirY.setObjectName(u"doubleSpinBoxDirY")
        self.doubleSpinBoxDirY.setEnabled(False)
        self.doubleSpinBoxDirY.setMinimum(-1.000000000000000)
        self.doubleSpinBoxDirY.setMaximum(1.000000000000000)
        self.doubleSpinBoxDirY.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBoxDirY)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButtonDirZ = QPushButton(self.groupBoxDir)
        self.pushButtonDirZ.setObjectName(u"pushButtonDirZ")

        self.horizontalLayout_4.addWidget(self.pushButtonDirZ)

        self.doubleSpinBoxDirZ = QDoubleSpinBox(self.groupBoxDir)
        self.doubleSpinBoxDirZ.setObjectName(u"doubleSpinBoxDirZ")
        self.doubleSpinBoxDirZ.setEnabled(False)
        self.doubleSpinBoxDirZ.setMinimum(-1.000000000000000)
        self.doubleSpinBoxDirZ.setMaximum(1.000000000000000)
        self.doubleSpinBoxDirZ.setSingleStep(0.100000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBoxDirZ)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.groupBoxDir)


        self.retranslateUi(PartGui__DlgProjectionOnSurface)

        QMetaObject.connectSlotsByName(PartGui__DlgProjectionOnSurface)
    # setupUi

    def retranslateUi(self, PartGui__DlgProjectionOnSurface):
        PartGui__DlgProjectionOnSurface.setWindowTitle(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Project on Surface", None))
        self.pushButtonAddProjFace.setText(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Select Projection Surface", None))
        self.pushButtonAddFace.setText(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Add Face", None))
        self.pushButtonAddWire.setText(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Add Wire", None))
        self.pushButtonAddEdge.setText(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Add Edge", None))
        self.radioButtonShowAll.setText(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Show all", None))
        self.radioButtonFaces.setText(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Show faces", None))
        self.radioButtonEdges.setText(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Show edges", None))
        self.labelExtrudeHeigth.setText(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Extrude height", None))
        self.labelDepth.setText(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Solid depth", None))
        self.groupBoxDir.setTitle(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Direction", None))
        self.pushButtonGetCurrentCamDir.setText(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Get Current Camera Direction", None))
        self.pushButtonDirX.setText(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"X", None))
        self.pushButtonDirY.setText(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Y", None))
        self.pushButtonDirZ.setText(QCoreApplication.translate("PartGui::DlgProjectionOnSurface", u"Z", None))
    # retranslateUi

