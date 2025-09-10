# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskAssemblyCreateJoint.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QToolButton,
    QWidget)

class Ui_TaskAssemblyCreateJoint(object):
    def setupUi(self, TaskAssemblyCreateJoint):
        if not TaskAssemblyCreateJoint.objectName():
            TaskAssemblyCreateJoint.setObjectName(u"TaskAssemblyCreateJoint")
        TaskAssemblyCreateJoint.resize(150, 150)
        self.gridLayout = QGridLayout(TaskAssemblyCreateJoint)
        self.gridLayout.setObjectName(u"gridLayout")
        self.jointType = QComboBox(TaskAssemblyCreateJoint)
        self.jointType.setObjectName(u"jointType")

        self.gridLayout.addWidget(self.jointType, 0, 0, 1, 2)

        self.featureList = QListWidget(TaskAssemblyCreateJoint)
        self.featureList.setObjectName(u"featureList")
        self.featureList.setMaximumSize(QSize(16777215, 75))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.featureList.sizePolicy().hasHeightForWidth())
        self.featureList.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.featureList, 1, 0, 1, 2)

        self.hLayoutDistance = QHBoxLayout()
        self.hLayoutDistance.setObjectName(u"hLayoutDistance")
        self.distanceLabel = QLabel(TaskAssemblyCreateJoint)
        self.distanceLabel.setObjectName(u"distanceLabel")

        self.hLayoutDistance.addWidget(self.distanceLabel)

        self.distanceSpinbox = Gui_QuantitySpinBox(TaskAssemblyCreateJoint)
        self.distanceSpinbox.setObjectName(u"distanceSpinbox")
        sizePolicy.setHeightForWidth(self.distanceSpinbox.sizePolicy().hasHeightForWidth())
        self.distanceSpinbox.setSizePolicy(sizePolicy)
        self.distanceSpinbox.setProperty(u"unit", u"mm")

        self.hLayoutDistance.addWidget(self.distanceSpinbox)


        self.gridLayout.addLayout(self.hLayoutDistance, 2, 0, 1, 2)

        self.hLayoutDistance2 = QHBoxLayout()
        self.hLayoutDistance2.setObjectName(u"hLayoutDistance2")
        self.distanceLabel2 = QLabel(TaskAssemblyCreateJoint)
        self.distanceLabel2.setObjectName(u"distanceLabel2")

        self.hLayoutDistance2.addWidget(self.distanceLabel2)

        self.distanceSpinbox2 = Gui_QuantitySpinBox(TaskAssemblyCreateJoint)
        self.distanceSpinbox2.setObjectName(u"distanceSpinbox2")
        sizePolicy.setHeightForWidth(self.distanceSpinbox2.sizePolicy().hasHeightForWidth())
        self.distanceSpinbox2.setSizePolicy(sizePolicy)
        self.distanceSpinbox2.setProperty(u"unit", u"mm")

        self.hLayoutDistance2.addWidget(self.distanceSpinbox2)


        self.gridLayout.addLayout(self.hLayoutDistance2, 3, 0, 1, 2)

        self.hLayout = QHBoxLayout()
        self.hLayout.setObjectName(u"hLayout")
        self.offsetLabel = QLabel(TaskAssemblyCreateJoint)
        self.offsetLabel.setObjectName(u"offsetLabel")

        self.hLayout.addWidget(self.offsetLabel)

        self.offsetSpinbox = Gui_QuantitySpinBox(TaskAssemblyCreateJoint)
        self.offsetSpinbox.setObjectName(u"offsetSpinbox")
        sizePolicy.setHeightForWidth(self.offsetSpinbox.sizePolicy().hasHeightForWidth())
        self.offsetSpinbox.setSizePolicy(sizePolicy)
        self.offsetSpinbox.setProperty(u"unit", u"mm")

        self.hLayout.addWidget(self.offsetSpinbox)


        self.gridLayout.addLayout(self.hLayout, 4, 0, 1, 2)

        self.hLayoutRotation = QHBoxLayout()
        self.hLayoutRotation.setObjectName(u"hLayoutRotation")
        self.rotationLabel = QLabel(TaskAssemblyCreateJoint)
        self.rotationLabel.setObjectName(u"rotationLabel")

        self.hLayoutRotation.addWidget(self.rotationLabel)

        self.rotationSpinbox = Gui_QuantitySpinBox(TaskAssemblyCreateJoint)
        self.rotationSpinbox.setObjectName(u"rotationSpinbox")
        sizePolicy.setHeightForWidth(self.rotationSpinbox.sizePolicy().hasHeightForWidth())
        self.rotationSpinbox.setSizePolicy(sizePolicy)
        self.rotationSpinbox.setProperty(u"unit", u"deg")

        self.hLayoutRotation.addWidget(self.rotationSpinbox)


        self.gridLayout.addLayout(self.hLayoutRotation, 5, 0, 1, 2)

        self.hLayoutOffset1 = QHBoxLayout()
        self.hLayoutOffset1.setObjectName(u"hLayoutOffset1")
        self.offset1Label = QLabel(TaskAssemblyCreateJoint)
        self.offset1Label.setObjectName(u"offset1Label")

        self.hLayoutOffset1.addWidget(self.offset1Label)

        self.offset1Button = QPushButton(TaskAssemblyCreateJoint)
        self.offset1Button.setObjectName(u"offset1Button")

        self.hLayoutOffset1.addWidget(self.offset1Button)


        self.gridLayout.addLayout(self.hLayoutOffset1, 6, 0, 1, 2)

        self.hLayoutOffset2 = QHBoxLayout()
        self.hLayoutOffset2.setObjectName(u"hLayoutOffset2")
        self.offset2Label = QLabel(TaskAssemblyCreateJoint)
        self.offset2Label.setObjectName(u"offset2Label")

        self.hLayoutOffset2.addWidget(self.offset2Label)

        self.offset2Button = QPushButton(TaskAssemblyCreateJoint)
        self.offset2Button.setObjectName(u"offset2Button")

        self.hLayoutOffset2.addWidget(self.offset2Button)


        self.gridLayout.addLayout(self.hLayoutOffset2, 7, 0, 1, 2)

        self.advancedOffsetCheckbox = QCheckBox(TaskAssemblyCreateJoint)
        self.advancedOffsetCheckbox.setObjectName(u"advancedOffsetCheckbox")
        self.advancedOffsetCheckbox.setChecked(False)

        self.gridLayout.addWidget(self.advancedOffsetCheckbox, 8, 0, 1, 2)

        self.PushButtonReverse = QToolButton(TaskAssemblyCreateJoint)
        self.PushButtonReverse.setObjectName(u"PushButtonReverse")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.PushButtonReverse.sizePolicy().hasHeightForWidth())
        self.PushButtonReverse.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/icons/button_sort.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PushButtonReverse.setIcon(icon)

        self.gridLayout.addWidget(self.PushButtonReverse, 9, 0, 1, 1)

        self.groupBox_limits = QGroupBox(TaskAssemblyCreateJoint)
        self.groupBox_limits.setObjectName(u"groupBox_limits")
        self.gridLayout_limits = QGridLayout(self.groupBox_limits)
        self.gridLayout_limits.setObjectName(u"gridLayout_limits")
        self.limitCheckbox1 = QCheckBox(self.groupBox_limits)
        self.limitCheckbox1.setObjectName(u"limitCheckbox1")
        self.limitCheckbox1.setChecked(False)

        self.gridLayout_limits.addWidget(self.limitCheckbox1, 0, 0, 1, 1)

        self.limitLenMinSpinbox = Gui_QuantitySpinBox(self.groupBox_limits)
        self.limitLenMinSpinbox.setObjectName(u"limitLenMinSpinbox")
        sizePolicy.setHeightForWidth(self.limitLenMinSpinbox.sizePolicy().hasHeightForWidth())
        self.limitLenMinSpinbox.setSizePolicy(sizePolicy)
        self.limitLenMinSpinbox.setProperty(u"unit", u"mm")

        self.gridLayout_limits.addWidget(self.limitLenMinSpinbox, 0, 1, 1, 1)

        self.limitCheckbox2 = QCheckBox(self.groupBox_limits)
        self.limitCheckbox2.setObjectName(u"limitCheckbox2")
        self.limitCheckbox2.setChecked(False)

        self.gridLayout_limits.addWidget(self.limitCheckbox2, 1, 0, 1, 1)

        self.limitLenMaxSpinbox = Gui_QuantitySpinBox(self.groupBox_limits)
        self.limitLenMaxSpinbox.setObjectName(u"limitLenMaxSpinbox")
        sizePolicy.setHeightForWidth(self.limitLenMaxSpinbox.sizePolicy().hasHeightForWidth())
        self.limitLenMaxSpinbox.setSizePolicy(sizePolicy)
        self.limitLenMaxSpinbox.setProperty(u"unit", u"mm")

        self.gridLayout_limits.addWidget(self.limitLenMaxSpinbox, 1, 1, 1, 1)

        self.limitCheckbox3 = QCheckBox(self.groupBox_limits)
        self.limitCheckbox3.setObjectName(u"limitCheckbox3")
        self.limitCheckbox3.setChecked(False)

        self.gridLayout_limits.addWidget(self.limitCheckbox3, 2, 0, 1, 1)

        self.limitRotMinSpinbox = Gui_QuantitySpinBox(self.groupBox_limits)
        self.limitRotMinSpinbox.setObjectName(u"limitRotMinSpinbox")
        sizePolicy.setHeightForWidth(self.limitRotMinSpinbox.sizePolicy().hasHeightForWidth())
        self.limitRotMinSpinbox.setSizePolicy(sizePolicy)
        self.limitRotMinSpinbox.setProperty(u"unit", u"deg")
        self.limitRotMinSpinbox.setMinimum(-180.000000000000000)
        self.limitRotMinSpinbox.setMaximum(180.000000000000000)

        self.gridLayout_limits.addWidget(self.limitRotMinSpinbox, 2, 1, 1, 1)

        self.limitCheckbox4 = QCheckBox(self.groupBox_limits)
        self.limitCheckbox4.setObjectName(u"limitCheckbox4")
        self.limitCheckbox4.setChecked(False)

        self.gridLayout_limits.addWidget(self.limitCheckbox4, 3, 0, 1, 1)

        self.limitRotMaxSpinbox = Gui_QuantitySpinBox(self.groupBox_limits)
        self.limitRotMaxSpinbox.setObjectName(u"limitRotMaxSpinbox")
        sizePolicy.setHeightForWidth(self.limitRotMaxSpinbox.sizePolicy().hasHeightForWidth())
        self.limitRotMaxSpinbox.setSizePolicy(sizePolicy)
        self.limitRotMaxSpinbox.setProperty(u"unit", u"deg")
        self.limitRotMaxSpinbox.setMinimum(-180.000000000000000)
        self.limitRotMaxSpinbox.setMaximum(180.000000000000000)

        self.gridLayout_limits.addWidget(self.limitRotMaxSpinbox, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_limits, 10, 0, 1, 1)

        self.reverseRotCheckbox = QCheckBox(TaskAssemblyCreateJoint)
        self.reverseRotCheckbox.setObjectName(u"reverseRotCheckbox")
        self.reverseRotCheckbox.setChecked(True)

        self.gridLayout.addWidget(self.reverseRotCheckbox, 11, 0, 1, 1)


        self.retranslateUi(TaskAssemblyCreateJoint)

        QMetaObject.connectSlotsByName(TaskAssemblyCreateJoint)
    # setupUi

    def retranslateUi(self, TaskAssemblyCreateJoint):
        TaskAssemblyCreateJoint.setWindowTitle(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Create Joint", None))
        self.distanceLabel.setText(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Distance", None))
        self.distanceLabel2.setText(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Radius 2", None))
        self.offsetLabel.setText(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Offset", None))
        self.rotationLabel.setText(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Rotation", None))
        self.offset1Label.setText(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Offset1", None))
#if QT_CONFIG(tooltip)
        self.offset1Button.setToolTip(QCoreApplication.translate("TaskAssemblyCreateJoint", u"By clicking this button, you can set the attachment offset of the first marker (coordinate system) of the joint.", None))
#endif // QT_CONFIG(tooltip)
        self.offset1Button.setText("")
        self.offset2Label.setText(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Offset2", None))
#if QT_CONFIG(tooltip)
        self.offset2Button.setToolTip(QCoreApplication.translate("TaskAssemblyCreateJoint", u"By clicking this button, you can set the attachment offset of the second marker (coordinate system) of the joint.", None))
#endif // QT_CONFIG(tooltip)
        self.offset2Button.setText("")
        self.advancedOffsetCheckbox.setText(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Show advanced offsets", None))
#if QT_CONFIG(tooltip)
        self.PushButtonReverse.setToolTip(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Reverse the direction of the joint.", None))
#endif // QT_CONFIG(tooltip)
        self.PushButtonReverse.setText(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Reverse", None))
        self.groupBox_limits.setTitle(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Limits", None))
        self.limitCheckbox1.setText(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Min length", None))
        self.limitCheckbox2.setText(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Max length", None))
        self.limitCheckbox3.setText(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Min angle", None))
        self.limitCheckbox4.setText(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Max angle", None))
        self.reverseRotCheckbox.setText(QCoreApplication.translate("TaskAssemblyCreateJoint", u"Reverse rotation", None))
    # retranslateUi

