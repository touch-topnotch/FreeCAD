# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskPreviewParameters.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_PartDesignGui_TaskPreviewParameters(object):
    def setupUi(self, PartDesignGui__TaskPreviewParameters):
        if not PartDesignGui__TaskPreviewParameters.objectName():
            PartDesignGui__TaskPreviewParameters.setObjectName(u"PartDesignGui__TaskPreviewParameters")
        PartDesignGui__TaskPreviewParameters.resize(364, 62)
        PartDesignGui__TaskPreviewParameters.setWindowTitle(u"Form")
        self.verticalLayout_4 = QVBoxLayout(PartDesignGui__TaskPreviewParameters)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.showFinalCheckBox = QCheckBox(PartDesignGui__TaskPreviewParameters)
        self.showFinalCheckBox.setObjectName(u"showFinalCheckBox")

        self.verticalLayout_4.addWidget(self.showFinalCheckBox)

        self.showTransparentPreviewCheckBox = QCheckBox(PartDesignGui__TaskPreviewParameters)
        self.showTransparentPreviewCheckBox.setObjectName(u"showTransparentPreviewCheckBox")

        self.verticalLayout_4.addWidget(self.showTransparentPreviewCheckBox)


        self.retranslateUi(PartDesignGui__TaskPreviewParameters)

        QMetaObject.connectSlotsByName(PartDesignGui__TaskPreviewParameters)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskPreviewParameters):
        self.showFinalCheckBox.setText(QCoreApplication.translate("PartDesignGui::TaskPreviewParameters", u"Show final result", None))
        self.showTransparentPreviewCheckBox.setText(QCoreApplication.translate("PartDesignGui::TaskPreviewParameters", u"Show preview overlay", None))
        pass
    # retranslateUi

