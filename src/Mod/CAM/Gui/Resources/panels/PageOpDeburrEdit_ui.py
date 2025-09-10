# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpDeburrEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 450)
        Form.setWindowTitle(u"Form")
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(125, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.toolController = QComboBox(self.frame)
        self.toolController.setObjectName(u"toolController")

        self.gridLayout_2.addWidget(self.toolController, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(125, 0))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.coolantController = QComboBox(self.frame)
        self.coolantController.setObjectName(u"coolantController")

        self.gridLayout_2.addWidget(self.coolantController, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(12, -1, 12, -1)
        self.direction_label = QLabel(Form)
        self.direction_label.setObjectName(u"direction_label")
        sizePolicy1.setHeightForWidth(self.direction_label.sizePolicy().hasHeightForWidth())
        self.direction_label.setSizePolicy(sizePolicy1)
        self.direction_label.setMinimumSize(QSize(125, 0))
        self.direction_label.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.direction_label)

        self.direction = QComboBox(Form)
        self.direction.addItem("")
        self.direction.addItem("")
        self.direction.setObjectName(u"direction")

        self.horizontalLayout_5.addWidget(self.direction)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(125, 0))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 0))
        self.label_3.setText(u"W =")

        self.horizontalLayout.addWidget(self.label_3)

        self.value_W = Gui_InputField(self.widget)
        self.value_W.setObjectName(u"value_W")

        self.horizontalLayout.addWidget(self.value_W)


        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 0))
        self.label_4.setText(u"h = ")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.value_h = Gui_InputField(self.widget)
        self.value_h.setObjectName(u"value_h")

        self.horizontalLayout_2.addWidget(self.value_h)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.joinFrame = QFrame(self.widget)
        self.joinFrame.setObjectName(u"joinFrame")
        self.joinFrame.setFrameShape(QFrame.StyledPanel)
        self.joinFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.joinFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setContentsMargins(0, 6, 0, 3)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.joinFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.joinRound = QToolButton(self.joinFrame)
        self.joinRound.setObjectName(u"joinRound")
        self.joinRound.setCheckable(True)
        self.joinRound.setChecked(True)
        self.joinRound.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.joinRound)

        self.joinMiter = QToolButton(self.joinFrame)
        self.joinMiter.setObjectName(u"joinMiter")
        self.joinMiter.setCheckable(True)
        self.joinMiter.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.joinMiter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.joinFrame, 3, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 154, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 4, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.widget)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.opImage = QLabel(self.widget_2)
        self.opImage.setObjectName(u"opImage")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.opImage.sizePolicy().hasHeightForWidth())
        self.opImage.setSizePolicy(sizePolicy2)
        self.opImage.setMinimumSize(QSize(150, 150))
        self.opImage.setMaximumSize(QSize(150, 150))
        self.opImage.setScaledContents(True)
        self.opImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.opImage)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.widget_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)


        self.retranslateUi(Form)

        self.direction.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.label.setText(QCoreApplication.translate("Form", u"Tool Controller", None))
#if QT_CONFIG(tooltip)
        self.toolController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"Coolant Mode", None))
#if QT_CONFIG(tooltip)
        self.coolantController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation.", None))
#endif // QT_CONFIG(tooltip)
        self.direction_label.setText(QCoreApplication.translate("Form", u"Direction", None))
        self.direction.setItemText(0, QCoreApplication.translate("Form", u"CW", None))
        self.direction.setItemText(1, QCoreApplication.translate("Form", u"CCW", None))

#if QT_CONFIG(tooltip)
        self.direction.setToolTip(QCoreApplication.translate("Form", u"The direction in which the profile is performed, clockwise or counterclockwise.", None))
#endif // QT_CONFIG(tooltip)
        self.direction.setCurrentText(QCoreApplication.translate("Form", u"CW", None))
#if QT_CONFIG(tooltip)
        self.value_W.setToolTip(QCoreApplication.translate("Form", u"Width of chamfer cut.", None))
#endif // QT_CONFIG(tooltip)
        self.value_W.setProperty(u"unit", QCoreApplication.translate("Form", u"mm", None))
#if QT_CONFIG(tooltip)
        self.value_h.setToolTip(QCoreApplication.translate("Form", u"Extra depth of tool immersion.", None))
#endif // QT_CONFIG(tooltip)
        self.value_h.setProperty(u"unit", QCoreApplication.translate("Form", u"mm", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Join:", None))
#if QT_CONFIG(tooltip)
        self.joinRound.setToolTip(QCoreApplication.translate("Form", u"Round joint", None))
#endif // QT_CONFIG(tooltip)
        self.joinRound.setText("")
#if QT_CONFIG(tooltip)
        self.joinMiter.setToolTip(QCoreApplication.translate("Form", u"Miter joint", None))
#endif // QT_CONFIG(tooltip)
        self.joinMiter.setText("")
        self.opImage.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        pass
    # retranslateUi

