# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgActiveBody.ui'
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
    QLabel, QListWidget, QListWidgetItem, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_PartDesignGui_DlgActiveBody(object):
    def setupUi(self, PartDesignGui__DlgActiveBody):
        if not PartDesignGui__DlgActiveBody.objectName():
            PartDesignGui__DlgActiveBody.setObjectName(u"PartDesignGui__DlgActiveBody")
        PartDesignGui__DlgActiveBody.resize(480, 270)
        self.verticalLayout_2 = QVBoxLayout(PartDesignGui__DlgActiveBody)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(PartDesignGui__DlgActiveBody)
        self.label.setObjectName(u"label")
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.bodySelect = QListWidget(PartDesignGui__DlgActiveBody)
        QListWidgetItem(self.bodySelect)
        self.bodySelect.setObjectName(u"bodySelect")

        self.verticalLayout_2.addWidget(self.bodySelect)

        self.buttonBox = QDialogButtonBox(PartDesignGui__DlgActiveBody)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(PartDesignGui__DlgActiveBody)
        self.buttonBox.accepted.connect(PartDesignGui__DlgActiveBody.accept)
        self.buttonBox.rejected.connect(PartDesignGui__DlgActiveBody.reject)

        QMetaObject.connectSlotsByName(PartDesignGui__DlgActiveBody)
    # setupUi

    def retranslateUi(self, PartDesignGui__DlgActiveBody):
        PartDesignGui__DlgActiveBody.setWindowTitle(QCoreApplication.translate("PartDesignGui::DlgActiveBody", u"Active Body Required", None))
        self.label.setText(QCoreApplication.translate("PartDesignGui::DlgActiveBody", u"To create a new Part Design object, there must be an active body in the document.\n"
"Select a body from below, or create a new body.", None))

        __sortingEnabled = self.bodySelect.isSortingEnabled()
        self.bodySelect.setSortingEnabled(False)
        ___qlistwidgetitem = self.bodySelect.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("PartDesignGui::DlgActiveBody", u"Create New Body", None));
        self.bodySelect.setSortingEnabled(__sortingEnabled)

    # retranslateUi

