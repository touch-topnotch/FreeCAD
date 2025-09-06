# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Clipping.ui'
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
    QDialogButtonBox, QDoubleSpinBox, QGridLayout, QGroupBox,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Gui_Dialog_Clipping(object):
    def setupUi(self, Gui__Dialog__Clipping):
        if not Gui__Dialog__Clipping.objectName():
            Gui__Dialog__Clipping.setObjectName(u"Gui__Dialog__Clipping")
        Gui__Dialog__Clipping.resize(304, 430)
        self.gridLayout_5 = QGridLayout(Gui__Dialog__Clipping)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBoxX = QGroupBox(Gui__Dialog__Clipping)
        self.groupBoxX.setObjectName(u"groupBoxX")
        self.groupBoxX.setCheckable(True)
        self.groupBoxX.setChecked(False)
        self.gridLayout = QGridLayout(self.groupBoxX)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBoxX)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.clipX = QDoubleSpinBox(self.groupBoxX)
        self.clipX.setObjectName(u"clipX")

        self.gridLayout.addWidget(self.clipX, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.flipClipX = QPushButton(self.groupBoxX)
        self.flipClipX.setObjectName(u"flipClipX")

        self.gridLayout.addWidget(self.flipClipX, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.groupBoxX, 0, 0, 1, 1)

        self.groupBoxY = QGroupBox(Gui__Dialog__Clipping)
        self.groupBoxY.setObjectName(u"groupBoxY")
        self.groupBoxY.setCheckable(True)
        self.groupBoxY.setChecked(False)
        self.gridLayout_2 = QGridLayout(self.groupBoxY)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBoxY)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.clipY = QDoubleSpinBox(self.groupBoxY)
        self.clipY.setObjectName(u"clipY")

        self.gridLayout_2.addWidget(self.clipY, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.flipClipY = QPushButton(self.groupBoxY)
        self.flipClipY.setObjectName(u"flipClipY")

        self.gridLayout_2.addWidget(self.flipClipY, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.groupBoxY, 1, 0, 1, 1)

        self.groupBoxZ = QGroupBox(Gui__Dialog__Clipping)
        self.groupBoxZ.setObjectName(u"groupBoxZ")
        self.groupBoxZ.setCheckable(True)
        self.groupBoxZ.setChecked(False)
        self.gridLayout_3 = QGridLayout(self.groupBoxZ)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBoxZ)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.clipZ = QDoubleSpinBox(self.groupBoxZ)
        self.clipZ.setObjectName(u"clipZ")

        self.gridLayout_3.addWidget(self.clipZ, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.flipClipZ = QPushButton(self.groupBoxZ)
        self.flipClipZ.setObjectName(u"flipClipZ")

        self.gridLayout_3.addWidget(self.flipClipZ, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.groupBoxZ, 2, 0, 1, 1)

        self.groupBoxView = QGroupBox(Gui__Dialog__Clipping)
        self.groupBoxView.setObjectName(u"groupBoxView")
        self.groupBoxView.setCheckable(True)
        self.groupBoxView.setChecked(False)
        self.gridLayout_6 = QGridLayout(self.groupBoxView)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_4 = QLabel(self.groupBoxView)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 0, 1, 1, 1)

        self.clipView = QDoubleSpinBox(self.groupBoxView)
        self.clipView.setObjectName(u"clipView")

        self.gridLayout_6.addWidget(self.clipView, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(84, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.fromView = QPushButton(self.groupBoxView)
        self.fromView.setObjectName(u"fromView")

        self.gridLayout_6.addWidget(self.fromView, 0, 4, 1, 1)

        self.adjustViewdirection = QCheckBox(self.groupBoxView)
        self.adjustViewdirection.setObjectName(u"adjustViewdirection")

        self.gridLayout_6.addWidget(self.adjustViewdirection, 1, 0, 1, 5)

        self.groupBox = QGroupBox(self.groupBoxView)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.dirX = QDoubleSpinBox(self.groupBox)
        self.dirX.setObjectName(u"dirX")

        self.gridLayout_4.addWidget(self.dirX, 0, 0, 1, 1)

        self.dirY = QDoubleSpinBox(self.groupBox)
        self.dirY.setObjectName(u"dirY")

        self.gridLayout_4.addWidget(self.dirY, 0, 1, 1, 1)

        self.dirZ = QDoubleSpinBox(self.groupBox)
        self.dirZ.setObjectName(u"dirZ")

        self.gridLayout_4.addWidget(self.dirZ, 0, 2, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 2, 0, 1, 5)


        self.gridLayout_5.addWidget(self.groupBoxView, 3, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__Clipping)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.gridLayout_5.addWidget(self.buttonBox, 4, 0, 1, 1)

        QWidget.setTabOrder(self.groupBoxX, self.clipX)
        QWidget.setTabOrder(self.clipX, self.flipClipX)
        QWidget.setTabOrder(self.flipClipX, self.groupBoxY)
        QWidget.setTabOrder(self.groupBoxY, self.clipY)
        QWidget.setTabOrder(self.clipY, self.flipClipY)
        QWidget.setTabOrder(self.flipClipY, self.groupBoxZ)
        QWidget.setTabOrder(self.groupBoxZ, self.clipZ)
        QWidget.setTabOrder(self.clipZ, self.flipClipZ)
        QWidget.setTabOrder(self.flipClipZ, self.groupBoxView)
        QWidget.setTabOrder(self.groupBoxView, self.clipView)
        QWidget.setTabOrder(self.clipView, self.fromView)
        QWidget.setTabOrder(self.fromView, self.adjustViewdirection)
        QWidget.setTabOrder(self.adjustViewdirection, self.dirX)
        QWidget.setTabOrder(self.dirX, self.dirY)
        QWidget.setTabOrder(self.dirY, self.dirZ)

        self.retranslateUi(Gui__Dialog__Clipping)
        self.buttonBox.rejected.connect(Gui__Dialog__Clipping.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__Clipping)
    # setupUi

    def retranslateUi(self, Gui__Dialog__Clipping):
        Gui__Dialog__Clipping.setWindowTitle(QCoreApplication.translate("Gui::Dialog::Clipping", u"Clipping", None))
        self.groupBoxX.setTitle(QCoreApplication.translate("Gui::Dialog::Clipping", u"Clipping X", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::Clipping", u"Offset", None))
        self.flipClipX.setText(QCoreApplication.translate("Gui::Dialog::Clipping", u"Flip", None))
        self.groupBoxY.setTitle(QCoreApplication.translate("Gui::Dialog::Clipping", u"Clipping Y", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::Clipping", u"Offset", None))
        self.flipClipY.setText(QCoreApplication.translate("Gui::Dialog::Clipping", u"Flip", None))
        self.groupBoxZ.setTitle(QCoreApplication.translate("Gui::Dialog::Clipping", u"Clipping Z", None))
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::Clipping", u"Offset", None))
        self.flipClipZ.setText(QCoreApplication.translate("Gui::Dialog::Clipping", u"Flip", None))
        self.groupBoxView.setTitle(QCoreApplication.translate("Gui::Dialog::Clipping", u"Custom Clipping Direction", None))
        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::Clipping", u"Offset", None))
        self.fromView.setText(QCoreApplication.translate("Gui::Dialog::Clipping", u"View", None))
        self.adjustViewdirection.setText(QCoreApplication.translate("Gui::Dialog::Clipping", u"Adjust to view direction", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::Clipping", u"Direction", None))
    # retranslateUi

