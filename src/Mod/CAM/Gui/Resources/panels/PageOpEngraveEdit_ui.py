# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpEngraveEdit.ui'
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
    QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 258)
        Form.setWindowTitle(u"Form")
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.toolController = QComboBox(self.frame_2)
        self.toolController.setObjectName(u"toolController")

        self.gridLayout.addWidget(self.toolController, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.coolantController = QComboBox(self.frame_2)
        self.coolantController.setObjectName(u"coolantController")

        self.gridLayout.addWidget(self.coolantController, 1, 1, 1, 1)

        self.editToolController = QCheckBox(self.frame_2)
        self.editToolController.setObjectName(u"editToolController")

        self.gridLayout.addWidget(self.editToolController, 2, 0, 1, 2)


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.startVertex = QSpinBox(self.widget)
        self.startVertex.setObjectName(u"startVertex")
        self.startVertex.setMaximum(999999)

        self.gridLayout_2.addWidget(self.startVertex, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.label.setText(QCoreApplication.translate("Form", u"Tool controller", None))
#if QT_CONFIG(tooltip)
        self.toolController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Coolant mode", None))
#if QT_CONFIG(tooltip)
        self.coolantController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation", None))
#endif // QT_CONFIG(tooltip)
        self.editToolController.setText(QCoreApplication.translate("Form", u"Edit Tool Controller", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Start at vertex", None))
#if QT_CONFIG(tooltip)
        self.startVertex.setToolTip(QCoreApplication.translate("Form", u"Specify the vertex number of the underlying shape string at which engraving should start", None))
#endif // QT_CONFIG(tooltip)
        pass
    # retranslateUi

