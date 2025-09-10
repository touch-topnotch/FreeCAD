# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsFemElmer.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QWidget)
import Fem_rc

class Ui_FemGui_DlgSettingsFemElmerImp(object):
    def setupUi(self, FemGui__DlgSettingsFemElmerImp):
        if not FemGui__DlgSettingsFemElmerImp.objectName():
            FemGui__DlgSettingsFemElmerImp.setObjectName(u"FemGui__DlgSettingsFemElmerImp")
        FemGui__DlgSettingsFemElmerImp.resize(350, 259)
        self.gridLayout_3 = QGridLayout(FemGui__DlgSettingsFemElmerImp)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gb_gmsh_param = QGroupBox(FemGui__DlgSettingsFemElmerImp)
        self.gb_gmsh_param.setObjectName(u"gb_gmsh_param")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_gmsh_param.sizePolicy().hasHeightForWidth())
        self.gb_gmsh_param.setSizePolicy(sizePolicy)
        self.gb_gmsh_param.setLayoutDirection(Qt.LeftToRight)
        self.gb_gmsh_param.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gridLayout = QGridLayout(self.gb_gmsh_param)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.l_grid_binary_std = QLabel(self.gb_gmsh_param)
        self.l_grid_binary_std.setObjectName(u"l_grid_binary_std")

        self.gridLayout.addWidget(self.l_grid_binary_std, 0, 0, 1, 1)

        self.fc_elmer_binary_path = Gui_PrefFileChooser(self.gb_gmsh_param)
        self.fc_elmer_binary_path.setObjectName(u"fc_elmer_binary_path")
        self.fc_elmer_binary_path.setEnabled(False)
        sizePolicy.setHeightForWidth(self.fc_elmer_binary_path.sizePolicy().hasHeightForWidth())
        self.fc_elmer_binary_path.setSizePolicy(sizePolicy)
        self.fc_elmer_binary_path.setMinimumSize(QSize(0, 0))
        self.fc_elmer_binary_path.setSizeIncrement(QSize(0, 0))
        self.fc_elmer_binary_path.setBaseSize(QSize(0, 0))
        self.fc_elmer_binary_path.setProperty(u"prefEntry", u"elmerBinaryPath")
        self.fc_elmer_binary_path.setProperty(u"prefPath", u"Mod/Fem/Elmer")

        self.gridLayout.addWidget(self.fc_elmer_binary_path, 3, 1, 1, 1)

        self.cb_grid_binary_std = Gui_PrefCheckBox(self.gb_gmsh_param)
        self.cb_grid_binary_std.setObjectName(u"cb_grid_binary_std")
        self.cb_grid_binary_std.setChecked(True)
        self.cb_grid_binary_std.setProperty(u"prefEntry", u"UseStandardGridLocation")
        self.cb_grid_binary_std.setProperty(u"prefPath", u"Mod/Fem/Elmer")

        self.gridLayout.addWidget(self.cb_grid_binary_std, 0, 1, 1, 1)

        self.fc_grid_binary_path = Gui_PrefFileChooser(self.gb_gmsh_param)
        self.fc_grid_binary_path.setObjectName(u"fc_grid_binary_path")
        self.fc_grid_binary_path.setEnabled(False)
        sizePolicy.setHeightForWidth(self.fc_grid_binary_path.sizePolicy().hasHeightForWidth())
        self.fc_grid_binary_path.setSizePolicy(sizePolicy)
        self.fc_grid_binary_path.setMinimumSize(QSize(0, 0))
        self.fc_grid_binary_path.setSizeIncrement(QSize(0, 0))
        self.fc_grid_binary_path.setBaseSize(QSize(0, 0))
        self.fc_grid_binary_path.setProperty(u"prefEntry", u"gridBinaryPath")
        self.fc_grid_binary_path.setProperty(u"prefPath", u"Mod/Fem/Elmer")

        self.gridLayout.addWidget(self.fc_grid_binary_path, 1, 1, 1, 1)

        self.l_elmer_binary_std = QLabel(self.gb_gmsh_param)
        self.l_elmer_binary_std.setObjectName(u"l_elmer_binary_std")

        self.gridLayout.addWidget(self.l_elmer_binary_std, 2, 0, 1, 1)

        self.cb_elmer_binary_std = Gui_PrefCheckBox(self.gb_gmsh_param)
        self.cb_elmer_binary_std.setObjectName(u"cb_elmer_binary_std")
        self.cb_elmer_binary_std.setChecked(True)
        self.cb_elmer_binary_std.setProperty(u"prefEntry", u"UseStandardElmerLocation")
        self.cb_elmer_binary_std.setProperty(u"prefPath", u"Mod/Fem/Elmer")

        self.gridLayout.addWidget(self.cb_elmer_binary_std, 2, 1, 1, 1)

        self.l_grid_binary_path = QLabel(self.gb_gmsh_param)
        self.l_grid_binary_path.setObjectName(u"l_grid_binary_path")
        self.l_grid_binary_path.setEnabled(False)
        self.l_grid_binary_path.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.l_grid_binary_path, 1, 0, 1, 1)

        self.l_elmer_binary_path = QLabel(self.gb_gmsh_param)
        self.l_elmer_binary_path.setObjectName(u"l_elmer_binary_path")
        self.l_elmer_binary_path.setEnabled(False)
        self.l_elmer_binary_path.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.l_elmer_binary_path, 3, 0, 1, 1)


        self.gridLayout_3.addWidget(self.gb_gmsh_param, 0, 0, 1, 1)

        self.gb_elmer_options = QGroupBox(FemGui__DlgSettingsFemElmerImp)
        self.gb_elmer_options.setObjectName(u"gb_elmer_options")
        self.gridLayout_2 = QGridLayout(self.gb_elmer_options)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.l_elmer_multithreading = QLabel(self.gb_elmer_options)
        self.l_elmer_multithreading.setObjectName(u"l_elmer_multithreading")

        self.gridLayout_2.addWidget(self.l_elmer_multithreading, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_cores = QLabel(self.gb_elmer_options)
        self.label_cores.setObjectName(u"label_cores")
        self.label_cores.setEnabled(True)

        self.horizontalLayout.addWidget(self.label_cores)

        self.sb_elmer_num_cores = Gui_PrefSpinBox(self.gb_elmer_options)
        self.sb_elmer_num_cores.setObjectName(u"sb_elmer_num_cores")
        self.sb_elmer_num_cores.setEnabled(True)
        self.sb_elmer_num_cores.setMinimum(1)
        self.sb_elmer_num_cores.setMaximum(32)
        self.sb_elmer_num_cores.setProperty(u"prefEntry", u"UseNumberOfCores")
        self.sb_elmer_num_cores.setProperty(u"prefPath", u"Mod/Fem/Elmer")

        self.horizontalLayout.addWidget(self.sb_elmer_num_cores)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.l_elmer_multiCPU = QLabel(self.gb_elmer_options)
        self.l_elmer_multiCPU.setObjectName(u"l_elmer_multiCPU")

        self.gridLayout_2.addWidget(self.l_elmer_multiCPU, 1, 0, 1, 1)

        self.cb_elmer_filtering = Gui_PrefCheckBox(self.gb_elmer_options)
        self.cb_elmer_filtering.setObjectName(u"cb_elmer_filtering")
        self.cb_elmer_filtering.setChecked(True)
        self.cb_elmer_filtering.setProperty(u"prefEntry", u"FilterMultiCPUResults")
        self.cb_elmer_filtering.setProperty(u"prefPath", u"Mod/Fem/Elmer")

        self.gridLayout_2.addWidget(self.cb_elmer_filtering, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.gb_elmer_options, 1, 0, 1, 1)

        self.gb_elmer_results = QGroupBox(FemGui__DlgSettingsFemElmerImp)
        self.gb_elmer_results.setObjectName(u"gb_elmer_results")
        self.gdl_results = QGridLayout(self.gb_elmer_results)
        self.gdl_results.setSpacing(6)
        self.gdl_results.setContentsMargins(11, 11, 11, 11)
        self.gdl_results.setObjectName(u"gdl_results")
        self.ckb_elmer_format = Gui_PrefCheckBox(self.gb_elmer_results)
        self.ckb_elmer_format.setObjectName(u"ckb_elmer_format")
        self.ckb_elmer_format.setChecked(False)
        self.ckb_elmer_format.setProperty(u"prefEntry", u"BinaryOutput")
        self.ckb_elmer_format.setProperty(u"prefPath", u"Mod/Fem/Elmer")

        self.gdl_results.addWidget(self.ckb_elmer_format, 0, 0, 1, 1)

        self.ckb_elmer_geom_id = Gui_PrefCheckBox(self.gb_elmer_results)
        self.ckb_elmer_geom_id.setObjectName(u"ckb_elmer_geom_id")
        self.ckb_elmer_geom_id.setChecked(False)
        self.ckb_elmer_geom_id.setProperty(u"prefEntry", u"SaveGeometryIndex")
        self.ckb_elmer_geom_id.setProperty(u"prefPath", u"Mod/Fem/Elmer")

        self.gdl_results.addWidget(self.ckb_elmer_geom_id, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.gb_elmer_results, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.retranslateUi(FemGui__DlgSettingsFemElmerImp)
        self.cb_grid_binary_std.toggled.connect(self.l_grid_binary_path.setDisabled)
        self.cb_grid_binary_std.toggled.connect(self.fc_grid_binary_path.setDisabled)
        self.cb_elmer_binary_std.toggled.connect(self.fc_elmer_binary_path.setDisabled)
        self.cb_elmer_binary_std.toggled.connect(self.l_elmer_binary_path.setDisabled)

        QMetaObject.connectSlotsByName(FemGui__DlgSettingsFemElmerImp)
    # setupUi

    def retranslateUi(self, FemGui__DlgSettingsFemElmerImp):
        FemGui__DlgSettingsFemElmerImp.setWindowTitle(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Elmer", None))
        self.gb_gmsh_param.setTitle(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Elmer binaries", None))
        self.l_grid_binary_std.setText(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"ElmerGrid:", None))
#if QT_CONFIG(tooltip)
        self.fc_elmer_binary_path.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"<html><head/><body><p>Leave blank to use default Elmer elmer binary file</p><p><span style=\" font-weight:600;\">Note:</span> To use multithreading you must specify here<br> the executable variant with the suffix &quot;_mpi&quot;.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cb_grid_binary_std.setText(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Search in known binary directories", None))
#if QT_CONFIG(tooltip)
        self.fc_grid_binary_path.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Leave blank to use default ElmerGrid binary file", None))
#endif // QT_CONFIG(tooltip)
        self.l_elmer_binary_std.setText(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"ElmerSolver:", None))
        self.cb_elmer_binary_std.setText(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Search in known binary directories", None))
        self.l_grid_binary_path.setText(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"ElmerGrid binary path", None))
        self.l_elmer_binary_path.setText(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"ElmerSolver binary path", None))
        self.gb_elmer_options.setTitle(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Options", None))
        self.l_elmer_multithreading.setText(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Multithreading:", None))
        self.label_cores.setText(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"CPU cores to be used:", None))
#if QT_CONFIG(tooltip)
        self.sb_elmer_num_cores.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"<html><head/><body><p><span style=\" font-weight:600;\">Note:</span> It is recommended to use an even number of cores to benefit from mesh symmetries. (Using 8 cores can be faster than 9 cores.)<br/><span style=\" font-weight:600;\">Note too:</span> In extreme cases ElmerSolver might not converge if the core number is too high.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.l_elmer_multiCPU.setText(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Multi-core CPU support:", None))
#if QT_CONFIG(tooltip)
        self.cb_elmer_filtering.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"The mesh volume regions processed by each CPU core\n"
"will be merged to make the volume boundaries invisible.", None))
#endif // QT_CONFIG(tooltip)
        self.cb_elmer_filtering.setText(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Filter results", None))
        self.gb_elmer_results.setTitle(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Results", None))
#if QT_CONFIG(tooltip)
        self.ckb_elmer_format.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Save result in binary format", None))
#endif // QT_CONFIG(tooltip)
        self.ckb_elmer_format.setText(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Use binary format", None))
#if QT_CONFIG(tooltip)
        self.ckb_elmer_geom_id.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Save the index of geometric entities", None))
#endif // QT_CONFIG(tooltip)
        self.ckb_elmer_geom_id.setText(QCoreApplication.translate("FemGui::DlgSettingsFemElmerImp", u"Save geometry IDs", None))
    # retranslateUi

