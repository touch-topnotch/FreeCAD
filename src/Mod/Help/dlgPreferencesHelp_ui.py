# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgPreferencesHelp.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(504, 549)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton_2 = Gui_PrefRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setProperty(u"prefEntry", u"optionGithub")
        self.radioButton_2.setProperty(u"prefPath", u"Mod/Help")

        self.gridLayout.addWidget(self.radioButton_2, 2, 0, 1, 1)

        self.radioOffline = Gui_PrefRadioButton(self.groupBox)
        self.radioOffline.setObjectName(u"radioOffline")
        self.radioOffline.setProperty(u"prefEntry", u"optionCustom")
        self.radioOffline.setProperty(u"prefPath", u"Mod/Help")

        self.gridLayout.addWidget(self.radioOffline, 6, 0, 1, 1)

        self.lineEdit_2 = Gui_PrefLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_2.setProperty(u"prefEntry", u"Suffix")
        self.lineEdit_2.setProperty(u"prefPath", u"Mod/Help")

        self.gridLayout.addWidget(self.lineEdit_2, 7, 1, 1, 1)

        self.fileChooser = Gui_PrefFileChooser(self.groupBox)
        self.fileChooser.setObjectName(u"fileChooser")
        self.fileChooser.setMode(Gui.FileChooser.Directory)
        self.fileChooser.setProperty(u"prefEntry", u"Location")
        self.fileChooser.setProperty(u"prefPath", u"Mod/Help")

        self.gridLayout.addWidget(self.fileChooser, 6, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)

        self.radioButton = Gui_PrefRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)
        self.radioButton.setProperty(u"prefEntry", u"optionWiki")
        self.radioButton.setProperty(u"prefPath", u"Mod/Help")

        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioOnline = Gui_PrefRadioButton(self.groupBox)
        self.radioOnline.setObjectName(u"radioOnline")
        self.radioOnline.setChecked(False)
        self.radioOnline.setProperty(u"prefEntry", u"optionMarkdown")
        self.radioOnline.setProperty(u"prefPath", u"Mod/Help")

        self.gridLayout.addWidget(self.radioOnline, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_3)

        self.radioBrowser = Gui_PrefRadioButton(self.groupBox_2)
        self.radioBrowser.setObjectName(u"radioBrowser")
        self.radioBrowser.setChecked(True)
        self.radioBrowser.setProperty(u"prefEntry", u"optionBrowser")
        self.radioBrowser.setProperty(u"prefPath", u"Mod/Help")

        self.verticalLayout_3.addWidget(self.radioBrowser)

        self.radioTab = Gui_PrefRadioButton(self.groupBox_2)
        self.radioTab.setObjectName(u"radioTab")
        self.radioTab.setChecked(False)
        self.radioTab.setProperty(u"prefEntry", u"optionTab")
        self.radioTab.setProperty(u"prefPath", u"Mod/Help")

        self.verticalLayout_3.addWidget(self.radioTab)

        self.radioDialog = Gui_PrefRadioButton(self.groupBox_2)
        self.radioDialog.setObjectName(u"radioDialog")
        self.radioDialog.setEnabled(True)
        self.radioDialog.setProperty(u"prefEntry", u"optionDialog")
        self.radioDialog.setProperty(u"prefPath", u"Mod/Help")

        self.verticalLayout_3.addWidget(self.radioDialog)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.styleSheet = Gui_PrefFileChooser(self.groupBox_3)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setProperty(u"prefEntry", u"StyleSheet")
        self.styleSheet.setProperty(u"prefPath", u"Mod/Help")

        self.horizontalLayout.addWidget(self.styleSheet)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Help", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Source", None))
#if QT_CONFIG(tooltip)
        self.radioButton_2.setToolTip(QCoreApplication.translate("Form", u"Fetches the documentation from pages rendered on GitHub.\n"
"This is currently not available.", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"GitHub (online)", None))
#if QT_CONFIG(tooltip)
        self.radioOffline.setToolTip(QCoreApplication.translate("Form", u"Set this to a custom URL or the folder where the help files are located.\n"
"You can easily download the documentation for offline use by using the Addon\n"
"Manager and installing the \"offline-documentation\" addon. If this\n"
"field is left blank, FreeCAD will automatically search for the help files at\n"
"the default location ($USERAPPDATADIR/Mod/offline-documentation).", None))
#endif // QT_CONFIG(tooltip)
        self.radioOffline.setText(QCoreApplication.translate("Form", u"Custom location", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip(QCoreApplication.translate("Form", u"A translation suffix to use, for example \"fr\"\n"
"to get French translation of the documentation.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.fileChooser.setToolTip(QCoreApplication.translate("Form", u"Set this to a custom URL or the folder where the help files are located.\n"
"Documentation can be downloaded for offline use via the Addon Manager and installing the\n"
"\"offline-documentation\" addon. If this field is left blank, FreeCAD will\n"
"automatically search for the help files at the default location\n"
"($USERAPPDATADIR/Mod/offline-documentation).", None))
#endif // QT_CONFIG(tooltip)
        self.fileChooser.setFileName("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Translation suffix", None))
#if QT_CONFIG(tooltip)
        self.radioButton.setToolTip(QCoreApplication.translate("Form", u"The documentation pages will be fetched from the official\n"
"FreeCADwiki at https://wiki.freecad.org", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton.setText(QCoreApplication.translate("Form", u"FreeCAD Wiki (online)", None))
#if QT_CONFIG(tooltip)
        self.radioOnline.setToolTip(QCoreApplication.translate("Form", u"The documentation pages will be fetched from an automatic Markdown conversion\n"
"of the FreeCAD wiki,hosted on FreeCAD's GitHub account. This can be styled with a\n"
"custom stylesheet below and can look nicer than the wiki option. The 'Markdown' or\n"
"'Pandoc' Python module should be installed for optimal results.", None))
#endif // QT_CONFIG(tooltip)
        self.radioOnline.setText(QCoreApplication.translate("Form", u"Markdown version (online)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Display", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Note: if PySide Web components are not found on the system, help pages will open in the default web browser regardless of the options below.", None))
#if QT_CONFIG(tooltip)
        self.radioBrowser.setToolTip(QCoreApplication.translate("Form", u"The documentation will open in the default web browser", None))
#endif // QT_CONFIG(tooltip)
        self.radioBrowser.setText(QCoreApplication.translate("Form", u"In the default web browser", None))
#if QT_CONFIG(tooltip)
        self.radioTab.setToolTip(QCoreApplication.translate("Form", u"The documentation will open in a new tab inside the FreeCAD interface. This requires the PySide QtWebengineWidgets component.", None))
#endif // QT_CONFIG(tooltip)
        self.radioTab.setText(QCoreApplication.translate("Form", u"In a FreeCAD tab", None))
#if QT_CONFIG(tooltip)
        self.radioDialog.setToolTip(QCoreApplication.translate("Form", u"Documentation opens in a dockable dialog within FreeCAD, allowing simultaneous work in the 3D view.\n"
"Requires the PySide QtWebengineWidgets component.", None))
#endif // QT_CONFIG(tooltip)
        self.radioDialog.setText(QCoreApplication.translate("Form", u"In a separate, embeddable dialog", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Options", None))
        self.label.setText(QCoreApplication.translate("Form", u"Custom stylesheet", None))
#if QT_CONFIG(tooltip)
        self.styleSheet.setToolTip(QCoreApplication.translate("Form", u"Specify the path to an alternative CSS file for styling Markdown pages.\n"
"This only applies if Markdown is selected above.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

