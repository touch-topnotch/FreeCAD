# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskImage.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Gui_TaskImage(object):
    def setupUi(self, Gui__TaskImage):
        if not Gui__TaskImage.objectName():
            Gui__TaskImage.setObjectName(u"Gui__TaskImage")
        Gui__TaskImage.resize(421, 267)
        self.gridLayout_5 = QGridLayout(Gui__TaskImage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox = QGroupBox(Gui__TaskImage)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.XY_radioButton = QRadioButton(self.groupBox)
        self.XY_radioButton.setObjectName(u"XY_radioButton")

        self.verticalLayout.addWidget(self.XY_radioButton)

        self.XZ_radioButton = QRadioButton(self.groupBox)
        self.XZ_radioButton.setObjectName(u"XZ_radioButton")

        self.verticalLayout.addWidget(self.XZ_radioButton)

        self.YZ_radioButton = QRadioButton(self.groupBox)
        self.YZ_radioButton.setObjectName(u"YZ_radioButton")

        self.verticalLayout.addWidget(self.YZ_radioButton)


        self.gridLayout_8.addWidget(self.groupBox, 0, 0, 1, 1)

        self.previewLabel = QLabel(Gui__TaskImage)
        self.previewLabel.setObjectName(u"previewLabel")
        self.previewLabel.setMinimumSize(QSize(48, 48))
        self.previewLabel.setMaximumSize(QSize(48, 48))
        self.previewLabel.setText(u"Preview")

        self.gridLayout_8.addWidget(self.previewLabel, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_8, 0, 0, 1, 2)

        self.Reverse_checkBox = QCheckBox(Gui__TaskImage)
        self.Reverse_checkBox.setObjectName(u"Reverse_checkBox")

        self.gridLayout_5.addWidget(self.Reverse_checkBox, 1, 0, 1, 2)

        self.labelZ = QLabel(Gui__TaskImage)
        self.labelZ.setObjectName(u"labelZ")

        self.gridLayout_5.addWidget(self.labelZ, 2, 0, 1, 1)

        self.spinBoxZ = Gui_QuantitySpinBox(Gui__TaskImage)
        self.spinBoxZ.setObjectName(u"spinBoxZ")
        self.spinBoxZ.setProperty(u"unit", u"mm")
        self.spinBoxZ.setProperty(u"minimum", -999999999.000000000000000)
        self.spinBoxZ.setProperty(u"maximum", 999999999.000000000000000)

        self.gridLayout_5.addWidget(self.spinBoxZ, 2, 1, 1, 1)

        self.labelX = QLabel(Gui__TaskImage)
        self.labelX.setObjectName(u"labelX")

        self.gridLayout_5.addWidget(self.labelX, 3, 0, 1, 1)

        self.spinBoxX = Gui_QuantitySpinBox(Gui__TaskImage)
        self.spinBoxX.setObjectName(u"spinBoxX")
        self.spinBoxX.setProperty(u"unit", u"mm")
        self.spinBoxX.setProperty(u"minimum", -999999999.000000000000000)
        self.spinBoxX.setProperty(u"maximum", 999999999.000000000000000)

        self.gridLayout_5.addWidget(self.spinBoxX, 3, 1, 1, 1)

        self.labelY = QLabel(Gui__TaskImage)
        self.labelY.setObjectName(u"labelY")

        self.gridLayout_5.addWidget(self.labelY, 4, 0, 1, 1)

        self.spinBoxY = Gui_QuantitySpinBox(Gui__TaskImage)
        self.spinBoxY.setObjectName(u"spinBoxY")
        self.spinBoxY.setProperty(u"unit", u"mm")
        self.spinBoxY.setProperty(u"minimum", -999999999.000000000000000)
        self.spinBoxY.setProperty(u"maximum", 999999999.000000000000000)

        self.gridLayout_5.addWidget(self.spinBoxY, 4, 1, 1, 1)

        self.labelRotation = QLabel(Gui__TaskImage)
        self.labelRotation.setObjectName(u"labelRotation")

        self.gridLayout_5.addWidget(self.labelRotation, 5, 0, 1, 1)

        self.spinBoxRotation = Gui_QuantitySpinBox(Gui__TaskImage)
        self.spinBoxRotation.setObjectName(u"spinBoxRotation")
        self.spinBoxRotation.setProperty(u"unit", u"deg")

        self.gridLayout_5.addWidget(self.spinBoxRotation, 5, 1, 1, 1)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.labelTransparency = QLabel(Gui__TaskImage)
        self.labelTransparency.setObjectName(u"labelTransparency")

        self.hboxLayout.addWidget(self.labelTransparency)

        self.sliderTransparency = QSlider(Gui__TaskImage)
        self.sliderTransparency.setObjectName(u"sliderTransparency")
        self.sliderTransparency.setMaximum(100)
        self.sliderTransparency.setOrientation(Qt.Horizontal)

        self.hboxLayout.addWidget(self.sliderTransparency)

        self.spinBoxTransparency = QSpinBox(Gui__TaskImage)
        self.spinBoxTransparency.setObjectName(u"spinBoxTransparency")
        self.spinBoxTransparency.setValue(0)
        self.spinBoxTransparency.setMinimum(0)
        self.spinBoxTransparency.setMaximum(100)

        self.hboxLayout.addWidget(self.spinBoxTransparency)


        self.gridLayout_5.addLayout(self.hboxLayout, 6, 0, 1, 2)

        self.groupBox1 = QGroupBox(Gui__TaskImage)
        self.groupBox1.setObjectName(u"groupBox1")
        self.gridLayout_2 = QGridLayout(self.groupBox1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox1)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.spinBoxWidth = Gui_QuantitySpinBox(self.groupBox1)
        self.spinBoxWidth.setObjectName(u"spinBoxWidth")
        self.spinBoxWidth.setProperty(u"unit", u"mm")
        self.spinBoxWidth.setProperty(u"minimum", 0.000000010000000)
        self.spinBoxWidth.setProperty(u"maximum", 999999999.000000000000000)

        self.gridLayout_2.addWidget(self.spinBoxWidth, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinBoxHeight = Gui_QuantitySpinBox(self.groupBox1)
        self.spinBoxHeight.setObjectName(u"spinBoxHeight")
        self.spinBoxHeight.setProperty(u"unit", u"mm")
        self.spinBoxHeight.setProperty(u"minimum", 0.000000010000000)
        self.spinBoxHeight.setProperty(u"maximum", 999999999.000000000000000)

        self.gridLayout_2.addWidget(self.spinBoxHeight, 1, 1, 1, 1)

        self.checkBoxRatio = QCheckBox(self.groupBox1)
        self.checkBoxRatio.setObjectName(u"checkBoxRatio")
        self.checkBoxRatio.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBoxRatio, 2, 0, 1, 2)

        self.pushButtonScale = QPushButton(self.groupBox1)
        self.pushButtonScale.setObjectName(u"pushButtonScale")

        self.gridLayout_2.addWidget(self.pushButtonScale, 3, 0, 1, 2)

        self.groupBoxCalibration = QGroupBox(self.groupBox1)
        self.groupBoxCalibration.setObjectName(u"groupBoxCalibration")
        self.horizontalLayout = QHBoxLayout(self.groupBoxCalibration)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonApply = QPushButton(self.groupBoxCalibration)
        self.pushButtonApply.setObjectName(u"pushButtonApply")

        self.horizontalLayout.addWidget(self.pushButtonApply)

        self.pushButtonCancel = QPushButton(self.groupBoxCalibration)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.horizontalLayout.addWidget(self.pushButtonCancel)


        self.gridLayout_2.addWidget(self.groupBoxCalibration, 4, 0, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox1, 7, 0, 1, 2)


        self.retranslateUi(Gui__TaskImage)

        QMetaObject.connectSlotsByName(Gui__TaskImage)
    # setupUi

    def retranslateUi(self, Gui__TaskImage):
        Gui__TaskImage.setWindowTitle(QCoreApplication.translate("Gui::TaskImage", u"Image plane settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::TaskImage", u"Planes", None))
        self.XY_radioButton.setText(QCoreApplication.translate("Gui::TaskImage", u"XY-Plane", None))
        self.XZ_radioButton.setText(QCoreApplication.translate("Gui::TaskImage", u"XZ-Plane", None))
        self.YZ_radioButton.setText(QCoreApplication.translate("Gui::TaskImage", u"YZ-Plane", None))
        self.Reverse_checkBox.setText(QCoreApplication.translate("Gui::TaskImage", u"Reverse direction", None))
        self.labelZ.setText(QCoreApplication.translate("Gui::TaskImage", u"Offset:", None))
        self.labelX.setText(QCoreApplication.translate("Gui::TaskImage", u"X distance:", None))
        self.labelY.setText(QCoreApplication.translate("Gui::TaskImage", u"Y distance:", None))
        self.labelRotation.setText(QCoreApplication.translate("Gui::TaskImage", u"Rotation :", None))
        self.labelTransparency.setText(QCoreApplication.translate("Gui::TaskImage", u"Transparency :", None))
        self.groupBox1.setTitle(QCoreApplication.translate("Gui::TaskImage", u"Image size", None))
        self.label.setText(QCoreApplication.translate("Gui::TaskImage", u"Width:", None))
        self.label_2.setText(QCoreApplication.translate("Gui::TaskImage", u"Height:", None))
        self.checkBoxRatio.setText(QCoreApplication.translate("Gui::TaskImage", u"Keep aspect ratio", None))
#if QT_CONFIG(tooltip)
        self.pushButtonScale.setToolTip(QCoreApplication.translate("Gui::TaskImage", u"Interactively scale the image by setting a length between two points of the image.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonScale.setText(QCoreApplication.translate("Gui::TaskImage", u"Calibrate", None))
        self.groupBoxCalibration.setTitle(QCoreApplication.translate("Gui::TaskImage", u"Calibration", None))
        self.pushButtonApply.setText(QCoreApplication.translate("Gui::TaskImage", u"Apply", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Gui::TaskImage", u"Cancel", None))
    # retranslateUi

