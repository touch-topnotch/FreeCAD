# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgImportExportIges.ui'
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
    QGroupBox, QLabel, QLineEdit, QRadioButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_PartGui_DlgImportExportIges(object):
    def setupUi(self, PartGui__DlgImportExportIges):
        if not PartGui__DlgImportExportIges.objectName():
            PartGui__DlgImportExportIges.setObjectName(u"PartGui__DlgImportExportIges")
        PartGui__DlgImportExportIges.resize(515, 446)
        self.gridLayout_5 = QGridLayout(PartGui__DlgImportExportIges)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox = QGroupBox(PartGui__DlgImportExportIges)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.spacerItem = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.spacerItem, 0, 1, 1, 1)

        self.comboBoxUnits = QComboBox(self.groupBox)
        self.comboBoxUnits.addItem("")
        self.comboBoxUnits.addItem("")
        self.comboBoxUnits.addItem("")
        self.comboBoxUnits.setObjectName(u"comboBoxUnits")

        self.gridLayout_4.addWidget(self.comboBoxUnits, 0, 2, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButtonBRepOff = QRadioButton(self.groupBox_3)
        self.radioButtonBRepOff.setObjectName(u"radioButtonBRepOff")
        self.radioButtonBRepOff.setChecked(True)

        self.gridLayout.addWidget(self.radioButtonBRepOff, 0, 0, 1, 1)

        self.radioButtonBRepOn = QRadioButton(self.groupBox_3)
        self.radioButtonBRepOn.setObjectName(u"radioButtonBRepOn")

        self.gridLayout.addWidget(self.radioButtonBRepOn, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 3)


        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(PartGui__DlgImportExportIges)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkSkipBlank = QCheckBox(self.groupBox_2)
        self.checkSkipBlank.setObjectName(u"checkSkipBlank")

        self.gridLayout_3.addWidget(self.checkSkipBlank, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBoxHeader = QGroupBox(PartGui__DlgImportExportIges)
        self.groupBoxHeader.setObjectName(u"groupBoxHeader")
        self.gridLayout_2 = QGridLayout(self.groupBoxHeader)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBoxHeader)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEditCompany = QLineEdit(self.groupBoxHeader)
        self.lineEditCompany.setObjectName(u"lineEditCompany")

        self.gridLayout_2.addWidget(self.lineEditCompany, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBoxHeader)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEditAuthor = QLineEdit(self.groupBoxHeader)
        self.lineEditAuthor.setObjectName(u"lineEditAuthor")

        self.gridLayout_2.addWidget(self.lineEditAuthor, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBoxHeader)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEditProduct = QLineEdit(self.groupBoxHeader)
        self.lineEditProduct.setObjectName(u"lineEditProduct")

        self.gridLayout_2.addWidget(self.lineEditProduct, 2, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBoxHeader, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 82, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 3, 0, 1, 1)

        QWidget.setTabOrder(self.comboBoxUnits, self.radioButtonBRepOff)
        QWidget.setTabOrder(self.radioButtonBRepOff, self.radioButtonBRepOn)
        QWidget.setTabOrder(self.radioButtonBRepOn, self.checkSkipBlank)
        QWidget.setTabOrder(self.checkSkipBlank, self.lineEditCompany)
        QWidget.setTabOrder(self.lineEditCompany, self.lineEditAuthor)
        QWidget.setTabOrder(self.lineEditAuthor, self.lineEditProduct)

        self.retranslateUi(PartGui__DlgImportExportIges)

        QMetaObject.connectSlotsByName(PartGui__DlgImportExportIges)
    # setupUi

    def retranslateUi(self, PartGui__DlgImportExportIges):
        PartGui__DlgImportExportIges.setWindowTitle(QCoreApplication.translate("PartGui::DlgImportExportIges", u"IGES", None))
        self.groupBox.setTitle(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Export", None))
        self.label.setText(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Units for export of IGES", None))
        self.comboBoxUnits.setItemText(0, QCoreApplication.translate("PartGui::DlgImportExportIges", u"Millimeter", None))
        self.comboBoxUnits.setItemText(1, QCoreApplication.translate("PartGui::DlgImportExportIges", u"Meter", None))
        self.comboBoxUnits.setItemText(2, QCoreApplication.translate("PartGui::DlgImportExportIges", u"Inch", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Export Solids and Shells As", None))
#if QT_CONFIG(tooltip)
        self.radioButtonBRepOff.setToolTip(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Solids and shells will be exported as trimmed surface", None))
#endif // QT_CONFIG(tooltip)
        self.radioButtonBRepOff.setText(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Groups of Trimmed Surfaces (type 144)", None))
#if QT_CONFIG(tooltip)
        self.radioButtonBRepOn.setToolTip(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Solids will be exported as manifold solid B-rep object, shells as shell", None))
#endif // QT_CONFIG(tooltip)
        self.radioButtonBRepOn.setText(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Solids (type 186) and shells (type 514) / B-rep mode", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Import", None))
#if QT_CONFIG(tooltip)
        self.checkSkipBlank.setToolTip(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Blank entities will not be imported", None))
#endif // QT_CONFIG(tooltip)
        self.checkSkipBlank.setText(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Skip blank entities", None))
#if QT_CONFIG(tooltip)
        self.groupBoxHeader.setToolTip(QCoreApplication.translate("PartGui::DlgImportExportIges", u"If not empty, field contents will be used in the IGES file header", None))
#endif // QT_CONFIG(tooltip)
        self.groupBoxHeader.setTitle(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Header", None))
        self.label_2.setText(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Company", None))
        self.label_4.setText(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Author", None))
        self.label_3.setText(QCoreApplication.translate("PartGui::DlgImportExportIges", u"Product", None))
    # retranslateUi

