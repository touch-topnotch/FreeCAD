# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-sh3d-import.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsArch(object):
    def setupUi(self, Gui__Dialog__DlgSettingsArch):
        if not Gui__Dialog__DlgSettingsArch.objectName():
            Gui__Dialog__DlgSettingsArch.setObjectName(u"Gui__Dialog__DlgSettingsArch")
        Gui__Dialog__DlgSettingsArch.resize(555, 729)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsArch)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(9, 9, 9, 9)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.groupBox_3 = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_1 = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setProperty(u"prefEntry", u"sh3dShowDialog")
        self.checkBox_1.setProperty(u"prefPath", u"Mod/Arch")
        self.checkBox_1.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox_1)

        self.checkBox_debugGeometry = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBox_debugGeometry.setObjectName(u"checkBox_debugGeometry")
        self.checkBox_debugGeometry.setProperty(u"prefEntry", u"sh3dDebugGeometry")
        self.checkBox_debugGeometry.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout_3.addWidget(self.checkBox_debugGeometry)


        self.vboxLayout.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_9 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setProperty(u"prefEntry", u"sh3dMerge")
        self.checkBox_9.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_9)

        self.checkBox_3 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setProperty(u"prefEntry", u"sh3dImportDoorsAndWindows")
        self.checkBox_3.setProperty(u"prefPath", u"Mod/Arch")
        self.checkBox_3.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_4 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setProperty(u"prefEntry", u"sh3dImportFurnitures")
        self.checkBox_4.setProperty(u"prefPath", u"Mod/Arch")
        self.checkBox_4.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_4)

        self.checkBox_5 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setProperty(u"prefEntry", u"sh3dCreateArchEquipment")
        self.checkBox_5.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_5)

        self.checkBox_6 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setProperty(u"prefEntry", u"sh3dJoinArchWall")
        self.checkBox_6.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_6)

        self.checkBox_7 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setProperty(u"prefEntry", u"sh3dImportLights")
        self.checkBox_7.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_7)

        self.checkBox_8 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setProperty(u"prefEntry", u"sh3dImportCameras")
        self.checkBox_8.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_8)

        self.checkBox_10 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setProperty(u"prefEntry", u"sh3dCreateRenderProject")
        self.checkBox_10.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_10)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label1 = QLabel(self.groupBox_2)
        self.label1.setObjectName(u"label1")

        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)

        self.ArchSH3DDefaultFloorColor = Gui_PrefColorButton(self.groupBox_2)
        self.ArchSH3DDefaultFloorColor.setObjectName(u"ArchSH3DDefaultFloorColor")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ArchSH3DDefaultFloorColor.sizePolicy().hasHeightForWidth())
        self.ArchSH3DDefaultFloorColor.setSizePolicy(sizePolicy)
        self.ArchSH3DDefaultFloorColor.setProperty(u"color", QColor(168, 168, 168))
        self.ArchSH3DDefaultFloorColor.setProperty(u"prefEntry", u"sh3dDefaultFloorColor")
        self.ArchSH3DDefaultFloorColor.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout.addWidget(self.ArchSH3DDefaultFloorColor, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout1 = QGridLayout()
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.label11 = QLabel(self.groupBox_2)
        self.label11.setObjectName(u"label11")

        self.gridLayout1.addWidget(self.label11, 0, 0, 1, 1)

        self.ArchSH3DDefaultCeilingColor = Gui_PrefColorButton(self.groupBox_2)
        self.ArchSH3DDefaultCeilingColor.setObjectName(u"ArchSH3DDefaultCeilingColor")
        sizePolicy.setHeightForWidth(self.ArchSH3DDefaultCeilingColor.sizePolicy().hasHeightForWidth())
        self.ArchSH3DDefaultCeilingColor.setSizePolicy(sizePolicy)
        self.ArchSH3DDefaultCeilingColor.setProperty(u"color", QColor(246, 246, 246))
        self.ArchSH3DDefaultCeilingColor.setProperty(u"prefEntry", u"sh3dDefaultCeilingColor")
        self.ArchSH3DDefaultCeilingColor.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout1.addWidget(self.ArchSH3DDefaultCeilingColor, 0, 1, 1, 1)

        self.gridLayout1.setColumnStretch(0, 2)
        self.gridLayout1.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout1)

        self.checkBox_12 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setProperty(u"prefEntry", u"sh3dCreateIFCProject")
        self.checkBox_12.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_12)

        self.checkBox_13 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setProperty(u"prefEntry", u"sh3dCreateGroundMesh")
        self.checkBox_13.setProperty(u"prefPath", u"Mod/Arch")
        self.checkBox_13.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_13)

        self.gridLayout2 = QGridLayout()
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.label12 = QLabel(self.groupBox_2)
        self.label12.setObjectName(u"label12")

        self.gridLayout2.addWidget(self.label12, 0, 0, 1, 1)

        self.ArchSH3DDefaultGroundColor = Gui_PrefColorButton(self.groupBox_2)
        self.ArchSH3DDefaultGroundColor.setObjectName(u"ArchSH3DDefaultGroundColor")
        sizePolicy.setHeightForWidth(self.ArchSH3DDefaultGroundColor.sizePolicy().hasHeightForWidth())
        self.ArchSH3DDefaultGroundColor.setSizePolicy(sizePolicy)
        self.ArchSH3DDefaultGroundColor.setProperty(u"color", QColor(230, 230, 230))
        self.ArchSH3DDefaultGroundColor.setProperty(u"prefEntry", u"sh3dDefaultGroundColor")
        self.ArchSH3DDefaultGroundColor.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout2.addWidget(self.ArchSH3DDefaultGroundColor, 0, 1, 1, 1)

        self.gridLayout2.setColumnStretch(0, 2)
        self.gridLayout2.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout2)

        self.gridLayout3 = QGridLayout()
        self.gridLayout3.setSpacing(6)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.label13 = QLabel(self.groupBox_2)
        self.label13.setObjectName(u"label13")

        self.gridLayout3.addWidget(self.label13, 0, 0, 1, 1)

        self.ArchSH3DDefaultSkyColor = Gui_PrefColorButton(self.groupBox_2)
        self.ArchSH3DDefaultSkyColor.setObjectName(u"ArchSH3DDefaultSkyColor")
        sizePolicy.setHeightForWidth(self.ArchSH3DDefaultSkyColor.sizePolicy().hasHeightForWidth())
        self.ArchSH3DDefaultSkyColor.setSizePolicy(sizePolicy)
        self.ArchSH3DDefaultSkyColor.setProperty(u"color", QColor(204, 228, 252))
        self.ArchSH3DDefaultSkyColor.setProperty(u"prefEntry", u"sh3dDefaultSkyColor")
        self.ArchSH3DDefaultSkyColor.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout3.addWidget(self.ArchSH3DDefaultSkyColor, 0, 1, 1, 1)

        self.gridLayout3.setColumnStretch(0, 2)
        self.gridLayout3.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout3)

        self.checkBox_decorate_surfaces = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_decorate_surfaces.setObjectName(u"checkBox_decorate_surfaces")
        self.checkBox_decorate_surfaces.setProperty(u"prefEntry", u"sh3dDecorateSurfaces")
        self.checkBox_decorate_surfaces.setProperty(u"prefPath", u"Mod/Arch")
        self.checkBox_decorate_surfaces.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_decorate_surfaces)

        self.gridLayout4 = QGridLayout()
        self.gridLayout4.setSpacing(6)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.label14 = QLabel(self.groupBox_2)
        self.label14.setObjectName(u"label14")

        self.gridLayout4.addWidget(self.label14, 0, 0, 1, 1)

        self.ArchSH3DDefaultFurnitureColor = Gui_PrefColorButton(self.groupBox_2)
        self.ArchSH3DDefaultFurnitureColor.setObjectName(u"ArchSH3DDefaultFurnitureColor")
        sizePolicy.setHeightForWidth(self.ArchSH3DDefaultFurnitureColor.sizePolicy().hasHeightForWidth())
        self.ArchSH3DDefaultFurnitureColor.setSizePolicy(sizePolicy)
        self.ArchSH3DDefaultFurnitureColor.setProperty(u"color", QColor(168, 150, 26))
        self.ArchSH3DDefaultFurnitureColor.setProperty(u"prefEntry", u"sh3dDefaultFurnitureColor")
        self.ArchSH3DDefaultFurnitureColor.setProperty(u"prefPath", u"Mod/Arch")

        self.gridLayout4.addWidget(self.ArchSH3DDefaultFurnitureColor, 0, 1, 1, 1)

        self.gridLayout4.setColumnStretch(0, 2)
        self.gridLayout4.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout4)

        self.checkBox_11 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setProperty(u"prefEntry", u"sh3dFitView")
        self.checkBox_11.setProperty(u"prefPath", u"Mod/Arch")

        self.verticalLayout.addWidget(self.checkBox_11)


        self.vboxLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Gui__Dialog__DlgSettingsArch)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsArch)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsArch):
        Gui__Dialog__DlgSettingsArch.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"SH3D Import", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"General Options", None))
        self.checkBox_1.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Show this dialog when importing", None))
#if QT_CONFIG(tooltip)
        self.checkBox_debugGeometry.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"DEBUG: keep the construction geometries in the active document. Useful when debugging a failed import", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_debugGeometry.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Debug geometry", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Import Options", None))
#if QT_CONFIG(tooltip)
        self.checkBox_9.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Merge imported element with existing FreeCAD object", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_9.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Merge into existing document", None))
#if QT_CONFIG(tooltip)
        self.checkBox_3.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Whether to import the model's doors and windows", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Doors and Windows", None))
#if QT_CONFIG(tooltip)
        self.checkBox_4.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Whether to import the model's furnitures", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Furnitures", None))
#if QT_CONFIG(tooltip)
        self.checkBox_5.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Whether to create Arch::Equipment for each furniture defined in the model (NOTE: this can negatively impact the import process speed)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_5.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Create Arch::Equipment", None))
#if QT_CONFIG(tooltip)
        self.checkBox_6.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Whether to join the different Arch::Wall together", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_6.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Join Arch::Wall", None))
#if QT_CONFIG(tooltip)
        self.checkBox_7.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Whether to import the model's lights. Note that you also need to import\n"
"                    the model's furnitures.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_7.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Lights (requires Render)", None))
#if QT_CONFIG(tooltip)
        self.checkBox_8.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Whether to import the model's cameras", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_8.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Cameras (requires Render)", None))
#if QT_CONFIG(tooltip)
        self.checkBox_10.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Create a default Render project with the newly created site (requires the Render workbench to be installed)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_10.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Create render project", None))
        self.label1.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Default floor color", None))
#if QT_CONFIG(tooltip)
        self.ArchSH3DDefaultFloorColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"This color might be used when a room does not define its own color", None))
#endif // QT_CONFIG(tooltip)
        self.label11.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Default ceiling color", None))
#if QT_CONFIG(tooltip)
        self.ArchSH3DDefaultCeilingColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"This color might be used when a room does not define its own color", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_12.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Create a default IFC project with the newly created site", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_12.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Create IFC project", None))
#if QT_CONFIG(tooltip)
        self.checkBox_13.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Create a mesh to represent the default ground level", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_13.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Create ground level mesh", None))
        self.label12.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Default ground color", None))
#if QT_CONFIG(tooltip)
        self.ArchSH3DDefaultGroundColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"This color might be used when the environment does not define a color for the ground", None))
#endif // QT_CONFIG(tooltip)
        self.label13.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Default sky color", None))
#if QT_CONFIG(tooltip)
        self.ArchSH3DDefaultSkyColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"This color might be used when the environment does not define a color for the sky", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_decorate_surfaces.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Create face binders and baseboards for walls, and floors and ceilings for rooms", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_decorate_surfaces.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Decorate surfaces", None))
        self.label14.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Default furniture color", None))
#if QT_CONFIG(tooltip)
        self.ArchSH3DDefaultFurnitureColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"This color is used when a furniture does not define its own color", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_11.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Fit view while importing", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_11.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Fit view while importing", None))
    # retranslateUi

