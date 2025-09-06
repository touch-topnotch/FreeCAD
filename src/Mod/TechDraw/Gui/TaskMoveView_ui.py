# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskMoveView.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_TaskMoveView(object):
    def setupUi(self, TaskMoveView):
        if not TaskMoveView.objectName():
            TaskMoveView.setObjectName(u"TaskMoveView")
        TaskMoveView.resize(400, 159)
        self.verticalLayout = QVBoxLayout(TaskMoveView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lViewName = QLabel(TaskMoveView)
        self.lViewName.setObjectName(u"lViewName")

        self.gridLayout.addWidget(self.lViewName, 0, 0, 1, 1)

        self.leView = QLineEdit(TaskMoveView)
        self.leView.setObjectName(u"leView")
        self.leView.setReadOnly(True)

        self.gridLayout.addWidget(self.leView, 0, 1, 1, 1)

        self.pbView = QPushButton(TaskMoveView)
        self.pbView.setObjectName(u"pbView")
        self.pbView.setText(u"\u2026")

        self.gridLayout.addWidget(self.pbView, 0, 2, 1, 1)

        self.lFromPage = QLabel(TaskMoveView)
        self.lFromPage.setObjectName(u"lFromPage")

        self.gridLayout.addWidget(self.lFromPage, 1, 0, 1, 1)

        self.leFromPage = QLineEdit(TaskMoveView)
        self.leFromPage.setObjectName(u"leFromPage")
        self.leFromPage.setReadOnly(True)

        self.gridLayout.addWidget(self.leFromPage, 1, 1, 1, 1)

        self.pbFromPage = QPushButton(TaskMoveView)
        self.pbFromPage.setObjectName(u"pbFromPage")
        self.pbFromPage.setText(u"\u2026")

        self.gridLayout.addWidget(self.pbFromPage, 1, 2, 1, 1)

        self.lToPage = QLabel(TaskMoveView)
        self.lToPage.setObjectName(u"lToPage")

        self.gridLayout.addWidget(self.lToPage, 2, 0, 1, 1)

        self.leToPage = QLineEdit(TaskMoveView)
        self.leToPage.setObjectName(u"leToPage")
        self.leToPage.setReadOnly(True)

        self.gridLayout.addWidget(self.leToPage, 2, 1, 1, 1)

        self.pbToPage = QPushButton(TaskMoveView)
        self.pbToPage.setObjectName(u"pbToPage")
        self.pbToPage.setText(u"\u2026")

        self.gridLayout.addWidget(self.pbToPage, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)

        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(TaskMoveView)

        QMetaObject.connectSlotsByName(TaskMoveView)
    # setupUi

    def retranslateUi(self, TaskMoveView):
        TaskMoveView.setWindowTitle(QCoreApplication.translate("TaskMoveView", u"Move View", None))
        self.lViewName.setText(QCoreApplication.translate("TaskMoveView", u"View to move", None))
        self.lFromPage.setText(QCoreApplication.translate("TaskMoveView", u"From page", None))
        self.lToPage.setText(QCoreApplication.translate("TaskMoveView", u"To page", None))
    # retranslateUi

