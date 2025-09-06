# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgBlock.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_BlockDefinition(object):
    def setupUi(self, BlockDefinition):
        if not BlockDefinition.objectName():
            BlockDefinition.setObjectName(u"BlockDefinition")
        BlockDefinition.resize(299, 477)
        self.gridLayout = QGridLayout(BlockDefinition)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(BlockDefinition)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout1 = QGridLayout(self.groupBox)
#ifndef Q_OS_MAC
        self.gridLayout1.setSpacing(6)
#endif
        self.gridLayout1.setContentsMargins(6, 6, 6, 6)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout2 = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout2.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)
#endif
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.TextLabel1 = QLabel(self.groupBox)
        self.TextLabel1.setObjectName(u"TextLabel1")

        self.gridLayout2.addWidget(self.TextLabel1, 0, 0, 1, 1)

        self.FirstLimitType = QComboBox(self.groupBox)
        self.FirstLimitType.addItem("")
        self.FirstLimitType.addItem("")
        self.FirstLimitType.addItem("")
        self.FirstLimitType.addItem("")
        self.FirstLimitType.addItem("")
        self.FirstLimitType.setObjectName(u"FirstLimitType")

        self.gridLayout2.addWidget(self.FirstLimitType, 0, 1, 1, 1)

        self.TextLabel2 = QLabel(self.groupBox)
        self.TextLabel2.setObjectName(u"TextLabel2")

        self.gridLayout2.addWidget(self.TextLabel2, 1, 0, 1, 1)

        self.FirstLimitLength = QSpinBox(self.groupBox)
        self.FirstLimitLength.setObjectName(u"FirstLimitLength")
        self.FirstLimitLength.setValue(20)

        self.gridLayout2.addWidget(self.FirstLimitLength, 1, 1, 1, 1)

        self.TextLabel3 = QLabel(self.groupBox)
        self.TextLabel3.setObjectName(u"TextLabel3")

        self.gridLayout2.addWidget(self.TextLabel3, 2, 0, 1, 1)

        self.FirstLimitSelection = QLineEdit(self.groupBox)
        self.FirstLimitSelection.setObjectName(u"FirstLimitSelection")
        self.FirstLimitSelection.setEnabled(False)

        self.gridLayout2.addWidget(self.FirstLimitSelection, 2, 1, 1, 1)


        self.gridLayout1.addLayout(self.gridLayout2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.GroupBox6 = QGroupBox(BlockDefinition)
        self.GroupBox6.setObjectName(u"GroupBox6")
        self.hboxLayout = QHBoxLayout(self.GroupBox6)
#ifndef Q_OS_MAC
        self.hboxLayout.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.hboxLayout.setContentsMargins(9, 9, 9, 9)
#endif
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout1 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.hboxLayout1.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.hboxLayout1.setContentsMargins(0, 0, 0, 0)
#endif
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.TextLabel4 = QLabel(self.GroupBox6)
        self.TextLabel4.setObjectName(u"TextLabel4")

        self.hboxLayout1.addWidget(self.TextLabel4)

        self.ProfileSelection = QLineEdit(self.GroupBox6)
        self.ProfileSelection.setObjectName(u"ProfileSelection")

        self.hboxLayout1.addWidget(self.ProfileSelection)


        self.hboxLayout.addLayout(self.hboxLayout1)


        self.gridLayout.addWidget(self.GroupBox6, 1, 0, 1, 1)

        self.gridLayout3 = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout3.setSpacing(6)
#endif
        self.gridLayout3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.Reverse = QPushButton(BlockDefinition)
        self.Reverse.setObjectName(u"Reverse")

        self.gridLayout3.addWidget(self.Reverse, 0, 0, 1, 1)

        self.BothSides = QCheckBox(BlockDefinition)
        self.BothSides.setObjectName(u"BothSides")

        self.gridLayout3.addWidget(self.BothSides, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout3, 2, 0, 1, 1)

        self.SecondLimit = QGroupBox(BlockDefinition)
        self.SecondLimit.setObjectName(u"SecondLimit")
        self.SecondLimit.setEnabled(False)
        self.gridLayout4 = QGridLayout(self.SecondLimit)
#ifndef Q_OS_MAC
        self.gridLayout4.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.gridLayout4.setContentsMargins(9, 9, 9, 9)
#endif
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.gridLayout5 = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout5.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.gridLayout5.setContentsMargins(0, 0, 0, 0)
#endif
        self.gridLayout5.setObjectName(u"gridLayout5")
        self.TextLabel1_2 = QLabel(self.SecondLimit)
        self.TextLabel1_2.setObjectName(u"TextLabel1_2")

        self.gridLayout5.addWidget(self.TextLabel1_2, 0, 0, 1, 1)

        self.SecondLimitType = QComboBox(self.SecondLimit)
        self.SecondLimitType.addItem("")
        self.SecondLimitType.addItem("")
        self.SecondLimitType.addItem("")
        self.SecondLimitType.addItem("")
        self.SecondLimitType.addItem("")
        self.SecondLimitType.setObjectName(u"SecondLimitType")

        self.gridLayout5.addWidget(self.SecondLimitType, 0, 1, 1, 1)

        self.TextLabel2_2 = QLabel(self.SecondLimit)
        self.TextLabel2_2.setObjectName(u"TextLabel2_2")

        self.gridLayout5.addWidget(self.TextLabel2_2, 1, 0, 1, 1)

        self.SecondLimitLength = QSpinBox(self.SecondLimit)
        self.SecondLimitLength.setObjectName(u"SecondLimitLength")
        self.SecondLimitLength.setValue(20)

        self.gridLayout5.addWidget(self.SecondLimitLength, 1, 1, 1, 1)

        self.TextLabel3_2 = QLabel(self.SecondLimit)
        self.TextLabel3_2.setObjectName(u"TextLabel3_2")

        self.gridLayout5.addWidget(self.TextLabel3_2, 2, 0, 1, 1)

        self.SecondLimitSelection = QLineEdit(self.SecondLimit)
        self.SecondLimitSelection.setObjectName(u"SecondLimitSelection")
        self.SecondLimitSelection.setEnabled(False)

        self.gridLayout5.addWidget(self.SecondLimitSelection, 2, 1, 1, 1)


        self.gridLayout4.addLayout(self.gridLayout5, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.SecondLimit, 3, 0, 1, 1)

        self.Direction = QGroupBox(BlockDefinition)
        self.Direction.setObjectName(u"Direction")
        self.vboxLayout = QVBoxLayout(self.Direction)
#ifndef Q_OS_MAC
        self.vboxLayout.setSpacing(6)
#endif
        self.vboxLayout.setContentsMargins(6, 6, 6, 6)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.DirectionPerpendicular = QCheckBox(self.Direction)
        self.DirectionPerpendicular.setObjectName(u"DirectionPerpendicular")
        self.DirectionPerpendicular.setChecked(True)

        self.vboxLayout.addWidget(self.DirectionPerpendicular)

        self.gridLayout6 = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout6.setSpacing(6)
#endif
        self.gridLayout6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout6.setObjectName(u"gridLayout6")
        self.TextLabel5 = QLabel(self.Direction)
        self.TextLabel5.setObjectName(u"TextLabel5")

        self.gridLayout6.addWidget(self.TextLabel5, 0, 0, 1, 1)

        self.DirectionSelection = QLineEdit(self.Direction)
        self.DirectionSelection.setObjectName(u"DirectionSelection")
        self.DirectionSelection.setEnabled(False)

        self.gridLayout6.addWidget(self.DirectionSelection, 0, 1, 1, 1)


        self.vboxLayout.addLayout(self.gridLayout6)


        self.gridLayout.addWidget(self.Direction, 4, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(BlockDefinition)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)

        QWidget.setTabOrder(self.FirstLimitType, self.FirstLimitLength)
        QWidget.setTabOrder(self.FirstLimitLength, self.FirstLimitSelection)
        QWidget.setTabOrder(self.FirstLimitSelection, self.ProfileSelection)
        QWidget.setTabOrder(self.ProfileSelection, self.Reverse)
        QWidget.setTabOrder(self.Reverse, self.BothSides)
        QWidget.setTabOrder(self.BothSides, self.SecondLimitType)
        QWidget.setTabOrder(self.SecondLimitType, self.SecondLimitLength)
        QWidget.setTabOrder(self.SecondLimitLength, self.SecondLimitSelection)
        QWidget.setTabOrder(self.SecondLimitSelection, self.DirectionPerpendicular)
        QWidget.setTabOrder(self.DirectionPerpendicular, self.DirectionSelection)

        self.retranslateUi(BlockDefinition)
        self.buttonBox.accepted.connect(BlockDefinition.accept)
        self.buttonBox.rejected.connect(BlockDefinition.reject)

        QMetaObject.connectSlotsByName(BlockDefinition)
    # setupUi

    def retranslateUi(self, BlockDefinition):
        BlockDefinition.setWindowTitle(QCoreApplication.translate("BlockDefinition", u"Block Definition", None))
        self.groupBox.setTitle(QCoreApplication.translate("BlockDefinition", u"First Limit", None))
        self.TextLabel1.setText(QCoreApplication.translate("BlockDefinition", u"Type", None))
        self.FirstLimitType.setItemText(0, QCoreApplication.translate("BlockDefinition", u"Dimension", None))
        self.FirstLimitType.setItemText(1, QCoreApplication.translate("BlockDefinition", u"Up to next", None))
        self.FirstLimitType.setItemText(2, QCoreApplication.translate("BlockDefinition", u"Up to last", None))
        self.FirstLimitType.setItemText(3, QCoreApplication.translate("BlockDefinition", u"Up to plane", None))
        self.FirstLimitType.setItemText(4, QCoreApplication.translate("BlockDefinition", u"Up to face", None))

        self.TextLabel2.setText(QCoreApplication.translate("BlockDefinition", u"Length", None))
        self.FirstLimitLength.setSuffix(QCoreApplication.translate("BlockDefinition", u"mm", None))
        self.TextLabel3.setText(QCoreApplication.translate("BlockDefinition", u"Limit", None))
        self.FirstLimitSelection.setText(QCoreApplication.translate("BlockDefinition", u"No selection", None))
        self.GroupBox6.setTitle(QCoreApplication.translate("BlockDefinition", u"Profile", None))
        self.TextLabel4.setText(QCoreApplication.translate("BlockDefinition", u"Selection", None))
        self.ProfileSelection.setText(QCoreApplication.translate("BlockDefinition", u"No selection", None))
        self.Reverse.setText(QCoreApplication.translate("BlockDefinition", u"Reverse", None))
        self.BothSides.setText(QCoreApplication.translate("BlockDefinition", u"Both sides", None))
        self.SecondLimit.setTitle(QCoreApplication.translate("BlockDefinition", u"Second Limit", None))
        self.TextLabel1_2.setText(QCoreApplication.translate("BlockDefinition", u"Type", None))
        self.SecondLimitType.setItemText(0, QCoreApplication.translate("BlockDefinition", u"Dimension", None))
        self.SecondLimitType.setItemText(1, QCoreApplication.translate("BlockDefinition", u"Up to next", None))
        self.SecondLimitType.setItemText(2, QCoreApplication.translate("BlockDefinition", u"Up to last", None))
        self.SecondLimitType.setItemText(3, QCoreApplication.translate("BlockDefinition", u"Up to plane", None))
        self.SecondLimitType.setItemText(4, QCoreApplication.translate("BlockDefinition", u"Up to face", None))

        self.TextLabel2_2.setText(QCoreApplication.translate("BlockDefinition", u"Length", None))
        self.SecondLimitLength.setSuffix(QCoreApplication.translate("BlockDefinition", u"mm", None))
        self.TextLabel3_2.setText(QCoreApplication.translate("BlockDefinition", u"Limit", None))
        self.SecondLimitSelection.setText(QCoreApplication.translate("BlockDefinition", u"No selection", None))
        self.Direction.setTitle(QCoreApplication.translate("BlockDefinition", u"Direction", None))
        self.DirectionPerpendicular.setText(QCoreApplication.translate("BlockDefinition", u"Perpendicular to sketch", None))
        self.TextLabel5.setText(QCoreApplication.translate("BlockDefinition", u"Reference", None))
        self.DirectionSelection.setText(QCoreApplication.translate("BlockDefinition", u"No selection", None))
    # retranslateUi

