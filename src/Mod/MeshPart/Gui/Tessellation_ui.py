# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tessellation.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QWidget)

class Ui_MeshPartGui_Tessellation(object):
    def setupUi(self, MeshPartGui__Tessellation):
        if not MeshPartGui__Tessellation.objectName():
            MeshPartGui__Tessellation.setObjectName(u"MeshPartGui__Tessellation")
        MeshPartGui__Tessellation.resize(363, 508)
        self.gridLayout_7 = QGridLayout(MeshPartGui__Tessellation)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBoxMeshingOptions = QGroupBox(MeshPartGui__Tessellation)
        self.groupBoxMeshingOptions.setObjectName(u"groupBoxMeshingOptions")
        self.gridLayout_6 = QGridLayout(self.groupBoxMeshingOptions)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.stackedWidget = QTabWidget(self.groupBoxMeshingOptions)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageStandard = QWidget()
        self.pageStandard.setObjectName(u"pageStandard")
        self.gridLayout_3 = QGridLayout(self.pageStandard)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelSurfaceDeviation = QLabel(self.pageStandard)
        self.labelSurfaceDeviation.setObjectName(u"labelSurfaceDeviation")

        self.gridLayout.addWidget(self.labelSurfaceDeviation, 0, 0, 1, 1)

        self.spinSurfaceDeviation = Gui_QuantitySpinBox(self.pageStandard)
        self.spinSurfaceDeviation.setObjectName(u"spinSurfaceDeviation")
        self.spinSurfaceDeviation.setProperty(u"unit", u"mm")
        self.spinSurfaceDeviation.setMinimum(0.001000000000000)
        self.spinSurfaceDeviation.setSingleStep(0.100000000000000)
        self.spinSurfaceDeviation.setValue(0.100000000000000)

        self.gridLayout.addWidget(self.spinSurfaceDeviation, 0, 1, 1, 1)

        self.labelAngularDeviation = QLabel(self.pageStandard)
        self.labelAngularDeviation.setObjectName(u"labelAngularDeviation")

        self.gridLayout.addWidget(self.labelAngularDeviation, 1, 0, 1, 1)

        self.spinAngularDeviation = Gui_QuantitySpinBox(self.pageStandard)
        self.spinAngularDeviation.setObjectName(u"spinAngularDeviation")
        self.spinAngularDeviation.setProperty(u"unit", u"deg")
        self.spinAngularDeviation.setMinimum(1.000000000000000)
        self.spinAngularDeviation.setMaximum(180.000000000000000)
        self.spinAngularDeviation.setSingleStep(5.000000000000000)
        self.spinAngularDeviation.setValue(30.000000000000000)

        self.gridLayout.addWidget(self.spinAngularDeviation, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.relativeDeviation = QCheckBox(self.pageStandard)
        self.relativeDeviation.setObjectName(u"relativeDeviation")

        self.gridLayout_3.addWidget(self.relativeDeviation, 1, 0, 1, 1)

        self.meshShapeColors = QCheckBox(self.pageStandard)
        self.meshShapeColors.setObjectName(u"meshShapeColors")

        self.gridLayout_3.addWidget(self.meshShapeColors, 2, 0, 1, 1)

        self.groupsFaceColors = QCheckBox(self.pageStandard)
        self.groupsFaceColors.setObjectName(u"groupsFaceColors")

        self.gridLayout_3.addWidget(self.groupsFaceColors, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 189, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.stackedWidget.addTab(self.pageStandard, "")
        self.pageMefisto = QWidget()
        self.pageMefisto.setObjectName(u"pageMefisto")
        self.gridLayout_9 = QGridLayout(self.pageMefisto)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkMaximumEdgeLength = QCheckBox(self.pageMefisto)
        self.checkMaximumEdgeLength.setObjectName(u"checkMaximumEdgeLength")
        self.checkMaximumEdgeLength.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkMaximumEdgeLength)

        self.spinMaximumEdgeLength = Gui_QuantitySpinBox(self.pageMefisto)
        self.spinMaximumEdgeLength.setObjectName(u"spinMaximumEdgeLength")
        self.spinMaximumEdgeLength.setProperty(u"unit", u"mm")
        self.spinMaximumEdgeLength.setSingleStep(0.100000000000000)
        self.spinMaximumEdgeLength.setValue(1.000000000000000)

        self.horizontalLayout_2.addWidget(self.spinMaximumEdgeLength)

        self.estimateMaximumEdgeLength = QPushButton(self.pageMefisto)
        self.estimateMaximumEdgeLength.setObjectName(u"estimateMaximumEdgeLength")

        self.horizontalLayout_2.addWidget(self.estimateMaximumEdgeLength)


        self.gridLayout_9.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 189, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.stackedWidget.addTab(self.pageMefisto, "")
        self.pageNetgen = QWidget()
        self.pageNetgen.setObjectName(u"pageNetgen")
        self.gridLayout_5 = QGridLayout(self.pageNetgen)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelFineness = QLabel(self.pageNetgen)
        self.labelFineness.setObjectName(u"labelFineness")

        self.gridLayout_4.addWidget(self.labelFineness, 0, 0, 1, 1)

        self.comboFineness = QComboBox(self.pageNetgen)
        self.comboFineness.addItem("")
        self.comboFineness.addItem("")
        self.comboFineness.addItem("")
        self.comboFineness.addItem("")
        self.comboFineness.addItem("")
        self.comboFineness.addItem("")
        self.comboFineness.setObjectName(u"comboFineness")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboFineness.sizePolicy().hasHeightForWidth())
        self.comboFineness.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.comboFineness, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelGrading = QLabel(self.pageNetgen)
        self.labelGrading.setObjectName(u"labelGrading")

        self.gridLayout_2.addWidget(self.labelGrading, 0, 0, 1, 1)

        self.doubleGrading = QDoubleSpinBox(self.pageNetgen)
        self.doubleGrading.setObjectName(u"doubleGrading")
        self.doubleGrading.setEnabled(False)
        self.doubleGrading.setDecimals(1)
        self.doubleGrading.setMinimum(0.100000000000000)
        self.doubleGrading.setMaximum(1.000000000000000)
        self.doubleGrading.setSingleStep(0.100000000000000)
        self.doubleGrading.setValue(0.300000000000000)

        self.gridLayout_2.addWidget(self.doubleGrading, 0, 1, 1, 1)

        self.labelEdgeElements = QLabel(self.pageNetgen)
        self.labelEdgeElements.setObjectName(u"labelEdgeElements")

        self.gridLayout_2.addWidget(self.labelEdgeElements, 1, 0, 1, 1)

        self.spinEdgeElements = QDoubleSpinBox(self.pageNetgen)
        self.spinEdgeElements.setObjectName(u"spinEdgeElements")
        self.spinEdgeElements.setEnabled(False)
        self.spinEdgeElements.setDecimals(1)
        self.spinEdgeElements.setMinimum(0.200000000000000)
        self.spinEdgeElements.setMaximum(10.000000000000000)
        self.spinEdgeElements.setSingleStep(0.100000000000000)
        self.spinEdgeElements.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.spinEdgeElements, 1, 1, 1, 1)

        self.labelCurvatureElements = QLabel(self.pageNetgen)
        self.labelCurvatureElements.setObjectName(u"labelCurvatureElements")

        self.gridLayout_2.addWidget(self.labelCurvatureElements, 2, 0, 1, 1)

        self.spinCurvatureElements = QDoubleSpinBox(self.pageNetgen)
        self.spinCurvatureElements.setObjectName(u"spinCurvatureElements")
        self.spinCurvatureElements.setEnabled(False)
        self.spinCurvatureElements.setDecimals(1)
        self.spinCurvatureElements.setMinimum(0.200000000000000)
        self.spinCurvatureElements.setMaximum(10.000000000000000)
        self.spinCurvatureElements.setSingleStep(0.100000000000000)
        self.spinCurvatureElements.setValue(2.000000000000000)

        self.gridLayout_2.addWidget(self.spinCurvatureElements, 2, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 1, 1, 1)

        self.checkOptimizeSurface = QCheckBox(self.pageNetgen)
        self.checkOptimizeSurface.setObjectName(u"checkOptimizeSurface")
        self.checkOptimizeSurface.setChecked(True)

        self.gridLayout_4.addWidget(self.checkOptimizeSurface, 2, 0, 1, 2)

        self.checkSecondOrder = QCheckBox(self.pageNetgen)
        self.checkSecondOrder.setObjectName(u"checkSecondOrder")

        self.gridLayout_4.addWidget(self.checkSecondOrder, 3, 0, 1, 2)

        self.checkQuadDominated = QCheckBox(self.pageNetgen)
        self.checkQuadDominated.setObjectName(u"checkQuadDominated")

        self.gridLayout_4.addWidget(self.checkQuadDominated, 4, 0, 1, 2)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.stackedWidget.addTab(self.pageNetgen, "")

        self.gridLayout_6.addWidget(self.stackedWidget, 0, 0, 1, 3)

        self.checkBoxDontQuit = QCheckBox(self.groupBoxMeshingOptions)
        self.checkBoxDontQuit.setObjectName(u"checkBoxDontQuit")

        self.gridLayout_6.addWidget(self.checkBoxDontQuit, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBoxMeshingOptions, 0, 0, 1, 1)


        self.retranslateUi(MeshPartGui__Tessellation)
        self.checkMaximumEdgeLength.toggled.connect(self.spinMaximumEdgeLength.setEnabled)

        self.stackedWidget.setCurrentIndex(0)
        self.comboFineness.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MeshPartGui__Tessellation)
    # setupUi

    def retranslateUi(self, MeshPartGui__Tessellation):
        MeshPartGui__Tessellation.setWindowTitle(QCoreApplication.translate("MeshPartGui::Tessellation", u"Tessellation", None))
        self.groupBoxMeshingOptions.setTitle(QCoreApplication.translate("MeshPartGui::Tessellation", u"Meshing Options", None))
        self.labelSurfaceDeviation.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Surface deviation", None))
#if QT_CONFIG(tooltip)
        self.spinSurfaceDeviation.setToolTip(QCoreApplication.translate("MeshPartGui::Tessellation", u"Maximal linear deflection of a mesh section from the surface of the object", None))
#endif // QT_CONFIG(tooltip)
        self.labelAngularDeviation.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Angular deviation", None))
#if QT_CONFIG(tooltip)
        self.spinAngularDeviation.setToolTip(QCoreApplication.translate("MeshPartGui::Tessellation", u"Maximal angular deflection of a mesh section to the next section", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.relativeDeviation.setToolTip(QCoreApplication.translate("MeshPartGui::Tessellation", u"The maximal linear deviation of a mesh segment will be the specified\n"
"surface deviation multiplied by the length of the current mesh segment (edge)", None))
#endif // QT_CONFIG(tooltip)
        self.relativeDeviation.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Relative surface deviation", None))
#if QT_CONFIG(tooltip)
        self.meshShapeColors.setToolTip(QCoreApplication.translate("MeshPartGui::Tessellation", u"Mesh will get face colors of the object", None))
#endif // QT_CONFIG(tooltip)
        self.meshShapeColors.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Apply face colors to mesh", None))
#if QT_CONFIG(tooltip)
        self.groupsFaceColors.setToolTip(QCoreApplication.translate("MeshPartGui::Tessellation", u"Mesh segments will be grouped according to the color of the object faces.\n"
"These groups will be exported for mesh output formats supporting\n"
"this feature (e.g. the format OBJ).", None))
#endif // QT_CONFIG(tooltip)
        self.groupsFaceColors.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Define segments by face colors", None))
        self.stackedWidget.setTabText(self.stackedWidget.indexOf(self.pageStandard), QCoreApplication.translate("MeshPartGui::Tessellation", u"Standard", None))
#if QT_CONFIG(tooltip)
        self.stackedWidget.setTabToolTip(self.stackedWidget.indexOf(self.pageStandard), QCoreApplication.translate("MeshPartGui::Tessellation", u"Use the standard mesher", None))
#endif // QT_CONFIG(tooltip)
        self.checkMaximumEdgeLength.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Maximum edge length", None))
#if QT_CONFIG(tooltip)
        self.checkMaximumEdgeLength.setToolTip(QCoreApplication.translate("MeshPartGui::Tessellation", u"If this number is smaller the mesh becomes finer.\n"
"The smallest value is 0.", None))
#endif // QT_CONFIG(tooltip)
        self.estimateMaximumEdgeLength.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Estimate", None))
        self.stackedWidget.setTabText(self.stackedWidget.indexOf(self.pageMefisto), QCoreApplication.translate("MeshPartGui::Tessellation", u"Mefisto", None))
#if QT_CONFIG(tooltip)
        self.stackedWidget.setTabToolTip(self.stackedWidget.indexOf(self.pageMefisto), QCoreApplication.translate("MeshPartGui::Tessellation", u"Use the Mefisto mesher", None))
#endif // QT_CONFIG(tooltip)
        self.labelFineness.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Fineness:", None))
        self.comboFineness.setItemText(0, QCoreApplication.translate("MeshPartGui::Tessellation", u"Very coarse", None))
        self.comboFineness.setItemText(1, QCoreApplication.translate("MeshPartGui::Tessellation", u"Coarse", None))
        self.comboFineness.setItemText(2, QCoreApplication.translate("MeshPartGui::Tessellation", u"Moderate", None))
        self.comboFineness.setItemText(3, QCoreApplication.translate("MeshPartGui::Tessellation", u"Fine", None))
        self.comboFineness.setItemText(4, QCoreApplication.translate("MeshPartGui::Tessellation", u"Very fine", None))
        self.comboFineness.setItemText(5, QCoreApplication.translate("MeshPartGui::Tessellation", u"User defined", None))

        self.labelGrading.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Mesh size grading", None))
#if QT_CONFIG(tooltip)
        self.doubleGrading.setToolTip(QCoreApplication.translate("MeshPartGui::Tessellation", u"If this parameter is smaller, the mesh becomes finer.\n"
"A value in the range of 0.1-1.", None))
#endif // QT_CONFIG(tooltip)
        self.labelEdgeElements.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Elements per edge", None))
#if QT_CONFIG(tooltip)
        self.spinEdgeElements.setToolTip(QCoreApplication.translate("MeshPartGui::Tessellation", u"If this parameter is larger, the mesh becomes finer.\n"
"A value in the range of 0.2-10.", None))
#endif // QT_CONFIG(tooltip)
        self.labelCurvatureElements.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Elements per curvature radius", None))
#if QT_CONFIG(tooltip)
        self.spinCurvatureElements.setToolTip(QCoreApplication.translate("MeshPartGui::Tessellation", u"If this parameter is larger, the mesh becomes finer.\n"
"A value in the range of 0.2-10.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkOptimizeSurface.setToolTip(QCoreApplication.translate("MeshPartGui::Tessellation", u"Whether optimization of surface shape will be done", None))
#endif // QT_CONFIG(tooltip)
        self.checkOptimizeSurface.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Optimize surface", None))
#if QT_CONFIG(tooltip)
        self.checkSecondOrder.setToolTip(QCoreApplication.translate("MeshPartGui::Tessellation", u"Whether second order elements will be generated", None))
#endif // QT_CONFIG(tooltip)
        self.checkSecondOrder.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Second order elements", None))
#if QT_CONFIG(tooltip)
        self.checkQuadDominated.setToolTip(QCoreApplication.translate("MeshPartGui::Tessellation", u"Whether meshes will be arranged preferably using quadrilateral faces", None))
#endif // QT_CONFIG(tooltip)
        self.checkQuadDominated.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Quad dominated", None))
        self.stackedWidget.setTabText(self.stackedWidget.indexOf(self.pageNetgen), QCoreApplication.translate("MeshPartGui::Tessellation", u"Netgen", None))
#if QT_CONFIG(tooltip)
        self.stackedWidget.setTabToolTip(self.stackedWidget.indexOf(self.pageNetgen), QCoreApplication.translate("MeshPartGui::Tessellation", u"Use the Netgen mesher", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxDontQuit.setText(QCoreApplication.translate("MeshPartGui::Tessellation", u"Leave panel open", None))
    # retranslateUi

