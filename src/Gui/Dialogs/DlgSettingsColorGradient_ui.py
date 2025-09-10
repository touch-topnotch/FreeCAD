# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsColorGradient.ui'
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
    QDialog, QDialogButtonBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Gui_Dialog_DlgSettingsColorGradient(object):
    def setupUi(self, Gui__Dialog__DlgSettingsColorGradient):
        if not Gui__Dialog__DlgSettingsColorGradient.objectName():
            Gui__Dialog__DlgSettingsColorGradient.setObjectName(u"Gui__Dialog__DlgSettingsColorGradient")
        Gui__Dialog__DlgSettingsColorGradient.resize(255, 313)
        Gui__Dialog__DlgSettingsColorGradient.setSizeGripEnabled(True)
        Gui__Dialog__DlgSettingsColorGradient.setModal(True)
        self.verticalLayout = QVBoxLayout(Gui__Dialog__DlgSettingsColorGradient)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxModel = QGroupBox(Gui__Dialog__DlgSettingsColorGradient)
        self.groupBoxModel.setObjectName(u"groupBoxModel")
        self.horizontalLayout = QHBoxLayout(self.groupBoxModel)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textLabel5 = QLabel(self.groupBoxModel)
        self.textLabel5.setObjectName(u"textLabel5")

        self.horizontalLayout.addWidget(self.textLabel5)

        self.comboBoxModel = QComboBox(self.groupBoxModel)
        self.comboBoxModel.addItem("")
        self.comboBoxModel.addItem("")
        self.comboBoxModel.addItem("")
        self.comboBoxModel.addItem("")
        self.comboBoxModel.setObjectName(u"comboBoxModel")

        self.horizontalLayout.addWidget(self.comboBoxModel)

        self.spacerItem = QSpacerItem(3, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.spacerItem)


        self.verticalLayout.addWidget(self.groupBoxModel)

        self.buttonGroupStyle = QGroupBox(Gui__Dialog__DlgSettingsColorGradient)
        self.buttonGroupStyle.setObjectName(u"buttonGroupStyle")
        self.gridLayout = QGridLayout(self.buttonGroupStyle)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.radioButtonFlow = QRadioButton(self.buttonGroupStyle)
        self.radioButtonFlow.setObjectName(u"radioButtonFlow")
        self.radioButtonFlow.setChecked(True)

        self.gridLayout.addWidget(self.radioButtonFlow, 0, 0, 1, 1)

        self.radioButtonZero = QRadioButton(self.buttonGroupStyle)
        self.radioButtonZero.setObjectName(u"radioButtonZero")

        self.gridLayout.addWidget(self.radioButtonZero, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.buttonGroupStyle)

        self.groupBoxVisible = QGroupBox(Gui__Dialog__DlgSettingsColorGradient)
        self.groupBoxVisible.setObjectName(u"groupBoxVisible")
        self.hboxLayout = QHBoxLayout(self.groupBoxVisible)
        self.hboxLayout.setSpacing(0)
        self.hboxLayout.setContentsMargins(11, 11, 11, 11)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(11, 11, 11, 11)
        self.checkBoxGrayed = QCheckBox(self.groupBoxVisible)
        self.checkBoxGrayed.setObjectName(u"checkBoxGrayed")

        self.hboxLayout.addWidget(self.checkBoxGrayed)

        self.checkBoxInvisible = QCheckBox(self.groupBoxVisible)
        self.checkBoxInvisible.setObjectName(u"checkBoxInvisible")

        self.hboxLayout.addWidget(self.checkBoxInvisible)


        self.verticalLayout.addWidget(self.groupBoxVisible)

        self.groupBoxRange = QGroupBox(Gui__Dialog__DlgSettingsColorGradient)
        self.groupBoxRange.setObjectName(u"groupBoxRange")
        self.gridLayout_2 = QGridLayout(self.groupBoxRange)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textLabelMax = QLabel(self.groupBoxRange)
        self.textLabelMax.setObjectName(u"textLabelMax")

        self.gridLayout_2.addWidget(self.textLabelMax, 0, 0, 2, 1)

        self.floatLineEditMax = QLineEdit(self.groupBoxRange)
        self.floatLineEditMax.setObjectName(u"floatLineEditMax")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.floatLineEditMax.sizePolicy().hasHeightForWidth())
        self.floatLineEditMax.setSizePolicy(sizePolicy)
        self.floatLineEditMax.setMinimumSize(QSize(60, 0))
        self.floatLineEditMax.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.floatLineEditMax, 0, 1, 2, 1)

        self.spacerItem1 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.spacerItem1, 0, 3, 1, 1)

        self.textLabel1 = QLabel(self.groupBoxRange)
        self.textLabel1.setObjectName(u"textLabel1")

        self.gridLayout_2.addWidget(self.textLabel1, 0, 4, 2, 1)

        self.spinBoxLabel = QSpinBox(self.groupBoxRange)
        self.spinBoxLabel.setObjectName(u"spinBoxLabel")
        self.spinBoxLabel.setMinimumSize(QSize(40, 0))
        self.spinBoxLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.spinBoxLabel, 0, 5, 2, 1)

        self.textLabelMin = QLabel(self.groupBoxRange)
        self.textLabelMin.setObjectName(u"textLabelMin")

        self.gridLayout_2.addWidget(self.textLabelMin, 2, 0, 1, 1)

        self.floatLineEditMin = QLineEdit(self.groupBoxRange)
        self.floatLineEditMin.setObjectName(u"floatLineEditMin")
        sizePolicy.setHeightForWidth(self.floatLineEditMin.sizePolicy().hasHeightForWidth())
        self.floatLineEditMin.setSizePolicy(sizePolicy)
        self.floatLineEditMin.setMinimumSize(QSize(60, 0))
        self.floatLineEditMin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.floatLineEditMin, 2, 1, 1, 1)

        self.textLabel1_2 = QLabel(self.groupBoxRange)
        self.textLabel1_2.setObjectName(u"textLabel1_2")

        self.gridLayout_2.addWidget(self.textLabel1_2, 2, 4, 1, 1)

        self.spinBoxDecimals = QSpinBox(self.groupBoxRange)
        self.spinBoxDecimals.setObjectName(u"spinBoxDecimals")
        self.spinBoxDecimals.setMinimumSize(QSize(40, 0))
        self.spinBoxDecimals.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBoxDecimals.setMaximum(6)
        self.spinBoxDecimals.setValue(2)

        self.gridLayout_2.addWidget(self.spinBoxDecimals, 2, 5, 1, 1)


        self.verticalLayout.addWidget(self.groupBoxRange)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__DlgSettingsColorGradient)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.textLabel5.setBuddy(self.comboBoxModel)
        self.textLabelMax.setBuddy(self.floatLineEditMax)
        self.textLabel1.setBuddy(self.spinBoxLabel)
        self.textLabelMin.setBuddy(self.floatLineEditMin)
        self.textLabel1_2.setBuddy(self.spinBoxDecimals)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.comboBoxModel, self.radioButtonFlow)
        QWidget.setTabOrder(self.radioButtonFlow, self.checkBoxGrayed)
        QWidget.setTabOrder(self.checkBoxGrayed, self.checkBoxInvisible)
        QWidget.setTabOrder(self.checkBoxInvisible, self.floatLineEditMax)
        QWidget.setTabOrder(self.floatLineEditMax, self.floatLineEditMin)
        QWidget.setTabOrder(self.floatLineEditMin, self.spinBoxLabel)

        self.retranslateUi(Gui__Dialog__DlgSettingsColorGradient)
        self.buttonBox.accepted.connect(Gui__Dialog__DlgSettingsColorGradient.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__DlgSettingsColorGradient.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsColorGradient)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsColorGradient):
        Gui__Dialog__DlgSettingsColorGradient.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Color-gradient settings", None))
        self.groupBoxModel.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Color model", None))
        self.textLabel5.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"&Gradient:", None))
        self.comboBoxModel.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"red-yellow-green-cyan-blue", None))
        self.comboBoxModel.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"blue-cyan-green-yellow-red", None))
        self.comboBoxModel.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"white-black", None))
        self.comboBoxModel.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"black-white", None))

        self.buttonGroupStyle.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Style", None))
#if QT_CONFIG(tooltip)
        self.radioButtonFlow.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Color gradient is used with its full color range", None))
#endif // QT_CONFIG(tooltip)
        self.radioButtonFlow.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"&Flow", None))
#if QT_CONFIG(shortcut)
        self.radioButtonFlow.setShortcut(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Alt+F", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.radioButtonZero.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Color gradient starts from the zero value", None))
#endif // QT_CONFIG(tooltip)
        self.radioButtonZero.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"&Zero", None))
#if QT_CONFIG(shortcut)
        self.radioButtonZero.setShortcut(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Alt+Z", None))
#endif // QT_CONFIG(shortcut)
        self.groupBoxVisible.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Visibility", None))
#if QT_CONFIG(tooltip)
        self.checkBoxGrayed.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Data outside the specified min-max range\n"
"will be displayed in gray", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxGrayed.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Out g&rayed", None))
#if QT_CONFIG(shortcut)
        self.checkBoxGrayed.setShortcut(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Alt+R", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.checkBoxInvisible.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Data outside the specified min-max range\n"
"will be displayed with transparency", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxInvisible.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Out &transparent", None))
#if QT_CONFIG(shortcut)
        self.checkBoxInvisible.setShortcut(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Alt+I", None))
#endif // QT_CONFIG(shortcut)
        self.groupBoxRange.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Parameter range", None))
        self.textLabelMax.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Ma&ximum:", None))
        self.textLabel1.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"&Labels:", None))
#if QT_CONFIG(tooltip)
        self.spinBoxLabel.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Number of labels besides the color bar", None))
#endif // QT_CONFIG(tooltip)
        self.textLabelMin.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Mi&nimum:", None))
        self.textLabel1_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"&Decimals:", None))
#if QT_CONFIG(tooltip)
        self.spinBoxDecimals.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsColorGradient", u"Number of decimals for labels\n"
"besides the color bar", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

