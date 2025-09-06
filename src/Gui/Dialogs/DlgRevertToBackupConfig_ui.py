# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgRevertToBackupConfig.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QListWidget, QListWidgetItem, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgRevertToBackupConfig(object):
    def setupUi(self, Gui__Dialog__DlgRevertToBackupConfig):
        if not Gui__Dialog__DlgRevertToBackupConfig.objectName():
            Gui__Dialog__DlgRevertToBackupConfig.setObjectName(u"Gui__Dialog__DlgRevertToBackupConfig")
        Gui__Dialog__DlgRevertToBackupConfig.resize(610, 471)
        self.verticalLayout = QVBoxLayout(Gui__Dialog__DlgRevertToBackupConfig)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Gui__Dialog__DlgRevertToBackupConfig)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(Gui__Dialog__DlgRevertToBackupConfig)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.listWidget = QListWidget(Gui__Dialog__DlgRevertToBackupConfig)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__DlgRevertToBackupConfig)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Gui__Dialog__DlgRevertToBackupConfig)
        self.buttonBox.accepted.connect(Gui__Dialog__DlgRevertToBackupConfig.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__DlgRevertToBackupConfig.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgRevertToBackupConfig)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgRevertToBackupConfig):
        Gui__Dialog__DlgRevertToBackupConfig.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgRevertToBackupConfig", u"Revert to Backup Config", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgRevertToBackupConfig", u"WARNING: this process will undo any preference changes made since the specified date, and will also reset your recent files and Macros to their state on that date.", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgRevertToBackupConfig", u"Available backup files", None))
    # retranslateUi

