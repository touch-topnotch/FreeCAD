# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SketcherSettingsAppearance.ui'
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

class Ui_SketcherGui_SketcherSettingsAppearance(object):
    def setupUi(self, SketcherGui__SketcherSettingsAppearance):
        if not SketcherGui__SketcherSettingsAppearance.objectName():
            SketcherGui__SketcherSettingsAppearance.setObjectName(u"SketcherGui__SketcherSettingsAppearance")
        SketcherGui__SketcherSettingsAppearance.resize(689, 863)
        self.verticalLayout_2 = QVBoxLayout(SketcherGui__SketcherSettingsAppearance)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(SketcherGui__SketcherSettingsAppearance)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.CreateLineColor = Gui_PrefColorButton(self.groupBox)
        self.CreateLineColor.setObjectName(u"CreateLineColor")
        self.CreateLineColor.setProperty(u"color", QColor(127, 127, 127))
        self.CreateLineColor.setProperty(u"prefEntry", u"CreateLineColor")
        self.CreateLineColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.CreateLineColor, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.CursorTextColor = Gui_PrefColorButton(self.groupBox)
        self.CursorTextColor.setObjectName(u"CursorTextColor")
        self.CursorTextColor.setProperty(u"color", QColor(0, 0, 255))
        self.CursorTextColor.setProperty(u"prefEntry", u"CursorTextColor")
        self.CursorTextColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.CursorTextColor, 4, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 5, 0, 1, 1)

        self.CursorCrosshairColor = Gui_PrefColorButton(self.groupBox)
        self.CursorCrosshairColor.setObjectName(u"CursorCrosshairColor")
        self.CursorCrosshairColor.setProperty(u"color", QColor(255, 255, 255))
        self.CursorCrosshairColor.setProperty(u"prefEntry", u"CursorCrosshairColor")
        self.CursorCrosshairColor.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.CursorCrosshairColor, 5, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(SketcherGui__SketcherSettingsAppearance)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(95, 0))

        self.gridLayout_6.addWidget(self.label_7, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(95, 0))

        self.gridLayout_6.addWidget(self.label_9, 1, 2, 1, 1)

        self.label_pattern = QLabel(self.groupBox_2)
        self.label_pattern.setObjectName(u"label_pattern")

        self.gridLayout_6.addWidget(self.label_pattern, 1, 3, 1, 1)

        self.label_width = QLabel(self.groupBox_2)
        self.label_width.setObjectName(u"label_width")

        self.gridLayout_6.addWidget(self.label_width, 1, 4, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_6, 1, 5, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 5, 0, 1, 1)

        self.FullyConstraintElementColor = Gui_PrefColorButton(self.groupBox_2)
        self.FullyConstraintElementColor.setObjectName(u"FullyConstraintElementColor")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FullyConstraintElementColor.sizePolicy().hasHeightForWidth())
        self.FullyConstraintElementColor.setSizePolicy(sizePolicy)
        self.FullyConstraintElementColor.setProperty(u"color", QColor(128, 208, 160))
        self.FullyConstraintElementColor.setProperty(u"prefEntry", u"FullyConstraintElementColor")
        self.FullyConstraintElementColor.setProperty(u"prefPath", u"View")

        self.gridLayout_6.addWidget(self.FullyConstraintElementColor, 5, 1, 1, 1)

        self.EditedEdgeColor = Gui_PrefColorButton(self.groupBox_2)
        self.EditedEdgeColor.setObjectName(u"EditedEdgeColor")
        sizePolicy.setHeightForWidth(self.EditedEdgeColor.sizePolicy().hasHeightForWidth())
        self.EditedEdgeColor.setSizePolicy(sizePolicy)
        self.EditedEdgeColor.setProperty(u"color", QColor(255, 255, 255))
        self.EditedEdgeColor.setProperty(u"prefEntry", u"EditedEdgeColor")
        self.EditedEdgeColor.setProperty(u"prefPath", u"View")

        self.gridLayout_6.addWidget(self.EditedEdgeColor, 5, 2, 1, 1)

        self.EdgePattern = QComboBox(self.groupBox_2)
        self.EdgePattern.setObjectName(u"EdgePattern")

        self.gridLayout_6.addWidget(self.EdgePattern, 5, 3, 1, 1)

        self.EdgeWidth = Gui_PrefSpinBox(self.groupBox_2)
        self.EdgeWidth.setObjectName(u"EdgeWidth")
        self.EdgeWidth.setProperty(u"unit", u"px")
        self.EdgeWidth.setSuffix(u" px")
        self.EdgeWidth.setMinimum(1)
        self.EdgeWidth.setMaximum(99)
        self.EdgeWidth.setValue(2)
        self.EdgeWidth.setProperty(u"prefEntry", u"EdgeWidth")
        self.EdgeWidth.setProperty(u"prefPath", u"Mod/Sketcher/View")

        self.gridLayout_6.addWidget(self.EdgeWidth, 5, 4, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 7, 0, 1, 1)

        self.FullyConstraintConstructionElementColor = Gui_PrefColorButton(self.groupBox_2)
        self.FullyConstraintConstructionElementColor.setObjectName(u"FullyConstraintConstructionElementColor")
        sizePolicy.setHeightForWidth(self.FullyConstraintConstructionElementColor.sizePolicy().hasHeightForWidth())
        self.FullyConstraintConstructionElementColor.setSizePolicy(sizePolicy)
        self.FullyConstraintConstructionElementColor.setProperty(u"color", QColor(143, 169, 253))
        self.FullyConstraintConstructionElementColor.setProperty(u"prefEntry", u"FullyConstraintConstructionElementColor")
        self.FullyConstraintConstructionElementColor.setProperty(u"prefPath", u"View")

        self.gridLayout_6.addWidget(self.FullyConstraintConstructionElementColor, 7, 1, 1, 1)

        self.ConstructionColor = Gui_PrefColorButton(self.groupBox_2)
        self.ConstructionColor.setObjectName(u"ConstructionColor")
        sizePolicy.setHeightForWidth(self.ConstructionColor.sizePolicy().hasHeightForWidth())
        self.ConstructionColor.setSizePolicy(sizePolicy)
        self.ConstructionColor.setProperty(u"color", QColor(0, 0, 220))
        self.ConstructionColor.setProperty(u"prefEntry", u"ConstructionColor")
        self.ConstructionColor.setProperty(u"prefPath", u"View")

        self.gridLayout_6.addWidget(self.ConstructionColor, 7, 2, 1, 1)

        self.ConstructionPattern = QComboBox(self.groupBox_2)
        self.ConstructionPattern.setObjectName(u"ConstructionPattern")

        self.gridLayout_6.addWidget(self.ConstructionPattern, 7, 3, 1, 1)

        self.ConstructionWidth = Gui_PrefSpinBox(self.groupBox_2)
        self.ConstructionWidth.setObjectName(u"ConstructionWidth")
        self.ConstructionWidth.setProperty(u"unit", u"px")
        self.ConstructionWidth.setSuffix(u" px")
        self.ConstructionWidth.setMinimum(1)
        self.ConstructionWidth.setMaximum(99)
        self.ConstructionWidth.setValue(2)
        self.ConstructionWidth.setProperty(u"prefEntry", u"ConstructionWidth")
        self.ConstructionWidth.setProperty(u"prefPath", u"Mod/Sketcher/View")

        self.gridLayout_6.addWidget(self.ConstructionWidth, 7, 4, 1, 1)

        self.label_ia = QLabel(self.groupBox_2)
        self.label_ia.setObjectName(u"label_ia")

        self.gridLayout_6.addWidget(self.label_ia, 8, 0, 1, 1)

        self.FullyConstraintInternalAlignmentColor = Gui_PrefColorButton(self.groupBox_2)
        self.FullyConstraintInternalAlignmentColor.setObjectName(u"FullyConstraintInternalAlignmentColor")
        sizePolicy.setHeightForWidth(self.FullyConstraintInternalAlignmentColor.sizePolicy().hasHeightForWidth())
        self.FullyConstraintInternalAlignmentColor.setSizePolicy(sizePolicy)
        self.FullyConstraintInternalAlignmentColor.setProperty(u"color", QColor(222, 222, 200))
        self.FullyConstraintInternalAlignmentColor.setProperty(u"prefEntry", u"FullyConstraintInternalAlignmentColor")
        self.FullyConstraintInternalAlignmentColor.setProperty(u"prefPath", u"View")

        self.gridLayout_6.addWidget(self.FullyConstraintInternalAlignmentColor, 8, 1, 1, 1)

        self.InternalAlignedGeoColor = Gui_PrefColorButton(self.groupBox_2)
        self.InternalAlignedGeoColor.setObjectName(u"InternalAlignedGeoColor")
        sizePolicy.setHeightForWidth(self.InternalAlignedGeoColor.sizePolicy().hasHeightForWidth())
        self.InternalAlignedGeoColor.setSizePolicy(sizePolicy)
        self.InternalAlignedGeoColor.setProperty(u"color", QColor(178, 178, 127))
        self.InternalAlignedGeoColor.setProperty(u"prefEntry", u"InternalAlignedGeoColor")
        self.InternalAlignedGeoColor.setProperty(u"prefPath", u"View")

        self.gridLayout_6.addWidget(self.InternalAlignedGeoColor, 8, 2, 1, 1)

        self.InternalPattern = QComboBox(self.groupBox_2)
        self.InternalPattern.setObjectName(u"InternalPattern")

        self.gridLayout_6.addWidget(self.InternalPattern, 8, 3, 1, 1)

        self.InternalWidth = Gui_PrefSpinBox(self.groupBox_2)
        self.InternalWidth.setObjectName(u"InternalWidth")
        self.InternalWidth.setProperty(u"unit", u"px")
        self.InternalWidth.setSuffix(u" px")
        self.InternalWidth.setMinimum(1)
        self.InternalWidth.setMaximum(99)
        self.InternalWidth.setValue(2)
        self.InternalWidth.setProperty(u"prefEntry", u"InternalWidth")
        self.InternalWidth.setProperty(u"prefPath", u"Mod/Sketcher/View")

        self.gridLayout_6.addWidget(self.InternalWidth, 8, 4, 1, 1)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_6.addWidget(self.label_20, 9, 0, 1, 1)

        self.ExternalColor = Gui_PrefColorButton(self.groupBox_2)
        self.ExternalColor.setObjectName(u"ExternalColor")
        sizePolicy.setHeightForWidth(self.ExternalColor.sizePolicy().hasHeightForWidth())
        self.ExternalColor.setSizePolicy(sizePolicy)
        self.ExternalColor.setProperty(u"color", QColor(204, 51, 115))
        self.ExternalColor.setProperty(u"prefEntry", u"ExternalColor")
        self.ExternalColor.setProperty(u"prefPath", u"View")

        self.gridLayout_6.addWidget(self.ExternalColor, 9, 1, 1, 1)

        self.ExternalPattern = QComboBox(self.groupBox_2)
        self.ExternalPattern.setObjectName(u"ExternalPattern")

        self.gridLayout_6.addWidget(self.ExternalPattern, 9, 3, 1, 1)

        self.ExternalWidth = Gui_PrefSpinBox(self.groupBox_2)
        self.ExternalWidth.setObjectName(u"ExternalWidth")
        self.ExternalWidth.setProperty(u"unit", u"px")
        self.ExternalWidth.setSuffix(u" px")
        self.ExternalWidth.setMinimum(1)
        self.ExternalWidth.setMaximum(99)
        self.ExternalWidth.setValue(2)
        self.ExternalWidth.setProperty(u"prefEntry", u"ExternalWidth")
        self.ExternalWidth.setProperty(u"prefPath", u"Mod/Sketcher/View")

        self.gridLayout_6.addWidget(self.ExternalWidth, 9, 4, 1, 1)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_6.addWidget(self.label_21, 10, 0, 1, 1)

        self.ExternalDefiningColor = Gui_PrefColorButton(self.groupBox_2)
        self.ExternalDefiningColor.setObjectName(u"ExternalDefiningColor")
        sizePolicy.setHeightForWidth(self.ExternalDefiningColor.sizePolicy().hasHeightForWidth())
        self.ExternalDefiningColor.setSizePolicy(sizePolicy)
        self.ExternalDefiningColor.setProperty(u"color", QColor(204, 51, 153))
        self.ExternalDefiningColor.setProperty(u"prefEntry", u"ExternalDefiningColor")
        self.ExternalDefiningColor.setProperty(u"prefPath", u"View")

        self.gridLayout_6.addWidget(self.ExternalDefiningColor, 10, 1, 1, 1)

        self.ExternalDefiningPattern = QComboBox(self.groupBox_2)
        self.ExternalDefiningPattern.setObjectName(u"ExternalDefiningPattern")

        self.gridLayout_6.addWidget(self.ExternalDefiningPattern, 10, 3, 1, 1)

        self.ExternalDefiningWidth = Gui_PrefSpinBox(self.groupBox_2)
        self.ExternalDefiningWidth.setObjectName(u"ExternalDefiningWidth")
        self.ExternalDefiningWidth.setProperty(u"unit", u"px")
        self.ExternalDefiningWidth.setSuffix(u" px")
        self.ExternalDefiningWidth.setMinimum(1)
        self.ExternalDefiningWidth.setMaximum(99)
        self.ExternalDefiningWidth.setValue(2)
        self.ExternalDefiningWidth.setProperty(u"prefEntry", u"ExternalDefiningWidth")
        self.ExternalDefiningWidth.setProperty(u"prefPath", u"Mod/Sketcher/View")

        self.gridLayout_6.addWidget(self.ExternalDefiningWidth, 10, 4, 1, 1)

        self.label_45 = QLabel(self.groupBox_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(200, 0))

        self.gridLayout_6.addWidget(self.label_45, 11, 0, 1, 1)

        self.FullyConstrainedColor = Gui_PrefColorButton(self.groupBox_2)
        self.FullyConstrainedColor.setObjectName(u"FullyConstrainedColor")
        sizePolicy.setHeightForWidth(self.FullyConstrainedColor.sizePolicy().hasHeightForWidth())
        self.FullyConstrainedColor.setSizePolicy(sizePolicy)
        self.FullyConstrainedColor.setProperty(u"color", QColor(0, 255, 0))
        self.FullyConstrainedColor.setProperty(u"prefEntry", u"FullyConstrainedColor")
        self.FullyConstrainedColor.setProperty(u"prefPath", u"View")

        self.gridLayout_6.addWidget(self.FullyConstrainedColor, 11, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 12, 0, 1, 1)

        self.InvalidSketchColor = Gui_PrefColorButton(self.groupBox_2)
        self.InvalidSketchColor.setObjectName(u"InvalidSketchColor")
        sizePolicy.setHeightForWidth(self.InvalidSketchColor.sizePolicy().hasHeightForWidth())
        self.InvalidSketchColor.setSizePolicy(sizePolicy)
        self.InvalidSketchColor.setProperty(u"color", QColor(255, 109, 0))
        self.InvalidSketchColor.setProperty(u"prefEntry", u"InvalidSketchColor")
        self.InvalidSketchColor.setProperty(u"prefPath", u"View")

        self.gridLayout_6.addWidget(self.InvalidSketchColor, 12, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBoxSketcherColor = QGroupBox(SketcherGui__SketcherSettingsAppearance)
        self.groupBoxSketcherColor.setObjectName(u"groupBoxSketcherColor")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBoxSketcherColor)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_14 = QLabel(self.groupBoxSketcherColor)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(200, 0))

        self.gridLayout_2.addWidget(self.label_14, 10, 0, 1, 1)

        self.ConstrainedColor = Gui_PrefColorButton(self.groupBoxSketcherColor)
        self.ConstrainedColor.setObjectName(u"ConstrainedColor")
        self.ConstrainedColor.setProperty(u"color", QColor(255, 38, 0))
        self.ConstrainedColor.setProperty(u"prefEntry", u"ConstrainedIcoColor")
        self.ConstrainedColor.setProperty(u"prefPath", u"View")

        self.gridLayout_2.addWidget(self.ConstrainedColor, 10, 1, 1, 1)

        self.label_15 = QLabel(self.groupBoxSketcherColor)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 11, 0, 1, 1)

        self.DatumColor = Gui_PrefColorButton(self.groupBoxSketcherColor)
        self.DatumColor.setObjectName(u"DatumColor")
        self.DatumColor.setProperty(u"color", QColor(255, 38, 0))
        self.DatumColor.setProperty(u"prefEntry", u"ConstrainedDimColor")
        self.DatumColor.setProperty(u"prefPath", u"View")

        self.gridLayout_2.addWidget(self.DatumColor, 11, 1, 1, 1)

        self.label_8 = QLabel(self.groupBoxSketcherColor)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 12, 0, 1, 1)

        self.NonDrivingConstraintColor = Gui_PrefColorButton(self.groupBoxSketcherColor)
        self.NonDrivingConstraintColor.setObjectName(u"NonDrivingConstraintColor")
        self.NonDrivingConstraintColor.setProperty(u"color", QColor(0, 38, 255))
        self.NonDrivingConstraintColor.setProperty(u"prefEntry", u"NonDrivingConstrDimColor")
        self.NonDrivingConstraintColor.setProperty(u"prefPath", u"View")

        self.gridLayout_2.addWidget(self.NonDrivingConstraintColor, 12, 1, 1, 1)

        self.labelexpr = QLabel(self.groupBoxSketcherColor)
        self.labelexpr.setObjectName(u"labelexpr")

        self.gridLayout_2.addWidget(self.labelexpr, 13, 0, 1, 1)

        self.ExprBasedConstrDimColor = Gui_PrefColorButton(self.groupBoxSketcherColor)
        self.ExprBasedConstrDimColor.setObjectName(u"ExprBasedConstrDimColor")
        self.ExprBasedConstrDimColor.setProperty(u"color", QColor(255, 127, 38))
        self.ExprBasedConstrDimColor.setProperty(u"prefEntry", u"ExprBasedConstrDimColor")
        self.ExprBasedConstrDimColor.setProperty(u"prefPath", u"View")

        self.gridLayout_2.addWidget(self.ExprBasedConstrDimColor, 13, 1, 1, 1)

        self.labeldeact = QLabel(self.groupBoxSketcherColor)
        self.labeldeact.setObjectName(u"labeldeact")

        self.gridLayout_2.addWidget(self.labeldeact, 14, 0, 1, 1)

        self.DeactivatedConstrDimColor = Gui_PrefColorButton(self.groupBoxSketcherColor)
        self.DeactivatedConstrDimColor.setObjectName(u"DeactivatedConstrDimColor")
        self.DeactivatedConstrDimColor.setProperty(u"color", QColor(127, 127, 127))
        self.DeactivatedConstrDimColor.setProperty(u"prefEntry", u"DeactivatedConstrDimColor")
        self.DeactivatedConstrDimColor.setProperty(u"prefPath", u"View")

        self.gridLayout_2.addWidget(self.DeactivatedConstrDimColor, 14, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.groupBoxSketcherColor)

        self.groupBox_3 = QGroupBox(SketcherGui__SketcherSettingsAppearance)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)

        self.SketchVertexColor = Gui_PrefColorButton(self.groupBox_3)
        self.SketchVertexColor.setObjectName(u"SketchVertexColor")
        self.SketchVertexColor.setProperty(u"color", QColor(255, 255, 255))
        self.SketchVertexColor.setProperty(u"prefEntry", u"SketchVertexColor")
        self.SketchVertexColor.setProperty(u"prefPath", u"View")

        self.gridLayout_4.addWidget(self.SketchVertexColor, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(200, 0))

        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)

        self.SketchEdgeColor = Gui_PrefColorButton(self.groupBox_3)
        self.SketchEdgeColor.setObjectName(u"SketchEdgeColor")
        self.SketchEdgeColor.setProperty(u"color", QColor(255, 255, 255))
        self.SketchEdgeColor.setProperty(u"prefEntry", u"SketchEdgeColor")
        self.SketchEdgeColor.setProperty(u"prefPath", u"View")

        self.gridLayout_4.addWidget(self.SketchEdgeColor, 1, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)

        self.InternalFaceColor = Gui_PrefColorButton(self.groupBox_3)
        self.InternalFaceColor.setObjectName(u"InternalFaceColor")
        sizePolicy.setHeightForWidth(self.InternalFaceColor.sizePolicy().hasHeightForWidth())
        self.InternalFaceColor.setSizePolicy(sizePolicy)
        self.InternalFaceColor.setProperty(u"color", QColor(84, 171, 255, 62))
        self.InternalFaceColor.setProperty(u"prefEntry", u"SketchFaceColor")
        self.InternalFaceColor.setProperty(u"prefPath", u"Mod/Sketcher/General")

        self.gridLayout_4.addWidget(self.InternalFaceColor, 2, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(SketcherGui__SketcherSettingsAppearance)

        self.EdgePattern.setCurrentIndex(-1)
        self.ConstructionPattern.setCurrentIndex(-1)
        self.InternalPattern.setCurrentIndex(-1)
        self.ExternalPattern.setCurrentIndex(-1)
        self.ExternalDefiningPattern.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(SketcherGui__SketcherSettingsAppearance)
    # setupUi

    def retranslateUi(self, SketcherGui__SketcherSettingsAppearance):
        SketcherGui__SketcherSettingsAppearance.setWindowTitle(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Appearance", None))
        self.groupBox.setTitle(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Working Colors", None))
        self.label_6.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Creating line", None))
#if QT_CONFIG(tooltip)
        self.CreateLineColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color used while new sketch elements are created", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Coordinate text", None))
#if QT_CONFIG(tooltip)
        self.CursorTextColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Text color of the coordinates", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Cursor crosshair", None))
#if QT_CONFIG(tooltip)
        self.CursorCrosshairColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of the crosshair cursor", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Geometric Element Colors", None))
        self.label_7.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Constrained", None))
        self.label_9.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Unconstrained", None))
        self.label_pattern.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Line Type", None))
        self.label_width.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Width", None))
        self.label.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Geometry", None))
#if QT_CONFIG(tooltip)
        self.FullyConstraintElementColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of fully constrained normal geometry in edit mode", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.EditedEdgeColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of normal geometry in edit mode", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.EdgePattern.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Line pattern of normal edges", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.EdgeWidth.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Width of normal edges", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Construction geometry", None))
#if QT_CONFIG(tooltip)
        self.FullyConstraintConstructionElementColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of fully constrained construction geometry in edit mode", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ConstructionColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of construction geometry in edit mode", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ConstructionPattern.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Line pattern of construction edges", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ConstructionWidth.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Width of construction edges", None))
#endif // QT_CONFIG(tooltip)
        self.label_ia.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Internal alignment geometry", None))
#if QT_CONFIG(tooltip)
        self.FullyConstraintInternalAlignmentColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of fully constrained internal alignment geometry in edit mode", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.InternalAlignedGeoColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of internal alignment geometry in edit mode", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.InternalPattern.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Line pattern of internal aligned edges", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.InternalWidth.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Width of internal aligned edges", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"External reference geometry", None))
#if QT_CONFIG(tooltip)
        self.ExternalColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of external geometry in edit mode", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ExternalPattern.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Line pattern of external reference edges", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ExternalWidth.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Width of external edges", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"External defining geometry", None))
#if QT_CONFIG(tooltip)
        self.ExternalDefiningColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of external defining geometry in edit mode", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ExternalDefiningPattern.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Line pattern of external defining edges", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ExternalDefiningWidth.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Width of external defining edges", None))
#endif // QT_CONFIG(tooltip)
        self.label_45.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Fully constrained sketch", None))
#if QT_CONFIG(tooltip)
        self.FullyConstrainedColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of geometry indicating a fully constrained sketch", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Invalid sketch", None))
#if QT_CONFIG(tooltip)
        self.InvalidSketchColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of geometry indicating an invalid sketch", None))
#endif // QT_CONFIG(tooltip)
        self.groupBoxSketcherColor.setTitle(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Constraint Colors", None))
        self.label_14.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Constraint symbols", None))
#if QT_CONFIG(tooltip)
        self.ConstrainedColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of driving constraints in edit mode", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Dimensional constraints", None))
#if QT_CONFIG(tooltip)
        self.DatumColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of dimensional driving constraints in edit mode", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Reference constraints", None))
#if QT_CONFIG(tooltip)
        self.NonDrivingConstraintColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of reference constraints in edit mode", None))
#endif // QT_CONFIG(tooltip)
        self.labelexpr.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Expression dependent constraint", None))
#if QT_CONFIG(tooltip)
        self.ExprBasedConstrDimColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of expression dependent constraints in edit mode", None))
#endif // QT_CONFIG(tooltip)
        self.labeldeact.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Deactivated constraints", None))
#if QT_CONFIG(tooltip)
        self.DeactivatedConstrDimColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of deactivated constraints in edit mode", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Colors Outside Sketcher", None))
        self.label_18.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Vertex", None))
#if QT_CONFIG(tooltip)
        self.SketchVertexColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of vertices outside edit mode", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Edge", None))
#if QT_CONFIG(tooltip)
        self.SketchEdgeColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of edges outside edit mode", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Face", None))
#if QT_CONFIG(tooltip)
        self.InternalFaceColor.setToolTip(QCoreApplication.translate("SketcherGui::SketcherSettingsAppearance", u"Color of internal faces formed by intersecting geometry or closed loops in the sketch", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

