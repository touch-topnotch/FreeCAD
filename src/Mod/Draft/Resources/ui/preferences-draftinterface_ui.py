# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-draftinterface.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsDraft(object):
    def setupUi(self, Gui__Dialog__DlgSettingsDraft):
        if not Gui__Dialog__DlgSettingsDraft.objectName():
            Gui__Dialog__DlgSettingsDraft.setObjectName(u"Gui__Dialog__DlgSettingsDraft")
        Gui__Dialog__DlgSettingsDraft.resize(513, 516)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsDraft)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(11, 11, 11, 11)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.groupBox_1 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.gridLayout_1 = QGridLayout(self.groupBox_1)
        self.gridLayout_1.setSpacing(6)
        self.gridLayout_1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.label_inCommandShortcutRelative = QLabel(self.groupBox_1)
        self.label_inCommandShortcutRelative.setObjectName(u"label_inCommandShortcutRelative")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutRelative, 0, 0, 1, 1)

        self.lineEdit_inCommandShortcutRelative = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutRelative.setObjectName(u"lineEdit_inCommandShortcutRelative")
        self.lineEdit_inCommandShortcutRelative.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutRelative.setMaxLength(1)
        self.lineEdit_inCommandShortcutRelative.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutRelative.setProperty(u"prefEntry", u"inCommandShortcutRelative")
        self.lineEdit_inCommandShortcutRelative.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutRelative, 0, 1, 1, 1)

        self.horizontalSpacer_1 = QSpacerItem(25, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_1.addItem(self.horizontalSpacer_1, 0, 2, 1, 1)

        self.label_inCommandShortcutGlobal = QLabel(self.groupBox_1)
        self.label_inCommandShortcutGlobal.setObjectName(u"label_inCommandShortcutGlobal")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutGlobal, 0, 3, 1, 1)

        self.lineEdit_inCommandShortcutGlobal = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutGlobal.setObjectName(u"lineEdit_inCommandShortcutGlobal")
        self.lineEdit_inCommandShortcutGlobal.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutGlobal.setMaxLength(1)
        self.lineEdit_inCommandShortcutGlobal.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutGlobal.setProperty(u"prefEntry", u"inCommandShortcutGlobal")
        self.lineEdit_inCommandShortcutGlobal.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutGlobal, 0, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(25, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_1.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.label_inCommandShortcutLength = QLabel(self.groupBox_1)
        self.label_inCommandShortcutLength.setObjectName(u"label_inCommandShortcutLength")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutLength, 0, 6, 1, 1)

        self.lineEdit_inCommandShortcutLength = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutLength.setObjectName(u"lineEdit_inCommandShortcutLength")
        self.lineEdit_inCommandShortcutLength.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutLength.setMaxLength(1)
        self.lineEdit_inCommandShortcutLength.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutLength.setProperty(u"prefEntry", u"inCommandShortcutLength")
        self.lineEdit_inCommandShortcutLength.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutLength, 0, 7, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_1.addItem(self.horizontalSpacer_3, 0, 8, 1, 1)

        self.label_inCommandShortcutMakeFace = QLabel(self.groupBox_1)
        self.label_inCommandShortcutMakeFace.setObjectName(u"label_inCommandShortcutMakeFace")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutMakeFace, 1, 0, 1, 1)

        self.lineEdit_inCommandShortcutMakeFace = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutMakeFace.setObjectName(u"lineEdit_inCommandShortcutMakeFace")
        self.lineEdit_inCommandShortcutMakeFace.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutMakeFace.setMaxLength(1)
        self.lineEdit_inCommandShortcutMakeFace.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutMakeFace.setProperty(u"prefEntry", u"inCommandShortcutMakeFace")
        self.lineEdit_inCommandShortcutMakeFace.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutMakeFace, 1, 1, 1, 1)

        self.label_inCommandShortcutSelectEdge = QLabel(self.groupBox_1)
        self.label_inCommandShortcutSelectEdge.setObjectName(u"label_inCommandShortcutSelectEdge")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutSelectEdge, 1, 3, 1, 1)

        self.lineEdit_inCommandShortcutSelectEdge = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutSelectEdge.setObjectName(u"lineEdit_inCommandShortcutSelectEdge")
        self.lineEdit_inCommandShortcutSelectEdge.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutSelectEdge.setMaxLength(1)
        self.lineEdit_inCommandShortcutSelectEdge.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutSelectEdge.setProperty(u"prefEntry", u"inCommandShortcutSelectEdge")
        self.lineEdit_inCommandShortcutSelectEdge.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutSelectEdge, 1, 4, 1, 1)

        self.label_inCommandShortcutSubelementMode = QLabel(self.groupBox_1)
        self.label_inCommandShortcutSubelementMode.setObjectName(u"label_inCommandShortcutSubelementMode")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutSubelementMode, 1, 6, 1, 1)

        self.lineEdit_inCommandShortcutSubelementMode = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutSubelementMode.setObjectName(u"lineEdit_inCommandShortcutSubelementMode")
        self.lineEdit_inCommandShortcutSubelementMode.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutSubelementMode.setMaxLength(1)
        self.lineEdit_inCommandShortcutSubelementMode.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutSubelementMode.setProperty(u"prefEntry", u"inCommandShortcutSubelementMode")
        self.lineEdit_inCommandShortcutSubelementMode.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutSubelementMode, 1, 7, 1, 1)

        self.label_inCommandShortcutCopy = QLabel(self.groupBox_1)
        self.label_inCommandShortcutCopy.setObjectName(u"label_inCommandShortcutCopy")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutCopy, 2, 0, 1, 1)

        self.lineEdit_inCommandShortcutCopy = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutCopy.setObjectName(u"lineEdit_inCommandShortcutCopy")
        self.lineEdit_inCommandShortcutCopy.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutCopy.setMaxLength(1)
        self.lineEdit_inCommandShortcutCopy.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutCopy.setProperty(u"prefEntry", u"inCommandShortcutCopy")
        self.lineEdit_inCommandShortcutCopy.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutCopy, 2, 1, 1, 1)

        self.label_inCommandShortcutUndo = QLabel(self.groupBox_1)
        self.label_inCommandShortcutUndo.setObjectName(u"label_inCommandShortcutUndo")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutUndo, 2, 3, 1, 1)

        self.lineEdit_inCommandShortcutUndo = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutUndo.setObjectName(u"lineEdit_inCommandShortcutUndo")
        self.lineEdit_inCommandShortcutUndo.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutUndo.setText(u"/")
        self.lineEdit_inCommandShortcutUndo.setMaxLength(1)
        self.lineEdit_inCommandShortcutUndo.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutUndo.setProperty(u"prefEntry", u"inCommandShortcutUndo")
        self.lineEdit_inCommandShortcutUndo.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutUndo, 2, 4, 1, 1)

        self.label_inCommandShortcutWipe = QLabel(self.groupBox_1)
        self.label_inCommandShortcutWipe.setObjectName(u"label_inCommandShortcutWipe")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutWipe, 2, 6, 1, 1)

        self.lineEdit_inCommandShortcutWipe = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutWipe.setObjectName(u"lineEdit_inCommandShortcutWipe")
        self.lineEdit_inCommandShortcutWipe.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutWipe.setMaxLength(1)
        self.lineEdit_inCommandShortcutWipe.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutWipe.setProperty(u"prefEntry", u"inCommandShortcutWipe")
        self.lineEdit_inCommandShortcutWipe.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutWipe, 2, 7, 1, 1)

        self.label_inCommandShortcutClose = QLabel(self.groupBox_1)
        self.label_inCommandShortcutClose.setObjectName(u"label_inCommandShortcutClose")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutClose, 3, 0, 1, 1)

        self.lineEdit_inCommandShortcutClose = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutClose.setObjectName(u"lineEdit_inCommandShortcutClose")
        self.lineEdit_inCommandShortcutClose.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutClose.setMaxLength(1)
        self.lineEdit_inCommandShortcutClose.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutClose.setProperty(u"prefEntry", u"inCommandShortcutClose")
        self.lineEdit_inCommandShortcutClose.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutClose, 3, 1, 1, 1)

        self.label_inCommandShortcutExit = QLabel(self.groupBox_1)
        self.label_inCommandShortcutExit.setObjectName(u"label_inCommandShortcutExit")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutExit, 3, 3, 1, 1)

        self.lineEdit_inCommandShortcutExit = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutExit.setObjectName(u"lineEdit_inCommandShortcutExit")
        self.lineEdit_inCommandShortcutExit.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutExit.setMaxLength(1)
        self.lineEdit_inCommandShortcutExit.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutExit.setProperty(u"prefEntry", u"inCommandShortcutExit")
        self.lineEdit_inCommandShortcutExit.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutExit, 3, 4, 1, 1)

        self.label_inCommandShortcutContinue = QLabel(self.groupBox_1)
        self.label_inCommandShortcutContinue.setObjectName(u"label_inCommandShortcutContinue")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutContinue, 3, 6, 1, 1)

        self.lineEdit_inCommandShortcutContinue = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutContinue.setObjectName(u"lineEdit_inCommandShortcutContinue")
        self.lineEdit_inCommandShortcutContinue.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutContinue.setMaxLength(1)
        self.lineEdit_inCommandShortcutContinue.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutContinue.setProperty(u"prefEntry", u"inCommandShortcutContinue")
        self.lineEdit_inCommandShortcutContinue.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutContinue, 3, 7, 1, 1)

        self.label_inCommandShortcutCycleSnap = QLabel(self.groupBox_1)
        self.label_inCommandShortcutCycleSnap.setObjectName(u"label_inCommandShortcutCycleSnap")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutCycleSnap, 4, 0, 1, 1)

        self.lineEdit_inCommandShortcutCycleSnap = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutCycleSnap.setObjectName(u"lineEdit_inCommandShortcutCycleSnap")
        self.lineEdit_inCommandShortcutCycleSnap.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutCycleSnap.setText(u"`")
        self.lineEdit_inCommandShortcutCycleSnap.setMaxLength(1)
        self.lineEdit_inCommandShortcutCycleSnap.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutCycleSnap.setProperty(u"prefEntry", u"inCommandShortcutCycleSnap")
        self.lineEdit_inCommandShortcutCycleSnap.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutCycleSnap, 4, 1, 1, 1)

        self.label_inCommandShortcutAddHold = QLabel(self.groupBox_1)
        self.label_inCommandShortcutAddHold.setObjectName(u"label_inCommandShortcutAddHold")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutAddHold, 4, 3, 1, 1)

        self.lineEdit_inCommandShortcutAddHold = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutAddHold.setObjectName(u"lineEdit_inCommandShortcutAddHold")
        self.lineEdit_inCommandShortcutAddHold.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutAddHold.setMaxLength(1)
        self.lineEdit_inCommandShortcutAddHold.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutAddHold.setProperty(u"prefEntry", u"inCommandShortcutAddHold")
        self.lineEdit_inCommandShortcutAddHold.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutAddHold, 4, 4, 1, 1)

        self.label_inCommandShortcutSetWP = QLabel(self.groupBox_1)
        self.label_inCommandShortcutSetWP.setObjectName(u"label_inCommandShortcutSetWP")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutSetWP, 4, 6, 1, 1)

        self.lineEdit_inCommandShortcutSetWP = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutSetWP.setObjectName(u"lineEdit_inCommandShortcutSetWP")
        self.lineEdit_inCommandShortcutSetWP.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutSetWP.setMaxLength(1)
        self.lineEdit_inCommandShortcutSetWP.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutSetWP.setProperty(u"prefEntry", u"inCommandShortcutSetWP")
        self.lineEdit_inCommandShortcutSetWP.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutSetWP, 4, 7, 1, 1)

        self.label_inCommandShortcutSnap = QLabel(self.groupBox_1)
        self.label_inCommandShortcutSnap.setObjectName(u"label_inCommandShortcutSnap")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutSnap, 5, 0, 1, 1)

        self.lineEdit_inCommandShortcutSnap = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutSnap.setObjectName(u"lineEdit_inCommandShortcutSnap")
        self.lineEdit_inCommandShortcutSnap.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutSnap.setMaxLength(1)
        self.lineEdit_inCommandShortcutSnap.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutSnap.setProperty(u"prefEntry", u"inCommandShortcutSnap")
        self.lineEdit_inCommandShortcutSnap.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutSnap, 5, 1, 1, 1)

        self.label_inCommandShortcutIncreaseRadius = QLabel(self.groupBox_1)
        self.label_inCommandShortcutIncreaseRadius.setObjectName(u"label_inCommandShortcutIncreaseRadius")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutIncreaseRadius, 5, 3, 1, 1)

        self.lineEdit_inCommandShortcutIncreaseRadius = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutIncreaseRadius.setObjectName(u"lineEdit_inCommandShortcutIncreaseRadius")
        self.lineEdit_inCommandShortcutIncreaseRadius.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutIncreaseRadius.setText(u"P")
        self.lineEdit_inCommandShortcutIncreaseRadius.setMaxLength(1)
        self.lineEdit_inCommandShortcutIncreaseRadius.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutIncreaseRadius.setProperty(u"prefEntry", u"inCommandShortcutIncreaseRadius")
        self.lineEdit_inCommandShortcutIncreaseRadius.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutIncreaseRadius, 5, 4, 1, 1)

        self.label_inCommandShortcutDecreaseRadius = QLabel(self.groupBox_1)
        self.label_inCommandShortcutDecreaseRadius.setObjectName(u"label_inCommandShortcutDecreaseRadius")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutDecreaseRadius, 5, 6, 1, 1)

        self.lineEdit_inCommandShortcutDecreaseRadius = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutDecreaseRadius.setObjectName(u"lineEdit_inCommandShortcutDecreaseRadius")
        self.lineEdit_inCommandShortcutDecreaseRadius.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutDecreaseRadius.setText(u"M")
        self.lineEdit_inCommandShortcutDecreaseRadius.setMaxLength(1)
        self.lineEdit_inCommandShortcutDecreaseRadius.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutDecreaseRadius.setProperty(u"prefEntry", u"inCommandShortcutDecreaseRadius")
        self.lineEdit_inCommandShortcutDecreaseRadius.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutDecreaseRadius, 5, 7, 1, 1)

        self.label_inCommandShortcutRestrictX = QLabel(self.groupBox_1)
        self.label_inCommandShortcutRestrictX.setObjectName(u"label_inCommandShortcutRestrictX")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutRestrictX, 6, 0, 1, 1)

        self.lineEdit_inCommandShortcutRestrictX = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutRestrictX.setObjectName(u"lineEdit_inCommandShortcutRestrictX")
        self.lineEdit_inCommandShortcutRestrictX.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutRestrictX.setMaxLength(1)
        self.lineEdit_inCommandShortcutRestrictX.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutRestrictX.setProperty(u"prefEntry", u"inCommandShortcutRestrictX")
        self.lineEdit_inCommandShortcutRestrictX.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutRestrictX, 6, 1, 1, 1)

        self.label_inCommandShortcutRestrictY = QLabel(self.groupBox_1)
        self.label_inCommandShortcutRestrictY.setObjectName(u"label_inCommandShortcutRestrictY")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutRestrictY, 6, 3, 1, 1)

        self.lineEdit_inCommandShortcutRestrictY = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutRestrictY.setObjectName(u"lineEdit_inCommandShortcutRestrictY")
        self.lineEdit_inCommandShortcutRestrictY.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutRestrictY.setMaxLength(1)
        self.lineEdit_inCommandShortcutRestrictY.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutRestrictY.setProperty(u"prefEntry", u"inCommandShortcutRestrictY")
        self.lineEdit_inCommandShortcutRestrictY.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutRestrictY, 6, 4, 1, 1)

        self.label_inCommandShortcutRestrictZ = QLabel(self.groupBox_1)
        self.label_inCommandShortcutRestrictZ.setObjectName(u"label_inCommandShortcutRestrictZ")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutRestrictZ, 6, 6, 1, 1)

        self.lineEdit_inCommandShortcutRestrictZ = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutRestrictZ.setObjectName(u"lineEdit_inCommandShortcutRestrictZ")
        self.lineEdit_inCommandShortcutRestrictZ.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutRestrictZ.setMaxLength(1)
        self.lineEdit_inCommandShortcutRestrictZ.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutRestrictZ.setProperty(u"prefEntry", u"inCommandShortcutRestrictZ")
        self.lineEdit_inCommandShortcutRestrictZ.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutRestrictZ, 6, 7, 1, 1)

        self.label_inCommandShortcutRecenter = QLabel(self.groupBox_1)
        self.label_inCommandShortcutRecenter.setObjectName(u"label_inCommandShortcutRecenter")

        self.gridLayout_1.addWidget(self.label_inCommandShortcutRecenter, 7, 0, 1, 1)

        self.lineEdit_inCommandShortcutRecenter = Gui_PrefLineEdit(self.groupBox_1)
        self.lineEdit_inCommandShortcutRecenter.setObjectName(u"lineEdit_inCommandShortcutRecenter")
        self.lineEdit_inCommandShortcutRecenter.setMaximumSize(QSize(25, 16777215))
        self.lineEdit_inCommandShortcutRecenter.setMaxLength(1)
        self.lineEdit_inCommandShortcutRecenter.setClearButtonEnabled(False)
        self.lineEdit_inCommandShortcutRecenter.setProperty(u"prefEntry", u"inCommandShortcutRecenter")
        self.lineEdit_inCommandShortcutRecenter.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.lineEdit_inCommandShortcutRecenter, 7, 1, 1, 1)


        self.vboxLayout.addWidget(self.groupBox_1)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_SnapBarShowOnlyDuringCommands = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_SnapBarShowOnlyDuringCommands.setObjectName(u"checkBox_SnapBarShowOnlyDuringCommands")
        self.checkBox_SnapBarShowOnlyDuringCommands.setChecked(False)
        self.checkBox_SnapBarShowOnlyDuringCommands.setProperty(u"prefEntry", u"SnapBarShowOnlyDuringCommands")
        self.checkBox_SnapBarShowOnlyDuringCommands.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.checkBox_SnapBarShowOnlyDuringCommands, 0, 0, 1, 1)

        self.checkBox_DisplayStatusbarSnapWidget = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_DisplayStatusbarSnapWidget.setObjectName(u"checkBox_DisplayStatusbarSnapWidget")
        self.checkBox_DisplayStatusbarSnapWidget.setChecked(True)
        self.checkBox_DisplayStatusbarSnapWidget.setProperty(u"prefEntry", u"DisplayStatusbarSnapWidget")
        self.checkBox_DisplayStatusbarSnapWidget.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.checkBox_DisplayStatusbarSnapWidget, 1, 0, 1, 1)

        self.checkBox_DisplayStatusbarScaleWidget = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_DisplayStatusbarScaleWidget.setObjectName(u"checkBox_DisplayStatusbarScaleWidget")
        self.checkBox_DisplayStatusbarScaleWidget.setChecked(True)
        self.checkBox_DisplayStatusbarScaleWidget.setProperty(u"prefEntry", u"DisplayStatusbarScaleWidget")
        self.checkBox_DisplayStatusbarScaleWidget.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.checkBox_DisplayStatusbarScaleWidget, 2, 0, 1, 1)


        self.vboxLayout.addWidget(self.groupBox_2)

        self.verticalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer_1)


        self.retranslateUi(Gui__Dialog__DlgSettingsDraft)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsDraft)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsDraft):
        Gui__Dialog__DlgSettingsDraft.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Interface", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"In-Command Shortcuts", None))
        self.label_inCommandShortcutRelative.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Relative", None))
        self.lineEdit_inCommandShortcutRelative.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"R", None))
        self.label_inCommandShortcutGlobal.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Global", None))
        self.lineEdit_inCommandShortcutGlobal.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"G", None))
        self.label_inCommandShortcutLength.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Length", None))
        self.lineEdit_inCommandShortcutLength.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"L", None))
        self.label_inCommandShortcutMakeFace.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Make face", None))
        self.lineEdit_inCommandShortcutMakeFace.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"F", None))
        self.label_inCommandShortcutSelectEdge.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Select edge", None))
        self.lineEdit_inCommandShortcutSelectEdge.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"E", None))
        self.label_inCommandShortcutSubelementMode.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Subelement mode", None))
        self.lineEdit_inCommandShortcutSubelementMode.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"B", None))
        self.label_inCommandShortcutCopy.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Copy", None))
        self.lineEdit_inCommandShortcutCopy.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"C", None))
        self.label_inCommandShortcutUndo.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Undo", None))
        self.label_inCommandShortcutWipe.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Wipe", None))
        self.lineEdit_inCommandShortcutWipe.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"W", None))
        self.label_inCommandShortcutClose.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Close", None))
        self.lineEdit_inCommandShortcutClose.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"O", None))
        self.label_inCommandShortcutExit.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Exit", None))
        self.lineEdit_inCommandShortcutExit.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"A", None))
        self.label_inCommandShortcutContinue.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Continue", None))
        self.lineEdit_inCommandShortcutContinue.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"N", None))
        self.label_inCommandShortcutCycleSnap.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Cycle snap", None))
        self.label_inCommandShortcutAddHold.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Add hold", None))
        self.lineEdit_inCommandShortcutAddHold.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Q", None))
        self.label_inCommandShortcutSetWP.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Set working plane", None))
        self.lineEdit_inCommandShortcutSetWP.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"U", None))
        self.label_inCommandShortcutSnap.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Snap", None))
        self.lineEdit_inCommandShortcutSnap.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"S", None))
        self.label_inCommandShortcutIncreaseRadius.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Increase radius", None))
        self.label_inCommandShortcutDecreaseRadius.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Decrease radius", None))
        self.label_inCommandShortcutRestrictX.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Restrict X", None))
        self.lineEdit_inCommandShortcutRestrictX.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"X", None))
        self.label_inCommandShortcutRestrictY.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Restrict Y", None))
        self.lineEdit_inCommandShortcutRestrictY.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Y", None))
        self.label_inCommandShortcutRestrictZ.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Restrict Z", None))
        self.lineEdit_inCommandShortcutRestrictZ.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Z", None))
        self.label_inCommandShortcutRecenter.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Recenter", None))
        self.lineEdit_inCommandShortcutRecenter.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"D", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"UI Options", None))
#if QT_CONFIG(tooltip)
        self.checkBox_SnapBarShowOnlyDuringCommands.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, the Draft Snap toolbar will only be visible during commands", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_SnapBarShowOnlyDuringCommands.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Only show the Draft Snap toolbar during commands", None))
#if QT_CONFIG(tooltip)
        self.checkBox_DisplayStatusbarSnapWidget.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, the Draft Snap Widget is displayed in the Draft Status Bar", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_DisplayStatusbarSnapWidget.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Show the Draft Snap Widget in the Draft Workbench", None))
#if QT_CONFIG(tooltip)
        self.checkBox_DisplayStatusbarScaleWidget.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"If checked, the Draft Scale Widget is displayed in the Draft Status Bar", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_DisplayStatusbarScaleWidget.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Show the Draft Scale Widget in the Draft Workbench", None))
    # retranslateUi

