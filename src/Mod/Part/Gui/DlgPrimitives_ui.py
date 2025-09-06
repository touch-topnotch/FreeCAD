# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPrimitives.ui'
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
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QWidget)
import Part_rc

class Ui_PartGui_DlgPrimitives(object):
    def setupUi(self, PartGui__DlgPrimitives):
        if not PartGui__DlgPrimitives.objectName():
            PartGui__DlgPrimitives.setObjectName(u"PartGui__DlgPrimitives")
        PartGui__DlgPrimitives.resize(360, 246)
        PartGui__DlgPrimitives.setProperty(u"sizeGripEnabled", True)
        self.gridLayout = QGridLayout(PartGui__DlgPrimitives)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.PrimitiveTypeCB = QComboBox(PartGui__DlgPrimitives)
        icon = QIcon()
        icon.addFile(u":/icons/parametric/Part_Plane_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/icons/parametric/Part_Box_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/icons/parametric/Part_Cylinder_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/icons/parametric/Part_Cone_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/icons/parametric/Part_Sphere_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/icons/parametric/Part_Ellipsoid_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/icons/parametric/Part_Torus_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/icons/parametric/Part_Prism_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u":/icons/parametric/Part_Wedge_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u":/icons/parametric/Part_Helix_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon9, "")
        icon10 = QIcon()
        icon10.addFile(u":/icons/parametric/Part_Spiral_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon10, "")
        icon11 = QIcon()
        icon11.addFile(u":/icons/parametric/Part_Circle_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon11, "")
        icon12 = QIcon()
        icon12.addFile(u":/icons/parametric/Part_Ellipse_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon12, "")
        icon13 = QIcon()
        icon13.addFile(u":/icons/parametric/Part_Point_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon13, "")
        icon14 = QIcon()
        icon14.addFile(u":/icons/parametric/Part_Line_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon14, "")
        icon15 = QIcon()
        icon15.addFile(u":/icons/parametric/Part_Polygon_Parametric.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PrimitiveTypeCB.addItem(icon15, "")
        self.PrimitiveTypeCB.setObjectName(u"PrimitiveTypeCB")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PrimitiveTypeCB.sizePolicy().hasHeightForWidth())
        self.PrimitiveTypeCB.setSizePolicy(sizePolicy)
        self.PrimitiveTypeCB.setMaxVisibleItems(16)

        self.gridLayout.addWidget(self.PrimitiveTypeCB, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(PartGui__DlgPrimitives)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout1 = QGridLayout(self.groupBox_2)
        self.gridLayout1.setSpacing(0)
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(0, 0, 0, 0)
        self.widgetStack2 = QStackedWidget(self.groupBox_2)
        self.widgetStack2.setObjectName(u"widgetStack2")
        self.page0_plane = QWidget()
        self.page0_plane.setObjectName(u"page0_plane")
        self.gridLayout2 = QGridLayout(self.page0_plane)
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayout2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout3 = QGridLayout()
        self.gridLayout3.setSpacing(6)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.gridLayout3.setContentsMargins(0, 0, 0, 0)
        self.textLabel2_2 = QLabel(self.page0_plane)
        self.textLabel2_2.setObjectName(u"textLabel2_2")

        self.gridLayout3.addWidget(self.textLabel2_2, 0, 0, 1, 1)

        self.planeLength = Gui_QuantitySpinBox(self.page0_plane)
        self.planeLength.setObjectName(u"planeLength")
        self.planeLength.setKeyboardTracking(False)
        self.planeLength.setProperty(u"unit", u"mm")
        self.planeLength.setValue(10.000000000000000)

        self.gridLayout3.addWidget(self.planeLength, 0, 2, 1, 1)

        self.textLabel3_2 = QLabel(self.page0_plane)
        self.textLabel3_2.setObjectName(u"textLabel3_2")

        self.gridLayout3.addWidget(self.textLabel3_2, 1, 0, 1, 1)

        self.planeWidth = Gui_QuantitySpinBox(self.page0_plane)
        self.planeWidth.setObjectName(u"planeWidth")
        self.planeWidth.setKeyboardTracking(False)
        self.planeWidth.setProperty(u"unit", u"mm")
        self.planeWidth.setValue(10.000000000000000)

        self.gridLayout3.addWidget(self.planeWidth, 1, 2, 1, 1)


        self.gridLayout2.addLayout(self.gridLayout3, 0, 0, 1, 1)

        self.spacerItem = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout2.addItem(self.spacerItem, 1, 0, 1, 1)

        self.widgetStack2.addWidget(self.page0_plane)
        self.Page1_box = QWidget()
        self.Page1_box.setObjectName(u"Page1_box")
        self.gridLayout4 = QGridLayout(self.Page1_box)
        self.gridLayout4.setSpacing(6)
        self.gridLayout4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.gridLayout4.setContentsMargins(9, 9, 9, 9)
        self.gridLayout5 = QGridLayout()
        self.gridLayout5.setSpacing(6)
        self.gridLayout5.setObjectName(u"gridLayout5")
        self.gridLayout5.setContentsMargins(0, 0, 0, 0)
        self.textLabel2 = QLabel(self.Page1_box)
        self.textLabel2.setObjectName(u"textLabel2")

        self.gridLayout5.addWidget(self.textLabel2, 0, 0, 1, 1)

        self.boxLength = Gui_QuantitySpinBox(self.Page1_box)
        self.boxLength.setObjectName(u"boxLength")
        self.boxLength.setKeyboardTracking(False)
        self.boxLength.setProperty(u"unit", u"mm")
        self.boxLength.setValue(10.000000000000000)

        self.gridLayout5.addWidget(self.boxLength, 0, 2, 1, 1)

        self.textLabel3 = QLabel(self.Page1_box)
        self.textLabel3.setObjectName(u"textLabel3")

        self.gridLayout5.addWidget(self.textLabel3, 1, 0, 1, 1)

        self.boxWidth = Gui_QuantitySpinBox(self.Page1_box)
        self.boxWidth.setObjectName(u"boxWidth")
        self.boxWidth.setKeyboardTracking(False)
        self.boxWidth.setProperty(u"unit", u"mm")
        self.boxWidth.setValue(10.000000000000000)

        self.gridLayout5.addWidget(self.boxWidth, 1, 2, 1, 1)

        self.textLabel4 = QLabel(self.Page1_box)
        self.textLabel4.setObjectName(u"textLabel4")

        self.gridLayout5.addWidget(self.textLabel4, 2, 0, 1, 1)

        self.boxHeight = Gui_QuantitySpinBox(self.Page1_box)
        self.boxHeight.setObjectName(u"boxHeight")
        self.boxHeight.setKeyboardTracking(False)
        self.boxHeight.setProperty(u"unit", u"mm")
        self.boxHeight.setValue(10.000000000000000)

        self.gridLayout5.addWidget(self.boxHeight, 2, 2, 1, 1)


        self.gridLayout4.addLayout(self.gridLayout5, 0, 0, 1, 1)

        self.spacerItem1 = QSpacerItem(20, 51, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout4.addItem(self.spacerItem1, 1, 0, 1, 1)

        self.widgetStack2.addWidget(self.Page1_box)
        self.Page2_cylinder = QWidget()
        self.Page2_cylinder.setObjectName(u"Page2_cylinder")
        self.gridLayout6 = QGridLayout(self.Page2_cylinder)
        self.gridLayout6.setSpacing(6)
        self.gridLayout6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout6.setObjectName(u"gridLayout6")
        self.gridLayout6.setContentsMargins(9, 9, 9, 9)
        self.gridLayout7 = QGridLayout()
        self.gridLayout7.setSpacing(6)
        self.gridLayout7.setObjectName(u"gridLayout7")
        self.gridLayout7.setContentsMargins(0, 0, 0, 0)
        self.textLabel5 = QLabel(self.Page2_cylinder)
        self.textLabel5.setObjectName(u"textLabel5")

        self.gridLayout7.addWidget(self.textLabel5, 0, 0, 1, 1)

        self.cylinderRadius = Gui_QuantitySpinBox(self.Page2_cylinder)
        self.cylinderRadius.setObjectName(u"cylinderRadius")
        self.cylinderRadius.setKeyboardTracking(False)
        self.cylinderRadius.setProperty(u"unit", u"mm")
        self.cylinderRadius.setValue(2.000000000000000)

        self.gridLayout7.addWidget(self.cylinderRadius, 0, 1, 1, 1)

        self.textLabel6 = QLabel(self.Page2_cylinder)
        self.textLabel6.setObjectName(u"textLabel6")

        self.gridLayout7.addWidget(self.textLabel6, 1, 0, 1, 1)

        self.cylinderHeight = Gui_QuantitySpinBox(self.Page2_cylinder)
        self.cylinderHeight.setObjectName(u"cylinderHeight")
        self.cylinderHeight.setKeyboardTracking(False)
        self.cylinderHeight.setProperty(u"unit", u"mm")
        self.cylinderHeight.setValue(10.000000000000000)

        self.gridLayout7.addWidget(self.cylinderHeight, 1, 1, 1, 1)

        self.labelCylinderXSkew = QLabel(self.Page2_cylinder)
        self.labelCylinderXSkew.setObjectName(u"labelCylinderXSkew")

        self.gridLayout7.addWidget(self.labelCylinderXSkew, 2, 0, 1, 1)

        self.cylinderXSkew = Gui_QuantitySpinBox(self.Page2_cylinder)
        self.cylinderXSkew.setObjectName(u"cylinderXSkew")
        self.cylinderXSkew.setKeyboardTracking(False)
        self.cylinderXSkew.setProperty(u"unit", u"deg")
        self.cylinderXSkew.setMinimum(-90.000000000000000)
        self.cylinderXSkew.setMaximum(90.000000000000000)

        self.gridLayout7.addWidget(self.cylinderXSkew, 2, 1, 1, 1)

        self.labelCylinderYSkew = QLabel(self.Page2_cylinder)
        self.labelCylinderYSkew.setObjectName(u"labelCylinderYSkew")

        self.gridLayout7.addWidget(self.labelCylinderYSkew, 3, 0, 1, 1)

        self.cylinderYSkew = Gui_QuantitySpinBox(self.Page2_cylinder)
        self.cylinderYSkew.setObjectName(u"cylinderYSkew")
        self.cylinderYSkew.setKeyboardTracking(False)
        self.cylinderYSkew.setProperty(u"unit", u"deg")
        self.cylinderYSkew.setMinimum(-90.000000000000000)
        self.cylinderYSkew.setMaximum(90.000000000000000)

        self.gridLayout7.addWidget(self.cylinderYSkew, 3, 1, 1, 1)


        self.gridLayout6.addLayout(self.gridLayout7, 0, 0, 1, 1)

        self.line_2 = QFrame(self.Page2_cylinder)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout6.addWidget(self.line_2, 1, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.Page2_cylinder)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(123, 0))

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)

        self.cylinderAngle = Gui_QuantitySpinBox(self.Page2_cylinder)
        self.cylinderAngle.setObjectName(u"cylinderAngle")
        self.cylinderAngle.setKeyboardTracking(False)
        self.cylinderAngle.setProperty(u"unit", u"deg")
        self.cylinderAngle.setValue(360.000000000000000)

        self.gridLayout_7.addWidget(self.cylinderAngle, 0, 1, 1, 1)


        self.gridLayout6.addLayout(self.gridLayout_7, 2, 0, 1, 1)

        self.spacerItem2 = QSpacerItem(31, 81, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout6.addItem(self.spacerItem2, 3, 0, 1, 1)

        self.widgetStack2.addWidget(self.Page2_cylinder)
        self.Page3_cone = QWidget()
        self.Page3_cone.setObjectName(u"Page3_cone")
        self.gridLayout8 = QGridLayout(self.Page3_cone)
        self.gridLayout8.setSpacing(6)
        self.gridLayout8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout8.setObjectName(u"gridLayout8")
        self.gridLayout8.setContentsMargins(9, 9, 9, 9)
        self.gridLayout9 = QGridLayout()
        self.gridLayout9.setSpacing(6)
        self.gridLayout9.setObjectName(u"gridLayout9")
        self.gridLayout9.setContentsMargins(0, 0, 0, 0)
        self.textLabel9 = QLabel(self.Page3_cone)
        self.textLabel9.setObjectName(u"textLabel9")

        self.gridLayout9.addWidget(self.textLabel9, 0, 0, 1, 1)

        self.coneRadius1 = Gui_QuantitySpinBox(self.Page3_cone)
        self.coneRadius1.setObjectName(u"coneRadius1")
        self.coneRadius1.setKeyboardTracking(False)
        self.coneRadius1.setProperty(u"unit", u"mm")
        self.coneRadius1.setValue(2.000000000000000)

        self.gridLayout9.addWidget(self.coneRadius1, 0, 2, 1, 1)

        self.textLabel10 = QLabel(self.Page3_cone)
        self.textLabel10.setObjectName(u"textLabel10")

        self.gridLayout9.addWidget(self.textLabel10, 1, 0, 1, 1)

        self.coneRadius2 = Gui_QuantitySpinBox(self.Page3_cone)
        self.coneRadius2.setObjectName(u"coneRadius2")
        self.coneRadius2.setKeyboardTracking(False)
        self.coneRadius2.setProperty(u"unit", u"mm")
        self.coneRadius2.setValue(4.000000000000000)

        self.gridLayout9.addWidget(self.coneRadius2, 1, 2, 1, 1)

        self.textLabel11 = QLabel(self.Page3_cone)
        self.textLabel11.setObjectName(u"textLabel11")

        self.gridLayout9.addWidget(self.textLabel11, 2, 0, 2, 1)

        self.coneHeight = Gui_QuantitySpinBox(self.Page3_cone)
        self.coneHeight.setObjectName(u"coneHeight")
        self.coneHeight.setKeyboardTracking(False)
        self.coneHeight.setProperty(u"unit", u"mm")
        self.coneHeight.setValue(10.000000000000000)

        self.gridLayout9.addWidget(self.coneHeight, 3, 2, 1, 1)


        self.gridLayout8.addLayout(self.gridLayout9, 0, 0, 1, 1)

        self.line_3 = QFrame(self.Page3_cone)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout8.addWidget(self.line_3, 1, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setSpacing(6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.Page3_cone)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_12.addWidget(self.label_4, 0, 0, 1, 1)

        self.coneAngle = Gui_QuantitySpinBox(self.Page3_cone)
        self.coneAngle.setObjectName(u"coneAngle")
        self.coneAngle.setKeyboardTracking(False)
        self.coneAngle.setProperty(u"unit", u"deg")
        self.coneAngle.setValue(360.000000000000000)

        self.gridLayout_12.addWidget(self.coneAngle, 0, 1, 1, 1)


        self.gridLayout8.addLayout(self.gridLayout_12, 2, 0, 1, 1)

        self.spacerItem3 = QSpacerItem(31, 91, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout8.addItem(self.spacerItem3, 3, 0, 1, 1)

        self.widgetStack2.addWidget(self.Page3_cone)
        self.Page4_sphere = QWidget()
        self.Page4_sphere.setObjectName(u"Page4_sphere")
        self.gridLayout10 = QGridLayout(self.Page4_sphere)
        self.gridLayout10.setSpacing(6)
        self.gridLayout10.setContentsMargins(11, 11, 11, 11)
        self.gridLayout10.setObjectName(u"gridLayout10")
        self.gridLayout10.setContentsMargins(9, 9, 9, 9)
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.textLabel14 = QLabel(self.Page4_sphere)
        self.textLabel14.setObjectName(u"textLabel14")

        self.hboxLayout.addWidget(self.textLabel14)

        self.sphereRadius = Gui_QuantitySpinBox(self.Page4_sphere)
        self.sphereRadius.setObjectName(u"sphereRadius")
        self.sphereRadius.setKeyboardTracking(False)
        self.sphereRadius.setProperty(u"unit", u"mm")
        self.sphereRadius.setValue(5.000000000000000)

        self.hboxLayout.addWidget(self.sphereRadius)


        self.gridLayout10.addLayout(self.hboxLayout, 0, 0, 1, 1)

        self.line = QFrame(self.Page4_sphere)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout10.addWidget(self.line, 1, 0, 1, 1)

        self.gridLayout11 = QGridLayout()
        self.gridLayout11.setSpacing(6)
        self.gridLayout11.setObjectName(u"gridLayout11")
        self.gridLayout11.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.Page4_sphere)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout11.addWidget(self.label_3, 0, 0, 1, 1)

        self.sphereAngle3 = Gui_QuantitySpinBox(self.Page4_sphere)
        self.sphereAngle3.setObjectName(u"sphereAngle3")
        self.sphereAngle3.setKeyboardTracking(False)
        self.sphereAngle3.setProperty(u"unit", u"deg")
        self.sphereAngle3.setValue(360.000000000000000)

        self.gridLayout11.addWidget(self.sphereAngle3, 0, 2, 1, 1)

        self.label_2 = QLabel(self.Page4_sphere)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout11.addWidget(self.label_2, 1, 0, 1, 1)

        self.sphereAngle1 = Gui_QuantitySpinBox(self.Page4_sphere)
        self.sphereAngle1.setObjectName(u"sphereAngle1")
        self.sphereAngle1.setKeyboardTracking(False)
        self.sphereAngle1.setProperty(u"unit", u"deg")
        self.sphereAngle1.setValue(-90.000000000000000)

        self.gridLayout11.addWidget(self.sphereAngle1, 1, 2, 1, 1)

        self.spacerItem4 = QSpacerItem(81, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout11.addItem(self.spacerItem4, 2, 0, 1, 1)

        self.sphereAngle2 = Gui_QuantitySpinBox(self.Page4_sphere)
        self.sphereAngle2.setObjectName(u"sphereAngle2")
        self.sphereAngle2.setKeyboardTracking(False)
        self.sphereAngle2.setProperty(u"unit", u"deg")
        self.sphereAngle2.setValue(90.000000000000000)

        self.gridLayout11.addWidget(self.sphereAngle2, 2, 2, 1, 1)


        self.gridLayout10.addLayout(self.gridLayout11, 2, 0, 1, 1)

        self.spacerItem5 = QSpacerItem(21, 151, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout10.addItem(self.spacerItem5, 3, 0, 1, 1)

        self.widgetStack2.addWidget(self.Page4_sphere)
        self.Page5_ellipsoid = QWidget()
        self.Page5_ellipsoid.setObjectName(u"Page5_ellipsoid")
        self.gridLayout12 = QGridLayout(self.Page5_ellipsoid)
        self.gridLayout12.setSpacing(6)
        self.gridLayout12.setContentsMargins(11, 11, 11, 11)
        self.gridLayout12.setObjectName(u"gridLayout12")
        self.gridLayout12.setContentsMargins(9, 9, 9, 9)
        self.gridLayout13 = QGridLayout()
        self.gridLayout13.setSpacing(6)
        self.gridLayout13.setObjectName(u"gridLayout13")
        self.gridLayout13.setContentsMargins(0, 0, 0, 0)
        self.textLabel21 = QLabel(self.Page5_ellipsoid)
        self.textLabel21.setObjectName(u"textLabel21")

        self.gridLayout13.addWidget(self.textLabel21, 0, 0, 1, 1)

        self.ellipsoidRadius1 = Gui_QuantitySpinBox(self.Page5_ellipsoid)
        self.ellipsoidRadius1.setObjectName(u"ellipsoidRadius1")
        self.ellipsoidRadius1.setKeyboardTracking(False)
        self.ellipsoidRadius1.setProperty(u"unit", u"mm")
        self.ellipsoidRadius1.setValue(2.000000000000000)

        self.gridLayout13.addWidget(self.ellipsoidRadius1, 0, 1, 1, 1)

        self.textLabel22 = QLabel(self.Page5_ellipsoid)
        self.textLabel22.setObjectName(u"textLabel22")

        self.gridLayout13.addWidget(self.textLabel22, 1, 0, 1, 1)

        self.ellipsoidRadius2 = Gui_QuantitySpinBox(self.Page5_ellipsoid)
        self.ellipsoidRadius2.setObjectName(u"ellipsoidRadius2")
        self.ellipsoidRadius2.setKeyboardTracking(False)
        self.ellipsoidRadius2.setProperty(u"unit", u"mm")
        self.ellipsoidRadius2.setValue(4.000000000000000)

        self.gridLayout13.addWidget(self.ellipsoidRadius2, 1, 1, 1, 1)

        self.textLabel23 = QLabel(self.Page5_ellipsoid)
        self.textLabel23.setObjectName(u"textLabel23")

        self.gridLayout13.addWidget(self.textLabel23, 2, 0, 1, 1)

        self.ellipsoidRadius3 = Gui_QuantitySpinBox(self.Page5_ellipsoid)
        self.ellipsoidRadius3.setObjectName(u"ellipsoidRadius3")
        self.ellipsoidRadius3.setKeyboardTracking(False)
        self.ellipsoidRadius3.setProperty(u"unit", u"mm")
        self.ellipsoidRadius3.setValue(4.000000000000000)

        self.gridLayout13.addWidget(self.ellipsoidRadius3, 2, 1, 1, 1)


        self.gridLayout12.addLayout(self.gridLayout13, 0, 0, 1, 1)

        self.line_5 = QFrame(self.Page5_ellipsoid)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout12.addWidget(self.line_5, 1, 0, 1, 1)

        self.gridLayout14 = QGridLayout()
        self.gridLayout14.setSpacing(6)
        self.gridLayout14.setObjectName(u"gridLayout14")
        self.gridLayout14.setContentsMargins(0, 0, 0, 0)
        self.label23 = QLabel(self.Page5_ellipsoid)
        self.label23.setObjectName(u"label23")

        self.gridLayout14.addWidget(self.label23, 0, 0, 1, 1)

        self.ellipsoidAngle3 = Gui_QuantitySpinBox(self.Page5_ellipsoid)
        self.ellipsoidAngle3.setObjectName(u"ellipsoidAngle3")
        self.ellipsoidAngle3.setKeyboardTracking(False)
        self.ellipsoidAngle3.setProperty(u"unit", u"deg")
        self.ellipsoidAngle3.setValue(360.000000000000000)

        self.gridLayout14.addWidget(self.ellipsoidAngle3, 0, 1, 1, 1)

        self.label24 = QLabel(self.Page5_ellipsoid)
        self.label24.setObjectName(u"label24")

        self.gridLayout14.addWidget(self.label24, 1, 0, 1, 1)

        self.ellipsoidAngle1 = Gui_QuantitySpinBox(self.Page5_ellipsoid)
        self.ellipsoidAngle1.setObjectName(u"ellipsoidAngle1")
        self.ellipsoidAngle1.setKeyboardTracking(False)
        self.ellipsoidAngle1.setProperty(u"unit", u"deg")
        self.ellipsoidAngle1.setValue(-90.000000000000000)

        self.gridLayout14.addWidget(self.ellipsoidAngle1, 1, 1, 1, 1)

        self.spacerItem6 = QSpacerItem(81, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout14.addItem(self.spacerItem6, 2, 0, 1, 1)

        self.ellipsoidAngle2 = Gui_QuantitySpinBox(self.Page5_ellipsoid)
        self.ellipsoidAngle2.setObjectName(u"ellipsoidAngle2")
        self.ellipsoidAngle2.setKeyboardTracking(False)
        self.ellipsoidAngle2.setProperty(u"unit", u"deg")
        self.ellipsoidAngle2.setValue(90.000000000000000)

        self.gridLayout14.addWidget(self.ellipsoidAngle2, 2, 1, 1, 1)


        self.gridLayout12.addLayout(self.gridLayout14, 2, 0, 1, 1)

        self.spacerItem7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout12.addItem(self.spacerItem7, 3, 0, 1, 1)

        self.widgetStack2.addWidget(self.Page5_ellipsoid)
        self.Page6_torus = QWidget()
        self.Page6_torus.setObjectName(u"Page6_torus")
        self.gridLayout15 = QGridLayout(self.Page6_torus)
        self.gridLayout15.setSpacing(6)
        self.gridLayout15.setContentsMargins(11, 11, 11, 11)
        self.gridLayout15.setObjectName(u"gridLayout15")
        self.gridLayout15.setContentsMargins(9, 9, 9, 9)
        self.gridLayout16 = QGridLayout()
        self.gridLayout16.setSpacing(6)
        self.gridLayout16.setObjectName(u"gridLayout16")
        self.gridLayout16.setContentsMargins(0, 0, 0, 0)
        self.textLabel19 = QLabel(self.Page6_torus)
        self.textLabel19.setObjectName(u"textLabel19")

        self.gridLayout16.addWidget(self.textLabel19, 0, 0, 1, 1)

        self.torusRadius1 = Gui_QuantitySpinBox(self.Page6_torus)
        self.torusRadius1.setObjectName(u"torusRadius1")
        self.torusRadius1.setKeyboardTracking(False)
        self.torusRadius1.setProperty(u"unit", u"mm")
        self.torusRadius1.setValue(10.000000000000000)

        self.gridLayout16.addWidget(self.torusRadius1, 0, 2, 1, 1)

        self.textLabel20 = QLabel(self.Page6_torus)
        self.textLabel20.setObjectName(u"textLabel20")

        self.gridLayout16.addWidget(self.textLabel20, 1, 0, 1, 1)

        self.torusRadius2 = Gui_QuantitySpinBox(self.Page6_torus)
        self.torusRadius2.setObjectName(u"torusRadius2")
        self.torusRadius2.setKeyboardTracking(False)
        self.torusRadius2.setProperty(u"unit", u"mm")
        self.torusRadius2.setValue(2.000000000000000)

        self.gridLayout16.addWidget(self.torusRadius2, 1, 2, 1, 1)


        self.gridLayout15.addLayout(self.gridLayout16, 0, 0, 1, 1)

        self.line_4 = QFrame(self.Page6_torus)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout15.addWidget(self.line_4, 1, 0, 1, 1)

        self.gridLayout17 = QGridLayout()
        self.gridLayout17.setSpacing(6)
        self.gridLayout17.setObjectName(u"gridLayout17")
        self.gridLayout17.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.Page6_torus)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout17.addWidget(self.label_5, 0, 0, 1, 1)

        self.torusAngle3 = Gui_QuantitySpinBox(self.Page6_torus)
        self.torusAngle3.setObjectName(u"torusAngle3")
        self.torusAngle3.setKeyboardTracking(False)
        self.torusAngle3.setProperty(u"unit", u"deg")
        self.torusAngle3.setValue(360.000000000000000)

        self.gridLayout17.addWidget(self.torusAngle3, 0, 1, 1, 1)

        self.label_6 = QLabel(self.Page6_torus)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout17.addWidget(self.label_6, 1, 0, 1, 1)

        self.torusAngle1 = Gui_QuantitySpinBox(self.Page6_torus)
        self.torusAngle1.setObjectName(u"torusAngle1")
        self.torusAngle1.setKeyboardTracking(False)
        self.torusAngle1.setProperty(u"unit", u"deg")
        self.torusAngle1.setValue(-180.000000000000000)

        self.gridLayout17.addWidget(self.torusAngle1, 1, 1, 1, 1)

        self.spacerItem8 = QSpacerItem(81, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout17.addItem(self.spacerItem8, 2, 0, 1, 1)

        self.torusAngle2 = Gui_QuantitySpinBox(self.Page6_torus)
        self.torusAngle2.setObjectName(u"torusAngle2")
        self.torusAngle2.setKeyboardTracking(False)
        self.torusAngle2.setProperty(u"unit", u"deg")
        self.torusAngle2.setValue(180.000000000000000)

        self.gridLayout17.addWidget(self.torusAngle2, 2, 1, 1, 1)


        self.gridLayout15.addLayout(self.gridLayout17, 2, 0, 1, 1)

        self.spacerItem9 = QSpacerItem(20, 91, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout15.addItem(self.spacerItem9, 3, 0, 1, 1)

        self.widgetStack2.addWidget(self.Page6_torus)
        self.page_prism = QWidget()
        self.page_prism.setObjectName(u"page_prism")
        self.gridLayout18 = QGridLayout(self.page_prism)
        self.gridLayout18.setSpacing(6)
        self.gridLayout18.setContentsMargins(11, 11, 11, 11)
        self.gridLayout18.setObjectName(u"gridLayout18")
        self.gridLayout18.setContentsMargins(9, 9, 9, 9)
        self.gridLayout19 = QGridLayout()
        self.gridLayout19.setSpacing(6)
        self.gridLayout19.setObjectName(u"gridLayout19")
        self.gridLayout19.setContentsMargins(0, 0, 0, 0)
        self.labelPrismPolygon = QLabel(self.page_prism)
        self.labelPrismPolygon.setObjectName(u"labelPrismPolygon")

        self.gridLayout19.addWidget(self.labelPrismPolygon, 0, 0, 1, 1)

        self.prismPolygon = QSpinBox(self.page_prism)
        self.prismPolygon.setObjectName(u"prismPolygon")
        self.prismPolygon.setKeyboardTracking(False)
        self.prismPolygon.setMinimum(3)
        self.prismPolygon.setMaximum(1000)
        self.prismPolygon.setValue(6)

        self.gridLayout19.addWidget(self.prismPolygon, 0, 2, 1, 1)

        self.labelPrismCircumradius = QLabel(self.page_prism)
        self.labelPrismCircumradius.setObjectName(u"labelPrismCircumradius")

        self.gridLayout19.addWidget(self.labelPrismCircumradius, 1, 0, 1, 1)

        self.prismCircumradius = Gui_QuantitySpinBox(self.page_prism)
        self.prismCircumradius.setObjectName(u"prismCircumradius")
        self.prismCircumradius.setKeyboardTracking(False)
        self.prismCircumradius.setProperty(u"unit", u"mm")
        self.prismCircumradius.setValue(2.000000000000000)

        self.gridLayout19.addWidget(self.prismCircumradius, 1, 2, 1, 1)

        self.labelPrismHeight = QLabel(self.page_prism)
        self.labelPrismHeight.setObjectName(u"labelPrismHeight")

        self.gridLayout19.addWidget(self.labelPrismHeight, 2, 0, 1, 1)

        self.prismHeight = Gui_QuantitySpinBox(self.page_prism)
        self.prismHeight.setObjectName(u"prismHeight")
        self.prismHeight.setKeyboardTracking(False)
        self.prismHeight.setProperty(u"unit", u"mm")
        self.prismHeight.setValue(10.000000000000000)

        self.gridLayout19.addWidget(self.prismHeight, 2, 2, 1, 1)

        self.labelPrismXSkew = QLabel(self.page_prism)
        self.labelPrismXSkew.setObjectName(u"labelPrismXSkew")

        self.gridLayout19.addWidget(self.labelPrismXSkew, 3, 0, 1, 1)

        self.prismXSkew = Gui_QuantitySpinBox(self.page_prism)
        self.prismXSkew.setObjectName(u"prismXSkew")
        self.prismXSkew.setKeyboardTracking(False)
        self.prismXSkew.setProperty(u"unit", u"deg")
        self.prismXSkew.setMinimum(-90.000000000000000)
        self.prismXSkew.setMaximum(90.000000000000000)

        self.gridLayout19.addWidget(self.prismXSkew, 3, 2, 1, 1)

        self.labelPrismYSkew = QLabel(self.page_prism)
        self.labelPrismYSkew.setObjectName(u"labelPrismYSkew")

        self.gridLayout19.addWidget(self.labelPrismYSkew, 4, 0, 1, 1)

        self.prismYSkew = Gui_QuantitySpinBox(self.page_prism)
        self.prismYSkew.setObjectName(u"prismYSkew")
        self.prismYSkew.setKeyboardTracking(False)
        self.prismYSkew.setProperty(u"unit", u"deg")
        self.prismYSkew.setMinimum(-90.000000000000000)
        self.prismYSkew.setMaximum(90.000000000000000)

        self.gridLayout19.addWidget(self.prismYSkew, 4, 2, 1, 1)


        self.gridLayout18.addLayout(self.gridLayout19, 0, 0, 1, 1)

        self.spacerItem10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout18.addItem(self.spacerItem10, 1, 0, 1, 1)

        self.widgetStack2.addWidget(self.page_prism)
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

        self.verticalSpacer_2 = QSpacerItem(20, 81, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.widgetStack2.addWidget(self.page7_wedge)
        self.page8_helix = QWidget()
        self.page8_helix.setObjectName(u"page8_helix")
        self.gridLayout20 = QGridLayout(self.page8_helix)
        self.gridLayout20.setSpacing(6)
        self.gridLayout20.setContentsMargins(11, 11, 11, 11)
        self.gridLayout20.setObjectName(u"gridLayout20")
        self.gridLayout20.setContentsMargins(9, 9, 9, 9)
        self.gridLayout21 = QGridLayout()
        self.gridLayout21.setSpacing(6)
        self.gridLayout21.setObjectName(u"gridLayout21")
        self.gridLayout21.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.page8_helix)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout21.addWidget(self.label_7, 0, 0, 1, 1)

        self.helixPitch = Gui_QuantitySpinBox(self.page8_helix)
        self.helixPitch.setObjectName(u"helixPitch")
        self.helixPitch.setKeyboardTracking(False)
        self.helixPitch.setProperty(u"unit", u"mm")
        self.helixPitch.setValue(1.000000000000000)

        self.gridLayout21.addWidget(self.helixPitch, 0, 1, 1, 1)

        self.label_8 = QLabel(self.page8_helix)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout21.addWidget(self.label_8, 1, 0, 1, 1)

        self.helixHeight = Gui_QuantitySpinBox(self.page8_helix)
        self.helixHeight.setObjectName(u"helixHeight")
        self.helixHeight.setKeyboardTracking(False)
        self.helixHeight.setProperty(u"unit", u"mm")
        self.helixHeight.setValue(2.000000000000000)

        self.gridLayout21.addWidget(self.helixHeight, 1, 1, 1, 1)

        self.label_9 = QLabel(self.page8_helix)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout21.addWidget(self.label_9, 2, 0, 1, 1)

        self.helixRadius = Gui_QuantitySpinBox(self.page8_helix)
        self.helixRadius.setObjectName(u"helixRadius")
        self.helixRadius.setKeyboardTracking(False)
        self.helixRadius.setProperty(u"unit", u"mm")
        self.helixRadius.setValue(1.000000000000000)

        self.gridLayout21.addWidget(self.helixRadius, 2, 1, 1, 1)

        self.label_20 = QLabel(self.page8_helix)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout21.addWidget(self.label_20, 3, 0, 1, 1)

        self.helixAngle = Gui_QuantitySpinBox(self.page8_helix)
        self.helixAngle.setObjectName(u"helixAngle")
        self.helixAngle.setKeyboardTracking(False)
        self.helixAngle.setProperty(u"unit", u"deg")

        self.gridLayout21.addWidget(self.helixAngle, 3, 1, 1, 1)

        self.label_15 = QLabel(self.page8_helix)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout21.addWidget(self.label_15, 4, 0, 1, 1)

        self.helixLocalCS = QComboBox(self.page8_helix)
        self.helixLocalCS.addItem("")
        self.helixLocalCS.addItem("")
        self.helixLocalCS.setObjectName(u"helixLocalCS")

        self.gridLayout21.addWidget(self.helixLocalCS, 4, 1, 1, 1)


        self.gridLayout20.addLayout(self.gridLayout21, 0, 0, 1, 1)

        self.spacerItem11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout20.addItem(self.spacerItem11, 1, 0, 1, 1)

        self.widgetStack2.addWidget(self.page8_helix)
        self.page9_spiral = QWidget()
        self.page9_spiral.setObjectName(u"page9_spiral")
        self.gridLayout22 = QGridLayout(self.page9_spiral)
        self.gridLayout22.setSpacing(6)
        self.gridLayout22.setContentsMargins(11, 11, 11, 11)
        self.gridLayout22.setObjectName(u"gridLayout22")
        self.gridLayout22.setContentsMargins(9, 9, 9, 9)
        self.gridLayout23 = QGridLayout()
        self.gridLayout23.setSpacing(6)
        self.gridLayout23.setObjectName(u"gridLayout23")
        self.gridLayout23.setContentsMargins(0, 0, 0, 0)
        self.label_spiral_growth = QLabel(self.page9_spiral)
        self.label_spiral_growth.setObjectName(u"label_spiral_growth")

        self.gridLayout23.addWidget(self.label_spiral_growth, 0, 0, 1, 1)

        self.spiralGrowth = Gui_QuantitySpinBox(self.page9_spiral)
        self.spiralGrowth.setObjectName(u"spiralGrowth")
        self.spiralGrowth.setKeyboardTracking(False)
        self.spiralGrowth.setProperty(u"unit", u"mm")
        self.spiralGrowth.setValue(1.000000000000000)

        self.gridLayout23.addWidget(self.spiralGrowth, 0, 1, 1, 1)

        self.label_spiral_rotation = QLabel(self.page9_spiral)
        self.label_spiral_rotation.setObjectName(u"label_spiral_rotation")

        self.gridLayout23.addWidget(self.label_spiral_rotation, 1, 0, 1, 1)

        self.spiralRotation = QDoubleSpinBox(self.page9_spiral)
        self.spiralRotation.setObjectName(u"spiralRotation")
        self.spiralRotation.setKeyboardTracking(False)
        self.spiralRotation.setMaximum(1000.000000000000000)
        self.spiralRotation.setValue(2.000000000000000)

        self.gridLayout23.addWidget(self.spiralRotation, 1, 1, 1, 1)

        self.label_spiral_radius = QLabel(self.page9_spiral)
        self.label_spiral_radius.setObjectName(u"label_spiral_radius")

        self.gridLayout23.addWidget(self.label_spiral_radius, 2, 0, 1, 1)

        self.spiralRadius = Gui_QuantitySpinBox(self.page9_spiral)
        self.spiralRadius.setObjectName(u"spiralRadius")
        self.spiralRadius.setKeyboardTracking(False)
        self.spiralRadius.setProperty(u"unit", u"mm")
        self.spiralRadius.setValue(1.000000000000000)

        self.gridLayout23.addWidget(self.spiralRadius, 2, 1, 1, 1)


        self.gridLayout22.addLayout(self.gridLayout23, 0, 0, 1, 1)

        self.spacerItem12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout22.addItem(self.spacerItem12, 1, 0, 1, 1)

        self.widgetStack2.addWidget(self.page9_spiral)
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

        self.verticalSpacer = QSpacerItem(20, 95, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.widgetStack2.addWidget(self.page10_circle)
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

        self.verticalSpacer_5 = QSpacerItem(20, 131, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.widgetStack2.addWidget(self.page)
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

        self.verticalSpacer_3 = QSpacerItem(20, 139, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.widgetStack2.addWidget(self.page11_vertex)
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

        self.gridLayout_5.addWidget(self.Start_Vertex, 0, 1, 1, 1)

        self.Finish_Vertex = QLabel(self.page12_edge)
        self.Finish_Vertex.setObjectName(u"Finish_Vertex")
        self.Finish_Vertex.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.Finish_Vertex, 0, 2, 1, 1)

        self.X1 = QLabel(self.page12_edge)
        self.X1.setObjectName(u"X1")
        self.X1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.X1, 1, 0, 1, 1)

        self.edgeX1 = Gui_QuantitySpinBox(self.page12_edge)
        self.edgeX1.setObjectName(u"edgeX1")
        self.edgeX1.setKeyboardTracking(False)
        self.edgeX1.setProperty(u"unit", u"mm")

        self.gridLayout_5.addWidget(self.edgeX1, 1, 1, 1, 1)

        self.edgeX2 = Gui_QuantitySpinBox(self.page12_edge)
        self.edgeX2.setObjectName(u"edgeX2")
        self.edgeX2.setKeyboardTracking(False)
        self.edgeX2.setProperty(u"unit", u"mm")
        self.edgeX2.setValue(10.000000000000000)

        self.gridLayout_5.addWidget(self.edgeX2, 1, 2, 1, 1)

        self.Y1 = QLabel(self.page12_edge)
        self.Y1.setObjectName(u"Y1")
        self.Y1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.Y1, 2, 0, 1, 1)

        self.edgeY1 = Gui_QuantitySpinBox(self.page12_edge)
        self.edgeY1.setObjectName(u"edgeY1")
        self.edgeY1.setKeyboardTracking(False)
        self.edgeY1.setProperty(u"unit", u"mm")

        self.gridLayout_5.addWidget(self.edgeY1, 2, 1, 1, 1)

        self.edgeY2 = Gui_QuantitySpinBox(self.page12_edge)
        self.edgeY2.setObjectName(u"edgeY2")
        self.edgeY2.setKeyboardTracking(False)
        self.edgeY2.setProperty(u"unit", u"mm")
        self.edgeY2.setValue(10.000000000000000)

        self.gridLayout_5.addWidget(self.edgeY2, 2, 2, 1, 1)

        self.Z1 = QLabel(self.page12_edge)
        self.Z1.setObjectName(u"Z1")
        self.Z1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.Z1, 3, 0, 1, 1)

        self.edgeZ1 = Gui_QuantitySpinBox(self.page12_edge)
        self.edgeZ1.setObjectName(u"edgeZ1")
        self.edgeZ1.setKeyboardTracking(False)
        self.edgeZ1.setProperty(u"unit", u"mm")

        self.gridLayout_5.addWidget(self.edgeZ1, 3, 1, 1, 1)

        self.edgeZ2 = Gui_QuantitySpinBox(self.page12_edge)
        self.edgeZ2.setObjectName(u"edgeZ2")
        self.edgeZ2.setKeyboardTracking(False)
        self.edgeZ2.setProperty(u"unit", u"mm")
        self.edgeZ2.setValue(10.000000000000000)

        self.gridLayout_5.addWidget(self.edgeZ2, 3, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 81, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.widgetStack2.addWidget(self.page12_edge)
        self.page_regularPolygon = QWidget()
        self.page_regularPolygon.setObjectName(u"page_regularPolygon")
        self.gridLayout24 = QGridLayout(self.page_regularPolygon)
        self.gridLayout24.setSpacing(6)
        self.gridLayout24.setContentsMargins(11, 11, 11, 11)
        self.gridLayout24.setObjectName(u"gridLayout24")
        self.gridLayout24.setContentsMargins(9, 9, 9, 9)
        self.gridLayout25 = QGridLayout()
        self.gridLayout25.setSpacing(6)
        self.gridLayout25.setObjectName(u"gridLayout25")
        self.gridLayout25.setContentsMargins(0, 0, 0, 0)
        self.labelRegularPolygonPolygon = QLabel(self.page_regularPolygon)
        self.labelRegularPolygonPolygon.setObjectName(u"labelRegularPolygonPolygon")

        self.gridLayout25.addWidget(self.labelRegularPolygonPolygon, 0, 0, 1, 1)

        self.regularPolygonPolygon = QSpinBox(self.page_regularPolygon)
        self.regularPolygonPolygon.setObjectName(u"regularPolygonPolygon")
        self.regularPolygonPolygon.setKeyboardTracking(False)
        self.regularPolygonPolygon.setMinimum(3)
        self.regularPolygonPolygon.setMaximum(1000)
        self.regularPolygonPolygon.setValue(6)

        self.gridLayout25.addWidget(self.regularPolygonPolygon, 0, 1, 1, 1)

        self.labelRegularPolygonCircumradius = QLabel(self.page_regularPolygon)
        self.labelRegularPolygonCircumradius.setObjectName(u"labelRegularPolygonCircumradius")

        self.gridLayout25.addWidget(self.labelRegularPolygonCircumradius, 1, 0, 1, 1)

        self.regularPolygonCircumradius = Gui_QuantitySpinBox(self.page_regularPolygon)
        self.regularPolygonCircumradius.setObjectName(u"regularPolygonCircumradius")
        self.regularPolygonCircumradius.setKeyboardTracking(False)
        self.regularPolygonCircumradius.setProperty(u"unit", u"mm")
        self.regularPolygonCircumradius.setValue(2.000000000000000)

        self.gridLayout25.addWidget(self.regularPolygonCircumradius, 1, 1, 1, 1)


        self.gridLayout24.addLayout(self.gridLayout25, 0, 0, 1, 1)

        self.spacerItem13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout24.addItem(self.spacerItem13, 1, 0, 1, 1)

        self.widgetStack2.addWidget(self.page_regularPolygon)

        self.gridLayout1.addWidget(self.widgetStack2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        QWidget.setTabOrder(self.PrimitiveTypeCB, self.planeLength)
        QWidget.setTabOrder(self.planeLength, self.planeWidth)
        QWidget.setTabOrder(self.planeWidth, self.boxLength)
        QWidget.setTabOrder(self.boxLength, self.boxWidth)
        QWidget.setTabOrder(self.boxWidth, self.boxHeight)
        QWidget.setTabOrder(self.boxHeight, self.cylinderRadius)
        QWidget.setTabOrder(self.cylinderRadius, self.cylinderHeight)
        QWidget.setTabOrder(self.cylinderHeight, self.cylinderAngle)
        QWidget.setTabOrder(self.cylinderAngle, self.coneRadius1)
        QWidget.setTabOrder(self.coneRadius1, self.coneRadius2)
        QWidget.setTabOrder(self.coneRadius2, self.coneHeight)
        QWidget.setTabOrder(self.coneHeight, self.coneAngle)
        QWidget.setTabOrder(self.coneAngle, self.sphereRadius)
        QWidget.setTabOrder(self.sphereRadius, self.sphereAngle3)
        QWidget.setTabOrder(self.sphereAngle3, self.sphereAngle1)
        QWidget.setTabOrder(self.sphereAngle1, self.sphereAngle2)
        QWidget.setTabOrder(self.sphereAngle2, self.ellipsoidRadius1)
        QWidget.setTabOrder(self.ellipsoidRadius1, self.ellipsoidRadius2)
        QWidget.setTabOrder(self.ellipsoidRadius2, self.ellipsoidRadius3)
        QWidget.setTabOrder(self.ellipsoidRadius3, self.ellipsoidAngle3)
        QWidget.setTabOrder(self.ellipsoidAngle3, self.ellipsoidAngle1)
        QWidget.setTabOrder(self.ellipsoidAngle1, self.ellipsoidAngle2)
        QWidget.setTabOrder(self.ellipsoidAngle2, self.torusRadius1)
        QWidget.setTabOrder(self.torusRadius1, self.torusRadius2)
        QWidget.setTabOrder(self.torusRadius2, self.torusAngle3)
        QWidget.setTabOrder(self.torusAngle3, self.torusAngle1)
        QWidget.setTabOrder(self.torusAngle1, self.torusAngle2)
        QWidget.setTabOrder(self.torusAngle2, self.prismPolygon)
        QWidget.setTabOrder(self.prismPolygon, self.prismCircumradius)
        QWidget.setTabOrder(self.prismCircumradius, self.prismHeight)
        QWidget.setTabOrder(self.prismHeight, self.wedgeXmin)
        QWidget.setTabOrder(self.wedgeXmin, self.wedgeXmax)
        QWidget.setTabOrder(self.wedgeXmax, self.wedgeYmin)
        QWidget.setTabOrder(self.wedgeYmin, self.wedgeYmax)
        QWidget.setTabOrder(self.wedgeYmax, self.wedgeZmin)
        QWidget.setTabOrder(self.wedgeZmin, self.wedgeZmax)
        QWidget.setTabOrder(self.wedgeZmax, self.wedgeX2min)
        QWidget.setTabOrder(self.wedgeX2min, self.wedgeX2max)
        QWidget.setTabOrder(self.wedgeX2max, self.wedgeZ2min)
        QWidget.setTabOrder(self.wedgeZ2min, self.wedgeZ2max)
        QWidget.setTabOrder(self.wedgeZ2max, self.helixPitch)
        QWidget.setTabOrder(self.helixPitch, self.helixHeight)
        QWidget.setTabOrder(self.helixHeight, self.helixRadius)
        QWidget.setTabOrder(self.helixRadius, self.helixAngle)
        QWidget.setTabOrder(self.helixAngle, self.helixLocalCS)
        QWidget.setTabOrder(self.helixLocalCS, self.spiralGrowth)
        QWidget.setTabOrder(self.spiralGrowth, self.spiralRotation)
        QWidget.setTabOrder(self.spiralRotation, self.spiralRadius)
        QWidget.setTabOrder(self.spiralRadius, self.circleRadius)
        QWidget.setTabOrder(self.circleRadius, self.circleAngle1)
        QWidget.setTabOrder(self.circleAngle1, self.circleAngle2)
        QWidget.setTabOrder(self.circleAngle2, self.buttonCircleFromThreePoints)
        QWidget.setTabOrder(self.buttonCircleFromThreePoints, self.ellipseMajorRadius)
        QWidget.setTabOrder(self.ellipseMajorRadius, self.ellipseMinorRadius)
        QWidget.setTabOrder(self.ellipseMinorRadius, self.ellipseAngle1)
        QWidget.setTabOrder(self.ellipseAngle1, self.ellipseAngle2)
        QWidget.setTabOrder(self.ellipseAngle2, self.vertexX)
        QWidget.setTabOrder(self.vertexX, self.vertexY)
        QWidget.setTabOrder(self.vertexY, self.vertexZ)
        QWidget.setTabOrder(self.vertexZ, self.edgeX1)
        QWidget.setTabOrder(self.edgeX1, self.edgeY1)
        QWidget.setTabOrder(self.edgeY1, self.edgeZ1)
        QWidget.setTabOrder(self.edgeZ1, self.edgeX2)
        QWidget.setTabOrder(self.edgeX2, self.edgeY2)
        QWidget.setTabOrder(self.edgeY2, self.edgeZ2)
        QWidget.setTabOrder(self.edgeZ2, self.regularPolygonPolygon)
        QWidget.setTabOrder(self.regularPolygonPolygon, self.regularPolygonCircumradius)

        self.retranslateUi(PartGui__DlgPrimitives)
        self.PrimitiveTypeCB.activated.connect(self.widgetStack2.setCurrentIndex)

        self.widgetStack2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PartGui__DlgPrimitives)
    # setupUi

    def retranslateUi(self, PartGui__DlgPrimitives):
        PartGui__DlgPrimitives.setWindowTitle(QCoreApplication.translate("PartGui::DlgPrimitives", u"Geometric Primitives", None))
        self.PrimitiveTypeCB.setItemText(0, QCoreApplication.translate("PartGui::DlgPrimitives", u"Plane", None))
        self.PrimitiveTypeCB.setItemText(1, QCoreApplication.translate("PartGui::DlgPrimitives", u"Box", None))
        self.PrimitiveTypeCB.setItemText(2, QCoreApplication.translate("PartGui::DlgPrimitives", u"Cylinder", None))
        self.PrimitiveTypeCB.setItemText(3, QCoreApplication.translate("PartGui::DlgPrimitives", u"Cone", None))
        self.PrimitiveTypeCB.setItemText(4, QCoreApplication.translate("PartGui::DlgPrimitives", u"Sphere", None))
        self.PrimitiveTypeCB.setItemText(5, QCoreApplication.translate("PartGui::DlgPrimitives", u"Ellipsoid", None))
        self.PrimitiveTypeCB.setItemText(6, QCoreApplication.translate("PartGui::DlgPrimitives", u"Torus", None))
        self.PrimitiveTypeCB.setItemText(7, QCoreApplication.translate("PartGui::DlgPrimitives", u"Prism", None))
        self.PrimitiveTypeCB.setItemText(8, QCoreApplication.translate("PartGui::DlgPrimitives", u"Wedge", None))
        self.PrimitiveTypeCB.setItemText(9, QCoreApplication.translate("PartGui::DlgPrimitives", u"Helix", None))
        self.PrimitiveTypeCB.setItemText(10, QCoreApplication.translate("PartGui::DlgPrimitives", u"Spiral", None))
        self.PrimitiveTypeCB.setItemText(11, QCoreApplication.translate("PartGui::DlgPrimitives", u"Circle", None))
        self.PrimitiveTypeCB.setItemText(12, QCoreApplication.translate("PartGui::DlgPrimitives", u"Ellipse", None))
        self.PrimitiveTypeCB.setItemText(13, QCoreApplication.translate("PartGui::DlgPrimitives", u"Point", None))
        self.PrimitiveTypeCB.setItemText(14, QCoreApplication.translate("PartGui::DlgPrimitives", u"Line", None))
        self.PrimitiveTypeCB.setItemText(15, QCoreApplication.translate("PartGui::DlgPrimitives", u"Regular polygon", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("PartGui::DlgPrimitives", u"Parameter", None))
        self.textLabel2_2.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Length", None))
        self.textLabel3_2.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Width", None))
        self.textLabel2.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Length", None))
        self.textLabel3.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Width", None))
        self.textLabel4.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Height", None))
        self.textLabel5.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Radius", None))
        self.textLabel6.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Height", None))
        self.labelCylinderXSkew.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle in first direction", None))
#if QT_CONFIG(tooltip)
        self.cylinderXSkew.setToolTip(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle in first direction", None))
#endif // QT_CONFIG(tooltip)
        self.labelCylinderYSkew.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle in second direction", None))
#if QT_CONFIG(tooltip)
        self.cylinderYSkew.setToolTip(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle in second direction", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Rotation angle", None))
        self.textLabel9.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Radius 1", None))
        self.textLabel10.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Radius 2", None))
        self.textLabel11.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Height", None))
        self.label_4.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle", None))
        self.textLabel14.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Radius", None))
        self.label_3.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"U parameter", None))
        self.label_2.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"V parameters", None))
        self.textLabel21.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Radius 1", None))
        self.textLabel22.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Radius 2", None))
        self.textLabel23.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Radius 3", None))
        self.label23.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"U parameter", None))
        self.label24.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"V parameter", None))
        self.textLabel19.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Radius 1", None))
        self.textLabel20.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Radius 2", None))
        self.label_5.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"U parameter", None))
        self.label_6.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"V parameter", None))
        self.labelPrismPolygon.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Polygon", None))
        self.labelPrismCircumradius.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Circumradius", None))
        self.labelPrismHeight.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Height", None))
        self.labelPrismXSkew.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle in first direction", None))
#if QT_CONFIG(tooltip)
        self.prismXSkew.setToolTip(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle in first direction", None))
#endif // QT_CONFIG(tooltip)
        self.labelPrismYSkew.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle in second direction", None))
#if QT_CONFIG(tooltip)
        self.prismYSkew.setToolTip(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle in second direction", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"X min/max", None))
        self.label_11.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Y min/max", None))
        self.label_12.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Z min/max", None))
        self.label_13.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"X2 min/max", None))
        self.label_14.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Z2 min/max", None))
        self.label_7.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Pitch", None))
        self.label_8.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Height", None))
        self.label_9.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Radius", None))
        self.label_20.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle", None))
        self.label_15.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Coordinate system", None))
        self.helixLocalCS.setItemText(0, QCoreApplication.translate("PartGui::DlgPrimitives", u"Right-handed", None))
        self.helixLocalCS.setItemText(1, QCoreApplication.translate("PartGui::DlgPrimitives", u"Left-handed", None))

        self.label_spiral_growth.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Growth", None))
        self.label_spiral_rotation.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Number of rotations", None))
        self.label_spiral_radius.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Radius", None))
        self.Radius.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Radius", None))
        self.Angle1.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle 1", None))
        self.Angle2.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle 2", None))
        self.buttonCircleFromThreePoints.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"From 3 Points", None))
        self.labelEllMajorRadius.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Major radius", None))
        self.labelEllMinorRadius.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Minor radius", None))
        self.labelEllAngle1.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle 1", None))
        self.labelEllAngle2.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Angle 2", None))
        self.label_X_Axis.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"X", None))
        self.label_Y_Axis.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Y", None))
        self.label_Z_Axis.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Z", None))
        self.Start_Vertex.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Start point", None))
        self.Finish_Vertex.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"End point", None))
        self.X1.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"X", None))
        self.Y1.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Y", None))
        self.Z1.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Z", None))
        self.labelRegularPolygonPolygon.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Polygon", None))
        self.labelRegularPolygonCircumradius.setText(QCoreApplication.translate("PartGui::DlgPrimitives", u"Circumradius", None))
    # retranslateUi

