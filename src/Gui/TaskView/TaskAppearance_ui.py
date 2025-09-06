# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskAppearance.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Gui_TaskView_TaskAppearance(object):
    def setupUi(self, Gui__TaskView__TaskAppearance):
        if not Gui__TaskView__TaskAppearance.objectName():
            Gui__TaskView__TaskAppearance.setObjectName(u"Gui__TaskView__TaskAppearance")
        Gui__TaskView__TaskAppearance.resize(193, 174)
        self.vboxLayout = QVBoxLayout(Gui__TaskView__TaskAppearance)
#ifndef Q_OS_MAC
        self.vboxLayout.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.vboxLayout.setContentsMargins(9, 9, 9, 9)
#endif
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.hboxLayout = QHBoxLayout()
#ifndef Q_OS_MAC
        self.hboxLayout.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
#endif
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.textLabel1 = QLabel(Gui__TaskView__TaskAppearance)
        self.textLabel1.setObjectName(u"textLabel1")

        self.hboxLayout.addWidget(self.textLabel1)

        self.changeMode = QComboBox(Gui__TaskView__TaskAppearance)
        self.changeMode.setObjectName(u"changeMode")

        self.hboxLayout.addWidget(self.changeMode)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.hboxLayout1 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.hboxLayout1.setSpacing(6)
#endif
        self.hboxLayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.textLabel1_3 = QLabel(Gui__TaskView__TaskAppearance)
        self.textLabel1_3.setObjectName(u"textLabel1_3")
        self.textLabel1_3.setEnabled(False)

        self.hboxLayout1.addWidget(self.textLabel1_3)

        self.changePlot = QComboBox(Gui__TaskView__TaskAppearance)
        self.changePlot.setObjectName(u"changePlot")
        self.changePlot.setEnabled(False)

        self.hboxLayout1.addWidget(self.changePlot)


        self.vboxLayout.addLayout(self.hboxLayout1)

        self.hboxLayout2 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.hboxLayout2.setSpacing(6)
#endif
        self.hboxLayout2.setContentsMargins(0, 0, 0, 0)
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.textLabel2 = QLabel(Gui__TaskView__TaskAppearance)
        self.textLabel2.setObjectName(u"textLabel2")

        self.hboxLayout2.addWidget(self.textLabel2)

        self.spacerItem = QSpacerItem(71, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout2.addItem(self.spacerItem)

        self.spinPointSize = QSpinBox(Gui__TaskView__TaskAppearance)
        self.spinPointSize.setObjectName(u"spinPointSize")
        self.spinPointSize.setMaximum(64)
        self.spinPointSize.setMinimum(1)
        self.spinPointSize.setValue(2)

        self.hboxLayout2.addWidget(self.spinPointSize)


        self.vboxLayout.addLayout(self.hboxLayout2)

        self.hboxLayout3 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.hboxLayout3.setSpacing(6)
#endif
        self.hboxLayout3.setContentsMargins(0, 0, 0, 0)
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.textLabel3 = QLabel(Gui__TaskView__TaskAppearance)
        self.textLabel3.setObjectName(u"textLabel3")

        self.hboxLayout3.addWidget(self.textLabel3)

        self.spacerItem1 = QSpacerItem(71, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout3.addItem(self.spacerItem1)

        self.spinLineWidth = QSpinBox(Gui__TaskView__TaskAppearance)
        self.spinLineWidth.setObjectName(u"spinLineWidth")
        self.spinLineWidth.setMaximum(64)
        self.spinLineWidth.setMinimum(1)
        self.spinLineWidth.setValue(2)

        self.hboxLayout3.addWidget(self.spinLineWidth)


        self.vboxLayout.addLayout(self.hboxLayout3)

        self.textLabel1_2 = QLabel(Gui__TaskView__TaskAppearance)
        self.textLabel1_2.setObjectName(u"textLabel1_2")

        self.vboxLayout.addWidget(self.textLabel1_2)

        self.hboxLayout4 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.hboxLayout4.setSpacing(6)
#endif
        self.hboxLayout4.setContentsMargins(0, 0, 0, 0)
        self.hboxLayout4.setObjectName(u"hboxLayout4")
        self.horizontalSlider = QSlider(Gui__TaskView__TaskAppearance)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.hboxLayout4.addWidget(self.horizontalSlider)

        self.spinTransparency = QSpinBox(Gui__TaskView__TaskAppearance)
        self.spinTransparency.setObjectName(u"spinTransparency")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinTransparency.sizePolicy().hasHeightForWidth())
        self.spinTransparency.setSizePolicy(sizePolicy)
        self.spinTransparency.setMaximum(100)
        self.spinTransparency.setSingleStep(5)

        self.hboxLayout4.addWidget(self.spinTransparency)


        self.vboxLayout.addLayout(self.hboxLayout4)


        self.retranslateUi(Gui__TaskView__TaskAppearance)
        self.horizontalSlider.valueChanged.connect(self.spinTransparency.setValue)
        self.spinTransparency.valueChanged.connect(self.horizontalSlider.setValue)

        QMetaObject.connectSlotsByName(Gui__TaskView__TaskAppearance)
    # setupUi

    def retranslateUi(self, Gui__TaskView__TaskAppearance):
        Gui__TaskView__TaskAppearance.setWindowTitle(QCoreApplication.translate("Gui::TaskView::TaskAppearance", u"Appearance", None))
        self.textLabel1.setText(QCoreApplication.translate("Gui::TaskView::TaskAppearance", u"Document window", None))
        self.textLabel1_3.setText(QCoreApplication.translate("Gui::TaskView::TaskAppearance", u"Plot mode", None))
        self.textLabel2.setText(QCoreApplication.translate("Gui::TaskView::TaskAppearance", u"Point size", None))
        self.textLabel3.setText(QCoreApplication.translate("Gui::TaskView::TaskAppearance", u"Line width", None))
        self.textLabel1_2.setText(QCoreApplication.translate("Gui::TaskView::TaskAppearance", u"Transparency", None))
    # retranslateUi

