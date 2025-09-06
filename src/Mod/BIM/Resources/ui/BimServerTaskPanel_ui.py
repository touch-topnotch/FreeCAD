# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BimServerTaskPanel.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_BimServer(object):
    def setupUi(self, BimServer):
        if not BimServer.objectName():
            BimServer.setObjectName(u"BimServer")
        BimServer.resize(232, 486)
        self.verticalLayout = QVBoxLayout(BimServer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupServer = QGroupBox(BimServer)
        self.groupServer.setObjectName(u"groupServer")
        self.verticalLayout_2 = QVBoxLayout(self.groupServer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelServerName = QLabel(self.groupServer)
        self.labelServerName.setObjectName(u"labelServerName")

        self.horizontalLayout.addWidget(self.labelServerName)

        self.buttonServer = QPushButton(self.groupServer)
        self.buttonServer.setObjectName(u"buttonServer")

        self.horizontalLayout.addWidget(self.buttonServer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.labelStatus = QLabel(self.groupServer)
        self.labelStatus.setObjectName(u"labelStatus")
        font = QFont()
        font.setBold(True)
        self.labelStatus.setFont(font)

        self.horizontalLayout_8.addWidget(self.labelStatus)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.buttonBrowser = QPushButton(self.groupServer)
        self.buttonBrowser.setObjectName(u"buttonBrowser")

        self.horizontalLayout_7.addWidget(self.buttonBrowser)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupServer)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboProjects = QComboBox(self.groupServer)
        self.comboProjects.setObjectName(u"comboProjects")

        self.horizontalLayout_2.addWidget(self.comboProjects)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupServer)

        self.groupDownload = QGroupBox(BimServer)
        self.groupDownload.setObjectName(u"groupDownload")
        self.verticalLayout_3 = QVBoxLayout(self.groupDownload)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.groupDownload)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.listRevisions = QListWidget(self.groupDownload)
        self.listRevisions.setObjectName(u"listRevisions")
        self.listRevisions.setModelColumn(0)

        self.verticalLayout_3.addWidget(self.listRevisions)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.buttonOpen = QPushButton(self.groupDownload)
        self.buttonOpen.setObjectName(u"buttonOpen")

        self.horizontalLayout_3.addWidget(self.buttonOpen)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.groupDownload)

        self.groupBox_3 = QGroupBox(BimServer)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.comboRoot = QComboBox(self.groupBox_3)
        self.comboRoot.setObjectName(u"comboRoot")

        self.horizontalLayout_4.addWidget(self.comboRoot)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.editComment = QLineEdit(self.groupBox_3)
        self.editComment.setObjectName(u"editComment")

        self.horizontalLayout_5.addWidget(self.editComment)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.buttonUpload = QPushButton(self.groupBox_3)
        self.buttonUpload.setObjectName(u"buttonUpload")

        self.horizontalLayout_6.addWidget(self.buttonUpload)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.retranslateUi(BimServer)

        QMetaObject.connectSlotsByName(BimServer)
    # setupUi

    def retranslateUi(self, BimServer):
        BimServer.setWindowTitle(QCoreApplication.translate("BimServer", u"BIM Server", None))
        self.groupServer.setTitle(QCoreApplication.translate("BimServer", u"Server", None))
#if QT_CONFIG(tooltip)
        self.labelServerName.setToolTip(QCoreApplication.translate("BimServer", u"Name of the currently connected BIM Server. Settings can be adjusted in BIM preferences.", None))
#endif // QT_CONFIG(tooltip)
        self.labelServerName.setText(QCoreApplication.translate("BimServer", u"BIM Server", None))
        self.buttonServer.setText(QCoreApplication.translate("BimServer", u"Connect", None))
        self.labelStatus.setText(QCoreApplication.translate("BimServer", u"Idle", None))
        self.buttonBrowser.setText(QCoreApplication.translate("BimServer", u"Open in Browser", None))
        self.label_2.setText(QCoreApplication.translate("BimServer", u"Project", None))
#if QT_CONFIG(tooltip)
        self.comboProjects.setToolTip(QCoreApplication.translate("BimServer", u"The list of projects present on the BIM Server", None))
#endif // QT_CONFIG(tooltip)
        self.groupDownload.setTitle(QCoreApplication.translate("BimServer", u"Download", None))
        self.label_3.setText(QCoreApplication.translate("BimServer", u"Available revisions", None))
        self.buttonOpen.setText(QCoreApplication.translate("BimServer", u"Open", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("BimServer", u"Upload", None))
        self.label_5.setText(QCoreApplication.translate("BimServer", u"Root object", None))
        self.label_6.setText(QCoreApplication.translate("BimServer", u"Comment", None))
        self.buttonUpload.setText(QCoreApplication.translate("BimServer", u"Upload", None))
    # retranslateUi

