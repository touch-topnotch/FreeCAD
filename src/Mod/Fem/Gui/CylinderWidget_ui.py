# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CylinderWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_CylinderWidget(object):
    def setupUi(self, CylinderWidget):
        if not CylinderWidget.objectName():
            CylinderWidget.setObjectName(u"CylinderWidget")
        CylinderWidget.resize(244, 358)
        CylinderWidget.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(CylinderWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(CylinderWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.centerX = Gui_PrefQuantitySpinBox(self.groupBox)
        self.centerX.setObjectName(u"centerX")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerX.sizePolicy().hasHeightForWidth())
        self.centerX.setSizePolicy(sizePolicy)
        self.centerX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.centerX.setKeyboardTracking(False)

        self.gridLayout_2.addWidget(self.centerX, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.centerY = Gui_PrefQuantitySpinBox(self.groupBox)
        self.centerY.setObjectName(u"centerY")
        sizePolicy.setHeightForWidth(self.centerY.sizePolicy().hasHeightForWidth())
        self.centerY.setSizePolicy(sizePolicy)
        self.centerY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.centerY.setKeyboardTracking(False)

        self.gridLayout_2.addWidget(self.centerY, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.centerZ = Gui_PrefQuantitySpinBox(self.groupBox)
        self.centerZ.setObjectName(u"centerZ")
        sizePolicy.setHeightForWidth(self.centerZ.sizePolicy().hasHeightForWidth())
        self.centerZ.setSizePolicy(sizePolicy)
        self.centerZ.setMinimumSize(QSize(0, 0))
        self.centerZ.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.centerZ.setKeyboardTracking(False)

        self.gridLayout_2.addWidget(self.centerZ, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(CylinderWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.axisX = Gui_PrefQuantitySpinBox(self.groupBox_2)
        self.axisX.setObjectName(u"axisX")
        sizePolicy.setHeightForWidth(self.axisX.sizePolicy().hasHeightForWidth())
        self.axisX.setSizePolicy(sizePolicy)
        self.axisX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.axisX.setKeyboardTracking(False)

        self.gridLayout_3.addWidget(self.axisX, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.axisY = Gui_PrefQuantitySpinBox(self.groupBox_2)
        self.axisY.setObjectName(u"axisY")
        sizePolicy.setHeightForWidth(self.axisY.sizePolicy().hasHeightForWidth())
        self.axisY.setSizePolicy(sizePolicy)
        self.axisY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.axisY.setKeyboardTracking(False)

        self.gridLayout_3.addWidget(self.axisY, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)

        self.axisZ = Gui_PrefQuantitySpinBox(self.groupBox_2)
        self.axisZ.setObjectName(u"axisZ")
        sizePolicy.setHeightForWidth(self.axisZ.sizePolicy().hasHeightForWidth())
        self.axisZ.setSizePolicy(sizePolicy)
        self.axisZ.setMinimumSize(QSize(0, 0))
        self.axisZ.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.axisZ.setKeyboardTracking(False)

        self.gridLayout_3.addWidget(self.axisZ, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(CylinderWidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label)

        self.radius = Gui_PrefQuantitySpinBox(CylinderWidget)
        self.radius.setObjectName(u"radius")
        sizePolicy.setHeightForWidth(self.radius.sizePolicy().hasHeightForWidth())
        self.radius.setSizePolicy(sizePolicy)
        self.radius.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.radius.setKeyboardTracking(False)

        self.horizontalLayout.addWidget(self.radius)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CylinderWidget)

        QMetaObject.connectSlotsByName(CylinderWidget)
    # setupUi

    def retranslateUi(self, CylinderWidget):
        self.groupBox.setTitle(QCoreApplication.translate("CylinderWidget", u"Center", None))
        self.label_7.setText(QCoreApplication.translate("CylinderWidget", u"x", None))
        self.label_8.setText(QCoreApplication.translate("CylinderWidget", u"y", None))
        self.label_9.setText(QCoreApplication.translate("CylinderWidget", u"z", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("CylinderWidget", u"Axis", None))
        self.label_4.setText(QCoreApplication.translate("CylinderWidget", u"x", None))
        self.label_5.setText(QCoreApplication.translate("CylinderWidget", u"y", None))
        self.label_6.setText(QCoreApplication.translate("CylinderWidget", u"z", None))
        self.label.setText(QCoreApplication.translate("CylinderWidget", u"Radius", None))
        pass
    # retranslateUi

