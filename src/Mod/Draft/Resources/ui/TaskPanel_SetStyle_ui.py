# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskPanel_SetStyle.ui'
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
    QFontComboBox, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(290, 968)
        self.verticalLayout_1 = QVBoxLayout(Form)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.comboPresets = QComboBox(Form)
        self.comboPresets.addItem("")
        self.comboPresets.setObjectName(u"comboPresets")

        self.horizontalLayout_1.addWidget(self.comboPresets)

        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMaximumSize(QSize(32, 16777215))
        icon = QIcon()
        iconThemeName = u"gtk-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.saveButton.setIcon(icon)

        self.horizontalLayout_1.addWidget(self.saveButton)


        self.verticalLayout_1.addLayout(self.horizontalLayout_1)

        self.tabs = QTabWidget(Form)
        self.tabs.setObjectName(u"tabs")
        self.tab_Shape = QWidget()
        self.tab_Shape.setObjectName(u"tab_Shape")
        self.verticalLayout_2 = QVBoxLayout(self.tab_Shape)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_1 = QGroupBox(self.tab_Shape)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.gridLayout_1 = QGridLayout(self.groupBox_1)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.label_ShapeColor = QLabel(self.groupBox_1)
        self.label_ShapeColor.setObjectName(u"label_ShapeColor")

        self.gridLayout_1.addWidget(self.label_ShapeColor, 0, 0, 1, 1)

        self.ShapeColor = Gui_ColorButton(self.groupBox_1)
        self.ShapeColor.setObjectName(u"ShapeColor")

        self.gridLayout_1.addWidget(self.ShapeColor, 0, 1, 1, 1)

        self.label_AmbientColor = QLabel(self.groupBox_1)
        self.label_AmbientColor.setObjectName(u"label_AmbientColor")

        self.gridLayout_1.addWidget(self.label_AmbientColor, 1, 0, 1, 1)

        self.AmbientColor = Gui_ColorButton(self.groupBox_1)
        self.AmbientColor.setObjectName(u"AmbientColor")

        self.gridLayout_1.addWidget(self.AmbientColor, 1, 1, 1, 1)

        self.label_EmissiveColor = QLabel(self.groupBox_1)
        self.label_EmissiveColor.setObjectName(u"label_EmissiveColor")

        self.gridLayout_1.addWidget(self.label_EmissiveColor, 2, 0, 1, 1)

        self.EmissiveColor = Gui_ColorButton(self.groupBox_1)
        self.EmissiveColor.setObjectName(u"EmissiveColor")

        self.gridLayout_1.addWidget(self.EmissiveColor, 2, 1, 1, 1)

        self.label_SpecularColor = QLabel(self.groupBox_1)
        self.label_SpecularColor.setObjectName(u"label_SpecularColor")

        self.gridLayout_1.addWidget(self.label_SpecularColor, 3, 0, 1, 1)

        self.SpecularColor = Gui_ColorButton(self.groupBox_1)
        self.SpecularColor.setObjectName(u"SpecularColor")

        self.gridLayout_1.addWidget(self.SpecularColor, 3, 1, 1, 1)

        self.label_Transparency = QLabel(self.groupBox_1)
        self.label_Transparency.setObjectName(u"label_Transparency")

        self.gridLayout_1.addWidget(self.label_Transparency, 4, 0, 1, 1)

        self.Transparency = QSpinBox(self.groupBox_1)
        self.Transparency.setObjectName(u"Transparency")
        self.Transparency.setSuffix(u" %")
        self.Transparency.setMaximum(100)

        self.gridLayout_1.addWidget(self.Transparency, 4, 1, 1, 1)

        self.label_Shininess = QLabel(self.groupBox_1)
        self.label_Shininess.setObjectName(u"label_Shininess")

        self.gridLayout_1.addWidget(self.label_Shininess, 5, 0, 1, 1)

        self.Shininess = QSpinBox(self.groupBox_1)
        self.Shininess.setObjectName(u"Shininess")
        self.Shininess.setSuffix(u" %")
        self.Shininess.setMaximum(100)

        self.gridLayout_1.addWidget(self.Shininess, 5, 1, 1, 1)

        self.gridLayout_1.setColumnStretch(0, 1)
        self.gridLayout_1.setColumnMinimumWidth(1, 100)

        self.verticalLayout_2.addWidget(self.groupBox_1)

        self.groupBox_2 = QGroupBox(self.tab_Shape)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_LineColor = QLabel(self.groupBox_2)
        self.label_LineColor.setObjectName(u"label_LineColor")

        self.gridLayout_2.addWidget(self.label_LineColor, 0, 0, 1, 1)

        self.LineColor = Gui_ColorButton(self.groupBox_2)
        self.LineColor.setObjectName(u"LineColor")

        self.gridLayout_2.addWidget(self.LineColor, 0, 1, 1, 1)

        self.label_LineWidth = QLabel(self.groupBox_2)
        self.label_LineWidth.setObjectName(u"label_LineWidth")

        self.gridLayout_2.addWidget(self.label_LineWidth, 1, 0, 1, 1)

        self.LineWidth = QSpinBox(self.groupBox_2)
        self.LineWidth.setObjectName(u"LineWidth")

        self.gridLayout_2.addWidget(self.LineWidth, 1, 1, 1, 1)

        self.label_PointColor = QLabel(self.groupBox_2)
        self.label_PointColor.setObjectName(u"label_PointColor")

        self.gridLayout_2.addWidget(self.label_PointColor, 2, 0, 1, 1)

        self.PointColor = Gui_ColorButton(self.groupBox_2)
        self.PointColor.setObjectName(u"PointColor")

        self.gridLayout_2.addWidget(self.PointColor, 2, 1, 1, 1)

        self.label_PointSize = QLabel(self.groupBox_2)
        self.label_PointSize.setObjectName(u"label_PointSize")

        self.gridLayout_2.addWidget(self.label_PointSize, 3, 0, 1, 1)

        self.PointSize = QSpinBox(self.groupBox_2)
        self.PointSize.setObjectName(u"PointSize")

        self.gridLayout_2.addWidget(self.PointSize, 3, 1, 1, 1)

        self.label_DrawStyle = QLabel(self.groupBox_2)
        self.label_DrawStyle.setObjectName(u"label_DrawStyle")

        self.gridLayout_2.addWidget(self.label_DrawStyle, 4, 0, 1, 1)

        self.DrawStyle = QComboBox(self.groupBox_2)
        self.DrawStyle.addItem("")
        self.DrawStyle.addItem("")
        self.DrawStyle.addItem("")
        self.DrawStyle.addItem("")
        self.DrawStyle.setObjectName(u"DrawStyle")

        self.gridLayout_2.addWidget(self.DrawStyle, 4, 1, 1, 1)

        self.label_DisplayMode = QLabel(self.groupBox_2)
        self.label_DisplayMode.setObjectName(u"label_DisplayMode")

        self.gridLayout_2.addWidget(self.label_DisplayMode, 5, 0, 1, 1)

        self.DisplayMode = QComboBox(self.groupBox_2)
        self.DisplayMode.addItem("")
        self.DisplayMode.addItem("")
        self.DisplayMode.addItem("")
        self.DisplayMode.addItem("")
        self.DisplayMode.setObjectName(u"DisplayMode")

        self.gridLayout_2.addWidget(self.DisplayMode, 5, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnMinimumWidth(1, 100)

        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_1)

        self.tabs.addTab(self.tab_Shape, "")
        self.tab_Annotation = QWidget()
        self.tab_Annotation.setObjectName(u"tab_Annotation")
        self.verticalLayout_3 = QVBoxLayout(self.tab_Annotation)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_3 = QGroupBox(self.tab_Annotation)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_ScaleMultiplier = QLabel(self.groupBox_3)
        self.label_ScaleMultiplier.setObjectName(u"label_ScaleMultiplier")

        self.gridLayout_3.addWidget(self.label_ScaleMultiplier, 0, 0, 1, 1)

        self.ScaleMultiplier = QDoubleSpinBox(self.groupBox_3)
        self.ScaleMultiplier.setObjectName(u"ScaleMultiplier")
        self.ScaleMultiplier.setMinimum(0)
        self.ScaleMultiplier.setMaximum(10000)

        self.gridLayout_3.addWidget(self.ScaleMultiplier, 0, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnMinimumWidth(1, 100)

        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.tab_Annotation)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_TextFont = QLabel(self.groupBox_4)
        self.label_TextFont.setObjectName(u"label_TextFont")

        self.gridLayout_4.addWidget(self.label_TextFont, 0, 0, 1, 1)

        self.TextFont = QFontComboBox(self.groupBox_4)
        self.TextFont.setObjectName(u"TextFont")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextFont.sizePolicy().hasHeightForWidth())
        self.TextFont.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.TextFont, 0, 1, 1, 1)

        self.label_TextSize = QLabel(self.groupBox_4)
        self.label_TextSize.setObjectName(u"label_TextSize")

        self.gridLayout_4.addWidget(self.label_TextSize, 1, 0, 1, 1)

        self.TextSize = Gui_InputField(self.groupBox_4)
        self.TextSize.setObjectName(u"TextSize")
        self.TextSize.setProperty(u"unit", u"")

        self.gridLayout_4.addWidget(self.TextSize, 1, 1, 1, 1)

        self.label_LineSpacing = QLabel(self.groupBox_4)
        self.label_LineSpacing.setObjectName(u"label_LineSpacing")

        self.gridLayout_4.addWidget(self.label_LineSpacing, 2, 0, 1, 1)

        self.LineSpacing = QDoubleSpinBox(self.groupBox_4)
        self.LineSpacing.setObjectName(u"LineSpacing")

        self.gridLayout_4.addWidget(self.LineSpacing, 2, 1, 1, 1)

        self.label_TextColor = QLabel(self.groupBox_4)
        self.label_TextColor.setObjectName(u"label_TextColor")

        self.gridLayout_4.addWidget(self.label_TextColor, 3, 0, 1, 1)

        self.TextColor = Gui_ColorButton(self.groupBox_4)
        self.TextColor.setObjectName(u"TextColor")

        self.gridLayout_4.addWidget(self.TextColor, 3, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnMinimumWidth(1, 100)

        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.tab_Annotation)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_AnnoLineWidth = QLabel(self.groupBox_5)
        self.label_AnnoLineWidth.setObjectName(u"label_AnnoLineWidth")

        self.gridLayout_5.addWidget(self.label_AnnoLineWidth, 0, 0, 1, 1)

        self.AnnoLineWidth = QSpinBox(self.groupBox_5)
        self.AnnoLineWidth.setObjectName(u"AnnoLineWidth")

        self.gridLayout_5.addWidget(self.AnnoLineWidth, 0, 1, 1, 1)

        self.label_ArrowStyleStart = QLabel(self.groupBox_5)
        self.label_ArrowStyleStart.setObjectName(u"label_ArrowStyleStart")

        self.gridLayout_5.addWidget(self.label_ArrowStyleStart, 1, 0, 1, 1)

        self.ArrowStyleStart = QComboBox(self.groupBox_5)
        self.ArrowStyleStart.addItem("")
        self.ArrowStyleStart.addItem("")
        self.ArrowStyleStart.addItem("")
        self.ArrowStyleStart.addItem("")
        self.ArrowStyleStart.addItem("")
        self.ArrowStyleStart.addItem("")
        self.ArrowStyleStart.setObjectName(u"ArrowStyleStart")

        self.gridLayout_5.addWidget(self.ArrowStyleStart, 1, 1, 1, 1)

        self.label_ArrowSizeStart = QLabel(self.groupBox_5)
        self.label_ArrowSizeStart.setObjectName(u"label_ArrowSizeStart")

        self.gridLayout_5.addWidget(self.label_ArrowSizeStart, 2, 0, 1, 1)

        self.ArrowSizeStart = Gui_InputField(self.groupBox_5)
        self.ArrowSizeStart.setObjectName(u"ArrowSizeStart")
        self.ArrowSizeStart.setProperty(u"unit", u"")

        self.gridLayout_5.addWidget(self.ArrowSizeStart, 2, 1, 1, 1)

        self.label_ArrowStyleEnd = QLabel(self.groupBox_5)
        self.label_ArrowStyleEnd.setObjectName(u"label_ArrowStyleEnd")

        self.gridLayout_5.addWidget(self.label_ArrowStyleEnd, 3, 0, 1, 1)

        self.ArrowStyleEnd = QComboBox(self.groupBox_5)
        self.ArrowStyleEnd.addItem("")
        self.ArrowStyleEnd.addItem("")
        self.ArrowStyleEnd.addItem("")
        self.ArrowStyleEnd.addItem("")
        self.ArrowStyleEnd.addItem("")
        self.ArrowStyleEnd.addItem("")
        self.ArrowStyleEnd.setObjectName(u"ArrowStyleEnd")

        self.gridLayout_5.addWidget(self.ArrowStyleEnd, 3, 1, 1, 1)

        self.label_ArrowSizeEnd = QLabel(self.groupBox_5)
        self.label_ArrowSizeEnd.setObjectName(u"label_ArrowSizeEnd")

        self.gridLayout_5.addWidget(self.label_ArrowSizeEnd, 4, 0, 1, 1)

        self.ArrowSizeEnd = Gui_InputField(self.groupBox_5)
        self.ArrowSizeEnd.setObjectName(u"ArrowSizeEnd")
        self.ArrowSizeEnd.setProperty(u"unit", u"")

        self.gridLayout_5.addWidget(self.ArrowSizeEnd, 4, 1, 1, 1)

        self.label_AnnoLineColor = QLabel(self.groupBox_5)
        self.label_AnnoLineColor.setObjectName(u"label_AnnoLineColor")

        self.gridLayout_5.addWidget(self.label_AnnoLineColor, 5, 0, 1, 1)

        self.AnnoLineColor = Gui_ColorButton(self.groupBox_5)
        self.AnnoLineColor.setObjectName(u"AnnoLineColor")

        self.gridLayout_5.addWidget(self.AnnoLineColor, 5, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnMinimumWidth(1, 100)

        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.tab_Annotation)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_ShowUnit = QLabel(self.groupBox_6)
        self.label_ShowUnit.setObjectName(u"label_ShowUnit")

        self.gridLayout_6.addWidget(self.label_ShowUnit, 0, 0, 1, 1)

        self.ShowUnit = QCheckBox(self.groupBox_6)
        self.ShowUnit.setObjectName(u"ShowUnit")

        self.gridLayout_6.addWidget(self.ShowUnit, 0, 1, 1, 1)

        self.label_UnitOverride = QLabel(self.groupBox_6)
        self.label_UnitOverride.setObjectName(u"label_UnitOverride")

        self.gridLayout_6.addWidget(self.label_UnitOverride, 1, 0, 1, 1)

        self.UnitOverride = QLineEdit(self.groupBox_6)
        self.UnitOverride.setObjectName(u"UnitOverride")

        self.gridLayout_6.addWidget(self.UnitOverride, 1, 1, 1, 1)

        self.label_DimOvershoot = QLabel(self.groupBox_6)
        self.label_DimOvershoot.setObjectName(u"label_DimOvershoot")

        self.gridLayout_6.addWidget(self.label_DimOvershoot, 2, 0, 1, 1)

        self.DimOvershoot = Gui_InputField(self.groupBox_6)
        self.DimOvershoot.setObjectName(u"DimOvershoot")
        self.DimOvershoot.setProperty(u"unit", u"")

        self.gridLayout_6.addWidget(self.DimOvershoot, 2, 1, 1, 1)

        self.label_ExtLines = QLabel(self.groupBox_6)
        self.label_ExtLines.setObjectName(u"label_ExtLines")

        self.gridLayout_6.addWidget(self.label_ExtLines, 3, 0, 1, 1)

        self.ExtLines = Gui_InputField(self.groupBox_6)
        self.ExtLines.setObjectName(u"ExtLines")
        self.ExtLines.setProperty(u"unit", u"")

        self.gridLayout_6.addWidget(self.ExtLines, 3, 1, 1, 1)

        self.label_ExtOvershoot = QLabel(self.groupBox_6)
        self.label_ExtOvershoot.setObjectName(u"label_ExtOvershoot")

        self.gridLayout_6.addWidget(self.label_ExtOvershoot, 4, 0, 1, 1)

        self.ExtOvershoot = Gui_InputField(self.groupBox_6)
        self.ExtOvershoot.setObjectName(u"ExtOvershoot")
        self.ExtOvershoot.setProperty(u"unit", u"")

        self.gridLayout_6.addWidget(self.ExtOvershoot, 4, 1, 1, 1)

        self.label_TextSpacing = QLabel(self.groupBox_6)
        self.label_TextSpacing.setObjectName(u"label_TextSpacing")

        self.gridLayout_6.addWidget(self.label_TextSpacing, 5, 0, 1, 1)

        self.TextSpacing = Gui_InputField(self.groupBox_6)
        self.TextSpacing.setObjectName(u"TextSpacing")
        self.TextSpacing.setProperty(u"unit", u"")

        self.gridLayout_6.addWidget(self.TextSpacing, 5, 1, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnMinimumWidth(1, 100)

        self.verticalLayout_3.addWidget(self.groupBox_6)

        self.tabs.addTab(self.tab_Annotation, "")

        self.verticalLayout_1.addWidget(self.tabs)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.applyButton = QPushButton(Form)
        self.applyButton.setObjectName(u"applyButton")
        icon1 = QIcon()
        iconThemeName = u"gtk-apply"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.applyButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.applyButton)

        self.annotButton = QPushButton(Form)
        self.annotButton.setObjectName(u"annotButton")

        self.horizontalLayout_2.addWidget(self.annotButton)


        self.verticalLayout_1.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Style Settings", None))
        self.comboPresets.setItemText(0, QCoreApplication.translate("Form", u"Load preset", None))

#if QT_CONFIG(tooltip)
        self.comboPresets.setToolTip(QCoreApplication.translate("Form", u"Fill the values below from a stored style preset", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.saveButton.setToolTip(QCoreApplication.translate("Form", u"Saves the current style as a preset", None))
#endif // QT_CONFIG(tooltip)
        self.saveButton.setText("")
        self.groupBox_1.setTitle(QCoreApplication.translate("Form", u"Shape Appearance", None))
        self.label_ShapeColor.setText(QCoreApplication.translate("Form", u"Shape color", None))
        self.label_AmbientColor.setText(QCoreApplication.translate("Form", u"Ambient shape color", None))
        self.label_EmissiveColor.setText(QCoreApplication.translate("Form", u"Emissive shape color", None))
        self.label_SpecularColor.setText(QCoreApplication.translate("Form", u"Specular shape color", None))
        self.label_Transparency.setText(QCoreApplication.translate("Form", u"Shape transparency", None))
        self.label_Shininess.setText(QCoreApplication.translate("Form", u"Shape shininess", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Other", None))
        self.label_LineColor.setText(QCoreApplication.translate("Form", u"Line color", None))
        self.label_LineWidth.setText(QCoreApplication.translate("Form", u"Line width", None))
        self.LineWidth.setSuffix(QCoreApplication.translate("Form", u" px", None))
        self.label_PointColor.setText(QCoreApplication.translate("Form", u"Point color", None))
        self.label_PointSize.setText(QCoreApplication.translate("Form", u"Point size", None))
        self.PointSize.setSuffix(QCoreApplication.translate("Form", u" px", None))
        self.label_DrawStyle.setText(QCoreApplication.translate("Form", u"Draw style", None))
        self.DrawStyle.setItemText(0, QCoreApplication.translate("Form", u"Solid", None))
        self.DrawStyle.setItemText(1, QCoreApplication.translate("Form", u"Dashed", None))
        self.DrawStyle.setItemText(2, QCoreApplication.translate("Form", u"Dotted", None))
        self.DrawStyle.setItemText(3, QCoreApplication.translate("Form", u"DashDot", None))

        self.label_DisplayMode.setText(QCoreApplication.translate("Form", u"Display mode", None))
        self.DisplayMode.setItemText(0, QCoreApplication.translate("Form", u"Flat Lines", None))
        self.DisplayMode.setItemText(1, QCoreApplication.translate("Form", u"Shaded", None))
        self.DisplayMode.setItemText(2, QCoreApplication.translate("Form", u"Wireframe", None))
        self.DisplayMode.setItemText(3, QCoreApplication.translate("Form", u"Points", None))

        self.tabs.setTabText(self.tabs.indexOf(self.tab_Shape), QCoreApplication.translate("Form", u"Shape", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Annotations", None))
        self.label_ScaleMultiplier.setText(QCoreApplication.translate("Form", u"Scale multiplier", None))
#if QT_CONFIG(tooltip)
        self.ScaleMultiplier.setToolTip(QCoreApplication.translate("Form", u"The annotation scale multiplier is the inverse of the scale set in the\n"
"Annotation scale widget. If the scale is 1:100 the multiplier is 100.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Texts", None))
        self.label_TextFont.setText(QCoreApplication.translate("Form", u"Font name", None))
#if QT_CONFIG(tooltip)
        self.TextFont.setToolTip(QCoreApplication.translate("Form", u"The font for texts, dimensions and labels", None))
#endif // QT_CONFIG(tooltip)
        self.label_TextSize.setText(QCoreApplication.translate("Form", u"Font size", None))
#if QT_CONFIG(tooltip)
        self.TextSize.setToolTip(QCoreApplication.translate("Form", u"The height for texts, dimension texts and label texts", None))
#endif // QT_CONFIG(tooltip)
        self.label_LineSpacing.setText(QCoreApplication.translate("Form", u"Line spacing factor", None))
#if QT_CONFIG(tooltip)
        self.LineSpacing.setToolTip(QCoreApplication.translate("Form", u"The line spacing for multi-line texts and labels (relative to the font size)", None))
#endif // QT_CONFIG(tooltip)
        self.label_TextColor.setText(QCoreApplication.translate("Form", u"Text color", None))
#if QT_CONFIG(tooltip)
        self.TextColor.setToolTip(QCoreApplication.translate("Form", u"The color for texts, dimension texts and label texts", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"Lines and Arrows", None))
        self.label_AnnoLineWidth.setText(QCoreApplication.translate("Form", u"Line width", None))
        self.AnnoLineWidth.setSuffix(QCoreApplication.translate("Form", u" px", None))
        self.label_ArrowStyleStart.setText(QCoreApplication.translate("Form", u"Start arrow type", None))
        self.ArrowStyleStart.setItemText(0, QCoreApplication.translate("Form", u"Dot", None))
        self.ArrowStyleStart.setItemText(1, QCoreApplication.translate("Form", u"Circle", None))
        self.ArrowStyleStart.setItemText(2, QCoreApplication.translate("Form", u"Arrow", None))
        self.ArrowStyleStart.setItemText(3, QCoreApplication.translate("Form", u"Tick", None))
        self.ArrowStyleStart.setItemText(4, QCoreApplication.translate("Form", u"Tick-2", None))
        self.ArrowStyleStart.setItemText(5, QCoreApplication.translate("Form", u"None", None))

        self.label_ArrowSizeStart.setText(QCoreApplication.translate("Form", u"Start arrow size", None))
        self.label_ArrowStyleEnd.setText(QCoreApplication.translate("Form", u"End arrow type", None))
        self.ArrowStyleEnd.setItemText(0, QCoreApplication.translate("Form", u"Dot", None))
        self.ArrowStyleEnd.setItemText(1, QCoreApplication.translate("Form", u"Circle", None))
        self.ArrowStyleEnd.setItemText(2, QCoreApplication.translate("Form", u"Arrow", None))
        self.ArrowStyleEnd.setItemText(3, QCoreApplication.translate("Form", u"Tick", None))
        self.ArrowStyleEnd.setItemText(4, QCoreApplication.translate("Form", u"Tick-2", None))
        self.ArrowStyleEnd.setItemText(5, QCoreApplication.translate("Form", u"None", None))

        self.label_ArrowSizeEnd.setText(QCoreApplication.translate("Form", u"End arrow size", None))
        self.label_AnnoLineColor.setText(QCoreApplication.translate("Form", u"Line and arrow color", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"Dimensions", None))
        self.label_ShowUnit.setText(QCoreApplication.translate("Form", u"Show unit", None))
#if QT_CONFIG(tooltip)
        self.ShowUnit.setToolTip(QCoreApplication.translate("Form", u"Adds a unit symbol to dimension texts", None))
#endif // QT_CONFIG(tooltip)
        self.ShowUnit.setText("")
        self.label_UnitOverride.setText(QCoreApplication.translate("Form", u"Unit override", None))
#if QT_CONFIG(tooltip)
        self.UnitOverride.setToolTip(QCoreApplication.translate("Form", u"The unit override for dimensions. Leave blank to use the current FreeCAD unit.", None))
#endif // QT_CONFIG(tooltip)
        self.label_DimOvershoot.setText(QCoreApplication.translate("Form", u"Dimension line overshoot", None))
#if QT_CONFIG(tooltip)
        self.DimOvershoot.setToolTip(QCoreApplication.translate("Form", u"The distance the dimension line is extended past the extension lines", None))
#endif // QT_CONFIG(tooltip)
        self.label_ExtLines.setText(QCoreApplication.translate("Form", u"Extension line length", None))
#if QT_CONFIG(tooltip)
        self.ExtLines.setToolTip(QCoreApplication.translate("Form", u"The length of extension lines. Use 0 for full extension lines. A negative value\n"
"defines the gap between the ends of the extension lines and the measured points.\n"
"A positive value defines the maximum length of the extension lines. Only used\n"
"for linear dimensions.", None))
#endif // QT_CONFIG(tooltip)
        self.label_ExtOvershoot.setText(QCoreApplication.translate("Form", u"Extension line overshoot", None))
#if QT_CONFIG(tooltip)
        self.ExtOvershoot.setToolTip(QCoreApplication.translate("Form", u"The length of extension lines above the dimension line", None))
#endif // QT_CONFIG(tooltip)
        self.label_TextSpacing.setText(QCoreApplication.translate("Form", u"Text spacing", None))
#if QT_CONFIG(tooltip)
        self.TextSpacing.setToolTip(QCoreApplication.translate("Form", u"The space between the dimension line and the dimension text", None))
#endif // QT_CONFIG(tooltip)
        self.tabs.setTabText(self.tabs.indexOf(self.tab_Annotation), QCoreApplication.translate("Form", u"Annotation", None))
#if QT_CONFIG(tooltip)
        self.applyButton.setToolTip(QCoreApplication.translate("Form", u"Apply the above style to selected object(s)", None))
#endif // QT_CONFIG(tooltip)
        self.applyButton.setText(QCoreApplication.translate("Form", u"Selected", None))
#if QT_CONFIG(tooltip)
        self.annotButton.setToolTip(QCoreApplication.translate("Form", u"Apply the above style to all annotations (texts, dimensions and labels)", None))
#endif // QT_CONFIG(tooltip)
        self.annotButton.setText(QCoreApplication.translate("Form", u"Annotations", None))
    # retranslateUi

