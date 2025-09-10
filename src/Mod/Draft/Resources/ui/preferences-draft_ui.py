# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-draft.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsDraft(object):
    def setupUi(self, Gui__Dialog__DlgSettingsDraft):
        if not Gui__Dialog__DlgSettingsDraft.objectName():
            Gui__Dialog__DlgSettingsDraft.setObjectName(u"Gui__Dialog__DlgSettingsDraft")
        Gui__Dialog__DlgSettingsDraft.resize(500, 560)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsDraft)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(11, 11, 11, 11)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.groupBox_1 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.gridLayout_1 = QGridLayout(self.groupBox_1)
        self.gridLayout_1.setSpacing(6)
        self.gridLayout_1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.label_precision = QLabel(self.groupBox_1)
        self.label_precision.setObjectName(u"label_precision")

        self.gridLayout_1.addWidget(self.label_precision, 0, 0, 1, 1)

        self.spinBox_precision = Gui_PrefSpinBox(self.groupBox_1)
        self.spinBox_precision.setObjectName(u"spinBox_precision")
        self.spinBox_precision.setMinimumSize(QSize(140, 0))
        self.spinBox_precision.setMaximum(10)
        self.spinBox_precision.setValue(6)
        self.spinBox_precision.setProperty(u"prefEntry", u"precision")
        self.spinBox_precision.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.spinBox_precision, 0, 1, 1, 1)

        self.horizontalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_1.addItem(self.horizontalSpacer_1, 0, 2, 1, 1)

        self.label_defaultWP = QLabel(self.groupBox_1)
        self.label_defaultWP.setObjectName(u"label_defaultWP")

        self.gridLayout_1.addWidget(self.label_defaultWP, 1, 0, 1, 1)

        self.comboBox_defaultWP = Gui_PrefComboBox(self.groupBox_1)
        self.comboBox_defaultWP.addItem("")
        self.comboBox_defaultWP.addItem("")
        self.comboBox_defaultWP.addItem("")
        self.comboBox_defaultWP.addItem("")
        self.comboBox_defaultWP.setObjectName(u"comboBox_defaultWP")
        self.comboBox_defaultWP.setProperty(u"prefEntry", u"defaultWP")
        self.comboBox_defaultWP.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.comboBox_defaultWP, 1, 1, 1, 1)

        self.checkBox_showPlaneTracker = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_showPlaneTracker.setObjectName(u"checkBox_showPlaneTracker")
        self.checkBox_showPlaneTracker.setProperty(u"prefEntry", u"showPlaneTracker")
        self.checkBox_showPlaneTracker.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.checkBox_showPlaneTracker, 2, 0, 1, 3)

        self.checkBox_AutogroupAddGroups = Gui_PrefCheckBox(self.groupBox_1)
        self.checkBox_AutogroupAddGroups.setObjectName(u"checkBox_AutogroupAddGroups")
        self.checkBox_AutogroupAddGroups.setProperty(u"prefEntry", u"AutogroupAddGroups")
        self.checkBox_AutogroupAddGroups.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.checkBox_AutogroupAddGroups, 3, 0, 1, 3)


        self.vboxLayout.addWidget(self.groupBox_1)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_ToolMessages = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_ToolMessages.setObjectName(u"checkBox_ToolMessages")
        self.checkBox_ToolMessages.setProperty(u"prefEntry", u"ToolMessages")
        self.checkBox_ToolMessages.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.checkBox_ToolMessages, 0, 0, 1, 3)

        self.checkBox_focusOnLength = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_focusOnLength.setObjectName(u"checkBox_focusOnLength")
        self.checkBox_focusOnLength.setProperty(u"prefEntry", u"focusOnLength")
        self.checkBox_focusOnLength.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.checkBox_focusOnLength, 1, 0, 1, 3)

        self.checkBox_selectBaseObjects = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_selectBaseObjects.setObjectName(u"checkBox_selectBaseObjects")
        self.checkBox_selectBaseObjects.setProperty(u"prefEntry", u"selectBaseObjects")
        self.checkBox_selectBaseObjects.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.checkBox_selectBaseObjects, 2, 0, 1, 3)

        self.checkBox_UsePartPrimitives = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_UsePartPrimitives.setObjectName(u"checkBox_UsePartPrimitives")
        self.checkBox_UsePartPrimitives.setProperty(u"prefEntry", u"UsePartPrimitives")
        self.checkBox_UsePartPrimitives.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.checkBox_UsePartPrimitives, 3, 0, 1, 3)

        self.checkBox_preserveFaceColor = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_preserveFaceColor.setObjectName(u"checkBox_preserveFaceColor")
        self.checkBox_preserveFaceColor.setProperty(u"prefEntry", u"preserveFaceColor")
        self.checkBox_preserveFaceColor.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.checkBox_preserveFaceColor, 4, 0, 1, 3)

        self.checkBox_preserveFaceNames = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_preserveFaceNames.setObjectName(u"checkBox_preserveFaceNames")
        self.checkBox_preserveFaceNames.setProperty(u"prefEntry", u"preserveFaceNames")
        self.checkBox_preserveFaceNames.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.checkBox_preserveFaceNames, 5, 0, 1, 3)

        self.label_MouseDelay = QLabel(self.groupBox_2)
        self.label_MouseDelay.setObjectName(u"label_MouseDelay")

        self.gridLayout_2.addWidget(self.label_MouseDelay, 6, 0, 1, 1)

        self.spinBox_MouseDelay = Gui_PrefSpinBox(self.groupBox_2)
        self.spinBox_MouseDelay.setObjectName(u"spinBox_MouseDelay")
        self.spinBox_MouseDelay.setMaximum(10000)
        self.spinBox_MouseDelay.setValue(1)
        self.spinBox_MouseDelay.setProperty(u"prefEntry", u"MouseDelay")
        self.spinBox_MouseDelay.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.spinBox_MouseDelay, 6, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 6, 2, 1, 1)

        self.label_DraftEditMaxObjects = QLabel(self.groupBox_2)
        self.label_DraftEditMaxObjects.setObjectName(u"label_DraftEditMaxObjects")

        self.gridLayout_2.addWidget(self.label_DraftEditMaxObjects, 7, 0, 1, 1)

        self.spinBox_DraftEditMaxObjects = Gui_PrefSpinBox(self.groupBox_2)
        self.spinBox_DraftEditMaxObjects.setObjectName(u"spinBox_DraftEditMaxObjects")
        self.spinBox_DraftEditMaxObjects.setMinimum(1)
        self.spinBox_DraftEditMaxObjects.setMaximum(25)
        self.spinBox_DraftEditMaxObjects.setValue(5)
        self.spinBox_DraftEditMaxObjects.setDisplayIntegerBase(10)
        self.spinBox_DraftEditMaxObjects.setProperty(u"prefEntry", u"DraftEditMaxObjects")
        self.spinBox_DraftEditMaxObjects.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.spinBox_DraftEditMaxObjects, 7, 1, 1, 1)

        self.label_DraftEditPickRadius = QLabel(self.groupBox_2)
        self.label_DraftEditPickRadius.setObjectName(u"label_DraftEditPickRadius")

        self.gridLayout_2.addWidget(self.label_DraftEditPickRadius, 8, 0, 1, 1)

        self.spinBox_DraftEditPickRadius = Gui_PrefSpinBox(self.groupBox_2)
        self.spinBox_DraftEditPickRadius.setObjectName(u"spinBox_DraftEditPickRadius")
        self.spinBox_DraftEditPickRadius.setMinimum(1)
        self.spinBox_DraftEditPickRadius.setValue(20)
        self.spinBox_DraftEditPickRadius.setProperty(u"prefEntry", u"DraftEditPickRadius")
        self.spinBox_DraftEditPickRadius.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.spinBox_DraftEditPickRadius, 8, 1, 1, 1)

        self.label_ClonePrefix = QLabel(self.groupBox_2)
        self.label_ClonePrefix.setObjectName(u"label_ClonePrefix")

        self.gridLayout_2.addWidget(self.label_ClonePrefix, 9, 0, 1, 1)

        self.lineEdit_ClonePrefix = Gui_PrefLineEdit(self.groupBox_2)
        self.lineEdit_ClonePrefix.setObjectName(u"lineEdit_ClonePrefix")
        self.lineEdit_ClonePrefix.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_ClonePrefix.setProperty(u"prefEntry", u"ClonePrefix")
        self.lineEdit_ClonePrefix.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.lineEdit_ClonePrefix, 9, 1, 1, 1)

        self.label_constructiongroupname = QLabel(self.groupBox_2)
        self.label_constructiongroupname.setObjectName(u"label_constructiongroupname")

        self.gridLayout_2.addWidget(self.label_constructiongroupname, 10, 0, 1, 1)

        self.lineEdit_constructiongroupname = Gui_PrefLineEdit(self.groupBox_2)
        self.lineEdit_constructiongroupname.setObjectName(u"lineEdit_constructiongroupname")
        self.lineEdit_constructiongroupname.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_constructiongroupname.setProperty(u"prefEntry", u"constructiongroupname")
        self.lineEdit_constructiongroupname.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.lineEdit_constructiongroupname, 10, 1, 1, 1)

        self.label_constructioncolor = QLabel(self.groupBox_2)
        self.label_constructioncolor.setObjectName(u"label_constructioncolor")

        self.gridLayout_2.addWidget(self.label_constructioncolor, 11, 0, 1, 1)

        self.colorButton_constructioncolor = Gui_PrefColorButton(self.groupBox_2)
        self.colorButton_constructioncolor.setObjectName(u"colorButton_constructioncolor")
        self.colorButton_constructioncolor.setProperty(u"color", QColor(44, 125, 255))
        self.colorButton_constructioncolor.setProperty(u"prefEntry", u"constructioncolor")
        self.colorButton_constructioncolor.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.colorButton_constructioncolor, 11, 1, 1, 1)


        self.vboxLayout.addWidget(self.groupBox_2)

        self.verticalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer_1)


        self.retranslateUi(Gui__Dialog__DlgSettingsDraft)

        self.comboBox_defaultWP.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsDraft)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsDraft):
        Gui__Dialog__DlgSettingsDraft.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"General", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"General", None))
        self.label_precision.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Internal precision level", None))
#if QT_CONFIG(tooltip)
        self.spinBox_precision.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The number of decimals used in internal coordinate operations (for example 3 = 0.001).\n"
"Values between 6 and 8 are usually considered the best trade-off.", None))
#endif // QT_CONFIG(tooltip)
        self.label_defaultWP.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Default working plane", None))
        self.comboBox_defaultWP.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Automatic", None))
        self.comboBox_defaultWP.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"XY (Top)", None))
        self.comboBox_defaultWP.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"XZ (Front)", None))
        self.comboBox_defaultWP.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"YZ (Side)", None))

#if QT_CONFIG(tooltip)
        self.comboBox_defaultWP.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default working plane for new views. If set to \"Automatic\" the working plane\n"
"will automatically align with the current view whenever a command is started.\n"
"Additionally it will align to preselected planar faces, or when points on planar\n"
"faces are picked during commands.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_showPlaneTracker.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, a widget indicating the current working\n"
"plane orientation appears when picking points", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_showPlaneTracker.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Show working plane tracker", None))
#if QT_CONFIG(tooltip)
        self.checkBox_AutogroupAddGroups.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, the layers drop-down list also includes groups.\n"
"Objects can then automatically be added to groups as well.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_AutogroupAddGroups.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Include groups in layer list", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Command options", None))
#if QT_CONFIG(tooltip)
        self.checkBox_ToolMessages.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, instructions are displayed in the Report view when using Draft commands", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_ToolMessages.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Show prompts in the Report view", None))
#if QT_CONFIG(tooltip)
        self.checkBox_focusOnLength.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, Length input, instead of the X coordinate, will have the initial focus.\n"
"This allows indicating a direction and then type a distance.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_focusOnLength.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Set focus on Length instead of X coordinate", None))
#if QT_CONFIG(tooltip)
        self.checkBox_selectBaseObjects.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, base objects, instead of created copies, are selected after copying", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_selectBaseObjects.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Select base objects after copying", None))
#if QT_CONFIG(tooltip)
        self.checkBox_UsePartPrimitives.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, Draft commands will create Part primitives instead of Draft objects.\n"
"Note that this is not fully supported, and many objects will not be editable with\n"
"Draft modification commands.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_UsePartPrimitives.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Create Part primitives if possible", None))
#if QT_CONFIG(tooltip)
        self.checkBox_preserveFaceColor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, Draft Downgrade and Draft Upgrade will keep face colors.\n"
"Only for the splitFaces and makeShell options.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_preserveFaceColor.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Keep face colors during downgrade/upgrade", None))
#if QT_CONFIG(tooltip)
        self.checkBox_preserveFaceNames.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, Draft Downgrade and Draft Upgrade will keep face names.\n"
"Only for the splitFaces and makeShell options.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_preserveFaceNames.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Keep face names during downgrade/upgrade", None))
        self.label_MouseDelay.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Mouse delay", None))
#if QT_CONFIG(tooltip)
        self.spinBox_MouseDelay.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"This is a delay during which the mouse is inactive, after entering numbers\n"
"manually in any of the coordinate fields. Setting this to 0 disables the delay.\n"
"If a delay of 1 is set, after entering a numeric value, the mouse will not\n"
"update the field anymore during one second, to avoid moving the mouse\n"
"accidentally and modifying the entered value.", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_MouseDelay.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u" seconds", None))
        self.label_DraftEditMaxObjects.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Max. number of editable objects", None))
#if QT_CONFIG(tooltip)
        self.spinBox_DraftEditMaxObjects.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The maximum number of objects Draft Edit is allowed to process at the same time", None))
#endif // QT_CONFIG(tooltip)
        self.label_DraftEditPickRadius.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Edit node pick radius", None))
#if QT_CONFIG(tooltip)
        self.spinBox_DraftEditPickRadius.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The pick radius of edit nodes", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox_DraftEditPickRadius.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u" px", None))
        self.label_ClonePrefix.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Label prefix for clones", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_ClonePrefix.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default prefix added to the label of new clones", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_ClonePrefix.setText("")
        self.label_constructiongroupname.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Construction group label", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_constructiongroupname.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default label for the construction geometry group", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_constructiongroupname.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Construction", None))
        self.label_constructioncolor.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Construction geometry color", None))
#if QT_CONFIG(tooltip)
        self.colorButton_constructioncolor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default color for Draft objects in construction mode", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

