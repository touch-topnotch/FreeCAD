# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageDiametersEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QToolButton, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(345, 235)
        Form.setWindowTitle(u"Form")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.startDepthLabel = QLabel(Form)
        self.startDepthLabel.setObjectName(u"startDepthLabel")

        self.gridLayout.addWidget(self.startDepthLabel, 0, 0, 1, 1)

        self.minDiameter = Gui_QuantitySpinBox(Form)
        self.minDiameter.setObjectName(u"minDiameter")
        self.minDiameter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.minDiameter.setMinimum(-999999999.000000000000000)
        self.minDiameter.setMaximum(999999999.000000000000000)

        self.gridLayout.addWidget(self.minDiameter, 0, 1, 1, 1)

        self.startDepthSet = QToolButton(Form)
        self.startDepthSet.setObjectName(u"startDepthSet")
        self.startDepthSet.setText(u"\u2026")
        icon = QIcon()
        icon.addFile(u":/icons/button_left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.startDepthSet.setIcon(icon)

        self.gridLayout.addWidget(self.startDepthSet, 0, 2, 1, 1)

        self.finalDepthLabel = QLabel(Form)
        self.finalDepthLabel.setObjectName(u"finalDepthLabel")

        self.gridLayout.addWidget(self.finalDepthLabel, 1, 0, 1, 1)

        self.maxDiameter = Gui_QuantitySpinBox(Form)
        self.maxDiameter.setObjectName(u"maxDiameter")
        self.maxDiameter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.maxDiameter.setMinimum(-999999999.000000000000000)
        self.maxDiameter.setMaximum(999999999.000000000000000)

        self.gridLayout.addWidget(self.maxDiameter, 1, 1, 1, 1)

        self.finalDepthSet = QToolButton(Form)
        self.finalDepthSet.setObjectName(u"finalDepthSet")
        self.finalDepthSet.setText(u"\u2026")
        self.finalDepthSet.setIcon(icon)

        self.gridLayout.addWidget(self.finalDepthSet, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 3)

        QWidget.setTabOrder(self.minDiameter, self.maxDiameter)
        QWidget.setTabOrder(self.maxDiameter, self.startDepthSet)
        QWidget.setTabOrder(self.startDepthSet, self.finalDepthSet)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.startDepthLabel.setText(QCoreApplication.translate("Form", u"Min Diameter", None))
#if QT_CONFIG(tooltip)
        self.minDiameter.setToolTip(QCoreApplication.translate("Form", u"Start depth of the operation. The highest point in Z-axis the operation needs to process.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.startDepthSet.setToolTip(QCoreApplication.translate("Form", u"Transfer the Z value of the selected feature as the start depth for the operation", None))
#endif // QT_CONFIG(tooltip)
        self.finalDepthLabel.setText(QCoreApplication.translate("Form", u"Max diameter", None))
#if QT_CONFIG(tooltip)
        self.maxDiameter.setToolTip(QCoreApplication.translate("Form", u"The depth of the operation which corresponds to the lowest value in Z-axis the operation needs to process.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.finalDepthSet.setToolTip(QCoreApplication.translate("Form", u"Transfer the Z value of the selected feature as the final depth for the operation.", None))
#endif // QT_CONFIG(tooltip)
        pass
    # retranslateUi

