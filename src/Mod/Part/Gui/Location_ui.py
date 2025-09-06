# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Location.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_PartGui_Location(object):
    def setupUi(self, PartGui__Location):
        if not PartGui__Location.objectName():
            PartGui__Location.setObjectName(u"PartGui__Location")
        PartGui__Location.resize(280, 307)
        PartGui__Location.setProperty(u"sizeGripEnabled", True)
        self.verticalLayout = QVBoxLayout(PartGui__Location)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PositionGB = QGroupBox(PartGui__Location)
        self.PositionGB.setObjectName(u"PositionGB")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PositionGB.sizePolicy().hasHeightForWidth())
        self.PositionGB.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.PositionGB)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelLength2_2 = QLabel(self.PositionGB)
        self.labelLength2_2.setObjectName(u"labelLength2_2")

        self.gridLayout.addWidget(self.labelLength2_2, 0, 0, 1, 1)

        self.XPositionQSB = Gui_QuantitySpinBox(self.PositionGB)
        self.XPositionQSB.setObjectName(u"XPositionQSB")
        self.XPositionQSB.setKeyboardTracking(False)
        self.XPositionQSB.setProperty(u"unit", u"")

        self.gridLayout.addWidget(self.XPositionQSB, 0, 1, 1, 1)

        self.labelLength2_3 = QLabel(self.PositionGB)
        self.labelLength2_3.setObjectName(u"labelLength2_3")

        self.gridLayout.addWidget(self.labelLength2_3, 1, 0, 1, 1)

        self.YPositionQSB = Gui_QuantitySpinBox(self.PositionGB)
        self.YPositionQSB.setObjectName(u"YPositionQSB")
        self.YPositionQSB.setKeyboardTracking(False)
        self.YPositionQSB.setProperty(u"unit", u"")

        self.gridLayout.addWidget(self.YPositionQSB, 1, 1, 1, 1)

        self.labelLength2_4 = QLabel(self.PositionGB)
        self.labelLength2_4.setObjectName(u"labelLength2_4")

        self.gridLayout.addWidget(self.labelLength2_4, 2, 0, 1, 1)

        self.ZPositionQSB = Gui_QuantitySpinBox(self.PositionGB)
        self.ZPositionQSB.setObjectName(u"ZPositionQSB")
        self.ZPositionQSB.setKeyboardTracking(False)
        self.ZPositionQSB.setProperty(u"unit", u"")

        self.gridLayout.addWidget(self.ZPositionQSB, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.viewPositionButton = QPushButton(self.PositionGB)
        self.viewPositionButton.setObjectName(u"viewPositionButton")

        self.verticalLayout_2.addWidget(self.viewPositionButton)


        self.verticalLayout.addWidget(self.PositionGB)

        self.RotationGB = QGroupBox(PartGui__Location)
        self.RotationGB.setObjectName(u"RotationGB")
        sizePolicy.setHeightForWidth(self.RotationGB.sizePolicy().hasHeightForWidth())
        self.RotationGB.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.RotationGB)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelXSkew = QLabel(self.RotationGB)
        self.labelXSkew.setObjectName(u"labelXSkew")

        self.gridLayout_2.addWidget(self.labelXSkew, 0, 0, 1, 1)

        self.XDirectionEdit = Gui_DoubleSpinBox(self.RotationGB)
        self.XDirectionEdit.setObjectName(u"XDirectionEdit")
        self.XDirectionEdit.setKeyboardTracking(False)
        self.XDirectionEdit.setMinimum(-100.000000000000000)
        self.XDirectionEdit.setMaximum(100.000000000000000)
        self.XDirectionEdit.setSingleStep(0.100000000000000)
        self.XDirectionEdit.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.XDirectionEdit, 0, 1, 1, 1)

        self.labelYSkew = QLabel(self.RotationGB)
        self.labelYSkew.setObjectName(u"labelYSkew")

        self.gridLayout_2.addWidget(self.labelYSkew, 1, 0, 1, 1)

        self.YDirectionEdit = Gui_DoubleSpinBox(self.RotationGB)
        self.YDirectionEdit.setObjectName(u"YDirectionEdit")
        self.YDirectionEdit.setKeyboardTracking(False)
        self.YDirectionEdit.setMinimum(-100.000000000000000)
        self.YDirectionEdit.setMaximum(100.000000000000000)
        self.YDirectionEdit.setSingleStep(0.100000000000000)
        self.YDirectionEdit.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.YDirectionEdit, 1, 1, 1, 1)

        self.labelZSkew = QLabel(self.RotationGB)
        self.labelZSkew.setObjectName(u"labelZSkew")

        self.gridLayout_2.addWidget(self.labelZSkew, 2, 0, 1, 1)

        self.ZDirectionEdit = Gui_DoubleSpinBox(self.RotationGB)
        self.ZDirectionEdit.setObjectName(u"ZDirectionEdit")
        self.ZDirectionEdit.setKeyboardTracking(False)
        self.ZDirectionEdit.setMinimum(-100.000000000000000)
        self.ZDirectionEdit.setMaximum(100.000000000000000)
        self.ZDirectionEdit.setSingleStep(0.100000000000000)
        self.ZDirectionEdit.setValue(1.000000000000000)
        self.ZDirectionEdit.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.ZDirectionEdit, 2, 1, 1, 1)

        self.labelLength2 = QLabel(self.RotationGB)
        self.labelLength2.setObjectName(u"labelLength2")

        self.gridLayout_2.addWidget(self.labelLength2, 3, 0, 1, 1)

        self.AngleQSB = Gui_QuantitySpinBox(self.RotationGB)
        self.AngleQSB.setObjectName(u"AngleQSB")
        self.AngleQSB.setProperty(u"unit", u"")
        self.AngleQSB.setSingleStep(5.000000000000000)

        self.gridLayout_2.addWidget(self.AngleQSB, 3, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.RotationGB)


        self.retranslateUi(PartGui__Location)

        QMetaObject.connectSlotsByName(PartGui__Location)
    # setupUi

    def retranslateUi(self, PartGui__Location):
        PartGui__Location.setWindowTitle(QCoreApplication.translate("PartGui::Location", u"Location", None))
        self.PositionGB.setTitle(QCoreApplication.translate("PartGui::Location", u"Position", None))
        self.labelLength2_2.setText(QCoreApplication.translate("PartGui::Location", u"X", None))
        self.labelLength2_3.setText(QCoreApplication.translate("PartGui::Location", u"Y", None))
        self.labelLength2_4.setText(QCoreApplication.translate("PartGui::Location", u"Z", None))
        self.viewPositionButton.setText(QCoreApplication.translate("PartGui::Location", u"3D View", None))
#if QT_CONFIG(tooltip)
        self.RotationGB.setToolTip(QCoreApplication.translate("PartGui::Location", u"Use custom vector for pad direction otherwise\n"
"the sketch plane's normal vector will be used", None))
#endif // QT_CONFIG(tooltip)
        self.RotationGB.setTitle(QCoreApplication.translate("PartGui::Location", u"Rotation Axis", None))
        self.labelXSkew.setText(QCoreApplication.translate("PartGui::Location", u"X", None))
#if QT_CONFIG(tooltip)
        self.XDirectionEdit.setToolTip(QCoreApplication.translate("PartGui::Location", u"X-component of direction vector", None))
#endif // QT_CONFIG(tooltip)
        self.labelYSkew.setText(QCoreApplication.translate("PartGui::Location", u"Y", None))
#if QT_CONFIG(tooltip)
        self.YDirectionEdit.setToolTip(QCoreApplication.translate("PartGui::Location", u"Y-component of direction vector", None))
#endif // QT_CONFIG(tooltip)
        self.labelZSkew.setText(QCoreApplication.translate("PartGui::Location", u"Z", None))
#if QT_CONFIG(tooltip)
        self.ZDirectionEdit.setToolTip(QCoreApplication.translate("PartGui::Location", u"Z-component of direction vector", None))
#endif // QT_CONFIG(tooltip)
        self.labelLength2.setText(QCoreApplication.translate("PartGui::Location", u"Angle", None))
    # retranslateUi

