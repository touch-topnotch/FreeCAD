# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskProjection.ui'
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

class Ui_TechDrawGui_TaskProjection(object):
    def setupUi(self, TechDrawGui__TaskProjection):
        if not TechDrawGui__TaskProjection.objectName():
            TechDrawGui__TaskProjection.setObjectName(u"TechDrawGui__TaskProjection")
        TechDrawGui__TaskProjection.resize(353, 300)
        self.verticalLayout_2 = QVBoxLayout(TechDrawGui__TaskProjection)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cbVisSharp = QCheckBox(TechDrawGui__TaskProjection)
        self.cbVisSharp.setObjectName(u"cbVisSharp")
        self.cbVisSharp.setChecked(True)

        self.verticalLayout.addWidget(self.cbVisSharp)

        self.cbVisSmooth = QCheckBox(TechDrawGui__TaskProjection)
        self.cbVisSmooth.setObjectName(u"cbVisSmooth")
        self.cbVisSmooth.setChecked(True)

        self.verticalLayout.addWidget(self.cbVisSmooth)

        self.cbVisSewn = QCheckBox(TechDrawGui__TaskProjection)
        self.cbVisSewn.setObjectName(u"cbVisSewn")
        self.cbVisSewn.setChecked(True)

        self.verticalLayout.addWidget(self.cbVisSewn)

        self.cbVisOutline = QCheckBox(TechDrawGui__TaskProjection)
        self.cbVisOutline.setObjectName(u"cbVisOutline")
        self.cbVisOutline.setChecked(True)

        self.verticalLayout.addWidget(self.cbVisOutline)

        self.cbVisIso = QCheckBox(TechDrawGui__TaskProjection)
        self.cbVisIso.setObjectName(u"cbVisIso")
        self.cbVisIso.setChecked(True)

        self.verticalLayout.addWidget(self.cbVisIso)

        self.cbHidSharp = QCheckBox(TechDrawGui__TaskProjection)
        self.cbHidSharp.setObjectName(u"cbHidSharp")

        self.verticalLayout.addWidget(self.cbHidSharp)

        self.cbHidSmooth = QCheckBox(TechDrawGui__TaskProjection)
        self.cbHidSmooth.setObjectName(u"cbHidSmooth")

        self.verticalLayout.addWidget(self.cbHidSmooth)

        self.cbHidSewn = QCheckBox(TechDrawGui__TaskProjection)
        self.cbHidSewn.setObjectName(u"cbHidSewn")

        self.verticalLayout.addWidget(self.cbHidSewn)

        self.cbHidOutline = QCheckBox(TechDrawGui__TaskProjection)
        self.cbHidOutline.setObjectName(u"cbHidOutline")

        self.verticalLayout.addWidget(self.cbHidOutline)

        self.cbHidIso = QCheckBox(TechDrawGui__TaskProjection)
        self.cbHidIso.setObjectName(u"cbHidIso")

        self.verticalLayout.addWidget(self.cbHidIso)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(TechDrawGui__TaskProjection)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskProjection)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskProjection):
        TechDrawGui__TaskProjection.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskProjection", u"Project Shapes", None))
        self.cbVisSharp.setText(QCoreApplication.translate("TechDrawGui::TaskProjection", u"Visible sharp edges", None))
        self.cbVisSmooth.setText(QCoreApplication.translate("TechDrawGui::TaskProjection", u"Visible smooth edges", None))
        self.cbVisSewn.setText(QCoreApplication.translate("TechDrawGui::TaskProjection", u"Visible sewn edges", None))
        self.cbVisOutline.setText(QCoreApplication.translate("TechDrawGui::TaskProjection", u"Visible outline edges", None))
        self.cbVisIso.setText(QCoreApplication.translate("TechDrawGui::TaskProjection", u"Visible isoparameters", None))
        self.cbHidSharp.setText(QCoreApplication.translate("TechDrawGui::TaskProjection", u"Hidden sharp edges", None))
        self.cbHidSmooth.setText(QCoreApplication.translate("TechDrawGui::TaskProjection", u"Hidden smooth edges", None))
        self.cbHidSewn.setText(QCoreApplication.translate("TechDrawGui::TaskProjection", u"Hidden sewn edges", None))
        self.cbHidOutline.setText(QCoreApplication.translate("TechDrawGui::TaskProjection", u"Hidden outline edges", None))
        self.cbHidIso.setText(QCoreApplication.translate("TechDrawGui::TaskProjection", u"Hidden iso-parameters", None))
    # retranslateUi

