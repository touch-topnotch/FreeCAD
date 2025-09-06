# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgTCChooser.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_DlgJobChooser(object):
    def setupUi(self, DlgJobChooser):
        if not DlgJobChooser.objectName():
            DlgJobChooser.setObjectName(u"DlgJobChooser")
        DlgJobChooser.setWindowModality(Qt.WindowModal)
        DlgJobChooser.resize(367, 99)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DlgJobChooser.sizePolicy().hasHeightForWidth())
        DlgJobChooser.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(DlgJobChooser)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DlgJobChooser)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.uiToolController = QComboBox(DlgJobChooser)
        self.uiToolController.setObjectName(u"uiToolController")

        self.verticalLayout.addWidget(self.uiToolController)

        self.buttonBox = QDialogButtonBox(DlgJobChooser)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DlgJobChooser)
        self.buttonBox.accepted.connect(DlgJobChooser.accept)
        self.buttonBox.rejected.connect(DlgJobChooser.reject)

        QMetaObject.connectSlotsByName(DlgJobChooser)
    # setupUi

    def retranslateUi(self, DlgJobChooser):
        DlgJobChooser.setWindowTitle(QCoreApplication.translate("DlgJobChooser", u"Tool Controller Selection", None))
        self.label.setText(QCoreApplication.translate("DlgJobChooser", u"Tool controller", None))
    # retranslateUi

