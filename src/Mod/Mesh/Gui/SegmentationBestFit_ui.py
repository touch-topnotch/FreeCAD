# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SegmentationBestFit.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_MeshGui_SegmentationBestFit(object):
    def setupUi(self, MeshGui__SegmentationBestFit):
        if not MeshGui__SegmentationBestFit.objectName():
            MeshGui__SegmentationBestFit.setObjectName(u"MeshGui__SegmentationBestFit")
        MeshGui__SegmentationBestFit.resize(289, 354)
        self.gridLayout_4 = QGridLayout(MeshGui__SegmentationBestFit)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBoxPln = QGroupBox(MeshGui__SegmentationBestFit)
        self.groupBoxPln.setObjectName(u"groupBoxPln")
        self.groupBoxPln.setCheckable(True)
        self.gridLayout = QGridLayout(self.groupBoxPln)
        self.gridLayout.setObjectName(u"gridLayout")
        self.planeParameters = QPushButton(self.groupBoxPln)
        self.planeParameters.setObjectName(u"planeParameters")

        self.gridLayout.addWidget(self.planeParameters, 0, 1, 1, 1)

        self.label = QLabel(self.groupBoxPln)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.tolPln = QDoubleSpinBox(self.groupBoxPln)
        self.tolPln.setObjectName(u"tolPln")
        self.tolPln.setSingleStep(0.010000000000000)
        self.tolPln.setValue(0.010000000000000)

        self.gridLayout.addWidget(self.tolPln, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBoxPln)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.numPln = QSpinBox(self.groupBoxPln)
        self.numPln.setObjectName(u"numPln")
        self.numPln.setMaximum(100000)
        self.numPln.setValue(100)

        self.gridLayout.addWidget(self.numPln, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBoxPln, 0, 0, 1, 2)

        self.groupBoxCyl = QGroupBox(MeshGui__SegmentationBestFit)
        self.groupBoxCyl.setObjectName(u"groupBoxCyl")
        self.groupBoxCyl.setCheckable(True)
        self.gridLayout_2 = QGridLayout(self.groupBoxCyl)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cylinderParameters = QPushButton(self.groupBoxCyl)
        self.cylinderParameters.setObjectName(u"cylinderParameters")

        self.gridLayout_2.addWidget(self.cylinderParameters, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBoxCyl)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.tolCyl = QDoubleSpinBox(self.groupBoxCyl)
        self.tolCyl.setObjectName(u"tolCyl")
        self.tolCyl.setSingleStep(0.010000000000000)
        self.tolCyl.setValue(0.010000000000000)

        self.gridLayout_2.addWidget(self.tolCyl, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBoxCyl)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.numCyl = QSpinBox(self.groupBoxCyl)
        self.numCyl.setObjectName(u"numCyl")
        self.numCyl.setMaximum(100000)
        self.numCyl.setValue(100)

        self.gridLayout_2.addWidget(self.numCyl, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBoxCyl, 1, 0, 1, 2)

        self.groupBoxSph = QGroupBox(MeshGui__SegmentationBestFit)
        self.groupBoxSph.setObjectName(u"groupBoxSph")
        self.groupBoxSph.setCheckable(True)
        self.gridLayout_3 = QGridLayout(self.groupBoxSph)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sphereParameters = QPushButton(self.groupBoxSph)
        self.sphereParameters.setObjectName(u"sphereParameters")

        self.gridLayout_3.addWidget(self.sphereParameters, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBoxSph)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.tolSph = QDoubleSpinBox(self.groupBoxSph)
        self.tolSph.setObjectName(u"tolSph")
        self.tolSph.setSingleStep(0.010000000000000)
        self.tolSph.setValue(0.010000000000000)

        self.gridLayout_3.addWidget(self.tolSph, 1, 1, 1, 1)

        self.label_8 = QLabel(self.groupBoxSph)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.numSph = QSpinBox(self.groupBoxSph)
        self.numSph.setObjectName(u"numSph")
        self.numSph.setMaximum(100000)
        self.numSph.setValue(100)

        self.gridLayout_3.addWidget(self.numSph, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBoxSph, 2, 0, 1, 2)


        self.retranslateUi(MeshGui__SegmentationBestFit)

        QMetaObject.connectSlotsByName(MeshGui__SegmentationBestFit)
    # setupUi

    def retranslateUi(self, MeshGui__SegmentationBestFit):
        MeshGui__SegmentationBestFit.setWindowTitle(QCoreApplication.translate("MeshGui::SegmentationBestFit", u"Mesh Segmentation", None))
        self.groupBoxPln.setTitle(QCoreApplication.translate("MeshGui::SegmentationBestFit", u"Plane", None))
        self.planeParameters.setText(QCoreApplication.translate("MeshGui::SegmentationBestFit", u"Parameters", None))
        self.label.setText(QCoreApplication.translate("MeshGui::SegmentationBestFit", u"Tolerance", None))
        self.label_2.setText(QCoreApplication.translate("MeshGui::SegmentationBestFit", u"Minimum number of faces", None))
        self.groupBoxCyl.setTitle(QCoreApplication.translate("MeshGui::SegmentationBestFit", u"Cylinder", None))
        self.cylinderParameters.setText(QCoreApplication.translate("MeshGui::SegmentationBestFit", u"Parameters", None))
        self.label_4.setText(QCoreApplication.translate("MeshGui::SegmentationBestFit", u"Tolerance", None))
        self.label_5.setText(QCoreApplication.translate("MeshGui::SegmentationBestFit", u"Minimum number of faces", None))
        self.groupBoxSph.setTitle(QCoreApplication.translate("MeshGui::SegmentationBestFit", u"Sphere", None))
        self.sphereParameters.setText(QCoreApplication.translate("MeshGui::SegmentationBestFit", u"Parameters", None))
        self.label_7.setText(QCoreApplication.translate("MeshGui::SegmentationBestFit", u"Tolerance", None))
        self.label_8.setText(QCoreApplication.translate("MeshGui::SegmentationBestFit", u"Minimum number of faces", None))
    # retranslateUi

