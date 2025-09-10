# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpProbeEdit.ui'
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
    QGroupBox, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QSpinBox, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(424, 376)
        Form.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.toolController = QComboBox(self.frame_2)
        self.toolController.setObjectName(u"toolController")

        self.gridLayout.addWidget(self.toolController, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.PointCountX = QSpinBox(self.groupBox_2)
        self.PointCountX.setObjectName(u"PointCountX")
        self.PointCountX.setMinimum(3)
        self.PointCountX.setMaximum(1000)

        self.gridLayout_3.addWidget(self.PointCountX, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 3, 1, 1)

        self.PointCountY = QSpinBox(self.groupBox_2)
        self.PointCountY.setObjectName(u"PointCountY")
        self.PointCountY.setMinimum(3)
        self.PointCountY.setMaximum(1000)

        self.gridLayout_3.addWidget(self.PointCountY, 0, 4, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.Xoffset = Gui_InputField(self.groupBox)
        self.Xoffset.setObjectName(u"Xoffset")
        self.Xoffset.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.Xoffset, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.Yoffset = Gui_InputField(self.groupBox)
        self.Yoffset.setObjectName(u"Yoffset")
        self.Yoffset.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.Yoffset, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.OutputFileName = QLineEdit(self.groupBox_3)
        self.OutputFileName.setObjectName(u"OutputFileName")

        self.gridLayout_4.addWidget(self.OutputFileName, 0, 1, 1, 1)

        self.SetOutputFileName = QToolButton(self.groupBox_3)
        self.SetOutputFileName.setObjectName(u"SetOutputFileName")
        self.SetOutputFileName.setText(u"...")

        self.gridLayout_4.addWidget(self.SetOutputFileName, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.label.setText(QCoreApplication.translate("Form", u"Tool Controller", None))
#if QT_CONFIG(tooltip)
        self.toolController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Probe Grid Points", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"X:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Y:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Probe", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"X Offset", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Y Offset", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Output", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"File Name", None))
#if QT_CONFIG(tooltip)
        self.OutputFileName.setToolTip(QCoreApplication.translate("Form", u"Enter the filename where the probe points should be written", None))
#endif // QT_CONFIG(tooltip)
        self.OutputFileName.setText(QCoreApplication.translate("Form", u"ProbePoints.txt", None))
        pass
    # retranslateUi

