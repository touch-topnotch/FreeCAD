# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogSetup.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFontComboBox, QGridLayout,
    QLabel, QLineEdit, QScrollArea, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_BIMSetupDialog(object):
    def setupUi(self, BIMSetupDialog):
        if not BIMSetupDialog.objectName():
            BIMSetupDialog.setObjectName(u"BIMSetupDialog")
        BIMSetupDialog.setWindowModality(Qt.WindowModal)
        BIMSetupDialog.resize(640, 691)
        self.verticalLayout = QVBoxLayout(BIMSetupDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(BIMSetupDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.label_18 = QLabel(BIMSetupDialog)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout.addWidget(self.label_18)

        self.scrollArea = QScrollArea(BIMSetupDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -546, 667, 871))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 11, 0, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 4, 0, 1, 1)

        self.settingNewdocument = QCheckBox(self.scrollAreaWidgetContents)
        self.settingNewdocument.setObjectName(u"settingNewdocument")

        self.gridLayout.addWidget(self.settingNewdocument, 15, 1, 1, 1)

        self.comboPresets = QComboBox(self.scrollAreaWidgetContents)
        self.comboPresets.addItem("")
        self.comboPresets.addItem("")
        self.comboPresets.addItem("")
        self.comboPresets.addItem("")
        self.comboPresets.setObjectName(u"comboPresets")

        self.gridLayout.addWidget(self.comboPresets, 0, 1, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 6, 0, 1, 1)

        self.settingUnits = QComboBox(self.scrollAreaWidgetContents)
        self.settingUnits.addItem("")
        self.settingUnits.addItem("")
        self.settingUnits.addItem("")
        self.settingUnits.addItem("")
        self.settingUnits.addItem("")
        self.settingUnits.addItem("")
        self.settingUnits.setObjectName(u"settingUnits")

        self.gridLayout.addWidget(self.settingUnits, 3, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 16, 0, 1, 1)

        self.settingDecimals = QSpinBox(self.scrollAreaWidgetContents)
        self.settingDecimals.setObjectName(u"settingDecimals")
        self.settingDecimals.setValue(2)

        self.gridLayout.addWidget(self.settingDecimals, 4, 1, 1, 1)

        self.settingSquares = QSpinBox(self.scrollAreaWidgetContents)
        self.settingSquares.setObjectName(u"settingSquares")
        self.settingSquares.setValue(10)

        self.gridLayout.addWidget(self.settingSquares, 6, 1, 1, 1)

        self.settingDimstyle = QComboBox(self.scrollAreaWidgetContents)
        self.settingDimstyle.addItem("")
        self.settingDimstyle.addItem("")
        self.settingDimstyle.addItem("")
        self.settingDimstyle.addItem("")
        self.settingDimstyle.setObjectName(u"settingDimstyle")

        self.gridLayout.addWidget(self.settingDimstyle, 11, 1, 1, 1)

        self.label_28 = QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 17, 0, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 7, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 15, 0, 1, 1)

        self.label_27 = QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_5.addWidget(self.label_19)

        self.label_31 = QLabel(self.scrollAreaWidgetContents)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_5.addWidget(self.label_31)

        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_5.addWidget(self.label_22)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_5.addWidget(self.label_13)


        self.gridLayout.addLayout(self.verticalLayout_5, 2, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)

        self.settingLinewidth = QSpinBox(self.scrollAreaWidgetContents)
        self.settingLinewidth.setObjectName(u"settingLinewidth")
        self.settingLinewidth.setValue(2)

        self.gridLayout.addWidget(self.settingLinewidth, 10, 1, 1, 1)

        self.settingBackupfiles = QSpinBox(self.scrollAreaWidgetContents)
        self.settingBackupfiles.setObjectName(u"settingBackupfiles")
        self.settingBackupfiles.setValue(1)

        self.gridLayout.addWidget(self.settingBackupfiles, 16, 1, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 14, 0, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)

        self.settingGrid = Gui_InputField(self.scrollAreaWidgetContents)
        self.settingGrid.setObjectName(u"settingGrid")
        self.settingGrid.setProperty(u"unit", u"")

        self.gridLayout.addWidget(self.settingGrid, 5, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.colorButtonConstruction = Gui_ColorButton(self.scrollAreaWidgetContents)
        self.colorButtonConstruction.setObjectName(u"colorButtonConstruction")

        self.gridLayout_2.addWidget(self.colorButtonConstruction, 3, 3, 1, 1)

        self.colorButtonFaces = Gui_ColorButton(self.scrollAreaWidgetContents)
        self.colorButtonFaces.setObjectName(u"colorButtonFaces")

        self.gridLayout_2.addWidget(self.colorButtonFaces, 2, 3, 1, 1)

        self.label_25 = QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 3, 2, 1, 1)

        self.label_26 = QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 3, 0, 1, 1)

        self.label_24 = QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 2, 2, 1, 1)

        self.colorButtonHelpers = Gui_ColorButton(self.scrollAreaWidgetContents)
        self.colorButtonHelpers.setObjectName(u"colorButtonHelpers")

        self.gridLayout_2.addWidget(self.colorButtonHelpers, 3, 1, 1, 1)

        self.label_23 = QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_2.addWidget(self.label_23, 2, 0, 1, 1)

        self.colorButtonLines = Gui_ColorButton(self.scrollAreaWidgetContents)
        self.colorButtonLines.setObjectName(u"colorButtonLines")

        self.gridLayout_2.addWidget(self.colorButtonLines, 2, 1, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)

        self.colorButtonTop = Gui_ColorButton(self.scrollAreaWidgetContents)
        self.colorButtonTop.setObjectName(u"colorButtonTop")

        self.gridLayout_2.addWidget(self.colorButtonTop, 0, 1, 1, 1)

        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 0, 2, 1, 1)

        self.colorButtonBottom = Gui_ColorButton(self.scrollAreaWidgetContents)
        self.colorButtonBottom.setObjectName(u"colorButtonBottom")

        self.gridLayout_2.addWidget(self.colorButtonBottom, 0, 3, 1, 1)

        self.label_29 = QLabel(self.scrollAreaWidgetContents)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 1, 0, 1, 1)

        self.label_30 = QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_2.addWidget(self.label_30, 1, 2, 1, 1)

        self.colorButtonSimple = Gui_PrefColorButton(self.scrollAreaWidgetContents)
        self.colorButtonSimple.setObjectName(u"colorButtonSimple")

        self.gridLayout_2.addWidget(self.colorButtonSimple, 1, 1, 1, 1)

        self.colorButtonText = Gui_PrefColorButton(self.scrollAreaWidgetContents)
        self.colorButtonText.setObjectName(u"colorButtonText")

        self.gridLayout_2.addWidget(self.colorButtonText, 1, 3, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 1, 1, 1)

        self.settingCameraHeight = QSpinBox(self.scrollAreaWidgetContents)
        self.settingCameraHeight.setObjectName(u"settingCameraHeight")
        self.settingCameraHeight.setMaximum(99999)
        self.settingCameraHeight.setValue(5)

        self.gridLayout.addWidget(self.settingCameraHeight, 17, 1, 1, 1)

        self.settingAuthor = QLineEdit(self.scrollAreaWidgetContents)
        self.settingAuthor.setObjectName(u"settingAuthor")

        self.gridLayout.addWidget(self.settingAuthor, 13, 1, 1, 1)

        self.settingText = Gui_InputField(self.scrollAreaWidgetContents)
        self.settingText.setObjectName(u"settingText")
        self.settingText.setProperty(u"unit", u"")

        self.gridLayout.addWidget(self.settingText, 8, 1, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 12, 0, 1, 1)

        self.settingLicense = QComboBox(self.scrollAreaWidgetContents)
        self.settingLicense.addItem("")
        self.settingLicense.addItem(u"CC-BY")
        self.settingLicense.addItem(u"CC-BY-SA")
        self.settingLicense.addItem(u"CC-BY-NC")
        self.settingLicense.addItem(u"CC-BY-SA-NC")
        self.settingLicense.addItem("")
        self.settingLicense.setObjectName(u"settingLicense")

        self.gridLayout.addWidget(self.settingLicense, 14, 1, 1, 1)

        self.settingArrowsize = Gui_InputField(self.scrollAreaWidgetContents)
        self.settingArrowsize.setObjectName(u"settingArrowsize")
        self.settingArrowsize.setProperty(u"unit", u"")

        self.gridLayout.addWidget(self.settingArrowsize, 12, 1, 1, 1)

        self.settingFont = QFontComboBox(self.scrollAreaWidgetContents)
        self.settingFont.setObjectName(u"settingFont")

        self.gridLayout.addWidget(self.settingFont, 9, 1, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 13, 0, 1, 1)

        self.settingWP = QComboBox(self.scrollAreaWidgetContents)
        self.settingWP.addItem("")
        self.settingWP.addItem("")
        self.settingWP.addItem("")
        self.settingWP.addItem("")
        self.settingWP.setObjectName(u"settingWP")

        self.gridLayout.addWidget(self.settingWP, 7, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.labelSnapTip = QLabel(BIMSetupDialog)
        self.labelSnapTip.setObjectName(u"labelSnapTip")
        self.labelSnapTip.setWordWrap(True)

        self.verticalLayout.addWidget(self.labelSnapTip)

        self.labelVersion = QLabel(BIMSetupDialog)
        self.labelVersion.setObjectName(u"labelVersion")
        self.labelVersion.setWordWrap(True)
        self.labelVersion.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.verticalLayout.addWidget(self.labelVersion)

        self.labelMissingWorkbenches = QLabel(BIMSetupDialog)
        self.labelMissingWorkbenches.setObjectName(u"labelMissingWorkbenches")
        self.labelMissingWorkbenches.setWordWrap(True)

        self.verticalLayout.addWidget(self.labelMissingWorkbenches)

        self.labelIfcOpenShell = QLabel(BIMSetupDialog)
        self.labelIfcOpenShell.setObjectName(u"labelIfcOpenShell")
        self.labelIfcOpenShell.setWordWrap(True)
        self.labelIfcOpenShell.setOpenExternalLinks(False)

        self.verticalLayout.addWidget(self.labelIfcOpenShell)

        self.buttonBox = QDialogButtonBox(BIMSetupDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(BIMSetupDialog)
        self.buttonBox.rejected.connect(BIMSetupDialog.reject)
        self.buttonBox.accepted.connect(BIMSetupDialog.accept)

        QMetaObject.connectSlotsByName(BIMSetupDialog)
    # setupUi

    def retranslateUi(self, BIMSetupDialog):
        BIMSetupDialog.setWindowTitle(QCoreApplication.translate("BIMSetupDialog", u"BIM Setup", None))
        self.label_2.setText(QCoreApplication.translate("BIMSetupDialog", u"This dialog will help you to set FreeCAD up for efficient BIM workflow by setting a couple of typical FreeCAD options. This dialog can be accessed again anytime from menu Manage -> Setup, and more options are available under menu Edit -> Preferences.", None))
        self.label_18.setText(QCoreApplication.translate("BIMSetupDialog", u"Hover your mouse on each setting for additional info.", None))
        self.label_7.setText(QCoreApplication.translate("BIMSetupDialog", u"Default dimension style", None))
        self.label_14.setText(QCoreApplication.translate("BIMSetupDialog", u"Number of decimals", None))
#if QT_CONFIG(tooltip)
        self.settingNewdocument.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>Check this to make FreeCAD start with a new blank document. Location in preferences: <span style=\" font-weight:600;\">General &gt; Document &gt; Create new document at startup</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.settingNewdocument.setText("")
        self.comboPresets.setItemText(0, QCoreApplication.translate("BIMSetupDialog", u"Choose your preferred working unit...", None))
        self.comboPresets.setItemText(1, QCoreApplication.translate("BIMSetupDialog", u"Centimeters", None))
        self.comboPresets.setItemText(2, QCoreApplication.translate("BIMSetupDialog", u"Meters", None))
        self.comboPresets.setItemText(3, QCoreApplication.translate("BIMSetupDialog", u"US / Imperial", None))

#if QT_CONFIG(tooltip)
        self.comboPresets.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"Choose one of the presets in this list to fill all the settings below with predetermined values. Then, adjust to your likings", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("BIMSetupDialog", u"Main grid line every", None))
        self.settingUnits.setItemText(0, QCoreApplication.translate("BIMSetupDialog", u"millimeters", None))
        self.settingUnits.setItemText(1, QCoreApplication.translate("BIMSetupDialog", u"centimeters", None))
        self.settingUnits.setItemText(2, QCoreApplication.translate("BIMSetupDialog", u"meters", None))
        self.settingUnits.setItemText(3, QCoreApplication.translate("BIMSetupDialog", u"inches", None))
        self.settingUnits.setItemText(4, QCoreApplication.translate("BIMSetupDialog", u"feet", None))
        self.settingUnits.setItemText(5, QCoreApplication.translate("BIMSetupDialog", u"architectural", None))

#if QT_CONFIG(tooltip)
        self.settingUnits.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>The unit you prefer to work with, that will be used everywhere: in dialogs, measurements and dimensions. However, you can enter any other unit anytime. For example, if you configured FreeCAD to work in millimeters, you can still enter measures as &quot;10m&quot; or &quot;5ft&quot;. You can also change the default unit system anytime without causing any modification to your model. Location in preferences: <span style=\" font-weight:600;\">General &gt; Default unit system</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("BIMSetupDialog", u"Default text size", None))
        self.label_12.setText(QCoreApplication.translate("BIMSetupDialog", u"Number of backup files", None))
#if QT_CONFIG(tooltip)
        self.settingDecimals.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>The number of decimals you wish to see used in the interface controls and measurements. Location in preferences: <span style=\" font-weight:600;\">General &gt; Units &gt; Number of decimals</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.settingSquares.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>How many small squares between each main line of the grid. Location in preferences: <span style=\" font-weight:600;\">Draft &gt; Grid and snapping &gt; Main line every</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.settingSquares.setSuffix(QCoreApplication.translate("BIMSetupDialog", u" square(s)", None))
        self.settingDimstyle.setItemText(0, QCoreApplication.translate("BIMSetupDialog", u"dot", None))
        self.settingDimstyle.setItemText(1, QCoreApplication.translate("BIMSetupDialog", u"arrow", None))
        self.settingDimstyle.setItemText(2, QCoreApplication.translate("BIMSetupDialog", u"slash", None))
        self.settingDimstyle.setItemText(3, QCoreApplication.translate("BIMSetupDialog", u"thick slash", None))

#if QT_CONFIG(tooltip)
        self.settingDimstyle.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>Default dimension style. Location in preferences: <span style=\" font-weight:600;\">Draft &gt; Texts and dimensions &gt; Arrow style, TechDraw &gt; TechDraw 2 &gt; Arrow Style</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText(QCoreApplication.translate("BIMSetupDialog", u"Default camera altitude", None))
        self.label_15.setText(QCoreApplication.translate("BIMSetupDialog", u"Default grid position", None))
        self.label.setText(QCoreApplication.translate("BIMSetupDialog", u"Preferred working units", None))
        self.label_11.setText(QCoreApplication.translate("BIMSetupDialog", u"Open a new document at startup", None))
        self.label_27.setText(QCoreApplication.translate("BIMSetupDialog", u"Fill with default values", None))
        self.label_19.setText(QCoreApplication.translate("BIMSetupDialog", u"3D view background", None))
        self.label_31.setText("")
        self.label_22.setText(QCoreApplication.translate("BIMSetupDialog", u"Geometry color", None))
        self.label_13.setText("")
        self.label_5.setText(QCoreApplication.translate("BIMSetupDialog", u"Default font", None))
#if QT_CONFIG(tooltip)
        self.settingLinewidth.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>Default line width. Location in preferences: <span style=\" font-weight:600;\">Display &gt; Part colors &gt; Default line width, Draft &gt; Visual settings &gt; Default line width</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.settingLinewidth.setSuffix(QCoreApplication.translate("BIMSetupDialog", u" px", None))
#if QT_CONFIG(tooltip)
        self.settingBackupfiles.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>The number of backup files to keep when saving a file. Location in preferences: <span style=\" font-weight:600;\">General &gt; Document &gt; Maximum number of backup files</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("BIMSetupDialog", u"Default size of a grid square", None))
        self.label_9.setText(QCoreApplication.translate("BIMSetupDialog", u"Default license for new files", None))
        self.label_6.setText(QCoreApplication.translate("BIMSetupDialog", u"Default line width", None))
#if QT_CONFIG(tooltip)
        self.settingGrid.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>This is the size of the smallest square of the grid. Location in preferences: <span style=\" font-weight:600;\">Draft &gt; Grid and snapping &gt; Grid spacing</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.settingGrid.setText(QCoreApplication.translate("BIMSetupDialog", u"0 ", None))
#if QT_CONFIG(tooltip)
        self.colorButtonConstruction.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>The default color of construction geometry. Location in preferences: <span style=\" font-weight:600;\">Draft &gt; General &gt; Construction geometry color</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.colorButtonFaces.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>The default color of faces in the 3D view. Location in preferences: <span style=\" font-weight:600;\">Display &gt; Part Color &gt; Default shape color</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("BIMSetupDialog", u"Construction:", None))
        self.label_26.setText(QCoreApplication.translate("BIMSetupDialog", u"Helpers:", None))
        self.label_24.setText(QCoreApplication.translate("BIMSetupDialog", u"Faces:", None))
#if QT_CONFIG(tooltip)
        self.colorButtonHelpers.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>The default color for helper objects such as grids and axes. Location in preferences: <span style=\" font-weight:600;\">BIM  &gt; Defaults &gt; Helpers</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_23.setText(QCoreApplication.translate("BIMSetupDialog", u"Lines:", None))
#if QT_CONFIG(tooltip)
        self.colorButtonLines.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>The default color of lines in the 3D view. Location in preferences: <span style=\" font-weight:600;\">Display &gt; Part Colors &gt; Default line color, Draft &gt; Visual settings &gt; Default line color</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("BIMSetupDialog", u"Gradient top:", None))
#if QT_CONFIG(tooltip)
        self.colorButtonTop.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>The top color of the 3D view background gradient. Location in preferences: <span style=\" font-weight:600;\">Display &gt; Colors &gt; Color gradient</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText(QCoreApplication.translate("BIMSetupDialog", u"Gradient bottom:", None))
#if QT_CONFIG(tooltip)
        self.colorButtonBottom.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>The bottom color of the 3D view background gradient. Location in preferences: <span style=\" font-weight:600;\">Display &gt; Colors &gt; Color gradient</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("BIMSetupDialog", u"Plain background:", None))
        self.label_30.setText(QCoreApplication.translate("BIMSetupDialog", u"Text:", None))
#if QT_CONFIG(tooltip)
        self.colorButtonSimple.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"The background color when switched to simple color", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.colorButtonText.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"The color to use for texts and dimensions", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.settingCameraHeight.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"This is the altitude of the camera when you create a blank file. Good values are between 5 (view a few centimeters wide) and 5000 (view a few meters wide)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.settingAuthor.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>Your name (optional). You can also add your email like this: John Doe &lt;john@doe.com&gt;. Location in preferences: <span style=\" font-weight:600;\">General &gt; Document &gt; Author name</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.settingAuthor.setText("")
#if QT_CONFIG(tooltip)
        self.settingText.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>The default size of texts and dimension texts. Location in preferences: <span style=\" font-weight:600;\">Draft &gt; Texts and dimensions &gt; Font size, TechDraw &gt; TechDraw 2 &gt; Font size</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.settingText.setText(QCoreApplication.translate("BIMSetupDialog", u"0 ", None))
        self.label_16.setText(QCoreApplication.translate("BIMSetupDialog", u"Default dimension arrow size", None))
        self.settingLicense.setItemText(0, QCoreApplication.translate("BIMSetupDialog", u"All rights reserved (no specific license)", None))
        self.settingLicense.setItemText(5, "")

#if QT_CONFIG(tooltip)
        self.settingLicense.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>Optional license you wish to use for new files. Keep &quot;All rights reserved&quot; if you don't wish to use any particular license. Location in preferences: <span style=\" font-weight:600;\">General &gt; Document &gt; Default license</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.settingArrowsize.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>Default dimension arrow size. Location in preferences: <span style=\" font-weight:600;\">TechDraw &gt; TechDraw 2 &gt; Arrow size, Draft &gt; Texts and dimensions &gt; Arrow size</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.settingArrowsize.setText(QCoreApplication.translate("BIMSetupDialog", u"0 ", None))
#if QT_CONFIG(tooltip)
        self.settingFont.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>Default font. Location in preferences: <span style=\" font-weight:600;\">Draft &gt; Texts and dimensions &gt; Font family, TechDraw &gt; TechDraw 1 &gt; Label Font</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("BIMSetupDialog", u"Default author for new files", None))
        self.settingWP.setItemText(0, QCoreApplication.translate("BIMSetupDialog", u"Auto (continuously adapts to the current view)", None))
        self.settingWP.setItemText(1, QCoreApplication.translate("BIMSetupDialog", u"Top (XY)", None))
        self.settingWP.setItemText(2, QCoreApplication.translate("BIMSetupDialog", u"Front (XZ)", None))
        self.settingWP.setItemText(3, QCoreApplication.translate("BIMSetupDialog", u"Side (YZ)", None))

#if QT_CONFIG(tooltip)
        self.settingWP.setToolTip(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p>Where the grid appears at FreeCAD startup. Location in preferences: <span style=\" font-weight:600;\">Draft &gt; General &gt; Default working plane</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelSnapTip.setText(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Tip</span>: You might also want to set the appropriate snapping modes on the Snapping toolbar. Enabling only the snap positions that you need will make drawing in FreeCAD considerably faster.</p></body></html>", None))
        self.labelVersion.setText(QCoreApplication.translate("BIMSetupDialog", u"<html><head/><body><p><b>Tip</b>: You are currently using FreeCAD version %1. Consider using the <a href=\"https://github.com/FreeCAD/FreeCAD/releases\"><span style=\" text-decoration: underline; color:#0000ff;\">latest development version %2</span></a>, which brings all the latest improvements to FreeCAD.</p></body></html>", None))
        self.labelMissingWorkbenches.setText(QCoreApplication.translate("BIMSetupDialog", u"Missing Workbenches", None))
        self.labelIfcOpenShell.setText(QCoreApplication.translate("BIMSetupDialog", u"<b>IfcOpenShell</b> is missing on your system. IfcOpenShell is needed to import or export IFC files to/from FreeCAD. Check <a href=\"https://www.freecadweb.org/wiki/Arch_IFC\">this wiki page</a> to know more, or <a href=\"#install\">download and install it</a> directly.</p>", None))
    # retranslateUi

