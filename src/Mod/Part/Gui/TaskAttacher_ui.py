# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskAttacher.ui'
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

class Ui_PartGui_TaskAttacher(object):
    def setupUi(self, PartGui__TaskAttacher):
        if not PartGui__TaskAttacher.objectName():
            PartGui__TaskAttacher.setObjectName(u"PartGui__TaskAttacher")
        PartGui__TaskAttacher.resize(271, 604)
        PartGui__TaskAttacher.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(PartGui__TaskAttacher)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.message = QLabel(PartGui__TaskAttacher)
        self.message.setObjectName(u"message")
        self.message.setAlignment(Qt.AlignCenter)
        self.message.setWordWrap(True)

        self.verticalLayout.addWidget(self.message)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buttonRef1 = QPushButton(PartGui__TaskAttacher)
        self.buttonRef1.setObjectName(u"buttonRef1")
        self.buttonRef1.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.buttonRef1)

        self.lineRef1 = QLineEdit(PartGui__TaskAttacher)
        self.lineRef1.setObjectName(u"lineRef1")

        self.horizontalLayout_3.addWidget(self.lineRef1)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.buttonRef2 = QPushButton(PartGui__TaskAttacher)
        self.buttonRef2.setObjectName(u"buttonRef2")
        self.buttonRef2.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.buttonRef2)

        self.lineRef2 = QLineEdit(PartGui__TaskAttacher)
        self.lineRef2.setObjectName(u"lineRef2")

        self.horizontalLayout_5.addWidget(self.lineRef2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.buttonRef3 = QPushButton(PartGui__TaskAttacher)
        self.buttonRef3.setObjectName(u"buttonRef3")
        self.buttonRef3.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.buttonRef3)

        self.lineRef3 = QLineEdit(PartGui__TaskAttacher)
        self.lineRef3.setObjectName(u"lineRef3")

        self.horizontalLayout_6.addWidget(self.lineRef3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.buttonRef4 = QPushButton(PartGui__TaskAttacher)
        self.buttonRef4.setObjectName(u"buttonRef4")
        self.buttonRef4.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.buttonRef4)

        self.lineRef4 = QLineEdit(PartGui__TaskAttacher)
        self.lineRef4.setObjectName(u"lineRef4")

        self.horizontalLayout_7.addWidget(self.lineRef4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.label = QLabel(PartGui__TaskAttacher)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.listOfModes = QListWidget(PartGui__TaskAttacher)
        self.listOfModes.setObjectName(u"listOfModes")
        self.listOfModes.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout.addWidget(self.listOfModes)

        self.groupBox_AttachmentOffset = QGroupBox(PartGui__TaskAttacher)
        self.groupBox_AttachmentOffset.setObjectName(u"groupBox_AttachmentOffset")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_AttachmentOffset.sizePolicy().hasHeightForWidth())
        self.groupBox_AttachmentOffset.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.groupBox_AttachmentOffset)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelOffsetX = QLabel(self.groupBox_AttachmentOffset)
        self.labelOffsetX.setObjectName(u"labelOffsetX")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelOffsetX.sizePolicy().hasHeightForWidth())
        self.labelOffsetX.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelOffsetX, 1, 0, 1, 1)

        self.attachmentOffsetX = Gui_PrefQuantitySpinBox(self.groupBox_AttachmentOffset)
        self.attachmentOffsetX.setObjectName(u"attachmentOffsetX")
        sizePolicy.setHeightForWidth(self.attachmentOffsetX.sizePolicy().hasHeightForWidth())
        self.attachmentOffsetX.setSizePolicy(sizePolicy)
        self.attachmentOffsetX.setMinimumSize(QSize(0, 5))
        self.attachmentOffsetX.setKeyboardTracking(False)

        self.gridLayout.addWidget(self.attachmentOffsetX, 1, 1, 1, 1)

        self.labelOffsetY = QLabel(self.groupBox_AttachmentOffset)
        self.labelOffsetY.setObjectName(u"labelOffsetY")
        sizePolicy1.setHeightForWidth(self.labelOffsetY.sizePolicy().hasHeightForWidth())
        self.labelOffsetY.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelOffsetY, 2, 0, 1, 1)

        self.attachmentOffsetY = Gui_PrefQuantitySpinBox(self.groupBox_AttachmentOffset)
        self.attachmentOffsetY.setObjectName(u"attachmentOffsetY")
        sizePolicy.setHeightForWidth(self.attachmentOffsetY.sizePolicy().hasHeightForWidth())
        self.attachmentOffsetY.setSizePolicy(sizePolicy)
        self.attachmentOffsetY.setMinimumSize(QSize(0, 5))
        self.attachmentOffsetY.setKeyboardTracking(False)

        self.gridLayout.addWidget(self.attachmentOffsetY, 2, 1, 1, 1)

        self.labelOffsetZ = QLabel(self.groupBox_AttachmentOffset)
        self.labelOffsetZ.setObjectName(u"labelOffsetZ")
        sizePolicy1.setHeightForWidth(self.labelOffsetZ.sizePolicy().hasHeightForWidth())
        self.labelOffsetZ.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelOffsetZ, 3, 0, 1, 1)

        self.attachmentOffsetZ = Gui_PrefQuantitySpinBox(self.groupBox_AttachmentOffset)
        self.attachmentOffsetZ.setObjectName(u"attachmentOffsetZ")
        sizePolicy.setHeightForWidth(self.attachmentOffsetZ.sizePolicy().hasHeightForWidth())
        self.attachmentOffsetZ.setSizePolicy(sizePolicy)
        self.attachmentOffsetZ.setMinimumSize(QSize(0, 5))
        self.attachmentOffsetZ.setKeyboardTracking(False)

        self.gridLayout.addWidget(self.attachmentOffsetZ, 3, 1, 1, 1)

        self.labelRoll = QLabel(self.groupBox_AttachmentOffset)
        self.labelRoll.setObjectName(u"labelRoll")
        sizePolicy1.setHeightForWidth(self.labelRoll.sizePolicy().hasHeightForWidth())
        self.labelRoll.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelRoll, 4, 0, 1, 1)

        self.attachmentOffsetRoll = Gui_QuantitySpinBox(self.groupBox_AttachmentOffset)
        self.attachmentOffsetRoll.setObjectName(u"attachmentOffsetRoll")
        sizePolicy.setHeightForWidth(self.attachmentOffsetRoll.sizePolicy().hasHeightForWidth())
        self.attachmentOffsetRoll.setSizePolicy(sizePolicy)
        self.attachmentOffsetRoll.setKeyboardTracking(False)
        self.attachmentOffsetRoll.setProperty(u"unit", u"deg")
        self.attachmentOffsetRoll.setMinimum(-360.000000000000000)
        self.attachmentOffsetRoll.setMaximum(360.000000000000000)

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
        self.attachmentOffsetPitch.setKeyboardTracking(False)
        self.attachmentOffsetPitch.setProperty(u"unit", u"deg")
        self.attachmentOffsetPitch.setMinimum(-360.000000000000000)
        self.attachmentOffsetPitch.setMaximum(360.000000000000000)

        self.gridLayout.addWidget(self.attachmentOffsetPitch, 5, 1, 1, 1)

        self.labelYaw = QLabel(self.groupBox_AttachmentOffset)
        self.labelYaw.setObjectName(u"labelYaw")
        sizePolicy1.setHeightForWidth(self.labelYaw.sizePolicy().hasHeightForWidth())
        self.labelYaw.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelYaw, 6, 0, 1, 1)

        self.attachmentOffsetYaw = Gui_QuantitySpinBox(self.groupBox_AttachmentOffset)
        self.attachmentOffsetYaw.setObjectName(u"attachmentOffsetYaw")
        sizePolicy.setHeightForWidth(self.attachmentOffsetYaw.sizePolicy().hasHeightForWidth())
        self.attachmentOffsetYaw.setSizePolicy(sizePolicy)
        self.attachmentOffsetYaw.setKeyboardTracking(False)
        self.attachmentOffsetYaw.setProperty(u"unit", u"deg")
        self.attachmentOffsetYaw.setMinimum(-360.000000000000000)
        self.attachmentOffsetYaw.setMaximum(360.000000000000000)

        self.gridLayout.addWidget(self.attachmentOffsetYaw, 6, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_AttachmentOffset)

        self.checkBoxFlip = QCheckBox(PartGui__TaskAttacher)
        self.checkBoxFlip.setObjectName(u"checkBoxFlip")

        self.verticalLayout.addWidget(self.checkBoxFlip)

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

        self.retranslateUi(PartGui__TaskAttacher)

        QMetaObject.connectSlotsByName(PartGui__TaskAttacher)
    # setupUi

    def retranslateUi(self, PartGui__TaskAttacher):
        self.message.setText(QCoreApplication.translate("PartGui::TaskAttacher", u"Selection accepted", None))
        self.buttonRef1.setText(QCoreApplication.translate("PartGui::TaskAttacher", u"Reference 1", None))
        self.buttonRef2.setText(QCoreApplication.translate("PartGui::TaskAttacher", u"Reference 2", None))
        self.buttonRef3.setText(QCoreApplication.translate("PartGui::TaskAttacher", u"Reference 3", None))
        self.buttonRef4.setText(QCoreApplication.translate("PartGui::TaskAttacher", u"Reference 4", None))
        self.label.setText(QCoreApplication.translate("PartGui::TaskAttacher", u"Attachment mode", None))
#if QT_CONFIG(tooltip)
        self.groupBox_AttachmentOffset.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupBox_AttachmentOffset.setTitle(QCoreApplication.translate("PartGui::TaskAttacher", u"Attachment Offset in its Local Coordinate System", None))
        self.labelOffsetX.setText(QCoreApplication.translate("PartGui::TaskAttacher", u"In X-direction", None))
#if QT_CONFIG(tooltip)
        self.attachmentOffsetX.setToolTip(QCoreApplication.translate("PartGui::TaskAttacher", u"The offset is expressed in the local coordinate system\n"
"of the object being attached", None))
#endif // QT_CONFIG(tooltip)
        self.labelOffsetY.setText(QCoreApplication.translate("PartGui::TaskAttacher", u"In Y-direction", None))
#if QT_CONFIG(tooltip)
        self.attachmentOffsetY.setToolTip(QCoreApplication.translate("PartGui::TaskAttacher", u"The offset is expressed in the local coordinate system\n"
"of the object being attached", None))
#endif // QT_CONFIG(tooltip)
        self.labelOffsetZ.setText(QCoreApplication.translate("PartGui::TaskAttacher", u"In Z-direction", None))
#if QT_CONFIG(tooltip)
        self.attachmentOffsetZ.setToolTip(QCoreApplication.translate("PartGui::TaskAttacher", u"The offset is expressed in the local coordinate system\n"
"of the object being attached", None))
#endif // QT_CONFIG(tooltip)
        self.labelRoll.setText(QCoreApplication.translate("PartGui::TaskAttacher", u"Around X-axis", None))
#if QT_CONFIG(tooltip)
        self.attachmentOffsetRoll.setToolTip(QCoreApplication.translate("PartGui::TaskAttacher", u"Rotation around the local X-axis. The offset is expressed in the local coordinate system\n"
"of the object being attached.", None))
#endif // QT_CONFIG(tooltip)
        self.labelPitch.setText(QCoreApplication.translate("PartGui::TaskAttacher", u"Around Y-axis", None))
#if QT_CONFIG(tooltip)
        self.attachmentOffsetPitch.setToolTip(QCoreApplication.translate("PartGui::TaskAttacher", u"Rotation around the local Y-axis. The offset is expressed in the local coordinate system\n"
"of the object being attached.", None))
#endif // QT_CONFIG(tooltip)
        self.labelYaw.setText(QCoreApplication.translate("PartGui::TaskAttacher", u"Around Z-axis", None))
#if QT_CONFIG(tooltip)
        self.attachmentOffsetYaw.setToolTip(QCoreApplication.translate("PartGui::TaskAttacher", u"Rotation around the local Z-axis. The offset is expressed in the local coordinate system\n"
"of the object being attached.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBoxFlip.setToolTip(QCoreApplication.translate("PartGui::TaskAttacher", u"Flip side of attachment and offset", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxFlip.setText(QCoreApplication.translate("PartGui::TaskAttacher", u"Flip sides", None))
        pass
    # retranslateUi

