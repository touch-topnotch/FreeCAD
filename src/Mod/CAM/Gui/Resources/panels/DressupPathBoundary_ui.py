# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DressupPathBoundary.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(417, 647)
        Form.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stockGroup = QGroupBox(Form)
        self.stockGroup.setObjectName(u"stockGroup")
        self.verticalLayout_5 = QVBoxLayout(self.stockGroup)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_2 = QWidget(self.stockGroup)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stock = QComboBox(self.widget_2)
        self.stock.addItem("")
        self.stock.addItem("")
        self.stock.addItem("")
        self.stock.addItem("")
        self.stock.setObjectName(u"stock")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stock.sizePolicy().hasHeightForWidth())
        self.stock.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.stock)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.horizontalSpacer = QSpacerItem(40, 6, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer)

        self.stockFromExisting = QFrame(self.stockGroup)
        self.stockFromExisting.setObjectName(u"stockFromExisting")
        self.gridLayout_8 = QGridLayout(self.stockFromExisting)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.stockExisting = QComboBox(self.stockFromExisting)
        self.stockExisting.setObjectName(u"stockExisting")

        self.gridLayout_8.addWidget(self.stockExisting, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.stockFromExisting)

        self.stockFromBase = QFrame(self.stockGroup)
        self.stockFromBase.setObjectName(u"stockFromBase")
        self.gridLayout_9 = QGridLayout(self.stockFromBase)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.stockExtXLabel = QLabel(self.stockFromBase)
        self.stockExtXLabel.setObjectName(u"stockExtXLabel")

        self.gridLayout_9.addWidget(self.stockExtXLabel, 0, 1, 1, 1)

        self.stockExtXneg = Gui_InputField(self.stockFromBase)
        self.stockExtXneg.setObjectName(u"stockExtXneg")

        self.gridLayout_9.addWidget(self.stockExtXneg, 0, 2, 1, 1)

        self.stockExtXpos = Gui_InputField(self.stockFromBase)
        self.stockExtXpos.setObjectName(u"stockExtXpos")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stockExtXpos.sizePolicy().hasHeightForWidth())
        self.stockExtXpos.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.stockExtXpos, 0, 3, 1, 1)

        self.stockExtYLabel = QLabel(self.stockFromBase)
        self.stockExtYLabel.setObjectName(u"stockExtYLabel")

        self.gridLayout_9.addWidget(self.stockExtYLabel, 1, 1, 1, 1)

        self.stockExtYneg = Gui_InputField(self.stockFromBase)
        self.stockExtYneg.setObjectName(u"stockExtYneg")

        self.gridLayout_9.addWidget(self.stockExtYneg, 1, 2, 1, 1)

        self.stockExtYpos = Gui_InputField(self.stockFromBase)
        self.stockExtYpos.setObjectName(u"stockExtYpos")

        self.gridLayout_9.addWidget(self.stockExtYpos, 1, 3, 1, 1)

        self.stockExtZLabel = QLabel(self.stockFromBase)
        self.stockExtZLabel.setObjectName(u"stockExtZLabel")

        self.gridLayout_9.addWidget(self.stockExtZLabel, 2, 1, 1, 1)

        self.stockExtZneg = Gui_InputField(self.stockFromBase)
        self.stockExtZneg.setObjectName(u"stockExtZneg")

        self.gridLayout_9.addWidget(self.stockExtZneg, 2, 2, 1, 1)

        self.stockExtZpos = Gui_InputField(self.stockFromBase)
        self.stockExtZpos.setObjectName(u"stockExtZpos")

        self.gridLayout_9.addWidget(self.stockExtZpos, 2, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.stockFromBase)

        self.stockCreateCylinder = QFrame(self.stockGroup)
        self.stockCreateCylinder.setObjectName(u"stockCreateCylinder")
        self.gridLayout_10 = QGridLayout(self.stockCreateCylinder)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.stockCylinderRadiusLabel = QLabel(self.stockCreateCylinder)
        self.stockCylinderRadiusLabel.setObjectName(u"stockCylinderRadiusLabel")

        self.gridLayout_10.addWidget(self.stockCylinderRadiusLabel, 0, 1, 1, 1)

        self.stockCylinderRadius = Gui_InputField(self.stockCreateCylinder)
        self.stockCylinderRadius.setObjectName(u"stockCylinderRadius")

        self.gridLayout_10.addWidget(self.stockCylinderRadius, 0, 2, 1, 1)

        self.stockCylinderHeightLabel = QLabel(self.stockCreateCylinder)
        self.stockCylinderHeightLabel.setObjectName(u"stockCylinderHeightLabel")

        self.gridLayout_10.addWidget(self.stockCylinderHeightLabel, 1, 1, 1, 1)

        self.stockCylinderHeight = Gui_InputField(self.stockCreateCylinder)
        self.stockCylinderHeight.setObjectName(u"stockCylinderHeight")

        self.gridLayout_10.addWidget(self.stockCylinderHeight, 1, 2, 1, 1)


        self.verticalLayout_5.addWidget(self.stockCreateCylinder)

        self.stockCreateBox = QFrame(self.stockGroup)
        self.stockCreateBox.setObjectName(u"stockCreateBox")
        self.gridLayout_11 = QGridLayout(self.stockCreateBox)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.stockBoxLengthLabel = QLabel(self.stockCreateBox)
        self.stockBoxLengthLabel.setObjectName(u"stockBoxLengthLabel")

        self.gridLayout_11.addWidget(self.stockBoxLengthLabel, 0, 1, 1, 1)

        self.stockBoxLength = Gui_InputField(self.stockCreateBox)
        self.stockBoxLength.setObjectName(u"stockBoxLength")

        self.gridLayout_11.addWidget(self.stockBoxLength, 0, 2, 1, 1)

        self.stockBoxWidthLabel = QLabel(self.stockCreateBox)
        self.stockBoxWidthLabel.setObjectName(u"stockBoxWidthLabel")

        self.gridLayout_11.addWidget(self.stockBoxWidthLabel, 1, 1, 1, 1)

        self.stockBoxWidth = Gui_InputField(self.stockCreateBox)
        self.stockBoxWidth.setObjectName(u"stockBoxWidth")

        self.gridLayout_11.addWidget(self.stockBoxWidth, 1, 2, 1, 1)

        self.stockBoxHeightLabel = QLabel(self.stockCreateBox)
        self.stockBoxHeightLabel.setObjectName(u"stockBoxHeightLabel")

        self.gridLayout_11.addWidget(self.stockBoxHeightLabel, 2, 1, 1, 1)

        self.stockBoxHeight = Gui_InputField(self.stockCreateBox)
        self.stockBoxHeight.setObjectName(u"stockBoxHeight")

        self.gridLayout_11.addWidget(self.stockBoxHeight, 2, 2, 1, 1)


        self.verticalLayout_5.addWidget(self.stockCreateBox)


        self.verticalLayout.addWidget(self.stockGroup)

        self.stockInside = QCheckBox(Form)
        self.stockInside.setObjectName(u"stockInside")
        self.stockInside.setChecked(True)

        self.verticalLayout.addWidget(self.stockInside)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        QWidget.setTabOrder(self.stock, self.stockExisting)
        QWidget.setTabOrder(self.stockExisting, self.stockExtXneg)
        QWidget.setTabOrder(self.stockExtXneg, self.stockExtXpos)
        QWidget.setTabOrder(self.stockExtXpos, self.stockExtYneg)
        QWidget.setTabOrder(self.stockExtYneg, self.stockExtYpos)
        QWidget.setTabOrder(self.stockExtYpos, self.stockExtZneg)
        QWidget.setTabOrder(self.stockExtZneg, self.stockExtZpos)
        QWidget.setTabOrder(self.stockExtZpos, self.stockCylinderRadius)
        QWidget.setTabOrder(self.stockCylinderRadius, self.stockCylinderHeight)
        QWidget.setTabOrder(self.stockCylinderHeight, self.stockBoxLength)
        QWidget.setTabOrder(self.stockBoxLength, self.stockBoxWidth)
        QWidget.setTabOrder(self.stockBoxWidth, self.stockBoxHeight)
        QWidget.setTabOrder(self.stockBoxHeight, self.stockInside)

        self.retranslateUi(Form)

        self.stock.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.stockGroup.setTitle(QCoreApplication.translate("Form", u"Boundary Body", None))
        self.stock.setItemText(0, QCoreApplication.translate("Form", u"Create box", None))
        self.stock.setItemText(1, QCoreApplication.translate("Form", u"Create cylinder", None))
        self.stock.setItemText(2, QCoreApplication.translate("Form", u"Extend model's bounding box", None))
        self.stock.setItemText(3, QCoreApplication.translate("Form", u"Use existing solid", None))

#if QT_CONFIG(tooltip)
        self.stock.setToolTip(QCoreApplication.translate("Form", u"Select what type of shape to use to constrain the underlying Path.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.stockExisting.setToolTip(QCoreApplication.translate("Form", u"Select the body to be used to constrain the underlying path", None))
#endif // QT_CONFIG(tooltip)
        self.stockExtXLabel.setText(QCoreApplication.translate("Form", u"Ext. X", None))
#if QT_CONFIG(tooltip)
        self.stockExtXneg.setToolTip(QCoreApplication.translate("Form", u"Extension of bounding box's MinX", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.stockExtXpos.setToolTip(QCoreApplication.translate("Form", u"Extension of bounding box's MaxX", None))
#endif // QT_CONFIG(tooltip)
        self.stockExtYLabel.setText(QCoreApplication.translate("Form", u"Ext. Y", None))
#if QT_CONFIG(tooltip)
        self.stockExtYneg.setToolTip(QCoreApplication.translate("Form", u"Extension of bounding box's MinY", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.stockExtYpos.setToolTip(QCoreApplication.translate("Form", u"Extension of bounding box's MaxY", None))
#endif // QT_CONFIG(tooltip)
        self.stockExtZLabel.setText(QCoreApplication.translate("Form", u"Ext. Z", None))
#if QT_CONFIG(tooltip)
        self.stockExtZneg.setToolTip(QCoreApplication.translate("Form", u"Extension of bounding box's MinZ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.stockExtZpos.setToolTip(QCoreApplication.translate("Form", u"Extension of bounding box's MaxZ", None))
#endif // QT_CONFIG(tooltip)
        self.stockCylinderRadiusLabel.setText(QCoreApplication.translate("Form", u"Radius", None))
#if QT_CONFIG(tooltip)
        self.stockCylinderRadius.setToolTip(QCoreApplication.translate("Form", u"Radius of the cylinder", None))
#endif // QT_CONFIG(tooltip)
        self.stockCylinderHeightLabel.setText(QCoreApplication.translate("Form", u"Height", None))
#if QT_CONFIG(tooltip)
        self.stockCylinderHeight.setToolTip(QCoreApplication.translate("Form", u"Height of the cylinder", None))
#endif // QT_CONFIG(tooltip)
        self.stockBoxLengthLabel.setText(QCoreApplication.translate("Form", u"Length", None))
#if QT_CONFIG(tooltip)
        self.stockBoxLength.setToolTip(QCoreApplication.translate("Form", u"Length of the box", None))
#endif // QT_CONFIG(tooltip)
        self.stockBoxWidthLabel.setText(QCoreApplication.translate("Form", u"Width", None))
#if QT_CONFIG(tooltip)
        self.stockBoxWidth.setToolTip(QCoreApplication.translate("Form", u"Width of the box", None))
#endif // QT_CONFIG(tooltip)
        self.stockBoxHeightLabel.setText(QCoreApplication.translate("Form", u"Height", None))
#if QT_CONFIG(tooltip)
        self.stockBoxHeight.setToolTip(QCoreApplication.translate("Form", u"Height of the box", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.stockInside.setToolTip(QCoreApplication.translate("Form", u"If checked, the path is constrained by the solid. Otherwise the volume of the solid describes a 'keep out' zone", None))
#endif // QT_CONFIG(tooltip)
        self.stockInside.setText(QCoreApplication.translate("Form", u"Constrained to inside", None))
        pass
    # retranslateUi

