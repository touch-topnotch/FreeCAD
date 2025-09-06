# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsMaterial.ui'
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

class Ui_MatGui_DlgSettingsMaterial(object):
    def setupUi(self, MatGui__DlgSettingsMaterial):
        if not MatGui__DlgSettingsMaterial.objectName():
            MatGui__DlgSettingsMaterial.setObjectName(u"MatGui__DlgSettingsMaterial")
        MatGui__DlgSettingsMaterial.resize(434, 553)
        self.verticalLayout = QVBoxLayout(MatGui__DlgSettingsMaterial)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gb_4_materials = QGroupBox(MatGui__DlgSettingsMaterial)
        self.gb_4_materials.setObjectName(u"gb_4_materials")
        self.verticalLayout_2 = QVBoxLayout(self.gb_4_materials)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.cb_use_built_in_materials = Gui_PrefCheckBox(self.gb_4_materials)
        self.cb_use_built_in_materials.setObjectName(u"cb_use_built_in_materials")
        self.cb_use_built_in_materials.setChecked(True)
        self.cb_use_built_in_materials.setProperty(u"prefEntry", u"UseBuiltInMaterials")
        self.cb_use_built_in_materials.setProperty(u"prefPath", u"Mod/Material/Resources")

        self.verticalLayout_6.addWidget(self.cb_use_built_in_materials)

        self.cb_use_mat_from_workbenches = Gui_PrefCheckBox(self.gb_4_materials)
        self.cb_use_mat_from_workbenches.setObjectName(u"cb_use_mat_from_workbenches")
        self.cb_use_mat_from_workbenches.setChecked(True)
        self.cb_use_mat_from_workbenches.setProperty(u"prefEntry", u"UseMaterialsFromWorkbenches")
        self.cb_use_mat_from_workbenches.setProperty(u"prefPath", u"Mod/Material/Resources")

        self.verticalLayout_6.addWidget(self.cb_use_mat_from_workbenches)

        self.cb_use_mat_from_config_dir = Gui_PrefCheckBox(self.gb_4_materials)
        self.cb_use_mat_from_config_dir.setObjectName(u"cb_use_mat_from_config_dir")
        self.cb_use_mat_from_config_dir.setChecked(True)
        self.cb_use_mat_from_config_dir.setProperty(u"prefEntry", u"UseMaterialsFromConfigDir")
        self.cb_use_mat_from_config_dir.setProperty(u"prefPath", u"Mod/Material/Resources")

        self.verticalLayout_6.addWidget(self.cb_use_mat_from_config_dir)

        self.cb_use_mat_from_custom_dir = Gui_PrefCheckBox(self.gb_4_materials)
        self.cb_use_mat_from_custom_dir.setObjectName(u"cb_use_mat_from_custom_dir")
        self.cb_use_mat_from_custom_dir.setChecked(True)
        self.cb_use_mat_from_custom_dir.setProperty(u"prefEntry", u"UseMaterialsFromCustomDir")
        self.cb_use_mat_from_custom_dir.setProperty(u"prefPath", u"Mod/Material/Resources")

        self.verticalLayout_6.addWidget(self.cb_use_mat_from_custom_dir)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.l_custom_mat_dir = QLabel(self.gb_4_materials)
        self.l_custom_mat_dir.setObjectName(u"l_custom_mat_dir")
        self.l_custom_mat_dir.setEnabled(True)
        self.l_custom_mat_dir.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.l_custom_mat_dir, 1, 0, 1, 1)

        self.fc_custom_mat_dir = Gui_PrefFileChooser(self.gb_4_materials)
        self.fc_custom_mat_dir.setObjectName(u"fc_custom_mat_dir")
        self.fc_custom_mat_dir.setEnabled(True)
        self.fc_custom_mat_dir.setMode(Gui.FileChooser.Directory)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_custom_mat_dir.sizePolicy().hasHeightForWidth())
        self.fc_custom_mat_dir.setSizePolicy(sizePolicy)
        self.fc_custom_mat_dir.setProperty(u"prefEntry", u"CustomMaterialsDir")
        self.fc_custom_mat_dir.setProperty(u"prefPath", u"Mod/Material/Resources")

        self.gridLayout.addWidget(self.fc_custom_mat_dir, 1, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout_6)


        self.verticalLayout.addWidget(self.gb_4_materials)

        self.gb_4_materials_2 = QGroupBox(MatGui__DlgSettingsMaterial)
        self.gb_4_materials_2.setObjectName(u"gb_4_materials_2")
        self.verticalLayout_3 = QVBoxLayout(self.gb_4_materials_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cb_delete_duplicates = Gui_PrefCheckBox(self.gb_4_materials_2)
        self.cb_delete_duplicates.setObjectName(u"cb_delete_duplicates")
        self.cb_delete_duplicates.setChecked(True)
        self.cb_delete_duplicates.setProperty(u"prefEntry", u"DeleteDuplicates")
        self.cb_delete_duplicates.setProperty(u"prefPath", u"Mod/Material/Cards")

        self.verticalLayout_3.addWidget(self.cb_delete_duplicates)

        self.cb_sort_by_resources = Gui_PrefCheckBox(self.gb_4_materials_2)
        self.cb_sort_by_resources.setObjectName(u"cb_sort_by_resources")
        self.cb_sort_by_resources.setChecked(True)
        self.cb_sort_by_resources.setProperty(u"prefEntry", u"SortByResources")
        self.cb_sort_by_resources.setProperty(u"prefPath", u"Mod/Material/Cards")

        self.verticalLayout_3.addWidget(self.cb_sort_by_resources)


        self.verticalLayout.addWidget(self.gb_4_materials_2)

        self.gbMaterialSelector = QGroupBox(MatGui__DlgSettingsMaterial)
        self.gbMaterialSelector.setObjectName(u"gbMaterialSelector")
        self.verticalLayout_5 = QVBoxLayout(self.gbMaterialSelector)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.cb_show_favorites = Gui_PrefCheckBox(self.gbMaterialSelector)
        self.cb_show_favorites.setObjectName(u"cb_show_favorites")
        self.cb_show_favorites.setChecked(True)
        self.cb_show_favorites.setProperty(u"prefEntry", u"ShowFavorites")
        self.cb_show_favorites.setProperty(u"prefPath", u"Mod/Material/TreeWidget")

        self.verticalLayout_5.addWidget(self.cb_show_favorites)

        self.cb_show_recent = Gui_PrefCheckBox(self.gbMaterialSelector)
        self.cb_show_recent.setObjectName(u"cb_show_recent")
        self.cb_show_recent.setChecked(True)
        self.cb_show_recent.setProperty(u"prefEntry", u"ShowRecent")
        self.cb_show_recent.setProperty(u"prefPath", u"Mod/Material/TreeWidget")

        self.verticalLayout_5.addWidget(self.cb_show_recent)

        self.cb_show_empty_libraries = Gui_PrefCheckBox(self.gbMaterialSelector)
        self.cb_show_empty_libraries.setObjectName(u"cb_show_empty_libraries")
        self.cb_show_empty_libraries.setChecked(True)
        self.cb_show_empty_libraries.setProperty(u"prefEntry", u"ShowEmptyLibraries")
        self.cb_show_empty_libraries.setProperty(u"prefPath", u"Mod/Material/TreeWidget")

        self.verticalLayout_5.addWidget(self.cb_show_empty_libraries)

        self.cb_show_empty_folders = Gui_PrefCheckBox(self.gbMaterialSelector)
        self.cb_show_empty_folders.setObjectName(u"cb_show_empty_folders")
        self.cb_show_empty_folders.setProperty(u"prefEntry", u"ShowEmptyFolders")
        self.cb_show_empty_folders.setProperty(u"prefPath", u"Mod/Material/TreeWidget")

        self.verticalLayout_5.addWidget(self.cb_show_empty_folders)

        self.cb_show_legacy = Gui_PrefCheckBox(self.gbMaterialSelector)
        self.cb_show_legacy.setObjectName(u"cb_show_legacy")
        self.cb_show_legacy.setProperty(u"prefEntry", u"ShowLegacy")
        self.cb_show_legacy.setProperty(u"prefPath", u"Mod/Material/TreeWidget")

        self.verticalLayout_5.addWidget(self.cb_show_legacy)


        self.verticalLayout.addWidget(self.gbMaterialSelector)

        self.groupBox = QGroupBox(MatGui__DlgSettingsMaterial)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cb_show_favorites_editor = Gui_PrefCheckBox(self.groupBox)
        self.cb_show_favorites_editor.setObjectName(u"cb_show_favorites_editor")
        self.cb_show_favorites_editor.setChecked(True)
        self.cb_show_favorites_editor.setProperty(u"prefEntry", u"ShowFavorites")
        self.cb_show_favorites_editor.setProperty(u"prefPath", u"Mod/Material/Editor")

        self.verticalLayout_4.addWidget(self.cb_show_favorites_editor)

        self.cb_show_recent_editor = Gui_PrefCheckBox(self.groupBox)
        self.cb_show_recent_editor.setObjectName(u"cb_show_recent_editor")
        self.cb_show_recent_editor.setChecked(True)
        self.cb_show_recent_editor.setProperty(u"prefEntry", u"ShowRecent")
        self.cb_show_recent_editor.setProperty(u"prefPath", u"Mod/Material/Editor")

        self.verticalLayout_4.addWidget(self.cb_show_recent_editor)

        self.cb_show_empty_libraries_editor = Gui_PrefCheckBox(self.groupBox)
        self.cb_show_empty_libraries_editor.setObjectName(u"cb_show_empty_libraries_editor")
        self.cb_show_empty_libraries_editor.setChecked(True)
        self.cb_show_empty_libraries_editor.setProperty(u"prefEntry", u"ShowEmptyLibraries")
        self.cb_show_empty_libraries_editor.setProperty(u"prefPath", u"Mod/Material/Editor")

        self.verticalLayout_4.addWidget(self.cb_show_empty_libraries_editor)

        self.cb_show_empty_folders_editor = Gui_PrefCheckBox(self.groupBox)
        self.cb_show_empty_folders_editor.setObjectName(u"cb_show_empty_folders_editor")
        self.cb_show_empty_folders_editor.setProperty(u"prefEntry", u"ShowEmptyFolders")
        self.cb_show_empty_folders_editor.setProperty(u"prefPath", u"Mod/Material/Editor")

        self.verticalLayout_4.addWidget(self.cb_show_empty_folders_editor)

        self.cb_show_legacy_editor = Gui_PrefCheckBox(self.groupBox)
        self.cb_show_legacy_editor.setObjectName(u"cb_show_legacy_editor")
        self.cb_show_legacy_editor.setChecked(True)
        self.cb_show_legacy_editor.setProperty(u"prefEntry", u"ShowLegacy")
        self.cb_show_legacy_editor.setProperty(u"prefPath", u"Mod/Material/Editor")

        self.verticalLayout_4.addWidget(self.cb_show_legacy_editor)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(MatGui__DlgSettingsMaterial)
        self.cb_use_mat_from_custom_dir.toggled.connect(self.fc_custom_mat_dir.setEnabled)

        QMetaObject.connectSlotsByName(MatGui__DlgSettingsMaterial)
    # setupUi

    def retranslateUi(self, MatGui__DlgSettingsMaterial):
        MatGui__DlgSettingsMaterial.setWindowTitle(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"General", None))
        self.gb_4_materials.setTitle(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Card Resources", None))
#if QT_CONFIG(tooltip)
        self.cb_use_built_in_materials.setToolTip(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"The cards built-in to FreeCAD will be listed as available", None))
#endif // QT_CONFIG(tooltip)
        self.cb_use_built_in_materials.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Use built-in materials", None))
#if QT_CONFIG(tooltip)
        self.cb_use_mat_from_workbenches.setToolTip(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Use materials added by external workbenches", None))
#endif // QT_CONFIG(tooltip)
        self.cb_use_mat_from_workbenches.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Use materials from external workbenches", None))
#if QT_CONFIG(tooltip)
        self.cb_use_mat_from_config_dir.setToolTip(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Cards from FreeCAD\u2019s preferences directory are also listed as available", None))
#endif // QT_CONFIG(tooltip)
        self.cb_use_mat_from_config_dir.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Use materials from the Materials preference directory", None))
#if QT_CONFIG(tooltip)
        self.cb_use_mat_from_custom_dir.setToolTip(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Material cards from the specified directory will also be listed as available", None))
#endif // QT_CONFIG(tooltip)
        self.cb_use_mat_from_custom_dir.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Use materials from user-defined directory", None))
        self.l_custom_mat_dir.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"User directory", None))
        self.gb_4_materials_2.setTitle(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Card Sorting and Duplicates", None))
#if QT_CONFIG(tooltip)
        self.cb_delete_duplicates.setToolTip(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Duplicate cards will be deleted from the displayed material card list", None))
#endif // QT_CONFIG(tooltip)
        self.cb_delete_duplicates.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Delete card duplicates", None))
#if QT_CONFIG(tooltip)
        self.cb_sort_by_resources.setToolTip(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Material cards appear sorted by their resources (locations).\n"
"If unchecked, they will be sorted by their name.", None))
#endif // QT_CONFIG(tooltip)
        self.cb_sort_by_resources.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Sort by resources", None))
        self.gbMaterialSelector.setTitle(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Material Selector", None))
        self.cb_show_favorites.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Show favorites", None))
        self.cb_show_recent.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Show recent", None))
        self.cb_show_empty_libraries.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Show empty libraries", None))
        self.cb_show_empty_folders.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Show empty folders", None))
        self.cb_show_legacy.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Show legacy files", None))
        self.groupBox.setTitle(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Material Editor", None))
        self.cb_show_favorites_editor.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Show favorites", None))
        self.cb_show_recent_editor.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Show recent", None))
        self.cb_show_empty_libraries_editor.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Show empty libraries", None))
        self.cb_show_empty_folders_editor.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Show empty folders", None))
        self.cb_show_legacy_editor.setText(QCoreApplication.translate("MatGui::DlgSettingsMaterial", u"Show legacy files", None))
    # retranslateUi

