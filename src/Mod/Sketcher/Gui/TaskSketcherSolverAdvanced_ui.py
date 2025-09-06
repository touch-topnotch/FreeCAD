# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskSketcherSolverAdvanced.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_TaskSketcherSolverAdvanced(object):
    def setupUi(self, TaskSketcherSolverAdvanced):
        if not TaskSketcherSolverAdvanced.objectName():
            TaskSketcherSolverAdvanced.setObjectName(u"TaskSketcherSolverAdvanced")
        TaskSketcherSolverAdvanced.resize(326, 630)
        TaskSketcherSolverAdvanced.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(TaskSketcherSolverAdvanced)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelDefaultSolver = QLabel(TaskSketcherSolverAdvanced)
        self.labelDefaultSolver.setObjectName(u"labelDefaultSolver")

        self.horizontalLayout_4.addWidget(self.labelDefaultSolver)

        self.comboBoxDefaultSolver = Gui_PrefComboBox(TaskSketcherSolverAdvanced)
        self.comboBoxDefaultSolver.addItem("")
        self.comboBoxDefaultSolver.addItem("")
        self.comboBoxDefaultSolver.addItem("")
        self.comboBoxDefaultSolver.setObjectName(u"comboBoxDefaultSolver")
        self.comboBoxDefaultSolver.setProperty(u"prefEntry", u"DefaultSolver")
        self.comboBoxDefaultSolver.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_4.addWidget(self.comboBoxDefaultSolver)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_4_2 = QHBoxLayout()
        self.horizontalLayout_4_2.setObjectName(u"horizontalLayout_4_2")
        self.labelDogLegGaussStep = QLabel(TaskSketcherSolverAdvanced)
        self.labelDogLegGaussStep.setObjectName(u"labelDogLegGaussStep")

        self.horizontalLayout_4_2.addWidget(self.labelDogLegGaussStep)

        self.comboBoxDogLegGaussStep = Gui_PrefComboBox(TaskSketcherSolverAdvanced)
        self.comboBoxDogLegGaussStep.addItem("")
        self.comboBoxDogLegGaussStep.addItem("")
        self.comboBoxDogLegGaussStep.addItem("")
        self.comboBoxDogLegGaussStep.setObjectName(u"comboBoxDogLegGaussStep")
        self.comboBoxDogLegGaussStep.setProperty(u"prefEntry", u"DogLegGaussStep")
        self.comboBoxDogLegGaussStep.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_4_2.addWidget(self.comboBoxDogLegGaussStep)


        self.verticalLayout.addLayout(self.horizontalLayout_4_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelMaxIter = QLabel(TaskSketcherSolverAdvanced)
        self.labelMaxIter.setObjectName(u"labelMaxIter")

        self.horizontalLayout_2.addWidget(self.labelMaxIter)

        self.spinBoxMaxIter = Gui_PrefSpinBox(TaskSketcherSolverAdvanced)
        self.spinBoxMaxIter.setObjectName(u"spinBoxMaxIter")
        self.spinBoxMaxIter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBoxMaxIter.setMaximum(999)
        self.spinBoxMaxIter.setValue(100)
        self.spinBoxMaxIter.setProperty(u"prefEntry", u"MaxIter")
        self.spinBoxMaxIter.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_2.addWidget(self.spinBoxMaxIter)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelSketchSizeMultiplier = QLabel(TaskSketcherSolverAdvanced)
        self.labelSketchSizeMultiplier.setObjectName(u"labelSketchSizeMultiplier")

        self.horizontalLayout_3.addWidget(self.labelSketchSizeMultiplier)

        self.checkBoxSketchSizeMultiplier = Gui_PrefCheckBox(TaskSketcherSolverAdvanced)
        self.checkBoxSketchSizeMultiplier.setObjectName(u"checkBoxSketchSizeMultiplier")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxSketchSizeMultiplier.sizePolicy().hasHeightForWidth())
        self.checkBoxSketchSizeMultiplier.setSizePolicy(sizePolicy)
        self.checkBoxSketchSizeMultiplier.setLayoutDirection(Qt.RightToLeft)
        self.checkBoxSketchSizeMultiplier.setProperty(u"prefEntry", u"SketchSizeMultiplier")
        self.checkBoxSketchSizeMultiplier.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_3.addWidget(self.checkBoxSketchSizeMultiplier)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.labelSolverConvergence = QLabel(TaskSketcherSolverAdvanced)
        self.labelSolverConvergence.setObjectName(u"labelSolverConvergence")

        self.horizontalLayout_9.addWidget(self.labelSolverConvergence)

        self.lineEditConvergence = Gui_PrefLineEdit(TaskSketcherSolverAdvanced)
        self.lineEditConvergence.setObjectName(u"lineEditConvergence")
        self.lineEditConvergence.setLayoutDirection(Qt.LeftToRight)
        self.lineEditConvergence.setText(u"1E-10")
        self.lineEditConvergence.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEditConvergence.setProperty(u"prefEntry", u"Convergence")
        self.lineEditConvergence.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_9.addWidget(self.lineEditConvergence)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.labelSolverParam1 = QLabel(TaskSketcherSolverAdvanced)
        self.labelSolverParam1.setObjectName(u"labelSolverParam1")
        self.labelSolverParam1.setText(u"Param1")

        self.horizontalLayout_10.addWidget(self.labelSolverParam1)

        self.lineEditSolverParam1 = Gui_PrefLineEdit(TaskSketcherSolverAdvanced)
        self.lineEditSolverParam1.setObjectName(u"lineEditSolverParam1")
        self.lineEditSolverParam1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEditSolverParam1.setProperty(u"prefEntry", u"param")
        self.lineEditSolverParam1.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_10.addWidget(self.lineEditSolverParam1)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.labelSolverParam2 = QLabel(TaskSketcherSolverAdvanced)
        self.labelSolverParam2.setObjectName(u"labelSolverParam2")
        self.labelSolverParam2.setText(u"Param2")

        self.horizontalLayout_11.addWidget(self.labelSolverParam2)

        self.lineEditSolverParam2 = Gui_PrefLineEdit(TaskSketcherSolverAdvanced)
        self.lineEditSolverParam2.setObjectName(u"lineEditSolverParam2")
        self.lineEditSolverParam2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEditSolverParam2.setProperty(u"prefEntry", u"param")
        self.lineEditSolverParam2.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_11.addWidget(self.lineEditSolverParam2)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.labelSolverParam3 = QLabel(TaskSketcherSolverAdvanced)
        self.labelSolverParam3.setObjectName(u"labelSolverParam3")
        self.labelSolverParam3.setText(u"Param3")

        self.horizontalLayout_12.addWidget(self.labelSolverParam3)

        self.lineEditSolverParam3 = Gui_PrefLineEdit(TaskSketcherSolverAdvanced)
        self.lineEditSolverParam3.setObjectName(u"lineEditSolverParam3")
        self.lineEditSolverParam3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEditSolverParam3.setProperty(u"prefEntry", u"param")
        self.lineEditSolverParam3.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_12.addWidget(self.lineEditSolverParam3)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelQRAlgorithm = QLabel(TaskSketcherSolverAdvanced)
        self.labelQRAlgorithm.setObjectName(u"labelQRAlgorithm")

        self.horizontalLayout.addWidget(self.labelQRAlgorithm)

        self.comboBoxQRMethod = Gui_PrefComboBox(TaskSketcherSolverAdvanced)
        self.comboBoxQRMethod.addItem("")
        self.comboBoxQRMethod.addItem("")
        self.comboBoxQRMethod.setObjectName(u"comboBoxQRMethod")
        self.comboBoxQRMethod.setProperty(u"prefEntry", u"QRMethod")
        self.comboBoxQRMethod.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout.addWidget(self.comboBoxQRMethod)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.labelPivotThreshold = QLabel(TaskSketcherSolverAdvanced)
        self.labelPivotThreshold.setObjectName(u"labelPivotThreshold")

        self.horizontalLayout_18.addWidget(self.labelPivotThreshold)

        self.lineEditQRPivotThreshold = Gui_PrefLineEdit(TaskSketcherSolverAdvanced)
        self.lineEditQRPivotThreshold.setObjectName(u"lineEditQRPivotThreshold")
        self.lineEditQRPivotThreshold.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEditQRPivotThreshold.setProperty(u"prefEntry", u"QRPivotThreshold")
        self.lineEditQRPivotThreshold.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_18.addWidget(self.lineEditQRPivotThreshold)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelRedundantSolver = QLabel(TaskSketcherSolverAdvanced)
        self.labelRedundantSolver.setObjectName(u"labelRedundantSolver")

        self.horizontalLayout_5.addWidget(self.labelRedundantSolver)

        self.comboBoxRedundantDefaultSolver = Gui_PrefComboBox(TaskSketcherSolverAdvanced)
        self.comboBoxRedundantDefaultSolver.addItem("")
        self.comboBoxRedundantDefaultSolver.addItem("")
        self.comboBoxRedundantDefaultSolver.addItem("")
        self.comboBoxRedundantDefaultSolver.setObjectName(u"comboBoxRedundantDefaultSolver")
        self.comboBoxRedundantDefaultSolver.setProperty(u"prefEntry", u"RedundantDefaultSolver")
        self.comboBoxRedundantDefaultSolver.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_5.addWidget(self.comboBoxRedundantDefaultSolver)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelRedundantSolverMaxIterations = QLabel(TaskSketcherSolverAdvanced)
        self.labelRedundantSolverMaxIterations.setObjectName(u"labelRedundantSolverMaxIterations")

        self.horizontalLayout_6.addWidget(self.labelRedundantSolverMaxIterations)

        self.spinBoxRedundantSolverMaxIterations = Gui_PrefSpinBox(TaskSketcherSolverAdvanced)
        self.spinBoxRedundantSolverMaxIterations.setObjectName(u"spinBoxRedundantSolverMaxIterations")
        self.spinBoxRedundantSolverMaxIterations.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBoxRedundantSolverMaxIterations.setMaximum(999)
        self.spinBoxRedundantSolverMaxIterations.setValue(100)
        self.spinBoxRedundantSolverMaxIterations.setProperty(u"prefEntry", u"RedundantSolverMaxIterations")
        self.spinBoxRedundantSolverMaxIterations.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_6.addWidget(self.spinBoxRedundantSolverMaxIterations)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.labelRedundantSketchSizeMultiplier = QLabel(TaskSketcherSolverAdvanced)
        self.labelRedundantSketchSizeMultiplier.setObjectName(u"labelRedundantSketchSizeMultiplier")

        self.horizontalLayout_7.addWidget(self.labelRedundantSketchSizeMultiplier)

        self.checkBoxRedundantSketchSizeMultiplier = Gui_PrefCheckBox(TaskSketcherSolverAdvanced)
        self.checkBoxRedundantSketchSizeMultiplier.setObjectName(u"checkBoxRedundantSketchSizeMultiplier")
        self.checkBoxRedundantSketchSizeMultiplier.setLayoutDirection(Qt.RightToLeft)
        self.checkBoxRedundantSketchSizeMultiplier.setProperty(u"prefEntry", u"RedundantSketchSizeMultiplier")
        self.checkBoxRedundantSketchSizeMultiplier.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_7.addWidget(self.checkBoxRedundantSketchSizeMultiplier)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.labelRedundantConvergence = QLabel(TaskSketcherSolverAdvanced)
        self.labelRedundantConvergence.setObjectName(u"labelRedundantConvergence")

        self.horizontalLayout_13.addWidget(self.labelRedundantConvergence)

        self.lineEditRedundantConvergence = Gui_PrefLineEdit(TaskSketcherSolverAdvanced)
        self.lineEditRedundantConvergence.setObjectName(u"lineEditRedundantConvergence")
        self.lineEditRedundantConvergence.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEditRedundantConvergence.setProperty(u"prefEntry", u"RedundantConvergence")
        self.lineEditRedundantConvergence.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_13.addWidget(self.lineEditRedundantConvergence)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.labelRedundantSolverParam1 = QLabel(TaskSketcherSolverAdvanced)
        self.labelRedundantSolverParam1.setObjectName(u"labelRedundantSolverParam1")
        self.labelRedundantSolverParam1.setText(u"Redundant param1")

        self.horizontalLayout_14.addWidget(self.labelRedundantSolverParam1)

        self.lineEditRedundantSolverParam1 = Gui_PrefLineEdit(TaskSketcherSolverAdvanced)
        self.lineEditRedundantSolverParam1.setObjectName(u"lineEditRedundantSolverParam1")
        self.lineEditRedundantSolverParam1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEditRedundantSolverParam1.setProperty(u"prefEntry", u"param")
        self.lineEditRedundantSolverParam1.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_14.addWidget(self.lineEditRedundantSolverParam1)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.labelRedundantSolverParam2 = QLabel(TaskSketcherSolverAdvanced)
        self.labelRedundantSolverParam2.setObjectName(u"labelRedundantSolverParam2")
        self.labelRedundantSolverParam2.setText(u"Redundant param2")

        self.horizontalLayout_15.addWidget(self.labelRedundantSolverParam2)

        self.lineEditRedundantSolverParam2 = Gui_PrefLineEdit(TaskSketcherSolverAdvanced)
        self.lineEditRedundantSolverParam2.setObjectName(u"lineEditRedundantSolverParam2")
        self.lineEditRedundantSolverParam2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEditRedundantSolverParam2.setProperty(u"prefEntry", u"param")
        self.lineEditRedundantSolverParam2.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_15.addWidget(self.lineEditRedundantSolverParam2)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.labelRedundantSolverParam3 = QLabel(TaskSketcherSolverAdvanced)
        self.labelRedundantSolverParam3.setObjectName(u"labelRedundantSolverParam3")
        self.labelRedundantSolverParam3.setText(u"Redundant param3")

        self.horizontalLayout_16.addWidget(self.labelRedundantSolverParam3)

        self.lineEditRedundantSolverParam3 = Gui_PrefLineEdit(TaskSketcherSolverAdvanced)
        self.lineEditRedundantSolverParam3.setObjectName(u"lineEditRedundantSolverParam3")
        self.lineEditRedundantSolverParam3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEditRedundantSolverParam3.setProperty(u"prefEntry", u"param")
        self.lineEditRedundantSolverParam3.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_16.addWidget(self.lineEditRedundantSolverParam3)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.labelDebugMode = QLabel(TaskSketcherSolverAdvanced)
        self.labelDebugMode.setObjectName(u"labelDebugMode")

        self.horizontalLayout_8.addWidget(self.labelDebugMode)

        self.comboBoxDebugMode = Gui_PrefComboBox(TaskSketcherSolverAdvanced)
        self.comboBoxDebugMode.addItem("")
        self.comboBoxDebugMode.addItem("")
        self.comboBoxDebugMode.addItem("")
        self.comboBoxDebugMode.setObjectName(u"comboBoxDebugMode")
        self.comboBoxDebugMode.setProperty(u"prefEntry", u"DebugMode")
        self.comboBoxDebugMode.setProperty(u"prefPath", u"Mod/Sketcher/SolverAdvanced")

        self.horizontalLayout_8.addWidget(self.comboBoxDebugMode)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButtonSolve = QPushButton(TaskSketcherSolverAdvanced)
        self.pushButtonSolve.setObjectName(u"pushButtonSolve")

        self.horizontalLayout_17.addWidget(self.pushButtonSolve)

        self.pushButtonDefaults = QPushButton(TaskSketcherSolverAdvanced)
        self.pushButtonDefaults.setObjectName(u"pushButtonDefaults")

        self.horizontalLayout_17.addWidget(self.pushButtonDefaults)


        self.verticalLayout.addLayout(self.horizontalLayout_17)


        self.retranslateUi(TaskSketcherSolverAdvanced)

        self.comboBoxDefaultSolver.setCurrentIndex(2)
        self.comboBoxDogLegGaussStep.setCurrentIndex(0)
        self.comboBoxQRMethod.setCurrentIndex(1)
        self.comboBoxRedundantDefaultSolver.setCurrentIndex(2)
        self.comboBoxDebugMode.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(TaskSketcherSolverAdvanced)
    # setupUi

    def retranslateUi(self, TaskSketcherSolverAdvanced):
#if QT_CONFIG(tooltip)
        self.labelDefaultSolver.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Default algorithm used for solving the sketch", None))
#endif // QT_CONFIG(tooltip)
        self.labelDefaultSolver.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Default solver", None))
        self.comboBoxDefaultSolver.setItemText(0, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"BFGS", None))
        self.comboBoxDefaultSolver.setItemText(1, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"LevenbergMarquardt", None))
        self.comboBoxDefaultSolver.setItemText(2, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"DogLeg", None))

#if QT_CONFIG(tooltip)
        self.comboBoxDefaultSolver.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Solver used for solving the geometry.\n"
"LevenbergMarquardt and DogLeg are trust region optimization algorithms.\n"
"BFGS solver uses the Broyden\u2013Fletcher\u2013Goldfarb\u2013Shanno algorithm.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelDogLegGaussStep.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Type of function to apply in DogLeg for the Gauss step", None))
#endif // QT_CONFIG(tooltip)
        self.labelDogLegGaussStep.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"DogLeg Gauss step", None))
        self.comboBoxDogLegGaussStep.setItemText(0, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"FullPivLU", None))
        self.comboBoxDogLegGaussStep.setItemText(1, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"LeastNorm-FullPivLU", None))
        self.comboBoxDogLegGaussStep.setItemText(2, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"LeastNorm-LDLT", None))

#if QT_CONFIG(tooltip)
        self.comboBoxDogLegGaussStep.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Step type used in the DogLeg algorithm", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelMaxIter.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Maximum number of iterations of the default algorithm", None))
#endif // QT_CONFIG(tooltip)
        self.labelMaxIter.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Maximum iterations", None))
#if QT_CONFIG(tooltip)
        self.spinBoxMaxIter.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Maximum iterations to find convergence before solver is stopped", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelSketchSizeMultiplier.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Scales the maximum iteration count based on the sketch size", None))
#endif // QT_CONFIG(tooltip)
        self.labelSketchSizeMultiplier.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Sketch size multiplier", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSketchSizeMultiplier.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Scales the maximum iteration count based on the number of parameters", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSketchSizeMultiplier.setText("")
#if QT_CONFIG(tooltip)
        self.labelSolverConvergence.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Error threshold under which convergence is reached", None))
#endif // QT_CONFIG(tooltip)
        self.labelSolverConvergence.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Convergence", None))
#if QT_CONFIG(tooltip)
        self.lineEditConvergence.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Threshold for squared error that is used\n"
"to determine whether a solution converges or not", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelQRAlgorithm.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Algorithm used for the rank revealing QR decomposition", None))
#endif // QT_CONFIG(tooltip)
        self.labelQRAlgorithm.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"QR algorithm", None))
        self.comboBoxQRMethod.setItemText(0, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Eigen Dense QR", None))
        self.comboBoxQRMethod.setItemText(1, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Eigen Sparse QR", None))

#if QT_CONFIG(tooltip)
        self.comboBoxQRMethod.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"During diagnosing the QR rank of matrix is calculated.\n"
"Eigen Dense QR is a dense matrix QR with full pivoting; usually slower\n"
"Eigen Sparse QR algorithm is optimized for sparse matrices; usually faster", None))
#endif // QT_CONFIG(tooltip)
        self.labelPivotThreshold.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Pivot threshold", None))
#if QT_CONFIG(tooltip)
        self.lineEditQRPivotThreshold.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"During a QR, values under the pivot threshold are treated as zero", None))
#endif // QT_CONFIG(tooltip)
        self.lineEditQRPivotThreshold.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"1E-13", None))
#if QT_CONFIG(tooltip)
        self.labelRedundantSolver.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Solving algorithm used to detect redundant constraints", None))
#endif // QT_CONFIG(tooltip)
        self.labelRedundantSolver.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Redundant solver", None))
        self.comboBoxRedundantDefaultSolver.setItemText(0, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"BFGS", None))
        self.comboBoxRedundantDefaultSolver.setItemText(1, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"LevenbergMarquardt", None))
        self.comboBoxRedundantDefaultSolver.setItemText(2, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"DogLeg", None))

#if QT_CONFIG(tooltip)
        self.comboBoxRedundantDefaultSolver.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Solver used to determine whether a group is redundant or conflicting", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelRedundantSolverMaxIterations.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Maximum number of iterations of the solver used to detect redundant constraints", None))
#endif // QT_CONFIG(tooltip)
        self.labelRedundantSolverMaxIterations.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Maximum redundant solver iterations", None))
#if QT_CONFIG(tooltip)
        self.spinBoxRedundantSolverMaxIterations.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Same as 'Maximum iterations', but for redundant solving", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.labelRedundantSketchSizeMultiplier.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Multiplies the maximum iterations value for the redundant algorithm by the sketch size", None))
#endif // QT_CONFIG(tooltip)
        self.labelRedundantSketchSizeMultiplier.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Redundant sketch size multiplier", None))
#if QT_CONFIG(tooltip)
        self.checkBoxRedundantSketchSizeMultiplier.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Same as 'Sketch size multiplier', but for redundant solving", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxRedundantSketchSizeMultiplier.setText("")
#if QT_CONFIG(tooltip)
        self.labelRedundantConvergence.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Error threshold under which convergence is reached for the solving of redundant constraints", None))
#endif // QT_CONFIG(tooltip)
        self.labelRedundantConvergence.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Redundant convergence", None))
#if QT_CONFIG(tooltip)
        self.lineEditRedundantConvergence.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Same as 'Convergence', but for redundant solving", None))
#endif // QT_CONFIG(tooltip)
        self.lineEditRedundantConvergence.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"1E-10", None))
#if QT_CONFIG(tooltip)
        self.labelDebugMode.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Degree of verbosity of the debug output to the console", None))
#endif // QT_CONFIG(tooltip)
        self.labelDebugMode.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Console debug mode", None))
        self.comboBoxDebugMode.setItemText(0, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"None", None))
        self.comboBoxDebugMode.setItemText(1, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Minimum", None))
        self.comboBoxDebugMode.setItemText(2, QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Iteration level", None))

#if QT_CONFIG(tooltip)
        self.comboBoxDebugMode.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Verbosity of console output", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonSolve.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Solve", None))
#if QT_CONFIG(tooltip)
        self.pushButtonDefaults.setToolTip(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Resets all solver values to their default values", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonDefaults.setText(QCoreApplication.translate("TaskSketcherSolverAdvanced", u"Restore Defaults", None))
        pass
    # retranslateUi

