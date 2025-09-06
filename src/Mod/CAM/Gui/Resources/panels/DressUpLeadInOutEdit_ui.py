# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DressUpLeadInOutEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_CAM_DressupLeadInOut(object):
    def setupUi(self, CAM_DressupLeadInOut):
        if not CAM_DressupLeadInOut.objectName():
            CAM_DressupLeadInOut.setObjectName(u"CAM_DressupLeadInOut")
        CAM_DressupLeadInOut.resize(359, 534)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CAM_DressupLeadInOut.sizePolicy().hasHeightForWidth())
        CAM_DressupLeadInOut.setSizePolicy(sizePolicy)
        CAM_DressupLeadInOut.setWindowTitle(u"LeadInOut")
        self.verticalLayout_3 = QVBoxLayout(CAM_DressupLeadInOut)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.chkLeadIn = QCheckBox(CAM_DressupLeadInOut)
        self.chkLeadIn.setObjectName(u"chkLeadIn")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.chkLeadIn)

        self.label_3 = QLabel(CAM_DressupLeadInOut)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.cboStyleIn = QComboBox(CAM_DressupLeadInOut)
        self.cboStyleIn.setObjectName(u"cboStyleIn")
        self.cboStyleIn.setMinimumSize(QSize(80, 0))
        self.cboStyleIn.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.cboStyleIn)

        self.label_5 = QLabel(CAM_DressupLeadInOut)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.dspLenIn = Gui_InputField(CAM_DressupLeadInOut)
        self.dspLenIn.setObjectName(u"dspLenIn")
        self.dspLenIn.setMinimum(0.100000000000000)
        self.dspLenIn.setProperty(u"unit", u"")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.dspLenIn)

        self.label = QLabel(CAM_DressupLeadInOut)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label)

        self.dspExtendIn = Gui_InputField(CAM_DressupLeadInOut)
        self.dspExtendIn.setObjectName(u"dspExtendIn")
        self.dspExtendIn.setProperty(u"unit", u"")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.dspExtendIn)


        self.verticalLayout_3.addLayout(self.formLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.chkLeadOut = QCheckBox(CAM_DressupLeadInOut)
        self.chkLeadOut.setObjectName(u"chkLeadOut")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.chkLeadOut)

        self.label_4 = QLabel(CAM_DressupLeadInOut)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.cboStyleOut = QComboBox(CAM_DressupLeadInOut)
        self.cboStyleOut.setObjectName(u"cboStyleOut")
        self.cboStyleOut.setMinimumSize(QSize(80, 0))
        self.cboStyleOut.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cboStyleOut)

        self.label_6 = QLabel(CAM_DressupLeadInOut)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.dspLenOut = Gui_InputField(CAM_DressupLeadInOut)
        self.dspLenOut.setObjectName(u"dspLenOut")
        self.dspLenOut.setMinimum(0.100000000000000)
        self.dspLenOut.setProperty(u"unit", u"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dspLenOut)

        self.label_2 = QLabel(CAM_DressupLeadInOut)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.dspExtendOut = Gui_InputField(CAM_DressupLeadInOut)
        self.dspExtendOut.setObjectName(u"dspExtendOut")
        self.dspExtendOut.setProperty(u"unit", u"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dspExtendOut)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.chkRapidPlunge = QCheckBox(CAM_DressupLeadInOut)
        self.chkRapidPlunge.setObjectName(u"chkRapidPlunge")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chkRapidPlunge.sizePolicy().hasHeightForWidth())
        self.chkRapidPlunge.setSizePolicy(sizePolicy1)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.chkRapidPlunge)

        self.chkLayers = QCheckBox(CAM_DressupLeadInOut)
        self.chkLayers.setObjectName(u"chkLayers")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.chkLayers)

        self.chkKeepToolDown = QCheckBox(CAM_DressupLeadInOut)
        self.chkKeepToolDown.setObjectName(u"chkKeepToolDown")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.chkKeepToolDown)


        self.verticalLayout_3.addLayout(self.formLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(CAM_DressupLeadInOut)

        QMetaObject.connectSlotsByName(CAM_DressupLeadInOut)
    # setupUi

    def retranslateUi(self, CAM_DressupLeadInOut):
#if QT_CONFIG(tooltip)
        self.chkLeadIn.setToolTip(QCoreApplication.translate("CAM_DressupLeadInOut", u"Enable lead-in move", None))
#endif // QT_CONFIG(tooltip)
        self.chkLeadIn.setText(QCoreApplication.translate("CAM_DressupLeadInOut", u"Enable lead-in", None))
        self.label_3.setText(QCoreApplication.translate("CAM_DressupLeadInOut", u"Style", None))
        self.label_5.setText(QCoreApplication.translate("CAM_DressupLeadInOut", u"Length/radius", None))
#if QT_CONFIG(tooltip)
        self.dspLenIn.setToolTip(QCoreApplication.translate("CAM_DressupLeadInOut", u"Length or radius of the lead-in", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("CAM_DressupLeadInOut", u"Extend", None))
#if QT_CONFIG(tooltip)
        self.dspExtendIn.setToolTip(QCoreApplication.translate("CAM_DressupLeadInOut", u"Extends the lead-in distance", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.chkLeadOut.setToolTip(QCoreApplication.translate("CAM_DressupLeadInOut", u"Enable lead-out move", None))
#endif // QT_CONFIG(tooltip)
        self.chkLeadOut.setText(QCoreApplication.translate("CAM_DressupLeadInOut", u"Enable lead out", None))
        self.label_4.setText(QCoreApplication.translate("CAM_DressupLeadInOut", u"Style", None))
        self.label_6.setText(QCoreApplication.translate("CAM_DressupLeadInOut", u"Length/radius", None))
#if QT_CONFIG(tooltip)
        self.dspLenOut.setToolTip(QCoreApplication.translate("CAM_DressupLeadInOut", u"Length or radius of the lead-out", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("CAM_DressupLeadInOut", u"Extend", None))
#if QT_CONFIG(tooltip)
        self.dspExtendOut.setToolTip(QCoreApplication.translate("CAM_DressupLeadInOut", u"Extends the lead-out distance", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.chkRapidPlunge.setToolTip(QCoreApplication.translate("CAM_DressupLeadInOut", u"Plunge at rapid speed", None))
#endif // QT_CONFIG(tooltip)
        self.chkRapidPlunge.setText(QCoreApplication.translate("CAM_DressupLeadInOut", u"Rapid plunge", None))
#if QT_CONFIG(tooltip)
        self.chkLayers.setToolTip(QCoreApplication.translate("CAM_DressupLeadInOut", u"Apply lead-in/out on all layers", None))
#endif // QT_CONFIG(tooltip)
        self.chkLayers.setText(QCoreApplication.translate("CAM_DressupLeadInOut", u"Include layers", None))
#if QT_CONFIG(tooltip)
        self.chkKeepToolDown.setToolTip(QCoreApplication.translate("CAM_DressupLeadInOut", u"Keep the tool down in the path", None))
#endif // QT_CONFIG(tooltip)
        self.chkKeepToolDown.setText(QCoreApplication.translate("CAM_DressupLeadInOut", u"Keep tool down", None))
        pass
    # retranslateUi

