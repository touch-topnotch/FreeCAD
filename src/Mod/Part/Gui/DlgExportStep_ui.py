# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgExportStep.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QLabel, QSizePolicy, QWidget)

class Ui_PartGui_DlgExportStep(object):
    def setupUi(self, PartGui__DlgExportStep):
        if not PartGui__DlgExportStep.objectName():
            PartGui__DlgExportStep.setObjectName(u"PartGui__DlgExportStep")
        PartGui__DlgExportStep.resize(445, 278)
        self.gridLayout_4 = QGridLayout(PartGui__DlgExportStep)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(PartGui__DlgExportStep)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 6, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 5, 0, 1, 1)

        self.comboBoxUnits = QComboBox(self.groupBox)
        self.comboBoxUnits.addItem("")
        self.comboBoxUnits.addItem("")
        self.comboBoxUnits.addItem("")
        self.comboBoxUnits.setObjectName(u"comboBoxUnits")

        self.gridLayout_3.addWidget(self.comboBoxUnits, 5, 1, 1, 1)

        self.comboBoxSchema = QComboBox(self.groupBox)
        self.comboBoxSchema.addItem(u"AP203")
        self.comboBoxSchema.addItem(u"AP214 Committee Draft")
        self.comboBoxSchema.addItem(u"AP214 Draft International Standard")
        self.comboBoxSchema.addItem(u"AP214 International Standard")
        self.comboBoxSchema.addItem(u"AP242 Draft International Standard")
        self.comboBoxSchema.setObjectName(u"comboBoxSchema")

        self.gridLayout_3.addWidget(self.comboBoxSchema, 6, 1, 1, 1)

        self.checkBoxExportLegacy = Gui_PrefCheckBox(self.groupBox)
        self.checkBoxExportLegacy.setObjectName(u"checkBoxExportLegacy")
        self.checkBoxExportLegacy.setProperty(u"prefEntry", u"ExportLegacy")
        self.checkBoxExportLegacy.setProperty(u"prefPath", u"Mod/Import")

        self.gridLayout_3.addWidget(self.checkBoxExportLegacy, 4, 0, 1, 2)

        self.checkBoxKeepPlacement = Gui_PrefCheckBox(self.groupBox)
        self.checkBoxKeepPlacement.setObjectName(u"checkBoxKeepPlacement")
        self.checkBoxKeepPlacement.setProperty(u"prefEntry", u"ExportKeepPlacement")
        self.checkBoxKeepPlacement.setProperty(u"prefPath", u"Mod/Import")

        self.gridLayout_3.addWidget(self.checkBoxKeepPlacement, 3, 0, 1, 1)

        self.checkBoxExportHiddenObj = Gui_PrefCheckBox(self.groupBox)
        self.checkBoxExportHiddenObj.setObjectName(u"checkBoxExportHiddenObj")
        self.checkBoxExportHiddenObj.setProperty(u"prefEntry", u"ExportHiddenObject")
        self.checkBoxExportHiddenObj.setProperty(u"prefPath", u"Mod/Import")

        self.gridLayout_3.addWidget(self.checkBoxExportHiddenObj, 2, 0, 1, 2)

        self.checkBoxPcurves = QCheckBox(self.groupBox)
        self.checkBoxPcurves.setObjectName(u"checkBoxPcurves")

        self.gridLayout_3.addWidget(self.checkBoxPcurves, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        QWidget.setTabOrder(self.checkBoxPcurves, self.checkBoxExportHiddenObj)

        self.retranslateUi(PartGui__DlgExportStep)

        QMetaObject.connectSlotsByName(PartGui__DlgExportStep)
    # setupUi

    def retranslateUi(self, PartGui__DlgExportStep):
        PartGui__DlgExportStep.setWindowTitle(QCoreApplication.translate("PartGui::DlgExportStep", u"STEP Export Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("PartGui::DlgExportStep", u"Export", None))
        self.label_2.setText(QCoreApplication.translate("PartGui::DlgExportStep", u"Scheme", None))
        self.label.setText(QCoreApplication.translate("PartGui::DlgExportStep", u"Units for export of STEP", None))
        self.comboBoxUnits.setItemText(0, QCoreApplication.translate("PartGui::DlgExportStep", u"Millimeter", None))
        self.comboBoxUnits.setItemText(1, QCoreApplication.translate("PartGui::DlgExportStep", u"Meter", None))
        self.comboBoxUnits.setItemText(2, QCoreApplication.translate("PartGui::DlgExportStep", u"Inch", None))


        self.checkBoxExportLegacy.setText(QCoreApplication.translate("PartGui::DlgExportStep", u"Use legacy export function", None))
#if QT_CONFIG(tooltip)
        self.checkBoxKeepPlacement.setToolTip(QCoreApplication.translate("PartGui::DlgExportStep", u"Keeps the placement information when exporting\n"
"a single object. When importing back the STEP file, the\n"
"placement will be encoded into the shape geometry, instead of keeping\n"
"it inside the placement property.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxKeepPlacement.setText(QCoreApplication.translate("PartGui::DlgExportStep", u"Export single object placement", None))
#if QT_CONFIG(tooltip)
        self.checkBoxExportHiddenObj.setToolTip(QCoreApplication.translate("PartGui::DlgExportStep", u"Uncheck this to skip invisible objects when exporting, which is useful for CADs that do not support invisibility STEP styling.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxExportHiddenObj.setText(QCoreApplication.translate("PartGui::DlgExportStep", u"Export invisible objects", None))
        self.checkBoxPcurves.setText(QCoreApplication.translate("PartGui::DlgExportStep", u"Write out curves in parametric space of surface", None))
    # retranslateUi

