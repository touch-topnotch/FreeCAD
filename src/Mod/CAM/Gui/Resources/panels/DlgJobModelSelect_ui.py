# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgJobModelSelect.ui'
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
    QListWidget, QListWidgetItem, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(383, 786)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.models = QTabWidget(Dialog)
        self.models.setObjectName(u"models")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.solidList = QListWidget(self.tab)
        self.solidList.setObjectName(u"solidList")

        self.verticalLayout_2.addWidget(self.solidList)

        self.models.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.twoDList = QListWidget(self.tab_3)
        self.twoDList.setObjectName(u"twoDList")

        self.verticalLayout_4.addWidget(self.twoDList)

        self.models.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.modelsList = QListWidget(self.tab_2)
        self.modelsList.setObjectName(u"modelsList")

        self.verticalLayout_3.addWidget(self.modelsList)

        self.models.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.models)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.models.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Select Base Models", None))
        self.models.setTabText(self.models.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Solids", None))
        self.models.setTabText(self.models.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"2D", None))
        self.models.setTabText(self.models.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Base Models", None))
    # retranslateUi

