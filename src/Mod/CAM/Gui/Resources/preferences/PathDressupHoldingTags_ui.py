# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PathDressupHoldingTags.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QLabel, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(477, 478)
        Form.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.ifWidth = Gui_InputField(self.groupBox)
        self.ifWidth.setObjectName(u"ifWidth")

        self.gridLayout_2.addWidget(self.ifWidth, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.ifHeight = Gui_InputField(self.groupBox)
        self.ifHeight.setObjectName(u"ifHeight")

        self.gridLayout_2.addWidget(self.ifHeight, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.dsbAngle = QDoubleSpinBox(self.groupBox)
        self.dsbAngle.setObjectName(u"dsbAngle")
        self.dsbAngle.setSuffix(u" \u00b0")
        self.dsbAngle.setMinimum(5.000000000000000)
        self.dsbAngle.setMaximum(90.000000000000000)
        self.dsbAngle.setSingleStep(15.000000000000000)
        self.dsbAngle.setValue(45.000000000000000)

        self.gridLayout_2.addWidget(self.dsbAngle, 2, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.ifRadius = Gui_InputField(self.groupBox)
        self.ifRadius.setObjectName(u"ifRadius")

        self.gridLayout_2.addWidget(self.ifRadius, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.sbCount = QSpinBox(self.groupBox_2)
        self.sbCount.setObjectName(u"sbCount")
        self.sbCount.setMinimum(2)
        self.sbCount.setValue(4)

        self.gridLayout.addWidget(self.sbCount, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Tag Parameters", None))
        self.label.setText(QCoreApplication.translate("Form", u"Default width", None))
#if QT_CONFIG(tooltip)
        self.ifWidth.setToolTip(QCoreApplication.translate("Form", u"Set the default width of holding tags.\n"
"\n"
"If the width is set to 0 the dressup will try to guess a reasonable value based on the path itself.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Default height", None))
#if QT_CONFIG(tooltip)
        self.ifHeight.setToolTip(QCoreApplication.translate("Form", u"Default height of holding tags.\n"
"\n"
"If the specified height is 0 the dressup will use half the height of the part. Should the height be bigger than the height of the part the dressup will reduce the height to the height of the part.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Default angle", None))
#if QT_CONFIG(tooltip)
        self.dsbAngle.setToolTip(QCoreApplication.translate("Form", u"Plunge angle for ascent and descent of holding tag", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"Default radius", None))
#if QT_CONFIG(tooltip)
        self.ifRadius.setToolTip(QCoreApplication.translate("Form", u"Radius of the fillet on the tag's top edge.\n"
"\n"
"If the radius is bigger than that which the tag shape itself supports, the resulting shape will be that of a dome.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Tag Generation", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Initial # tags", None))
#if QT_CONFIG(tooltip)
        self.sbCount.setToolTip(QCoreApplication.translate("Form", u"Specify the number of tags generated when a new dressup is created", None))
#endif // QT_CONFIG(tooltip)
        pass
    # retranslateUi

