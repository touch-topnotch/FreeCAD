# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PathEdit.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QToolButton, QVBoxLayout, QWidget)
import resource_rc
import Material_rc
import Material_rc
import Path_rc

class Ui_pathEdit(object):
    def setupUi(self, pathEdit):
        if not pathEdit.objectName():
            pathEdit.setObjectName(u"pathEdit")
        pathEdit.resize(737, 809)
        self.tabGeneral = QWidget()
        self.tabGeneral.setObjectName(u"tabGeneral")
        self.verticalLayout_12 = QVBoxLayout(self.tabGeneral)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.jobBox = QToolBox(self.tabGeneral)
        self.jobBox.setObjectName(u"jobBox")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 707, 648))
        self.verticalLayout_17 = QVBoxLayout(self.page_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.groupBox_6 = QGroupBox(self.page_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.jobLabel = QLineEdit(self.groupBox_6)
        self.jobLabel.setObjectName(u"jobLabel")

        self.verticalLayout_16.addWidget(self.jobLabel)


        self.verticalLayout_17.addWidget(self.groupBox_6)

        self.groupBox_4 = QGroupBox(self.page_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.jobModel = QListWidget(self.groupBox_4)
        self.jobModel.setObjectName(u"jobModel")
        self.jobModel.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_14.addWidget(self.jobModel)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(334, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.jobModelEdit = QPushButton(self.groupBox_4)
        self.jobModelEdit.setObjectName(u"jobModelEdit")

        self.horizontalLayout_6.addWidget(self.jobModelEdit)


        self.verticalLayout_14.addLayout(self.horizontalLayout_6)


        self.verticalLayout_17.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.page_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.jobDescription = QPlainTextEdit(self.groupBox_5)
        self.jobDescription.setObjectName(u"jobDescription")

        self.verticalLayout_15.addWidget(self.jobDescription)


        self.verticalLayout_17.addWidget(self.groupBox_5)

        self.jobBox.addItem(self.page_5, u"Job")
        self.templateExport = QWidget()
        self.templateExport.setObjectName(u"templateExport")
        self.templateExport.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_13 = QVBoxLayout(self.templateExport)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.jobBox.addItem(self.templateExport, u"Template Export")

        self.verticalLayout_12.addWidget(self.jobBox)

        pathEdit.addTab(self.tabGeneral, "")
        self.tabOutput = QWidget()
        self.tabOutput.setObjectName(u"tabOutput")
        self.gridLayout = QGridLayout(self.tabOutput)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(self.tabOutput)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.postProcessorOutputFile = QLineEdit(self.tabOutput)
        self.postProcessorOutputFile.setObjectName(u"postProcessorOutputFile")

        self.gridLayout.addWidget(self.postProcessorOutputFile, 0, 1, 1, 1)

        self.postProcessorSetOutputFile = QToolButton(self.tabOutput)
        self.postProcessorSetOutputFile.setObjectName(u"postProcessorSetOutputFile")
        self.postProcessorSetOutputFile.setText(u"...")

        self.gridLayout.addWidget(self.postProcessorSetOutputFile, 0, 2, 1, 1)

        self.label_10 = QLabel(self.tabOutput)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.postProcessor = QComboBox(self.tabOutput)
        self.postProcessor.setObjectName(u"postProcessor")

        self.gridLayout.addWidget(self.postProcessor, 1, 1, 1, 2)

        self.label_11 = QLabel(self.tabOutput)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.postProcessorArguments = QLineEdit(self.tabOutput)
        self.postProcessorArguments.setObjectName(u"postProcessorArguments")

        self.gridLayout.addWidget(self.postProcessorArguments, 2, 1, 1, 2)

        self.groupBox_7 = QGroupBox(self.tabOutput)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.formLayout_4 = QFormLayout(self.groupBox_7)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.orderBy = QComboBox(self.groupBox_7)
        self.orderBy.setObjectName(u"orderBy")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.orderBy)

        self.label = QLabel(self.groupBox_7)
        self.label.setObjectName(u"label")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.groupBox_7)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.wcslist = QListWidget(self.groupBox_7)
        __qlistwidgetitem = QListWidgetItem(self.wcslist)
        __qlistwidgetitem.setText(u"G54");
        __qlistwidgetitem.setCheckState(Qt.Unchecked);
        __qlistwidgetitem1 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem1.setText(u"G55");
        __qlistwidgetitem1.setCheckState(Qt.Unchecked);
        __qlistwidgetitem2 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem2.setText(u"G56");
        __qlistwidgetitem2.setCheckState(Qt.Unchecked);
        __qlistwidgetitem3 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem3.setText(u"G57");
        __qlistwidgetitem3.setCheckState(Qt.Unchecked);
        __qlistwidgetitem4 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem4.setText(u"G58");
        __qlistwidgetitem4.setCheckState(Qt.Unchecked);
        __qlistwidgetitem5 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem5.setText(u"G59");
        __qlistwidgetitem5.setCheckState(Qt.Unchecked);
        __qlistwidgetitem6 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem6.setText(u"G59.1");
        __qlistwidgetitem6.setCheckState(Qt.Unchecked);
        __qlistwidgetitem7 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem7.setText(u"G59.2");
        __qlistwidgetitem7.setCheckState(Qt.Unchecked);
        __qlistwidgetitem8 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem8.setText(u"G59.3");
        __qlistwidgetitem8.setCheckState(Qt.Unchecked);
        __qlistwidgetitem9 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem9.setText(u"G59.4");
        __qlistwidgetitem9.setCheckState(Qt.Unchecked);
        __qlistwidgetitem10 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem10.setText(u"G59.5");
        __qlistwidgetitem10.setCheckState(Qt.Unchecked);
        __qlistwidgetitem11 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem11.setText(u"G59.6");
        __qlistwidgetitem11.setCheckState(Qt.Unchecked);
        __qlistwidgetitem12 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem12.setText(u"G59.7");
        __qlistwidgetitem12.setCheckState(Qt.Unchecked);
        __qlistwidgetitem13 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem13.setText(u"G59.8");
        __qlistwidgetitem13.setCheckState(Qt.Unchecked);
        __qlistwidgetitem14 = QListWidgetItem(self.wcslist)
        __qlistwidgetitem14.setText(u"G59.9");
        __qlistwidgetitem14.setCheckState(Qt.Unchecked);
        self.wcslist.setObjectName(u"wcslist")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wcslist.sizePolicy().hasHeightForWidth())
        self.wcslist.setSizePolicy(sizePolicy1)
        self.wcslist.setMinimumSize(QSize(0, 0))
        self.wcslist.setResizeMode(QListView.Adjust)
        self.wcslist.setSpacing(0)
        self.wcslist.setViewMode(QListView.IconMode)
        self.wcslist.setModelColumn(0)
        self.wcslist.setUniformItemSizes(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.wcslist)

        self.splitOutput = QCheckBox(self.groupBox_7)
        self.splitOutput.setObjectName(u"splitOutput")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.splitOutput)


        self.gridLayout.addWidget(self.groupBox_7, 4, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 747, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        pathEdit.addTab(self.tabOutput, "")
        self.tabSetup = QWidget()
        self.tabSetup.setObjectName(u"tabSetup")
        self.verticalLayout = QVBoxLayout(self.tabSetup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolBox_2 = QToolBox(self.tabSetup)
        self.toolBox_2.setObjectName(u"toolBox_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 688, 1368))
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.stockGroup = QGroupBox(self.page_3)
        self.stockGroup.setObjectName(u"stockGroup")
        self.verticalLayout_5 = QVBoxLayout(self.stockGroup)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.stock = QComboBox(self.stockGroup)
        self.stock.addItem("")
        self.stock.addItem("")
        self.stock.addItem("")
        self.stock.addItem("")
        self.stock.setObjectName(u"stock")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stock.sizePolicy().hasHeightForWidth())
        self.stock.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.stock)

        self.refreshStock = QPushButton(self.stockGroup)
        self.refreshStock.setObjectName(u"refreshStock")

        self.horizontalLayout_5.addWidget(self.refreshStock)

        self.btnMaterial = QPushButton(self.stockGroup)
        self.btnMaterial.setObjectName(u"btnMaterial")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnMaterial.sizePolicy().hasHeightForWidth())
        self.btnMaterial.setSizePolicy(sizePolicy3)
        icon = QIcon()
        icon.addFile(u":/icons/MaterialWorkbench.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMaterial.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btnMaterial)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer = QSpacerItem(40, 6, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer)

        self.stockFromExisting = QFrame(self.stockGroup)
        self.stockFromExisting.setObjectName(u"stockFromExisting")
        self.gridLayout_8 = QGridLayout(self.stockFromExisting)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.stockExisting = QComboBox(self.stockFromExisting)
        self.stockExisting.setObjectName(u"stockExisting")

        self.gridLayout_8.addWidget(self.stockExisting, 0, 1, 1, 1)

        self.comboBox = QComboBox(self.stockFromExisting)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_8.addWidget(self.comboBox, 1, 1, 1, 1)


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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stockExtXpos.sizePolicy().hasHeightForWidth())
        self.stockExtXpos.setSizePolicy(sizePolicy4)

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


        self.verticalLayout_9.addWidget(self.stockGroup)

        self.modelAlignGroup = QGroupBox(self.page_3)
        self.modelAlignGroup.setObjectName(u"modelAlignGroup")
        self.gridLayout_2 = QGridLayout(self.modelAlignGroup)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.moveToOrigin = QPushButton(self.modelAlignGroup)
        self.moveToOrigin.setObjectName(u"moveToOrigin")

        self.gridLayout_2.addWidget(self.moveToOrigin, 0, 0, 1, 1)

        self.setOrigin = QPushButton(self.modelAlignGroup)
        self.setOrigin.setObjectName(u"setOrigin")

        self.gridLayout_2.addWidget(self.setOrigin, 0, 1, 1, 1)

        self.centerInStock = QPushButton(self.modelAlignGroup)
        self.centerInStock.setObjectName(u"centerInStock")

        self.gridLayout_2.addWidget(self.centerInStock, 2, 0, 1, 1)

        self.centerInStockXY = QPushButton(self.modelAlignGroup)
        self.centerInStockXY.setObjectName(u"centerInStockXY")

        self.gridLayout_2.addWidget(self.centerInStockXY, 2, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.modelAlignGroup)

        self.modelSetGroup = QGroupBox(self.page_3)
        self.modelSetGroup.setObjectName(u"modelSetGroup")
        self.gridLayout_5 = QGridLayout(self.modelSetGroup)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.modelSetXAxis = QPushButton(self.modelSetGroup)
        self.modelSetXAxis.setObjectName(u"modelSetXAxis")

        self.gridLayout_5.addWidget(self.modelSetXAxis, 0, 0, 1, 1)

        self.modelSetYAxis = QPushButton(self.modelSetGroup)
        self.modelSetYAxis.setObjectName(u"modelSetYAxis")

        self.gridLayout_5.addWidget(self.modelSetYAxis, 0, 1, 1, 1)

        self.modelSetZAxis = QPushButton(self.modelSetGroup)
        self.modelSetZAxis.setObjectName(u"modelSetZAxis")

        self.gridLayout_5.addWidget(self.modelSetZAxis, 0, 2, 1, 1)

        self.modelSetX0 = QPushButton(self.modelSetGroup)
        self.modelSetX0.setObjectName(u"modelSetX0")

        self.gridLayout_5.addWidget(self.modelSetX0, 1, 0, 1, 1)

        self.modelSetY0 = QPushButton(self.modelSetGroup)
        self.modelSetY0.setObjectName(u"modelSetY0")

        self.gridLayout_5.addWidget(self.modelSetY0, 1, 1, 1, 1)

        self.modelSetZ0 = QPushButton(self.modelSetGroup)
        self.modelSetZ0.setObjectName(u"modelSetZ0")

        self.gridLayout_5.addWidget(self.modelSetZ0, 1, 2, 1, 1)

        self.linkStockAndModel = QCheckBox(self.modelSetGroup)
        self.linkStockAndModel.setObjectName(u"linkStockAndModel")

        self.gridLayout_5.addWidget(self.linkStockAndModel, 2, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.modelSetGroup)

        self.modelMoveGroup = QGroupBox(self.page_3)
        self.modelMoveGroup.setObjectName(u"modelMoveGroup")
        self.gridLayout_3 = QGridLayout(self.modelMoveGroup)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.modelMoveLeftUp = QPushButton(self.modelMoveGroup)
        self.modelMoveLeftUp.setObjectName(u"modelMoveLeftUp")
        icon1 = QIcon()
        icon1.addFile(u":/icons/arrow-left-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modelMoveLeftUp.setIcon(icon1)
        self.modelMoveLeftUp.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.modelMoveLeftUp, 0, 0, 1, 1)

        self.modelMoveUp = QPushButton(self.modelMoveGroup)
        self.modelMoveUp.setObjectName(u"modelMoveUp")
        icon2 = QIcon()
        icon2.addFile(u":/icons/arrow-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modelMoveUp.setIcon(icon2)
        self.modelMoveUp.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.modelMoveUp, 0, 1, 1, 1)

        self.modelMoveRightUp = QPushButton(self.modelMoveGroup)
        self.modelMoveRightUp.setObjectName(u"modelMoveRightUp")
        icon3 = QIcon()
        icon3.addFile(u":/icons/arrow-right-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modelMoveRightUp.setIcon(icon3)
        self.modelMoveRightUp.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.modelMoveRightUp, 0, 2, 1, 1)

        self.modelMoveLeft = QPushButton(self.modelMoveGroup)
        self.modelMoveLeft.setObjectName(u"modelMoveLeft")
        icon4 = QIcon()
        icon4.addFile(u":/icons/arrow-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modelMoveLeft.setIcon(icon4)
        self.modelMoveLeft.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.modelMoveLeft, 1, 0, 1, 1)

        self.modelMoveValue = QDoubleSpinBox(self.modelMoveGroup)
        self.modelMoveValue.setObjectName(u"modelMoveValue")
        self.modelMoveValue.setMinimum(-1000.000000000000000)
        self.modelMoveValue.setMaximum(1000.000000000000000)
        self.modelMoveValue.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.modelMoveValue, 1, 1, 1, 1)

        self.modelMoveRight = QPushButton(self.modelMoveGroup)
        self.modelMoveRight.setObjectName(u"modelMoveRight")
        icon5 = QIcon()
        icon5.addFile(u":/icons/arrow-right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modelMoveRight.setIcon(icon5)
        self.modelMoveRight.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.modelMoveRight, 1, 2, 1, 1)

        self.modelMoveLeftDown = QPushButton(self.modelMoveGroup)
        self.modelMoveLeftDown.setObjectName(u"modelMoveLeftDown")
        icon6 = QIcon()
        icon6.addFile(u":/icons/arrow-left-down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modelMoveLeftDown.setIcon(icon6)
        self.modelMoveLeftDown.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.modelMoveLeftDown, 2, 0, 1, 1)

        self.modelMoveDown = QPushButton(self.modelMoveGroup)
        self.modelMoveDown.setObjectName(u"modelMoveDown")
        icon7 = QIcon()
        icon7.addFile(u":/icons/arrow-down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modelMoveDown.setIcon(icon7)
        self.modelMoveDown.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.modelMoveDown, 2, 1, 1, 1)

        self.modelMoveRightDown = QPushButton(self.modelMoveGroup)
        self.modelMoveRightDown.setObjectName(u"modelMoveRightDown")
        icon8 = QIcon()
        icon8.addFile(u":/icons/arrow-right-down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modelMoveRightDown.setIcon(icon8)
        self.modelMoveRightDown.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.modelMoveRightDown, 2, 2, 1, 1)


        self.verticalLayout_9.addWidget(self.modelMoveGroup)

        self.modelRotateGroup = QGroupBox(self.page_3)
        self.modelRotateGroup.setObjectName(u"modelRotateGroup")
        self.gridLayout_6 = QGridLayout(self.modelRotateGroup)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.modelRotateLeft = QPushButton(self.modelRotateGroup)
        self.modelRotateLeft.setObjectName(u"modelRotateLeft")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.modelRotateLeft.sizePolicy().hasHeightForWidth())
        self.modelRotateLeft.setSizePolicy(sizePolicy5)
        icon9 = QIcon()
        icon9.addFile(u":/icons/arrow-ccw.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modelRotateLeft.setIcon(icon9)
        self.modelRotateLeft.setIconSize(QSize(32, 32))

        self.gridLayout_6.addWidget(self.modelRotateLeft, 0, 0, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.modelRotateValue = QDoubleSpinBox(self.modelRotateGroup)
        self.modelRotateValue.setObjectName(u"modelRotateValue")
        self.modelRotateValue.setMinimum(-180.000000000000000)
        self.modelRotateValue.setMaximum(360.000000000000000)
        self.modelRotateValue.setValue(90.000000000000000)

        self.verticalLayout_18.addWidget(self.modelRotateValue)

        self.modelRotateCompound = QCheckBox(self.modelRotateGroup)
        self.modelRotateCompound.setObjectName(u"modelRotateCompound")
        self.modelRotateCompound.setChecked(True)

        self.verticalLayout_18.addWidget(self.modelRotateCompound)


        self.gridLayout_6.addLayout(self.verticalLayout_18, 0, 1, 1, 1)

        self.modelRotateRight = QPushButton(self.modelRotateGroup)
        self.modelRotateRight.setObjectName(u"modelRotateRight")
        sizePolicy5.setHeightForWidth(self.modelRotateRight.sizePolicy().hasHeightForWidth())
        self.modelRotateRight.setSizePolicy(sizePolicy5)
        icon10 = QIcon()
        icon10.addFile(u":/icons/arrow-cw.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.modelRotateRight.setIcon(icon10)
        self.modelRotateRight.setIconSize(QSize(32, 32))

        self.gridLayout_6.addWidget(self.modelRotateRight, 0, 2, 1, 1)


        self.verticalLayout_9.addWidget(self.modelRotateGroup)

        self.verticalSpacer_2 = QSpacerItem(20, 195, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.toolBox_2.addItem(self.page_3, u"Layout")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 707, 648))
        self.gridLayout_13 = QGridLayout(self.page_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupBox = QGroupBox(self.page_4)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.setupStartDepthExpr = QLineEdit(self.groupBox)
        self.setupStartDepthExpr.setObjectName(u"setupStartDepthExpr")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.setupStartDepthExpr)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.setupFinalDepthExpr = QLineEdit(self.groupBox)
        self.setupFinalDepthExpr.setObjectName(u"setupFinalDepthExpr")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.setupFinalDepthExpr)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.setupStepDownExpr = QLineEdit(self.groupBox)
        self.setupStepDownExpr.setObjectName(u"setupStepDownExpr")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.setupStepDownExpr)


        self.gridLayout_13.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.page_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_15, 0, 1, 1, 2)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_14, 0, 3, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)

        self.setupClearanceHeightExpr = QLineEdit(self.groupBox_2)
        self.setupClearanceHeightExpr.setObjectName(u"setupClearanceHeightExpr")

        self.gridLayout_4.addWidget(self.setupClearanceHeightExpr, 1, 1, 1, 2)

        self.setupClearanceHeightOffs = Gui_QuantitySpinBox(self.groupBox_2)
        self.setupClearanceHeightOffs.setObjectName(u"setupClearanceHeightOffs")

        self.gridLayout_4.addWidget(self.setupClearanceHeightOffs, 1, 3, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 3, 0, 1, 1)

        self.setupSafeHeightExpr = QLineEdit(self.groupBox_2)
        self.setupSafeHeightExpr.setObjectName(u"setupSafeHeightExpr")

        self.gridLayout_4.addWidget(self.setupSafeHeightExpr, 3, 1, 1, 2)

        self.setupSafeHeightOffs = Gui_QuantitySpinBox(self.groupBox_2)
        self.setupSafeHeightOffs.setObjectName(u"setupSafeHeightOffs")

        self.gridLayout_4.addWidget(self.setupSafeHeightOffs, 3, 3, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.page_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_12 = QGridLayout(self.groupBox_8)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_17 = QLabel(self.groupBox_8)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_12.addWidget(self.label_17, 0, 0, 1, 1)

        self.setupCoolantMode = QComboBox(self.groupBox_8)
        self.setupCoolantMode.setObjectName(u"setupCoolantMode")

        self.gridLayout_12.addWidget(self.setupCoolantMode, 0, 1, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_8, 2, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_5, 3, 0, 1, 1)

        self.toolBox_2.addItem(self.page_4, u"Default Values")

        self.verticalLayout.addWidget(self.toolBox_2)

        pathEdit.addTab(self.tabSetup, "")
        self.tabTools = QWidget()
        self.tabTools.setObjectName(u"tabTools")
        self.verticalLayout_3 = QVBoxLayout(self.tabTools)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.tabTools)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 707, 648))
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.toolControllerList = QTableWidget(self.frame_2)
        if (self.toolControllerList.columnCount() < 5):
            self.toolControllerList.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.toolControllerList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.toolControllerList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon11 = QIcon()
        iconThemeName = u"object-flip-horizontal"
        if QIcon.hasThemeIcon(iconThemeName):
            icon11 = QIcon.fromTheme(iconThemeName)
        else:
            icon11.addFile(u"../../../../../../../../../../../../../../../../../../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setIcon(icon11);
        self.toolControllerList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon12 = QIcon()
        iconThemeName = u"object-flip-vertical"
        if QIcon.hasThemeIcon(iconThemeName):
            icon12 = QIcon.fromTheme(iconThemeName)
        else:
            icon12.addFile(u"../../../../../../../../../../../../../../../../../../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setIcon(icon12);
        self.toolControllerList.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.toolControllerList.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.toolControllerList.setObjectName(u"toolControllerList")
        self.toolControllerList.verticalHeader().setVisible(False)

        self.verticalLayout_6.addWidget(self.toolControllerList)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.toolControllerEdit = QPushButton(self.frame_2)
        self.toolControllerEdit.setObjectName(u"toolControllerEdit")
        self.toolControllerEdit.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.toolControllerEdit)

        self.toolControllerAdd = QPushButton(self.frame_2)
        self.toolControllerAdd.setObjectName(u"toolControllerAdd")

        self.horizontalLayout_2.addWidget(self.toolControllerAdd)

        self.toolControllerDelete = QPushButton(self.frame_2)
        self.toolControllerDelete.setObjectName(u"toolControllerDelete")
        self.toolControllerDelete.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.toolControllerDelete)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.toolBox.addItem(self.page, u"Tools")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 512, 183))
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_3 = QGroupBox(self.page_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_2 = QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.setupRapidHorizontal = Gui_QuantitySpinBox(self.groupBox_3)
        self.setupRapidHorizontal.setObjectName(u"setupRapidHorizontal")
        sizePolicy2.setHeightForWidth(self.setupRapidHorizontal.sizePolicy().hasHeightForWidth())
        self.setupRapidHorizontal.setSizePolicy(sizePolicy2)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.setupRapidHorizontal)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.setupRapidVertical = Gui_QuantitySpinBox(self.groupBox_3)
        self.setupRapidVertical.setObjectName(u"setupRapidVertical")
        sizePolicy2.setHeightForWidth(self.setupRapidVertical.sizePolicy().hasHeightForWidth())
        self.setupRapidVertical.setSizePolicy(sizePolicy2)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.setupRapidVertical)


        self.verticalLayout_8.addWidget(self.groupBox_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.page_2, u"Default Values")

        self.verticalLayout_3.addWidget(self.toolBox)

        pathEdit.addTab(self.tabTools, "")
        self.tabWorkplan = QWidget()
        self.tabWorkplan.setObjectName(u"tabWorkplan")
        self.verticalLayout_4 = QVBoxLayout(self.tabWorkplan)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.activeToolGroup = QWidget(self.tabWorkplan)
        self.activeToolGroup.setObjectName(u"activeToolGroup")
        self.formLayout_3 = QFormLayout(self.activeToolGroup)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_18 = QLabel(self.activeToolGroup)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.activeToolController = QComboBox(self.activeToolGroup)
        self.activeToolController.setObjectName(u"activeToolController")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.activeToolController)


        self.verticalLayout_4.addWidget(self.activeToolGroup)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.operationsList = QListWidget(self.tabWorkplan)
        self.operationsList.setObjectName(u"operationsList")
        self.operationsList.setDragDropMode(QAbstractItemView.InternalMove)

        self.horizontalLayout_4.addWidget(self.operationsList)

        self.operationMove = QWidget(self.tabWorkplan)
        self.operationMove.setObjectName(u"operationMove")
        self.verticalLayout_2 = QVBoxLayout(self.operationMove)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.operationUp = QToolButton(self.operationMove)
        self.operationUp.setObjectName(u"operationUp")
        self.operationUp.setText(u"...")
        icon13 = QIcon()
        icon13.addFile(u":/icons/button_up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.operationUp.setIcon(icon13)

        self.verticalLayout_2.addWidget(self.operationUp)

        self.operationDown = QToolButton(self.operationMove)
        self.operationDown.setObjectName(u"operationDown")
        self.operationDown.setText(u"...")
        icon14 = QIcon()
        icon14.addFile(u":/icons/button_down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.operationDown.setIcon(icon14)

        self.verticalLayout_2.addWidget(self.operationDown)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)


        self.horizontalLayout_4.addWidget(self.operationMove)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.operationModify = QWidget(self.tabWorkplan)
        self.operationModify.setObjectName(u"operationModify")
        self.horizontalLayout_3 = QHBoxLayout(self.operationModify)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.operationEdit = QPushButton(self.operationModify)
        self.operationEdit.setObjectName(u"operationEdit")

        self.horizontalLayout_3.addWidget(self.operationEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.operationDelete = QPushButton(self.operationModify)
        self.operationDelete.setObjectName(u"operationDelete")

        self.horizontalLayout_3.addWidget(self.operationDelete)


        self.verticalLayout_4.addWidget(self.operationModify)

        pathEdit.addTab(self.tabWorkplan, "")
        self.tabOpDefaults = QWidget()
        self.tabOpDefaults.setObjectName(u"tabOpDefaults")
        self.verticalLayout_11 = QVBoxLayout(self.tabOpDefaults)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.opDefaultOp = QComboBox(self.tabOpDefaults)
        self.opDefaultOp.setObjectName(u"opDefaultOp")

        self.verticalLayout_11.addWidget(self.opDefaultOp)

        pathEdit.addTab(self.tabOpDefaults, "")
        QWidget.setTabOrder(self.postProcessorOutputFile, self.postProcessorSetOutputFile)
        QWidget.setTabOrder(self.postProcessorSetOutputFile, self.postProcessor)
        QWidget.setTabOrder(self.postProcessor, self.postProcessorArguments)
        QWidget.setTabOrder(self.postProcessorArguments, self.stock)
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
        QWidget.setTabOrder(self.stockBoxHeight, self.toolControllerEdit)
        QWidget.setTabOrder(self.toolControllerEdit, self.toolControllerAdd)
        QWidget.setTabOrder(self.toolControllerAdd, self.toolControllerDelete)
        QWidget.setTabOrder(self.toolControllerDelete, self.activeToolController)
        QWidget.setTabOrder(self.activeToolController, self.operationsList)
        QWidget.setTabOrder(self.operationsList, self.operationDelete)
        QWidget.setTabOrder(self.operationDelete, self.operationEdit)
        QWidget.setTabOrder(self.operationEdit, self.operationUp)
        QWidget.setTabOrder(self.operationUp, self.operationDown)

        self.retranslateUi(pathEdit)

        pathEdit.setCurrentIndex(2)
        self.jobBox.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(0)
        self.stock.setCurrentIndex(2)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(pathEdit)
    # setupUi

    def retranslateUi(self, pathEdit):
        pathEdit.setWindowTitle(QCoreApplication.translate("pathEdit", u"Job Edit", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("pathEdit", u"Label", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("pathEdit", u"Model", None))
        self.jobModelEdit.setText(QCoreApplication.translate("pathEdit", u"Edit", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("pathEdit", u"Description", None))
        self.jobBox.setItemText(self.jobBox.indexOf(self.page_5), QCoreApplication.translate("pathEdit", u"Job", None))
        self.jobBox.setItemText(self.jobBox.indexOf(self.templateExport), QCoreApplication.translate("pathEdit", u"Template Export", None))
        pathEdit.setTabText(pathEdit.indexOf(self.tabGeneral), QCoreApplication.translate("pathEdit", u"General", None))
        self.label_9.setText(QCoreApplication.translate("pathEdit", u"Output File", None))
#if QT_CONFIG(tooltip)
        self.postProcessorOutputFile.setToolTip(QCoreApplication.translate("pathEdit", u"Enter a path and optionally file name (see below) to be used as the default for the post processor export.\n"
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
"if %S is included, you can specify where the number occurs.  Without it, the number will be    added to the end of the string.\n"
"\n"
"%S ... Sequence Number\n"
"\n"
"The following example stores all files with the same name as the document in the directory /home/freecad (please r"
                        "emove quotes):\n"
"\"/home/cnc/%d.g-code\"\n"
"See the file save policy below on how to deal with name conflicts.", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("pathEdit", u"Processor", None))
        self.label_11.setText(QCoreApplication.translate("pathEdit", u"Arguments", None))
#if QT_CONFIG(tooltip)
        self.postProcessorArguments.setToolTip(QCoreApplication.translate("pathEdit", u"Optional arguments passed to the Post Processor. The arguments are specific for each Post Processor, please see its documentation for details.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_7.setTitle(QCoreApplication.translate("pathEdit", u"Work Coordinate Systems", None))
#if QT_CONFIG(tooltip)
        self.orderBy.setToolTip(QCoreApplication.translate("pathEdit", u"Ordering by Fixture, will cause all operations to be performed in the first coordinate system before switching to the second. Then all operations will be performed there in the same order.\n"
"\n"
"This is useful if the operator can safely load work into one coordinate system while the machine is doing work in another.\n"
"\n"
"Ordering by Tool, will minimize the Tool Changes. A tool change will be done, then all operations in all coordinate systems before changing tools.\n"
"\n"
"Ordering by operation will do each operation in all coordinate systems before moving to the next operation. This is especially useful in conjunction with the 'split output' even with only a single work coordinate system since it will put each operation into a separate file.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("pathEdit", u"Systems", None))
        self.label_2.setText(QCoreApplication.translate("pathEdit", u"Order By", None))

        __sortingEnabled = self.wcslist.isSortingEnabled()
        self.wcslist.setSortingEnabled(False)
        self.wcslist.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.wcslist.setToolTip(QCoreApplication.translate("pathEdit", u"<html><head/><body><p><span style=\" font-style:italic;\">Work Coordinate Systems</span> also called <span style=\" font-style:italic;\">Work Offsets</span>, <span style=\" font-style:italic;\">Fixture Offsets</span>, or <span style=\" font-style:italic;\">Fixtures </span>are useful for building efficient production jobs where the same part is done many times on the machine.\n"
"FreeCAD has no knowledge of where a particular coordinate system exists within the machine coordinate system so adding additional coordinate systems to your job will have no visual change within your job. It will, however, change your G-code output. The exact way in which the output is affected is controlled by the 'order by' setting.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.splitOutput.setToolTip(QCoreApplication.translate("pathEdit", u"If multiple coordinate systems are in use, setting this to TRUE will cause the G-code to be written to multiple output files as controlled by the 'order by' property. For example, if ordering by Fixture, the first output file will be for the first fixture and separate file for the second.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.splitOutput.setWhatsThis(QCoreApplication.translate("pathEdit", u"<html><head/><body><p>If True, post processing will create multiple output files based on the <span style=\" font-style:italic;\">order by</span> setting.\n"
"\n"
"\n"
"For example, if <span style=\" font-style:italic;\">order by</span> is set to Tool, the first output file will contain the first tool change and all operations, in all coordinate systems, that can be done with that tool before the next tool change is called.\n"
"\n"
"\n"
"If <span style=\" font-style:italic;\">order by</span> is set to <span style=\" font-style:italic;\">operation</span> and <span style=\" font-style:italic;\">split output</span> is true, each operation will be written to a separate file.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.splitOutput.setText(QCoreApplication.translate("pathEdit", u"Split Output", None))
        pathEdit.setTabText(pathEdit.indexOf(self.tabOutput), QCoreApplication.translate("pathEdit", u"Output", None))
        self.stockGroup.setTitle(QCoreApplication.translate("pathEdit", u"Stock", None))
        self.stock.setItemText(0, QCoreApplication.translate("pathEdit", u"Create Box", None))
        self.stock.setItemText(1, QCoreApplication.translate("pathEdit", u"Create Cylinder", None))
        self.stock.setItemText(2, QCoreApplication.translate("pathEdit", u"Extend Model's Bounding Box", None))
        self.stock.setItemText(3, QCoreApplication.translate("pathEdit", u"Use Existing Solid", None))

        self.refreshStock.setText(QCoreApplication.translate("pathEdit", u"Refresh", None))
#if QT_CONFIG(tooltip)
        self.btnMaterial.setToolTip(QCoreApplication.translate("pathEdit", u"Assign Stock Material", None))
#endif // QT_CONFIG(tooltip)
        self.btnMaterial.setText("")
        self.stockExtXLabel.setText(QCoreApplication.translate("pathEdit", u"Ext. X", None))
        self.stockExtYLabel.setText(QCoreApplication.translate("pathEdit", u"Ext. Y", None))
        self.stockExtZLabel.setText(QCoreApplication.translate("pathEdit", u"Ext. Z", None))
        self.stockCylinderRadiusLabel.setText(QCoreApplication.translate("pathEdit", u"Radius", None))
        self.stockCylinderHeightLabel.setText(QCoreApplication.translate("pathEdit", u"Height", None))
        self.stockBoxLengthLabel.setText(QCoreApplication.translate("pathEdit", u"Length", None))
        self.stockBoxWidthLabel.setText(QCoreApplication.translate("pathEdit", u"Width", None))
        self.stockBoxHeightLabel.setText(QCoreApplication.translate("pathEdit", u"Height", None))
        self.modelAlignGroup.setTitle(QCoreApplication.translate("pathEdit", u"Alignment", None))
        self.moveToOrigin.setText(QCoreApplication.translate("pathEdit", u"Move to Origin", None))
        self.setOrigin.setText(QCoreApplication.translate("pathEdit", u"Set Origin", None))
        self.centerInStock.setText(QCoreApplication.translate("pathEdit", u"Center in Stock", None))
        self.centerInStockXY.setText(QCoreApplication.translate("pathEdit", u"XY in Stock", None))
        self.modelSetGroup.setTitle(QCoreApplication.translate("pathEdit", u"Set", None))
        self.modelSetXAxis.setText(QCoreApplication.translate("pathEdit", u"X-Axis", None))
        self.modelSetYAxis.setText(QCoreApplication.translate("pathEdit", u"Y-Axis", None))
        self.modelSetZAxis.setText(QCoreApplication.translate("pathEdit", u"Z-Axis", None))
        self.modelSetX0.setText(QCoreApplication.translate("pathEdit", u"X=0", None))
        self.modelSetY0.setText(QCoreApplication.translate("pathEdit", u"Y=0", None))
        self.modelSetZ0.setText(QCoreApplication.translate("pathEdit", u"Z=0", None))
        self.linkStockAndModel.setText(QCoreApplication.translate("pathEdit", u"Link Stock and Model", None))
        self.modelMoveGroup.setTitle(QCoreApplication.translate("pathEdit", u"Move - XY", None))
        self.modelMoveLeftUp.setText("")
        self.modelMoveUp.setText("")
        self.modelMoveRightUp.setText("")
        self.modelMoveLeft.setText("")
        self.modelMoveRight.setText("")
        self.modelMoveLeftDown.setText("")
        self.modelMoveDown.setText("")
        self.modelMoveRightDown.setText("")
        self.modelRotateGroup.setTitle(QCoreApplication.translate("pathEdit", u"Rotate - XY", None))
        self.modelRotateLeft.setText("")
        self.modelRotateCompound.setText(QCoreApplication.translate("pathEdit", u"Compound", None))
        self.modelRotateRight.setText("")
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_3), QCoreApplication.translate("pathEdit", u"Layout", None))
        self.groupBox.setTitle(QCoreApplication.translate("pathEdit", u"Depths", None))
        self.label_3.setText(QCoreApplication.translate("pathEdit", u"Start Depth", None))
#if QT_CONFIG(tooltip)
        self.setupStartDepthExpr.setToolTip(QCoreApplication.translate("pathEdit", u"Expression set as the StartDepth of a newly created operation.\n"
"\n"
"Default: OpStartDepth", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("pathEdit", u"Final Depth", None))
#if QT_CONFIG(tooltip)
        self.setupFinalDepthExpr.setToolTip(QCoreApplication.translate("pathEdit", u"Expression set as the FinalDepth for a newly created operation.\n"
"\n"
"Default: OpFinalDepth", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("pathEdit", u"Step Down", None))
#if QT_CONFIG(tooltip)
        self.setupStepDownExpr.setToolTip(QCoreApplication.translate("pathEdit", u"Expression set as the StepDown of a newly created operation.\n"
"\n"
"Default: OpToolDiameter", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("pathEdit", u"Heights", None))
        self.label_15.setText(QCoreApplication.translate("pathEdit", u"Expression", None))
        self.label_14.setText(QCoreApplication.translate("pathEdit", u"Offset", None))
        self.label_13.setText(QCoreApplication.translate("pathEdit", u"Clearance", None))
#if QT_CONFIG(tooltip)
        self.setupClearanceHeightExpr.setToolTip(QCoreApplication.translate("pathEdit", u"Expression set as ClearanceHeight for new operations.\n"
"\n"
"Default: \"OpStockZMax+SetupSheet.ClearanceHeightOffset\"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.setupClearanceHeightOffs.setToolTip(QCoreApplication.translate("pathEdit", u"ClearanceHeightOffset - can be used by expressions to set the default ClearanceHeight for new operations.\n"
"\n"
"Default: 3 mm", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("pathEdit", u"Safe", None))
#if QT_CONFIG(tooltip)
        self.setupSafeHeightExpr.setToolTip(QCoreApplication.translate("pathEdit", u"Expression set as SafeHeight for new operations.\n"
"\n"
"Default: \"OpStockZMax+SetupSheet.SafeHeightOffset\"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.setupSafeHeightOffs.setToolTip(QCoreApplication.translate("pathEdit", u"SafeHeightOffset can be for expressions to set the SafeHeight for new operations.\n"
"\n"
"Default: \"5mm\"", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_8.setTitle(QCoreApplication.translate("pathEdit", u"Coolant", None))
        self.label_17.setText(QCoreApplication.translate("pathEdit", u"Coolant Mode", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_4), QCoreApplication.translate("pathEdit", u"Default Values", None))
        pathEdit.setTabText(pathEdit.indexOf(self.tabSetup), QCoreApplication.translate("pathEdit", u"Setup", None))
        ___qtablewidgetitem = self.toolControllerList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pathEdit", u"Name", None));
        ___qtablewidgetitem1 = self.toolControllerList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pathEdit", u"Nr.", None));
        ___qtablewidgetitem2 = self.toolControllerList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("pathEdit", u"Feed", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem2.setToolTip(QCoreApplication.translate("pathEdit", u"Horizontal Feed", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem3 = self.toolControllerList.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("pathEdit", u"Feed", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem3.setToolTip(QCoreApplication.translate("pathEdit", u"Vertical Feed", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem4 = self.toolControllerList.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("pathEdit", u"Spindle", None));
        self.toolControllerEdit.setText(QCoreApplication.translate("pathEdit", u"Edit", None))
        self.toolControllerAdd.setText(QCoreApplication.translate("pathEdit", u"Add", None))
        self.toolControllerDelete.setText(QCoreApplication.translate("pathEdit", u"Remove", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("pathEdit", u"Tools", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("pathEdit", u"Rapid Speeds", None))
        self.label_8.setText(QCoreApplication.translate("pathEdit", u"Horizontal", None))
#if QT_CONFIG(tooltip)
        self.setupRapidHorizontal.setToolTip(QCoreApplication.translate("pathEdit", u"Rapid horizontal speed assigned as HorizRapid to new ToolController.", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("pathEdit", u"Vertical", None))
#if QT_CONFIG(tooltip)
        self.setupRapidVertical.setToolTip(QCoreApplication.translate("pathEdit", u"Rapid vertical speed assigned to VertRapid of new ToolController.", None))
#endif // QT_CONFIG(tooltip)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("pathEdit", u"Default Values", None))
        pathEdit.setTabText(pathEdit.indexOf(self.tabTools), QCoreApplication.translate("pathEdit", u"Tools", None))
        self.label_18.setText(QCoreApplication.translate("pathEdit", u"Active Tool", None))
        self.operationEdit.setText(QCoreApplication.translate("pathEdit", u"Edit", None))
        self.operationDelete.setText(QCoreApplication.translate("pathEdit", u"Delete", None))
        pathEdit.setTabText(pathEdit.indexOf(self.tabWorkplan), QCoreApplication.translate("pathEdit", u"Workplan", None))
        pathEdit.setTabText(pathEdit.indexOf(self.tabOpDefaults), QCoreApplication.translate("pathEdit", u"Op Defaults", None))
    # retranslateUi

