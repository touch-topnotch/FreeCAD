# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskCAMSimulator.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QSizePolicy, QSlider, QToolButton, QVBoxLayout,
    QWidget)
import Path_rc

class Ui_TaskPathSimulator(object):
    def setupUi(self, TaskPathSimulator):
        if not TaskPathSimulator.objectName():
            TaskPathSimulator.setObjectName(u"TaskPathSimulator")
        TaskPathSimulator.resize(577, 335)
        self.verticalLayout = QVBoxLayout(TaskPathSimulator)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.label_4 = QLabel(TaskPathSimulator)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.sliderAccuracy = QSlider(TaskPathSimulator)
        self.sliderAccuracy.setObjectName(u"sliderAccuracy")
        self.sliderAccuracy.setMinimum(1)
        self.sliderAccuracy.setMaximum(10)
        self.sliderAccuracy.setPageStep(2)
        self.sliderAccuracy.setValue(10)
        self.sliderAccuracy.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.sliderAccuracy)

        self.labelAccuracy = QLabel(TaskPathSimulator)
        self.labelAccuracy.setObjectName(u"labelAccuracy")
        self.labelAccuracy.setMinimumSize(QSize(50, 0))
        self.labelAccuracy.setMaximumSize(QSize(40, 16777215))
        self.labelAccuracy.setText(u"%")

        self.horizontalLayout_4.addWidget(self.labelAccuracy)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(TaskPathSimulator)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.comboJobs = QComboBox(TaskPathSimulator)
        self.comboJobs.setObjectName(u"comboJobs")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboJobs.sizePolicy().hasHeightForWidth())
        self.comboJobs.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.comboJobs)

        self.toolButtonPlay = QToolButton(TaskPathSimulator)
        self.toolButtonPlay.setObjectName(u"toolButtonPlay")
        icon = QIcon()
        icon.addFile(u":/icons/CAM_BPlay.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButtonPlay.setIcon(icon)
        self.toolButtonPlay.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.toolButtonPlay)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listOperations = QListWidget(TaskPathSimulator)
        self.listOperations.setObjectName(u"listOperations")
        self.listOperations.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout.addWidget(self.listOperations)


        self.retranslateUi(TaskPathSimulator)

        QMetaObject.connectSlotsByName(TaskPathSimulator)
    # setupUi

    def retranslateUi(self, TaskPathSimulator):
        TaskPathSimulator.setWindowTitle(QCoreApplication.translate("TaskPathSimulator", u"Path Simulator", None))
        self.label_4.setText(QCoreApplication.translate("TaskPathSimulator", u"Accuracy", None))
        self.label.setText(QCoreApplication.translate("TaskPathSimulator", u"Job", None))
#if QT_CONFIG(tooltip)
        self.toolButtonPlay.setToolTip(QCoreApplication.translate("TaskPathSimulator", u"Activate/resume simulation", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonPlay.setText(QCoreApplication.translate("TaskPathSimulator", u"Play", None))
    # retranslateUi

