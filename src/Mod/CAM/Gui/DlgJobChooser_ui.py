# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgJobChooser.ui'
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
    QDialogButtonBox, QSizePolicy, QVBoxLayout, QWidget)

class Ui_DlgJobChooser(object):
    def setupUi(self, DlgJobChooser):
        if not DlgJobChooser.objectName():
            DlgJobChooser.setObjectName(u"DlgJobChooser")
        DlgJobChooser.setWindowModality(Qt.WindowModal)
        DlgJobChooser.resize(264, 92)
        self.verticalLayout = QVBoxLayout(DlgJobChooser)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cboProject = QComboBox(DlgJobChooser)
        self.cboProject.setObjectName(u"cboProject")

        self.verticalLayout.addWidget(self.cboProject)

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
        DlgJobChooser.setWindowTitle(QCoreApplication.translate("DlgJobChooser", u"CAM Job Selection", None))
    # retranslateUi

