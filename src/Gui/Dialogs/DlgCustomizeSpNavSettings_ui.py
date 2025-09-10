# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgCustomizeSpNavSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_DlgCustomizeSpNavSettings(object):
    def setupUi(self, DlgCustomizeSpNavSettings):
        if not DlgCustomizeSpNavSettings.objectName():
            DlgCustomizeSpNavSettings.setObjectName(u"DlgCustomizeSpNavSettings")
        DlgCustomizeSpNavSettings.resize(439, 537)
        self.verticalLayout_12 = QVBoxLayout(DlgCustomizeSpNavSettings)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelSlow = QLabel(DlgCustomizeSpNavSettings)
        self.labelSlow.setObjectName(u"labelSlow")

        self.horizontalLayout_2.addWidget(self.labelSlow)

        self.SliderGlobal = QSlider(DlgCustomizeSpNavSettings)
        self.SliderGlobal.setObjectName(u"SliderGlobal")
        self.SliderGlobal.setMinimum(-50)
        self.SliderGlobal.setMaximum(50)
        self.SliderGlobal.setOrientation(Qt.Horizontal)
        self.SliderGlobal.setTickPosition(QSlider.TicksBelow)
        self.SliderGlobal.setTickInterval(10)

        self.horizontalLayout_2.addWidget(self.SliderGlobal)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.CBDominant = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBDominant.setObjectName(u"CBDominant")

        self.verticalLayout_10.addWidget(self.CBDominant)

        self.CBFlipYZ = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBFlipYZ.setObjectName(u"CBFlipYZ")

        self.verticalLayout_10.addWidget(self.CBFlipYZ)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.CBTranslations = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBTranslations.setObjectName(u"CBTranslations")
        self.CBTranslations.setChecked(True)

        self.verticalLayout_11.addWidget(self.CBTranslations)

        self.CBRotations = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBRotations.setObjectName(u"CBRotations")
        self.CBRotations.setChecked(True)

        self.verticalLayout_11.addWidget(self.CBRotations)


        self.horizontalLayout_3.addLayout(self.verticalLayout_11)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.ButtonCalibrate = QPushButton(DlgCustomizeSpNavSettings)
        self.ButtonCalibrate.setObjectName(u"ButtonCalibrate")

        self.horizontalLayout_3.addWidget(self.ButtonCalibrate)

        self.ButtonDefaultSpNavMotions = QPushButton(DlgCustomizeSpNavSettings)
        self.ButtonDefaultSpNavMotions.setObjectName(u"ButtonDefaultSpNavMotions")

        self.horizontalLayout_3.addWidget(self.ButtonDefaultSpNavMotions)


        self.verticalLayout_12.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 116, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ImagePanLR = QLabel(DlgCustomizeSpNavSettings)
        self.ImagePanLR.setObjectName(u"ImagePanLR")
        self.ImagePanLR.setPixmap(QPixmap(u":/icons/SpNav-PanLR"))

        self.verticalLayout.addWidget(self.ImagePanLR)

        self.ImagePanUD = QLabel(DlgCustomizeSpNavSettings)
        self.ImagePanUD.setObjectName(u"ImagePanUD")
        self.ImagePanUD.setPixmap(QPixmap(u":/icons/SpNav-PanUD"))

        self.verticalLayout.addWidget(self.ImagePanUD)

        self.ImageZoom = QLabel(DlgCustomizeSpNavSettings)
        self.ImageZoom.setObjectName(u"ImageZoom")
        self.ImageZoom.setPixmap(QPixmap(u":/icons/SpNav-Zoom"))

        self.verticalLayout.addWidget(self.ImageZoom)

        self.imageTilt = QLabel(DlgCustomizeSpNavSettings)
        self.imageTilt.setObjectName(u"imageTilt")
        self.imageTilt.setPixmap(QPixmap(u":/icons/SpNav-Tilt"))

        self.verticalLayout.addWidget(self.imageTilt)

        self.ImageRoll = QLabel(DlgCustomizeSpNavSettings)
        self.ImageRoll.setObjectName(u"ImageRoll")
        self.ImageRoll.setPixmap(QPixmap(u":/icons/SpNav-Roll"))

        self.verticalLayout.addWidget(self.ImageRoll)

        self.ImageSpin = QLabel(DlgCustomizeSpNavSettings)
        self.ImageSpin.setObjectName(u"ImageSpin")
        self.ImageSpin.setPixmap(QPixmap(u":/icons/SpNav-Spin"))

        self.verticalLayout.addWidget(self.ImageSpin)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.CBEnablePanLR = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBEnablePanLR.setObjectName(u"CBEnablePanLR")
        self.CBEnablePanLR.setChecked(True)

        self.verticalLayout_2.addWidget(self.CBEnablePanLR)

        self.CBReversePanLR = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBReversePanLR.setObjectName(u"CBReversePanLR")

        self.verticalLayout_2.addWidget(self.CBReversePanLR)


        self.verticalLayout_9.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.CBEnablePanUD = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBEnablePanUD.setObjectName(u"CBEnablePanUD")
        self.CBEnablePanUD.setChecked(True)

        self.verticalLayout_4.addWidget(self.CBEnablePanUD)

        self.CBReversePanUD = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBReversePanUD.setObjectName(u"CBReversePanUD")

        self.verticalLayout_4.addWidget(self.CBReversePanUD)


        self.verticalLayout_9.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.CBEnableZoom = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBEnableZoom.setObjectName(u"CBEnableZoom")
        self.CBEnableZoom.setChecked(True)

        self.verticalLayout_5.addWidget(self.CBEnableZoom)

        self.CBReverseZoom = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBReverseZoom.setObjectName(u"CBReverseZoom")

        self.verticalLayout_5.addWidget(self.CBReverseZoom)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.CBEnableTilt = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBEnableTilt.setObjectName(u"CBEnableTilt")
        self.CBEnableTilt.setChecked(True)

        self.verticalLayout_6.addWidget(self.CBEnableTilt)

        self.CBReverseTilt = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBReverseTilt.setObjectName(u"CBReverseTilt")

        self.verticalLayout_6.addWidget(self.CBReverseTilt)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.CBEnableRoll = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBEnableRoll.setObjectName(u"CBEnableRoll")
        self.CBEnableRoll.setChecked(True)

        self.verticalLayout_7.addWidget(self.CBEnableRoll)

        self.CBReverseRoll = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBReverseRoll.setObjectName(u"CBReverseRoll")

        self.verticalLayout_7.addWidget(self.CBReverseRoll)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.CBEnableSpin = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBEnableSpin.setObjectName(u"CBEnableSpin")
        self.CBEnableSpin.setChecked(True)

        self.verticalLayout_8.addWidget(self.CBEnableSpin)

        self.CBReverseSpin = QCheckBox(DlgCustomizeSpNavSettings)
        self.CBReverseSpin.setObjectName(u"CBReverseSpin")

        self.verticalLayout_8.addWidget(self.CBReverseSpin)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.horizontalLayout.addLayout(self.verticalLayout_9)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SliderPanLR = QSlider(DlgCustomizeSpNavSettings)
        self.SliderPanLR.setObjectName(u"SliderPanLR")
        self.SliderPanLR.setMinimum(-50)
        self.SliderPanLR.setMaximum(50)
        self.SliderPanLR.setSingleStep(1)
        self.SliderPanLR.setPageStep(1)
        self.SliderPanLR.setValue(0)
        self.SliderPanLR.setOrientation(Qt.Horizontal)
        self.SliderPanLR.setTickPosition(QSlider.TicksBelow)
        self.SliderPanLR.setTickInterval(10)

        self.verticalLayout_3.addWidget(self.SliderPanLR)

        self.SliderPanUD = QSlider(DlgCustomizeSpNavSettings)
        self.SliderPanUD.setObjectName(u"SliderPanUD")
        self.SliderPanUD.setMinimum(-50)
        self.SliderPanUD.setMaximum(50)
        self.SliderPanUD.setSingleStep(1)
        self.SliderPanUD.setPageStep(1)
        self.SliderPanUD.setValue(0)
        self.SliderPanUD.setOrientation(Qt.Horizontal)
        self.SliderPanUD.setTickPosition(QSlider.TicksBelow)
        self.SliderPanUD.setTickInterval(10)

        self.verticalLayout_3.addWidget(self.SliderPanUD)

        self.SliderZoom = QSlider(DlgCustomizeSpNavSettings)
        self.SliderZoom.setObjectName(u"SliderZoom")
        self.SliderZoom.setMinimum(-50)
        self.SliderZoom.setMaximum(50)
        self.SliderZoom.setSingleStep(1)
        self.SliderZoom.setPageStep(1)
        self.SliderZoom.setValue(0)
        self.SliderZoom.setOrientation(Qt.Horizontal)
        self.SliderZoom.setTickPosition(QSlider.TicksBelow)
        self.SliderZoom.setTickInterval(10)

        self.verticalLayout_3.addWidget(self.SliderZoom)

        self.SliderTilt = QSlider(DlgCustomizeSpNavSettings)
        self.SliderTilt.setObjectName(u"SliderTilt")
        self.SliderTilt.setMinimum(-50)
        self.SliderTilt.setMaximum(50)
        self.SliderTilt.setSingleStep(1)
        self.SliderTilt.setPageStep(1)
        self.SliderTilt.setValue(0)
        self.SliderTilt.setOrientation(Qt.Horizontal)
        self.SliderTilt.setTickPosition(QSlider.TicksBelow)
        self.SliderTilt.setTickInterval(10)

        self.verticalLayout_3.addWidget(self.SliderTilt)

        self.SliderRoll = QSlider(DlgCustomizeSpNavSettings)
        self.SliderRoll.setObjectName(u"SliderRoll")
        self.SliderRoll.setMinimum(-50)
        self.SliderRoll.setMaximum(50)
        self.SliderRoll.setSingleStep(1)
        self.SliderRoll.setPageStep(1)
        self.SliderRoll.setValue(0)
        self.SliderRoll.setOrientation(Qt.Horizontal)
        self.SliderRoll.setTickPosition(QSlider.TicksBelow)
        self.SliderRoll.setTickInterval(10)

        self.verticalLayout_3.addWidget(self.SliderRoll)

        self.SliderSpin = QSlider(DlgCustomizeSpNavSettings)
        self.SliderSpin.setObjectName(u"SliderSpin")
        self.SliderSpin.setMinimum(-50)
        self.SliderSpin.setMaximum(50)
        self.SliderSpin.setSingleStep(1)
        self.SliderSpin.setPageStep(1)
        self.SliderSpin.setValue(0)
        self.SliderSpin.setOrientation(Qt.Horizontal)
        self.SliderSpin.setTickPosition(QSlider.TicksBelow)
        self.SliderSpin.setTickInterval(10)

        self.verticalLayout_3.addWidget(self.SliderSpin)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout)


        self.retranslateUi(DlgCustomizeSpNavSettings)

        QMetaObject.connectSlotsByName(DlgCustomizeSpNavSettings)
    # setupUi

    def retranslateUi(self, DlgCustomizeSpNavSettings):
        DlgCustomizeSpNavSettings.setWindowTitle(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Spaceball Motion", None))
        self.labelSlow.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Global Sensitivity:", None))
        self.CBDominant.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Dominant Mode", None))
        self.CBFlipYZ.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Flip Y/Z", None))
        self.CBTranslations.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Enable Translations", None))
        self.CBRotations.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Enable Rotations", None))
        self.ButtonCalibrate.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Calibrate", None))
        self.ButtonDefaultSpNavMotions.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Default", None))
        self.ImagePanLR.setText("")
        self.ImagePanUD.setText("")
        self.ImageZoom.setText("")
        self.imageTilt.setText("")
        self.ImageRoll.setText("")
        self.ImageSpin.setText("")
        self.CBEnablePanLR.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Enable", None))
        self.CBReversePanLR.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Reverse", None))
        self.CBEnablePanUD.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Enable", None))
        self.CBReversePanUD.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Reverse", None))
        self.CBEnableZoom.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Enable", None))
        self.CBReverseZoom.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Reverse", None))
        self.CBEnableTilt.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Enable", None))
        self.CBReverseTilt.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Reverse", None))
        self.CBEnableRoll.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Enable", None))
        self.CBReverseRoll.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Reverse", None))
        self.CBEnableSpin.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Enable", None))
        self.CBReverseSpin.setText(QCoreApplication.translate("DlgCustomizeSpNavSettings", u"Reverse", None))
    # retranslateUi

