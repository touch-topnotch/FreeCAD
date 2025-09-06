# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GitTaskPanel.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(255, 516)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupStatus = QGroupBox(Form)
        self.groupStatus.setObjectName(u"groupStatus")
        self.verticalLayout_2 = QVBoxLayout(self.groupStatus)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelStatus = QLabel(self.groupStatus)
        self.labelStatus.setObjectName(u"labelStatus")

        self.verticalLayout_2.addWidget(self.labelStatus)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.buttonLog = QPushButton(self.groupStatus)
        self.buttonLog.setObjectName(u"buttonLog")

        self.horizontalLayout_2.addWidget(self.buttonLog)

        self.buttonRefresh = QPushButton(self.groupStatus)
        self.buttonRefresh.setObjectName(u"buttonRefresh")

        self.horizontalLayout_2.addWidget(self.buttonRefresh)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label = QLabel(self.groupStatus)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.listFiles = QListWidget(self.groupStatus)
        self.listFiles.setObjectName(u"listFiles")
        self.listFiles.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_2.addWidget(self.listFiles)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonDiff = QPushButton(self.groupStatus)
        self.buttonDiff.setObjectName(u"buttonDiff")

        self.horizontalLayout.addWidget(self.buttonDiff)

        self.buttonSelectAll = QPushButton(self.groupStatus)
        self.buttonSelectAll.setObjectName(u"buttonSelectAll")

        self.horizontalLayout.addWidget(self.buttonSelectAll)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupStatus)

        self.groupCommit = QGroupBox(Form)
        self.groupCommit.setObjectName(u"groupCommit")
        self.verticalLayout_3 = QVBoxLayout(self.groupCommit)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupCommit)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.editMessage = QLineEdit(self.groupCommit)
        self.editMessage.setObjectName(u"editMessage")

        self.horizontalLayout_3.addWidget(self.editMessage)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.buttonCommit = QPushButton(self.groupCommit)
        self.buttonCommit.setObjectName(u"buttonCommit")

        self.horizontalLayout_4.addWidget(self.buttonCommit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.groupCommit)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listRepos = QListWidget(self.groupBox_2)
        self.listRepos.setObjectName(u"listRepos")

        self.verticalLayout_4.addWidget(self.listRepos)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.buttonPull = QPushButton(self.groupBox_2)
        self.buttonPull.setObjectName(u"buttonPull")

        self.horizontalLayout_5.addWidget(self.buttonPull)

        self.buttonPush = QPushButton(self.groupBox_2)
        self.buttonPush.setObjectName(u"buttonPush")

        self.horizontalLayout_5.addWidget(self.buttonPush)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Git", None))
        self.groupStatus.setTitle(QCoreApplication.translate("Form", u"Status", None))
        self.labelStatus.setText("")
        self.buttonLog.setText(QCoreApplication.translate("Form", u"Log", None))
        self.buttonRefresh.setText(QCoreApplication.translate("Form", u"Refresh", None))
        self.label.setText(QCoreApplication.translate("Form", u"List of files to be committed", None))
        self.buttonDiff.setText(QCoreApplication.translate("Form", u"Diff", None))
        self.buttonSelectAll.setText(QCoreApplication.translate("Form", u"Select All", None))
        self.groupCommit.setTitle(QCoreApplication.translate("Form", u"Commit", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Commit message", None))
        self.buttonCommit.setText(QCoreApplication.translate("Form", u"Commit", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Remote repositories", None))
        self.buttonPull.setText(QCoreApplication.translate("Form", u"Pull", None))
        self.buttonPush.setText(QCoreApplication.translate("Form", u"Push", None))
    # retranslateUi

