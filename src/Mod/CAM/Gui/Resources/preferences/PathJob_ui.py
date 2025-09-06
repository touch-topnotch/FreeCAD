# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PathJob.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QSizePolicy, QSpacerItem,
    QToolBox, QToolButton, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsPath(object):
    def setupUi(self, Gui__Dialog__DlgSettingsPath):
        if not Gui__Dialog__DlgSettingsPath.objectName():
            Gui__Dialog__DlgSettingsPath.setObjectName(u"Gui__Dialog__DlgSettingsPath")
        Gui__Dialog__DlgSettingsPath.resize(707, 728)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsPath)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(11, 11, 11, 11)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.toolBox = QToolBox(Gui__Dialog__DlgSettingsPath)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 681, 370))
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_4 = QGroupBox(self.page)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.leDefaultFilePath = QLineEdit(self.groupBox_4)
        self.leDefaultFilePath.setObjectName(u"leDefaultFilePath")

        self.gridLayout_2.addWidget(self.leDefaultFilePath, 0, 1, 1, 1)

        self.tbDefaultFilePath = QToolButton(self.groupBox_4)
        self.tbDefaultFilePath.setObjectName(u"tbDefaultFilePath")
        self.tbDefaultFilePath.setText(u"\u2026")

        self.gridLayout_2.addWidget(self.tbDefaultFilePath, 0, 3, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.leDefaultJobTemplate = QLineEdit(self.groupBox_4)
        self.leDefaultJobTemplate.setObjectName(u"leDefaultJobTemplate")

        self.gridLayout_2.addWidget(self.leDefaultJobTemplate, 1, 1, 1, 1)

        self.tbDefaultJobTemplate = QToolButton(self.groupBox_4)
        self.tbDefaultJobTemplate.setObjectName(u"tbDefaultJobTemplate")
        self.tbDefaultJobTemplate.setText(u"\u2026")

        self.gridLayout_2.addWidget(self.tbDefaultJobTemplate, 1, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.page)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.geometryTolerance = Gui_InputField(self.groupBox_3)
        self.geometryTolerance.setObjectName(u"geometryTolerance")

        self.gridLayout_4.addWidget(self.geometryTolerance, 0, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 1, 0, 1, 1)

        self.curveAccuracy = Gui_InputField(self.groupBox_3)
        self.curveAccuracy.setObjectName(u"curveAccuracy")

        self.gridLayout_4.addWidget(self.curveAccuracy, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"General")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 681, 518))
        self.verticalLayout = QVBoxLayout(self.page_2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setContentsMargins(11, 11, 11, 11)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.formLayout_2.setLayout(1, QFormLayout.LabelRole, self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leOutputFile = QLineEdit(self.groupBox_2)
        self.leOutputFile.setObjectName(u"leOutputFile")

        self.horizontalLayout_2.addWidget(self.leOutputFile)

        self.tbOutputFile = QToolButton(self.groupBox_2)
        self.tbOutputFile.setObjectName(u"tbOutputFile")
        self.tbOutputFile.setText(u"\u2026")

        self.horizontalLayout_2.addWidget(self.tbOutputFile)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)


        self.formLayout_2.setLayout(2, QFormLayout.LabelRole, self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cboOutputPolicy = QComboBox(self.groupBox_2)
        self.cboOutputPolicy.addItem("")
        self.cboOutputPolicy.addItem("")
        self.cboOutputPolicy.addItem("")
        self.cboOutputPolicy.addItem("")
        self.cboOutputPolicy.setObjectName(u"cboOutputPolicy")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cboOutputPolicy.sizePolicy().hasHeightForWidth())
        self.cboOutputPolicy.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.cboOutputPolicy)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_5)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.page_2)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setSpacing(6)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.postProcessorList = QListWidget(self.groupBox)
        self.postProcessorList.setObjectName(u"postProcessorList")
        self.postProcessorList.setMouseTracking(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.postProcessorList)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.defaultPostProcessor = QComboBox(self.groupBox)
        self.defaultPostProcessor.setObjectName(u"defaultPostProcessor")
        self.defaultPostProcessor.setProperty(u"prefEntry", u"DefaultPostProcessor")
        self.defaultPostProcessor.setProperty(u"prefPath", u"Mod/CAM")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.defaultPostProcessor)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.defaultPostProcessorArgs = QLineEdit(self.groupBox)
        self.defaultPostProcessorArgs.setObjectName(u"defaultPostProcessorArgs")
        self.defaultPostProcessorArgs.setProperty(u"prefEntry", u"DefaultPostProcessorArgs")
        self.defaultPostProcessorArgs.setProperty(u"prefPath", u"Mod/CAM")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.defaultPostProcessorArgs)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.page_2, u"Post processor")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 662, 755))
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stockGroup = QGroupBox(self.page_3)
        self.stockGroup.setObjectName(u"stockGroup")
        self.stockGroup.setCheckable(True)
        self.stockGroup.setChecked(False)
        self.verticalLayout_5 = QVBoxLayout(self.stockGroup)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stock = QComboBox(self.stockGroup)
        self.stock.addItem("")
        self.stock.addItem("")
        self.stock.addItem("")
        self.stock.setObjectName(u"stock")

        self.verticalLayout_5.addWidget(self.stock)

        self.horizontalSpacer = QSpacerItem(40, 6, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer)

        self.stockFromBase = QFrame(self.stockGroup)
        self.stockFromBase.setObjectName(u"stockFromBase")
        self.gridLayout_9 = QGridLayout(self.stockFromBase)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.stockExtXLabel = QLabel(self.stockFromBase)
        self.stockExtXLabel.setObjectName(u"stockExtXLabel")

        self.gridLayout_9.addWidget(self.stockExtXLabel, 0, 1, 1, 1)

        self.stockExtXneg = Gui_InputField(self.stockFromBase)
        self.stockExtXneg.setObjectName(u"stockExtXneg")

        self.gridLayout_9.addWidget(self.stockExtXneg, 0, 2, 1, 1)

        self.stockExtXpos = Gui_InputField(self.stockFromBase)
        self.stockExtXpos.setObjectName(u"stockExtXpos")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stockExtXpos.sizePolicy().hasHeightForWidth())
        self.stockExtXpos.setSizePolicy(sizePolicy2)

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
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setContentsMargins(11, 11, 11, 11)
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
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setContentsMargins(11, 11, 11, 11)
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

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_2)

        self.stockPlacementGroup = QGroupBox(self.stockGroup)
        self.stockPlacementGroup.setObjectName(u"stockPlacementGroup")
        self.stockPlacementGroup.setCheckable(True)
        self.stockPlacementGroup.setChecked(False)
        self.gridLayout_3 = QGridLayout(self.stockPlacementGroup)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_9 = QLabel(self.stockPlacementGroup)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.stockAngle = Gui_InputField(self.stockPlacementGroup)
        self.stockAngle.setObjectName(u"stockAngle")

        self.gridLayout_3.addWidget(self.stockAngle, 0, 2, 1, 1)

        self.label_11 = QLabel(self.stockPlacementGroup)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)

        self.stockAxisX = QDoubleSpinBox(self.stockPlacementGroup)
        self.stockAxisX.setObjectName(u"stockAxisX")
        self.stockAxisX.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_3.addWidget(self.stockAxisX, 3, 2, 1, 1)

        self.stockAxisY = QDoubleSpinBox(self.stockPlacementGroup)
        self.stockAxisY.setObjectName(u"stockAxisY")
        self.stockAxisY.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_3.addWidget(self.stockAxisY, 3, 3, 1, 1)

        self.stockAxisZ = QDoubleSpinBox(self.stockPlacementGroup)
        self.stockAxisZ.setObjectName(u"stockAxisZ")
        self.stockAxisZ.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_3.addWidget(self.stockAxisZ, 3, 4, 1, 1)

        self.label_10 = QLabel(self.stockPlacementGroup)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 1)

        self.stockPositionX = Gui_InputField(self.stockPlacementGroup)
        self.stockPositionX.setObjectName(u"stockPositionX")

        self.gridLayout_3.addWidget(self.stockPositionX, 4, 2, 1, 1)

        self.stockPositionY = Gui_InputField(self.stockPlacementGroup)
        self.stockPositionY.setObjectName(u"stockPositionY")

        self.gridLayout_3.addWidget(self.stockPositionY, 4, 3, 1, 1)

        self.stockPositionZ = Gui_InputField(self.stockPlacementGroup)
        self.stockPositionZ.setObjectName(u"stockPositionZ")

        self.gridLayout_3.addWidget(self.stockPositionZ, 4, 4, 1, 1)


        self.verticalLayout_5.addWidget(self.stockPlacementGroup)


        self.verticalLayout_3.addWidget(self.stockGroup)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.page_3, u"Setup")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 681, 171))
        self.verticalLayout_4 = QVBoxLayout(self.page_4)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.toolsAbsolutePaths = QCheckBox(self.page_4)
        self.toolsAbsolutePaths.setObjectName(u"toolsAbsolutePaths")

        self.verticalLayout_4.addWidget(self.toolsAbsolutePaths)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.toolBox.addItem(self.page_4, u"Tools")

        self.vboxLayout.addWidget(self.toolBox)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer_5)

        QWidget.setTabOrder(self.leDefaultFilePath, self.tbDefaultFilePath)
        QWidget.setTabOrder(self.tbDefaultFilePath, self.leDefaultJobTemplate)
        QWidget.setTabOrder(self.leDefaultJobTemplate, self.tbDefaultJobTemplate)
        QWidget.setTabOrder(self.tbDefaultJobTemplate, self.geometryTolerance)
        QWidget.setTabOrder(self.geometryTolerance, self.leOutputFile)
        QWidget.setTabOrder(self.leOutputFile, self.tbOutputFile)
        QWidget.setTabOrder(self.tbOutputFile, self.cboOutputPolicy)
        QWidget.setTabOrder(self.cboOutputPolicy, self.postProcessorList)
        QWidget.setTabOrder(self.postProcessorList, self.defaultPostProcessor)
        QWidget.setTabOrder(self.defaultPostProcessor, self.defaultPostProcessorArgs)
        QWidget.setTabOrder(self.defaultPostProcessorArgs, self.stockGroup)
        QWidget.setTabOrder(self.stockGroup, self.stock)
        QWidget.setTabOrder(self.stock, self.stockExtXneg)
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
        QWidget.setTabOrder(self.stockBoxHeight, self.stockPlacementGroup)
        QWidget.setTabOrder(self.stockPlacementGroup, self.stockAngle)
        QWidget.setTabOrder(self.stockAngle, self.stockAxisX)
        QWidget.setTabOrder(self.stockAxisX, self.stockAxisY)
        QWidget.setTabOrder(self.stockAxisY, self.stockAxisZ)
        QWidget.setTabOrder(self.stockAxisZ, self.stockPositionX)
        QWidget.setTabOrder(self.stockPositionX, self.stockPositionY)
        QWidget.setTabOrder(self.stockPositionY, self.stockPositionZ)

        self.retranslateUi(Gui__Dialog__DlgSettingsPath)

        self.toolBox.setCurrentIndex(0)
        self.stock.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsPath)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsPath):
        Gui__Dialog__DlgSettingsPath.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Job Preferences", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Defaults", None))
        self.label_7.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Path", None))
#if QT_CONFIG(tooltip)
        self.leDefaultFilePath.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Path to look for templates, post processors, tool tables and other external files.\n"
"\n"
"If left empty the macro directory is used.", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Template", None))
#if QT_CONFIG(tooltip)
        self.leDefaultJobTemplate.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"The default template to be selected when creating a new job.\n"
"\n"
"This can be helpful when almost all jobs will be processed by the same machine with a similar setup.\n"
"\n"
"If left empty no template will be preselected.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Geometry", None))
        self.label_6.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Default geometry tolerance", None))
#if QT_CONFIG(tooltip)
        self.geometryTolerance.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Default value for new jobs, used for computing Paths. Smaller increases accuracy, but slows down computation", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Default curve accuracy", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"General", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Output File", None))
        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Default path", None))
#if QT_CONFIG(tooltip)
        self.leOutputFile.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Enter a path and optionally file name (see below) to be used as the default for the post processor export.\n"
"The following substitutions are performed before the name is resolved at the time of the post processing:\n"
"Substitution allows the following:\n"
"%D ... directory of the active document\n"
"%d ... name of the active document (with extension)\n"
"%M ... user macro directory\n"
"%j ... name of the active Job object\n"
"\n"
"The Following can be used if output is being split. If Output is not split\n"
"these will be ignored.\n"
"%T ... Tool Number\n"
"%t ... Tool Controller label\n"
"\n"
"%W ... Work Coordinate System\n"
"%O ... Operation Label\n"
"\n"
"When splitting output, a sequence number will always be added.\n"
"\n"
"if %S is included, you can specify where the number occurs.  Without it, the number will be added to the end of the string.\n"
"\n"
"%S ... Sequence Number\n"
"\n"
"The following example stores all files with the same name as the document in the directory /home/freecad (please remo"
                        "ve quotes):\n"
"&quot;/home/cnc/%d.g-code&quot;\n"
"See the file save policy below on how to deal with name conflicts.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"File save policy", None))
        self.cboOutputPolicy.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Open file dialog", None))
        self.cboOutputPolicy.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Open file dialog on conflict", None))
        self.cboOutputPolicy.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Overwrite existing file", None))
        self.cboOutputPolicy.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Append Unique ID on conflict", None))

#if QT_CONFIG(tooltip)
        self.cboOutputPolicy.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Choose how to deal with potential file name conflicts. Always open a dialog, only open a dialog if the output file already exists, overwrite any existing file or add a unique (3 digit) sequential ID to the file name.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Post Processor", None))
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Post processors selection", None))
#if QT_CONFIG(tooltip)
        self.postProcessorList.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"It doesn't seem there are any post processor scripts installed. Please add some into your macro directory and make sure the file name ends with &quot;_post.py&quot;.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Default post processor", None))
#if QT_CONFIG(tooltip)
        self.defaultPostProcessor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Select one of the post processors as the default", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Default arguments", None))
#if QT_CONFIG(tooltip)
        self.defaultPostProcessorArgs.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Optional arguments passed to the default post processor specified above. See the post processor's documentation for supported arguments.", None))
#endif // QT_CONFIG(tooltip)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Post processor", None))
        self.stockGroup.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Stock", None))
        self.stock.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Create box", None))
        self.stock.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Create cylinder", None))
        self.stock.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Extend model's bounding box", None))

        self.stockExtXLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Ext. X", None))
        self.stockExtYLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Ext. Y", None))
        self.stockExtZLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Ext. Z", None))
        self.stockCylinderRadiusLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Radius", None))
        self.stockCylinderHeightLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Height", None))
        self.stockBoxLengthLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Length", None))
        self.stockBoxWidthLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Width", None))
        self.stockBoxHeightLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Height", None))
        self.stockPlacementGroup.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Placement", None))
        self.label_9.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Angle", None))
        self.label_11.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Axis", None))
        self.label_10.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Position", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Setup", None))
#if QT_CONFIG(tooltip)
        self.toolsAbsolutePaths.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"References to tool bits and their shapes can either be stored with an absolute path or with a relative path to the search path.\n"
"Generally it is recommended to use relative paths due to their flexibility and robustness to layout changes.\n"
"Should multiple tools or tool shapes with the same name exist in different directories it can be required to use absolute paths.", None))
#endif // QT_CONFIG(tooltip)
        self.toolsAbsolutePaths.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Store Absolute Paths", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("Gui::Dialog::DlgSettingsPath", u"Tools", None))
    # retranslateUi

