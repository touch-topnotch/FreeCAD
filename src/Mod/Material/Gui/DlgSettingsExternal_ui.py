# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsExternal.ui'
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
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MatGui_DlgSettingsExternal(object):
    def setupUi(self, MatGui__DlgSettingsExternal):
        if not MatGui__DlgSettingsExternal.objectName():
            MatGui__DlgSettingsExternal.setObjectName(u"MatGui__DlgSettingsExternal")
        MatGui__DlgSettingsExternal.resize(400, 291)
        self.verticalLayout = QVBoxLayout(MatGui__DlgSettingsExternal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupExternal = QGroupBox(MatGui__DlgSettingsExternal)
        self.groupExternal.setObjectName(u"groupExternal")
        self.groupExternal.setCheckable(True)
        self.gridLayout_2 = QGridLayout(self.groupExternal)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupExternal)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.comboInterface = Gui_PrefComboBox(self.groupExternal)
        self.comboInterface.setObjectName(u"comboInterface")
        self.comboInterface.setCurrentText(u"")
        self.comboInterface.setProperty(u"prefEntry", u"Current")
        self.comboInterface.setProperty(u"prefPath", u"Mod/Material/ExternalInterface")

        self.gridLayout_2.addWidget(self.comboInterface, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.groupExternal)

        self.groupBox_2 = QGroupBox(MatGui__DlgSettingsExternal)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.inputModelCacheHitRate = QLineEdit(self.groupBox_2)
        self.inputModelCacheHitRate.setObjectName(u"inputModelCacheHitRate")
        self.inputModelCacheHitRate.setReadOnly(True)

        self.gridLayout_3.addWidget(self.inputModelCacheHitRate, 1, 1, 1, 1)

        self.spinMaterialCacheSize = Gui_PrefSpinBox(self.groupBox_2)
        self.spinMaterialCacheSize.setObjectName(u"spinMaterialCacheSize")
        self.spinMaterialCacheSize.setMaximum(4096)
        self.spinMaterialCacheSize.setProperty(u"prefEntry", u"MaterialCacheSize")
        self.spinMaterialCacheSize.setProperty(u"prefPath", u"Mod/Material/ExternalInterface")

        self.gridLayout_3.addWidget(self.spinMaterialCacheSize, 2, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.spinModelCacheSize = Gui_PrefSpinBox(self.groupBox_2)
        self.spinModelCacheSize.setObjectName(u"spinModelCacheSize")
        self.spinModelCacheSize.setMaximum(4096)
        self.spinModelCacheSize.setProperty(u"prefEntry", u"ModelCacheSize")
        self.spinModelCacheSize.setProperty(u"prefPath", u"Mod/Material/ExternalInterface")

        self.gridLayout_3.addWidget(self.spinModelCacheSize, 0, 1, 1, 1)

        self.inputMaterialCacheHitRate = QLineEdit(self.groupBox_2)
        self.inputMaterialCacheHitRate.setObjectName(u"inputMaterialCacheHitRate")

        self.gridLayout_3.addWidget(self.inputMaterialCacheHitRate, 3, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(MatGui__DlgSettingsExternal)

        QMetaObject.connectSlotsByName(MatGui__DlgSettingsExternal)
    # setupUi

    def retranslateUi(self, MatGui__DlgSettingsExternal):
        MatGui__DlgSettingsExternal.setWindowTitle(QCoreApplication.translate("MatGui::DlgSettingsExternal", u"External Interface", None))
        self.groupExternal.setTitle(QCoreApplication.translate("MatGui::DlgSettingsExternal", u"Use External Interface", None))
        self.label.setText(QCoreApplication.translate("MatGui::DlgSettingsExternal", u"External interface", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MatGui::DlgSettingsExternal", u"Cache", None))
        self.label_7.setText(QCoreApplication.translate("MatGui::DlgSettingsExternal", u"Model cache size", None))
        self.label_10.setText(QCoreApplication.translate("MatGui::DlgSettingsExternal", u"Hit rate", None))
        self.label_9.setText(QCoreApplication.translate("MatGui::DlgSettingsExternal", u"Hit rate", None))
        self.label_8.setText(QCoreApplication.translate("MatGui::DlgSettingsExternal", u"Material cache size", None))
    # retranslateUi

