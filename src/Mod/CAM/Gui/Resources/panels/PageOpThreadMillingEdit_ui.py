# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpThreadMillingEdit.ui'
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
    QFrame, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(318, 756)
        Form.setWindowTitle(u"Form")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout1 = QGridLayout(self.frame)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout1.addWidget(self.label, 0, 0, 1, 1)

        self.toolController = QComboBox(self.frame)
        self.toolController.setObjectName(u"toolController")

        self.gridLayout1.addWidget(self.toolController, 0, 1, 1, 1)

        self.editToolController = QCheckBox(self.frame)
        self.editToolController.setObjectName(u"editToolController")

        self.gridLayout1.addWidget(self.editToolController, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_2 = QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.threadOrientation = QComboBox(self.groupBox)
        self.threadOrientation.setObjectName(u"threadOrientation")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.threadOrientation)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.threadType = QComboBox(self.groupBox)
        self.threadType.setObjectName(u"threadType")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.threadType)

        self.threadName = QComboBox(self.groupBox)
        self.threadName.setObjectName(u"threadName")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.threadName)

        self.threadFitLabel = QLabel(self.groupBox)
        self.threadFitLabel.setObjectName(u"threadFitLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.threadFitLabel)

        self.threadFit = QSlider(self.groupBox)
        self.threadFit.setObjectName(u"threadFit")
        self.threadFit.setMaximum(100)
        self.threadFit.setValue(50)
        self.threadFit.setOrientation(Qt.Horizontal)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.threadFit)

        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label1)

        self.threadMajor = Gui_QuantitySpinBox(self.groupBox)
        self.threadMajor.setObjectName(u"threadMajor")
        self.threadMajor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.threadMajor)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_2)

        self.threadMinor = Gui_QuantitySpinBox(self.groupBox)
        self.threadMinor.setObjectName(u"threadMinor")
        self.threadMinor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.threadMinor)

        self.threadPitchLabel = QLabel(self.groupBox)
        self.threadPitchLabel.setObjectName(u"threadPitchLabel")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.threadPitchLabel)

        self.threadPitch = Gui_QuantitySpinBox(self.groupBox)
        self.threadPitch.setObjectName(u"threadPitch")
        self.threadPitch.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.threadPitch)

        self.threadTPI = QSpinBox(self.groupBox)
        self.threadTPI.setObjectName(u"threadTPI")
        self.threadTPI.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.threadTPI)

        self.threadTPILabel = QLabel(self.groupBox)
        self.threadTPILabel.setObjectName(u"threadTPILabel")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.threadTPILabel)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.opPasses = QSpinBox(self.groupBox_3)
        self.opPasses.setObjectName(u"opPasses")
        self.opPasses.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.opPasses.setMinimum(1)

        self.gridLayout_2.addWidget(self.opPasses, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.opDirection = QComboBox(self.groupBox_3)
        self.opDirection.setObjectName(u"opDirection")

        self.gridLayout_2.addWidget(self.opDirection, 1, 1, 1, 1)

        self.leadInOut = QCheckBox(self.groupBox_3)
        self.leadInOut.setObjectName(u"leadInOut")

        self.gridLayout_2.addWidget(self.leadInOut, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.retranslateUi(Form)

        self.threadOrientation.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.label.setText(QCoreApplication.translate("Form", u"Tool Controller", None))
#if QT_CONFIG(tooltip)
        self.toolController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation.", None))
#endif // QT_CONFIG(tooltip)
        self.editToolController.setText(QCoreApplication.translate("Form", u"Edit Tool Controller", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Thread", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Orientation", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Type", None))
        self.threadFitLabel.setText(QCoreApplication.translate("Form", u"Fit", None))
        self.label1.setText(QCoreApplication.translate("Form", u"Major diameter", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Minor diameter", None))
        self.threadPitchLabel.setText(QCoreApplication.translate("Form", u"Pitch", None))
        self.threadTPILabel.setText(QCoreApplication.translate("Form", u"TPI", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Operation", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Passes", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Direction", None))
        self.leadInOut.setText(QCoreApplication.translate("Form", u"Lead in/out", None))
        pass
    # retranslateUi

