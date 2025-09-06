# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskRestoreLines.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_TechDrawGui_TaskRestoreLines(object):
    def setupUi(self, TechDrawGui__TaskRestoreLines):
        if not TechDrawGui__TaskRestoreLines.objectName():
            TechDrawGui__TaskRestoreLines.setObjectName(u"TechDrawGui__TaskRestoreLines")
        TechDrawGui__TaskRestoreLines.resize(227, 130)
        self.verticalLayout = QVBoxLayout(TechDrawGui__TaskRestoreLines)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_All = QPushButton(TechDrawGui__TaskRestoreLines)
        self.pb_All.setObjectName(u"pb_All")

        self.gridLayout.addWidget(self.pb_All, 0, 0, 1, 1)

        self.l_All = QLabel(TechDrawGui__TaskRestoreLines)
        self.l_All.setObjectName(u"l_All")
        self.l_All.setText(u"0")
        self.l_All.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_All, 0, 1, 1, 1)

        self.pb_Geometry = QPushButton(TechDrawGui__TaskRestoreLines)
        self.pb_Geometry.setObjectName(u"pb_Geometry")

        self.gridLayout.addWidget(self.pb_Geometry, 1, 0, 1, 1)

        self.l_Geometry = QLabel(TechDrawGui__TaskRestoreLines)
        self.l_Geometry.setObjectName(u"l_Geometry")
        self.l_Geometry.setText(u"0")
        self.l_Geometry.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_Geometry, 1, 1, 1, 1)

        self.pb_Cosmetic = QPushButton(TechDrawGui__TaskRestoreLines)
        self.pb_Cosmetic.setObjectName(u"pb_Cosmetic")

        self.gridLayout.addWidget(self.pb_Cosmetic, 2, 0, 1, 1)

        self.l_Cosmetic = QLabel(TechDrawGui__TaskRestoreLines)
        self.l_Cosmetic.setObjectName(u"l_Cosmetic")
        self.l_Cosmetic.setText(u"0")
        self.l_Cosmetic.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_Cosmetic, 2, 1, 1, 1)

        self.pb_Center = QPushButton(TechDrawGui__TaskRestoreLines)
        self.pb_Center.setObjectName(u"pb_Center")

        self.gridLayout.addWidget(self.pb_Center, 3, 0, 1, 1)

        self.l_Center = QLabel(TechDrawGui__TaskRestoreLines)
        self.l_Center.setObjectName(u"l_Center")
        self.l_Center.setText(u"0")
        self.l_Center.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_Center, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(TechDrawGui__TaskRestoreLines)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskRestoreLines)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskRestoreLines):
        TechDrawGui__TaskRestoreLines.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskRestoreLines", u"Restore Invisible Lines", None))
        self.pb_All.setText(QCoreApplication.translate("TechDrawGui::TaskRestoreLines", u"All", None))
        self.pb_Geometry.setText(QCoreApplication.translate("TechDrawGui::TaskRestoreLines", u"Geometry", None))
        self.pb_Cosmetic.setText(QCoreApplication.translate("TechDrawGui::TaskRestoreLines", u"Cosmetic", None))
        self.pb_Center.setText(QCoreApplication.translate("TechDrawGui::TaskRestoreLines", u"Centerline", None))
    # retranslateUi

