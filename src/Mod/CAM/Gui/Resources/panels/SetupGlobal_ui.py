# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SetupGlobal.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 721)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_2 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.tabWidgetPage1)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.setupStartDepthExpr = QLineEdit(self.groupBox)
        self.setupStartDepthExpr.setObjectName(u"setupStartDepthExpr")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.setupStartDepthExpr)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.setupFinalDepthExpr = QLineEdit(self.groupBox)
        self.setupFinalDepthExpr.setObjectName(u"setupFinalDepthExpr")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.setupFinalDepthExpr)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.setupStepDownExpr = QLineEdit(self.groupBox)
        self.setupStepDownExpr.setObjectName(u"setupStepDownExpr")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.setupStepDownExpr)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tabWidgetPage1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 2)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.setupClearanceHeightExpr = QLineEdit(self.groupBox_2)
        self.setupClearanceHeightExpr.setObjectName(u"setupClearanceHeightExpr")

        self.gridLayout.addWidget(self.setupClearanceHeightExpr, 1, 1, 1, 2)

        self.setupClearanceHeightOffs = Gui_QuantitySpinBox(self.groupBox_2)
        self.setupClearanceHeightOffs.setObjectName(u"setupClearanceHeightOffs")

        self.gridLayout.addWidget(self.setupClearanceHeightOffs, 1, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.setupSafeHeightExpr = QLineEdit(self.groupBox_2)
        self.setupSafeHeightExpr.setObjectName(u"setupSafeHeightExpr")

        self.gridLayout.addWidget(self.setupSafeHeightExpr, 3, 1, 1, 2)

        self.setupSafeHeightOffs = Gui_QuantitySpinBox(self.groupBox_2)
        self.setupSafeHeightOffs.setObjectName(u"setupSafeHeightOffs")

        self.gridLayout.addWidget(self.setupSafeHeightOffs, 3, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.verticalLayout_3 = QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_3 = QGroupBox(self.tabWidgetPage2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_2 = QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.setupRapidHorizontal = Gui_QuantitySpinBox(self.groupBox_3)
        self.setupRapidHorizontal.setObjectName(u"setupRapidHorizontal")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setupRapidHorizontal.sizePolicy().hasHeightForWidth())
        self.setupRapidHorizontal.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.setupRapidHorizontal)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.setupRapidVertical = Gui_QuantitySpinBox(self.groupBox_3)
        self.setupRapidVertical.setObjectName(u"setupRapidVertical")
        sizePolicy.setHeightForWidth(self.setupRapidVertical.sizePolicy().hasHeightForWidth())
        self.setupRapidVertical.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.setupRapidVertical)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QWidget()
        self.tabWidgetPage3.setObjectName(u"tabWidgetPage3")
        self.gridLayout_3 = QGridLayout(self.tabWidgetPage3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_4 = QGroupBox(self.tabWidgetPage3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.setupCoolantMode = QComboBox(self.groupBox_4)
        self.setupCoolantMode.setObjectName(u"setupCoolantMode")

        self.gridLayout_2.addWidget(self.setupCoolantMode, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 570, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tabWidgetPage3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Setup Global", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Depths", None))
        self.label.setText(QCoreApplication.translate("Form", u"Start depth", None))
#if QT_CONFIG(tooltip)
        self.setupStartDepthExpr.setToolTip(QCoreApplication.translate("Form", u"Expression set as the StartDepth of a newly created operation.\n"
"\n"
"Default: OpStartDepth", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Final depth", None))
#if QT_CONFIG(tooltip)
        self.setupFinalDepthExpr.setToolTip(QCoreApplication.translate("Form", u"Expression set as the FinalDepth for a newly created operation.\n"
"\n"
"Default: OpFinalDepth", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Step down", None))
#if QT_CONFIG(tooltip)
        self.setupStepDownExpr.setToolTip(QCoreApplication.translate("Form", u"Expression set as the StepDown of a newly created operation.\n"
"\n"
"Default: OpToolDiameter", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Heights", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Expression", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Offset", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Clearance", None))
#if QT_CONFIG(tooltip)
        self.setupClearanceHeightExpr.setToolTip(QCoreApplication.translate("Form", u"Expression set as ClearanceHeight for new operations.\n"
"\n"
"Default: \"OpStockZMax+SetupSheet.ClearanceHeightOffset\"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.setupClearanceHeightOffs.setToolTip(QCoreApplication.translate("Form", u"ClearanceHeightOffset - can be used by expressions to set the default ClearanceHeight for new operations.\n"
"\n"
"Default: 3 mm", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Form", u"Safe", None))
#if QT_CONFIG(tooltip)
        self.setupSafeHeightExpr.setToolTip(QCoreApplication.translate("Form", u"Expression set as SafeHeight for new operations.\n"
"\n"
"Default: \"OpStockZMax+SetupSheet.SafeHeightOffset\"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.setupSafeHeightOffs.setToolTip(QCoreApplication.translate("Form", u"SafeHeightOffset can be for expressions to set the SafeHeight for new operations.\n"
"\n"
"Default: \"5mm\"", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("Form", u"Operation", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Rapid Speeds", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Horizontal", None))
#if QT_CONFIG(tooltip)
        self.setupRapidHorizontal.setToolTip(QCoreApplication.translate("Form", u"Rapid horizontal speed assigned as HorizRapid to new ToolController", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("Form", u"Vertical", None))
#if QT_CONFIG(tooltip)
        self.setupRapidVertical.setToolTip(QCoreApplication.translate("Form", u"Rapid vertical speed assigned to VertRapid of new ToolController.", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("Form", u"Tool Controller", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Coolant Mode", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Coolant mode", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), QCoreApplication.translate("Form", u"Coolant", None))
    # retranslateUi

