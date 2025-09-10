# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpVcarveEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QLabel,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(739, 379)
        Form.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
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

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.coolantController = QComboBox(self.frame_2)
        self.coolantController.setObjectName(u"coolantController")

        self.gridLayout.addWidget(self.coolantController, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.discretize = QDoubleSpinBox(Form)
        self.discretize.setObjectName(u"discretize")
        self.discretize.setDecimals(3)
        self.discretize.setMinimum(0.001000000000000)
        self.discretize.setMaximum(1.000000000000000)
        self.discretize.setSingleStep(0.010000000000000)
        self.discretize.setValue(0.010000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.discretize)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.colinearFilter = QSpinBox(Form)
        self.colinearFilter.setObjectName(u"colinearFilter")
        self.colinearFilter.setMaximum(90)
        self.colinearFilter.setValue(10)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.colinearFilter)

        self.finishingPassZOffsetLabel = QLabel(Form)
        self.finishingPassZOffsetLabel.setObjectName(u"finishingPassZOffsetLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.finishingPassZOffsetLabel)

        self.finishingPassZOffset = Gui_QuantitySpinBox(Form)
        self.finishingPassZOffset.setObjectName(u"finishingPassZOffset")
        self.finishingPassZOffset.setProperty(u"unit", u"")
        self.finishingPassZOffset.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.finishingPassZOffset)

        self.finishingPassEnabled = QCheckBox(Form)
        self.finishingPassEnabled.setObjectName(u"finishingPassEnabled")
        self.finishingPassEnabled.setEnabled(True)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.finishingPassEnabled)

        self.optimizeMovementsEnabled = QCheckBox(Form)
        self.optimizeMovementsEnabled.setObjectName(u"optimizeMovementsEnabled")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.optimizeMovementsEnabled)


        self.verticalLayout.addLayout(self.formLayout)

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
        self.label_4.setText(QCoreApplication.translate("Form", u"Coolant Mode", None))
#if QT_CONFIG(tooltip)
        self.coolantController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Discretization Deflection", None))
#if QT_CONFIG(tooltip)
        self.discretize.setToolTip(QCoreApplication.translate("Form", u"This value is used in discretizing arcs into segments. Smaller values will result in larger G-code. Larger values may cause unwanted segments in the medial line path.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Filter Colinear lines", None))
#if QT_CONFIG(tooltip)
        self.colinearFilter.setToolTip(QCoreApplication.translate("Form", u"Sets how aggressively colinear segments are filtered from the Voronoi diagram. Valid values are 0 - 90 degrees (larger numbers filter more). Default = 10", None))
#endif // QT_CONFIG(tooltip)
        self.finishingPassZOffsetLabel.setText(QCoreApplication.translate("Form", u"Finishing pass Z offset", None))
#if QT_CONFIG(tooltip)
        self.finishingPassZOffset.setToolTip(QCoreApplication.translate("Form", u"Endmill offset for the finishing pass run. Use small value like -0.2 mm to help clean \"fuzzy skin\" or other artefacts.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.finishingPassEnabled.setToolTip(QCoreApplication.translate("Form", u"After carving, travel again the path to remove artifacts and imperfections", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.finishingPassEnabled.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.finishingPassEnabled.setText(QCoreApplication.translate("Form", u"Finishing pass", None))
#if QT_CONFIG(tooltip)
        self.optimizeMovementsEnabled.setToolTip(QCoreApplication.translate("Form", u"Optimize path to avoid raising endmill when moving to adjacent edges. May result in sub-millimeter inaccuracies. ", None))
#endif // QT_CONFIG(tooltip)
        self.optimizeMovementsEnabled.setText(QCoreApplication.translate("Form", u"Optimize movements", None))
        pass
    # retranslateUi

