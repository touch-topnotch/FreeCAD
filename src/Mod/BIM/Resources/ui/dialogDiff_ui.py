# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogDiff.ui'
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
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_IFCdiff(object):
    def setupUi(self, IFCdiff):
        if not IFCdiff.objectName():
            IFCdiff.setObjectName(u"IFCdiff")
        IFCdiff.resize(721, 299)
        self.verticalLayout = QVBoxLayout(IFCdiff)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(IFCdiff)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.buttonBox = QDialogButtonBox(IFCdiff)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(IFCdiff)
        self.buttonBox.accepted.connect(IFCdiff.accept)
        self.buttonBox.rejected.connect(IFCdiff.reject)

        QMetaObject.connectSlotsByName(IFCdiff)
    # setupUi

    def retranslateUi(self, IFCdiff):
        IFCdiff.setWindowTitle(QCoreApplication.translate("IFCdiff", u"IFC Difference", None))
    # retranslateUi

