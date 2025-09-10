# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-dwg.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsDraft(object):
    def setupUi(self, Gui__Dialog__DlgSettingsDraft):
        if not Gui__Dialog__DlgSettingsDraft.objectName():
            Gui__Dialog__DlgSettingsDraft.setObjectName(u"Gui__Dialog__DlgSettingsDraft")
        Gui__Dialog__DlgSettingsDraft.resize(446, 462)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsDraft)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(9, 9, 9, 9)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox = Gui_PrefComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setProperty(u"prefEntry", u"DWGConversion")
        self.comboBox.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.gui__preffilechooser_2 = Gui_PrefFileChooser(self.groupBox)
        self.gui__preffilechooser_2.setObjectName(u"gui__preffilechooser_2")
        self.gui__preffilechooser_2.setProperty(u"prefEntry", u"TeighaFileConverter")
        self.gui__preffilechooser_2.setProperty(u"prefPath", u"Mod/Draft")

        self.horizontalLayout_4.addWidget(self.gui__preffilechooser_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)


        self.vboxLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Gui__Dialog__DlgSettingsDraft)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsDraft)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsDraft):
        Gui__Dialog__DlgSettingsDraft.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"DWG", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"DWG conversion", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Conversion method:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Automatic", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"LibreDWG", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"ODA Converter", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"QCAD pro", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"This is the method FreeCAD will use to convert DWG files to DXF. If \"Automatic\" is chosen, FreeCAD will try to find one of the following converters in the same order as they are shown here. If FreeCAD is unable to find any, you might need to choose a specific converter and indicate its path here under. Choose the \"dwg2dxf\" utility if using LibreDWG, \"ODAFileConverter\" if using the ODA file converter, or the \"dwg2dwg\" utility if using the pro version of QCAD.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Path to file converter", None))
#if QT_CONFIG(tooltip)
        self.gui__preffilechooser_2.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The path to your DWG file converter executable", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"<html><head/><body><p><span style=\" font-weight:600;\">Note:</span> DXF options apply to DWG files as well.</p></body></html>", None))
    # retranslateUi

