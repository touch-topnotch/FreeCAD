# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsPDF.ui'
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

class Ui_Gui_Dialog_DlgSettingsPDF(object):
    def setupUi(self, Gui__Dialog__DlgSettingsPDF):
        if not Gui__Dialog__DlgSettingsPDF.objectName():
            Gui__Dialog__DlgSettingsPDF.setObjectName(u"Gui__Dialog__DlgSettingsPDF")
        Gui__Dialog__DlgSettingsPDF.resize(446, 462)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsPDF)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(9, 9, 9, 9)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsPDF)
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
        self.comboBox.setProperty(u"prefEntry", u"PDFVersion")
        self.comboBox.setProperty(u"prefPath", u"Mod")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.warningLabel = QLabel(self.groupBox)
        self.warningLabel.setObjectName(u"warningLabel")
        self.warningLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.warningLabel)


        self.vboxLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Gui__Dialog__DlgSettingsPDF)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsPDF)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsPDF):
        Gui__Dialog__DlgSettingsPDF.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsPDF", u"PDF", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsPDF", u"PDF Export", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPDF", u"PDF Version:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsPDF", u"PDF/1.4", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsPDF", u"PDF/A-1b", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsPDF", u"PDF/1.6", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsPDF", u"PDF/X-4", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPDF", u"This is the PDF Version FreeCAD will use to export to PDF.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

