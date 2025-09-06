# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPartImportStep.ui'
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
    QGridLayout, QGroupBox, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_PartGui_DlgPartImportStep(object):
    def setupUi(self, PartGui__DlgPartImportStep):
        if not PartGui__DlgPartImportStep.objectName():
            PartGui__DlgPartImportStep.setObjectName(u"PartGui__DlgPartImportStep")
        PartGui__DlgPartImportStep.resize(349, 116)
        self.gridLayout = QGridLayout(PartGui__DlgPartImportStep)
        self.gridLayout.setObjectName(u"gridLayout")
        self.GroupBox5 = QGroupBox(PartGui__DlgPartImportStep)
        self.GroupBox5.setObjectName(u"GroupBox5")
        self.gridLayout_2 = QGridLayout(self.GroupBox5)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.FileName = QLineEdit(self.GroupBox5)
        self.FileName.setObjectName(u"FileName")

        self.gridLayout_2.addWidget(self.FileName, 0, 0, 1, 1)

        self.SearchFile = QPushButton(self.GroupBox5)
        self.SearchFile.setObjectName(u"SearchFile")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchFile.sizePolicy().hasHeightForWidth())
        self.SearchFile.setSizePolicy(sizePolicy)
        self.SearchFile.setMinimumSize(QSize(30, 0))
        self.SearchFile.setMaximumSize(QSize(30, 32767))

        self.gridLayout_2.addWidget(self.SearchFile, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.GroupBox5, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(PartGui__DlgPartImportStep)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.FileName, self.SearchFile)

        self.retranslateUi(PartGui__DlgPartImportStep)

        QMetaObject.connectSlotsByName(PartGui__DlgPartImportStep)
    # setupUi

    def retranslateUi(self, PartGui__DlgPartImportStep):
        PartGui__DlgPartImportStep.setWindowTitle(QCoreApplication.translate("PartGui::DlgPartImportStep", u"STEP Input File", None))
        self.GroupBox5.setTitle(QCoreApplication.translate("PartGui::DlgPartImportStep", u"File Name", None))
        self.FileName.setText("")
        self.SearchFile.setText(QCoreApplication.translate("PartGui::DlgPartImportStep", u"Search File", None))
    # retranslateUi

