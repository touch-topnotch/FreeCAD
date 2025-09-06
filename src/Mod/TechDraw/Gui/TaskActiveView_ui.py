# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskActiveView.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TaskActiveView(object):
    def setupUi(self, TaskActiveView):
        if not TaskActiveView.objectName():
            TaskActiveView.setObjectName(u"TaskActiveView")
        TaskActiveView.resize(375, 191)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TaskActiveView.sizePolicy().hasHeightForWidth())
        TaskActiveView.setSizePolicy(sizePolicy)
        TaskActiveView.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/icons/actions/TechDraw_ActiveView.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        TaskActiveView.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(TaskActiveView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.qsbWidth = Gui_QuantitySpinBox(TaskActiveView)
        self.qsbWidth.setObjectName(u"qsbWidth")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.qsbWidth.sizePolicy().hasHeightForWidth())
        self.qsbWidth.setSizePolicy(sizePolicy1)
        self.qsbWidth.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbWidth.setProperty(u"unit", u"")
        self.qsbWidth.setMinimum(0.000000000000000)
        self.qsbWidth.setValue(100.000000000000000)

        self.gridLayout.addWidget(self.qsbWidth, 1, 2, 1, 1)

        self.ccBgColor = Gui_ColorButton(TaskActiveView)
        self.ccBgColor.setObjectName(u"ccBgColor")
        self.ccBgColor.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.ccBgColor.sizePolicy().hasHeightForWidth())
        self.ccBgColor.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.ccBgColor, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 1, 1, 1)

        self.label_3 = QLabel(TaskActiveView)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.cbUse3d = QCheckBox(TaskActiveView)
        self.cbUse3d.setObjectName(u"cbUse3d")
        self.cbUse3d.setAutoExclusive(True)

        self.gridLayout.addWidget(self.cbUse3d, 5, 0, 1, 1)

        self.qsbHeight = Gui_QuantitySpinBox(TaskActiveView)
        self.qsbHeight.setObjectName(u"qsbHeight")
        sizePolicy1.setHeightForWidth(self.qsbHeight.sizePolicy().hasHeightForWidth())
        self.qsbHeight.setSizePolicy(sizePolicy1)
        self.qsbHeight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbHeight.setProperty(u"unit", u"")
        self.qsbHeight.setMinimum(0.000000000000000)
        self.qsbHeight.setValue(100.000000000000000)

        self.gridLayout.addWidget(self.qsbHeight, 2, 2, 1, 1)

        self.cbbg = QCheckBox(TaskActiveView)
        self.cbbg.setObjectName(u"cbbg")
        self.cbbg.setAutoExclusive(True)

        self.gridLayout.addWidget(self.cbbg, 4, 0, 1, 1)

        self.cbNoBG = QCheckBox(TaskActiveView)
        self.cbNoBG.setObjectName(u"cbNoBG")
        self.cbNoBG.setChecked(True)
        self.cbNoBG.setAutoExclusive(True)

        self.gridLayout.addWidget(self.cbNoBG, 3, 0, 1, 1)

        self.label_2 = QLabel(TaskActiveView)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.cbCrop = QCheckBox(TaskActiveView)
        self.cbCrop.setObjectName(u"cbCrop")

        self.gridLayout.addWidget(self.cbCrop, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(TaskActiveView)
        self.cbbg.toggled.connect(self.ccBgColor.setEnabled)

        QMetaObject.connectSlotsByName(TaskActiveView)
    # setupUi

    def retranslateUi(self, TaskActiveView):
        TaskActiveView.setWindowTitle(QCoreApplication.translate("TaskActiveView", u"Active View", None))
#if QT_CONFIG(tooltip)
        self.qsbWidth.setToolTip(QCoreApplication.translate("TaskActiveView", u"Crops captured image to this width", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ccBgColor.setToolTip(QCoreApplication.translate("TaskActiveView", u"Select a color for solid background", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("TaskActiveView", u"Crop to height", None))
        self.cbUse3d.setText(QCoreApplication.translate("TaskActiveView", u"Use 3D background", None))
#if QT_CONFIG(tooltip)
        self.qsbHeight.setToolTip(QCoreApplication.translate("TaskActiveView", u"Crops captured image to this height", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cbbg.setToolTip(QCoreApplication.translate("TaskActiveView", u"Paint background yes/no", None))
#endif // QT_CONFIG(tooltip)
        self.cbbg.setText(QCoreApplication.translate("TaskActiveView", u"Solid background", None))
        self.cbNoBG.setText(QCoreApplication.translate("TaskActiveView", u"No background", None))
        self.label_2.setText(QCoreApplication.translate("TaskActiveView", u"Crop to width", None))
        self.cbCrop.setText(QCoreApplication.translate("TaskActiveView", u"Crop image", None))
    # retranslateUi

