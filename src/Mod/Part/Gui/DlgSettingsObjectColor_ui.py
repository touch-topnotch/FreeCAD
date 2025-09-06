# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsObjectColor.ui'
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

class Ui_PartGui_DlgSettingsObjectColor(object):
    def setupUi(self, PartGui__DlgSettingsObjectColor):
        if not PartGui__DlgSettingsObjectColor.objectName():
            PartGui__DlgSettingsObjectColor.setObjectName(u"PartGui__DlgSettingsObjectColor")
        PartGui__DlgSettingsObjectColor.resize(476, 378)
        self.verticalLayout = QVBoxLayout(PartGui__DlgSettingsObjectColor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxDefaultColors = QGroupBox(PartGui__DlgSettingsObjectColor)
        self.groupBoxDefaultColors.setObjectName(u"groupBoxDefaultColors")
        self.horizontalLayout = QHBoxLayout(self.groupBoxDefaultColors)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.groupBoxDefaultColors)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.DefaultShapeColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.DefaultShapeColor.setObjectName(u"DefaultShapeColor")
        self.DefaultShapeColor.setColor(QColor(204, 204, 230))
        self.DefaultShapeColor.setProperty(u"prefEntry", u"DefaultShapeColor")
        self.DefaultShapeColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.DefaultShapeColor, 0, 1, 1, 1)

        self.checkRandomColor = Gui_PrefCheckBox(self.groupBoxDefaultColors)
        self.checkRandomColor.setObjectName(u"checkRandomColor")
        self.checkRandomColor.setProperty(u"prefEntry", u"RandomColor")
        self.checkRandomColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.checkRandomColor, 0, 2, 1, 1)

        self.label_ambient = QLabel(self.groupBoxDefaultColors)
        self.label_ambient.setObjectName(u"label_ambient")
        self.label_ambient.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_ambient, 1, 0, 1, 1)

        self.DefaultAmbientColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.DefaultAmbientColor.setObjectName(u"DefaultAmbientColor")
        self.DefaultAmbientColor.setColor(QColor(85, 85, 85))
        self.DefaultAmbientColor.setProperty(u"prefEntry", u"DefaultAmbientColor")
        self.DefaultAmbientColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.DefaultAmbientColor, 1, 1, 1, 1)

        self.label_emissive = QLabel(self.groupBoxDefaultColors)
        self.label_emissive.setObjectName(u"label_emissive")
        self.label_emissive.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_emissive, 2, 0, 1, 1)

        self.DefaultEmissiveColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.DefaultEmissiveColor.setObjectName(u"DefaultEmissiveColor")
        self.DefaultEmissiveColor.setColor(QColor(0, 0, 0))
        self.DefaultEmissiveColor.setProperty(u"prefEntry", u"DefaultEmissiveColor")
        self.DefaultEmissiveColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.DefaultEmissiveColor, 2, 1, 1, 1)

        self.label_specular = QLabel(self.groupBoxDefaultColors)
        self.label_specular.setObjectName(u"label_specular")
        self.label_specular.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_specular, 3, 0, 1, 1)

        self.DefaultSpecularColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.DefaultSpecularColor.setObjectName(u"DefaultSpecularColor")
        self.DefaultSpecularColor.setColor(QColor(136, 136, 136))
        self.DefaultSpecularColor.setProperty(u"prefEntry", u"DefaultSpecularColor")
        self.DefaultSpecularColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.DefaultSpecularColor, 3, 1, 1, 1)

        self.label_transparency = QLabel(self.groupBoxDefaultColors)
        self.label_transparency.setObjectName(u"label_transparency")
        self.label_transparency.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_transparency, 4, 0, 1, 1)

        self.DefaultShapeTransparency = Gui_PrefSpinBox(self.groupBoxDefaultColors)
        self.DefaultShapeTransparency.setObjectName(u"DefaultShapeTransparency")
        self.DefaultShapeTransparency.setSuffix(u" %")
        self.DefaultShapeTransparency.setMaximum(100)
        self.DefaultShapeTransparency.setSingleStep(5)
        self.DefaultShapeTransparency.setProperty(u"prefEntry", u"DefaultShapeTransparency")
        self.DefaultShapeTransparency.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.DefaultShapeTransparency, 4, 1, 1, 1)

        self.label_shininess = QLabel(self.groupBoxDefaultColors)
        self.label_shininess.setObjectName(u"label_shininess")
        self.label_shininess.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_shininess, 5, 0, 1, 1)

        self.DefaultShapeShininess = Gui_PrefSpinBox(self.groupBoxDefaultColors)
        self.DefaultShapeShininess.setObjectName(u"DefaultShapeShininess")
        self.DefaultShapeShininess.setSuffix(u" %")
        self.DefaultShapeShininess.setMaximum(100)
        self.DefaultShapeShininess.setValue(90)
        self.DefaultShapeShininess.setSingleStep(5)
        self.DefaultShapeShininess.setProperty(u"prefEntry", u"DefaultShapeShininess")
        self.DefaultShapeShininess.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.DefaultShapeShininess, 5, 1, 1, 1)

        self.label_7 = QLabel(self.groupBoxDefaultColors)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.DefaultShapeLineColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.DefaultShapeLineColor.setObjectName(u"DefaultShapeLineColor")
        self.DefaultShapeLineColor.setColor(QColor(25, 25, 25))
        self.DefaultShapeLineColor.setProperty(u"prefEntry", u"DefaultShapeLineColor")
        self.DefaultShapeLineColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.DefaultShapeLineColor, 6, 1, 1, 1)

        self.label_9 = QLabel(self.groupBoxDefaultColors)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.DefaultShapeLineWidth = Gui_PrefSpinBox(self.groupBoxDefaultColors)
        self.DefaultShapeLineWidth.setObjectName(u"DefaultShapeLineWidth")
        self.DefaultShapeLineWidth.setSuffix(u" px")
        self.DefaultShapeLineWidth.setMaximum(9)
        self.DefaultShapeLineWidth.setValue(2)
        self.DefaultShapeLineWidth.setProperty(u"prefEntry", u"DefaultShapeLineWidth")
        self.DefaultShapeLineWidth.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.DefaultShapeLineWidth, 7, 1, 1, 1)

        self.label_10 = QLabel(self.groupBoxDefaultColors)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)

        self.DefaultShapeVertexColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.DefaultShapeVertexColor.setObjectName(u"DefaultShapeVertexColor")
        self.DefaultShapeVertexColor.setColor(QColor(25, 25, 25))
        self.DefaultShapeVertexColor.setProperty(u"prefEntry", u"DefaultShapeVertexColor")
        self.DefaultShapeVertexColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.DefaultShapeVertexColor, 8, 1, 1, 1)

        self.label_11 = QLabel(self.groupBoxDefaultColors)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)

        self.DefaultShapeVertexSize = Gui_PrefSpinBox(self.groupBoxDefaultColors)
        self.DefaultShapeVertexSize.setObjectName(u"DefaultShapeVertexSize")
        self.DefaultShapeVertexSize.setSuffix(u" px")
        self.DefaultShapeVertexSize.setMaximum(9)
        self.DefaultShapeVertexSize.setValue(2)
        self.DefaultShapeVertexSize.setProperty(u"prefEntry", u"DefaultShapePointSize")
        self.DefaultShapeVertexSize.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.DefaultShapeVertexSize, 9, 1, 1, 1)

        self.label_8 = QLabel(self.groupBoxDefaultColors)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)

        self.BoundingBoxColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.BoundingBoxColor.setObjectName(u"BoundingBoxColor")
        self.BoundingBoxColor.setColor(QColor(255, 255, 255))
        self.BoundingBoxColor.setProperty(u"prefEntry", u"BoundingBoxColor")
        self.BoundingBoxColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.BoundingBoxColor, 10, 1, 1, 1)

        self.label_fontsize = QLabel(self.groupBoxDefaultColors)
        self.label_fontsize.setObjectName(u"label_fontsize")
        self.label_fontsize.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_fontsize, 11, 0, 1, 1)

        self.BoundingBoxFontSize = Gui_PrefDoubleSpinBox(self.groupBoxDefaultColors)
        self.BoundingBoxFontSize.setObjectName(u"BoundingBoxFontSize")
        self.BoundingBoxFontSize.setSuffix(u" pt")
        self.BoundingBoxFontSize.setDecimals(1)
        self.BoundingBoxFontSize.setMinimum(2.000000000000000)
        self.BoundingBoxFontSize.setMaximum(64.000000000000000)
        self.BoundingBoxFontSize.setValue(10.000000000000000)
        self.BoundingBoxFontSize.setProperty(u"prefEntry", u"BoundingBoxFontSize")
        self.BoundingBoxFontSize.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.BoundingBoxFontSize, 11, 1, 1, 1)

        self.twosideRendering = Gui_PrefCheckBox(self.groupBoxDefaultColors)
        self.twosideRendering.setObjectName(u"twosideRendering")
        self.twosideRendering.setMinimumSize(QSize(182, 0))
        self.twosideRendering.setChecked(True)
        self.twosideRendering.setProperty(u"prefEntry", u"TwoSideRendering")
        self.twosideRendering.setProperty(u"prefPath", u"Mod/Part")

        self.gridLayout.addWidget(self.twosideRendering, 12, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.groupBoxDefaultColors)

        self.groupBox = QGroupBox(PartGui__DlgSettingsObjectColor)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(182, 0))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.AnnotationTextColor = Gui_PrefColorButton(self.groupBox)
        self.AnnotationTextColor.setObjectName(u"AnnotationTextColor")
        self.AnnotationTextColor.setProperty(u"prefEntry", u"AnnotationTextColor")
        self.AnnotationTextColor.setProperty(u"prefPath", u"View")

        self.gridLayout_2.addWidget(self.AnnotationTextColor, 0, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 217, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        QWidget.setTabOrder(self.DefaultShapeColor, self.DefaultShapeLineWidth)
        QWidget.setTabOrder(self.DefaultShapeLineWidth, self.DefaultShapeLineColor)
        QWidget.setTabOrder(self.DefaultShapeLineColor, self.BoundingBoxColor)

        self.retranslateUi(PartGui__DlgSettingsObjectColor)
        self.checkRandomColor.toggled.connect(self.DefaultShapeColor.setDisabled)

        QMetaObject.connectSlotsByName(PartGui__DlgSettingsObjectColor)
    # setupUi

    def retranslateUi(self, PartGui__DlgSettingsObjectColor):
        PartGui__DlgSettingsObjectColor.setWindowTitle(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Shape Appearance", None))
        self.groupBoxDefaultColors.setTitle(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Default Shape Appearance Properties", None))
        self.label_6.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Shape color", None))
#if QT_CONFIG(tooltip)
        self.DefaultShapeColor.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"The default color for new shapes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkRandomColor.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Use random color instead", None))
#endif // QT_CONFIG(tooltip)
        self.checkRandomColor.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Random", None))
        self.label_ambient.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Ambient shape color", None))
#if QT_CONFIG(tooltip)
        self.DefaultAmbientColor.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"The default ambient color for new shapes", None))
#endif // QT_CONFIG(tooltip)
        self.label_emissive.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Emissive shape color", None))
#if QT_CONFIG(tooltip)
        self.DefaultEmissiveColor.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"The default emissive color for new shapes", None))
#endif // QT_CONFIG(tooltip)
        self.label_specular.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Specular shape color", None))
#if QT_CONFIG(tooltip)
        self.DefaultSpecularColor.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"The default specular color for new shapes", None))
#endif // QT_CONFIG(tooltip)
        self.label_transparency.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Shape transparency", None))
#if QT_CONFIG(tooltip)
        self.DefaultShapeTransparency.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"The default transparency for new shapes", None))
#endif // QT_CONFIG(tooltip)
        self.label_shininess.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Shape shininess", None))
#if QT_CONFIG(tooltip)
        self.DefaultShapeShininess.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"The default shininess for new shapes", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Line color", None))
#if QT_CONFIG(tooltip)
        self.DefaultShapeLineColor.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"The default line color for new shapes", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Line width", None))
#if QT_CONFIG(tooltip)
        self.DefaultShapeLineWidth.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"The default line thickness for new shapes", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Vertex color", None))
#if QT_CONFIG(tooltip)
        self.DefaultShapeVertexColor.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"The default color for new vertices", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Vertex size", None))
#if QT_CONFIG(tooltip)
        self.DefaultShapeVertexSize.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"The default size for new vertices", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Bounding box color", None))
#if QT_CONFIG(tooltip)
        self.BoundingBoxColor.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"The color of bounding boxes in the 3D view", None))
#endif // QT_CONFIG(tooltip)
        self.label_fontsize.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Bounding box font size", None))
#if QT_CONFIG(tooltip)
        self.BoundingBoxFontSize.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"The font size of bounding boxes in the 3D view", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.twosideRendering.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"The bottom side of the surface will be rendered the same way as the top.\n"
"If not checked, it depends on the option \"Backlight color\"\n"
"(preferences section Display -> 3D View); either the backlight color\n"
"will be used or black.", None))
#endif // QT_CONFIG(tooltip)
        self.twosideRendering.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Two-side rendering", None))
        self.groupBox.setTitle(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Default Annotation Color", None))
        self.label.setText(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Text color", None))
#if QT_CONFIG(tooltip)
        self.AnnotationTextColor.setToolTip(QCoreApplication.translate("PartGui::DlgSettingsObjectColor", u"Text color for document annotations", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

