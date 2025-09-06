# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ZCorrectEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QToolBox, QToolButton, QVBoxLayout, QWidget)

class Ui_TaskPanel(object):
    def setupUi(self, TaskPanel):
        if not TaskPanel.objectName():
            TaskPanel.setObjectName(u"TaskPanel")
        TaskPanel.resize(376, 387)
        self.verticalLayout = QVBoxLayout(TaskPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolBox = QToolBox(TaskPanel)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setFrameShape(QFrame.NoFrame)
        self.Dressup = QWidget()
        self.Dressup.setObjectName(u"Dressup")
        self.Dressup.setGeometry(QRect(0, 0, 358, 340))
        self.gridLayout = QGridLayout(self.Dressup)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_3 = QGroupBox(self.Dressup)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.ProbePointFileName = QLineEdit(self.groupBox_3)
        self.ProbePointFileName.setObjectName(u"ProbePointFileName")

        self.gridLayout_3.addWidget(self.ProbePointFileName, 0, 1, 1, 1)

        self.SetProbePointFileName = QToolButton(self.groupBox_3)
        self.SetProbePointFileName.setObjectName(u"SetProbePointFileName")
        self.SetProbePointFileName.setText(u"\u2026")

        self.gridLayout_3.addWidget(self.SetProbePointFileName, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.toolBox.addItem(self.Dressup, u"Dressup")

        self.verticalLayout.addWidget(self.toolBox)


        self.retranslateUi(TaskPanel)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TaskPanel)
    # setupUi

    def retranslateUi(self, TaskPanel):
        TaskPanel.setWindowTitle(QCoreApplication.translate("TaskPanel", u"Z Depth Correction", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("TaskPanel", u"Probe Points File", None))
        self.label_4.setText(QCoreApplication.translate("TaskPanel", u"File Name", None))
#if QT_CONFIG(tooltip)
        self.ProbePointFileName.setToolTip(QCoreApplication.translate("TaskPanel", u"Enter the filename containing the probe data", None))
#endif // QT_CONFIG(tooltip)
        self.ProbePointFileName.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.Dressup), QCoreApplication.translate("TaskPanel", u"Dressup", None))
    # retranslateUi

