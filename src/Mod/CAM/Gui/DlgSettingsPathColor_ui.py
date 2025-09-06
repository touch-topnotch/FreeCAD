# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsPathColor.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QSizePolicy, QSpacerItem, QWidget)

class Ui_PathGui_DlgSettingsPathColor(object):
    def setupUi(self, PathGui__DlgSettingsPathColor):
        if not PathGui__DlgSettingsPathColor.objectName():
            PathGui__DlgSettingsPathColor.setObjectName(u"PathGui__DlgSettingsPathColor")
        PathGui__DlgSettingsPathColor.resize(722, 718)
        self.formLayout = QFormLayout(PathGui__DlgSettingsPathColor)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.verticalSpacer = QSpacerItem(20, 217, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(2, QFormLayout.SpanningRole, self.verticalSpacer)

        self.groupBoxDefaultColors = QGroupBox(PathGui__DlgSettingsPathColor)
        self.groupBoxDefaultColors.setObjectName(u"groupBoxDefaultColors")
        self.gridLayout = QGridLayout(self.groupBoxDefaultColors)
        self.gridLayout.setObjectName(u"gridLayout")
        self.DefaultPathLineWidth = Gui_PrefSpinBox(self.groupBoxDefaultColors)
        self.DefaultPathLineWidth.setObjectName(u"DefaultPathLineWidth")
        self.DefaultPathLineWidth.setSuffix(u" px")
        self.DefaultPathLineWidth.setMaximum(9)
        self.DefaultPathLineWidth.setValue(1)
        self.DefaultPathLineWidth.setProperty(u"prefEntry", u"DefaultPathLineWidth")
        self.DefaultPathLineWidth.setProperty(u"prefPath", u"Mod/CAM")

        self.gridLayout.addWidget(self.DefaultPathLineWidth, 1, 1, 1, 1)

        self.label_11 = QLabel(self.groupBoxDefaultColors)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)

        self.label_6 = QLabel(self.groupBoxDefaultColors)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.DefaultBBoxNormalColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.DefaultBBoxNormalColor.setObjectName(u"DefaultBBoxNormalColor")
        self.DefaultBBoxNormalColor.setColor(QColor(255, 255, 255))
        self.DefaultBBoxNormalColor.setProperty(u"prefEntry", u"DefaultBBoxNormalColor")
        self.DefaultBBoxNormalColor.setProperty(u"prefPath", u"Mod/CAM")

        self.gridLayout.addWidget(self.DefaultBBoxNormalColor, 6, 1, 1, 1)

        self.label_13 = QLabel(self.groupBoxDefaultColors)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)

        self.DefaultNormalPathColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.DefaultNormalPathColor.setObjectName(u"DefaultNormalPathColor")
        self.DefaultNormalPathColor.setColor(QColor(0, 170, 0))
        self.DefaultNormalPathColor.setProperty(u"prefEntry", u"DefaultNormalPathColor")
        self.DefaultNormalPathColor.setProperty(u"prefPath", u"Mod/CAM")

        self.gridLayout.addWidget(self.DefaultNormalPathColor, 0, 1, 1, 1)

        self.DefaultRapidPathColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.DefaultRapidPathColor.setObjectName(u"DefaultRapidPathColor")
        self.DefaultRapidPathColor.setColor(QColor(170, 0, 0))
        self.DefaultRapidPathColor.setProperty(u"prefEntry", u"DefaultRapidPathColor")
        self.DefaultRapidPathColor.setProperty(u"prefPath", u"Mod/CAM")

        self.gridLayout.addWidget(self.DefaultRapidPathColor, 3, 1, 1, 1)

        self.label_8 = QLabel(self.groupBoxDefaultColors)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_7 = QLabel(self.groupBoxDefaultColors)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.DefaultHighlightPathColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.DefaultHighlightPathColor.setObjectName(u"DefaultHighlightPathColor")
        self.DefaultHighlightPathColor.setColor(QColor(255, 125, 0))
        self.DefaultHighlightPathColor.setProperty(u"prefEntry", u"DefaultHighlightPathColor")
        self.DefaultHighlightPathColor.setProperty(u"prefPath", u"Mod/CAM")

        self.gridLayout.addWidget(self.DefaultHighlightPathColor, 5, 1, 1, 1)

        self.label_14 = QLabel(self.groupBoxDefaultColors)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_14, 7, 0, 1, 1)

        self.label_10 = QLabel(self.groupBoxDefaultColors)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.DefaultPathMarkerColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.DefaultPathMarkerColor.setObjectName(u"DefaultPathMarkerColor")
        self.DefaultPathMarkerColor.setColor(QColor(85, 255, 0))
        self.DefaultPathMarkerColor.setProperty(u"prefEntry", u"DefaultPathMarkerColor")
        self.DefaultPathMarkerColor.setProperty(u"prefPath", u"Mod/CAM")

        self.gridLayout.addWidget(self.DefaultPathMarkerColor, 2, 1, 1, 1)

        self.label_9 = QLabel(self.groupBoxDefaultColors)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(182, 0))

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.DefaultProbePathColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.DefaultProbePathColor.setObjectName(u"DefaultProbePathColor")
        self.DefaultProbePathColor.setColor(QColor(255, 255, 5))
        self.DefaultProbePathColor.setProperty(u"prefEntry", u"DefaultProbePathColor")
        self.DefaultProbePathColor.setProperty(u"prefPath", u"Mod/CAM")

        self.gridLayout.addWidget(self.DefaultProbePathColor, 4, 1, 1, 1)

        self.DefaultBBoxSelectionColor = Gui_PrefColorButton(self.groupBoxDefaultColors)
        self.DefaultBBoxSelectionColor.setObjectName(u"DefaultBBoxSelectionColor")
        self.DefaultBBoxSelectionColor.setColor(QColor(200, 255, 255))
        self.DefaultBBoxSelectionColor.setProperty(u"prefEntry", u"DefaultBBoxSelectionColor")
        self.DefaultBBoxSelectionColor.setProperty(u"prefPath", u"Mod/CAM")

        self.gridLayout.addWidget(self.DefaultBBoxSelectionColor, 7, 1, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.groupBoxDefaultColors)

        self.groupBox_3 = QGroupBox(PathGui__DlgSettingsPathColor)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.formLayout_3 = QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.DefaultSelectionStyle = Gui_PrefComboBox(self.groupBox_3)
        self.DefaultSelectionStyle.addItem("")
        self.DefaultSelectionStyle.addItem("")
        self.DefaultSelectionStyle.addItem("")
        self.DefaultSelectionStyle.setObjectName(u"DefaultSelectionStyle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.DefaultSelectionStyle.sizePolicy().hasHeightForWidth())
        self.DefaultSelectionStyle.setSizePolicy(sizePolicy1)
        self.DefaultSelectionStyle.setProperty(u"prefEntry", u"DefaultSelectionStyle")
        self.DefaultSelectionStyle.setProperty(u"prefPath", u"Mod/CAM")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.DefaultSelectionStyle)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.DefaultTaskPanelLayout = Gui_PrefComboBox(self.groupBox_3)
        self.DefaultTaskPanelLayout.addItem("")
        self.DefaultTaskPanelLayout.addItem("")
        self.DefaultTaskPanelLayout.addItem("")
        self.DefaultTaskPanelLayout.addItem("")
        self.DefaultTaskPanelLayout.setObjectName(u"DefaultTaskPanelLayout")
        self.DefaultTaskPanelLayout.setProperty(u"prefEntry", u"DefaultTaskPanelLayout")
        self.DefaultTaskPanelLayout.setProperty(u"prefPath", u"Mod/CAM")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.DefaultTaskPanelLayout)


        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.groupBox_3)

        QWidget.setTabOrder(self.DefaultNormalPathColor, self.DefaultPathLineWidth)

        self.retranslateUi(PathGui__DlgSettingsPathColor)

        QMetaObject.connectSlotsByName(PathGui__DlgSettingsPathColor)
    # setupUi

    def retranslateUi(self, PathGui__DlgSettingsPathColor):
        PathGui__DlgSettingsPathColor.setWindowTitle(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"GUI", None))
        self.groupBoxDefaultColors.setTitle(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Default Path Colors", None))
#if QT_CONFIG(tooltip)
        self.DefaultPathLineWidth.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"The default line thickness for new shapes", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Path highlight color", None))
        self.label_6.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Default normal path color", None))
#if QT_CONFIG(tooltip)
        self.DefaultBBoxNormalColor.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"The default line color for new shapes", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Bounding box normal color", None))
#if QT_CONFIG(tooltip)
        self.DefaultNormalPathColor.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"The default color for new shapes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.DefaultRapidPathColor.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"The default line color for new shapes", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Probe path color", None))
        self.label_7.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Rapid path color", None))
#if QT_CONFIG(tooltip)
        self.DefaultHighlightPathColor.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"The default line color for new shapes", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Bounding box selection color", None))
        self.label_10.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Default path marker color", None))
#if QT_CONFIG(tooltip)
        self.DefaultPathMarkerColor.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"The default line color for new shapes", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Default pathline width", None))
#if QT_CONFIG(tooltip)
        self.DefaultProbePathColor.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"The default line color for new shapes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.DefaultBBoxSelectionColor.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"The default line color for new shapes", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"UI Settings", None))
        self.label_12.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Path selection style", None))
        self.DefaultSelectionStyle.setItemText(0, QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Shape", None))
        self.DefaultSelectionStyle.setItemText(1, QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Bounding box", None))
        self.DefaultSelectionStyle.setItemText(2, QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"None", None))

#if QT_CONFIG(tooltip)
        self.DefaultSelectionStyle.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Default path shape selection behavior in 3D viewer", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Task panel layout", None))
        self.DefaultTaskPanelLayout.setItemText(0, QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Classic", None))
        self.DefaultTaskPanelLayout.setItemText(1, QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Classic - reversed", None))
        self.DefaultTaskPanelLayout.setItemText(2, QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Multi-panel", None))
        self.DefaultTaskPanelLayout.setItemText(3, QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Multi-panel - reversed", None))

    # retranslateUi

