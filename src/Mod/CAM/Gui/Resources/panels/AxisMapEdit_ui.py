# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AxisMapEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_TaskPanel(object):
    def setupUi(self, TaskPanel):
        if not TaskPanel.objectName():
            TaskPanel.setObjectName(u"TaskPanel")
        TaskPanel.resize(376, 387)
        self.gridLayout = QGridLayout(TaskPanel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblRadius = QLabel(TaskPanel)
        self.lblRadius.setObjectName(u"lblRadius")

        self.gridLayout.addWidget(self.lblRadius, 0, 0, 1, 1)

        self.radius = Gui_QuantitySpinBox(TaskPanel)
        self.radius.setObjectName(u"radius")
        self.radius.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.radius, 0, 2, 1, 2)

        self.lblAxisMapInput = QLabel(TaskPanel)
        self.lblAxisMapInput.setObjectName(u"lblAxisMapInput")

        self.gridLayout.addWidget(self.lblAxisMapInput, 1, 0, 1, 1)

        self.axisMapInput = QComboBox(TaskPanel)
        self.axisMapInput.addItem("")
        self.axisMapInput.addItem("")
        self.axisMapInput.addItem("")
        self.axisMapInput.addItem("")
        self.axisMapInput.addItem("")
        self.axisMapInput.addItem("")
        self.axisMapInput.setObjectName(u"axisMapInput")

        self.gridLayout.addWidget(self.axisMapInput, 1, 2, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 275, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 1, 1)


        self.retranslateUi(TaskPanel)

        self.axisMapInput.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(TaskPanel)
    # setupUi

    def retranslateUi(self, TaskPanel):
        TaskPanel.setWindowTitle(QCoreApplication.translate("TaskPanel", u"AxisMap Dressup", None))
        self.lblRadius.setText(QCoreApplication.translate("TaskPanel", u"Radius", None))
#if QT_CONFIG(tooltip)
        self.radius.setToolTip(QCoreApplication.translate("TaskPanel", u"The radius of the wrapped axis", None))
#endif // QT_CONFIG(tooltip)
        self.lblAxisMapInput.setText(QCoreApplication.translate("TaskPanel", u"Axis mapping", None))
        self.axisMapInput.setItemText(0, QCoreApplication.translate("TaskPanel", u"X->A", None))
        self.axisMapInput.setItemText(1, QCoreApplication.translate("TaskPanel", u"Y->A", None))
        self.axisMapInput.setItemText(2, QCoreApplication.translate("TaskPanel", u"X->B", None))
        self.axisMapInput.setItemText(3, QCoreApplication.translate("TaskPanel", u"Y->B", None))
        self.axisMapInput.setItemText(4, QCoreApplication.translate("TaskPanel", u"X->C", None))
        self.axisMapInput.setItemText(5, QCoreApplication.translate("TaskPanel", u"Y->C", None))

#if QT_CONFIG(tooltip)
        self.axisMapInput.setToolTip(QCoreApplication.translate("TaskPanel", u"The input mapping axis. Coordinates of the first axis will be mapped to the second.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

