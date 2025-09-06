# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskPrimitiveParameters.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QVBoxLayout, QWidget)
import Part_rc

class Ui_PartDesignGui_DlgPrimitives(object):
    def setupUi(self, PartDesignGui__DlgPrimitives):
        if not PartDesignGui__DlgPrimitives.objectName():
            PartDesignGui__DlgPrimitives.setObjectName(u"PartDesignGui__DlgPrimitives")
        PartDesignGui__DlgPrimitives.resize(326, 241)
        PartDesignGui__DlgPrimitives.setProperty(u"sizeGripEnabled", True)
        self.verticalLayout = QVBoxLayout(PartDesignGui__DlgPrimitives)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widgetStack = QStackedWidget(PartDesignGui__DlgPrimitives)
        self.widgetStack.setObjectName(u"widgetStack")
        self.page0_plane = QWidget()
        self.page0_plane.setObjectName(u"page0_plane")
        self.gridLayout = QGridLayout(self.page0_plane)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self._2 = QGridLayout()
        self._2.setSpacing(6)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.textLabel2_2 = QLabel(self.page0_plane)
        self.textLabel2_2.setObjectName(u"textLabel2_2")

        self._2.addWidget(self.textLabel2_2, 0, 0, 1, 1)

        self.planeLength = Gui_QuantitySpinBox(self.page0_plane)
        self.planeLength.setObjectName(u"planeLength")
        self.planeLength.setKeyboardTracking(False)
        self.planeLength.setProperty(u"unit", u"mm")
        self.planeLength.setValue(10.000000000000000)

        self._2.addWidget(self.planeLength, 0, 2, 1, 1)

        self.textLabel3_2 = QLabel(self.page0_plane)
        self.textLabel3_2.setObjectName(u"textLabel3_2")

        self._2.addWidget(self.textLabel3_2, 1, 0, 1, 1)

        self.planeWidth = Gui_QuantitySpinBox(self.page0_plane)
        self.planeWidth.setObjectName(u"planeWidth")
        self.planeWidth.setKeyboardTracking(False)
        self.planeWidth.setProperty(u"unit", u"mm")
        self.planeWidth.setValue(10.000000000000000)

        self._2.addWidget(self.planeWidth, 1, 2, 1, 1)


        self.gridLayout.addLayout(self._2, 0, 0, 1, 1)

        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.spacerItem, 1, 0, 1, 1)

        self.widgetStack.addWidget(self.page0_plane)
        self.Page1_box = QWidget()
        self.Page1_box.setObjectName(u"Page1_box")
        self._3 = QGridLayout(self.Page1_box)
        self._3.setSpacing(6)
        self._3.setContentsMargins(11, 11, 11, 11)
        self._3.setObjectName(u"_3")
        self._3.setContentsMargins(0, 0, 0, 0)
        self._4 = QGridLayout()
        self._4.setSpacing(6)
        self._4.setObjectName(u"_4")
        self._4.setContentsMargins(0, 0, 0, 0)
        self.textLabel2 = QLabel(self.Page1_box)
        self.textLabel2.setObjectName(u"textLabel2")

        self._4.addWidget(self.textLabel2, 0, 0, 1, 1)

        self.boxLength = Gui_QuantitySpinBox(self.Page1_box)
        self.boxLength.setObjectName(u"boxLength")
        self.boxLength.setKeyboardTracking(False)
        self.boxLength.setProperty(u"unit", u"mm")
        self.boxLength.setValue(10.000000000000000)

        self._4.addWidget(self.boxLength, 0, 2, 1, 1)

        self.textLabel3 = QLabel(self.Page1_box)
        self.textLabel3.setObjectName(u"textLabel3")

        self._4.addWidget(self.textLabel3, 1, 0, 1, 1)

        self.boxWidth = Gui_QuantitySpinBox(self.Page1_box)
        self.boxWidth.setObjectName(u"boxWidth")
        self.boxWidth.setKeyboardTracking(False)
        self.boxWidth.setProperty(u"unit", u"mm")
        self.boxWidth.setValue(10.000000000000000)

        self._4.addWidget(self.boxWidth, 1, 2, 1, 1)

        self.textLabel4 = QLabel(self.Page1_box)
        self.textLabel4.setObjectName(u"textLabel4")

        self._4.addWidget(self.textLabel4, 2, 0, 1, 1)

        self.boxHeight = Gui_QuantitySpinBox(self.Page1_box)
        self.boxHeight.setObjectName(u"boxHeight")
        self.boxHeight.setKeyboardTracking(False)
        self.boxHeight.setProperty(u"unit", u"mm")
        self.boxHeight.setValue(10.000000000000000)

        self._4.addWidget(self.boxHeight, 2, 2, 1, 1)


        self._3.addLayout(self._4, 0, 0, 1, 1)

        self.spacerItem1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._3.addItem(self.spacerItem1, 1, 0, 1, 1)

        self.widgetStack.addWidget(self.Page1_box)
        self.Page2_cylinder = QWidget()
        self.Page2_cylinder.setObjectName(u"Page2_cylinder")
        self._5 = QGridLayout(self.Page2_cylinder)
        self._5.setSpacing(6)
        self._5.setContentsMargins(11, 11, 11, 11)
        self._5.setObjectName(u"_5")
        self._5.setContentsMargins(0, 0, 0, 0)
        self._7 = QGridLayout()
        self._7.setSpacing(6)
        self._7.setObjectName(u"_7")
        self._7.setContentsMargins(0, 0, 0, 0)
        self.textLabel5 = QLabel(self.Page2_cylinder)
        self.textLabel5.setObjectName(u"textLabel5")

        self._7.addWidget(self.textLabel5, 0, 0, 1, 1)

        self.cylinderRadius = Gui_QuantitySpinBox(self.Page2_cylinder)
        self.cylinderRadius.setObjectName(u"cylinderRadius")
        self.cylinderRadius.setKeyboardTracking(False)
        self.cylinderRadius.setProperty(u"unit", u"mm")
        self.cylinderRadius.setValue(2.000000000000000)

        self._7.addWidget(self.cylinderRadius, 0, 1, 1, 1)

        self.textLabel6 = QLabel(self.Page2_cylinder)
        self.textLabel6.setObjectName(u"textLabel6")

        self._7.addWidget(self.textLabel6, 1, 0, 1, 1)

        self.cylinderHeight = Gui_QuantitySpinBox(self.Page2_cylinder)
        self.cylinderHeight.setObjectName(u"cylinderHeight")
        self.cylinderHeight.setKeyboardTracking(False)
        self.cylinderHeight.setProperty(u"unit", u"mm")
        self.cylinderHeight.setValue(10.000000000000000)

        self._7.addWidget(self.cylinderHeight, 1, 1, 1, 1)

        self.labelCylinderXSkew = QLabel(self.Page2_cylinder)
        self.labelCylinderXSkew.setObjectName(u"labelCylinderXSkew")

        self._7.addWidget(self.labelCylinderXSkew, 2, 0, 1, 1)

        self.cylinderXSkew = Gui_QuantitySpinBox(self.Page2_cylinder)
        self.cylinderXSkew.setObjectName(u"cylinderXSkew")
        self.cylinderXSkew.setKeyboardTracking(False)
        self.cylinderXSkew.setProperty(u"unit", u"deg")
        self.cylinderXSkew.setMinimum(-90.000000000000000)
        self.cylinderXSkew.setMaximum(90.000000000000000)

        self._7.addWidget(self.cylinderXSkew, 2, 1, 1, 1)

        self.labelCylinderYSkew = QLabel(self.Page2_cylinder)
        self.labelCylinderYSkew.setObjectName(u"labelCylinderYSkew")

        self._7.addWidget(self.labelCylinderYSkew, 3, 0, 1, 1)

        self.cylinderYSkew = Gui_QuantitySpinBox(self.Page2_cylinder)
        self.cylinderYSkew.setObjectName(u"cylinderYSkew")
        self.cylinderYSkew.setKeyboardTracking(False)
        self.cylinderYSkew.setProperty(u"unit", u"deg")
        self.cylinderYSkew.setMinimum(-90.000000000000000)
        self.cylinderYSkew.setMaximum(90.000000000000000)

        self._7.addWidget(self.cylinderYSkew, 3, 1, 1, 1)


        self._5.addLayout(self._7, 0, 0, 1, 1)

        self.line_2 = QFrame(self.Page2_cylinder)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self._5.addWidget(self.line_2, 1, 0, 1, 1)

        self.gridLayout_1 = QGridLayout()
        self.gridLayout_1.setSpacing(6)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.Page2_cylinder)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(123, 0))

        self.gridLayout_1.addWidget(self.label, 0, 0, 1, 1)

        self.cylinderAngle = Gui_QuantitySpinBox(self.Page2_cylinder)
        self.cylinderAngle.setObjectName(u"cylinderAngle")
        self.cylinderAngle.setKeyboardTracking(False)
        self.cylinderAngle.setProperty(u"unit", u"deg")
        self.cylinderAngle.setValue(360.000000000000000)

        self.gridLayout_1.addWidget(self.cylinderAngle, 0, 1, 1, 1)


        self._5.addLayout(self.gridLayout_1, 2, 0, 1, 1)

        self.spacerItem2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._5.addItem(self.spacerItem2, 3, 0, 1, 1)

        self.widgetStack.addWidget(self.Page2_cylinder)
        self.Page3_cone = QWidget()
        self.Page3_cone.setObjectName(u"Page3_cone")
        self._8 = QGridLayout(self.Page3_cone)
        self._8.setSpacing(6)
        self._8.setContentsMargins(11, 11, 11, 11)
        self._8.setObjectName(u"_8")
        self._8.setContentsMargins(0, 0, 0, 0)
        self._10 = QGridLayout()
        self._10.setSpacing(6)
        self._10.setObjectName(u"_10")
        self._10.setContentsMargins(0, 0, 0, 0)
        self.textLabel9 = QLabel(self.Page3_cone)
        self.textLabel9.setObjectName(u"textLabel9")

        self._10.addWidget(self.textLabel9, 0, 0, 1, 1)

        self.coneRadius1 = Gui_QuantitySpinBox(self.Page3_cone)
        self.coneRadius1.setObjectName(u"coneRadius1")
        self.coneRadius1.setKeyboardTracking(False)
        self.coneRadius1.setProperty(u"unit", u"mm")
        self.coneRadius1.setValue(2.000000000000000)

        self._10.addWidget(self.coneRadius1, 0, 2, 1, 1)

        self.textLabel10 = QLabel(self.Page3_cone)
        self.textLabel10.setObjectName(u"textLabel10")

        self._10.addWidget(self.textLabel10, 1, 0, 1, 1)

        self.coneRadius2 = Gui_QuantitySpinBox(self.Page3_cone)
        self.coneRadius2.setObjectName(u"coneRadius2")
        self.coneRadius2.setKeyboardTracking(False)
        self.coneRadius2.setProperty(u"unit", u"mm")
        self.coneRadius2.setValue(4.000000000000000)

        self._10.addWidget(self.coneRadius2, 1, 2, 1, 1)

        self.textLabel11 = QLabel(self.Page3_cone)
        self.textLabel11.setObjectName(u"textLabel11")

        self._10.addWidget(self.textLabel11, 2, 0, 2, 1)

        self.coneHeight = Gui_QuantitySpinBox(self.Page3_cone)
        self.coneHeight.setObjectName(u"coneHeight")
        self.coneHeight.setKeyboardTracking(False)
        self.coneHeight.setProperty(u"unit", u"mm")
        self.coneHeight.setValue(10.000000000000000)

        self._10.addWidget(self.coneHeight, 3, 2, 1, 1)


        self._8.addLayout(self._10, 0, 0, 1, 1)

        self.line_3 = QFrame(self.Page3_cone)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self._8.addWidget(self.line_3, 1, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.Page3_cone)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)

        self.coneAngle = Gui_QuantitySpinBox(self.Page3_cone)
        self.coneAngle.setObjectName(u"coneAngle")
        self.coneAngle.setKeyboardTracking(False)
        self.coneAngle.setProperty(u"unit", u"deg")
        self.coneAngle.setValue(360.000000000000000)

        self.gridLayout_7.addWidget(self.coneAngle, 0, 1, 1, 1)


        self._8.addLayout(self.gridLayout_7, 2, 0, 1, 1)

        self.spacerItem3 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._8.addItem(self.spacerItem3, 3, 0, 1, 1)

        self.widgetStack.addWidget(self.Page3_cone)
        self.Page4_sphere = QWidget()
        self.Page4_sphere.setObjectName(u"Page4_sphere")
        self._11 = QGridLayout(self.Page4_sphere)
        self._11.setSpacing(6)
        self._11.setContentsMargins(11, 11, 11, 11)
        self._11.setObjectName(u"_11")
        self._11.setContentsMargins(0, 0, 0, 0)
        self._13 = QHBoxLayout()
        self._13.setSpacing(6)
        self._13.setObjectName(u"_13")
        self._13.setContentsMargins(0, 0, 0, 0)
        self.textLabel14 = QLabel(self.Page4_sphere)
        self.textLabel14.setObjectName(u"textLabel14")

        self._13.addWidget(self.textLabel14)

        self.sphereRadius = Gui_QuantitySpinBox(self.Page4_sphere)
        self.sphereRadius.setObjectName(u"sphereRadius")
        self.sphereRadius.setKeyboardTracking(False)
        self.sphereRadius.setProperty(u"unit", u"mm")
        self.sphereRadius.setValue(5.000000000000000)

        self._13.addWidget(self.sphereRadius)


        self._11.addLayout(self._13, 0, 0, 1, 1)

        self.line = QFrame(self.Page4_sphere)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self._11.addWidget(self.line, 1, 0, 1, 1)

        self._12 = QGridLayout()
        self._12.setSpacing(6)
        self._12.setObjectName(u"_12")
        self._12.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.Page4_sphere)
        self.label_3.setObjectName(u"label_3")

        self._12.addWidget(self.label_3, 0, 0, 1, 1)

        self.sphereAngle3 = Gui_QuantitySpinBox(self.Page4_sphere)
        self.sphereAngle3.setObjectName(u"sphereAngle3")
        self.sphereAngle3.setKeyboardTracking(False)
        self.sphereAngle3.setProperty(u"unit", u"deg")
        self.sphereAngle3.setValue(360.000000000000000)

        self._12.addWidget(self.sphereAngle3, 0, 2, 1, 1)

        self.label_2 = QLabel(self.Page4_sphere)
        self.label_2.setObjectName(u"label_2")

        self._12.addWidget(self.label_2, 1, 0, 1, 1)

        self.sphereAngle1 = Gui_QuantitySpinBox(self.Page4_sphere)
        self.sphereAngle1.setObjectName(u"sphereAngle1")
        self.sphereAngle1.setKeyboardTracking(False)
        self.sphereAngle1.setProperty(u"unit", u"deg")
        self.sphereAngle1.setValue(-90.000000000000000)

        self._12.addWidget(self.sphereAngle1, 1, 2, 1, 1)

        self.spacerItem4 = QSpacerItem(81, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self._12.addItem(self.spacerItem4, 2, 0, 1, 1)

        self.sphereAngle2 = Gui_QuantitySpinBox(self.Page4_sphere)
        self.sphereAngle2.setObjectName(u"sphereAngle2")
        self.sphereAngle2.setKeyboardTracking(False)
        self.sphereAngle2.setProperty(u"unit", u"deg")
        self.sphereAngle2.setValue(90.000000000000000)

        self._12.addWidget(self.sphereAngle2, 2, 2, 1, 1)


        self._11.addLayout(self._12, 2, 0, 1, 1)

        self.spacerItem5 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._11.addItem(self.spacerItem5, 3, 0, 1, 1)

        self.widgetStack.addWidget(self.Page4_sphere)
        self.Page5_ellipsoid = QWidget()
        self.Page5_ellipsoid.setObjectName(u"Page5_ellipsoid")
        self._14 = QGridLayout(self.Page5_ellipsoid)
        self._14.setSpacing(6)
        self._14.setContentsMargins(11, 11, 11, 11)
        self._14.setObjectName(u"_14")
        self._14.setContentsMargins(9, 9, 9, 9)
        self._15 = QGridLayout()
        self._15.setSpacing(6)
        self._15.setObjectName(u"_15")
        self._15.setContentsMargins(0, 0, 0, 0)
        self.textLabel21 = QLabel(self.Page5_ellipsoid)
        self.textLabel21.setObjectName(u"textLabel21")

        self._15.addWidget(self.textLabel21, 0, 0, 1, 1)

        self.ellipsoidRadius1 = Gui_QuantitySpinBox(self.Page5_ellipsoid)
        self.ellipsoidRadius1.setObjectName(u"ellipsoidRadius1")
        self.ellipsoidRadius1.setKeyboardTracking(False)
        self.ellipsoidRadius1.setProperty(u"unit", u"mm")
        self.ellipsoidRadius1.setValue(2.000000000000000)

        self._15.addWidget(self.ellipsoidRadius1, 0, 1, 1, 1)

        self.textLabel22 = QLabel(self.Page5_ellipsoid)
        self.textLabel22.setObjectName(u"textLabel22")

        self._15.addWidget(self.textLabel22, 1, 0, 1, 1)

        self.ellipsoidRadius2 = Gui_QuantitySpinBox(self.Page5_ellipsoid)
        self.ellipsoidRadius2.setObjectName(u"ellipsoidRadius2")
        self.ellipsoidRadius2.setKeyboardTracking(False)
        self.ellipsoidRadius2.setProperty(u"unit", u"mm")
        self.ellipsoidRadius2.setValue(4.000000000000000)

        self._15.addWidget(self.ellipsoidRadius2, 1, 1, 1, 1)

        self.textLabel23 = QLabel(self.Page5_ellipsoid)
        self.textLabel23.setObjectName(u"textLabel23")

        self._15.addWidget(self.textLabel23, 2, 0, 1, 1)

        self.ellipsoidRadius3 = Gui_QuantitySpinBox(self.Page5_ellipsoid)
        self.ellipsoidRadius3.setObjectName(u"ellipsoidRadius3")
        self.ellipsoidRadius3.setKeyboardTracking(False)
        self.ellipsoidRadius3.setProperty(u"unit", u"mm")
        self.ellipsoidRadius3.setValue(4.000000000000000)

        self._15.addWidget(self.ellipsoidRadius3, 2, 1, 1, 1)


        self._14.addLayout(self._15, 0, 0, 1, 1)

        self.line_5 = QFrame(self.Page5_ellipsoid)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self._14.addWidget(self.line_5, 1, 0, 1, 1)

        self._16 = QGridLayout()
        self._16.setSpacing(6)
        self._16.setObjectName(u"_16")
        self._16.setContentsMargins(0, 0, 0, 0)
        self.label23 = QLabel(self.Page5_ellipsoid)
        self.label23.setObjectName(u"label23")

        self._16.addWidget(self.label23, 0, 0, 1, 1)

        self.ellipsoidAngle3 = Gui_QuantitySpinBox(self.Page5_ellipsoid)
        self.ellipsoidAngle3.setObjectName(u"ellipsoidAngle3")
        self.ellipsoidAngle3.setKeyboardTracking(False)
        self.ellipsoidAngle3.setProperty(u"unit", u"deg")
        self.ellipsoidAngle3.setValue(360.000000000000000)

        self._16.addWidget(self.ellipsoidAngle3, 0, 1, 1, 1)

        self.label24 = QLabel(self.Page5_ellipsoid)
        self.label24.setObjectName(u"label24")

        self._16.addWidget(self.label24, 1, 0, 1, 1)

        self.ellipsoidAngle1 = Gui_QuantitySpinBox(self.Page5_ellipsoid)
        self.ellipsoidAngle1.setObjectName(u"ellipsoidAngle1")
        self.ellipsoidAngle1.setKeyboardTracking(False)
        self.ellipsoidAngle1.setProperty(u"unit", u"deg")
        self.ellipsoidAngle1.setValue(-90.000000000000000)

        self._16.addWidget(self.ellipsoidAngle1, 1, 1, 1, 1)

        self.spacerItem6 = QSpacerItem(81, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self._16.addItem(self.spacerItem6, 2, 0, 1, 1)

        self.ellipsoidAngle2 = Gui_QuantitySpinBox(self.Page5_ellipsoid)
        self.ellipsoidAngle2.setObjectName(u"ellipsoidAngle2")
        self.ellipsoidAngle2.setKeyboardTracking(False)
        self.ellipsoidAngle2.setProperty(u"unit", u"deg")
        self.ellipsoidAngle2.setValue(90.000000000000000)

        self._16.addWidget(self.ellipsoidAngle2, 2, 1, 1, 1)


        self._14.addLayout(self._16, 2, 0, 1, 1)

        self.spacerItem7 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._14.addItem(self.spacerItem7, 3, 0, 1, 1)

        self.widgetStack.addWidget(self.Page5_ellipsoid)
        self.Page6_torus = QWidget()
        self.Page6_torus.setObjectName(u"Page6_torus")
        self._17 = QGridLayout(self.Page6_torus)
        self._17.setSpacing(6)
        self._17.setContentsMargins(11, 11, 11, 11)
        self._17.setObjectName(u"_17")
        self._17.setContentsMargins(9, 9, 9, 9)
        self._19 = QGridLayout()
        self._19.setSpacing(6)
        self._19.setObjectName(u"_19")
        self._19.setContentsMargins(0, 0, 0, 0)
        self.textLabel19 = QLabel(self.Page6_torus)
        self.textLabel19.setObjectName(u"textLabel19")

        self._19.addWidget(self.textLabel19, 0, 0, 1, 1)

        self.torusRadius1 = Gui_QuantitySpinBox(self.Page6_torus)
        self.torusRadius1.setObjectName(u"torusRadius1")
        self.torusRadius1.setKeyboardTracking(False)
        self.torusRadius1.setProperty(u"unit", u"mm")
        self.torusRadius1.setValue(10.000000000000000)

        self._19.addWidget(self.torusRadius1, 0, 2, 1, 1)

        self.textLabel20 = QLabel(self.Page6_torus)
        self.textLabel20.setObjectName(u"textLabel20")

        self._19.addWidget(self.textLabel20, 1, 0, 1, 1)

        self.torusRadius2 = Gui_QuantitySpinBox(self.Page6_torus)
        self.torusRadius2.setObjectName(u"torusRadius2")
        self.torusRadius2.setKeyboardTracking(False)
        self.torusRadius2.setProperty(u"unit", u"mm")
        self.torusRadius2.setValue(2.000000000000000)

        self._19.addWidget(self.torusRadius2, 1, 2, 1, 1)


        self._17.addLayout(self._19, 0, 0, 1, 1)

        self.line_4 = QFrame(self.Page6_torus)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self._17.addWidget(self.line_4, 1, 0, 1, 1)

        self._18 = QGridLayout()
        self._18.setSpacing(6)
        self._18.setObjectName(u"_18")
        self._18.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.Page6_torus)
        self.label_5.setObjectName(u"label_5")

        self._18.addWidget(self.label_5, 0, 0, 1, 1)

        self.torusAngle3 = Gui_QuantitySpinBox(self.Page6_torus)
        self.torusAngle3.setObjectName(u"torusAngle3")
        self.torusAngle3.setKeyboardTracking(False)
        self.torusAngle3.setProperty(u"unit", u"deg")
        self.torusAngle3.setValue(360.000000000000000)

        self._18.addWidget(self.torusAngle3, 0, 1, 1, 1)

        self.label_6 = QLabel(self.Page6_torus)
        self.label_6.setObjectName(u"label_6")

        self._18.addWidget(self.label_6, 1, 0, 1, 1)

        self.torusAngle1 = Gui_QuantitySpinBox(self.Page6_torus)
        self.torusAngle1.setObjectName(u"torusAngle1")
        self.torusAngle1.setKeyboardTracking(False)
        self.torusAngle1.setProperty(u"unit", u"deg")
        self.torusAngle1.setValue(-180.000000000000000)

        self._18.addWidget(self.torusAngle1, 1, 1, 1, 1)

        self.spacerItem8 = QSpacerItem(81, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self._18.addItem(self.spacerItem8, 2, 0, 1, 1)

        self.torusAngle2 = Gui_QuantitySpinBox(self.Page6_torus)
        self.torusAngle2.setObjectName(u"torusAngle2")
        self.torusAngle2.setKeyboardTracking(False)
        self.torusAngle2.setProperty(u"unit", u"deg")
        self.torusAngle2.setValue(180.000000000000000)

        self._18.addWidget(self.torusAngle2, 2, 1, 1, 1)


        self._17.addLayout(self._18, 2, 0, 1, 1)

        self.spacerItem9 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._17.addItem(self.spacerItem9, 3, 0, 1, 1)

        self.widgetStack.addWidget(self.Page6_torus)
        self.page_prism = QWidget()
        self.page_prism.setObjectName(u"page_prism")
        self._20 = QGridLayout(self.page_prism)
        self._20.setSpacing(6)
        self._20.setContentsMargins(11, 11, 11, 11)
        self._20.setObjectName(u"_20")
        self._20.setContentsMargins(9, 9, 9, 9)
        self._21 = QGridLayout()
        self._21.setSpacing(6)
        self._21.setObjectName(u"_21")
        self._21.setContentsMargins(0, 0, 0, 0)
        self.labelPrismPolygon = QLabel(self.page_prism)
        self.labelPrismPolygon.setObjectName(u"labelPrismPolygon")

        self._21.addWidget(self.labelPrismPolygon, 0, 0, 1, 1)

        self.prismPolygon = QSpinBox(self.page_prism)
        self.prismPolygon.setObjectName(u"prismPolygon")
        self.prismPolygon.setMinimum(3)
        self.prismPolygon.setMaximum(1000)
        self.prismPolygon.setValue(6)

        self._21.addWidget(self.prismPolygon, 0, 2, 1, 1)

        self.labelPrismCircumradius = QLabel(self.page_prism)
        self.labelPrismCircumradius.setObjectName(u"labelPrismCircumradius")

        self._21.addWidget(self.labelPrismCircumradius, 1, 0, 1, 1)

        self.prismCircumradius = Gui_QuantitySpinBox(self.page_prism)
        self.prismCircumradius.setObjectName(u"prismCircumradius")
        self.prismCircumradius.setKeyboardTracking(False)
        self.prismCircumradius.setProperty(u"unit", u"mm")
        self.prismCircumradius.setValue(2.000000000000000)

        self._21.addWidget(self.prismCircumradius, 1, 2, 1, 1)

        self.labelPrismHeight = QLabel(self.page_prism)
        self.labelPrismHeight.setObjectName(u"labelPrismHeight")

        self._21.addWidget(self.labelPrismHeight, 2, 0, 1, 1)

        self.prismHeight = Gui_QuantitySpinBox(self.page_prism)
        self.prismHeight.setObjectName(u"prismHeight")
        self.prismHeight.setKeyboardTracking(False)
        self.prismHeight.setProperty(u"unit", u"mm")
        self.prismHeight.setValue(10.000000000000000)

        self._21.addWidget(self.prismHeight, 2, 2, 1, 1)

        self.labelPrismXSkew = QLabel(self.page_prism)
        self.labelPrismXSkew.setObjectName(u"labelPrismXSkew")

        self._21.addWidget(self.labelPrismXSkew, 3, 0, 1, 1)

        self.prismXSkew = Gui_QuantitySpinBox(self.page_prism)
        self.prismXSkew.setObjectName(u"prismXSkew")
        self.prismXSkew.setKeyboardTracking(False)
        self.prismXSkew.setProperty(u"unit", u"deg")
        self.prismXSkew.setMinimum(-90.000000000000000)
        self.prismXSkew.setMaximum(90.000000000000000)

        self._21.addWidget(self.prismXSkew, 3, 2, 1, 1)

        self.labelPrismYSkew = QLabel(self.page_prism)
        self.labelPrismYSkew.setObjectName(u"labelPrismYSkew")

        self._21.addWidget(self.labelPrismYSkew, 4, 0, 1, 1)

        self.prismYSkew = Gui_QuantitySpinBox(self.page_prism)
        self.prismYSkew.setObjectName(u"prismYSkew")
        self.prismYSkew.setKeyboardTracking(False)
        self.prismYSkew.setProperty(u"unit", u"deg")
        self.prismYSkew.setMinimum(-90.000000000000000)
        self.prismYSkew.setMaximum(90.000000000000000)

        self._21.addWidget(self.prismYSkew, 4, 2, 1, 1)


        self._20.addLayout(self._21, 0, 0, 1, 1)

        self.spacerItem10 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._20.addItem(self.spacerItem10, 1, 0, 1, 1)

        self.widgetStack.addWidget(self.page_prism)
        self.page7_wedge = QWidget()
        self.page7_wedge.setObjectName(u"page7_wedge")
        self.gridLayout_8 = QGridLayout(self.page7_wedge)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(4)
        self.label_10 = QLabel(self.page7_wedge)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.wedgeXmin = Gui_QuantitySpinBox(self.page7_wedge)
        self.wedgeXmin.setObjectName(u"wedgeXmin")
        self.wedgeXmin.setKeyboardTracking(False)
        self.wedgeXmin.setProperty(u"unit", u"mm")

        self.gridLayout_2.addWidget(self.wedgeXmin, 0, 1, 1, 1)

        self.wedgeXmax = Gui_QuantitySpinBox(self.page7_wedge)
        self.wedgeXmax.setObjectName(u"wedgeXmax")
        self.wedgeXmax.setKeyboardTracking(False)
        self.wedgeXmax.setProperty(u"unit", u"mm")
        self.wedgeXmax.setValue(10.000000000000000)

        self.gridLayout_2.addWidget(self.wedgeXmax, 0, 2, 1, 1)

        self.label_11 = QLabel(self.page7_wedge)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)

        self.wedgeYmin = Gui_QuantitySpinBox(self.page7_wedge)
        self.wedgeYmin.setObjectName(u"wedgeYmin")
        self.wedgeYmin.setKeyboardTracking(False)
        self.wedgeYmin.setProperty(u"unit", u"mm")

        self.gridLayout_2.addWidget(self.wedgeYmin, 1, 1, 1, 1)

        self.wedgeYmax = Gui_QuantitySpinBox(self.page7_wedge)
        self.wedgeYmax.setObjectName(u"wedgeYmax")
        self.wedgeYmax.setKeyboardTracking(False)
        self.wedgeYmax.setProperty(u"unit", u"mm")
        self.wedgeYmax.setValue(10.000000000000000)

        self.gridLayout_2.addWidget(self.wedgeYmax, 1, 2, 1, 1)

        self.label_12 = QLabel(self.page7_wedge)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)

        self.wedgeZmin = Gui_QuantitySpinBox(self.page7_wedge)
        self.wedgeZmin.setObjectName(u"wedgeZmin")
        self.wedgeZmin.setKeyboardTracking(False)
        self.wedgeZmin.setProperty(u"unit", u"mm")

        self.gridLayout_2.addWidget(self.wedgeZmin, 2, 1, 1, 1)

        self.wedgeZmax = Gui_QuantitySpinBox(self.page7_wedge)
        self.wedgeZmax.setObjectName(u"wedgeZmax")
        self.wedgeZmax.setKeyboardTracking(False)
        self.wedgeZmax.setProperty(u"unit", u"mm")
        self.wedgeZmax.setValue(10.000000000000000)

        self.gridLayout_2.addWidget(self.wedgeZmax, 2, 2, 1, 1)

        self.label_13 = QLabel(self.page7_wedge)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)

        self.wedgeX2min = Gui_QuantitySpinBox(self.page7_wedge)
        self.wedgeX2min.setObjectName(u"wedgeX2min")
        self.wedgeX2min.setKeyboardTracking(False)
        self.wedgeX2min.setProperty(u"unit", u"mm")
        self.wedgeX2min.setValue(2.000000000000000)

        self.gridLayout_2.addWidget(self.wedgeX2min, 3, 1, 1, 1)

        self.wedgeX2max = Gui_QuantitySpinBox(self.page7_wedge)
        self.wedgeX2max.setObjectName(u"wedgeX2max")
        self.wedgeX2max.setKeyboardTracking(False)
        self.wedgeX2max.setProperty(u"unit", u"mm")
        self.wedgeX2max.setValue(8.000000000000000)

        self.gridLayout_2.addWidget(self.wedgeX2max, 3, 2, 1, 1)

        self.label_14 = QLabel(self.page7_wedge)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)

        self.wedgeZ2min = Gui_QuantitySpinBox(self.page7_wedge)
        self.wedgeZ2min.setObjectName(u"wedgeZ2min")
        self.wedgeZ2min.setKeyboardTracking(False)
        self.wedgeZ2min.setProperty(u"unit", u"mm")
        self.wedgeZ2min.setValue(2.000000000000000)

        self.gridLayout_2.addWidget(self.wedgeZ2min, 4, 1, 1, 1)

        self.wedgeZ2max = Gui_QuantitySpinBox(self.page7_wedge)
        self.wedgeZ2max.setObjectName(u"wedgeZ2max")
        self.wedgeZ2max.setKeyboardTracking(False)
        self.wedgeZ2max.setProperty(u"unit", u"mm")
        self.wedgeZ2max.setValue(8.000000000000000)

        self.gridLayout_2.addWidget(self.wedgeZ2max, 4, 2, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.widgetStack.addWidget(self.page7_wedge)
        self.page8_helix = QWidget()
        self.page8_helix.setObjectName(u"page8_helix")
        self._22 = QGridLayout(self.page8_helix)
        self._22.setSpacing(6)
        self._22.setContentsMargins(11, 11, 11, 11)
        self._22.setObjectName(u"_22")
        self._22.setContentsMargins(9, 9, 9, 9)
        self._23 = QGridLayout()
        self._23.setSpacing(6)
        self._23.setObjectName(u"_23")
        self._23.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.page8_helix)
        self.label_7.setObjectName(u"label_7")

        self._23.addWidget(self.label_7, 0, 0, 1, 1)

        self.helixPitch = Gui_QuantitySpinBox(self.page8_helix)
        self.helixPitch.setObjectName(u"helixPitch")
        self.helixPitch.setKeyboardTracking(False)
        self.helixPitch.setProperty(u"unit", u"mm")
        self.helixPitch.setValue(1.000000000000000)

        self._23.addWidget(self.helixPitch, 0, 1, 1, 1)

        self.label_8 = QLabel(self.page8_helix)
        self.label_8.setObjectName(u"label_8")

        self._23.addWidget(self.label_8, 1, 0, 1, 1)

        self.helixHeight = Gui_QuantitySpinBox(self.page8_helix)
        self.helixHeight.setObjectName(u"helixHeight")
        self.helixHeight.setKeyboardTracking(False)
        self.helixHeight.setProperty(u"unit", u"mm")
        self.helixHeight.setValue(2.000000000000000)

        self._23.addWidget(self.helixHeight, 1, 1, 1, 1)

        self.label_9 = QLabel(self.page8_helix)
        self.label_9.setObjectName(u"label_9")

        self._23.addWidget(self.label_9, 2, 0, 1, 1)

        self.helixRadius = Gui_QuantitySpinBox(self.page8_helix)
        self.helixRadius.setObjectName(u"helixRadius")
        self.helixRadius.setKeyboardTracking(False)
        self.helixRadius.setProperty(u"unit", u"mm")
        self.helixRadius.setValue(1.000000000000000)

        self._23.addWidget(self.helixRadius, 2, 1, 1, 1)

        self.label_20 = QLabel(self.page8_helix)
        self.label_20.setObjectName(u"label_20")

        self._23.addWidget(self.label_20, 3, 0, 1, 1)

        self.helixAngle = Gui_QuantitySpinBox(self.page8_helix)
        self.helixAngle.setObjectName(u"helixAngle")
        self.helixAngle.setKeyboardTracking(False)
        self.helixAngle.setProperty(u"unit", u"deg")

        self._23.addWidget(self.helixAngle, 3, 1, 1, 1)

        self.label_15 = QLabel(self.page8_helix)
        self.label_15.setObjectName(u"label_15")

        self._23.addWidget(self.label_15, 4, 0, 1, 1)

        self.helixLocalCS = QComboBox(self.page8_helix)
        self.helixLocalCS.addItem("")
        self.helixLocalCS.addItem("")
        self.helixLocalCS.setObjectName(u"helixLocalCS")

        self._23.addWidget(self.helixLocalCS, 4, 1, 1, 1)


        self._22.addLayout(self._23, 0, 0, 1, 1)

        self.spacerItem11 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._22.addItem(self.spacerItem11, 1, 0, 1, 1)

        self.widgetStack.addWidget(self.page8_helix)
        self.page9_spiral = QWidget()
        self.page9_spiral.setObjectName(u"page9_spiral")
        self._24 = QGridLayout(self.page9_spiral)
        self._24.setSpacing(6)
        self._24.setContentsMargins(11, 11, 11, 11)
        self._24.setObjectName(u"_24")
        self._24.setContentsMargins(9, 9, 9, 9)
        self._25 = QGridLayout()
        self._25.setSpacing(6)
        self._25.setObjectName(u"_25")
        self._25.setContentsMargins(0, 0, 0, 0)
        self.label_spiral_growth = QLabel(self.page9_spiral)
        self.label_spiral_growth.setObjectName(u"label_spiral_growth")

        self._25.addWidget(self.label_spiral_growth, 0, 0, 1, 1)

        self.spiralGrowth = Gui_QuantitySpinBox(self.page9_spiral)
        self.spiralGrowth.setObjectName(u"spiralGrowth")
        self.spiralGrowth.setKeyboardTracking(False)
        self.spiralGrowth.setProperty(u"unit", u"mm")
        self.spiralGrowth.setValue(1.000000000000000)

        self._25.addWidget(self.spiralGrowth, 0, 1, 1, 1)

        self.label_spiral_rotation = QLabel(self.page9_spiral)
        self.label_spiral_rotation.setObjectName(u"label_spiral_rotation")

        self._25.addWidget(self.label_spiral_rotation, 1, 0, 1, 1)

        self.spiralRotation = QDoubleSpinBox(self.page9_spiral)
        self.spiralRotation.setObjectName(u"spiralRotation")
        self.spiralRotation.setKeyboardTracking(False)
        self.spiralRotation.setMaximum(1000.000000000000000)
        self.spiralRotation.setValue(2.000000000000000)

        self._25.addWidget(self.spiralRotation, 1, 1, 1, 1)

        self.label_spiral_radius = QLabel(self.page9_spiral)
        self.label_spiral_radius.setObjectName(u"label_spiral_radius")

        self._25.addWidget(self.label_spiral_radius, 2, 0, 1, 1)

        self.spiralRadius = Gui_QuantitySpinBox(self.page9_spiral)
        self.spiralRadius.setObjectName(u"spiralRadius")
        self.spiralRadius.setKeyboardTracking(False)
        self.spiralRadius.setProperty(u"unit", u"mm")
        self.spiralRadius.setValue(1.000000000000000)

        self._25.addWidget(self.spiralRadius, 2, 1, 1, 1)


        self._24.addLayout(self._25, 0, 0, 1, 1)

        self.spacerItem12 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._24.addItem(self.spacerItem12, 1, 0, 1, 1)

        self.widgetStack.addWidget(self.page9_spiral)
        self.page10_circle = QWidget()
        self.page10_circle.setObjectName(u"page10_circle")
        self.gridLayout_3 = QGridLayout(self.page10_circle)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.circleParameters = QGridLayout()
        self.circleParameters.setSpacing(6)
        self.circleParameters.setObjectName(u"circleParameters")
        self.circleParameters.setContentsMargins(0, 0, 0, 0)
        self.Radius = QLabel(self.page10_circle)
        self.Radius.setObjectName(u"Radius")

        self.circleParameters.addWidget(self.Radius, 0, 0, 1, 1)

        self.circleRadius = Gui_QuantitySpinBox(self.page10_circle)
        self.circleRadius.setObjectName(u"circleRadius")
        self.circleRadius.setKeyboardTracking(False)
        self.circleRadius.setProperty(u"unit", u"mm")
        self.circleRadius.setValue(2.000000000000000)

        self.circleParameters.addWidget(self.circleRadius, 0, 1, 1, 1)

        self.Angle1 = QLabel(self.page10_circle)
        self.Angle1.setObjectName(u"Angle1")

        self.circleParameters.addWidget(self.Angle1, 1, 0, 1, 1)

        self.circleAngle1 = Gui_QuantitySpinBox(self.page10_circle)
        self.circleAngle1.setObjectName(u"circleAngle1")
        self.circleAngle1.setKeyboardTracking(False)
        self.circleAngle1.setProperty(u"unit", u"deg")

        self.circleParameters.addWidget(self.circleAngle1, 1, 1, 1, 1)

        self.Angle2 = QLabel(self.page10_circle)
        self.Angle2.setObjectName(u"Angle2")

        self.circleParameters.addWidget(self.Angle2, 2, 0, 1, 1)

        self.circleAngle2 = Gui_QuantitySpinBox(self.page10_circle)
        self.circleAngle2.setObjectName(u"circleAngle2")
        self.circleAngle2.setKeyboardTracking(False)
        self.circleAngle2.setProperty(u"unit", u"deg")
        self.circleAngle2.setValue(360.000000000000000)

        self.circleParameters.addWidget(self.circleAngle2, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.circleParameters, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonCircleFromThreePoints = QPushButton(self.page10_circle)
        self.buttonCircleFromThreePoints.setObjectName(u"buttonCircleFromThreePoints")

        self.horizontalLayout.addWidget(self.buttonCircleFromThreePoints)


        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.widgetStack.addWidget(self.page10_circle)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_11 = QGridLayout(self.page)
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.labelEllMajorRadius = QLabel(self.page)
        self.labelEllMajorRadius.setObjectName(u"labelEllMajorRadius")

        self.gridLayout_10.addWidget(self.labelEllMajorRadius, 0, 0, 1, 1)

        self.ellipseMajorRadius = Gui_QuantitySpinBox(self.page)
        self.ellipseMajorRadius.setObjectName(u"ellipseMajorRadius")
        self.ellipseMajorRadius.setKeyboardTracking(False)
        self.ellipseMajorRadius.setProperty(u"unit", u"mm")
        self.ellipseMajorRadius.setValue(4.000000000000000)

        self.gridLayout_10.addWidget(self.ellipseMajorRadius, 0, 1, 1, 1)

        self.labelEllMinorRadius = QLabel(self.page)
        self.labelEllMinorRadius.setObjectName(u"labelEllMinorRadius")

        self.gridLayout_10.addWidget(self.labelEllMinorRadius, 1, 0, 1, 1)

        self.ellipseMinorRadius = Gui_QuantitySpinBox(self.page)
        self.ellipseMinorRadius.setObjectName(u"ellipseMinorRadius")
        self.ellipseMinorRadius.setKeyboardTracking(False)
        self.ellipseMinorRadius.setProperty(u"unit", u"mm")
        self.ellipseMinorRadius.setValue(2.000000000000000)

        self.gridLayout_10.addWidget(self.ellipseMinorRadius, 1, 1, 1, 1)

        self.labelEllAngle1 = QLabel(self.page)
        self.labelEllAngle1.setObjectName(u"labelEllAngle1")

        self.gridLayout_10.addWidget(self.labelEllAngle1, 2, 0, 1, 1)

        self.ellipseAngle1 = Gui_QuantitySpinBox(self.page)
        self.ellipseAngle1.setObjectName(u"ellipseAngle1")
        self.ellipseAngle1.setKeyboardTracking(False)
        self.ellipseAngle1.setProperty(u"unit", u"deg")

        self.gridLayout_10.addWidget(self.ellipseAngle1, 2, 1, 1, 1)

        self.labelEllAngle2 = QLabel(self.page)
        self.labelEllAngle2.setObjectName(u"labelEllAngle2")

        self.gridLayout_10.addWidget(self.labelEllAngle2, 3, 0, 1, 1)

        self.ellipseAngle2 = Gui_QuantitySpinBox(self.page)
        self.ellipseAngle2.setObjectName(u"ellipseAngle2")
        self.ellipseAngle2.setKeyboardTracking(False)
        self.ellipseAngle2.setProperty(u"unit", u"deg")
        self.ellipseAngle2.setValue(360.000000000000000)

        self.gridLayout_10.addWidget(self.ellipseAngle2, 3, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.widgetStack.addWidget(self.page)
        self.page11_vertex = QWidget()
        self.page11_vertex.setObjectName(u"page11_vertex")
        self.gridLayout_9 = QGridLayout(self.page11_vertex)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_X_Axis = QLabel(self.page11_vertex)
        self.label_X_Axis.setObjectName(u"label_X_Axis")
        self.label_X_Axis.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_X_Axis, 0, 0, 1, 1)

        self.vertexX = Gui_QuantitySpinBox(self.page11_vertex)
        self.vertexX.setObjectName(u"vertexX")
        self.vertexX.setKeyboardTracking(False)
        self.vertexX.setProperty(u"unit", u"mm")

        self.gridLayout_4.addWidget(self.vertexX, 0, 1, 1, 1)

        self.label_Y_Axis = QLabel(self.page11_vertex)
        self.label_Y_Axis.setObjectName(u"label_Y_Axis")
        self.label_Y_Axis.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_Y_Axis, 1, 0, 1, 1)

        self.vertexY = Gui_QuantitySpinBox(self.page11_vertex)
        self.vertexY.setObjectName(u"vertexY")
        self.vertexY.setKeyboardTracking(False)
        self.vertexY.setProperty(u"unit", u"mm")

        self.gridLayout_4.addWidget(self.vertexY, 1, 1, 1, 1)

        self.label_Z_Axis = QLabel(self.page11_vertex)
        self.label_Z_Axis.setObjectName(u"label_Z_Axis")
        self.label_Z_Axis.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_Z_Axis, 2, 0, 1, 1)

        self.vertexZ = Gui_QuantitySpinBox(self.page11_vertex)
        self.vertexZ.setObjectName(u"vertexZ")
        self.vertexZ.setKeyboardTracking(False)
        self.vertexZ.setProperty(u"unit", u"mm")

        self.gridLayout_4.addWidget(self.vertexZ, 2, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.widgetStack.addWidget(self.page11_vertex)
        self.page12_edge = QWidget()
        self.page12_edge.setObjectName(u"page12_edge")
        self.gridLayout_6 = QGridLayout(self.page12_edge)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Start_Vertex = QLabel(self.page12_edge)
        self.Start_Vertex.setObjectName(u"Start_Vertex")

        self.gridLayout_5.addWidget(self.Start_Vertex, 0, 0, 1, 1)

        self.X1 = QLabel(self.page12_edge)
        self.X1.setObjectName(u"X1")
        self.X1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.X1, 1, 0, 1, 1)

        self.edgeX1 = Gui_QuantitySpinBox(self.page12_edge)
        self.edgeX1.setObjectName(u"edgeX1")
        self.edgeX1.setKeyboardTracking(False)
        self.edgeX1.setProperty(u"unit", u"mm")

        self.gridLayout_5.addWidget(self.edgeX1, 1, 1, 1, 1)

        self.Y1 = QLabel(self.page12_edge)
        self.Y1.setObjectName(u"Y1")
        self.Y1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.Y1, 2, 0, 1, 1)

        self.edgeY1 = Gui_QuantitySpinBox(self.page12_edge)
        self.edgeY1.setObjectName(u"edgeY1")
        self.edgeY1.setKeyboardTracking(False)
        self.edgeY1.setProperty(u"unit", u"mm")

        self.gridLayout_5.addWidget(self.edgeY1, 2, 1, 1, 1)

        self.Z1 = QLabel(self.page12_edge)
        self.Z1.setObjectName(u"Z1")
        self.Z1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.Z1, 3, 0, 1, 1)

        self.edgeZ1 = Gui_QuantitySpinBox(self.page12_edge)
        self.edgeZ1.setObjectName(u"edgeZ1")
        self.edgeZ1.setKeyboardTracking(False)
        self.edgeZ1.setProperty(u"unit", u"mm")

        self.gridLayout_5.addWidget(self.edgeZ1, 3, 1, 1, 1)

        self.line_6 = QFrame(self.page12_edge)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_6, 4, 0, 1, 1)

        self.Finish_Vertex = QLabel(self.page12_edge)
        self.Finish_Vertex.setObjectName(u"Finish_Vertex")
        self.Finish_Vertex.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.Finish_Vertex, 5, 0, 1, 1)

        self.X2 = QLabel(self.page12_edge)
        self.X2.setObjectName(u"X2")
        self.X2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.X2, 6, 0, 1, 1)

        self.edgeX2 = Gui_QuantitySpinBox(self.page12_edge)
        self.edgeX2.setObjectName(u"edgeX2")
        self.edgeX2.setKeyboardTracking(False)
        self.edgeX2.setProperty(u"unit", u"mm")
        self.edgeX2.setValue(10.000000000000000)

        self.gridLayout_5.addWidget(self.edgeX2, 6, 1, 1, 1)

        self.Y2 = QLabel(self.page12_edge)
        self.Y2.setObjectName(u"Y2")
        self.Y2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.Y2, 7, 0, 1, 1)

        self.edgeY2 = Gui_QuantitySpinBox(self.page12_edge)
        self.edgeY2.setObjectName(u"edgeY2")
        self.edgeY2.setKeyboardTracking(False)
        self.edgeY2.setProperty(u"unit", u"mm")
        self.edgeY2.setValue(10.000000000000000)

        self.gridLayout_5.addWidget(self.edgeY2, 7, 1, 1, 1)

        self.Z2 = QLabel(self.page12_edge)
        self.Z2.setObjectName(u"Z2")
        self.Z2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.Z2, 8, 0, 1, 1)

        self.edgeZ2 = Gui_QuantitySpinBox(self.page12_edge)
        self.edgeZ2.setObjectName(u"edgeZ2")
        self.edgeZ2.setKeyboardTracking(False)
        self.edgeZ2.setProperty(u"unit", u"mm")
        self.edgeZ2.setValue(10.000000000000000)

        self.gridLayout_5.addWidget(self.edgeZ2, 8, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.widgetStack.addWidget(self.page12_edge)
        self.page_regularPolygon = QWidget()
        self.page_regularPolygon.setObjectName(u"page_regularPolygon")
        self._26 = QGridLayout(self.page_regularPolygon)
        self._26.setSpacing(6)
        self._26.setContentsMargins(11, 11, 11, 11)
        self._26.setObjectName(u"_26")
        self._26.setContentsMargins(9, 9, 9, 9)
        self._27 = QGridLayout()
        self._27.setSpacing(6)
        self._27.setObjectName(u"_27")
        self._27.setContentsMargins(0, 0, 0, 0)
        self.labelRegularPolygonPolygon = QLabel(self.page_regularPolygon)
        self.labelRegularPolygonPolygon.setObjectName(u"labelRegularPolygonPolygon")

        self._27.addWidget(self.labelRegularPolygonPolygon, 0, 0, 1, 1)

        self.regularPolygonPolygon = QSpinBox(self.page_regularPolygon)
        self.regularPolygonPolygon.setObjectName(u"regularPolygonPolygon")
        self.regularPolygonPolygon.setKeyboardTracking(False)
        self.regularPolygonPolygon.setMinimum(3)
        self.regularPolygonPolygon.setMaximum(1000)
        self.regularPolygonPolygon.setValue(6)

        self._27.addWidget(self.regularPolygonPolygon, 0, 1, 1, 1)

        self.labelRegularPolygonCircumradius = QLabel(self.page_regularPolygon)
        self.labelRegularPolygonCircumradius.setObjectName(u"labelRegularPolygonCircumradius")

        self._27.addWidget(self.labelRegularPolygonCircumradius, 1, 0, 1, 1)

        self.regularPolygonCircumradius = Gui_QuantitySpinBox(self.page_regularPolygon)
        self.regularPolygonCircumradius.setObjectName(u"regularPolygonCircumradius")
        self.regularPolygonCircumradius.setKeyboardTracking(False)
        self.regularPolygonCircumradius.setProperty(u"unit", u"mm")
        self.regularPolygonCircumradius.setValue(2.000000000000000)

        self._27.addWidget(self.regularPolygonCircumradius, 1, 1, 1, 1)


        self._26.addLayout(self._27, 0, 0, 1, 1)

        self.spacerItem13 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self._26.addItem(self.spacerItem13, 1, 0, 1, 1)

        self.widgetStack.addWidget(self.page_regularPolygon)

        self.verticalLayout.addWidget(self.widgetStack)


        self.retranslateUi(PartDesignGui__DlgPrimitives)

        self.widgetStack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PartDesignGui__DlgPrimitives)
    # setupUi

    def retranslateUi(self, PartDesignGui__DlgPrimitives):
        PartDesignGui__DlgPrimitives.setWindowTitle(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Geometric Primitives", None))
        self.textLabel2_2.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Length", None))
        self.textLabel3_2.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Width", None))
        self.textLabel2.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Length", None))
        self.textLabel3.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Width", None))
        self.textLabel4.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Height", None))
        self.textLabel5.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius", None))
        self.textLabel6.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Height", None))
        self.labelCylinderXSkew.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle in first direction", None))
#if QT_CONFIG(tooltip)
        self.cylinderXSkew.setToolTip(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle in first direction", None))
#endif // QT_CONFIG(tooltip)
        self.labelCylinderYSkew.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle in second direction", None))
#if QT_CONFIG(tooltip)
        self.cylinderYSkew.setToolTip(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle in second direction", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Rotation angle", None))
        self.textLabel9.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius 1", None))
        self.textLabel10.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius 2", None))
        self.textLabel11.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Height", None))
        self.label_4.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle", None))
        self.textLabel14.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius", None))
        self.label_3.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"U parameter", None))
        self.label_2.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"V parameters", None))
        self.textLabel21.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius 1", None))
#if QT_CONFIG(tooltip)
        self.ellipsoidRadius1.setToolTip(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius in local z-direction", None))
#endif // QT_CONFIG(tooltip)
        self.textLabel22.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius 2", None))
#if QT_CONFIG(tooltip)
        self.ellipsoidRadius2.setToolTip(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius in local X-direction", None))
#endif // QT_CONFIG(tooltip)
        self.textLabel23.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius 3", None))
#if QT_CONFIG(tooltip)
        self.ellipsoidRadius3.setToolTip(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius in local Y-direction\n"
"If zero, it is equal to Radius2", None))
#endif // QT_CONFIG(tooltip)
        self.label23.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"U parameter", None))
        self.label24.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"V parameter", None))
        self.textLabel19.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius 1", None))
#if QT_CONFIG(tooltip)
        self.torusRadius1.setToolTip(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius in local XY-plane", None))
#endif // QT_CONFIG(tooltip)
        self.textLabel20.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius 2", None))
#if QT_CONFIG(tooltip)
        self.torusRadius2.setToolTip(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius in local XZ-plane", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"U parameter", None))
        self.label_6.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"V parameter", None))
        self.labelPrismPolygon.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Polygon", None))
        self.labelPrismCircumradius.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Circumradius", None))
        self.labelPrismHeight.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Height", None))
        self.labelPrismXSkew.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle in first direction", None))
#if QT_CONFIG(tooltip)
        self.prismXSkew.setToolTip(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle in first direction", None))
#endif // QT_CONFIG(tooltip)
        self.labelPrismYSkew.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle in second direction", None))
#if QT_CONFIG(tooltip)
        self.prismYSkew.setToolTip(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle in second direction", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"X min/max", None))
        self.label_11.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Y min/max", None))
        self.label_12.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Z min/max", None))
        self.label_13.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"X2 min/max", None))
        self.label_14.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Z2 min/max", None))
        self.label_7.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Pitch", None))
        self.label_8.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Height", None))
        self.label_9.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius", None))
        self.label_20.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle", None))
        self.label_15.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Coordinate system", None))
        self.helixLocalCS.setItemText(0, QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Right-handed", None))
        self.helixLocalCS.setItemText(1, QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Left-handed", None))

        self.label_spiral_growth.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Growth", None))
        self.label_spiral_rotation.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Number of rotations", None))
        self.label_spiral_radius.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius", None))
        self.Radius.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Radius", None))
        self.Angle1.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle 1", None))
        self.Angle2.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle 2", None))
        self.buttonCircleFromThreePoints.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"From 3 Points", None))
        self.labelEllMajorRadius.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Major radius", None))
        self.labelEllMinorRadius.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Minor radius", None))
        self.labelEllAngle1.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle 1", None))
        self.labelEllAngle2.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Angle 2", None))
        self.label_X_Axis.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"X", None))
        self.label_Y_Axis.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Y", None))
        self.label_Z_Axis.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Z", None))
        self.Start_Vertex.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Start point", None))
        self.X1.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"X", None))
        self.Y1.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Y", None))
        self.Z1.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Z", None))
        self.Finish_Vertex.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"End point", None))
        self.X2.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"X", None))
        self.Y2.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Y", None))
        self.Z2.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Z", None))
        self.labelRegularPolygonPolygon.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Polygon", None))
        self.labelRegularPolygonCircumradius.setText(QCoreApplication.translate("PartDesignGui::DlgPrimitives", u"Circumradius", None))
    # retranslateUi

