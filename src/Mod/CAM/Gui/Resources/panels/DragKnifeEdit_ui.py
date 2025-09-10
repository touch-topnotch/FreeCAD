# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DragKnifeEdit.ui'
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

class Ui_TaskPanel(object):
    def setupUi(self, TaskPanel):
        if not TaskPanel.objectName():
            TaskPanel.setObjectName(u"TaskPanel")
        TaskPanel.resize(376, 387)
        self.gridLayout = QGridLayout(TaskPanel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblFilterAngle = QLabel(TaskPanel)
        self.lblFilterAngle.setObjectName(u"lblFilterAngle")

        self.gridLayout.addWidget(self.lblFilterAngle, 0, 0, 1, 1)

        self.filterAngle = Gui_QuantitySpinBox(TaskPanel)
        self.filterAngle.setObjectName(u"filterAngle")
        self.filterAngle.setProperty(u"unit", u"deg")

        self.gridLayout.addWidget(self.filterAngle, 0, 2, 1, 2)

        self.lblOffSetDistance = QLabel(TaskPanel)
        self.lblOffSetDistance.setObjectName(u"lblOffSetDistance")

        self.gridLayout.addWidget(self.lblOffSetDistance, 1, 0, 1, 1)

        self.offsetDistance = Gui_QuantitySpinBox(TaskPanel)
        self.offsetDistance.setObjectName(u"offsetDistance")
        self.offsetDistance.setProperty(u"unit", u"mm")
        self.offsetDistance.setMinimum(0.000000000000000)
        self.offsetDistance.setMaximum(100.000000000000000)
        self.offsetDistance.setValue(2.000000000000000)

        self.gridLayout.addWidget(self.offsetDistance, 1, 2, 1, 2)

        self.lblPivotHeight = QLabel(TaskPanel)
        self.lblPivotHeight.setObjectName(u"lblPivotHeight")

        self.gridLayout.addWidget(self.lblPivotHeight, 2, 0, 1, 1)

        self.pivotHeight = Gui_QuantitySpinBox(TaskPanel)
        self.pivotHeight.setObjectName(u"pivotHeight")
        self.pivotHeight.setProperty(u"unit", u"mm")
        self.pivotHeight.setMinimum(0.000000000000000)
        self.pivotHeight.setMaximum(100.000000000000000)
        self.pivotHeight.setValue(4.000000000000000)

        self.gridLayout.addWidget(self.pivotHeight, 2, 2, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 275, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 1, 1)


        self.retranslateUi(TaskPanel)

        QMetaObject.connectSlotsByName(TaskPanel)
    # setupUi

    def retranslateUi(self, TaskPanel):
        TaskPanel.setWindowTitle(QCoreApplication.translate("TaskPanel", u"Dragknife Dressup", None))
        self.lblFilterAngle.setText(QCoreApplication.translate("TaskPanel", u"Filter Angle", None))
#if QT_CONFIG(tooltip)
        self.filterAngle.setToolTip(QCoreApplication.translate("TaskPanel", u"Angles less than filter angle will not receive corner actions", None))
#endif // QT_CONFIG(tooltip)
        self.lblOffSetDistance.setText(QCoreApplication.translate("TaskPanel", u"Offset Distance", None))
#if QT_CONFIG(tooltip)
        self.offsetDistance.setToolTip(QCoreApplication.translate("TaskPanel", u"Distance the point trails behind the spindle", None))
#endif // QT_CONFIG(tooltip)
        self.lblPivotHeight.setText(QCoreApplication.translate("TaskPanel", u"Pivot Height", None))
#if QT_CONFIG(tooltip)
        self.pivotHeight.setToolTip(QCoreApplication.translate("TaskPanel", u"Height to raise during corner action", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

