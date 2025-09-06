# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskPathSimulator.ui'
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
    QProgressBar, QSizePolicy, QSlider, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)
import Path_rc

class Ui_TaskPathSimulator(object):
    def setupUi(self, TaskPathSimulator):
        if not TaskPathSimulator.objectName():
            TaskPathSimulator.setObjectName(u"TaskPathSimulator")
        TaskPathSimulator.resize(266, 335)
        self.verticalLayout = QVBoxLayout(TaskPathSimulator)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.toolButtonStop = QToolButton(TaskPathSimulator)
        self.toolButtonStop.setObjectName(u"toolButtonStop")
        icon = QIcon()
        icon.addFile(u":/icons/CAM_BStop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButtonStop.setIcon(icon)
        self.toolButtonStop.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.toolButtonStop)

        self.toolButtonPlay = QToolButton(TaskPathSimulator)
        self.toolButtonPlay.setObjectName(u"toolButtonPlay")
        icon1 = QIcon()
        icon1.addFile(u":/icons/CAM_BPlay.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButtonPlay.setIcon(icon1)
        self.toolButtonPlay.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.toolButtonPlay)

        self.toolButtonPause = QToolButton(TaskPathSimulator)
        self.toolButtonPause.setObjectName(u"toolButtonPause")
        icon2 = QIcon()
        icon2.addFile(u":/icons/CAM_BPause.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButtonPause.setIcon(icon2)
        self.toolButtonPause.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.toolButtonPause)

        self.toolButtonStep = QToolButton(TaskPathSimulator)
        self.toolButtonStep.setObjectName(u"toolButtonStep")
        icon3 = QIcon()
        icon3.addFile(u":/icons/CAM_BStep.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButtonStep.setIcon(icon3)
        self.toolButtonStep.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.toolButtonStep)

        self.toolButtonFF = QToolButton(TaskPathSimulator)
        self.toolButtonFF.setObjectName(u"toolButtonFF")
        icon4 = QIcon()
        icon4.addFile(u":/icons/CAM_BFastForward.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButtonFF.setIcon(icon4)
        self.toolButtonFF.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.toolButtonFF)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.progressBar = QProgressBar(TaskPathSimulator)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QSize(16777215, 5))
        self.progressBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_3 = QLabel(TaskPathSimulator)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.sliderSpeed = QSlider(TaskPathSimulator)
        self.sliderSpeed.setObjectName(u"sliderSpeed")
        self.sliderSpeed.setMinimum(1)
        self.sliderSpeed.setMaximum(50)
        self.sliderSpeed.setValue(50)
        self.sliderSpeed.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.sliderSpeed)

        self.labelGPerSec = QLabel(TaskPathSimulator)
        self.labelGPerSec.setObjectName(u"labelGPerSec")
        self.labelGPerSec.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_3.addWidget(self.labelGPerSec)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

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
        self.labelAccuracy.setText(u"%")

        self.horizontalLayout_4.addWidget(self.labelAccuracy)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(TaskPathSimulator)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.comboJobs = QComboBox(TaskPathSimulator)
        self.comboJobs.setObjectName(u"comboJobs")

        self.horizontalLayout.addWidget(self.comboJobs)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listOperations = QListWidget(TaskPathSimulator)
        self.listOperations.setObjectName(u"listOperations")
        self.listOperations.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout.addWidget(self.listOperations)

        self.labelNote = QLabel(TaskPathSimulator)
        self.labelNote.setObjectName(u"labelNote")
        self.labelNote.setStyleSheet(u"QLabel { color: rgb(250, 100, 0) }")
        self.labelNote.setWordWrap(True)

        self.verticalLayout.addWidget(self.labelNote)


        self.retranslateUi(TaskPathSimulator)

        QMetaObject.connectSlotsByName(TaskPathSimulator)
    # setupUi

    def retranslateUi(self, TaskPathSimulator):
        TaskPathSimulator.setWindowTitle(QCoreApplication.translate("TaskPathSimulator", u"Path Simulator", None))
#if QT_CONFIG(tooltip)
        self.toolButtonStop.setToolTip(QCoreApplication.translate("TaskPathSimulator", u"Stop running simulation", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonStop.setText(QCoreApplication.translate("TaskPathSimulator", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.toolButtonPlay.setToolTip(QCoreApplication.translate("TaskPathSimulator", u"Activate/resume simulation", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonPlay.setText(QCoreApplication.translate("TaskPathSimulator", u"Play", None))
#if QT_CONFIG(tooltip)
        self.toolButtonPause.setToolTip(QCoreApplication.translate("TaskPathSimulator", u"Pause simulation", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonPause.setText(QCoreApplication.translate("TaskPathSimulator", u"Pause", None))
#if QT_CONFIG(tooltip)
        self.toolButtonStep.setToolTip(QCoreApplication.translate("TaskPathSimulator", u"Single step simulation", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonStep.setText(QCoreApplication.translate("TaskPathSimulator", u"Step", None))
#if QT_CONFIG(tooltip)
        self.toolButtonFF.setToolTip(QCoreApplication.translate("TaskPathSimulator", u"Run the simulation until it ends without an animation", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonFF.setText(QCoreApplication.translate("TaskPathSimulator", u"Fast Forward", None))
        self.label_3.setText(QCoreApplication.translate("TaskPathSimulator", u"Speed", None))
        self.labelGPerSec.setText(QCoreApplication.translate("TaskPathSimulator", u"G/s", None))
        self.label_4.setText(QCoreApplication.translate("TaskPathSimulator", u"Accuracy", None))
        self.label.setText(QCoreApplication.translate("TaskPathSimulator", u"Job", None))
        self.labelNote.setText(QCoreApplication.translate("TaskPathSimulator", u"* Note: Volumetric simulation, inaccuracies are inherent.", None))
    # retranslateUi

