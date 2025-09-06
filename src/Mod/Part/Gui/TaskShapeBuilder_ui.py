# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskShapeBuilder.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_PartGui_TaskShapeBuilder(object):
    def setupUi(self, PartGui__TaskShapeBuilder):
        if not PartGui__TaskShapeBuilder.objectName():
            PartGui__TaskShapeBuilder.setObjectName(u"PartGui__TaskShapeBuilder")
        PartGui__TaskShapeBuilder.resize(200, 336)
        self.gridLayout_2 = QGridLayout(PartGui__TaskShapeBuilder)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(PartGui__TaskShapeBuilder)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButtonEdgeFromVertex = QRadioButton(self.groupBox)
        self.radioButtonEdgeFromVertex.setObjectName(u"radioButtonEdgeFromVertex")

        self.gridLayout.addWidget(self.radioButtonEdgeFromVertex, 0, 0, 1, 1)

        self.radioButtonWireFromEdge = QRadioButton(self.groupBox)
        self.radioButtonWireFromEdge.setObjectName(u"radioButtonWireFromEdge")

        self.gridLayout.addWidget(self.radioButtonWireFromEdge, 1, 0, 1, 1)

        self.radioButtonFaceFromVertex = QRadioButton(self.groupBox)
        self.radioButtonFaceFromVertex.setObjectName(u"radioButtonFaceFromVertex")

        self.gridLayout.addWidget(self.radioButtonFaceFromVertex, 2, 0, 1, 1)

        self.radioButtonFaceFromEdge = QRadioButton(self.groupBox)
        self.radioButtonFaceFromEdge.setObjectName(u"radioButtonFaceFromEdge")

        self.gridLayout.addWidget(self.radioButtonFaceFromEdge, 3, 0, 1, 1)

        self.radioButtonShellFromFace = QRadioButton(self.groupBox)
        self.radioButtonShellFromFace.setObjectName(u"radioButtonShellFromFace")

        self.gridLayout.addWidget(self.radioButtonShellFromFace, 4, 0, 1, 1)

        self.radioButtonSolidFromShell = QRadioButton(self.groupBox)
        self.radioButtonSolidFromShell.setObjectName(u"radioButtonSolidFromShell")

        self.gridLayout.addWidget(self.radioButtonSolidFromShell, 5, 0, 1, 1)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 6, 0, 1, 1)

        self.checkPlanar = QCheckBox(self.groupBox)
        self.checkPlanar.setObjectName(u"checkPlanar")

        self.gridLayout.addWidget(self.checkPlanar, 7, 0, 1, 1)

        self.checkRefine = QCheckBox(self.groupBox)
        self.checkRefine.setObjectName(u"checkRefine")
        self.checkRefine.setChecked(True)

        self.gridLayout.addWidget(self.checkRefine, 8, 0, 1, 1)

        self.checkFaces = QCheckBox(self.groupBox)
        self.checkFaces.setObjectName(u"checkFaces")

        self.gridLayout.addWidget(self.checkFaces, 9, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.selectButton = QPushButton(self.groupBox)
        self.selectButton.setObjectName(u"selectButton")

        self.horizontalLayout.addWidget(self.selectButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.createButton = QPushButton(self.groupBox)
        self.createButton.setObjectName(u"createButton")

        self.horizontalLayout.addWidget(self.createButton)


        self.gridLayout.addLayout(self.horizontalLayout, 10, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.label = QLabel(PartGui__TaskShapeBuilder)
        self.label.setObjectName(u"label")
        self.label.setText(u"TextLabel")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        QWidget.setTabOrder(self.radioButtonEdgeFromVertex, self.radioButtonFaceFromVertex)
        QWidget.setTabOrder(self.radioButtonFaceFromVertex, self.radioButtonFaceFromEdge)
        QWidget.setTabOrder(self.radioButtonFaceFromEdge, self.radioButtonShellFromFace)
        QWidget.setTabOrder(self.radioButtonShellFromFace, self.radioButtonSolidFromShell)
        QWidget.setTabOrder(self.radioButtonSolidFromShell, self.checkPlanar)
        QWidget.setTabOrder(self.checkPlanar, self.checkRefine)
        QWidget.setTabOrder(self.checkRefine, self.checkFaces)
        QWidget.setTabOrder(self.checkFaces, self.createButton)

        self.retranslateUi(PartGui__TaskShapeBuilder)

        QMetaObject.connectSlotsByName(PartGui__TaskShapeBuilder)
    # setupUi

    def retranslateUi(self, PartGui__TaskShapeBuilder):
        PartGui__TaskShapeBuilder.setWindowTitle(QCoreApplication.translate("PartGui::TaskShapeBuilder", u"Create Shape", None))
        self.groupBox.setTitle(QCoreApplication.translate("PartGui::TaskShapeBuilder", u"Create Shape", None))
        self.radioButtonEdgeFromVertex.setText(QCoreApplication.translate("PartGui::TaskShapeBuilder", u"Edge from vertices", None))
        self.radioButtonWireFromEdge.setText(QCoreApplication.translate("PartGui::TaskShapeBuilder", u"Wire from edges", None))
        self.radioButtonFaceFromVertex.setText(QCoreApplication.translate("PartGui::TaskShapeBuilder", u"Face from vertices", None))
        self.radioButtonFaceFromEdge.setText(QCoreApplication.translate("PartGui::TaskShapeBuilder", u"Face from edges", None))
        self.radioButtonShellFromFace.setText(QCoreApplication.translate("PartGui::TaskShapeBuilder", u"Shell from faces", None))
        self.radioButtonSolidFromShell.setText(QCoreApplication.translate("PartGui::TaskShapeBuilder", u"Solid from shell", None))
        self.checkPlanar.setText(QCoreApplication.translate("PartGui::TaskShapeBuilder", u"Planar", None))
        self.checkRefine.setText(QCoreApplication.translate("PartGui::TaskShapeBuilder", u"Refine shape", None))
        self.checkFaces.setText(QCoreApplication.translate("PartGui::TaskShapeBuilder", u"All faces", None))
        self.selectButton.setText(QCoreApplication.translate("PartGui::TaskShapeBuilder", u"Box Selection", None))
        self.createButton.setText(QCoreApplication.translate("PartGui::TaskShapeBuilder", u"Create", None))
    # retranslateUi

