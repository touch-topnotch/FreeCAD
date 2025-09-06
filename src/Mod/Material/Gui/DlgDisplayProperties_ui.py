# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgDisplayProperties.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QWidget)

class Ui_MatGui_DlgDisplayProperties(object):
    def setupUi(self, MatGui__DlgDisplayProperties):
        if not MatGui__DlgDisplayProperties.objectName():
            MatGui__DlgDisplayProperties.setObjectName(u"MatGui__DlgDisplayProperties")
        MatGui__DlgDisplayProperties.resize(290, 503)
        self.gridLayout_4 = QGridLayout(MatGui__DlgDisplayProperties)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox1 = QGroupBox(MatGui__DlgDisplayProperties)
        self.groupBox1.setObjectName(u"groupBox1")
        self.gridLayout_3 = QGridLayout(self.groupBox1)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.textLabel1 = QLabel(self.groupBox1)
        self.textLabel1.setObjectName(u"textLabel1")

        self.hboxLayout.addWidget(self.textLabel1)

        self.changeMode = QComboBox(self.groupBox1)
        self.changeMode.setObjectName(u"changeMode")

        self.hboxLayout.addWidget(self.changeMode)


        self.gridLayout_3.addLayout(self.hboxLayout, 0, 0, 1, 1)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setSpacing(6)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.hboxLayout1.setContentsMargins(0, 0, 0, 0)
        self.textLabel1_3 = QLabel(self.groupBox1)
        self.textLabel1_3.setObjectName(u"textLabel1_3")
        self.textLabel1_3.setEnabled(False)

        self.hboxLayout1.addWidget(self.textLabel1_3)

        self.changePlot = QComboBox(self.groupBox1)
        self.changePlot.setObjectName(u"changePlot")
        self.changePlot.setEnabled(False)

        self.hboxLayout1.addWidget(self.changePlot)


        self.gridLayout_3.addLayout(self.hboxLayout1, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox1, 0, 0, 1, 1)

        self.groupBox2 = QGroupBox(MatGui__DlgDisplayProperties)
        self.groupBox2.setObjectName(u"groupBox2")
        self.gridLayout1 = QGridLayout(self.groupBox2)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setSpacing(6)
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.hboxLayout2.setContentsMargins(0, 0, 0, 0)
        self.textLabel2 = QLabel(self.groupBox2)
        self.textLabel2.setObjectName(u"textLabel2")

        self.hboxLayout2.addWidget(self.textLabel2)

        self.spacerItem = QSpacerItem(71, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout2.addItem(self.spacerItem)

        self.spinPointSize = QSpinBox(self.groupBox2)
        self.spinPointSize.setObjectName(u"spinPointSize")
        self.spinPointSize.setMinimum(1)
        self.spinPointSize.setMaximum(64)
        self.spinPointSize.setValue(2)

        self.hboxLayout2.addWidget(self.spinPointSize)


        self.gridLayout1.addLayout(self.hboxLayout2, 0, 0, 1, 1)

        self.hboxLayout3 = QHBoxLayout()
        self.hboxLayout3.setSpacing(6)
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.hboxLayout3.setContentsMargins(0, 0, 0, 0)
        self.textLabel3 = QLabel(self.groupBox2)
        self.textLabel3.setObjectName(u"textLabel3")

        self.hboxLayout3.addWidget(self.textLabel3)

        self.spacerItem1 = QSpacerItem(71, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout3.addItem(self.spacerItem1)

        self.spinLineWidth = QSpinBox(self.groupBox2)
        self.spinLineWidth.setObjectName(u"spinLineWidth")
        self.spinLineWidth.setMinimum(1)
        self.spinLineWidth.setMaximum(64)
        self.spinLineWidth.setValue(2)

        self.hboxLayout3.addWidget(self.spinLineWidth)


        self.gridLayout1.addLayout(self.hboxLayout3, 1, 0, 1, 1)

        self.textLabel1_2 = QLabel(self.groupBox2)
        self.textLabel1_2.setObjectName(u"textLabel1_2")

        self.gridLayout1.addWidget(self.textLabel1_2, 2, 0, 1, 1)

        self.hboxLayout4 = QHBoxLayout()
        self.hboxLayout4.setSpacing(6)
        self.hboxLayout4.setObjectName(u"hboxLayout4")
        self.hboxLayout4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSlider = QSlider(self.groupBox2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.hboxLayout4.addWidget(self.horizontalSlider)

        self.spinTransparency = QSpinBox(self.groupBox2)
        self.spinTransparency.setObjectName(u"spinTransparency")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinTransparency.sizePolicy().hasHeightForWidth())
        self.spinTransparency.setSizePolicy(sizePolicy)
        self.spinTransparency.setMaximum(100)
        self.spinTransparency.setSingleStep(5)

        self.hboxLayout4.addWidget(self.spinTransparency)


        self.gridLayout1.addLayout(self.hboxLayout4, 3, 0, 1, 1)

        self.label = QLabel(self.groupBox2)
        self.label.setObjectName(u"label")

        self.gridLayout1.addWidget(self.label, 4, 0, 1, 1)

        self.hboxLayout5 = QHBoxLayout()
        self.hboxLayout5.setSpacing(6)
        self.hboxLayout5.setObjectName(u"hboxLayout5")
        self.hboxLayout5.setContentsMargins(0, 0, 0, 0)
        self.sliderLineTransparency = QSlider(self.groupBox2)
        self.sliderLineTransparency.setObjectName(u"sliderLineTransparency")
        self.sliderLineTransparency.setMaximum(100)
        self.sliderLineTransparency.setOrientation(Qt.Horizontal)

        self.hboxLayout5.addWidget(self.sliderLineTransparency)

        self.spinLineTransparency = QSpinBox(self.groupBox2)
        self.spinLineTransparency.setObjectName(u"spinLineTransparency")
        self.spinLineTransparency.setMaximum(100)
        self.spinLineTransparency.setSingleStep(5)

        self.hboxLayout5.addWidget(self.spinLineTransparency)


        self.gridLayout1.addLayout(self.hboxLayout5, 5, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox2, 2, 0, 1, 1)

        self.groupBox3 = QGroupBox(MatGui__DlgDisplayProperties)
        self.groupBox3.setObjectName(u"groupBox3")
        self.gridLayout_2 = QGridLayout(self.groupBox3)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.hboxLayout6 = QHBoxLayout()
        self.hboxLayout6.setSpacing(6)
        self.hboxLayout6.setObjectName(u"hboxLayout6")
        self.hboxLayout6.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addLayout(self.hboxLayout6, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.buttonPointColor = Gui_ColorButton(self.groupBox3)
        self.buttonPointColor.setObjectName(u"buttonPointColor")

        self.gridLayout.addWidget(self.buttonPointColor, 3, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.buttonColorPlot = QPushButton(self.groupBox3)
        self.buttonColorPlot.setObjectName(u"buttonColorPlot")
        self.buttonColorPlot.setText(u"Color Plot")

        self.gridLayout.addWidget(self.buttonColorPlot, 1, 1, 1, 1)

        self.buttonLineColor = Gui_ColorButton(self.groupBox3)
        self.buttonLineColor.setObjectName(u"buttonLineColor")

        self.gridLayout.addWidget(self.buttonLineColor, 2, 1, 1, 1)

        self.buttonCustomAppearance = QPushButton(self.groupBox3)
        self.buttonCustomAppearance.setObjectName(u"buttonCustomAppearance")
        self.buttonCustomAppearance.setText(u"Appearance")

        self.gridLayout.addWidget(self.buttonCustomAppearance, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.widgetMaterial = MatGui_MaterialTreeWidget(self.groupBox3)
        self.widgetMaterial.setObjectName(u"widgetMaterial")

        self.gridLayout_2.addWidget(self.widgetMaterial, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox3, 1, 0, 1, 1)

        QWidget.setTabOrder(self.changeMode, self.changePlot)
        QWidget.setTabOrder(self.changePlot, self.buttonLineColor)
        QWidget.setTabOrder(self.buttonLineColor, self.spinPointSize)
        QWidget.setTabOrder(self.spinPointSize, self.spinLineWidth)
        QWidget.setTabOrder(self.spinLineWidth, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.spinTransparency)
        QWidget.setTabOrder(self.spinTransparency, self.sliderLineTransparency)
        QWidget.setTabOrder(self.sliderLineTransparency, self.spinLineTransparency)

        self.retranslateUi(MatGui__DlgDisplayProperties)
        self.spinTransparency.valueChanged.connect(self.horizontalSlider.setValue)
        self.horizontalSlider.valueChanged.connect(self.spinTransparency.setValue)
        self.sliderLineTransparency.valueChanged.connect(self.spinLineTransparency.setValue)
        self.spinLineTransparency.valueChanged.connect(self.sliderLineTransparency.setValue)

        QMetaObject.connectSlotsByName(MatGui__DlgDisplayProperties)
    # setupUi

    def retranslateUi(self, MatGui__DlgDisplayProperties):
        MatGui__DlgDisplayProperties.setWindowTitle(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Display Properties", None))
        self.groupBox1.setTitle(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Viewing Mode", None))
        self.textLabel1.setText(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Document window", None))
        self.textLabel1_3.setText(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Plot mode", None))
        self.groupBox2.setTitle(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Display", None))
        self.textLabel2.setText(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Point size", None))
        self.textLabel3.setText(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Line width", None))
        self.textLabel1_2.setText(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Transparency", None))
        self.label.setText(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Line transparency", None))
        self.groupBox3.setTitle(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Material", None))
        self.label_4.setText(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Color plot", None))
        self.label_6.setText(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Custom appearance", None))
        self.label_5.setText(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Point color", None))
        self.label_3.setText(QCoreApplication.translate("MatGui::DlgDisplayProperties", u"Line color", None))
    # retranslateUi

