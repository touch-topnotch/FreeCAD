# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageDepthsEdit.ui'
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
import Path_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(338, 194)
        Form.setWindowTitle(u"Form")
        icon = QIcon()
        icon.addFile(u":/icons/CAM_Depths.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.startDepthLabel = QLabel(Form)
        self.startDepthLabel.setObjectName(u"startDepthLabel")
        self.startDepthLabel.setMinimumSize(QSize(0, 34))
        self.startDepthLabel.setMaximumSize(QSize(16777215, 34))

        self.gridLayout.addWidget(self.startDepthLabel, 0, 0, 1, 2)

        self.startDepth = Gui_QuantitySpinBox(Form)
        self.startDepth.setObjectName(u"startDepth")
        self.startDepth.setProperty(u"minimum", -999999999.000000000000000)
        self.startDepth.setProperty(u"maximum", 999999999.000000000000000)

        self.gridLayout.addWidget(self.startDepth, 0, 2, 1, 1)

        self.startDepthSet = QToolButton(Form)
        self.startDepthSet.setObjectName(u"startDepthSet")
        self.startDepthSet.setText(u"...")
        icon1 = QIcon()
        icon1.addFile(u":/icons/button_left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.startDepthSet.setIcon(icon1)

        self.gridLayout.addWidget(self.startDepthSet, 0, 3, 1, 1)

        self.finalDepthLabel = QLabel(Form)
        self.finalDepthLabel.setObjectName(u"finalDepthLabel")
        self.finalDepthLabel.setMinimumSize(QSize(0, 34))
        self.finalDepthLabel.setMaximumSize(QSize(16777215, 34))

        self.gridLayout.addWidget(self.finalDepthLabel, 1, 0, 1, 2)

        self.finalDepth = Gui_QuantitySpinBox(Form)
        self.finalDepth.setObjectName(u"finalDepth")
        self.finalDepth.setProperty(u"minimum", -999999999.000000000000000)
        self.finalDepth.setProperty(u"maximum", 999999999.000000000000000)

        self.gridLayout.addWidget(self.finalDepth, 1, 2, 1, 1)

        self.finalDepthSet = QToolButton(Form)
        self.finalDepthSet.setObjectName(u"finalDepthSet")
        self.finalDepthSet.setText(u"...")
        self.finalDepthSet.setIcon(icon1)

        self.gridLayout.addWidget(self.finalDepthSet, 1, 3, 1, 1)

        self.stepDownLabel = QLabel(Form)
        self.stepDownLabel.setObjectName(u"stepDownLabel")
        self.stepDownLabel.setMinimumSize(QSize(0, 34))
        self.stepDownLabel.setMaximumSize(QSize(16777215, 34))

        self.gridLayout.addWidget(self.stepDownLabel, 2, 0, 1, 1)

        self.stepDown = Gui_QuantitySpinBox(Form)
        self.stepDown.setObjectName(u"stepDown")
        self.stepDown.setProperty(u"minimum", -999999999.000000000000000)
        self.stepDown.setProperty(u"maximum", 999999999.000000000000000)

        self.gridLayout.addWidget(self.stepDown, 2, 2, 1, 1)

        self.finishDepthLabel = QLabel(Form)
        self.finishDepthLabel.setObjectName(u"finishDepthLabel")
        self.finishDepthLabel.setMinimumSize(QSize(0, 34))
        self.finishDepthLabel.setMaximumSize(QSize(16777215, 34))

        self.gridLayout.addWidget(self.finishDepthLabel, 3, 0, 1, 2)

        self.finishDepth = Gui_QuantitySpinBox(Form)
        self.finishDepth.setObjectName(u"finishDepth")
        self.finishDepth.setProperty(u"minimum", -999999999.000000000000000)
        self.finishDepth.setProperty(u"maximum", 999999999.000000000000000)

        self.gridLayout.addWidget(self.finishDepth, 3, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 1, 1, 1)

        QWidget.setTabOrder(self.startDepth, self.finalDepth)
        QWidget.setTabOrder(self.finalDepth, self.startDepthSet)
        QWidget.setTabOrder(self.startDepthSet, self.finalDepthSet)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.startDepthLabel.setText(QCoreApplication.translate("Form", u"Start Depth", None))
#if QT_CONFIG(tooltip)
        self.startDepth.setToolTip(QCoreApplication.translate("Form", u"Start Depth of the operation. The highest point in Z-axis the operation needs to process.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.startDepthSet.setToolTip(QCoreApplication.translate("Form", u"Transfer the Z value of the selected feature as the Start Depth for the operation.", None))
#endif // QT_CONFIG(tooltip)
        self.finalDepthLabel.setText(QCoreApplication.translate("Form", u"Final Depth", None))
#if QT_CONFIG(tooltip)
        self.finalDepth.setToolTip(QCoreApplication.translate("Form", u"The depth of the operation which corresponds to the lowest value in Z-axis the operation needs to process.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.finalDepthSet.setToolTip(QCoreApplication.translate("Form", u"Transfer the Z value of the selected feature as the Final Depth for the operation.", None))
#endif // QT_CONFIG(tooltip)
        self.stepDownLabel.setText(QCoreApplication.translate("Form", u"Step Down", None))
#if QT_CONFIG(tooltip)
        self.stepDown.setToolTip(QCoreApplication.translate("Form", u"The depth in Z-axis the operation moves downwards between layers. This value depends on the tool being used, the material to be cut, available cooling and many other factors. Please consult the tool manufacturers data sheets for the proper value.", None))
#endif // QT_CONFIG(tooltip)
        self.finishDepthLabel.setText(QCoreApplication.translate("Form", u"Finish Step Down", None))
#if QT_CONFIG(tooltip)
        self.finishDepth.setToolTip(QCoreApplication.translate("Form", u"Depth of the final cut of the operation. Can be used to produce a cleaner finish.", None))
#endif // QT_CONFIG(tooltip)
        pass
    # retranslateUi

