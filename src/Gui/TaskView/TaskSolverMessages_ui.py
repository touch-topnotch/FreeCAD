# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskSolverMessages.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QToolButton,
    QWidget)

class Ui_TaskSolverMessages(object):
    def setupUi(self, TaskSolverMessages):
        if not TaskSolverMessages.objectName():
            TaskSolverMessages.setObjectName(u"TaskSolverMessages")
        TaskSolverMessages.resize(350, 48)
        TaskSolverMessages.setMinimumSize(QSize(320, 0))
        TaskSolverMessages.setWindowTitle(u"Form")
        self.horizontalLayout = QHBoxLayout(TaskSolverMessages)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelStatus = Gui_StatefulLabel(TaskSolverMessages)
        self.labelStatus.setObjectName(u"labelStatus")

        self.horizontalLayout.addWidget(self.labelStatus)

        self.labelStatusLink = Gui_UrlLabel(TaskSolverMessages)
        self.labelStatusLink.setObjectName(u"labelStatusLink")

        self.horizontalLayout.addWidget(self.labelStatusLink)

        self.manualUpdate = QToolButton(TaskSolverMessages)
        self.manualUpdate.setObjectName(u"manualUpdate")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manualUpdate.sizePolicy().hasHeightForWidth())
        self.manualUpdate.setSizePolicy(sizePolicy)
        self.manualUpdate.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/icons/view-refresh.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.manualUpdate.setIcon(icon)

        self.horizontalLayout.addWidget(self.manualUpdate)

        self.settingsButton = QToolButton(TaskSolverMessages)
        self.settingsButton.setObjectName(u"settingsButton")
        sizePolicy.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
        self.settingsButton.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/icons/preferences-general.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsButton.setIcon(icon1)
        self.settingsButton.setPopupMode(QToolButton.MenuButtonPopup)

        self.horizontalLayout.addWidget(self.settingsButton)


        self.retranslateUi(TaskSolverMessages)

        QMetaObject.connectSlotsByName(TaskSolverMessages)
    # setupUi

    def retranslateUi(self, TaskSolverMessages):
        self.labelStatus.setText(QCoreApplication.translate("TaskSolverMessages", u"DOF", None))
        self.labelStatusLink.setText(QCoreApplication.translate("TaskSolverMessages", u"Link", None))
#if QT_CONFIG(tooltip)
        self.manualUpdate.setToolTip(QCoreApplication.translate("TaskSolverMessages", u"Forces the recomputation of the active document", None))
#endif // QT_CONFIG(tooltip)
        self.manualUpdate.setText("")
#if QT_CONFIG(tooltip)
        self.settingsButton.setToolTip(QCoreApplication.translate("TaskSolverMessages", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsButton.setText("")
        pass
    # retranslateUi

