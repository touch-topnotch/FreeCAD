# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShapeFromMesh.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_PartGui_ShapeFromMesh(object):
    def setupUi(self, PartGui__ShapeFromMesh):
        if not PartGui__ShapeFromMesh.objectName():
            PartGui__ShapeFromMesh.setObjectName(u"PartGui__ShapeFromMesh")
        PartGui__ShapeFromMesh.resize(349, 148)
        self.gridLayout_2 = QGridLayout(PartGui__ShapeFromMesh)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBoxSew = QGroupBox(PartGui__ShapeFromMesh)
        self.groupBoxSew.setObjectName(u"groupBoxSew")
        self.groupBoxSew.setCheckable(True)
        self.groupBoxSew.setChecked(True)
        self.gridLayout = QGridLayout(self.groupBoxSew)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBoxSew)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBoxSew)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout.addWidget(self.doubleSpinBox, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBoxSew, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(PartGui__ShapeFromMesh)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)


        self.retranslateUi(PartGui__ShapeFromMesh)
        self.buttonBox.accepted.connect(PartGui__ShapeFromMesh.accept)
        self.buttonBox.rejected.connect(PartGui__ShapeFromMesh.reject)

        QMetaObject.connectSlotsByName(PartGui__ShapeFromMesh)
    # setupUi

    def retranslateUi(self, PartGui__ShapeFromMesh):
        PartGui__ShapeFromMesh.setWindowTitle(QCoreApplication.translate("PartGui::ShapeFromMesh", u"Shape From Mesh", None))
        self.groupBoxSew.setTitle(QCoreApplication.translate("PartGui::ShapeFromMesh", u"Sew Shape", None))
        self.label.setText(QCoreApplication.translate("PartGui::ShapeFromMesh", u"Tolerance for sewing the shape", None))
    # retranslateUi

