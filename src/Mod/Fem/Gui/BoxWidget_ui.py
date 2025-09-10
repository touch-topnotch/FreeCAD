# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BoxWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_BoxWidget(object):
    def setupUi(self, BoxWidget):
        if not BoxWidget.objectName():
            BoxWidget.setObjectName(u"BoxWidget")
        BoxWidget.resize(246, 278)
        BoxWidget.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(BoxWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(BoxWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.xLabel = QLabel(self.groupBox)
        self.xLabel.setObjectName(u"xLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xLabel.sizePolicy().hasHeightForWidth())
        self.xLabel.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.xLabel, 0, 0, 1, 1)

        self.centerX = Gui_PrefQuantitySpinBox(self.groupBox)
        self.centerX.setObjectName(u"centerX")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centerX.sizePolicy().hasHeightForWidth())
        self.centerX.setSizePolicy(sizePolicy1)
        self.centerX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.centerX.setKeyboardTracking(False)

        self.gridLayout_2.addWidget(self.centerX, 0, 1, 1, 1)

        self.yLabel = QLabel(self.groupBox)
        self.yLabel.setObjectName(u"yLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.yLabel.sizePolicy().hasHeightForWidth())
        self.yLabel.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.yLabel, 1, 0, 1, 1)

        self.centerY = Gui_PrefQuantitySpinBox(self.groupBox)
        self.centerY.setObjectName(u"centerY")
        sizePolicy1.setHeightForWidth(self.centerY.sizePolicy().hasHeightForWidth())
        self.centerY.setSizePolicy(sizePolicy1)
        self.centerY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.centerY.setKeyboardTracking(False)

        self.gridLayout_2.addWidget(self.centerY, 1, 1, 1, 1)

        self.zLabel = QLabel(self.groupBox)
        self.zLabel.setObjectName(u"zLabel")

        self.gridLayout_2.addWidget(self.zLabel, 2, 0, 1, 1)

        self.centerZ = Gui_PrefQuantitySpinBox(self.groupBox)
        self.centerZ.setObjectName(u"centerZ")
        sizePolicy1.setHeightForWidth(self.centerZ.sizePolicy().hasHeightForWidth())
        self.centerZ.setSizePolicy(sizePolicy1)
        self.centerZ.setMinimumSize(QSize(0, 0))
        self.centerZ.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.centerZ.setKeyboardTracking(False)

        self.gridLayout_2.addWidget(self.centerZ, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lengthLabel = QLabel(BoxWidget)
        self.lengthLabel.setObjectName(u"lengthLabel")
        sizePolicy.setHeightForWidth(self.lengthLabel.sizePolicy().hasHeightForWidth())
        self.lengthLabel.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lengthLabel, 0, 0, 1, 1)

        self.length = Gui_PrefQuantitySpinBox(BoxWidget)
        self.length.setObjectName(u"length")
        sizePolicy1.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy1)
        self.length.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.length.setKeyboardTracking(False)

        self.gridLayout.addWidget(self.length, 0, 1, 1, 1)

        self.widthLabel = QLabel(BoxWidget)
        self.widthLabel.setObjectName(u"widthLabel")
        sizePolicy2.setHeightForWidth(self.widthLabel.sizePolicy().hasHeightForWidth())
        self.widthLabel.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.widthLabel, 1, 0, 1, 1)

        self.width = Gui_PrefQuantitySpinBox(BoxWidget)
        self.width.setObjectName(u"width")
        sizePolicy1.setHeightForWidth(self.width.sizePolicy().hasHeightForWidth())
        self.width.setSizePolicy(sizePolicy1)
        self.width.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.width.setKeyboardTracking(False)

        self.gridLayout.addWidget(self.width, 1, 1, 1, 1)

        self.heightLabel = QLabel(BoxWidget)
        self.heightLabel.setObjectName(u"heightLabel")
        sizePolicy2.setHeightForWidth(self.heightLabel.sizePolicy().hasHeightForWidth())
        self.heightLabel.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.heightLabel, 2, 0, 1, 1)

        self.height = Gui_PrefQuantitySpinBox(BoxWidget)
        self.height.setObjectName(u"height")
        sizePolicy1.setHeightForWidth(self.height.sizePolicy().hasHeightForWidth())
        self.height.setSizePolicy(sizePolicy1)
        self.height.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.height.setKeyboardTracking(False)

        self.gridLayout.addWidget(self.height, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(BoxWidget)

        QMetaObject.connectSlotsByName(BoxWidget)
    # setupUi

    def retranslateUi(self, BoxWidget):
        self.groupBox.setTitle(QCoreApplication.translate("BoxWidget", u"Center", None))
        self.xLabel.setText(QCoreApplication.translate("BoxWidget", u"x", None))
        self.yLabel.setText(QCoreApplication.translate("BoxWidget", u"y", None))
        self.zLabel.setText(QCoreApplication.translate("BoxWidget", u"z", None))
        self.lengthLabel.setText(QCoreApplication.translate("BoxWidget", u"Length", None))
        self.widthLabel.setText(QCoreApplication.translate("BoxWidget", u"Width", None))
        self.heightLabel.setText(QCoreApplication.translate("BoxWidget", u"Height", None))
        pass
    # retranslateUi

