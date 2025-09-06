# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogBimServerLogin.ui'
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
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(274, 179)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.editUrl = QLineEdit(Dialog)
        self.editUrl.setObjectName(u"editUrl")

        self.horizontalLayout_4.addWidget(self.editUrl)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.editLogin = QLineEdit(Dialog)
        self.editLogin.setObjectName(u"editLogin")

        self.horizontalLayout.addWidget(self.editLogin)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.editPassword = QLineEdit(Dialog)
        self.editPassword.setObjectName(u"editPassword")

        self.horizontalLayout_2.addWidget(self.editPassword)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.checkStore = QCheckBox(Dialog)
        self.checkStore.setObjectName(u"checkStore")

        self.verticalLayout.addWidget(self.checkStore)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"BimServer Login", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"BIM server URL", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Login (email)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.checkStore.setText(QCoreApplication.translate("Dialog", u"Stay logged in across FreeCAD sessions", None))
    # retranslateUi

