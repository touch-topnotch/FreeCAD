# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CrossSections.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_PartGui_CrossSections(object):
    def setupUi(self, PartGui__CrossSections):
        if not PartGui__CrossSections.objectName():
            PartGui__CrossSections.setObjectName(u"PartGui__CrossSections")
        PartGui__CrossSections.resize(235, 240)
        self.gridLayout_4 = QGridLayout(PartGui__CrossSections)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.planeBox = QGroupBox(PartGui__CrossSections)
        self.planeBox.setObjectName(u"planeBox")
        self.gridLayout = QGridLayout(self.planeBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.xyPlane = QRadioButton(self.planeBox)
        self.xyPlane.setObjectName(u"xyPlane")
        self.xyPlane.setChecked(True)

        self.gridLayout.addWidget(self.xyPlane, 0, 0, 1, 1)

        self.xzPlane = QRadioButton(self.planeBox)
        self.xzPlane.setObjectName(u"xzPlane")

        self.gridLayout.addWidget(self.xzPlane, 0, 1, 1, 1)

        self.yzPlane = QRadioButton(self.planeBox)
        self.yzPlane.setObjectName(u"yzPlane")

        self.gridLayout.addWidget(self.yzPlane, 0, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.planeBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.position = Gui_QuantitySpinBox(self.planeBox)
        self.position.setObjectName(u"position")
        self.position.setProperty(u"unit", u"mm")

        self.horizontalLayout.addWidget(self.position)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)


        self.gridLayout_4.addWidget(self.planeBox, 0, 0, 1, 1)

        self.sectionsBox = QGroupBox(PartGui__CrossSections)
        self.sectionsBox.setObjectName(u"sectionsBox")
        self.sectionsBox.setCheckable(True)
        self.sectionsBox.setChecked(False)
        self.gridLayout_3 = QGridLayout(self.sectionsBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBothSides = QCheckBox(self.sectionsBox)
        self.checkBothSides.setObjectName(u"checkBothSides")

        self.gridLayout_3.addWidget(self.checkBothSides, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.sectionsBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.countSections = QSpinBox(self.sectionsBox)
        self.countSections.setObjectName(u"countSections")
        self.countSections.setMinimum(1)
        self.countSections.setMaximum(2000000)

        self.gridLayout_2.addWidget(self.countSections, 0, 1, 1, 1)

        self.label_2 = QLabel(self.sectionsBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.distance = Gui_QuantitySpinBox(self.sectionsBox)
        self.distance.setObjectName(u"distance")
        self.distance.setProperty(u"unit", u"mm")

        self.gridLayout_2.addWidget(self.distance, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.sectionsBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.xyPlane, self.xzPlane)
        QWidget.setTabOrder(self.xzPlane, self.yzPlane)
        QWidget.setTabOrder(self.yzPlane, self.position)
        QWidget.setTabOrder(self.position, self.sectionsBox)
        QWidget.setTabOrder(self.sectionsBox, self.checkBothSides)
        QWidget.setTabOrder(self.checkBothSides, self.countSections)
        QWidget.setTabOrder(self.countSections, self.distance)

        self.retranslateUi(PartGui__CrossSections)

        QMetaObject.connectSlotsByName(PartGui__CrossSections)
    # setupUi

    def retranslateUi(self, PartGui__CrossSections):
        PartGui__CrossSections.setWindowTitle(QCoreApplication.translate("PartGui::CrossSections", u"Cross Sections", None))
        self.planeBox.setTitle(QCoreApplication.translate("PartGui::CrossSections", u"Guiding Plane", None))
        self.xyPlane.setText(QCoreApplication.translate("PartGui::CrossSections", u"XY", None))
        self.xzPlane.setText(QCoreApplication.translate("PartGui::CrossSections", u"XZ", None))
        self.yzPlane.setText(QCoreApplication.translate("PartGui::CrossSections", u"YZ", None))
        self.label.setText(QCoreApplication.translate("PartGui::CrossSections", u"Position", None))
        self.sectionsBox.setTitle(QCoreApplication.translate("PartGui::CrossSections", u"Sections", None))
        self.checkBothSides.setText(QCoreApplication.translate("PartGui::CrossSections", u"On both sides", None))
        self.label_3.setText(QCoreApplication.translate("PartGui::CrossSections", u"Count", None))
        self.label_2.setText(QCoreApplication.translate("PartGui::CrossSections", u"Distance", None))
    # retranslateUi

