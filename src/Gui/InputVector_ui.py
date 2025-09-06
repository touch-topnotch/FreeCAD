# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InputVector.ui'
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
    QDoubleSpinBox, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QWidget)

class Ui_Gui_Dialog_InputVector(object):
    def setupUi(self, Gui__Dialog__InputVector):
        if not Gui__Dialog__InputVector.objectName():
            Gui__Dialog__InputVector.setObjectName(u"Gui__Dialog__InputVector")
        Gui__Dialog__InputVector.resize(181, 177)
        self.gridLayout = QGridLayout(Gui__Dialog__InputVector)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Gui__Dialog__InputVector)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout1 = QGridLayout(self.groupBox)
#ifndef Q_OS_MAC
        self.gridLayout1.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
#endif
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout1.addWidget(self.label, 0, 0, 1, 1)

        self.vectorX = QDoubleSpinBox(self.groupBox)
        self.vectorX.setObjectName(u"vectorX")
        self.vectorX.setMinimum(-2147480000.000000000000000)
        self.vectorX.setMaximum(2147480000.000000000000000)

        self.gridLayout1.addWidget(self.vectorX, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout1.addWidget(self.label_2, 1, 0, 1, 1)

        self.vectorY = QDoubleSpinBox(self.groupBox)
        self.vectorY.setObjectName(u"vectorY")
        self.vectorY.setMinimum(-2147480000.000000000000000)
        self.vectorY.setMaximum(2147480000.000000000000000)

        self.gridLayout1.addWidget(self.vectorY, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout1.addWidget(self.label_3, 2, 0, 1, 1)

        self.vectorZ = QDoubleSpinBox(self.groupBox)
        self.vectorZ.setObjectName(u"vectorZ")
        self.vectorZ.setMinimum(-2147480000.000000000000000)
        self.vectorZ.setMaximum(2147480000.000000000000000)
        self.vectorZ.setValue(1.000000000000000)

        self.gridLayout1.addWidget(self.vectorZ, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__InputVector)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.vectorX, self.vectorY)
        QWidget.setTabOrder(self.vectorY, self.vectorZ)

        self.retranslateUi(Gui__Dialog__InputVector)
        self.buttonBox.accepted.connect(Gui__Dialog__InputVector.accept)

        QMetaObject.connectSlotsByName(Gui__Dialog__InputVector)
    # setupUi

    def retranslateUi(self, Gui__Dialog__InputVector):
        Gui__Dialog__InputVector.setWindowTitle(QCoreApplication.translate("Gui::Dialog::InputVector", u"Input Vector", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::InputVector", u"Vector", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::InputVector", u"X", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::InputVector", u"Y", None))
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::InputVector", u"Z", None))
    # retranslateUi

