# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskSelectPlane.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(210, 568)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.buttonTop = QPushButton(Form)
        self.buttonTop.setObjectName(u"buttonTop")

        self.verticalLayout.addWidget(self.buttonTop)

        self.buttonFront = QPushButton(Form)
        self.buttonFront.setObjectName(u"buttonFront")

        self.verticalLayout.addWidget(self.buttonFront)

        self.buttonSide = QPushButton(Form)
        self.buttonSide.setObjectName(u"buttonSide")

        self.verticalLayout.addWidget(self.buttonSide)

        self.buttonAlign = QPushButton(Form)
        self.buttonAlign.setObjectName(u"buttonAlign")

        self.verticalLayout.addWidget(self.buttonAlign)

        self.buttonAuto = QPushButton(Form)
        self.buttonAuto.setObjectName(u"buttonAuto")

        self.verticalLayout.addWidget(self.buttonAuto)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.fieldOffset = Gui_InputField(Form)
        self.fieldOffset.setObjectName(u"fieldOffset")
        self.fieldOffset.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.fieldOffset, 0, 1, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.checkCenter = QCheckBox(Form)
        self.checkCenter.setObjectName(u"checkCenter")
        self.checkCenter.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.checkCenter, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_7)

        self.buttonMove = QPushButton(Form)
        self.buttonMove.setObjectName(u"buttonMove")

        self.verticalLayout.addWidget(self.buttonMove)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.buttonColor = Gui_ColorButton(Form)
        self.buttonColor.setObjectName(u"buttonColor")

        self.gridLayout.addWidget(self.buttonColor, 0, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.fieldGridSpacing = Gui_InputField(Form)
        self.fieldGridSpacing.setObjectName(u"fieldGridSpacing")
        self.fieldGridSpacing.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.fieldGridSpacing, 1, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.fieldGridMainLine = QSpinBox(Form)
        self.fieldGridMainLine.setObjectName(u"fieldGridMainLine")

        self.gridLayout.addWidget(self.fieldGridMainLine, 2, 1, 1, 1)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.fieldGridExtension = QSpinBox(Form)
        self.fieldGridExtension.setObjectName(u"fieldGridExtension")
        self.fieldGridExtension.setMinimum(1)
        self.fieldGridExtension.setMaximum(9999)

        self.gridLayout.addWidget(self.fieldGridExtension, 3, 1, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.fieldSnapRadius = QSpinBox(Form)
        self.fieldSnapRadius.setObjectName(u"fieldSnapRadius")

        self.gridLayout.addWidget(self.fieldSnapRadius, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonCenter = QPushButton(Form)
        self.buttonCenter.setObjectName(u"buttonCenter")

        self.verticalLayout.addWidget(self.buttonCenter)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.buttonPrevious = QPushButton(Form)
        self.buttonPrevious.setObjectName(u"buttonPrevious")

        self.gridLayout_3.addWidget(self.buttonPrevious, 0, 0, 1, 1)

        self.buttonNext = QPushButton(Form)
        self.buttonNext.setObjectName(u"buttonNext")
        self.buttonNext.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_3.addWidget(self.buttonNext, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Working Plane Setup", None))
        self.label.setText(QCoreApplication.translate("Form", u"Choose an option below. Or define a working plane by selecting 3 vertices, 1 or more shapes, or a working plane proxy, and then confirm with a click in the 3D view.", None))
#if QT_CONFIG(tooltip)
        self.buttonTop.setToolTip(QCoreApplication.translate("Form", u"Sets the working plane to the XY-plane (ground plane)", None))
#endif // QT_CONFIG(tooltip)
        self.buttonTop.setText(QCoreApplication.translate("Form", u"Top (XY)", None))
#if QT_CONFIG(tooltip)
        self.buttonFront.setToolTip(QCoreApplication.translate("Form", u"Sets the working plane to the XZ-plane (front plane)", None))
#endif // QT_CONFIG(tooltip)
        self.buttonFront.setText(QCoreApplication.translate("Form", u"Front (XZ)", None))
#if QT_CONFIG(tooltip)
        self.buttonSide.setToolTip(QCoreApplication.translate("Form", u"Sets the working plane to the YZ-plane (side plane)", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSide.setText(QCoreApplication.translate("Form", u"Side (YZ)", None))
#if QT_CONFIG(tooltip)
        self.buttonAlign.setToolTip(QCoreApplication.translate("Form", u"Sets the working plane facing the current view", None))
#endif // QT_CONFIG(tooltip)
        self.buttonAlign.setText(QCoreApplication.translate("Form", u"Align to View", None))
#if QT_CONFIG(tooltip)
        self.buttonAuto.setToolTip(QCoreApplication.translate("Form", u"The working plane will align to the current\n"
"view each time a command is started", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.buttonAuto.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.buttonAuto.setText(QCoreApplication.translate("Form", u"Automatic", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Offset", None))
#if QT_CONFIG(tooltip)
        self.fieldOffset.setToolTip(QCoreApplication.translate("Form", u"An optional offset to give to the working plane\n"
"above its base position. Use this together with one\n"
"of the buttons above", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Form", u"If this is selected, the working plane will be\n"
"centered on the current view when pressing one\n"
"of the buttons above", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"Center plane on view", None))
#if QT_CONFIG(tooltip)
        self.checkCenter.setToolTip(QCoreApplication.translate("Form", u"Centers the working plane on the current view when pressing one\n"
"of the buttons above", None))
#endif // QT_CONFIG(tooltip)
        self.checkCenter.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Or select a single vertex to move the current working plane without changing its orientation. Then press the button below.", None))
#if QT_CONFIG(tooltip)
        self.buttonMove.setToolTip(QCoreApplication.translate("Form", u"Moves the working plane without changing its\n"
"orientation. If no point is selected, the plane\n"
"will be moved to the center of the view.", None))
#endif // QT_CONFIG(tooltip)
        self.buttonMove.setText(QCoreApplication.translate("Form", u"Move Working Plane", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("Form", u"The color of the grid", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("Form", u"Grid color", None))
#if QT_CONFIG(tooltip)
        self.buttonColor.setToolTip(QCoreApplication.translate("Form", u"The color of the grid", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Form", u"The distance between grid lines", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Grid spacing", None))
#if QT_CONFIG(tooltip)
        self.fieldGridSpacing.setToolTip(QCoreApplication.translate("Form", u"The distance between grid lines", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Form", u"The number of squares between major grid lines", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"Major lines every", None))
#if QT_CONFIG(tooltip)
        self.fieldGridMainLine.setToolTip(QCoreApplication.translate("Form", u"The number of squares between major grid lines", None))
#endif // QT_CONFIG(tooltip)
        self.fieldGridMainLine.setSuffix(QCoreApplication.translate("Form", u" squares", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("Form", u"The number of squares in the X- and Y-direction of the grid", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Form", u"Grid size", None))
#if QT_CONFIG(tooltip)
        self.fieldGridExtension.setToolTip(QCoreApplication.translate("Form", u"The number of squares in the X- and Y-direction of the grid", None))
#endif // QT_CONFIG(tooltip)
        self.fieldGridExtension.setSuffix(QCoreApplication.translate("Form", u" squares", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("Form", u"The distance at which a point can be snapped to", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Form", u"Snapping radius", None))
#if QT_CONFIG(tooltip)
        self.fieldSnapRadius.setToolTip(QCoreApplication.translate("Form", u"The distance at which a point can be snapped to", None))
#endif // QT_CONFIG(tooltip)
        self.fieldSnapRadius.setSuffix(QCoreApplication.translate("Form", u" px", None))
#if QT_CONFIG(tooltip)
        self.buttonCenter.setToolTip(QCoreApplication.translate("Form", u"Centers the view on the current working plane", None))
#endif // QT_CONFIG(tooltip)
        self.buttonCenter.setText(QCoreApplication.translate("Form", u"Center View", None))
#if QT_CONFIG(tooltip)
        self.buttonPrevious.setToolTip(QCoreApplication.translate("Form", u"Resets the working plane to its previous position", None))
#endif // QT_CONFIG(tooltip)
        self.buttonPrevious.setText(QCoreApplication.translate("Form", u"Previous", None))
#if QT_CONFIG(tooltip)
        self.buttonNext.setToolTip(QCoreApplication.translate("Form", u"Resets the working plane to its next position", None))
#endif // QT_CONFIG(tooltip)
        self.buttonNext.setText(QCoreApplication.translate("Form", u"Next", None))
    # retranslateUi

