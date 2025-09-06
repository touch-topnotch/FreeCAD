# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskPathCamoticsSim.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)
import Path_rc

class Ui_TaskPathSimulator(object):
    def setupUi(self, TaskPathSimulator):
        if not TaskPathSimulator.objectName():
            TaskPathSimulator.setObjectName(u"TaskPathSimulator")
        TaskPathSimulator.resize(377, 361)
        self.verticalLayout = QVBoxLayout(TaskPathSimulator)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(TaskPathSimulator)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(23)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txtStatus = QLabel(TaskPathSimulator)
        self.txtStatus.setObjectName(u"txtStatus")

        self.horizontalLayout_2.addWidget(self.txtStatus)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.timeSlider = QSlider(TaskPathSimulator)
        self.timeSlider.setObjectName(u"timeSlider")
        self.timeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.timeSlider)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.pathData = QTextBrowser(TaskPathSimulator)
        self.pathData.setObjectName(u"pathData")

        self.verticalLayout.addWidget(self.pathData)

        self.btnLaunchCamotics = QPushButton(TaskPathSimulator)
        self.btnLaunchCamotics.setObjectName(u"btnLaunchCamotics")

        self.verticalLayout.addWidget(self.btnLaunchCamotics)

        self.btnMakeFile = QPushButton(TaskPathSimulator)
        self.btnMakeFile.setObjectName(u"btnMakeFile")

        self.verticalLayout.addWidget(self.btnMakeFile)


        self.retranslateUi(TaskPathSimulator)

        QMetaObject.connectSlotsByName(TaskPathSimulator)
    # setupUi

    def retranslateUi(self, TaskPathSimulator):
        TaskPathSimulator.setWindowTitle(QCoreApplication.translate("TaskPathSimulator", u"Path Simulator", None))
        self.txtStatus.setText(QCoreApplication.translate("TaskPathSimulator", u"TextLabel", None))
        self.btnLaunchCamotics.setText(QCoreApplication.translate("TaskPathSimulator", u"Launch CAMotics", None))
        self.btnMakeFile.setText(QCoreApplication.translate("TaskPathSimulator", u"New CAMotics File", None))
    # retranslateUi

