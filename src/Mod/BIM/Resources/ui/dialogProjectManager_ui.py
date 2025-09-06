# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogProjectManager.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QDoubleSpinBox, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(443, 840)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.presets = QComboBox(Dialog)
        self.presets.addItem("")
        self.presets.setObjectName(u"presets")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.presets.sizePolicy().hasHeightForWidth())
        self.presets.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.presets)

        self.buttonSave = QPushButton(Dialog)
        self.buttonSave.setObjectName(u"buttonSave")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonSave.sizePolicy().hasHeightForWidth())
        self.buttonSave.setSizePolicy(sizePolicy1)
        icon = QIcon()
        iconThemeName = u"gtk-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../../../../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonSave.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.buttonSave)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -1041, 428, 1740))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupNewProject = QGroupBox(self.scrollAreaWidgetContents)
        self.groupNewProject.setObjectName(u"groupNewProject")
        self.groupNewProject.setCheckable(True)
        self.groupNewProject.setChecked(True)
        self.verticalLayout_4 = QVBoxLayout(self.groupNewProject)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.groupNewProject)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_8)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.radioNative1 = QRadioButton(self.groupNewProject)
        self.radioNative1.setObjectName(u"radioNative1")
        self.radioNative1.setChecked(False)

        self.verticalLayout_8.addWidget(self.radioNative1)

        self.radioNative2 = QRadioButton(self.groupNewProject)
        self.radioNative2.setObjectName(u"radioNative2")
        self.radioNative2.setChecked(True)

        self.verticalLayout_8.addWidget(self.radioNative2)

        self.radioNative3 = QRadioButton(self.groupNewProject)
        self.radioNative3.setObjectName(u"radioNative3")

        self.verticalLayout_8.addWidget(self.radioNative3)


        self.verticalLayout_4.addLayout(self.verticalLayout_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_18 = QLabel(self.groupNewProject)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_5.addWidget(self.label_18)

        self.projectName = QLineEdit(self.groupNewProject)
        self.projectName.setObjectName(u"projectName")

        self.horizontalLayout_5.addWidget(self.projectName)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.groupNewProject)

        self.groupSite = QGroupBox(self.scrollAreaWidgetContents)
        self.groupSite.setObjectName(u"groupSite")
        self.groupSite.setFlat(False)
        self.groupSite.setCheckable(True)
        self.verticalLayout_3 = QVBoxLayout(self.groupSite)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_19 = QLabel(self.groupSite)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_19)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.siteLongitude = QDoubleSpinBox(self.groupSite)
        self.siteLongitude.setObjectName(u"siteLongitude")
        self.siteLongitude.setDecimals(4)
        self.siteLongitude.setMinimum(-180.000000000000000)
        self.siteLongitude.setMaximum(180.000000000000000)

        self.gridLayout.addWidget(self.siteLongitude, 3, 1, 1, 1)

        self.label_6 = QLabel(self.groupSite)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_5 = QLabel(self.groupSite)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.siteName = QLineEdit(self.groupSite)
        self.siteName.setObjectName(u"siteName")

        self.gridLayout.addWidget(self.siteName, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupSite)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.siteDeviation = QDoubleSpinBox(self.groupSite)
        self.siteDeviation.setObjectName(u"siteDeviation")
        self.siteDeviation.setMaximum(359.990000000000009)

        self.gridLayout.addWidget(self.siteDeviation, 5, 1, 1, 1)

        self.label_3 = QLabel(self.groupSite)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.siteElevation = Gui_InputField(self.groupSite)
        self.siteElevation.setObjectName(u"siteElevation")
        self.siteElevation.setProperty(u"unit", u"")

        self.gridLayout.addWidget(self.siteElevation, 6, 1, 1, 1)

        self.siteAddress = QLineEdit(self.groupSite)
        self.siteAddress.setObjectName(u"siteAddress")

        self.gridLayout.addWidget(self.siteAddress, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupSite)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupSite)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.siteLatitude = QDoubleSpinBox(self.groupSite)
        self.siteLatitude.setObjectName(u"siteLatitude")
        self.siteLatitude.setDecimals(4)
        self.siteLatitude.setMinimum(-90.000000000000000)
        self.siteLatitude.setMaximum(90.000000000000000)

        self.gridLayout.addWidget(self.siteLatitude, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.groupSite)

        self.groupBuilding = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBuilding.setObjectName(u"groupBuilding")
        self.groupBuilding.setCheckable(True)
        self.verticalLayout_5 = QVBoxLayout(self.groupBuilding)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_15 = QLabel(self.groupBuilding)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_15)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_24 = QLabel(self.groupBuilding)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_4.addWidget(self.label_24, 4, 0, 1, 1)

        self.label_25 = QLabel(self.groupBuilding)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_4.addWidget(self.label_25, 5, 0, 1, 1)

        self.label_16 = QLabel(self.groupBuilding)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)

        self.buildingName = QLineEdit(self.groupBuilding)
        self.buildingName.setObjectName(u"buildingName")

        self.gridLayout_4.addWidget(self.buildingName, 0, 1, 1, 1)

        self.label_17 = QLabel(self.groupBuilding)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 9, 0, 1, 1)

        self.label_26 = QLabel(self.groupBuilding)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_4.addWidget(self.label_26, 10, 0, 1, 1)

        self.label_27 = QLabel(self.groupBuilding)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_4.addWidget(self.label_27, 7, 0, 1, 1)

        self.buildingUse = QComboBox(self.groupBuilding)
        self.buildingUse.setObjectName(u"buildingUse")
        self.buildingUse.setMaximumSize(QSize(16777215, 16777215))
        self.buildingUse.setMinimumContentsLength(0)

        self.gridLayout_4.addWidget(self.buildingUse, 3, 1, 1, 1)

        self.label_28 = QLabel(self.groupBuilding)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setWordWrap(False)

        self.gridLayout_4.addWidget(self.label_28, 8, 0, 1, 1)

        self.countVAxes = QSpinBox(self.groupBuilding)
        self.countVAxes.setObjectName(u"countVAxes")
        self.countVAxes.setValue(0)

        self.gridLayout_4.addWidget(self.countVAxes, 7, 1, 1, 1)

        self.label_29 = QLabel(self.groupBuilding)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_4.addWidget(self.label_29, 3, 0, 1, 1)

        self.countHAxes = QSpinBox(self.groupBuilding)
        self.countHAxes.setObjectName(u"countHAxes")
        self.countHAxes.setValue(0)

        self.gridLayout_4.addWidget(self.countHAxes, 9, 1, 1, 1)

        self.buildingWidth = Gui_InputField(self.groupBuilding)
        self.buildingWidth.setObjectName(u"buildingWidth")
        self.buildingWidth.setProperty(u"unit", u"")

        self.gridLayout_4.addWidget(self.buildingWidth, 5, 1, 1, 1)

        self.lineWidth = QSpinBox(self.groupBuilding)
        self.lineWidth.setObjectName(u"lineWidth")
        self.lineWidth.setValue(2)

        self.gridLayout_4.addWidget(self.lineWidth, 13, 1, 1, 1)

        self.distVAxes = Gui_InputField(self.groupBuilding)
        self.distVAxes.setObjectName(u"distVAxes")
        self.distVAxes.setProperty(u"unit", u"")

        self.gridLayout_4.addWidget(self.distVAxes, 8, 1, 1, 1)

        self.buildingLength = Gui_InputField(self.groupBuilding)
        self.buildingLength.setObjectName(u"buildingLength")
        self.buildingLength.setProperty(u"unit", u"")

        self.gridLayout_4.addWidget(self.buildingLength, 4, 1, 1, 1)

        self.distHAxes = Gui_InputField(self.groupBuilding)
        self.distHAxes.setObjectName(u"distHAxes")
        self.distHAxes.setProperty(u"unit", u"")

        self.gridLayout_4.addWidget(self.distHAxes, 10, 1, 1, 1)

        self.label_30 = QLabel(self.groupBuilding)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_4.addWidget(self.label_30, 13, 0, 1, 1)

        self.lineColor = Gui_ColorButton(self.groupBuilding)
        self.lineColor.setObjectName(u"lineColor")
        self.lineColor.setColor(QColor(33, 38, 94))

        self.gridLayout_4.addWidget(self.lineColor, 14, 1, 1, 1)

        self.label_31 = QLabel(self.groupBuilding)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_4.addWidget(self.label_31, 14, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)


        self.verticalLayout_2.addWidget(self.groupBuilding)

        self.addHumanFigure = QGroupBox(self.scrollAreaWidgetContents)
        self.addHumanFigure.setObjectName(u"addHumanFigure")
        self.addHumanFigure.setCheckable(True)
        self.verticalLayout_7 = QVBoxLayout(self.addHumanFigure)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(self.addHumanFigure)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_10)


        self.verticalLayout_2.addWidget(self.addHumanFigure)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_9)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.countLevels = QSpinBox(self.groupBox)
        self.countLevels.setObjectName(u"countLevels")
        self.countLevels.setSingleStep(1)
        self.countLevels.setValue(0)

        self.gridLayout_5.addWidget(self.countLevels, 0, 1, 1, 1)

        self.label_32 = QLabel(self.groupBox)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 1, 0, 1, 1)

        self.levelHeight = Gui_InputField(self.groupBox)
        self.levelHeight.setObjectName(u"levelHeight")
        self.levelHeight.setProperty(u"unit", u"")

        self.gridLayout_5.addWidget(self.levelHeight, 1, 1, 1, 1)

        self.label_33 = QLabel(self.groupBox)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_5.addWidget(self.label_33, 0, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_5)

        self.label_34 = QLabel(self.groupBox)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_34)

        self.groupsList = QListWidget(self.groupBox)
        self.groupsList.setObjectName(u"groupsList")
        self.groupsList.setDragEnabled(True)
        self.groupsList.setDragDropMode(QAbstractItemView.InternalMove)
        self.groupsList.setDefaultDropAction(Qt.MoveAction)

        self.verticalLayout_6.addWidget(self.groupsList)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonAdd = QPushButton(self.groupBox)
        self.buttonAdd.setObjectName(u"buttonAdd")
        icon1 = QIcon()
        iconThemeName = u"add"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"../../../../../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonAdd.setIcon(icon1)

        self.horizontalLayout.addWidget(self.buttonAdd)

        self.buttonDel = QPushButton(self.groupBox)
        self.buttonDel.setObjectName(u"buttonDel")
        icon2 = QIcon()
        iconThemeName = u"remove"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"../../../../../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonDel.setIcon(icon2)

        self.horizontalLayout.addWidget(self.buttonDel)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.buttonOK = QPushButton(Dialog)
        self.buttonOK.setObjectName(u"buttonOK")
        icon3 = QIcon()
        iconThemeName = u"gtk-ok"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u"../../../../../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonOK.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.buttonOK)

        self.buttonCancel = QPushButton(Dialog)
        self.buttonCancel.setObjectName(u"buttonCancel")
        icon4 = QIcon()
        iconThemeName = u"gtk-cancel"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u"../../../../../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonCancel.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.buttonCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"BIM Project Setup", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"This dialog assists in creating and configuring a new BIM project in FreeCAD", None))
        self.presets.setItemText(0, QCoreApplication.translate("Dialog", u"Use preset", None))

#if QT_CONFIG(tooltip)
        self.presets.setToolTip(QCoreApplication.translate("Dialog", u"Fill this dialog with preset values", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.buttonSave.setToolTip(QCoreApplication.translate("Dialog", u"The settings below can be saved as a preset. Presets are stored as .txt files in the local FreeCAD user folder", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSave.setText(QCoreApplication.translate("Dialog", u"Save Preset", None))
#if QT_CONFIG(tooltip)
        self.groupNewProject.setToolTip(QCoreApplication.translate("Dialog", u"Creates a new BIM project", None))
#endif // QT_CONFIG(tooltip)
        self.groupNewProject.setTitle(QCoreApplication.translate("Dialog", u"Create a New BIM Project", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"A new BIM project will be created, either as a new FreeCAD document or as a Native IFC project", None))
#if QT_CONFIG(tooltip)
        self.radioNative1.setToolTip(QCoreApplication.translate("Dialog", u"This will create a new FreeCAD document for the construction of a BIM model, but initially with no specific IFC structure. This is the most flexible option when starting working on a BIM project. This project can be converted to IFC anytime later.", None))
#endif // QT_CONFIG(tooltip)
        self.radioNative1.setText(QCoreApplication.translate("Dialog", u"Create a new document without IFC support", None))
#if QT_CONFIG(tooltip)
        self.radioNative2.setToolTip(QCoreApplication.translate("Dialog", u"This will create an IFC project. All the BIM objects added to the IFC project will immediately become IFC objects. This is less flexible, but helps to strictly adhere to the IFC standard.", None))
#endif // QT_CONFIG(tooltip)
        self.radioNative2.setText(QCoreApplication.translate("Dialog", u"Create a native IFC project in the current document", None))
#if QT_CONFIG(tooltip)
        self.radioNative3.setToolTip(QCoreApplication.translate("Dialog", u"The new IFC project will be created as a new FreeCAD document. In that mode, the IFC project is the FreeCAD document, anything created in that document becomes part of the IFC project. This is extremely restrictive as no non-IFC object can be added to the document.", None))
#endif // QT_CONFIG(tooltip)
        self.radioNative3.setText(QCoreApplication.translate("Dialog", u"Create a locked native IFC project as a new document", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Project name", None))
#if QT_CONFIG(tooltip)
        self.projectName.setToolTip(QCoreApplication.translate("Dialog", u"A name for this BIM or IFC project", None))
#endif // QT_CONFIG(tooltip)
        self.projectName.setText(QCoreApplication.translate("Dialog", u"Unnamed", None))
#if QT_CONFIG(tooltip)
        self.groupSite.setToolTip(QCoreApplication.translate("Dialog", u"Create a new site", None))
#endif // QT_CONFIG(tooltip)
        self.groupSite.setTitle(QCoreApplication.translate("Dialog", u"Create Site", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"The site object contains all the data relative to the project location. Later on, is it possible to attach a physical object representing the terrain.", None))
#if QT_CONFIG(tooltip)
        self.siteLongitude.setToolTip(QCoreApplication.translate("Dialog", u"The east longitude of this site", None))
#endif // QT_CONFIG(tooltip)
        self.siteLongitude.setSuffix(QCoreApplication.translate("Dialog", u" E", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Elevation", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Declination", None))
#if QT_CONFIG(tooltip)
        self.siteName.setToolTip(QCoreApplication.translate("Dialog", u"A name for this site", None))
#endif // QT_CONFIG(tooltip)
        self.siteName.setText(QCoreApplication.translate("Dialog", u"Default Site", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Name", None))
#if QT_CONFIG(tooltip)
        self.siteDeviation.setToolTip(QCoreApplication.translate("Dialog", u"The difference between the up direction of this site and the true north direction", None))
#endif // QT_CONFIG(tooltip)
        self.siteDeviation.setSuffix(QCoreApplication.translate("Dialog", u" \u00b0", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Longitude", None))
#if QT_CONFIG(tooltip)
        self.siteElevation.setToolTip(QCoreApplication.translate("Dialog", u"The elevation of this site", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.siteAddress.setToolTip(QCoreApplication.translate("Dialog", u"The physical (postal) address of this site", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Address", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Latitude", None))
#if QT_CONFIG(tooltip)
        self.siteLatitude.setToolTip(QCoreApplication.translate("Dialog", u"The north latitude of this site", None))
#endif // QT_CONFIG(tooltip)
        self.siteLatitude.setSuffix(QCoreApplication.translate("Dialog", u" N", None))
#if QT_CONFIG(tooltip)
        self.groupBuilding.setToolTip(QCoreApplication.translate("Dialog", u"Creates a new building", None))
#endif // QT_CONFIG(tooltip)
        self.groupBuilding.setTitle(QCoreApplication.translate("Dialog", u"Create Building", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"This will configure a single building for this project. If the project is made of several buildings, it can be duplicated after creation and its properties updated.", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Gross building length", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Gross building width", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.buildingName.setText(QCoreApplication.translate("Dialog", u"Default building", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Number of H axes", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Distance between H axes", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Number of V axes", None))
#if QT_CONFIG(tooltip)
        self.buildingUse.setToolTip(QCoreApplication.translate("Dialog", u"The primary function of this building", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText(QCoreApplication.translate("Dialog", u"Distance between V axes", None))
#if QT_CONFIG(tooltip)
        self.countVAxes.setToolTip(QCoreApplication.translate("Dialog", u"Number of vertical axes", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("Dialog", u"Primary function", None))
#if QT_CONFIG(tooltip)
        self.countHAxes.setToolTip(QCoreApplication.translate("Dialog", u"Number of horizontal axes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.buildingWidth.setToolTip(QCoreApplication.translate("Dialog", u"An estimate building width. Keep the value as 0 to not specify this now.", None))
#endif // QT_CONFIG(tooltip)
        self.buildingWidth.setText(QCoreApplication.translate("Dialog", u"0", None))
#if QT_CONFIG(tooltip)
        self.lineWidth.setToolTip(QCoreApplication.translate("Dialog", u"The line width of axes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.distVAxes.setToolTip(QCoreApplication.translate("Dialog", u"Distance between vertical axes", None))
#endif // QT_CONFIG(tooltip)
        self.distVAxes.setText(QCoreApplication.translate("Dialog", u"0", None))
#if QT_CONFIG(tooltip)
        self.buildingLength.setToolTip(QCoreApplication.translate("Dialog", u"An estimate building length. Keep the value as 0 to not specify this now.", None))
#endif // QT_CONFIG(tooltip)
        self.buildingLength.setText(QCoreApplication.translate("Dialog", u"0", None))
#if QT_CONFIG(tooltip)
        self.distHAxes.setToolTip(QCoreApplication.translate("Dialog", u"Distance between horizontal axes", None))
#endif // QT_CONFIG(tooltip)
        self.distHAxes.setText(QCoreApplication.translate("Dialog", u"0 ", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"Axes line width", None))
#if QT_CONFIG(tooltip)
        self.lineColor.setToolTip(QCoreApplication.translate("Dialog", u"The color of axes", None))
#endif // QT_CONFIG(tooltip)
        self.label_31.setText(QCoreApplication.translate("Dialog", u"Axes color", None))
#if QT_CONFIG(tooltip)
        self.addHumanFigure.setToolTip(QCoreApplication.translate("Dialog", u"Add a human figure to the document", None))
#endif // QT_CONFIG(tooltip)
        self.addHumanFigure.setTitle(QCoreApplication.translate("Dialog", u"Add Human Figure", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"A human figure will be added to the document, which helps give a sense of scale", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Levels", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"BIM projects are typically organized into levels that represent the different storeys of a building. Although it is not mandatory to work with levels in FreeCAD, the default levels can be set here.", None))
#if QT_CONFIG(tooltip)
        self.countLevels.setToolTip(QCoreApplication.translate("Dialog", u"The number of levels to create", None))
#endif // QT_CONFIG(tooltip)
        self.label_32.setText(QCoreApplication.translate("Dialog", u"Level height", None))
#if QT_CONFIG(tooltip)
        self.levelHeight.setToolTip(QCoreApplication.translate("Dialog", u"The vertical distance between each level", None))
#endif // QT_CONFIG(tooltip)
        self.levelHeight.setText(QCoreApplication.translate("Dialog", u"0 ", None))
        self.label_33.setText(QCoreApplication.translate("Dialog", u"Number of levels", None))
        self.label_34.setText(QCoreApplication.translate("Dialog", u"Default groups to be added to each level. Default groups such as walls and windows are useful to organize the different building elements inside a level.", None))
#if QT_CONFIG(tooltip)
        self.groupsList.setToolTip(QCoreApplication.translate("Dialog", u"A list of groups to add under each level", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.buttonAdd.setToolTip(QCoreApplication.translate("Dialog", u"Add New Group", None))
#endif // QT_CONFIG(tooltip)
        self.buttonAdd.setText(QCoreApplication.translate("Dialog", u"Add", None))
#if QT_CONFIG(tooltip)
        self.buttonDel.setToolTip(QCoreApplication.translate("Dialog", u"Delete a selected group", None))
#endif // QT_CONFIG(tooltip)
        self.buttonDel.setText(QCoreApplication.translate("Dialog", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.buttonOK.setToolTip(QCoreApplication.translate("Dialog", u"Accept the values of this form", None))
#endif // QT_CONFIG(tooltip)
        self.buttonOK.setText(QCoreApplication.translate("Dialog", u"OK", None))
#if QT_CONFIG(tooltip)
        self.buttonCancel.setToolTip(QCoreApplication.translate("Dialog", u"Cancel", None))
#endif // QT_CONFIG(tooltip)
        self.buttonCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

