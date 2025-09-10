# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettings3DView.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettings3DView(object):
    def setupUi(self, Gui__Dialog__DlgSettings3DView):
        if not Gui__Dialog__DlgSettings3DView.objectName():
            Gui__Dialog__DlgSettings3DView.setObjectName(u"Gui__Dialog__DlgSettings3DView")
        Gui__Dialog__DlgSettings3DView.resize(499, 600)
        self.verticalLayout_2 = QVBoxLayout(Gui__Dialog__DlgSettings3DView)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.GroupBoxGeneral = QGroupBox(Gui__Dialog__DlgSettings3DView)
        self.GroupBoxGeneral.setObjectName(u"GroupBoxGeneral")
        self.GroupBoxGeneral.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.GroupBoxGeneral)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayoutCoord = QGridLayout()
        self.gridLayoutCoord.setSpacing(6)
        self.gridLayoutCoord.setObjectName(u"gridLayoutCoord")
        self.CheckBox_CornerCoordSystem = Gui_PrefCheckBox(self.GroupBoxGeneral)
        self.CheckBox_CornerCoordSystem.setObjectName(u"CheckBox_CornerCoordSystem")
        self.CheckBox_CornerCoordSystem.setChecked(True)
        self.CheckBox_CornerCoordSystem.setProperty(u"prefEntry", u"CornerCoordSystem")
        self.CheckBox_CornerCoordSystem.setProperty(u"prefPath", u"View")

        self.gridLayoutCoord.addWidget(self.CheckBox_CornerCoordSystem, 0, 0, 1, 1)

        self.horizontalSpacerCoord = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutCoord.addItem(self.horizontalSpacerCoord, 0, 1, 1, 1)

        self.labelCoordSize = QLabel(self.GroupBoxGeneral)
        self.labelCoordSize.setObjectName(u"labelCoordSize")
        self.labelCoordSize.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayoutCoord.addWidget(self.labelCoordSize, 0, 2, 1, 1)

        self.SpinBox_CornerCoordSystemSize = Gui_PrefSpinBox(self.GroupBoxGeneral)
        self.SpinBox_CornerCoordSystemSize.setObjectName(u"SpinBox_CornerCoordSystemSize")
        self.SpinBox_CornerCoordSystemSize.setSuffix(u"%")
        self.SpinBox_CornerCoordSystemSize.setMinimum(2)
        self.SpinBox_CornerCoordSystemSize.setMaximum(100)
        self.SpinBox_CornerCoordSystemSize.setValue(10)
        self.SpinBox_CornerCoordSystemSize.setProperty(u"prefEntry", u"CornerCoordSystemSize")
        self.SpinBox_CornerCoordSystemSize.setProperty(u"prefPath", u"View")

        self.gridLayoutCoord.addWidget(self.SpinBox_CornerCoordSystemSize, 0, 3, 1, 1)

        self.axisLetterColorLabel = QLabel(self.GroupBoxGeneral)
        self.axisLetterColorLabel.setObjectName(u"axisLetterColorLabel")

        self.gridLayoutCoord.addWidget(self.axisLetterColorLabel, 1, 2, 1, 1)

        self.axisLetterColor = Gui_PrefColorButton(self.GroupBoxGeneral)
        self.axisLetterColor.setObjectName(u"axisLetterColor")
        self.axisLetterColor.setColor(QColor(0, 0, 0))
        self.axisLetterColor.setProperty(u"prefEntry", u"AxisLetterColor")
        self.axisLetterColor.setProperty(u"prefPath", u"View")

        self.gridLayoutCoord.addWidget(self.axisLetterColor, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayoutCoord)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.xAxisLabel = QLabel(self.GroupBoxGeneral)
        self.xAxisLabel.setObjectName(u"xAxisLabel")

        self.horizontalLayout_2.addWidget(self.xAxisLabel)

        self.xAxisColor = Gui_PrefColorButton(self.GroupBoxGeneral)
        self.xAxisColor.setObjectName(u"xAxisColor")
        self.xAxisColor.setProperty(u"prefEntry", u"AxisXColor")
        self.xAxisColor.setProperty(u"prefPath", u"View")
        self.xAxisColor.setProperty(u"color", QColor(204, 51, 51))

        self.horizontalLayout_2.addWidget(self.xAxisColor)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.yAxisLabel = QLabel(self.GroupBoxGeneral)
        self.yAxisLabel.setObjectName(u"yAxisLabel")

        self.horizontalLayout_2.addWidget(self.yAxisLabel)

        self.yAxisColor = Gui_PrefColorButton(self.GroupBoxGeneral)
        self.yAxisColor.setObjectName(u"yAxisColor")
        self.yAxisColor.setProperty(u"prefEntry", u"AxisYColor")
        self.yAxisColor.setProperty(u"prefPath", u"View")
        self.yAxisColor.setProperty(u"color", QColor(51, 204, 51))

        self.horizontalLayout_2.addWidget(self.yAxisColor)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.zAxisLabel = QLabel(self.GroupBoxGeneral)
        self.zAxisLabel.setObjectName(u"zAxisLabel")

        self.horizontalLayout_2.addWidget(self.zAxisLabel)

        self.zAxisColor = Gui_PrefColorButton(self.GroupBoxGeneral)
        self.zAxisColor.setObjectName(u"zAxisColor")
        self.zAxisColor.setProperty(u"prefEntry", u"AxisZColor")
        self.zAxisColor.setProperty(u"prefPath", u"View")
        self.zAxisColor.setProperty(u"color", QColor(51, 51, 204))

        self.horizontalLayout_2.addWidget(self.zAxisColor)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.CheckBox_ShowAxisCross = Gui_PrefCheckBox(self.GroupBoxGeneral)
        self.CheckBox_ShowAxisCross.setObjectName(u"CheckBox_ShowAxisCross")
        self.CheckBox_ShowAxisCross.setProperty(u"prefEntry", u"ShowAxisCross")
        self.CheckBox_ShowAxisCross.setProperty(u"prefPath", u"View")

        self.verticalLayout.addWidget(self.CheckBox_ShowAxisCross)

        self.CheckBox_ShowFPS = Gui_PrefCheckBox(self.GroupBoxGeneral)
        self.CheckBox_ShowFPS.setObjectName(u"CheckBox_ShowFPS")
        self.CheckBox_ShowFPS.setProperty(u"prefEntry", u"ShowFPS")
        self.CheckBox_ShowFPS.setProperty(u"prefPath", u"View")

        self.verticalLayout.addWidget(self.CheckBox_ShowFPS)


        self.verticalLayout_2.addWidget(self.GroupBoxGeneral)

        self.GroupBox12 = QGroupBox(Gui__Dialog__DlgSettings3DView)
        self.GroupBox12.setObjectName(u"GroupBox12")
        self.GroupBox12.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.GroupBox12)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.CheckBox_use_SW_OpenGL = Gui_PrefCheckBox(self.GroupBox12)
        self.CheckBox_use_SW_OpenGL.setObjectName(u"CheckBox_use_SW_OpenGL")
        self.CheckBox_use_SW_OpenGL.setProperty(u"prefEntry", u"UseSoftwareOpenGL")
        self.CheckBox_use_SW_OpenGL.setProperty(u"prefPath", u"OpenGL")

        self.verticalLayout_3.addWidget(self.CheckBox_use_SW_OpenGL)

        self.CheckBox_useVBO = Gui_PrefCheckBox(self.GroupBox12)
        self.CheckBox_useVBO.setObjectName(u"CheckBox_useVBO")
        self.CheckBox_useVBO.setProperty(u"prefEntry", u"UseVBO")
        self.CheckBox_useVBO.setProperty(u"prefPath", u"View")

        self.verticalLayout_3.addWidget(self.CheckBox_useVBO)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboAliasing = QComboBox(self.GroupBox12)
        self.comboAliasing.setObjectName(u"comboAliasing")
        self.comboAliasing.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.comboAliasing, 1, 1, 1, 1)

        self.markerSizeLabel = QLabel(self.GroupBox12)
        self.markerSizeLabel.setObjectName(u"markerSizeLabel")

        self.gridLayout.addWidget(self.markerSizeLabel, 3, 0, 1, 1)

        self.aliasingLAbel = QLabel(self.GroupBox12)
        self.aliasingLAbel.setObjectName(u"aliasingLAbel")

        self.gridLayout.addWidget(self.aliasingLAbel, 1, 0, 1, 1)

        self.transparentRenderLabel = QLabel(self.GroupBox12)
        self.transparentRenderLabel.setObjectName(u"transparentRenderLabel")

        self.gridLayout.addWidget(self.transparentRenderLabel, 2, 0, 1, 1)

        self.comboTransparentRender = Gui_PrefComboBox(self.GroupBox12)
        self.comboTransparentRender.addItem("")
        self.comboTransparentRender.addItem("")
        self.comboTransparentRender.setObjectName(u"comboTransparentRender")
        self.comboTransparentRender.setMinimumSize(QSize(120, 0))
        self.comboTransparentRender.setProperty(u"prefEntry", u"TransparentObjectRenderType")
        self.comboTransparentRender.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.comboTransparentRender, 2, 1, 1, 1)

        self.renderCache = QComboBox(self.GroupBox12)
        self.renderCache.addItem("")
        self.renderCache.addItem("")
        self.renderCache.addItem("")
        self.renderCache.setObjectName(u"renderCache")
        self.renderCache.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.renderCache, 0, 1, 1, 1)

        self.renderCacheLabel = QLabel(self.GroupBox12)
        self.renderCacheLabel.setObjectName(u"renderCacheLabel")

        self.gridLayout.addWidget(self.renderCacheLabel, 0, 0, 1, 1)

        self.textLabel1 = QLabel(self.GroupBox12)
        self.textLabel1.setObjectName(u"textLabel1")

        self.gridLayout.addWidget(self.textLabel1, 4, 0, 1, 1)

        self.boxMarkerSize = QComboBox(self.GroupBox12)
        self.boxMarkerSize.setObjectName(u"boxMarkerSize")
        self.boxMarkerSize.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.boxMarkerSize, 3, 1, 1, 1)

        self.FloatSpinBox_EyeDistance = Gui_PrefDoubleSpinBox(self.GroupBox12)
        self.FloatSpinBox_EyeDistance.setObjectName(u"FloatSpinBox_EyeDistance")
        self.FloatSpinBox_EyeDistance.setMinimumSize(QSize(120, 0))
        self.FloatSpinBox_EyeDistance.setDecimals(1)
        self.FloatSpinBox_EyeDistance.setMinimum(0.100000000000000)
        self.FloatSpinBox_EyeDistance.setMaximum(1000.000000000000000)
        self.FloatSpinBox_EyeDistance.setSingleStep(2.000000000000000)
        self.FloatSpinBox_EyeDistance.setValue(5.000000000000000)
        self.FloatSpinBox_EyeDistance.setProperty(u"prefEntry", u"EyeDistance")
        self.FloatSpinBox_EyeDistance.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.FloatSpinBox_EyeDistance, 4, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.GroupBox12)

        self.groupBoxCamera = QGroupBox(Gui__Dialog__DlgSettings3DView)
        self.groupBoxCamera.setObjectName(u"groupBoxCamera")
        self.gridLayout1 = QGridLayout(self.groupBoxCamera)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.radioPerspective = Gui_PrefRadioButton(self.groupBoxCamera)
        self.radioPerspective.setObjectName(u"radioPerspective")
        self.radioPerspective.setProperty(u"prefEntry", u"Perspective")
        self.radioPerspective.setProperty(u"prefPath", u"View")

        self.gridLayout1.addWidget(self.radioPerspective, 0, 0, 1, 1)

        self.radioOrthographic = Gui_PrefRadioButton(self.groupBoxCamera)
        self.radioOrthographic.setObjectName(u"radioOrthographic")
        self.radioOrthographic.setChecked(True)
        self.radioOrthographic.setProperty(u"prefEntry", u"Orthographic")
        self.radioOrthographic.setProperty(u"prefPath", u"View")

        self.gridLayout1.addWidget(self.radioOrthographic, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBoxCamera)

        self.spacerItem = QSpacerItem(455, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.spacerItem)


        self.retranslateUi(Gui__Dialog__DlgSettings3DView)
        self.CheckBox_CornerCoordSystem.toggled.connect(self.SpinBox_CornerCoordSystemSize.setEnabled)
        self.CheckBox_CornerCoordSystem.toggled.connect(self.axisLetterColor.setEnabled)

        self.renderCache.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettings3DView)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettings3DView):
        Gui__Dialog__DlgSettings3DView.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"3D View", None))
        self.GroupBoxGeneral.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"General", None))
#if QT_CONFIG(tooltip)
        self.CheckBox_CornerCoordSystem.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Main coordinate system will always be shown in\n"
"lower right corner within opened files", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox_CornerCoordSystem.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Show coordinate system in the corner", None))
        self.labelCoordSize.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Relative size:", None))
#if QT_CONFIG(tooltip)
        self.SpinBox_CornerCoordSystemSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Size of main coordinate system representation\n"
"in the corner -- in % of height/width of viewport", None))
#endif // QT_CONFIG(tooltip)
        self.axisLetterColorLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Letter color:", None))
#if QT_CONFIG(tooltip)
        self.axisLetterColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Axis letter and FPS counter color", None))
#endif // QT_CONFIG(tooltip)
        self.xAxisLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"X-axis color", None))
        self.xAxisColor.setText("")
        self.yAxisLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Y-axis color", None))
        self.yAxisColor.setText("")
        self.zAxisLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Z-axis color", None))
        self.zAxisColor.setText("")
#if QT_CONFIG(tooltip)
        self.CheckBox_ShowAxisCross.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Axis cross will be shown by default at file\n"
"opening or creation", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox_ShowAxisCross.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Show axis cross by default", None))
#if QT_CONFIG(tooltip)
        self.CheckBox_ShowFPS.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Time needed for last operation and resulting frame rate\n"
"will be shown at the lower left corner in opened files", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox_ShowFPS.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Show counter of frames per second", None))
        self.GroupBox12.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Rendering", None))
#if QT_CONFIG(tooltip)
        self.CheckBox_use_SW_OpenGL.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"This option is useful for troubleshooting graphics card and driver problems.\n"
"\n"
"Changing this option requires a restart of the application.", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox_use_SW_OpenGL.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Use software OpenGL", None))
#if QT_CONFIG(tooltip)
        self.CheckBox_useVBO.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"If selected, Vertex Buffer Objects (VBO) will be used.\n"
"A VBO is an OpenGL feature that provides methods for uploading\n"
"vertex data (position, normal vector, color, etc.) to the graphics card.\n"
"VBOs offer substantial performance gains because the data resides\n"
"in the graphics memory rather than the system memory and so it\n"
"can be rendered directly by GPU.\n"
"\n"
"Note: Sometimes this feature may lead to a host of different\n"
"issues ranging from graphical anomalies to GPU crash bugs. Remember to\n"
"report this setting as enabled when seeking support on the FreeCAD forums", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox_useVBO.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Use OpenGL VBO (Vertex Buffer Object)", None))
#if QT_CONFIG(tooltip)
        self.comboAliasing.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"What kind of multisample anti-aliasing is used", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.markerSizeLabel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.markerSizeLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Marker size:", None))
        self.aliasingLAbel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Anti-Aliasing", None))
#if QT_CONFIG(tooltip)
        self.transparentRenderLabel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.transparentRenderLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Transparent objects:", None))
        self.comboTransparentRender.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"One pass", None))
        self.comboTransparentRender.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Backface pass", None))

#if QT_CONFIG(tooltip)
        self.comboTransparentRender.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Render types of transparent objects", None))
#endif // QT_CONFIG(tooltip)
        self.renderCache.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Auto", None))
        self.renderCache.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Distributed", None))
        self.renderCache.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Centralized", None))

#if QT_CONFIG(tooltip)
        self.renderCache.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"'Render Caching' is another way to say 'Rendering Acceleration'.\n"
"There are 3 options available to achieve this:\n"
"1) 'Auto' (default), let Coin3D decide where to cache.\n"
"2) 'Distributed', manually turn on cache for all view provider root node.\n"
"3) 'Centralized', manually turn off cache in all nodes of all view provider, and\n"
"only cache at the scene graph root node. This offers the fastest rendering speed\n"
"but slower response to any scene changes.", None))
#endif // QT_CONFIG(tooltip)
        self.renderCacheLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Render cache", None))
        self.textLabel1.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Eye to eye distance for stereo modes", None))
#if QT_CONFIG(tooltip)
        self.boxMarkerSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Size of vertices in the Sketcher, TechDraw and other workbenches", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.FloatSpinBox_EyeDistance.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Eye-to-eye distance used for stereo projections.\n"
"The specified value is a factor that will be multiplied with the\n"
"bounding box size of the 3D object that is currently displayed.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBoxCamera.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Camera type", None))
#if QT_CONFIG(tooltip)
        self.radioPerspective.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Objects will appear in a perspective projection", None))
#endif // QT_CONFIG(tooltip)
        self.radioPerspective.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Perspective renderin&g", None))
#if QT_CONFIG(tooltip)
        self.radioOrthographic.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Objects will be projected in orthographic projection", None))
#endif // QT_CONFIG(tooltip)
        self.radioOrthographic.setText(QCoreApplication.translate("Gui::Dialog::DlgSettings3DView", u"Or&thographic rendering", None))
    # retranslateUi

