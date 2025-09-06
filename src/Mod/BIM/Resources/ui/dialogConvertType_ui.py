# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogConvertType.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(448, 161)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.checkKeepObject = QCheckBox(Dialog)
        self.checkKeepObject.setObjectName(u"checkKeepObject")

        self.verticalLayout.addWidget(self.checkKeepObject)

        self.checkDoNotAskAgain = QCheckBox(Dialog)
        self.checkDoNotAskAgain.setObjectName(u"checkDoNotAskAgain")

        self.verticalLayout.addWidget(self.checkDoNotAskAgain)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Convert to IFC Type", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"This object will be converted to a %1 type. Types can be used to give common attributes and properties to several objects at once.", None))
        self.checkKeepObject.setText(QCoreApplication.translate("Dialog", u"Keep original object. The object will adopt the new type", None))
        self.checkDoNotAskAgain.setText(QCoreApplication.translate("Dialog", u"Do not ask again and use this setting", None))
    # retranslateUi

