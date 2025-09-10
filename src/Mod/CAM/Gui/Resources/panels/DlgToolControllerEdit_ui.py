# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgToolControllerEdit.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QSpinBox,
    QToolBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(561, 739)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolBox = QToolBox(Dialog)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBoxPage1 = QWidget()
        self.toolBoxPage1.setObjectName(u"toolBoxPage1")
        self.toolBoxPage1.setGeometry(QRect(0, 0, 543, 638))
        self.verticalLayout_2 = QVBoxLayout(self.toolBoxPage1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_4 = QGroupBox(self.toolBoxPage1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tcName = QLineEdit(self.groupBox_4)
        self.tcName.setObjectName(u"tcName")
        self.tcName.setReadOnly(False)

        self.horizontalLayout.addWidget(self.tcName)

        self.tcNumber = QSpinBox(self.groupBox_4)
        self.tcNumber.setObjectName(u"tcNumber")
        self.tcNumber.setMaximum(99999)

        self.horizontalLayout.addWidget(self.tcNumber)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.frame = QFrame(self.toolBoxPage1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizFeed = Gui_QuantitySpinBox(self.frame)
        self.horizFeed.setObjectName(u"horizFeed")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizFeed.sizePolicy().hasHeightForWidth())
        self.horizFeed.setSizePolicy(sizePolicy)
        self.horizFeed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.horizFeed.setMinimum(0.000000000000000)
        self.horizFeed.setMaximum(9999999.000000000000000)
        self.horizFeed.setProperty(u"unit", u"mm/s")

        self.gridLayout.addWidget(self.horizFeed, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.vertFeed = Gui_QuantitySpinBox(self.frame)
        self.vertFeed.setObjectName(u"vertFeed")
        sizePolicy.setHeightForWidth(self.vertFeed.sizePolicy().hasHeightForWidth())
        self.vertFeed.setSizePolicy(sizePolicy)
        self.vertFeed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.vertFeed.setMinimum(0.000000000000000)
        self.vertFeed.setMaximum(9999999.000000000000000)
        self.vertFeed.setProperty(u"unit", u"mm/s")

        self.gridLayout.addWidget(self.vertFeed, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.horizRapid = Gui_QuantitySpinBox(self.frame)
        self.horizRapid.setObjectName(u"horizRapid")
        sizePolicy.setHeightForWidth(self.horizRapid.sizePolicy().hasHeightForWidth())
        self.horizRapid.setSizePolicy(sizePolicy)
        self.horizRapid.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.horizRapid.setMinimum(0.000000000000000)
        self.horizRapid.setMaximum(9999999.000000000000000)
        self.horizRapid.setProperty(u"unit", u"mm/s")

        self.gridLayout.addWidget(self.horizRapid, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.vertRapid = Gui_QuantitySpinBox(self.frame)
        self.vertRapid.setObjectName(u"vertRapid")
        sizePolicy.setHeightForWidth(self.vertRapid.sizePolicy().hasHeightForWidth())
        self.vertRapid.setSizePolicy(sizePolicy)
        self.vertRapid.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.vertRapid.setMinimum(0.000000000000000)
        self.vertRapid.setMaximum(9999999.000000000000000)
        self.vertRapid.setProperty(u"unit", u"mm/s")

        self.gridLayout.addWidget(self.vertRapid, 3, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.groupBox_3 = QGroupBox(self.toolBoxPage1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_2 = QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.spindleDirection = QComboBox(self.groupBox_3)
        self.spindleDirection.addItem("")
        self.spindleDirection.addItem("")
        self.spindleDirection.setObjectName(u"spindleDirection")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spindleDirection)

        self.spindleSpeed = QDoubleSpinBox(self.groupBox_3)
        self.spindleSpeed.setObjectName(u"spindleSpeed")
        self.spindleSpeed.setMinimum(0.000000000000000)
        self.spindleSpeed.setMaximum(100000.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.spindleSpeed)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.toolBoxPage1, u"Controller")
        self.toolBoxPage2 = QWidget()
        self.toolBoxPage2.setObjectName(u"toolBoxPage2")
        self.toolBoxPage2.setGeometry(QRect(0, 0, 543, 638))
        self.verticalLayout_3 = QVBoxLayout(self.toolBoxPage2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolEditor = QWidget(self.toolBoxPage2)
        self.toolEditor.setObjectName(u"toolEditor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolEditor.sizePolicy().hasHeightForWidth())
        self.toolEditor.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.toolEditor)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.toolEditor)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label_14 = QLabel(self.toolBoxPage2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFrameShape(QFrame.WinPanel)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_14)

        self.toolBox.addItem(self.toolBoxPage2, u"Tool")

        self.verticalLayout.addWidget(self.toolBox)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.tcName, self.tcNumber)
        QWidget.setTabOrder(self.tcNumber, self.horizFeed)
        QWidget.setTabOrder(self.horizFeed, self.vertFeed)
        QWidget.setTabOrder(self.vertFeed, self.horizRapid)
        QWidget.setTabOrder(self.horizRapid, self.vertRapid)
        QWidget.setTabOrder(self.vertRapid, self.spindleSpeed)
        QWidget.setTabOrder(self.spindleSpeed, self.spindleDirection)
        QWidget.setTabOrder(self.spindleDirection, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Tool Controller Editor", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Controller Name /  Tool Number", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Horiz. Feed", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Vert. Feed", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Horiz Rapid", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Vert Rapid", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Spindle", None))
        self.spindleDirection.setItemText(0, QCoreApplication.translate("Dialog", u"Forward", None))
        self.spindleDirection.setItemText(1, QCoreApplication.translate("Dialog", u"Reverse", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage1), QCoreApplication.translate("Dialog", u"Controller", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Any modifications only affect this ToolController!", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage2), QCoreApplication.translate("Dialog", u"Tool", None))
    # retranslateUi

