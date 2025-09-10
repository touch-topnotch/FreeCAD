# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RemoteDebugger.ui'
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
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QWidget)

class Ui_Gui_Dialog_RemoteDebugger(object):
    def setupUi(self, Gui__Dialog__RemoteDebugger):
        if not Gui__Dialog__RemoteDebugger.objectName():
            Gui__Dialog__RemoteDebugger.setObjectName(u"Gui__Dialog__RemoteDebugger")
        Gui__Dialog__RemoteDebugger.resize(426, 287)
        self.gridLayout_3 = QGridLayout(Gui__Dialog__RemoteDebugger)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(Gui__Dialog__RemoteDebugger)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWinpdb = QWidget()
        self.tabWinpdb.setObjectName(u"tabWinpdb")
        self.gridLayout = QGridLayout(self.tabWinpdb)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelPassword = QLabel(self.tabWinpdb)
        self.labelPassword.setObjectName(u"labelPassword")

        self.gridLayout.addWidget(self.labelPassword, 0, 0, 1, 1)

        self.lineEditPassword = QLineEdit(self.tabWinpdb)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEditPassword, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 155, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tabWinpdb, "")
        self.tabVSCode = QWidget()
        self.tabVSCode.setObjectName(u"tabVSCode")
        self.gridLayout_2 = QGridLayout(self.tabVSCode)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelAddress = QLabel(self.tabVSCode)
        self.labelAddress.setObjectName(u"labelAddress")

        self.gridLayout_2.addWidget(self.labelAddress, 0, 0, 1, 1)

        self.lineEditAddress = QLineEdit(self.tabVSCode)
        self.lineEditAddress.setObjectName(u"lineEditAddress")
        self.lineEditAddress.setText(u"localhost")

        self.gridLayout_2.addWidget(self.lineEditAddress, 0, 1, 1, 1)

        self.labelPort = QLabel(self.tabVSCode)
        self.labelPort.setObjectName(u"labelPort")

        self.gridLayout_2.addWidget(self.labelPort, 1, 0, 1, 1)

        self.spinBoxPort = QSpinBox(self.tabVSCode)
        self.spinBoxPort.setObjectName(u"spinBoxPort")
        self.spinBoxPort.setMaximum(65535)
        self.spinBoxPort.setValue(5678)

        self.gridLayout_2.addWidget(self.spinBoxPort, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 94, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.tabWidget.addTab(self.tabVSCode, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__RemoteDebugger)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_3.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__RemoteDebugger)
        self.buttonBox.accepted.connect(Gui__Dialog__RemoteDebugger.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__RemoteDebugger.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Gui__Dialog__RemoteDebugger)
    # setupUi

    def retranslateUi(self, Gui__Dialog__RemoteDebugger):
        Gui__Dialog__RemoteDebugger.setWindowTitle(QCoreApplication.translate("Gui::Dialog::RemoteDebugger", u"Attach to remote debugger", None))
        self.labelPassword.setText(QCoreApplication.translate("Gui::Dialog::RemoteDebugger", u"Password:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWinpdb), QCoreApplication.translate("Gui::Dialog::RemoteDebugger", u"winpdb", None))
        self.labelAddress.setText(QCoreApplication.translate("Gui::Dialog::RemoteDebugger", u"Address:", None))
        self.labelPort.setText(QCoreApplication.translate("Gui::Dialog::RemoteDebugger", u"Port:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVSCode), QCoreApplication.translate("Gui::Dialog::RemoteDebugger", u"VS Code", None))
    # retranslateUi

