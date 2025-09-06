# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-oca.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsDraft(object):
    def setupUi(self, Gui__Dialog__DlgSettingsDraft):
        if not Gui__Dialog__DlgSettingsDraft.objectName():
            Gui__Dialog__DlgSettingsDraft.setObjectName(u"Gui__Dialog__DlgSettingsDraft")
        Gui__Dialog__DlgSettingsDraft.resize(398, 340)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsDraft)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(9, 9, 9, 9)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.GroupBox12_3 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.GroupBox12_3.setObjectName(u"GroupBox12_3")
        self._6 = QVBoxLayout(self.GroupBox12_3)
        self._6.setSpacing(6)
        self._6.setContentsMargins(9, 9, 9, 9)
        self._6.setObjectName(u"_6")
        self._7 = QHBoxLayout()
        self._7.setSpacing(6)
        self._7.setContentsMargins(0, 0, 0, 0)
        self._7.setObjectName(u"_7")
        self.gui__prefcheckbox_4 = Gui_PrefCheckBox(self.GroupBox12_3)
        self.gui__prefcheckbox_4.setObjectName(u"gui__prefcheckbox_4")
        self.gui__prefcheckbox_4.setProperty(u"prefEntry", u"ocaareas")
        self.gui__prefcheckbox_4.setProperty(u"prefPath", u"Mod/Draft")

        self._7.addWidget(self.gui__prefcheckbox_4)


        self._6.addLayout(self._7)


        self.vboxLayout.addWidget(self.GroupBox12_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Gui__Dialog__DlgSettingsDraft)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsDraft)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsDraft):
        Gui__Dialog__DlgSettingsDraft.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"OCA", None))
        self.GroupBox12_3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Import Options", None))
#if QT_CONFIG(tooltip)
        self.gui__prefcheckbox_4.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Imports the areas (3D faces) too", None))
#endif // QT_CONFIG(tooltip)
        self.gui__prefcheckbox_4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Import OCA areas", None))
    # retranslateUi

