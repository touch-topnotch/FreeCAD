# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgImportStep.ui'
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
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_PartGui_DlgImportStep(object):
    def setupUi(self, PartGui__DlgImportStep):
        if not PartGui__DlgImportStep.objectName():
            PartGui__DlgImportStep.setObjectName(u"PartGui__DlgImportStep")
        PartGui__DlgImportStep.resize(445, 365)
        self.gridLayout_4 = QGridLayout(PartGui__DlgImportStep)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.GroupBox2 = QGroupBox(PartGui__DlgImportStep)
        self.GroupBox2.setObjectName(u"GroupBox2")
        self.verticalLayout = QVBoxLayout(self.GroupBox2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBoxMergeCompound = Gui_PrefCheckBox(self.GroupBox2)
        self.checkBoxMergeCompound.setObjectName(u"checkBoxMergeCompound")
        self.checkBoxMergeCompound.setProperty(u"prefEntry", u"ReadShapeCompoundMode")
        self.checkBoxMergeCompound.setProperty(u"prefPath", u"Mod/Import/hSTEP")

        self.verticalLayout.addWidget(self.checkBoxMergeCompound)

        self.checkBoxUseLinkGroup = Gui_PrefCheckBox(self.GroupBox2)
        self.checkBoxUseLinkGroup.setObjectName(u"checkBoxUseLinkGroup")
        self.checkBoxUseLinkGroup.setProperty(u"prefEntry", u"UseLinkGroup")
        self.checkBoxUseLinkGroup.setProperty(u"prefPath", u"Mod/Import")

        self.verticalLayout.addWidget(self.checkBoxUseLinkGroup)

        self.checkBoxImportHiddenObj = Gui_PrefCheckBox(self.GroupBox2)
        self.checkBoxImportHiddenObj.setObjectName(u"checkBoxImportHiddenObj")
        self.checkBoxImportHiddenObj.setProperty(u"prefEntry", u"ImportHiddenObject")
        self.checkBoxImportHiddenObj.setProperty(u"prefPath", u"Mod/Import")

        self.verticalLayout.addWidget(self.checkBoxImportHiddenObj)

        self.checkBoxReduceObjects = Gui_PrefCheckBox(self.GroupBox2)
        self.checkBoxReduceObjects.setObjectName(u"checkBoxReduceObjects")
        self.checkBoxReduceObjects.setProperty(u"prefEntry", u"ReduceObjects")
        self.checkBoxReduceObjects.setProperty(u"prefPath", u"Mod/Import")

        self.verticalLayout.addWidget(self.checkBoxReduceObjects)

        self.checkBoxExpandCompound = Gui_PrefCheckBox(self.GroupBox2)
        self.checkBoxExpandCompound.setObjectName(u"checkBoxExpandCompound")
        self.checkBoxExpandCompound.setProperty(u"prefEntry", u"ExpandCompound")
        self.checkBoxExpandCompound.setProperty(u"prefPath", u"Mod/Import")

        self.verticalLayout.addWidget(self.checkBoxExpandCompound)

        self.checkBoxShowProgress = Gui_PrefCheckBox(self.GroupBox2)
        self.checkBoxShowProgress.setObjectName(u"checkBoxShowProgress")
        self.checkBoxShowProgress.setProperty(u"prefEntry", u"ShowProgress")
        self.checkBoxShowProgress.setProperty(u"prefPath", u"Mod/Import")

        self.verticalLayout.addWidget(self.checkBoxShowProgress)

        self.checkBoxUseBaseName = Gui_PrefCheckBox(self.GroupBox2)
        self.checkBoxUseBaseName.setObjectName(u"checkBoxUseBaseName")
        self.checkBoxUseBaseName.setProperty(u"prefEntry", u"UseBaseName")
        self.checkBoxUseBaseName.setProperty(u"prefPath", u"Mod/Import")

        self.verticalLayout.addWidget(self.checkBoxUseBaseName)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.GroupBox2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        self.label_6.setMinimumSize(QSize(197, 0))

        self.horizontalLayout_2.addWidget(self.label_6)

        self.comboBoxImportCodePage = Gui_PrefComboBox(self.GroupBox2)
        self.comboBoxImportCodePage.setObjectName(u"comboBoxImportCodePage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxImportCodePage.sizePolicy().hasHeightForWidth())
        self.comboBoxImportCodePage.setSizePolicy(sizePolicy)
        self.comboBoxImportCodePage.setProperty(u"prefEntry", u"ImportCodePage")
        self.comboBoxImportCodePage.setProperty(u"prefPath", u"Mod/Import")

        self.horizontalLayout_2.addWidget(self.comboBoxImportCodePage)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.GroupBox2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.comboBoxImportMode = Gui_PrefComboBox(self.GroupBox2)
        self.comboBoxImportMode.addItem("")
        self.comboBoxImportMode.addItem("")
        self.comboBoxImportMode.addItem("")
        self.comboBoxImportMode.addItem("")
        self.comboBoxImportMode.addItem("")
        self.comboBoxImportMode.setObjectName(u"comboBoxImportMode")
        sizePolicy.setHeightForWidth(self.comboBoxImportMode.sizePolicy().hasHeightForWidth())
        self.comboBoxImportMode.setSizePolicy(sizePolicy)
        self.comboBoxImportMode.setProperty(u"prefEntry", u"ImportMode")
        self.comboBoxImportMode.setProperty(u"prefPath", u"Mod/Import")

        self.horizontalLayout.addWidget(self.comboBoxImportMode)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_4.addWidget(self.GroupBox2, 1, 0, 1, 1)

        QWidget.setTabOrder(self.checkBoxMergeCompound, self.checkBoxUseLinkGroup)
        QWidget.setTabOrder(self.checkBoxUseLinkGroup, self.checkBoxImportHiddenObj)
        QWidget.setTabOrder(self.checkBoxImportHiddenObj, self.checkBoxReduceObjects)
        QWidget.setTabOrder(self.checkBoxReduceObjects, self.checkBoxExpandCompound)
        QWidget.setTabOrder(self.checkBoxExpandCompound, self.checkBoxUseBaseName)
        QWidget.setTabOrder(self.checkBoxUseBaseName, self.comboBoxImportMode)

        self.retranslateUi(PartGui__DlgImportStep)

        QMetaObject.connectSlotsByName(PartGui__DlgImportStep)
    # setupUi

    def retranslateUi(self, PartGui__DlgImportStep):
        PartGui__DlgImportStep.setWindowTitle(QCoreApplication.translate("PartGui::DlgImportStep", u"STEP Import Settings", None))
        self.GroupBox2.setTitle(QCoreApplication.translate("PartGui::DlgImportStep", u"Import", None))
#if QT_CONFIG(tooltip)
        self.checkBoxMergeCompound.setToolTip(QCoreApplication.translate("PartGui::DlgImportStep", u"Merges compounds during file reading (slower but higher details)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxMergeCompound.setText(QCoreApplication.translate("PartGui::DlgImportStep", u"Enable STEP compound merge", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUseLinkGroup.setToolTip(QCoreApplication.translate("PartGui::DlgImportStep", u"Select this to use App::LinkGroup as group container, or else use App::Part", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUseLinkGroup.setText(QCoreApplication.translate("PartGui::DlgImportStep", u"Use LinkGroup", None))
#if QT_CONFIG(tooltip)
        self.checkBoxImportHiddenObj.setToolTip(QCoreApplication.translate("PartGui::DlgImportStep", u"Select this to import invisible objects", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxImportHiddenObj.setText(QCoreApplication.translate("PartGui::DlgImportStep", u"Import invisible objects", None))
#if QT_CONFIG(tooltip)
        self.checkBoxReduceObjects.setToolTip(QCoreApplication.translate("PartGui::DlgImportStep", u"Reduce number of objects using Link array", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxReduceObjects.setText(QCoreApplication.translate("PartGui::DlgImportStep", u"Reduce number of objects", None))
#if QT_CONFIG(tooltip)
        self.checkBoxExpandCompound.setToolTip(QCoreApplication.translate("PartGui::DlgImportStep", u"Expand compound shape with multiple solids", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxExpandCompound.setText(QCoreApplication.translate("PartGui::DlgImportStep", u"Expand compound shape", None))
#if QT_CONFIG(tooltip)
        self.checkBoxShowProgress.setToolTip(QCoreApplication.translate("PartGui::DlgImportStep", u"Show progress bar when importing", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxShowProgress.setText(QCoreApplication.translate("PartGui::DlgImportStep", u"Show progress bar when importing", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUseBaseName.setToolTip(QCoreApplication.translate("PartGui::DlgImportStep", u"Do not use instance names. Useful for some legacy STEP files with non-meaningful auto-generated instance names.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUseBaseName.setText(QCoreApplication.translate("PartGui::DlgImportStep", u"Ignore instance names", None))
        self.label_6.setText(QCoreApplication.translate("PartGui::DlgImportStep", u"CodePage", None))
        self.label_5.setText(QCoreApplication.translate("PartGui::DlgImportStep", u"Mode", None))
        self.comboBoxImportMode.setItemText(0, QCoreApplication.translate("PartGui::DlgImportStep", u"Single document", None))
        self.comboBoxImportMode.setItemText(1, QCoreApplication.translate("PartGui::DlgImportStep", u"Assembly per document", None))
        self.comboBoxImportMode.setItemText(2, QCoreApplication.translate("PartGui::DlgImportStep", u"Assembly per document in sub-directory", None))
        self.comboBoxImportMode.setItemText(3, QCoreApplication.translate("PartGui::DlgImportStep", u"Object per document", None))
        self.comboBoxImportMode.setItemText(4, QCoreApplication.translate("PartGui::DlgImportStep", u"Object per document in sub-directory", None))

    # retranslateUi

