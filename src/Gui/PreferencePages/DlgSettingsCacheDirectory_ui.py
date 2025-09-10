# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsCacheDirectory.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import resource_rc

class Ui_Gui_Dialog_DlgSettingsCacheDirectory(object):
    def setupUi(self, Gui__Dialog__DlgSettingsCacheDirectory):
        if not Gui__Dialog__DlgSettingsCacheDirectory.objectName():
            Gui__Dialog__DlgSettingsCacheDirectory.setObjectName(u"Gui__Dialog__DlgSettingsCacheDirectory")
        Gui__Dialog__DlgSettingsCacheDirectory.resize(425, 360)
        self.gridLayout_2 = QGridLayout(Gui__Dialog__DlgSettingsCacheDirectory)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.GroupBox5 = QGroupBox(Gui__Dialog__DlgSettingsCacheDirectory)
        self.GroupBox5.setObjectName(u"GroupBox5")
        self.gridLayout_3 = QGridLayout(self.GroupBox5)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.GroupBox5)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.cacheLocation = QLineEdit(self.GroupBox5)
        self.cacheLocation.setObjectName(u"cacheLocation")
        self.cacheLocation.setReadOnly(True)

        self.gridLayout.addWidget(self.cacheLocation, 0, 1, 1, 2)

        self.openButton = QPushButton(self.GroupBox5)
        self.openButton.setObjectName(u"openButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openButton.sizePolicy().hasHeightForWidth())
        self.openButton.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/document-open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.openButton.setIcon(icon)

        self.gridLayout.addWidget(self.openButton, 0, 3, 1, 1)

        self.labelPeriod = QLabel(self.GroupBox5)
        self.labelPeriod.setObjectName(u"labelPeriod")

        self.gridLayout.addWidget(self.labelPeriod, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(118, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.comboBoxPeriod = QComboBox(self.GroupBox5)
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.setObjectName(u"comboBoxPeriod")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBoxPeriod.sizePolicy().hasHeightForWidth())
        self.comboBoxPeriod.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBoxPeriod, 1, 2, 1, 2)

        self.labelCache = QLabel(self.GroupBox5)
        self.labelCache.setObjectName(u"labelCache")

        self.gridLayout.addWidget(self.labelCache, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(118, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 1, 1, 1)

        self.comboBoxLimit = QComboBox(self.GroupBox5)
        self.comboBoxLimit.setObjectName(u"comboBoxLimit")
        sizePolicy1.setHeightForWidth(self.comboBoxLimit.sizePolicy().hasHeightForWidth())
        self.comboBoxLimit.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBoxLimit, 2, 2, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 3)

        self.labelCurrentCache = QLabel(self.GroupBox5)
        self.labelCurrentCache.setObjectName(u"labelCurrentCache")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelCurrentCache.sizePolicy().hasHeightForWidth())
        self.labelCurrentCache.setSizePolicy(sizePolicy2)
        self.labelCurrentCache.setText(u"Current cache size:")

        self.gridLayout_3.addWidget(self.labelCurrentCache, 1, 0, 1, 1)

        self.pushButtonCheck = QPushButton(self.GroupBox5)
        self.pushButtonCheck.setObjectName(u"pushButtonCheck")

        self.gridLayout_3.addWidget(self.pushButtonCheck, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.GroupBox5, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 169, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgSettingsCacheDirectory)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsCacheDirectory)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsCacheDirectory):
        Gui__Dialog__DlgSettingsCacheDirectory.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsCacheDirectory", u"Cache", None))
        self.GroupBox5.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsCacheDirectory", u"Cache directory", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsCacheDirectory", u"Location (read-only):", None))
#if QT_CONFIG(tooltip)
        self.openButton.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsCacheDirectory", u"Browse cache directory", None))
#endif // QT_CONFIG(tooltip)
        self.labelPeriod.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsCacheDirectory", u"Check periodically at program start:", None))
        self.comboBoxPeriod.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsCacheDirectory", u"Always", None))
        self.comboBoxPeriod.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsCacheDirectory", u"Daily", None))
        self.comboBoxPeriod.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsCacheDirectory", u"Weekly", None))
        self.comboBoxPeriod.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsCacheDirectory", u"Monthly", None))
        self.comboBoxPeriod.setItemText(4, QCoreApplication.translate("Gui::Dialog::DlgSettingsCacheDirectory", u"Yearly", None))
        self.comboBoxPeriod.setItemText(5, QCoreApplication.translate("Gui::Dialog::DlgSettingsCacheDirectory", u"Never", None))

        self.labelCache.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsCacheDirectory", u"Cache size limit:", None))
        self.pushButtonCheck.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsCacheDirectory", u"Check now...", None))
    # retranslateUi

