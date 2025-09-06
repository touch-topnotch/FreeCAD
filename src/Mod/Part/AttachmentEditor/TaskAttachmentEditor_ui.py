# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskAttachmentEditor.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_PartDesignGui_TaskDatumParameters(object):
    def setupUi(self, PartDesignGui__TaskDatumParameters):
        if not PartDesignGui__TaskDatumParameters.objectName():
            PartDesignGui__TaskDatumParameters.setObjectName(u"PartDesignGui__TaskDatumParameters")
        PartDesignGui__TaskDatumParameters.resize(271, 604)
        PartDesignGui__TaskDatumParameters.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(PartDesignGui__TaskDatumParameters)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.message = QLabel(PartDesignGui__TaskDatumParameters)
        self.message.setObjectName(u"message")
        self.message.setAlignment(Qt.AlignCenter)
        self.message.setWordWrap(True)

        self.verticalLayout.addWidget(self.message)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buttonRef1 = QPushButton(PartDesignGui__TaskDatumParameters)
        self.buttonRef1.setObjectName(u"buttonRef1")
        self.buttonRef1.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.buttonRef1)

        self.lineRef1 = QLineEdit(PartDesignGui__TaskDatumParameters)
        self.lineRef1.setObjectName(u"lineRef1")

        self.horizontalLayout_3.addWidget(self.lineRef1)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.buttonRef2 = QPushButton(PartDesignGui__TaskDatumParameters)
        self.buttonRef2.setObjectName(u"buttonRef2")
        self.buttonRef2.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.buttonRef2)

        self.lineRef2 = QLineEdit(PartDesignGui__TaskDatumParameters)
        self.lineRef2.setObjectName(u"lineRef2")

        self.horizontalLayout_5.addWidget(self.lineRef2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.buttonRef3 = QPushButton(PartDesignGui__TaskDatumParameters)
        self.buttonRef3.setObjectName(u"buttonRef3")
        self.buttonRef3.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.buttonRef3)

        self.lineRef3 = QLineEdit(PartDesignGui__TaskDatumParameters)
        self.lineRef3.setObjectName(u"lineRef3")

        self.horizontalLayout_6.addWidget(self.lineRef3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.buttonRef4 = QPushButton(PartDesignGui__TaskDatumParameters)
        self.buttonRef4.setObjectName(u"buttonRef4")
        self.buttonRef4.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.buttonRef4)

        self.lineRef4 = QLineEdit(PartDesignGui__TaskDatumParameters)
        self.lineRef4.setObjectName(u"lineRef4")

        self.horizontalLayout_7.addWidget(self.lineRef4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.label = QLabel(PartDesignGui__TaskDatumParameters)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.listOfModes = QListWidget(PartDesignGui__TaskDatumParameters)
        self.listOfModes.setObjectName(u"listOfModes")
        self.listOfModes.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout.addWidget(self.listOfModes)

        self.groupBox_AttachmentOffset = QGroupBox(PartDesignGui__TaskDatumParameters)
        self.groupBox_AttachmentOffset.setObjectName(u"groupBox_AttachmentOffset")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_AttachmentOffset.sizePolicy().hasHeightForWidth())
        self.groupBox_AttachmentOffset.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.groupBox_AttachmentOffset)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelOffset = QLabel(self.groupBox_AttachmentOffset)
        self.labelOffset.setObjectName(u"labelOffset")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelOffset.sizePolicy().hasHeightForWidth())
        self.labelOffset.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelOffset, 1, 0, 1, 1)

        self.attachmentOffsetX = Gui_QuantitySpinBox(self.groupBox_AttachmentOffset)
        self.attachmentOffsetX.setObjectName(u"attachmentOffsetX")
        sizePolicy.setHeightForWidth(self.attachmentOffsetX.sizePolicy().hasHeightForWidth())
        self.attachmentOffsetX.setSizePolicy(sizePolicy)
        self.attachmentOffsetX.setMinimumSize(QSize(0, 5))

        self.gridLayout.addWidget(self.attachmentOffsetX, 1, 1, 1, 1)

        self.labelOffset2 = QLabel(self.groupBox_AttachmentOffset)
        self.labelOffset2.setObjectName(u"labelOffset2")
        sizePolicy1.setHeightForWidth(self.labelOffset2.sizePolicy().hasHeightForWidth())
        self.labelOffset2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelOffset2, 2, 0, 1, 1)

        self.attachmentOffsetY = Gui_QuantitySpinBox(self.groupBox_AttachmentOffset)
        self.attachmentOffsetY.setObjectName(u"attachmentOffsetY")
        sizePolicy.setHeightForWidth(self.attachmentOffsetY.sizePolicy().hasHeightForWidth())
        self.attachmentOffsetY.setSizePolicy(sizePolicy)
        self.attachmentOffsetY.setMinimumSize(QSize(0, 5))

        self.gridLayout.addWidget(self.attachmentOffsetY, 2, 1, 1, 1)

        self.labelOffset3 = QLabel(self.groupBox_AttachmentOffset)
        self.labelOffset3.setObjectName(u"labelOffset3")
        sizePolicy1.setHeightForWidth(self.labelOffset3.sizePolicy().hasHeightForWidth())
        self.labelOffset3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelOffset3, 3, 0, 1, 1)

        self.attachmentOffsetZ = Gui_QuantitySpinBox(self.groupBox_AttachmentOffset)
        self.attachmentOffsetZ.setObjectName(u"attachmentOffsetZ")
        sizePolicy.setHeightForWidth(self.attachmentOffsetZ.sizePolicy().hasHeightForWidth())
        self.attachmentOffsetZ.setSizePolicy(sizePolicy)
        self.attachmentOffsetZ.setMinimumSize(QSize(0, 5))

        self.gridLayout.addWidget(self.attachmentOffsetZ, 3, 1, 1, 1)

        self.labelYaw = QLabel(self.groupBox_AttachmentOffset)
        self.labelYaw.setObjectName(u"labelYaw")
        sizePolicy1.setHeightForWidth(self.labelYaw.sizePolicy().hasHeightForWidth())
        self.labelYaw.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelYaw, 4, 0, 1, 1)

        self.attachmentOffsetRoll = Gui_QuantitySpinBox(self.groupBox_AttachmentOffset)
        self.attachmentOffsetRoll.setObjectName(u"attachmentOffsetRoll")
        sizePolicy.setHeightForWidth(self.attachmentOffsetRoll.sizePolicy().hasHeightForWidth())
        self.attachmentOffsetRoll.setSizePolicy(sizePolicy)
        self.attachmentOffsetRoll.setMinimumSize(QSize(0, 5))
        self.attachmentOffsetRoll.setProperty(u"unit", u"deg")
        self.attachmentOffsetRoll.setProperty(u"minimum", -360.000000000000000)
        self.attachmentOffsetRoll.setProperty(u"maximum", 360.000000000000000)
        self.attachmentOffsetRoll.setProperty(u"value", 0.000000000000000)

        self.gridLayout.addWidget(self.attachmentOffsetRoll, 4, 1, 1, 1)

        self.labelPitch = QLabel(self.groupBox_AttachmentOffset)
        self.labelPitch.setObjectName(u"labelPitch")
        sizePolicy1.setHeightForWidth(self.labelPitch.sizePolicy().hasHeightForWidth())
        self.labelPitch.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelPitch, 5, 0, 1, 1)

        self.attachmentOffsetPitch = Gui_QuantitySpinBox(self.groupBox_AttachmentOffset)
        self.attachmentOffsetPitch.setObjectName(u"attachmentOffsetPitch")
        sizePolicy.setHeightForWidth(self.attachmentOffsetPitch.sizePolicy().hasHeightForWidth())
        self.attachmentOffsetPitch.setSizePolicy(sizePolicy)
        self.attachmentOffsetPitch.setMinimumSize(QSize(0, 5))
        self.attachmentOffsetPitch.setProperty(u"unit", u"deg")
        self.attachmentOffsetPitch.setProperty(u"minimum", -360.000000000000000)
        self.attachmentOffsetPitch.setProperty(u"maximum", 360.000000000000000)
        self.attachmentOffsetPitch.setProperty(u"value", 0.000000000000000)

        self.gridLayout.addWidget(self.attachmentOffsetPitch, 5, 1, 1, 1)

        self.labelRoll = QLabel(self.groupBox_AttachmentOffset)
        self.labelRoll.setObjectName(u"labelRoll")
        sizePolicy1.setHeightForWidth(self.labelRoll.sizePolicy().hasHeightForWidth())
        self.labelRoll.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelRoll, 6, 0, 1, 1)

        self.attachmentOffsetYaw = Gui_QuantitySpinBox(self.groupBox_AttachmentOffset)
        self.attachmentOffsetYaw.setObjectName(u"attachmentOffsetYaw")
        sizePolicy.setHeightForWidth(self.attachmentOffsetYaw.sizePolicy().hasHeightForWidth())
        self.attachmentOffsetYaw.setSizePolicy(sizePolicy)
        self.attachmentOffsetYaw.setMinimumSize(QSize(0, 5))
        self.attachmentOffsetYaw.setProperty(u"unit", u"deg")
        self.attachmentOffsetYaw.setProperty(u"minimum", -360.000000000000000)
        self.attachmentOffsetYaw.setProperty(u"maximum", 360.000000000000000)
        self.attachmentOffsetYaw.setProperty(u"value", 0.000000000000000)

        self.gridLayout.addWidget(self.attachmentOffsetYaw, 6, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_AttachmentOffset)

        self.checkBoxFlip = QCheckBox(PartDesignGui__TaskDatumParameters)
        self.checkBoxFlip.setObjectName(u"checkBoxFlip")

        self.verticalLayout.addWidget(self.checkBoxFlip)

#if QT_CONFIG(shortcut)
        self.labelOffset.setBuddy(self.labelOffset)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.buttonRef1, self.lineRef1)
        QWidget.setTabOrder(self.lineRef1, self.buttonRef2)
        QWidget.setTabOrder(self.buttonRef2, self.lineRef2)
        QWidget.setTabOrder(self.lineRef2, self.buttonRef3)
        QWidget.setTabOrder(self.buttonRef3, self.lineRef3)
        QWidget.setTabOrder(self.lineRef3, self.buttonRef4)
        QWidget.setTabOrder(self.buttonRef4, self.lineRef4)
        QWidget.setTabOrder(self.lineRef4, self.listOfModes)
        QWidget.setTabOrder(self.listOfModes, self.attachmentOffsetX)
        QWidget.setTabOrder(self.attachmentOffsetX, self.attachmentOffsetY)
        QWidget.setTabOrder(self.attachmentOffsetY, self.attachmentOffsetZ)
        QWidget.setTabOrder(self.attachmentOffsetZ, self.attachmentOffsetRoll)
        QWidget.setTabOrder(self.attachmentOffsetRoll, self.attachmentOffsetPitch)
        QWidget.setTabOrder(self.attachmentOffsetPitch, self.attachmentOffsetYaw)
        QWidget.setTabOrder(self.attachmentOffsetYaw, self.checkBoxFlip)

        self.retranslateUi(PartDesignGui__TaskDatumParameters)

        QMetaObject.connectSlotsByName(PartDesignGui__TaskDatumParameters)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskDatumParameters):
        self.message.setText(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Selection accepted", None))
        self.buttonRef1.setText(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Reference 1", None))
        self.buttonRef2.setText(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Reference 2", None))
        self.buttonRef3.setText(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Reference 3", None))
        self.buttonRef4.setText(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Reference 4", None))
        self.label.setText(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Attachment mode", None))
#if QT_CONFIG(tooltip)
        self.groupBox_AttachmentOffset.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupBox_AttachmentOffset.setTitle(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Attachment Offset in its Local Coordinate System", None))
        self.labelOffset.setText(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"In X-direction", None))
#if QT_CONFIG(tooltip)
        self.attachmentOffsetX.setToolTip(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Note: The placement is expressed in local space of object being attached.", None))
#endif // QT_CONFIG(tooltip)
        self.labelOffset2.setText(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"In Y-direction", None))
#if QT_CONFIG(tooltip)
        self.attachmentOffsetY.setToolTip(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Note: The placement is expressed in local space of object being attached.", None))
#endif // QT_CONFIG(tooltip)
        self.labelOffset3.setText(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"In Z-direction", None))
#if QT_CONFIG(tooltip)
        self.attachmentOffsetZ.setToolTip(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Note: The placement is expressed in local space of object being attached.", None))
#endif // QT_CONFIG(tooltip)
        self.labelYaw.setText(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Around X-axis", None))
#if QT_CONFIG(tooltip)
        self.attachmentOffsetRoll.setToolTip(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Rotation around the X-axis\n"
"Note: The placement is expressed in local space of object being attached.", None))
#endif // QT_CONFIG(tooltip)
        self.labelPitch.setText(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Around Y-axis", None))
#if QT_CONFIG(tooltip)
        self.attachmentOffsetPitch.setToolTip(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Rotation around the Y-axis\n"
"Note: The placement is expressed in local space of object being attached.", None))
#endif // QT_CONFIG(tooltip)
        self.labelRoll.setText(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Around Z-axis", None))
#if QT_CONFIG(tooltip)
        self.attachmentOffsetYaw.setToolTip(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Rotation around the Z-axis\n"
"Note: The placement is expressed in local space of object being attached.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxFlip.setText(QCoreApplication.translate("PartDesignGui::TaskDatumParameters", u"Flip sides", None))
        pass
    # retranslateUi

