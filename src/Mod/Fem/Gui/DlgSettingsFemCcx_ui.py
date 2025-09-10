# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsFemCcx.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import Fem_rc

class Ui_FemGui_DlgSettingsFemCcxImp(object):
    def setupUi(self, FemGui__DlgSettingsFemCcxImp):
        if not FemGui__DlgSettingsFemCcxImp.objectName():
            FemGui__DlgSettingsFemCcxImp.setObjectName(u"FemGui__DlgSettingsFemCcxImp")
        FemGui__DlgSettingsFemCcxImp.resize(595, 848)
        self.verticalLayout_2 = QVBoxLayout(FemGui__DlgSettingsFemCcxImp)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gb_01_ccx_param = QGroupBox(FemGui__DlgSettingsFemCcxImp)
        self.gb_01_ccx_param.setObjectName(u"gb_01_ccx_param")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_01_ccx_param.sizePolicy().hasHeightForWidth())
        self.gb_01_ccx_param.setSizePolicy(sizePolicy)
        self.gb_01_ccx_param.setLayoutDirection(Qt.LeftToRight)
        self.gb_01_ccx_param.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gridLayout_2 = QGridLayout(self.gb_01_ccx_param)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.l_ccx_binary_std = QLabel(self.gb_01_ccx_param)
        self.l_ccx_binary_std.setObjectName(u"l_ccx_binary_std")

        self.gridLayout.addWidget(self.l_ccx_binary_std, 2, 0, 1, 1)

        self.cb_ccx_binary_std = Gui_PrefCheckBox(self.gb_01_ccx_param)
        self.cb_ccx_binary_std.setObjectName(u"cb_ccx_binary_std")
        self.cb_ccx_binary_std.setChecked(True)
        self.cb_ccx_binary_std.setProperty(u"prefEntry", u"UseStandardCcxLocation")
        self.cb_ccx_binary_std.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gridLayout.addWidget(self.cb_ccx_binary_std, 2, 1, 1, 1)

        self.l_ccx_binary_path = QLabel(self.gb_01_ccx_param)
        self.l_ccx_binary_path.setObjectName(u"l_ccx_binary_path")
        self.l_ccx_binary_path.setEnabled(False)
        self.l_ccx_binary_path.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.l_ccx_binary_path, 3, 0, 1, 1)

        self.fc_ccx_binary_path = Gui_PrefFileChooser(self.gb_01_ccx_param)
        self.fc_ccx_binary_path.setObjectName(u"fc_ccx_binary_path")
        self.fc_ccx_binary_path.setEnabled(False)
        sizePolicy.setHeightForWidth(self.fc_ccx_binary_path.sizePolicy().hasHeightForWidth())
        self.fc_ccx_binary_path.setSizePolicy(sizePolicy)
        self.fc_ccx_binary_path.setMinimumSize(QSize(0, 0))
        self.fc_ccx_binary_path.setSizeIncrement(QSize(0, 0))
        self.fc_ccx_binary_path.setBaseSize(QSize(0, 0))
        self.fc_ccx_binary_path.setProperty(u"prefEntry", u"ccxBinaryPath")
        self.fc_ccx_binary_path.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gridLayout.addWidget(self.fc_ccx_binary_path, 3, 1, 1, 1)

        self.l_editor = QLabel(self.gb_01_ccx_param)
        self.l_editor.setObjectName(u"l_editor")

        self.gridLayout.addWidget(self.l_editor, 4, 0, 1, 1)

        self.cb_int_editor = Gui_PrefCheckBox(self.gb_01_ccx_param)
        self.cb_int_editor.setObjectName(u"cb_int_editor")
        self.cb_int_editor.setChecked(True)
        self.cb_int_editor.setProperty(u"prefEntry", u"UseInternalEditor")
        self.cb_int_editor.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gridLayout.addWidget(self.cb_int_editor, 4, 1, 1, 1)

        self.l_ext_editor = QLabel(self.gb_01_ccx_param)
        self.l_ext_editor.setObjectName(u"l_ext_editor")
        self.l_ext_editor.setEnabled(False)
        self.l_ext_editor.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.l_ext_editor, 5, 0, 1, 1)

        self.fc_ext_editor = Gui_PrefFileChooser(self.gb_01_ccx_param)
        self.fc_ext_editor.setObjectName(u"fc_ext_editor")
        self.fc_ext_editor.setEnabled(False)
        self.fc_ext_editor.setProperty(u"prefEntry", u"ExternalEditorPath")
        self.fc_ext_editor.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gridLayout.addWidget(self.fc_ext_editor, 5, 1, 1, 1)

        self.l_editor_2 = QLabel(self.gb_01_ccx_param)
        self.l_editor_2.setObjectName(u"l_editor_2")

        self.gridLayout.addWidget(self.l_editor_2, 6, 0, 1, 1)

        self.cb_split_inp_writer = Gui_PrefCheckBox(self.gb_01_ccx_param)
        self.cb_split_inp_writer.setObjectName(u"cb_split_inp_writer")
        self.cb_split_inp_writer.setEnabled(True)
        self.cb_split_inp_writer.setChecked(False)
        self.cb_split_inp_writer.setProperty(u"prefEntry", u"SplitInputWriter")
        self.cb_split_inp_writer.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gridLayout.addWidget(self.cb_split_inp_writer, 6, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.gb_01_ccx_param)

        self.gb_02_analysis_param = QGroupBox(FemGui__DlgSettingsFemCcxImp)
        self.gb_02_analysis_param.setObjectName(u"gb_02_analysis_param")
        self.horizontalLayout_3 = QHBoxLayout(self.gb_02_analysis_param)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gl_analysis = QGridLayout()
        self.gl_analysis.setSpacing(6)
        self.gl_analysis.setObjectName(u"gl_analysis")
        self.l_type = QLabel(self.gb_02_analysis_param)
        self.l_type.setObjectName(u"l_type")

        self.gl_analysis.addWidget(self.l_type, 0, 0, 1, 1)

        self.cb_analysis_type = Gui_PrefComboBox(self.gb_02_analysis_param)
        icon = QIcon()
        icon.addFile(u":/icons/fem-solver-analysis-static.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cb_analysis_type.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/icons/fem-solver-analysis-frequency.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cb_analysis_type.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/icons/fem-solver-analysis-thermomechanical.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cb_analysis_type.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/icons/fem-solver-analysis-checkmesh.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cb_analysis_type.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/icons/fem-solver-analysis-buckling.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cb_analysis_type.addItem(icon4, "")
        self.cb_analysis_type.setObjectName(u"cb_analysis_type")
        self.cb_analysis_type.setMinimumSize(QSize(148, 0))
        self.cb_analysis_type.setProperty(u"prefEntry", u"AnalysisType")
        self.cb_analysis_type.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_analysis.addWidget(self.cb_analysis_type, 0, 1, 1, 1)

        self.gl_analysis.setColumnStretch(0, 3)
        self.gl_analysis.setColumnStretch(1, 2)

        self.horizontalLayout_3.addLayout(self.gl_analysis)


        self.verticalLayout_2.addWidget(self.gb_02_analysis_param)

        self.gb_03_solver_param = QGroupBox(FemGui__DlgSettingsFemCcxImp)
        self.gb_03_solver_param.setObjectName(u"gb_03_solver_param")
        self.horizontalLayout_1 = QHBoxLayout(self.gb_03_solver_param)
        self.horizontalLayout_1.setSpacing(6)
        self.horizontalLayout_1.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.gl_solver = QGridLayout()
        self.gl_solver.setSpacing(6)
        self.gl_solver.setObjectName(u"gl_solver")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gl_solver.addItem(self.horizontalSpacer_3, 7, 1, 1, 1)

        self.l_ccx_initial_time_step = QLabel(self.gb_03_solver_param)
        self.l_ccx_initial_time_step.setObjectName(u"l_ccx_initial_time_step")

        self.gl_solver.addWidget(self.l_ccx_initial_time_step, 5, 0, 1, 1)

        self.l_ccx_analysis_time = QLabel(self.gb_03_solver_param)
        self.l_ccx_analysis_time.setObjectName(u"l_ccx_analysis_time")

        self.gl_solver.addWidget(self.l_ccx_analysis_time, 6, 0, 1, 1)

        self.cb_use_iterations_param = Gui_PrefCheckBox(self.gb_03_solver_param)
        self.cb_use_iterations_param.setObjectName(u"cb_use_iterations_param")
        self.cb_use_iterations_param.setChecked(False)
        self.cb_use_iterations_param.setProperty(u"prefEntry", u"UseNonCcxIterationParam")
        self.cb_use_iterations_param.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_solver.addWidget(self.cb_use_iterations_param, 3, 2, 1, 1)

        self.l_ccx_numcpu = QLabel(self.gb_03_solver_param)
        self.l_ccx_numcpu.setObjectName(u"l_ccx_numcpu")

        self.gl_solver.addWidget(self.l_ccx_numcpu, 0, 0, 1, 1)

        self.cb_BeamShellOutput = Gui_PrefCheckBox(self.gb_03_solver_param)
        self.cb_BeamShellOutput.setObjectName(u"cb_BeamShellOutput")
        self.cb_BeamShellOutput.setChecked(True)
        self.cb_BeamShellOutput.setProperty(u"prefEntry", u"BeamShellOutput")
        self.cb_BeamShellOutput.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_solver.addWidget(self.cb_BeamShellOutput, 9, 2, 1, 1)

        self.sb_ccx_numcpu = Gui_PrefSpinBox(self.gb_03_solver_param)
        self.sb_ccx_numcpu.setObjectName(u"sb_ccx_numcpu")
        self.sb_ccx_numcpu.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_ccx_numcpu.setMinimum(1)
        self.sb_ccx_numcpu.setProperty(u"prefEntry", u"AnalysisNumCPUs")
        self.sb_ccx_numcpu.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_solver.addWidget(self.sb_ccx_numcpu, 0, 2, 1, 1)

        self.cmb_solver = Gui_PrefComboBox(self.gb_03_solver_param)
        self.cmb_solver.addItem("")
        self.cmb_solver.addItem("")
        self.cmb_solver.addItem("")
        self.cmb_solver.addItem("")
        self.cmb_solver.addItem("")
        self.cmb_solver.addItem("")
        self.cmb_solver.setObjectName(u"cmb_solver")
        self.cmb_solver.setEnabled(True)
        self.cmb_solver.setEditable(False)
        self.cmb_solver.setProperty(u"prefEntry", u"Solver")
        self.cmb_solver.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_solver.addWidget(self.cmb_solver, 1, 2, 1, 1)

        self.l_non_lin_geom = QLabel(self.gb_03_solver_param)
        self.l_non_lin_geom.setObjectName(u"l_non_lin_geom")

        self.gl_solver.addWidget(self.l_non_lin_geom, 2, 0, 1, 1)

        self.dsb_ccx_maximum_time_step = Gui_PrefDoubleSpinBox(self.gb_03_solver_param)
        self.dsb_ccx_maximum_time_step.setObjectName(u"dsb_ccx_maximum_time_step")
        self.dsb_ccx_maximum_time_step.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.dsb_ccx_maximum_time_step.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsb_ccx_maximum_time_step.setSuffix(u" s")
        self.dsb_ccx_maximum_time_step.setDecimals(9)
        self.dsb_ccx_maximum_time_step.setMinimum(0.000000001000000)
        self.dsb_ccx_maximum_time_step.setSingleStep(1.000000000000000)
        self.dsb_ccx_maximum_time_step.setValue(1.000000000000000)
        self.dsb_ccx_maximum_time_step.setProperty(u"prefEntry", u"AnalysisTimeMaximumStep")
        self.dsb_ccx_maximum_time_step.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_solver.addWidget(self.dsb_ccx_maximum_time_step, 8, 2, 1, 1)

        self.dsb_ccx_analysis_time = Gui_PrefDoubleSpinBox(self.gb_03_solver_param)
        self.dsb_ccx_analysis_time.setObjectName(u"dsb_ccx_analysis_time")
        self.dsb_ccx_analysis_time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsb_ccx_analysis_time.setSuffix(u" s")
        self.dsb_ccx_analysis_time.setDecimals(9)
        self.dsb_ccx_analysis_time.setMinimum(0.000000001000000)
        self.dsb_ccx_analysis_time.setSingleStep(0.010000000000000)
        self.dsb_ccx_analysis_time.setValue(1.000000000000000)
        self.dsb_ccx_analysis_time.setProperty(u"prefEntry", u"AnalysisTime")
        self.dsb_ccx_analysis_time.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_solver.addWidget(self.dsb_ccx_analysis_time, 6, 2, 1, 1)

        self.l_solver = QLabel(self.gb_03_solver_param)
        self.l_solver.setObjectName(u"l_solver")
        self.l_solver.setEnabled(True)

        self.gl_solver.addWidget(self.l_solver, 1, 0, 1, 1)

        self.l_use_iterations_param = QLabel(self.gb_03_solver_param)
        self.l_use_iterations_param.setObjectName(u"l_use_iterations_param")

        self.gl_solver.addWidget(self.l_use_iterations_param, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gl_solver.addItem(self.horizontalSpacer_2, 5, 1, 1, 1)

        self.l_ccx_max_iterations = QLabel(self.gb_03_solver_param)
        self.l_ccx_max_iterations.setObjectName(u"l_ccx_max_iterations")

        self.gl_solver.addWidget(self.l_ccx_max_iterations, 4, 0, 1, 1)

        self.l_ccx_minimum_time_step = QLabel(self.gb_03_solver_param)
        self.l_ccx_minimum_time_step.setObjectName(u"l_ccx_minimum_time_step")

        self.gl_solver.addWidget(self.l_ccx_minimum_time_step, 7, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gl_solver.addItem(self.horizontalSpacer_4, 8, 1, 1, 1)

        self.dsb_ccx_minimum_time_step = Gui_PrefDoubleSpinBox(self.gb_03_solver_param)
        self.dsb_ccx_minimum_time_step.setObjectName(u"dsb_ccx_minimum_time_step")
        self.dsb_ccx_minimum_time_step.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.dsb_ccx_minimum_time_step.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsb_ccx_minimum_time_step.setSuffix(u" s")
        self.dsb_ccx_minimum_time_step.setDecimals(9)
        self.dsb_ccx_minimum_time_step.setMinimum(0.000000001000000)
        self.dsb_ccx_minimum_time_step.setSingleStep(0.010000000000000)
        self.dsb_ccx_minimum_time_step.setValue(0.000010000000000)
        self.dsb_ccx_minimum_time_step.setProperty(u"prefEntry", u"AnalysisTimeMinimumStep")
        self.dsb_ccx_minimum_time_step.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_solver.addWidget(self.dsb_ccx_minimum_time_step, 7, 2, 1, 1)

        self.cb_ccx_non_lin_geom = Gui_PrefCheckBox(self.gb_03_solver_param)
        self.cb_ccx_non_lin_geom.setObjectName(u"cb_ccx_non_lin_geom")
        self.cb_ccx_non_lin_geom.setChecked(False)
        self.cb_ccx_non_lin_geom.setProperty(u"prefEntry", u"NonlinearGeometry")
        self.cb_ccx_non_lin_geom.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_solver.addWidget(self.cb_ccx_non_lin_geom, 2, 2, 1, 1)

        self.dsb_ccx_initial_time_step = Gui_PrefDoubleSpinBox(self.gb_03_solver_param)
        self.dsb_ccx_initial_time_step.setObjectName(u"dsb_ccx_initial_time_step")
        self.dsb_ccx_initial_time_step.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.dsb_ccx_initial_time_step.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsb_ccx_initial_time_step.setSuffix(u" s")
        self.dsb_ccx_initial_time_step.setDecimals(9)
        self.dsb_ccx_initial_time_step.setMinimum(0.000000001000000)
        self.dsb_ccx_initial_time_step.setSingleStep(0.010000000000000)
        self.dsb_ccx_initial_time_step.setValue(0.010000000000000)
        self.dsb_ccx_initial_time_step.setProperty(u"prefEntry", u"AnalysisTimeInitialStep")
        self.dsb_ccx_initial_time_step.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_solver.addWidget(self.dsb_ccx_initial_time_step, 5, 2, 1, 1)

        self.l_BeamShellOutput = QLabel(self.gb_03_solver_param)
        self.l_BeamShellOutput.setObjectName(u"l_BeamShellOutput")

        self.gl_solver.addWidget(self.l_BeamShellOutput, 9, 0, 1, 1)

        self.sb_ccx_max_iterations = Gui_PrefSpinBox(self.gb_03_solver_param)
        self.sb_ccx_max_iterations.setObjectName(u"sb_ccx_max_iterations")
        self.sb_ccx_max_iterations.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_ccx_max_iterations.setMinimum(1)
        self.sb_ccx_max_iterations.setMaximum(10000000)
        self.sb_ccx_max_iterations.setSingleStep(10)
        self.sb_ccx_max_iterations.setValue(2000)
        self.sb_ccx_max_iterations.setProperty(u"prefEntry", u"AnalysisMaxIterations")
        self.sb_ccx_max_iterations.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_solver.addWidget(self.sb_ccx_max_iterations, 4, 2, 1, 1)

        self.l_ccx_maximum_time_step = QLabel(self.gb_03_solver_param)
        self.l_ccx_maximum_time_step.setObjectName(u"l_ccx_maximum_time_step")

        self.gl_solver.addWidget(self.l_ccx_maximum_time_step, 8, 0, 1, 1)

        self.l_pipeline_result = QLabel(self.gb_03_solver_param)
        self.l_pipeline_result.setObjectName(u"l_pipeline_result")

        self.gl_solver.addWidget(self.l_pipeline_result, 10, 0, 1, 1)

        self.ckb_pipeline_result = Gui_PrefCheckBox(self.gb_03_solver_param)
        self.ckb_pipeline_result.setObjectName(u"ckb_pipeline_result")
        self.ckb_pipeline_result.setChecked(False)
        self.ckb_pipeline_result.setProperty(u"prefEntry", u"ResultAsPipeline")
        self.ckb_pipeline_result.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_solver.addWidget(self.ckb_pipeline_result, 10, 2, 1, 1)

        self.l_result_format = QLabel(self.gb_03_solver_param)
        self.l_result_format.setObjectName(u"l_result_format")

        self.gl_solver.addWidget(self.l_result_format, 11, 0, 1, 1)

        self.ckb_result_format = Gui_PrefCheckBox(self.gb_03_solver_param)
        self.ckb_result_format.setObjectName(u"ckb_result_format")
        self.ckb_result_format.setChecked(False)
        self.ckb_result_format.setProperty(u"prefEntry", u"BinaryOutput")
        self.ckb_result_format.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_solver.addWidget(self.ckb_result_format, 11, 2, 1, 1)

        self.gl_solver.setColumnStretch(0, 3)

        self.horizontalLayout_1.addLayout(self.gl_solver)


        self.verticalLayout_2.addWidget(self.gb_03_solver_param)

        self.gb_04_thermomech_params = QGroupBox(FemGui__DlgSettingsFemCcxImp)
        self.gb_04_thermomech_params.setObjectName(u"gb_04_thermomech_params")
        self.horizontalLayout_2 = QHBoxLayout(self.gb_04_thermomech_params)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gl_thremomech = QGridLayout()
        self.gl_thremomech.setSpacing(6)
        self.gl_thremomech.setObjectName(u"gl_thremomech")
        self.l_static = QLabel(self.gb_04_thermomech_params)
        self.l_static.setObjectName(u"l_static")

        self.gl_thremomech.addWidget(self.l_static, 1, 0, 1, 1)

        self.cb_static = Gui_PrefCheckBox(self.gb_04_thermomech_params)
        self.cb_static.setObjectName(u"cb_static")
        self.cb_static.setChecked(True)
        self.cb_static.setProperty(u"prefEntry", u"StaticAnalysis")
        self.cb_static.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_thremomech.addWidget(self.cb_static, 1, 1, 1, 1)

        self.gl_thremomech.setColumnStretch(0, 3)
        self.gl_thremomech.setColumnStretch(1, 2)

        self.horizontalLayout_2.addLayout(self.gl_thremomech)


        self.verticalLayout_2.addWidget(self.gb_04_thermomech_params)

        self.gb_05_frequercy_params = QGroupBox(FemGui__DlgSettingsFemCcxImp)
        self.gb_05_frequercy_params.setObjectName(u"gb_05_frequercy_params")
        self.verticalLayout = QVBoxLayout(self.gb_05_frequercy_params)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gl_frequ = QGridLayout()
        self.gl_frequ.setSpacing(6)
        self.gl_frequ.setObjectName(u"gl_frequ")
        self.sb_eigenmode_number = Gui_PrefSpinBox(self.gb_05_frequercy_params)
        self.sb_eigenmode_number.setObjectName(u"sb_eigenmode_number")
        self.sb_eigenmode_number.setMinimumSize(QSize(158, 0))
        self.sb_eigenmode_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_eigenmode_number.setMaximum(100)
        self.sb_eigenmode_number.setValue(10)
        self.sb_eigenmode_number.setProperty(u"prefEntry", u"EigenmodesCount")
        self.sb_eigenmode_number.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_frequ.addWidget(self.sb_eigenmode_number, 1, 2, 1, 1)

        self.l_eigenmode_high_limit = QLabel(self.gb_05_frequercy_params)
        self.l_eigenmode_high_limit.setObjectName(u"l_eigenmode_high_limit")

        self.gl_frequ.addWidget(self.l_eigenmode_high_limit, 2, 0, 1, 1)

        self.l_eigenmode_number = QLabel(self.gb_05_frequercy_params)
        self.l_eigenmode_number.setObjectName(u"l_eigenmode_number")

        self.gl_frequ.addWidget(self.l_eigenmode_number, 1, 0, 1, 1)

        self.dsb_eigenmode_high_limit = Gui_PrefDoubleSpinBox(self.gb_05_frequercy_params)
        self.dsb_eigenmode_high_limit.setObjectName(u"dsb_eigenmode_high_limit")
        self.dsb_eigenmode_high_limit.setMinimumSize(QSize(158, 0))
        self.dsb_eigenmode_high_limit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsb_eigenmode_high_limit.setSuffix(u" Hz")
        self.dsb_eigenmode_high_limit.setDecimals(1)
        self.dsb_eigenmode_high_limit.setMaximum(1000000.000000000000000)
        self.dsb_eigenmode_high_limit.setSingleStep(10000.000000000000000)
        self.dsb_eigenmode_high_limit.setValue(1000000.000000000000000)
        self.dsb_eigenmode_high_limit.setProperty(u"prefEntry", u"EigenmodeHighLimit")
        self.dsb_eigenmode_high_limit.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_frequ.addWidget(self.dsb_eigenmode_high_limit, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gl_frequ.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.l_eigenmode_low_limit = QLabel(self.gb_05_frequercy_params)
        self.l_eigenmode_low_limit.setObjectName(u"l_eigenmode_low_limit")

        self.gl_frequ.addWidget(self.l_eigenmode_low_limit, 3, 0, 1, 1)

        self.dsb_eigenmode_low_limit = Gui_PrefDoubleSpinBox(self.gb_05_frequercy_params)
        self.dsb_eigenmode_low_limit.setObjectName(u"dsb_eigenmode_low_limit")
        self.dsb_eigenmode_low_limit.setMinimumSize(QSize(158, 0))
        self.dsb_eigenmode_low_limit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsb_eigenmode_low_limit.setDecimals(1)
        self.dsb_eigenmode_low_limit.setMinimum(0.000000000000000)
        self.dsb_eigenmode_low_limit.setMaximum(1000000.000000000000000)
        self.dsb_eigenmode_low_limit.setSingleStep(10000.000000000000000)
        self.dsb_eigenmode_low_limit.setValue(0.000000000000000)
        self.dsb_eigenmode_low_limit.setProperty(u"prefEntry", u"EigenmodeLowLimit")
        self.dsb_eigenmode_low_limit.setProperty(u"prefPath", u"Mod/Fem/Ccx")

        self.gl_frequ.addWidget(self.dsb_eigenmode_low_limit, 3, 2, 1, 1)

        self.gl_frequ.setColumnStretch(0, 6)

        self.verticalLayout.addLayout(self.gl_frequ)


        self.verticalLayout_2.addWidget(self.gb_05_frequercy_params)


        self.retranslateUi(FemGui__DlgSettingsFemCcxImp)
        self.cb_int_editor.toggled.connect(self.l_ext_editor.setDisabled)
        self.cb_int_editor.toggled.connect(self.fc_ext_editor.setDisabled)
        self.cb_ccx_binary_std.toggled.connect(self.l_ccx_binary_path.setDisabled)
        self.cb_ccx_binary_std.toggled.connect(self.fc_ccx_binary_path.setDisabled)

        QMetaObject.connectSlotsByName(FemGui__DlgSettingsFemCcxImp)
    # setupUi

    def retranslateUi(self, FemGui__DlgSettingsFemCcxImp):
        FemGui__DlgSettingsFemCcxImp.setWindowTitle(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"CalculiX", None))
        self.gb_01_ccx_param.setTitle(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"CalculiX", None))
        self.l_ccx_binary_std.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"CalculiX binary", None))
        self.cb_ccx_binary_std.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Search in known binary directories", None))
        self.l_ccx_binary_path.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"ccx binary path", None))
#if QT_CONFIG(tooltip)
        self.fc_ccx_binary_path.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Leave blank to use default CalculiX ccx binary file", None))
#endif // QT_CONFIG(tooltip)
        self.l_editor.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Input file Editor", None))
        self.cb_int_editor.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Use internal editor for *.inp files", None))
        self.l_ext_editor.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"External editor:", None))
        self.l_editor_2.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Input file splitting", None))
        self.cb_split_inp_writer.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Split writing of  *.inp", None))
        self.gb_02_analysis_param.setTitle(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Analysis defaults", None))
        self.l_type.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Type", None))
        self.cb_analysis_type.setItemText(0, QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Static", None))
        self.cb_analysis_type.setItemText(1, QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Frequency", None))
        self.cb_analysis_type.setItemText(2, QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Thermomech", None))
        self.cb_analysis_type.setItemText(3, QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Check Mesh", None))
        self.cb_analysis_type.setItemText(4, QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Buckling", None))

#if QT_CONFIG(tooltip)
        self.cb_analysis_type.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Default type on analysis", None))
#endif // QT_CONFIG(tooltip)
        self.gb_03_solver_param.setTitle(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Solver defaults", None))
        self.l_ccx_initial_time_step.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Time Initial Step", None))
        self.l_ccx_analysis_time.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Time End", None))
        self.cb_use_iterations_param.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Use non ccx defaults", None))
        self.l_ccx_numcpu.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Number of CPU's to use", None))
        self.cb_BeamShellOutput.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"3D Output, unchecked for 2D", None))
#if QT_CONFIG(tooltip)
        self.sb_ccx_numcpu.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Number of threads used for analysis", None))
#endif // QT_CONFIG(tooltip)
        self.cmb_solver.setItemText(0, QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Default", None))
        self.cmb_solver.setItemText(1, QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"PaStiX", None))
        self.cmb_solver.setItemText(2, QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Pardiso", None))
        self.cmb_solver.setItemText(3, QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"SPOOLES equation solver", None))
        self.cmb_solver.setItemText(4, QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Iterative Scaling", None))
        self.cmb_solver.setItemText(5, QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Cholesky iterative solver", None))

        self.l_non_lin_geom.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Non-linear geometry", None))
        self.l_solver.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Matrix solver", None))
        self.l_use_iterations_param.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Time incrementation control parameter", None))
        self.l_ccx_max_iterations.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Maximum number of iterations", None))
        self.l_ccx_minimum_time_step.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Time Minimum Step", None))
        self.cb_ccx_non_lin_geom.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Use non-linear geometry", None))
        self.l_BeamShellOutput.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Beam, shell element 3D output format", None))
        self.l_ccx_maximum_time_step.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Time Maximum Step", None))
        self.l_pipeline_result.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Result object", None))
        self.ckb_pipeline_result.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Pipeline only", None))
#if QT_CONFIG(tooltip)
        self.ckb_pipeline_result.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Load results as pipeline instead of CCX_Results objects.\n"
"After unchecking this option, the CalculiX command behaves like SolverCalculiXCcxTools", None))
#endif // QT_CONFIG(tooltip)
        self.l_result_format.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Result format", None))
#if QT_CONFIG(tooltip)
        self.ckb_result_format.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Save result in binary format.\n"
"Only takes effect if 'Pipeline only' is enabled", None))
#endif // QT_CONFIG(tooltip)
        self.ckb_result_format.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Use binary format", None))
        self.gb_04_thermomech_params.setTitle(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Thermo mechanical defaults", None))
        self.l_static.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Analysis type (transient or steady state)", None))
        self.cb_static.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Use steady state", None))
        self.gb_05_frequercy_params.setTitle(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Frequency defaults", None))
        self.l_eigenmode_high_limit.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"High frequency limit", None))
        self.l_eigenmode_number.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Eigenmode number", None))
        self.l_eigenmode_low_limit.setText(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u"Low frequency limit", None))
        self.dsb_eigenmode_low_limit.setSuffix(QCoreApplication.translate("FemGui::DlgSettingsFemCcxImp", u" Hz", None))
    # retranslateUi

