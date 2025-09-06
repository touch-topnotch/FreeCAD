# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Placement.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QWidget)

class Ui_Gui_Dialog_Placement(object):
    def setupUi(self, Gui__Dialog__Placement):
        if not Gui__Dialog__Placement.objectName():
            Gui__Dialog__Placement.setObjectName(u"Gui__Dialog__Placement")
        Gui__Dialog__Placement.resize(456, 492)
        self.gridLayout = QGridLayout(Gui__Dialog__Placement)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.GroupBox5 = QGroupBox(Gui__Dialog__Placement)
        self.GroupBox5.setObjectName(u"GroupBox5")
        self.gridLayout1 = QGridLayout(self.GroupBox5)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
        self.TextLabelX = QLabel(self.GroupBox5)
        self.TextLabelX.setObjectName(u"TextLabelX")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextLabelX.sizePolicy().hasHeightForWidth())
        self.TextLabelX.setSizePolicy(sizePolicy)
        self.TextLabelX.setText(u"X")

        self.gridLayout1.addWidget(self.TextLabelX, 0, 0, 1, 1)

        self.xPos = Gui_QuantitySpinBox(self.GroupBox5)
        self.xPos.setObjectName(u"xPos")

        self.gridLayout1.addWidget(self.xPos, 0, 1, 1, 1)

        self.TextLabelY = QLabel(self.GroupBox5)
        self.TextLabelY.setObjectName(u"TextLabelY")
        sizePolicy.setHeightForWidth(self.TextLabelY.sizePolicy().hasHeightForWidth())
        self.TextLabelY.setSizePolicy(sizePolicy)
        self.TextLabelY.setText(u"Y")

        self.gridLayout1.addWidget(self.TextLabelY, 2, 0, 1, 1)

        self.yPos = Gui_QuantitySpinBox(self.GroupBox5)
        self.yPos.setObjectName(u"yPos")

        self.gridLayout1.addWidget(self.yPos, 2, 1, 1, 1)

        self.TextLabelZ = QLabel(self.GroupBox5)
        self.TextLabelZ.setObjectName(u"TextLabelZ")
        sizePolicy.setHeightForWidth(self.TextLabelZ.sizePolicy().hasHeightForWidth())
        self.TextLabelZ.setSizePolicy(sizePolicy)
        self.TextLabelZ.setText(u"Z")

        self.gridLayout1.addWidget(self.TextLabelZ, 3, 0, 1, 1)

        self.zPos = Gui_QuantitySpinBox(self.GroupBox5)
        self.zPos.setObjectName(u"zPos")

        self.gridLayout1.addWidget(self.zPos, 3, 1, 1, 1)

        self.TextLabelAxial = QLabel(self.GroupBox5)
        self.TextLabelAxial.setObjectName(u"TextLabelAxial")
        sizePolicy.setHeightForWidth(self.TextLabelAxial.sizePolicy().hasHeightForWidth())
        self.TextLabelAxial.setSizePolicy(sizePolicy)

        self.gridLayout1.addWidget(self.TextLabelAxial, 4, 0, 1, 1)

        self.axialPos = Gui_QuantitySpinBox(self.GroupBox5)
        self.axialPos.setObjectName(u"axialPos")

        self.gridLayout1.addWidget(self.axialPos, 4, 1, 1, 1)

        self.applyAxial = QPushButton(self.GroupBox5)
        self.applyAxial.setObjectName(u"applyAxial")

        self.gridLayout1.addWidget(self.applyAxial, 5, 1, 1, 1)


        self.gridLayout.addWidget(self.GroupBox5, 0, 0, 1, 1)

        self.GroupBox5_3 = QGroupBox(Gui__Dialog__Placement)
        self.GroupBox5_3.setObjectName(u"GroupBox5_3")
        self.gridLayout2 = QGridLayout(self.GroupBox5_3)
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayout2.setContentsMargins(9, 9, 9, 9)
        self.TextLabelX_2 = QLabel(self.GroupBox5_3)
        self.TextLabelX_2.setObjectName(u"TextLabelX_2")
        sizePolicy.setHeightForWidth(self.TextLabelX_2.sizePolicy().hasHeightForWidth())
        self.TextLabelX_2.setSizePolicy(sizePolicy)
        self.TextLabelX_2.setText(u"X")

        self.gridLayout2.addWidget(self.TextLabelX_2, 0, 0, 1, 1)

        self.xCnt = Gui_QuantitySpinBox(self.GroupBox5_3)
        self.xCnt.setObjectName(u"xCnt")

        self.gridLayout2.addWidget(self.xCnt, 0, 1, 1, 1)

        self.TextLabelY_2 = QLabel(self.GroupBox5_3)
        self.TextLabelY_2.setObjectName(u"TextLabelY_2")
        sizePolicy.setHeightForWidth(self.TextLabelY_2.sizePolicy().hasHeightForWidth())
        self.TextLabelY_2.setSizePolicy(sizePolicy)
        self.TextLabelY_2.setText(u"Y")

        self.gridLayout2.addWidget(self.TextLabelY_2, 1, 0, 1, 1)

        self.yCnt = Gui_QuantitySpinBox(self.GroupBox5_3)
        self.yCnt.setObjectName(u"yCnt")

        self.gridLayout2.addWidget(self.yCnt, 1, 1, 1, 1)

        self.TextLabelZ_5 = QLabel(self.GroupBox5_3)
        self.TextLabelZ_5.setObjectName(u"TextLabelZ_5")
        sizePolicy.setHeightForWidth(self.TextLabelZ_5.sizePolicy().hasHeightForWidth())
        self.TextLabelZ_5.setSizePolicy(sizePolicy)
        self.TextLabelZ_5.setText(u"Z")

        self.gridLayout2.addWidget(self.TextLabelZ_5, 2, 0, 1, 1)

        self.zCnt = Gui_QuantitySpinBox(self.GroupBox5_3)
        self.zCnt.setObjectName(u"zCnt")

        self.gridLayout2.addWidget(self.zCnt, 2, 1, 1, 1)

        self.centerOfMass = QCheckBox(self.GroupBox5_3)
        self.centerOfMass.setObjectName(u"centerOfMass")

        self.gridLayout2.addWidget(self.centerOfMass, 3, 0, 1, 2)

        self.selectedVertex = QPushButton(self.GroupBox5_3)
        self.selectedVertex.setObjectName(u"selectedVertex")

        self.gridLayout2.addWidget(self.selectedVertex, 4, 0, 1, 2)


        self.gridLayout.addWidget(self.GroupBox5_3, 0, 1, 1, 1)

        self.GroupBox5_2 = QGroupBox(Gui__Dialog__Placement)
        self.GroupBox5_2.setObjectName(u"GroupBox5_2")
        self.gridLayout3 = QGridLayout(self.GroupBox5_2)
        self.gridLayout3.setSpacing(6)
        self.gridLayout3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.gridLayout3.setContentsMargins(9, 9, 9, 9)
        self.rotationInput = QComboBox(self.GroupBox5_2)
        self.rotationInput.addItem("")
        self.rotationInput.addItem("")
        self.rotationInput.setObjectName(u"rotationInput")

        self.gridLayout3.addWidget(self.rotationInput, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.GroupBox5_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout4 = QGridLayout(self.page)
        self.gridLayout4.setSpacing(6)
        self.gridLayout4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.gridLayout4.setContentsMargins(9, 0, 9, 0)
        self.gridLayout5 = QGridLayout()
        self.gridLayout5.setSpacing(6)
        self.gridLayout5.setObjectName(u"gridLayout5")
        self.gridLayout5.setContentsMargins(0, 0, 0, 0)
        self.TextLabelAxis = QLabel(self.page)
        self.TextLabelAxis.setObjectName(u"TextLabelAxis")
        sizePolicy.setHeightForWidth(self.TextLabelAxis.sizePolicy().hasHeightForWidth())
        self.TextLabelAxis.setSizePolicy(sizePolicy)

        self.gridLayout5.addWidget(self.TextLabelAxis, 0, 0, 1, 1)

        self.xAxis = Gui_QuantitySpinBox(self.page)
        self.xAxis.setObjectName(u"xAxis")

        self.gridLayout5.addWidget(self.xAxis, 0, 1, 1, 1)

        self.yAxis = Gui_QuantitySpinBox(self.page)
        self.yAxis.setObjectName(u"yAxis")

        self.gridLayout5.addWidget(self.yAxis, 1, 1, 1, 1)

        self.zAxis = Gui_QuantitySpinBox(self.page)
        self.zAxis.setObjectName(u"zAxis")

        self.gridLayout5.addWidget(self.zAxis, 2, 1, 1, 1)

        self.textLabelAngle = QLabel(self.page)
        self.textLabelAngle.setObjectName(u"textLabelAngle")
        sizePolicy.setHeightForWidth(self.textLabelAngle.sizePolicy().hasHeightForWidth())
        self.textLabelAngle.setSizePolicy(sizePolicy)

        self.gridLayout5.addWidget(self.textLabelAngle, 3, 0, 1, 1)

        self.angle = Gui_QuantitySpinBox(self.page)
        self.angle.setObjectName(u"angle")

        self.gridLayout5.addWidget(self.angle, 3, 1, 1, 1)


        self.gridLayout4.addLayout(self.gridLayout5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout6 = QGridLayout(self.page_3)
        self.gridLayout6.setSpacing(6)
        self.gridLayout6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout6.setObjectName(u"gridLayout6")
        self.gridLayout6.setContentsMargins(9, 0, 9, 0)
        self.gridLayout7 = QGridLayout()
        self.gridLayout7.setSpacing(6)
        self.gridLayout7.setObjectName(u"gridLayout7")
        self.gridLayout7.setContentsMargins(0, 0, 0, 0)
        self.TextLabelZ_2 = QLabel(self.page_3)
        self.TextLabelZ_2.setObjectName(u"TextLabelZ_2")
        sizePolicy.setHeightForWidth(self.TextLabelZ_2.sizePolicy().hasHeightForWidth())
        self.TextLabelZ_2.setSizePolicy(sizePolicy)

        self.gridLayout7.addWidget(self.TextLabelZ_2, 0, 0, 1, 1)

        self.yawAngle = Gui_QuantitySpinBox(self.page_3)
        self.yawAngle.setObjectName(u"yawAngle")

        self.gridLayout7.addWidget(self.yawAngle, 0, 1, 1, 1)

        self.TextLabelZ_3 = QLabel(self.page_3)
        self.TextLabelZ_3.setObjectName(u"TextLabelZ_3")
        sizePolicy.setHeightForWidth(self.TextLabelZ_3.sizePolicy().hasHeightForWidth())
        self.TextLabelZ_3.setSizePolicy(sizePolicy)

        self.gridLayout7.addWidget(self.TextLabelZ_3, 1, 0, 1, 1)

        self.pitchAngle = Gui_QuantitySpinBox(self.page_3)
        self.pitchAngle.setObjectName(u"pitchAngle")

        self.gridLayout7.addWidget(self.pitchAngle, 1, 1, 1, 1)

        self.TextLabelZ_4 = QLabel(self.page_3)
        self.TextLabelZ_4.setObjectName(u"TextLabelZ_4")
        sizePolicy.setHeightForWidth(self.TextLabelZ_4.sizePolicy().hasHeightForWidth())
        self.TextLabelZ_4.setSizePolicy(sizePolicy)

        self.gridLayout7.addWidget(self.TextLabelZ_4, 2, 0, 1, 1)

        self.rollAngle = Gui_QuantitySpinBox(self.page_3)
        self.rollAngle.setObjectName(u"rollAngle")

        self.gridLayout7.addWidget(self.rollAngle, 2, 1, 1, 1)


        self.gridLayout6.addLayout(self.gridLayout7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout3.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.GroupBox5_2, 1, 0, 1, 2)

        self.vSpacer = QSpacerItem(20, 41, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.vSpacer, 2, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.applyIncrementalPlacement = QCheckBox(Gui__Dialog__Placement)
        self.applyIncrementalPlacement.setObjectName(u"applyIncrementalPlacement")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.applyIncrementalPlacement.sizePolicy().hasHeightForWidth())
        self.applyIncrementalPlacement.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.applyIncrementalPlacement)

        self.hSpacer = QSpacerItem(78, 22, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hSpacer)

        self.resetButton = QPushButton(Gui__Dialog__Placement)
        self.resetButton.setObjectName(u"resetButton")

        self.horizontalLayout.addWidget(self.resetButton)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)

        self.buttonBoxLayout = QHBoxLayout()
        self.buttonBoxLayout.setSpacing(6)
        self.buttonBoxLayout.setObjectName(u"buttonBoxLayout")
        self.buttonBoxSpacer = QSpacerItem(88, 24, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonBoxLayout.addItem(self.buttonBoxSpacer)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__Placement)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.buttonBoxLayout.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.buttonBoxLayout, 4, 0, 1, 2)


        self.retranslateUi(Gui__Dialog__Placement)
        self.rotationInput.activated.connect(self.stackedWidget.setCurrentIndex)
        self.buttonBox.accepted.connect(Gui__Dialog__Placement.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__Placement.reject)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Gui__Dialog__Placement)
    # setupUi

    def retranslateUi(self, Gui__Dialog__Placement):
        Gui__Dialog__Placement.setWindowTitle(QCoreApplication.translate("Gui::Dialog::Placement", u"Placement", None))
        self.GroupBox5.setTitle(QCoreApplication.translate("Gui::Dialog::Placement", u"Translation", None))
        self.TextLabelAxial.setText(QCoreApplication.translate("Gui::Dialog::Placement", u"Axial", None))
#if QT_CONFIG(tooltip)
        self.applyAxial.setToolTip(QCoreApplication.translate("Gui::Dialog::Placement", u"Shift-click for opposite direction", None))
#endif // QT_CONFIG(tooltip)
        self.applyAxial.setText(QCoreApplication.translate("Gui::Dialog::Placement", u"Apply Axial", None))
        self.GroupBox5_3.setTitle(QCoreApplication.translate("Gui::Dialog::Placement", u"Center", None))
        self.centerOfMass.setText(QCoreApplication.translate("Gui::Dialog::Placement", u"Use center of mass", None))
        self.selectedVertex.setText(QCoreApplication.translate("Gui::Dialog::Placement", u"Selected Points", None))
        self.GroupBox5_2.setTitle(QCoreApplication.translate("Gui::Dialog::Placement", u"Rotation", None))
        self.rotationInput.setItemText(0, QCoreApplication.translate("Gui::Dialog::Placement", u"Rotation axis and angle", None))
        self.rotationInput.setItemText(1, QCoreApplication.translate("Gui::Dialog::Placement", u"Euler angles (Z\u2013Y\u2032\u2013X\u2033)", None))

        self.TextLabelAxis.setText(QCoreApplication.translate("Gui::Dialog::Placement", u"Axis", None))
        self.textLabelAngle.setText(QCoreApplication.translate("Gui::Dialog::Placement", u"Angle", None))
        self.TextLabelZ_2.setText(QCoreApplication.translate("Gui::Dialog::Placement", u"Yaw (around Z-axis)", None))
#if QT_CONFIG(tooltip)
        self.yawAngle.setToolTip(QCoreApplication.translate("Gui::Dialog::Placement", u"Yaw (around Z-axis)", None))
#endif // QT_CONFIG(tooltip)
        self.TextLabelZ_3.setText(QCoreApplication.translate("Gui::Dialog::Placement", u"Pitch (around Y-axis)", None))
#if QT_CONFIG(tooltip)
        self.pitchAngle.setToolTip(QCoreApplication.translate("Gui::Dialog::Placement", u"Pitch (around Y-axis)", None))
#endif // QT_CONFIG(tooltip)
        self.TextLabelZ_4.setText(QCoreApplication.translate("Gui::Dialog::Placement", u"Roll (around X-axis)", None))
#if QT_CONFIG(tooltip)
        self.rollAngle.setToolTip(QCoreApplication.translate("Gui::Dialog::Placement", u"Roll (around the X-axis)", None))
#endif // QT_CONFIG(tooltip)
        self.applyIncrementalPlacement.setText(QCoreApplication.translate("Gui::Dialog::Placement", u"Apply incremental changes", None))
        self.resetButton.setText(QCoreApplication.translate("Gui::Dialog::Placement", u"Reset", None))
    # retranslateUi

