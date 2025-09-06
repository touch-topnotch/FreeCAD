# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskDlgPathCompound.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QLabel,
    QListWidget, QListWidgetItem, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_TaskDlgPathCompound(object):
    def setupUi(self, TaskDlgPathCompound):
        if not TaskDlgPathCompound.objectName():
            TaskDlgPathCompound.setObjectName(u"TaskDlgPathCompound")
        TaskDlgPathCompound.resize(315, 404)
        self.verticalLayout = QVBoxLayout(TaskDlgPathCompound)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(TaskDlgPathCompound)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.PathsList = QListWidget(TaskDlgPathCompound)
        self.PathsList.setObjectName(u"PathsList")
        self.PathsList.setFrameShape(QFrame.StyledPanel)
        self.PathsList.setLineWidth(1)
        self.PathsList.setDragDropMode(QAbstractItemView.InternalMove)
        self.PathsList.setDefaultDropAction(Qt.MoveAction)

        self.verticalLayout.addWidget(self.PathsList)


        self.retranslateUi(TaskDlgPathCompound)

        QMetaObject.connectSlotsByName(TaskDlgPathCompound)
    # setupUi

    def retranslateUi(self, TaskDlgPathCompound):
        TaskDlgPathCompound.setWindowTitle(QCoreApplication.translate("TaskDlgPathCompound", u"Paths List", None))
        self.label.setText(QCoreApplication.translate("TaskDlgPathCompound", u"Reorder children by dragging and dropping them to their correct location", None))
    # retranslateUi

