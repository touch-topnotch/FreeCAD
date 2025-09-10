# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Advanced.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_PathGui_DlgSettingsPathColor(object):
    def setupUi(self, PathGui__DlgSettingsPathColor):
        if not PathGui__DlgSettingsPathColor.objectName():
            PathGui__DlgSettingsPathColor.setObjectName(u"PathGui__DlgSettingsPathColor")
        PathGui__DlgSettingsPathColor.resize(487, 691)
        self.verticalLayout_3 = QVBoxLayout(PathGui__DlgSettingsPathColor)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(PathGui__DlgSettingsPathColor)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.WarningSuppressAllSpeeds = Gui_PrefCheckBox(self.groupBox)
        self.WarningSuppressAllSpeeds.setObjectName(u"WarningSuppressAllSpeeds")
        self.WarningSuppressAllSpeeds.setChecked(True)
        self.WarningSuppressAllSpeeds.setProperty(u"prefEntry", u"WarningSuppressAllSpeeds")
        self.WarningSuppressAllSpeeds.setProperty(u"prefPath", u"Mod/CAM")

        self.verticalLayout.addWidget(self.WarningSuppressAllSpeeds)

        self.WarningSuppressRapidSpeeds = Gui_PrefCheckBox(self.groupBox)
        self.WarningSuppressRapidSpeeds.setObjectName(u"WarningSuppressRapidSpeeds")
        self.WarningSuppressRapidSpeeds.setChecked(True)
        self.WarningSuppressRapidSpeeds.setProperty(u"prefEntry", u"WarningSuppressRapidSpeeds")
        self.WarningSuppressRapidSpeeds.setProperty(u"prefPath", u"Mod/CAM")

        self.verticalLayout.addWidget(self.WarningSuppressRapidSpeeds)

        self.WarningSuppressVelocity = Gui_PrefCheckBox(self.groupBox)
        self.WarningSuppressVelocity.setObjectName(u"WarningSuppressVelocity")
        self.WarningSuppressVelocity.setChecked(False)
        self.WarningSuppressVelocity.setProperty(u"prefEntry", u"WarningSuppressVelocity")
        self.WarningSuppressVelocity.setProperty(u"prefPath", u"Mod/CAM")

        self.verticalLayout.addWidget(self.WarningSuppressVelocity)

        self.WarningSuppressSelectionMode = Gui_PrefCheckBox(self.groupBox)
        self.WarningSuppressSelectionMode.setObjectName(u"WarningSuppressSelectionMode")
        self.WarningSuppressSelectionMode.setChecked(True)
        self.WarningSuppressSelectionMode.setProperty(u"prefEntry", u"WarningSuppressSelectionMode")
        self.WarningSuppressSelectionMode.setProperty(u"prefPath", u"Mod/CAM")

        self.verticalLayout.addWidget(self.WarningSuppressSelectionMode)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(PathGui__DlgSettingsPathColor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.EnableAdvancedOCLFeatures = Gui_PrefCheckBox(self.groupBox_2)
        self.EnableAdvancedOCLFeatures.setObjectName(u"EnableAdvancedOCLFeatures")
        self.EnableAdvancedOCLFeatures.setProperty(u"prefEntry", u"EnableAdvancedOCLFeatures")
        self.EnableAdvancedOCLFeatures.setProperty(u"prefPath", u"Mod/CAM")

        self.verticalLayout_2.addWidget(self.EnableAdvancedOCLFeatures)

        self.WarningSuppressOpenCamLib = Gui_PrefCheckBox(self.groupBox_2)
        self.WarningSuppressOpenCamLib.setObjectName(u"WarningSuppressOpenCamLib")
        self.WarningSuppressOpenCamLib.setChecked(True)
        self.WarningSuppressOpenCamLib.setProperty(u"prefEntry", u"WarningSuppressOpenCamLib")
        self.WarningSuppressOpenCamLib.setProperty(u"prefPath", u"Mod/CAM")

        self.verticalLayout_2.addWidget(self.WarningSuppressOpenCamLib)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 217, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(PathGui__DlgSettingsPathColor)

        QMetaObject.connectSlotsByName(PathGui__DlgSettingsPathColor)
    # setupUi

    def retranslateUi(self, PathGui__DlgSettingsPathColor):
        PathGui__DlgSettingsPathColor.setWindowTitle(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Advanced", None))
        self.groupBox.setTitle(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Warnings", None))
#if QT_CONFIG(tooltip)
        self.WarningSuppressAllSpeeds.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Suppress all warnings about setting speed rates for accurate cycle time calculation", None))
#endif // QT_CONFIG(tooltip)
        self.WarningSuppressAllSpeeds.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Suppress all missing speeds warning", None))
#if QT_CONFIG(tooltip)
        self.WarningSuppressRapidSpeeds.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Suppress warning about setting the rapid speed rates for accurate cycle time calculation. Ignored if all speed warnings are already suppressed.", None))
#endif // QT_CONFIG(tooltip)
        self.WarningSuppressRapidSpeeds.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Suppress missing rapid speeds warning", None))
#if QT_CONFIG(tooltip)
        self.WarningSuppressVelocity.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Suppress warning whenever a Path selection mode is activated", None))
#endif // QT_CONFIG(tooltip)
        self.WarningSuppressVelocity.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Suppress feed rate warning", None))
#if QT_CONFIG(tooltip)
        self.WarningSuppressSelectionMode.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Suppress warning whenever a Path selection mode is activated", None))
#endif // QT_CONFIG(tooltip)
        self.WarningSuppressSelectionMode.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Suppress selection mode warning", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"OpenCAMLib", None))
        self.label.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"If OpenCAMLib is installed with Python bindings it can be used by some additional 3D operations. NOTE: Enabling OpenCAMLib here requires a restart of FreeCAD to take effect.", None))
        self.EnableAdvancedOCLFeatures.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Enable OCL dependent features", None))
#if QT_CONFIG(tooltip)
        self.WarningSuppressOpenCamLib.setToolTip(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Suppress warning if openCAMlib cannot be found", None))
#endif // QT_CONFIG(tooltip)
        self.WarningSuppressOpenCamLib.setText(QCoreApplication.translate("PathGui::DlgSettingsPathColor", u"Suppress openCAMlib warning", None))
    # retranslateUi

