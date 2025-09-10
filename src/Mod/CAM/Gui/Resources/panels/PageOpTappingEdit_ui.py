# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpTappingEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLabel, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(532, 351)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.dwellTimelabel = QLabel(Form)
        self.dwellTimelabel.setObjectName(u"dwellTimelabel")
        self.dwellTimelabel.setEnabled(False)

        self.gridLayout.addWidget(self.dwellTimelabel, 4, 4, 1, 1)

        self.dwellEnabled = QCheckBox(Form)
        self.dwellEnabled.setObjectName(u"dwellEnabled")

        self.gridLayout.addWidget(self.dwellEnabled, 3, 1, 2, 2)

        self.ExtraOffset = QComboBox(Form)
        self.ExtraOffset.addItem("")
        self.ExtraOffset.addItem("")
        self.ExtraOffset.addItem("")
        self.ExtraOffset.setObjectName(u"ExtraOffset")

        self.gridLayout.addWidget(self.ExtraOffset, 5, 6, 1, 1)

        self.dwellTime = Gui_QuantitySpinBox(Form)
        self.dwellTime.setObjectName(u"dwellTime")
        self.dwellTime.setEnabled(False)

        self.gridLayout.addWidget(self.dwellTime, 4, 6, 1, 1)

        self.Offsetlabel = QLabel(Form)
        self.Offsetlabel.setObjectName(u"Offsetlabel")

        self.gridLayout.addWidget(self.Offsetlabel, 5, 4, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 3)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.coolantController = QComboBox(self.frame)
        self.coolantController.setObjectName(u"coolantController")

        self.gridLayout_2.addWidget(self.coolantController, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.toolController = QComboBox(self.frame)
        self.toolController.setObjectName(u"toolController")

        self.gridLayout_2.addWidget(self.toolController, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        QWidget.setTabOrder(self.toolController, self.dwellEnabled)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.dwellTimelabel.setText(QCoreApplication.translate("Form", u"Time", None))
        self.dwellEnabled.setText(QCoreApplication.translate("Form", u"Dwell", None))
        self.ExtraOffset.setItemText(0, QCoreApplication.translate("Form", u"None", None))
        self.ExtraOffset.setItemText(1, QCoreApplication.translate("Form", u"Tap Tip", None))
        self.ExtraOffset.setItemText(2, QCoreApplication.translate("Form", u"2x Tap Tip", None))

        self.Offsetlabel.setText(QCoreApplication.translate("Form", u"Extend Depth", None))
#if QT_CONFIG(tooltip)
        self.coolantController.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The tool and its settings to be used for this operation.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Coolant Mode", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ToolController", None))
#if QT_CONFIG(tooltip)
        self.toolController.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The tool and its settings to be used for this operation.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

