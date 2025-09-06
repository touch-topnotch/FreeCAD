# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShapeSelector.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QToolBox, QVBoxLayout, QWidget)

class Ui_ShapeSelector(object):
    def setupUi(self, ShapeSelector):
        if not ShapeSelector.objectName():
            ShapeSelector.setObjectName(u"ShapeSelector")
        ShapeSelector.resize(900, 600)
        self.verticalLayout = QVBoxLayout(ShapeSelector)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QVBoxLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolBox = QToolBox(ShapeSelector)
        self.toolBox.setObjectName(u"toolBox")
        self.standardTools = QWidget()
        self.standardTools.setObjectName(u"standardTools")
        self.standardTools.setGeometry(QRect(0, 0, 880, 487))
        self.toolBox.addItem(self.standardTools, u"Standard tools")
        self.customTools = QWidget()
        self.customTools.setObjectName(u"customTools")
        self.customTools.setGeometry(QRect(0, 0, 880, 487))
        self.toolBox.addItem(self.customTools, u"My tools")

        self.gridLayout.addWidget(self.toolBox)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(ShapeSelector)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)

        self.verticalLayout.addWidget(self.buttonBox)

        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(ShapeSelector)

        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(ShapeSelector)
    # setupUi

    def retranslateUi(self, ShapeSelector):
        ShapeSelector.setWindowTitle(QCoreApplication.translate("ShapeSelector", u"Tool Shape Selection", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.standardTools), QCoreApplication.translate("ShapeSelector", u"Standard tools", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.customTools), QCoreApplication.translate("ShapeSelector", u"My tools", None))
    # retranslateUi

