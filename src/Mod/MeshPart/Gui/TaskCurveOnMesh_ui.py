# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskCurveOnMesh.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_MeshPartGui_TaskCurveOnMesh(object):
    def setupUi(self, MeshPartGui__TaskCurveOnMesh):
        if not MeshPartGui__TaskCurveOnMesh.objectName():
            MeshPartGui__TaskCurveOnMesh.setObjectName(u"MeshPartGui__TaskCurveOnMesh")
        MeshPartGui__TaskCurveOnMesh.resize(507, 637)
        self.gridLayout_3 = QGridLayout(MeshPartGui__TaskCurveOnMesh)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_3 = QGroupBox(MeshPartGui__TaskCurveOnMesh)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_instructions = QLabel(self.groupBox_3)
        self.lb_instructions.setObjectName(u"lb_instructions")
        self.lb_instructions.setWordWrap(True)

        self.verticalLayout.addWidget(self.lb_instructions)


        self.gridLayout_3.addWidget(self.groupBox_3, 0, 0, 1, 2)

        self.groupBox = QGroupBox(MeshPartGui__TaskCurveOnMesh)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(10)

        self.gridLayout_2.addWidget(self.spinBox, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.splitAngle = Gui_QuantitySpinBox(self.groupBox)
        self.splitAngle.setObjectName(u"splitAngle")
        self.splitAngle.setProperty(u"unit", u"deg")
        self.splitAngle.setMinimum(5.000000000000000)
        self.splitAngle.setMaximum(180.000000000000000)
        self.splitAngle.setValue(45.000000000000000)

        self.gridLayout_2.addWidget(self.splitAngle, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 2)

        self.groupBox_2 = QGroupBox(MeshPartGui__TaskCurveOnMesh)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setCheckable(True)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.meshTolerance = QDoubleSpinBox(self.groupBox_2)
        self.meshTolerance.setObjectName(u"meshTolerance")
        self.meshTolerance.setDecimals(3)
        self.meshTolerance.setMinimum(0.001000000000000)
        self.meshTolerance.setMaximum(10.000000000000000)
        self.meshTolerance.setSingleStep(0.010000000000000)
        self.meshTolerance.setValue(0.010000000000000)

        self.gridLayout.addWidget(self.meshTolerance, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.continuity = QComboBox(self.groupBox_2)
        self.continuity.setObjectName(u"continuity")

        self.gridLayout.addWidget(self.continuity, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.maxDegree = QComboBox(self.groupBox_2)
        self.maxDegree.setObjectName(u"maxDegree")

        self.gridLayout.addWidget(self.maxDegree, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 1, 2)

        self.startButton = QPushButton(MeshPartGui__TaskCurveOnMesh)
        self.startButton.setObjectName(u"startButton")

        self.gridLayout_3.addWidget(self.startButton, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(211, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        QWidget.setTabOrder(self.spinBox, self.splitAngle)
        QWidget.setTabOrder(self.splitAngle, self.meshTolerance)
        QWidget.setTabOrder(self.meshTolerance, self.continuity)
        QWidget.setTabOrder(self.continuity, self.maxDegree)
        QWidget.setTabOrder(self.maxDegree, self.startButton)

        self.retranslateUi(MeshPartGui__TaskCurveOnMesh)

        self.continuity.setCurrentIndex(-1)
        self.maxDegree.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MeshPartGui__TaskCurveOnMesh)
    # setupUi

    def retranslateUi(self, MeshPartGui__TaskCurveOnMesh):
        MeshPartGui__TaskCurveOnMesh.setWindowTitle(QCoreApplication.translate("MeshPartGui::TaskCurveOnMesh", u"Curve on Mesh", None))
        self.lb_instructions.setText(QCoreApplication.translate("MeshPartGui::TaskCurveOnMesh", u"Press 'Start', then pick points on the mesh; when enough points have been set, right-click and choose 'Create'. Repeat this process to create more splines. Close this task panel to complete the operation.\n"
"\n"
"This command only works with a Mesh object, not a regular face or surface. To convert an object to a mesh use the tools of the Mesh workbench.", None))
        self.groupBox.setTitle(QCoreApplication.translate("MeshPartGui::TaskCurveOnMesh", u"Wire", None))
        self.label_4.setText(QCoreApplication.translate("MeshPartGui::TaskCurveOnMesh", u"Snap tolerance to vertices", None))
        self.spinBox.setSuffix(QCoreApplication.translate("MeshPartGui::TaskCurveOnMesh", u" px", None))
        self.label_5.setText(QCoreApplication.translate("MeshPartGui::TaskCurveOnMesh", u"Split threshold", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MeshPartGui::TaskCurveOnMesh", u"Spline Approximation", None))
        self.label.setText(QCoreApplication.translate("MeshPartGui::TaskCurveOnMesh", u"Tolerance to mesh", None))
        self.label_2.setText(QCoreApplication.translate("MeshPartGui::TaskCurveOnMesh", u"Continuity", None))
        self.label_3.setText(QCoreApplication.translate("MeshPartGui::TaskCurveOnMesh", u"Maximum curve degree", None))
        self.startButton.setText(QCoreApplication.translate("MeshPartGui::TaskCurveOnMesh", u"Start", None))
    # retranslateUi

