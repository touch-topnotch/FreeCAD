# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskAssemblyCreateSimulation.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)

class Ui_TaskAssemblyCreateSimulation(object):
    def setupUi(self, TaskAssemblyCreateSimulation):
        if not TaskAssemblyCreateSimulation.objectName():
            TaskAssemblyCreateSimulation.setObjectName(u"TaskAssemblyCreateSimulation")
        TaskAssemblyCreateSimulation.resize(400, 602)
        self.verticalLayout_2 = QVBoxLayout(TaskAssemblyCreateSimulation)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_motions = QGroupBox(TaskAssemblyCreateSimulation)
        self.groupBox_motions.setObjectName(u"groupBox_motions")
        self.gridLayout = QGridLayout(self.groupBox_motions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.motionList = QListWidget(self.groupBox_motions)
        self.motionList.setObjectName(u"motionList")
        self.motionList.setMaximumSize(QSize(16777215, 75))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.motionList.sizePolicy().hasHeightForWidth())
        self.motionList.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.motionList, 0, 0, 1, 1)

        self.motion_buttonsLayout = QVBoxLayout()
        self.motion_buttonsLayout.setObjectName(u"motion_buttonsLayout")
        self.AddButton = QToolButton(self.groupBox_motions)
        self.AddButton.setObjectName(u"AddButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.AddButton.sizePolicy().hasHeightForWidth())
        self.AddButton.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/icons/list-add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.AddButton.setIcon(icon)

        self.motion_buttonsLayout.addWidget(self.AddButton)

        self.RemoveButton = QToolButton(self.groupBox_motions)
        self.RemoveButton.setObjectName(u"RemoveButton")
        sizePolicy1.setHeightForWidth(self.RemoveButton.sizePolicy().hasHeightForWidth())
        self.RemoveButton.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/edit-delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.RemoveButton.setIcon(icon1)

        self.motion_buttonsLayout.addWidget(self.RemoveButton)


        self.gridLayout.addLayout(self.motion_buttonsLayout, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_motions)

        self.groupBox_settings = QGroupBox(TaskAssemblyCreateSimulation)
        self.groupBox_settings.setObjectName(u"groupBox_settings")
        self.gridLayout1 = QGridLayout(self.groupBox_settings)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.TimeStartLabel = QLabel(self.groupBox_settings)
        self.TimeStartLabel.setObjectName(u"TimeStartLabel")

        self.gridLayout1.addWidget(self.TimeStartLabel, 0, 0, 1, 1)

        self.TimeStartSpinBox = Gui_PrefQuantitySpinBox(self.groupBox_settings)
        self.TimeStartSpinBox.setObjectName(u"TimeStartSpinBox")

        self.gridLayout1.addWidget(self.TimeStartSpinBox, 0, 1, 1, 1)

        self.TimeEndLabel = QLabel(self.groupBox_settings)
        self.TimeEndLabel.setObjectName(u"TimeEndLabel")

        self.gridLayout1.addWidget(self.TimeEndLabel, 1, 0, 1, 1)

        self.TimeEndSpinBox = Gui_PrefQuantitySpinBox(self.groupBox_settings)
        self.TimeEndSpinBox.setObjectName(u"TimeEndSpinBox")

        self.gridLayout1.addWidget(self.TimeEndSpinBox, 1, 1, 1, 1)

        self.TimeStepOutputLabel = QLabel(self.groupBox_settings)
        self.TimeStepOutputLabel.setObjectName(u"TimeStepOutputLabel")

        self.gridLayout1.addWidget(self.TimeStepOutputLabel, 2, 0, 1, 1)

        self.TimeStepOutputSpinBox = Gui_PrefQuantitySpinBox(self.groupBox_settings)
        self.TimeStepOutputSpinBox.setObjectName(u"TimeStepOutputSpinBox")

        self.gridLayout1.addWidget(self.TimeStepOutputSpinBox, 2, 1, 1, 1)

        self.GlobalErrorToleranceLabel = QLabel(self.groupBox_settings)
        self.GlobalErrorToleranceLabel.setObjectName(u"GlobalErrorToleranceLabel")

        self.gridLayout1.addWidget(self.GlobalErrorToleranceLabel, 5, 0, 1, 1)

        self.GlobalErrorToleranceSpinBox = Gui_PrefQuantitySpinBox(self.groupBox_settings)
        self.GlobalErrorToleranceSpinBox.setObjectName(u"GlobalErrorToleranceSpinBox")

        self.gridLayout1.addWidget(self.GlobalErrorToleranceSpinBox, 5, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_settings)

        self.RunKinematicsButton = QPushButton(TaskAssemblyCreateSimulation)
        self.RunKinematicsButton.setObjectName(u"RunKinematicsButton")

        self.verticalLayout_2.addWidget(self.RunKinematicsButton)

        self.groupBox_player = QGroupBox(TaskAssemblyCreateSimulation)
        self.groupBox_player.setObjectName(u"groupBox_player")
        self.gridLayout2 = QGridLayout(self.groupBox_player)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.FrameLabel = QLabel(self.groupBox_player)
        self.FrameLabel.setObjectName(u"FrameLabel")

        self.gridLayout_2.addWidget(self.FrameLabel, 0, 0, 1, 1)

        self.frameSlider = QSlider(self.groupBox_player)
        self.frameSlider.setObjectName(u"frameSlider")
        sizePolicy.setHeightForWidth(self.frameSlider.sizePolicy().hasHeightForWidth())
        self.frameSlider.setSizePolicy(sizePolicy)
        self.frameSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.frameSlider, 0, 1, 1, 1)

        self.FrameTimeLabel = QLabel(self.groupBox_player)
        self.FrameTimeLabel.setObjectName(u"FrameTimeLabel")

        self.gridLayout_2.addWidget(self.FrameTimeLabel, 0, 2, 1, 1)


        self.gridLayout2.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.fps_layout = QHBoxLayout()
        self.fps_layout.setObjectName(u"fps_layout")
        self.FramesPerSecondLabel = QLabel(self.groupBox_player)
        self.FramesPerSecondLabel.setObjectName(u"FramesPerSecondLabel")

        self.fps_layout.addWidget(self.FramesPerSecondLabel)

        self.FramesPerSecondSpinBox = QSpinBox(self.groupBox_player)
        self.FramesPerSecondSpinBox.setObjectName(u"FramesPerSecondSpinBox")

        self.fps_layout.addWidget(self.FramesPerSecondSpinBox)


        self.gridLayout2.addLayout(self.fps_layout, 1, 0, 1, 1)

        self.controls_layout = QHBoxLayout()
        self.controls_layout.setObjectName(u"controls_layout")
        self.StepBackwardButton = QToolButton(self.groupBox_player)
        self.StepBackwardButton.setObjectName(u"StepBackwardButton")
        sizePolicy1.setHeightForWidth(self.StepBackwardButton.sizePolicy().hasHeightForWidth())
        self.StepBackwardButton.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/media-playback-step-back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.StepBackwardButton.setIcon(icon2)

        self.controls_layout.addWidget(self.StepBackwardButton)

        self.PlayBackwardButton = QToolButton(self.groupBox_player)
        self.PlayBackwardButton.setObjectName(u"PlayBackwardButton")
        sizePolicy1.setHeightForWidth(self.PlayBackwardButton.sizePolicy().hasHeightForWidth())
        self.PlayBackwardButton.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/media-playback-start-back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PlayBackwardButton.setIcon(icon3)

        self.controls_layout.addWidget(self.PlayBackwardButton)

        self.StopButton = QToolButton(self.groupBox_player)
        self.StopButton.setObjectName(u"StopButton")
        sizePolicy1.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/media-playback-stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.StopButton.setIcon(icon4)

        self.controls_layout.addWidget(self.StopButton)

        self.PlayForwardButton = QToolButton(self.groupBox_player)
        self.PlayForwardButton.setObjectName(u"PlayForwardButton")
        sizePolicy1.setHeightForWidth(self.PlayForwardButton.sizePolicy().hasHeightForWidth())
        self.PlayForwardButton.setSizePolicy(sizePolicy1)
        icon5 = QIcon()
        icon5.addFile(u":/icons/media-playback-start.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PlayForwardButton.setIcon(icon5)

        self.controls_layout.addWidget(self.PlayForwardButton)

        self.StepForwardButton = QToolButton(self.groupBox_player)
        self.StepForwardButton.setObjectName(u"StepForwardButton")
        sizePolicy1.setHeightForWidth(self.StepForwardButton.sizePolicy().hasHeightForWidth())
        self.StepForwardButton.setSizePolicy(sizePolicy1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/media-playback-step.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.StepForwardButton.setIcon(icon6)

        self.controls_layout.addWidget(self.StepForwardButton)


        self.gridLayout2.addLayout(self.controls_layout, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_player)


        self.retranslateUi(TaskAssemblyCreateSimulation)

        QMetaObject.connectSlotsByName(TaskAssemblyCreateSimulation)
    # setupUi

    def retranslateUi(self, TaskAssemblyCreateSimulation):
        TaskAssemblyCreateSimulation.setWindowTitle(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Simulation", None))
        self.groupBox_motions.setTitle(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Motions", None))
#if QT_CONFIG(tooltip)
        self.AddButton.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Add a prescribed motion", None))
#endif // QT_CONFIG(tooltip)
        self.AddButton.setText("")
#if QT_CONFIG(tooltip)
        self.RemoveButton.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Delete selected motions", None))
#endif // QT_CONFIG(tooltip)
        self.RemoveButton.setText("")
        self.groupBox_settings.setTitle(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Simulation Settings", None))
        self.TimeStartLabel.setText(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Start", None))
#if QT_CONFIG(tooltip)
        self.TimeStartLabel.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Start time of the simulation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.TimeStartSpinBox.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Start time of the simulation", None))
#endif // QT_CONFIG(tooltip)
        self.TimeEndLabel.setText(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"End", None))
#if QT_CONFIG(tooltip)
        self.TimeEndLabel.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"End time of the simulation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.TimeEndSpinBox.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"End time of the simulation", None))
#endif // QT_CONFIG(tooltip)
        self.TimeStepOutputLabel.setText(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Step", None))
#if QT_CONFIG(tooltip)
        self.TimeStepOutputLabel.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Time step", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.TimeStepOutputSpinBox.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Time step", None))
#endif // QT_CONFIG(tooltip)
        self.GlobalErrorToleranceLabel.setText(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Tolerance", None))
#if QT_CONFIG(tooltip)
        self.GlobalErrorToleranceLabel.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Global error tolerance", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.GlobalErrorToleranceSpinBox.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Global error tolerance", None))
#endif // QT_CONFIG(tooltip)
        self.RunKinematicsButton.setText(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Generate", None))
        self.groupBox_player.setTitle(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Animation Player", None))
        self.FrameLabel.setText(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Frame", None))
        self.FrameTimeLabel.setText(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"0.00 s", None))
        self.FramesPerSecondLabel.setText(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Frames per second", None))
#if QT_CONFIG(tooltip)
        self.StepBackwardButton.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Step backward", None))
#endif // QT_CONFIG(tooltip)
        self.StepBackwardButton.setText("")
#if QT_CONFIG(tooltip)
        self.PlayBackwardButton.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Play backward", None))
#endif // QT_CONFIG(tooltip)
        self.PlayBackwardButton.setText("")
#if QT_CONFIG(tooltip)
        self.StopButton.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Stop", None))
#endif // QT_CONFIG(tooltip)
        self.StopButton.setText("")
#if QT_CONFIG(tooltip)
        self.PlayForwardButton.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Play forward", None))
#endif // QT_CONFIG(tooltip)
        self.PlayForwardButton.setText("")
#if QT_CONFIG(tooltip)
        self.StepForwardButton.setToolTip(QCoreApplication.translate("TaskAssemblyCreateSimulation", u"Step forward", None))
#endif // QT_CONFIG(tooltip)
        self.StepForwardButton.setText("")
    # retranslateUi

