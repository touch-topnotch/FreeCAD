# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsFemZ88.ui'
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
import Fem_rc

class Ui_FemGui_DlgSettingsFemZ88Imp(object):
    def setupUi(self, FemGui__DlgSettingsFemZ88Imp):
        if not FemGui__DlgSettingsFemZ88Imp.objectName():
            FemGui__DlgSettingsFemZ88Imp.setObjectName(u"FemGui__DlgSettingsFemZ88Imp")
        FemGui__DlgSettingsFemZ88Imp.resize(466, 218)
        self.verticalLayout_3 = QVBoxLayout(FemGui__DlgSettingsFemZ88Imp)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gb_z88_param_binary = QGroupBox(FemGui__DlgSettingsFemZ88Imp)
        self.gb_z88_param_binary.setObjectName(u"gb_z88_param_binary")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_z88_param_binary.sizePolicy().hasHeightForWidth())
        self.gb_z88_param_binary.setSizePolicy(sizePolicy)
        self.gb_z88_param_binary.setLayoutDirection(Qt.LeftToRight)
        self.gb_z88_param_binary.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.verticalLayout = QVBoxLayout(self.gb_z88_param_binary)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gl_z88 = QGridLayout()
        self.gl_z88.setSpacing(6)
        self.gl_z88.setObjectName(u"gl_z88")
        self.cb_z88_binary_std = Gui_PrefCheckBox(self.gb_z88_param_binary)
        self.cb_z88_binary_std.setObjectName(u"cb_z88_binary_std")
        self.cb_z88_binary_std.setMinimumSize(QSize(0, 20))
        self.cb_z88_binary_std.setChecked(True)
        self.cb_z88_binary_std.setProperty(u"prefEntry", u"UseStandardZ88Location")
        self.cb_z88_binary_std.setProperty(u"prefPath", u"Mod/Fem/Z88")

        self.gl_z88.addWidget(self.cb_z88_binary_std, 0, 2, 1, 1)

        self.l_z88_binary_path = QLabel(self.gb_z88_param_binary)
        self.l_z88_binary_path.setObjectName(u"l_z88_binary_path")
        self.l_z88_binary_path.setEnabled(True)
        sizePolicy.setHeightForWidth(self.l_z88_binary_path.sizePolicy().hasHeightForWidth())
        self.l_z88_binary_path.setSizePolicy(sizePolicy)
        self.l_z88_binary_path.setMinimumSize(QSize(0, 0))

        self.gl_z88.addWidget(self.l_z88_binary_path, 2, 0, 1, 1)

        self.fc_z88_binary_path = Gui_PrefFileChooser(self.gb_z88_param_binary)
        self.fc_z88_binary_path.setObjectName(u"fc_z88_binary_path")
        self.fc_z88_binary_path.setEnabled(False)
        sizePolicy.setHeightForWidth(self.fc_z88_binary_path.sizePolicy().hasHeightForWidth())
        self.fc_z88_binary_path.setSizePolicy(sizePolicy)
        self.fc_z88_binary_path.setMinimumSize(QSize(0, 20))
        self.fc_z88_binary_path.setSizeIncrement(QSize(0, 0))
        self.fc_z88_binary_path.setBaseSize(QSize(0, 0))
        self.fc_z88_binary_path.setProperty(u"prefEntry", u"z88BinaryPath")
        self.fc_z88_binary_path.setProperty(u"prefPath", u"Mod/Fem/Z88")

        self.gl_z88.addWidget(self.fc_z88_binary_path, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gl_z88)


        self.verticalLayout_3.addWidget(self.gb_z88_param_binary)

        self.gb_z88_param_solver = QGroupBox(FemGui__DlgSettingsFemZ88Imp)
        self.gb_z88_param_solver.setObjectName(u"gb_z88_param_solver")
        sizePolicy.setHeightForWidth(self.gb_z88_param_solver.sizePolicy().hasHeightForWidth())
        self.gb_z88_param_solver.setSizePolicy(sizePolicy)
        self.gb_z88_param_solver.setLayoutDirection(Qt.LeftToRight)
        self.gb_z88_param_solver.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.verticalLayout_2 = QVBoxLayout(self.gb_z88_param_solver)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gl_z88_2 = QGridLayout()
        self.gl_z88_2.setSpacing(6)
        self.gl_z88_2.setObjectName(u"gl_z88_2")
        self.l_solver_method = QLabel(self.gb_z88_param_solver)
        self.l_solver_method.setObjectName(u"l_solver_method")

        self.gl_z88_2.addWidget(self.l_solver_method, 1, 0, 1, 1)

        self.cmb_solver = Gui_PrefComboBox(self.gb_z88_param_solver)
        self.cmb_solver.addItem("")
        self.cmb_solver.addItem("")
        self.cmb_solver.addItem("")
        self.cmb_solver.setObjectName(u"cmb_solver")
        self.cmb_solver.setEnabled(True)
        self.cmb_solver.setMinimumSize(QSize(0, 20))
        self.cmb_solver.setEditable(False)
        self.cmb_solver.setProperty(u"prefEntry", u"Solver")
        self.cmb_solver.setProperty(u"prefPath", u"Mod/Fem/Z88")

        self.gl_z88_2.addWidget(self.cmb_solver, 1, 2, 1, 1)

        self.l_max_stiffness = QLabel(self.gb_z88_param_solver)
        self.l_max_stiffness.setObjectName(u"l_max_stiffness")

        self.gl_z88_2.addWidget(self.l_max_stiffness, 2, 0, 1, 1)

        self.sb_Z88_MaxGS = Gui_PrefSpinBox(self.gb_z88_param_solver)
        self.sb_Z88_MaxGS.setObjectName(u"sb_Z88_MaxGS")
        self.sb_Z88_MaxGS.setMinimumSize(QSize(0, 20))
        self.sb_Z88_MaxGS.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_Z88_MaxGS.setMinimum(6000000)
        self.sb_Z88_MaxGS.setMaximum(2147483647)
        self.sb_Z88_MaxGS.setSingleStep(10000000)
        self.sb_Z88_MaxGS.setValue(100000000)
        self.sb_Z88_MaxGS.setProperty(u"prefEntry", u"MaxGS")
        self.sb_Z88_MaxGS.setProperty(u"prefPath", u"Mod/Fem/Z88")

        self.gl_z88_2.addWidget(self.sb_Z88_MaxGS, 2, 2, 1, 1)

        self.l_max_coincidence = QLabel(self.gb_z88_param_solver)
        self.l_max_coincidence.setObjectName(u"l_max_coincidence")

        self.gl_z88_2.addWidget(self.l_max_coincidence, 3, 0, 1, 1)

        self.sb_Z88_MaxKOI = Gui_PrefSpinBox(self.gb_z88_param_solver)
        self.sb_Z88_MaxKOI.setObjectName(u"sb_Z88_MaxKOI")
        self.sb_Z88_MaxKOI.setMinimumSize(QSize(0, 20))
        self.sb_Z88_MaxKOI.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_Z88_MaxKOI.setMinimum(50000)
        self.sb_Z88_MaxKOI.setMaximum(2147483647)
        self.sb_Z88_MaxKOI.setSingleStep(100000)
        self.sb_Z88_MaxKOI.setValue(2800000)
        self.sb_Z88_MaxKOI.setProperty(u"prefEntry", u"MaxKOI")
        self.sb_Z88_MaxKOI.setProperty(u"prefPath", u"Mod/Fem/Z88")

        self.gl_z88_2.addWidget(self.sb_Z88_MaxKOI, 3, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gl_z88_2)


        self.verticalLayout_3.addWidget(self.gb_z88_param_solver)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(FemGui__DlgSettingsFemZ88Imp)
        self.cb_z88_binary_std.toggled.connect(self.l_z88_binary_path.setDisabled)
        self.cb_z88_binary_std.toggled.connect(self.fc_z88_binary_path.setDisabled)

        QMetaObject.connectSlotsByName(FemGui__DlgSettingsFemZ88Imp)
    # setupUi

    def retranslateUi(self, FemGui__DlgSettingsFemZ88Imp):
        FemGui__DlgSettingsFemZ88Imp.setWindowTitle(QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Z88", None))
        self.gb_z88_param_binary.setTitle(QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Z88 Binary", None))
        self.cb_z88_binary_std.setText(QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Search in known binary directories", None))
        self.l_z88_binary_path.setText(QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"z88r binary path", None))
#if QT_CONFIG(tooltip)
        self.fc_z88_binary_path.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Leave blank to use default Z88, z88r binary file", None))
#endif // QT_CONFIG(tooltip)
        self.gb_z88_param_solver.setTitle(QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Solver Settings", None))
        self.l_solver_method.setText(QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Solver method", None))
        self.cmb_solver.setItemText(0, QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Iteration solver with SOR preconditioning (-sorcg)", None))
        self.cmb_solver.setItemText(1, QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Iteration solver with SIC preconditioning (-siccg)", None))
        self.cmb_solver.setItemText(2, QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Simple Cholesky solver (-choly)", None))

#if QT_CONFIG(tooltip)
        self.cmb_solver.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Solver method to be used", None))
#endif // QT_CONFIG(tooltip)
        self.l_max_stiffness.setText(QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Max places in stiffness matrix", None))
#if QT_CONFIG(tooltip)
        self.sb_Z88_MaxGS.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Maximum places in the stiffness matrix.\n"
"You might need to increase this when using the\n"
"Cholesky solver and getting the error message\n"
"that \"MAXGS\" needs to be increased.", None))
#endif // QT_CONFIG(tooltip)
        self.l_max_coincidence.setText(QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Maximum places in coincidence vector", None))
#if QT_CONFIG(tooltip)
        self.sb_Z88_MaxKOI.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemZ88Imp", u"Maximal places in coincidence vector.\n"
"(number of knots per element times\n"
" number of finite elements)\n"
"\n"
"You might need to increase this when using an\n"
"iterative solver and you get the error message\n"
"that \"MAXKOI\" needs to be increased.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

