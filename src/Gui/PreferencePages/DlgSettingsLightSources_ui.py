# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsLightSources.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_Gui_Dialog_DlgSettingsLightSources(object):
    def setupUi(self, Gui__Dialog__DlgSettingsLightSources):
        if not Gui__Dialog__DlgSettingsLightSources.objectName():
            Gui__Dialog__DlgSettingsLightSources.setObjectName(u"Gui__Dialog__DlgSettingsLightSources")
        Gui__Dialog__DlgSettingsLightSources.resize(743, 515)
        self.gridLayout_2 = QGridLayout(Gui__Dialog__DlgSettingsLightSources)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBoxDirection = QGroupBox(Gui__Dialog__DlgSettingsLightSources)
        self.groupBoxDirection.setObjectName(u"groupBoxDirection")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBoxDirection.sizePolicy().hasHeightForWidth())
        self.groupBoxDirection.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.groupBoxDirection)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.viewer = Gui_View3DInventorViewer(self.groupBoxDirection)
        self.viewer.setObjectName(u"viewer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.viewer.sizePolicy().hasHeightForWidth())
        self.viewer.setSizePolicy(sizePolicy1)
        self.viewer.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.horizontalLayout = QHBoxLayout(self.viewer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, -1, 2, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.zoomInButton = QToolButton(self.viewer)
        self.zoomInButton.setObjectName(u"zoomInButton")
        self.zoomInButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/FreeCAD-default/scalable/zoom-in.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zoomInButton.setIcon(icon)
        self.zoomInButton.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.zoomInButton)

        self.zoomOutButton = QToolButton(self.viewer)
        self.zoomOutButton.setObjectName(u"zoomOutButton")
        self.zoomOutButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/FreeCAD-default/scalable/zoom-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zoomOutButton.setIcon(icon1)
        self.zoomOutButton.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.zoomOutButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_3.addWidget(self.viewer, 0, 0, 2, 1)


        self.gridLayout_2.addWidget(self.groupBoxDirection, 1, 0, 2, 1)

        self.bottomSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.bottomSpacer, 3, 0, 1, 1)

        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsLightSources)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.light1Label = QLabel(self.groupBox)
        self.light1Label.setObjectName(u"light1Label")

        self.gridLayout.addWidget(self.light1Label, 0, 4, 1, 1)

        self.ambientLightIntensitySpinBox = Gui_PrefSpinBox(self.groupBox)
        self.ambientLightIntensitySpinBox.setObjectName(u"ambientLightIntensitySpinBox")
        self.ambientLightIntensitySpinBox.setMaximum(100)
        self.ambientLightIntensitySpinBox.setValue(20)
        self.ambientLightIntensitySpinBox.setProperty(u"prefEntry", u"AmbientLightIntensity")
        self.ambientLightIntensitySpinBox.setProperty(u"prefPath", u"View/LightSources")

        self.gridLayout.addWidget(self.ambientLightIntensitySpinBox, 4, 6, 1, 1)

        self.backLightColor = Gui_PrefColorButton(self.groupBox)
        self.backLightColor.setObjectName(u"backLightColor")
        self.backLightColor.setColor(QColor(245, 245, 238))
        self.backLightColor.setProperty(u"prefEntry", u"BacklightColor")
        self.backLightColor.setProperty(u"prefPath", u"View/LightSources")

        self.gridLayout.addWidget(self.backLightColor, 2, 4, 1, 1)

        self.mainLightEnable = Gui_PrefCheckBox(self.groupBox)
        self.mainLightEnable.setObjectName(u"mainLightEnable")
        self.mainLightEnable.setChecked(True)
        self.mainLightEnable.setProperty(u"prefEntry", u"EnableHeadlight")
        self.mainLightEnable.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.mainLightEnable, 1, 0, 1, 1)

        self.backLightHorizontalAngle = Gui_QuantitySpinBox(self.groupBox)
        self.backLightHorizontalAngle.setObjectName(u"backLightHorizontalAngle")
        self.backLightHorizontalAngle.setProperty(u"unit", u"")
        self.backLightHorizontalAngle.setValue(-130.000000000000000)

        self.gridLayout.addWidget(self.backLightHorizontalAngle, 2, 2, 1, 1)

        self.backLightVerticalAngle = Gui_QuantitySpinBox(self.groupBox)
        self.backLightVerticalAngle.setObjectName(u"backLightVerticalAngle")
        self.backLightVerticalAngle.setProperty(u"unit", u"")
        self.backLightVerticalAngle.setValue(-10.000000000000000)

        self.gridLayout.addWidget(self.backLightVerticalAngle, 2, 3, 1, 1)

        self.backLightEnable = Gui_PrefCheckBox(self.groupBox)
        self.backLightEnable.setObjectName(u"backLightEnable")
        self.backLightEnable.setChecked(True)
        self.backLightEnable.setProperty(u"prefEntry", u"EnableBacklight")
        self.backLightEnable.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.backLightEnable, 2, 0, 1, 1)

        self.fillLightHorizontalAngle = Gui_QuantitySpinBox(self.groupBox)
        self.fillLightHorizontalAngle.setObjectName(u"fillLightHorizontalAngle")
        self.fillLightHorizontalAngle.setProperty(u"unit", u"")
        self.fillLightHorizontalAngle.setValue(-40.000000000000000)

        self.gridLayout.addWidget(self.fillLightHorizontalAngle, 3, 2, 1, 1)

        self.light1Label_2 = QLabel(self.groupBox)
        self.light1Label_2.setObjectName(u"light1Label_2")

        self.gridLayout.addWidget(self.light1Label_2, 0, 3, 1, 1)

        self.ambientLightColor = Gui_PrefColorButton(self.groupBox)
        self.ambientLightColor.setObjectName(u"ambientLightColor")
        self.ambientLightColor.setColor(QColor(255, 255, 255))
        self.ambientLightColor.setProperty(u"prefEntry", u"AmbientLightColor")
        self.ambientLightColor.setProperty(u"prefPath", u"View/LightSources")

        self.gridLayout.addWidget(self.ambientLightColor, 4, 4, 1, 1)

        self.light1Label_3 = QLabel(self.groupBox)
        self.light1Label_3.setObjectName(u"light1Label_3")

        self.gridLayout.addWidget(self.light1Label_3, 0, 2, 1, 1)

        self.mainLightIntensitySpinBox = Gui_PrefSpinBox(self.groupBox)
        self.mainLightIntensitySpinBox.setObjectName(u"mainLightIntensitySpinBox")
        self.mainLightIntensitySpinBox.setMaximum(100)
        self.mainLightIntensitySpinBox.setValue(90)
        self.mainLightIntensitySpinBox.setProperty(u"prefEntry", u"HeadlightIntensity")
        self.mainLightIntensitySpinBox.setProperty(u"prefPath", u"View/LightSources")

        self.gridLayout.addWidget(self.mainLightIntensitySpinBox, 1, 6, 1, 1)

        self.mainLightHorizontalAngle = Gui_QuantitySpinBox(self.groupBox)
        self.mainLightHorizontalAngle.setObjectName(u"mainLightHorizontalAngle")
        self.mainLightHorizontalAngle.setProperty(u"unit", u"")
        self.mainLightHorizontalAngle.setValue(100.000000000000000)

        self.gridLayout.addWidget(self.mainLightHorizontalAngle, 1, 2, 1, 1)

        self.fillLightVerticalAngle = Gui_QuantitySpinBox(self.groupBox)
        self.fillLightVerticalAngle.setObjectName(u"fillLightVerticalAngle")
        self.fillLightVerticalAngle.setProperty(u"unit", u"")
        self.fillLightVerticalAngle.setValue(5.000000000000000)

        self.gridLayout.addWidget(self.fillLightVerticalAngle, 3, 3, 1, 1)

        self.backLightIntensitySpinBox = Gui_PrefSpinBox(self.groupBox)
        self.backLightIntensitySpinBox.setObjectName(u"backLightIntensitySpinBox")
        self.backLightIntensitySpinBox.setMaximum(100)
        self.backLightIntensitySpinBox.setValue(60)
        self.backLightIntensitySpinBox.setProperty(u"prefEntry", u"BacklightIntensity")
        self.backLightIntensitySpinBox.setProperty(u"prefPath", u"View/LightSources")

        self.gridLayout.addWidget(self.backLightIntensitySpinBox, 2, 6, 1, 1)

        self.fillLightEnable = Gui_PrefCheckBox(self.groupBox)
        self.fillLightEnable.setObjectName(u"fillLightEnable")
        self.fillLightEnable.setChecked(True)
        self.fillLightEnable.setProperty(u"prefEntry", u"EnableFillLight")
        self.fillLightEnable.setProperty(u"prefPath", u"View")

        self.gridLayout.addWidget(self.fillLightEnable, 3, 0, 1, 1)

        self.fillLightIntensitySpinBox = Gui_PrefSpinBox(self.groupBox)
        self.fillLightIntensitySpinBox.setObjectName(u"fillLightIntensitySpinBox")
        self.fillLightIntensitySpinBox.setMaximum(100)
        self.fillLightIntensitySpinBox.setValue(40)
        self.fillLightIntensitySpinBox.setProperty(u"prefEntry", u"FillLightIntensity")
        self.fillLightIntensitySpinBox.setProperty(u"prefPath", u"View/LightSources")

        self.gridLayout.addWidget(self.fillLightIntensitySpinBox, 3, 6, 1, 1)

        self.light1Label_4 = QLabel(self.groupBox)
        self.light1Label_4.setObjectName(u"light1Label_4")

        self.gridLayout.addWidget(self.light1Label_4, 0, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.fillLightColor = Gui_PrefColorButton(self.groupBox)
        self.fillLightColor.setObjectName(u"fillLightColor")
        self.fillLightColor.setColor(QColor(230, 250, 255))
        self.fillLightColor.setProperty(u"prefEntry", u"FillLightColor")
        self.fillLightColor.setProperty(u"prefPath", u"View/LightSources")

        self.gridLayout.addWidget(self.fillLightColor, 3, 4, 1, 1)

        self.mainLightVerticalAngle = Gui_QuantitySpinBox(self.groupBox)
        self.mainLightVerticalAngle.setObjectName(u"mainLightVerticalAngle")
        self.mainLightVerticalAngle.setProperty(u"unit", u"")
        self.mainLightVerticalAngle.setValue(-46.000000000000000)

        self.gridLayout.addWidget(self.mainLightVerticalAngle, 1, 3, 1, 1)

        self.mainLightColor = Gui_PrefColorButton(self.groupBox)
        self.mainLightColor.setObjectName(u"mainLightColor")
        self.mainLightColor.setColor(QColor(255, 255, 255))
        self.mainLightColor.setProperty(u"prefEntry", u"HeadlightColor")
        self.mainLightColor.setProperty(u"prefPath", u"View/LightSources")

        self.gridLayout.addWidget(self.mainLightColor, 1, 4, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        QWidget.setTabOrder(self.mainLightEnable, self.mainLightHorizontalAngle)
        QWidget.setTabOrder(self.mainLightHorizontalAngle, self.mainLightVerticalAngle)
        QWidget.setTabOrder(self.mainLightVerticalAngle, self.mainLightColor)
        QWidget.setTabOrder(self.mainLightColor, self.mainLightIntensitySpinBox)
        QWidget.setTabOrder(self.mainLightIntensitySpinBox, self.backLightEnable)
        QWidget.setTabOrder(self.backLightEnable, self.backLightHorizontalAngle)
        QWidget.setTabOrder(self.backLightHorizontalAngle, self.backLightVerticalAngle)
        QWidget.setTabOrder(self.backLightVerticalAngle, self.backLightColor)
        QWidget.setTabOrder(self.backLightColor, self.backLightIntensitySpinBox)
        QWidget.setTabOrder(self.backLightIntensitySpinBox, self.fillLightEnable)
        QWidget.setTabOrder(self.fillLightEnable, self.fillLightHorizontalAngle)
        QWidget.setTabOrder(self.fillLightHorizontalAngle, self.fillLightVerticalAngle)
        QWidget.setTabOrder(self.fillLightVerticalAngle, self.fillLightColor)
        QWidget.setTabOrder(self.fillLightColor, self.fillLightIntensitySpinBox)
        QWidget.setTabOrder(self.fillLightIntensitySpinBox, self.ambientLightColor)
        QWidget.setTabOrder(self.ambientLightColor, self.ambientLightIntensitySpinBox)

        self.retranslateUi(Gui__Dialog__DlgSettingsLightSources)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsLightSources)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsLightSources):
        Gui__Dialog__DlgSettingsLightSources.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"Light Sources", None))
        self.groupBoxDirection.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"Preview", None))
#if QT_CONFIG(tooltip)
        self.zoomInButton.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"Pushes in", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.zoomOutButton.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"Pulls out", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"Light Sources", None))
        self.light1Label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"Color", None))
        self.ambientLightIntensitySpinBox.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"%", None))
        self.mainLightEnable.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"Main light", None))
        self.backLightEnable.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"Backlight", None))
        self.light1Label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"Vertical angle", None))
        self.light1Label_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"Horizontal angle", None))
        self.mainLightIntensitySpinBox.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"%", None))
        self.backLightIntensitySpinBox.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"%", None))
        self.fillLightEnable.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"Fill light", None))
        self.fillLightIntensitySpinBox.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"%", None))
        self.light1Label_4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"Intensity", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsLightSources", u"Ambient light", None))
    # retranslateUi

