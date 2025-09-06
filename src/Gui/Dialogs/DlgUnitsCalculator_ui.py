# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgUnitsCalculator.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTextEdit,
    QWidget)

class Ui_Gui_Dialog_DlgUnitCalculator(object):
    def setupUi(self, Gui__Dialog__DlgUnitCalculator):
        if not Gui__Dialog__DlgUnitCalculator.objectName():
            Gui__Dialog__DlgUnitCalculator.setObjectName(u"Gui__Dialog__DlgUnitCalculator")
        Gui__Dialog__DlgUnitCalculator.resize(537, 262)
        self.gridLayout_2 = QGridLayout(Gui__Dialog__DlgUnitCalculator)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ValueInput = Gui_InputField(Gui__Dialog__DlgUnitCalculator)
        self.ValueInput.setObjectName(u"ValueInput")
        self.ValueInput.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.ValueInput)

        self.label = QLabel(Gui__Dialog__DlgUnitCalculator)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.UnitInput = QLineEdit(Gui__Dialog__DlgUnitCalculator)
        self.UnitInput.setObjectName(u"UnitInput")
        self.UnitInput.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.UnitInput)

        self.label_2 = QLabel(Gui__Dialog__DlgUnitCalculator)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.ValueOutput = QLineEdit(Gui__Dialog__DlgUnitCalculator)
        self.ValueOutput.setObjectName(u"ValueOutput")
        self.ValueOutput.setMinimumSize(QSize(150, 0))
        self.ValueOutput.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.ValueOutput)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.textEdit = QTextEdit(Gui__Dialog__DlgUnitCalculator)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 1)

        self.groupBox = QGroupBox(Gui__Dialog__DlgUnitCalculator)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.quantitySpinBox = Gui_QuantitySpinBox(self.groupBox)
        self.quantitySpinBox.setObjectName(u"quantitySpinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quantitySpinBox.sizePolicy().hasHeightForWidth())
        self.quantitySpinBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.quantitySpinBox, 0, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.comboBoxScheme = QComboBox(self.groupBox)
        self.comboBoxScheme.setObjectName(u"comboBoxScheme")

        self.gridLayout.addWidget(self.comboBoxScheme, 0, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.spinBoxDecimals = QSpinBox(self.groupBox)
        self.spinBoxDecimals.setObjectName(u"spinBoxDecimals")
        self.spinBoxDecimals.setMinimum(2)
        self.spinBoxDecimals.setMaximum(12)
        self.spinBoxDecimals.setValue(5)

        self.gridLayout.addWidget(self.spinBoxDecimals, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)

        self.unitsBox = QComboBox(self.groupBox)
        self.unitsBox.setObjectName(u"unitsBox")
        sizePolicy.setHeightForWidth(self.unitsBox.sizePolicy().hasHeightForWidth())
        self.unitsBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.unitsBox, 1, 3, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_Copy = QPushButton(Gui__Dialog__DlgUnitCalculator)
        self.pushButton_Copy.setObjectName(u"pushButton_Copy")

        self.horizontalLayout.addWidget(self.pushButton_Copy)

        self.pushButton_Close = QPushButton(Gui__Dialog__DlgUnitCalculator)
        self.pushButton_Close.setObjectName(u"pushButton_Close")

        self.horizontalLayout.addWidget(self.pushButton_Close)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgUnitCalculator)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgUnitCalculator)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgUnitCalculator):
        Gui__Dialog__DlgUnitCalculator.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Units Converter", None))
#if QT_CONFIG(tooltip)
        self.ValueInput.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Input the source value and unit", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"as", None))
#if QT_CONFIG(tooltip)
        self.UnitInput.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Input the unit for the result", None))
#endif // QT_CONFIG(tooltip)
        self.UnitInput.setText("")
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"=>", None))
#if QT_CONFIG(tooltip)
        self.ValueOutput.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Result", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.textEdit.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"List of last used calculations.\n"
"To add a calculation press Return in the value input field", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Quantity", None))
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Quantity", None))
        self.label_6.setText(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Unit system", None))
#if QT_CONFIG(tooltip)
        self.comboBoxScheme.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Unit system to be used for the Quantity.\n"
"The preference system is the one set in the general preferences.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Decimals", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDecimals.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Decimals for the quantity", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Unit category", None))
#if QT_CONFIG(tooltip)
        self.unitsBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Unit category for the quantity", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_Copy.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Copies the result to the clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Copy.setText(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Copy", None))
        self.pushButton_Close.setText(QCoreApplication.translate("Gui::Dialog::DlgUnitCalculator", u"Close", None))
    # retranslateUi

