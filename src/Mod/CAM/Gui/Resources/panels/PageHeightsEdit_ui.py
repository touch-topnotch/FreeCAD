# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageHeightsEdit.ui'
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
    QSpacerItem, QWidget)
import Path_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(282, 242)
        Form.setWindowTitle(u"Form")
        icon = QIcon()
        icon.addFile(u":/icons/CAM_Heights.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.safeHeight = Gui_QuantitySpinBox(Form)
        self.safeHeight.setObjectName(u"safeHeight")
        self.safeHeight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.safeHeight.setMinimum(-999999999.000000000000000)
        self.safeHeight.setMaximum(999999999.000000000000000)

        self.gridLayout.addWidget(self.safeHeight, 0, 1, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.clearanceHeight = Gui_QuantitySpinBox(Form)
        self.clearanceHeight.setObjectName(u"clearanceHeight")
        self.clearanceHeight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.clearanceHeight.setMinimum(-999999999.000000000000000)
        self.clearanceHeight.setMaximum(999999999.000000000000000)

        self.gridLayout.addWidget(self.clearanceHeight, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.label_7.setText(QCoreApplication.translate("Form", u"Safe height", None))
#if QT_CONFIG(tooltip)
        self.safeHeight.setToolTip(QCoreApplication.translate("Form", u"The height above which it is safe to move the tool bit with rapid movements. Below this height all lateral and downward movements are performed with feed rate speeds.", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("Form", u"Clearance height", None))
#if QT_CONFIG(tooltip)
        self.clearanceHeight.setToolTip(QCoreApplication.translate("Form", u"The height where lateral movement of the toolbit is not obstructed by any fixtures or the part / stock material itself.", None))
#endif // QT_CONFIG(tooltip)
        pass
    # retranslateUi

