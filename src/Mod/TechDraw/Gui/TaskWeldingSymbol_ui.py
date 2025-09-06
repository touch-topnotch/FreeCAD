# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskWeldingSymbol.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TaskWeldingSymbol(object):
    def setupUi(self, TaskWeldingSymbol):
        if not TaskWeldingSymbol.objectName():
            TaskWeldingSymbol.setObjectName(u"TaskWeldingSymbol")
        TaskWeldingSymbol.resize(400, 244)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TaskWeldingSymbol.sizePolicy().hasHeightForWidth())
        TaskWeldingSymbol.setSizePolicy(sizePolicy)
        TaskWeldingSymbol.setMinimumSize(QSize(250, 0))
        icon = QIcon()
        icon.addFile(u":/icons/actions/TechDraw_WeldSymbol.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        TaskWeldingSymbol.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(TaskWeldingSymbol)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.hlArrowSideLayout = QHBoxLayout()
        self.hlArrowSideLayout.setObjectName(u"hlArrowSideLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.leArrowTextC = QLineEdit(TaskWeldingSymbol)
        self.leArrowTextC.setObjectName(u"leArrowTextC")

        self.gridLayout.addWidget(self.leArrowTextC, 0, 1, 1, 1)

        self.leArrowTextL = QLineEdit(TaskWeldingSymbol)
        self.leArrowTextL.setObjectName(u"leArrowTextL")

        self.gridLayout.addWidget(self.leArrowTextL, 2, 0, 1, 1)

        self.pbArrowSymbol = QPushButton(TaskWeldingSymbol)
        self.pbArrowSymbol.setObjectName(u"pbArrowSymbol")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pbArrowSymbol.sizePolicy().hasHeightForWidth())
        self.pbArrowSymbol.setSizePolicy(sizePolicy1)
        self.pbArrowSymbol.setMinimumSize(QSize(0, 0))
        self.pbArrowSymbol.setBaseSize(QSize(0, 32))
        self.pbArrowSymbol.setCheckable(False)

        self.gridLayout.addWidget(self.pbArrowSymbol, 2, 1, 1, 1)

        self.leArrowTextR = QLineEdit(TaskWeldingSymbol)
        self.leArrowTextR.setObjectName(u"leArrowTextR")

        self.gridLayout.addWidget(self.leArrowTextR, 2, 2, 1, 1)


        self.hlArrowSideLayout.addLayout(self.gridLayout)


        self.verticalLayout_4.addLayout(self.hlArrowSideLayout)

        self.line = QFrame(TaskWeldingSymbol)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_4.addWidget(self.line)

        self.hlOtherSideLayout = QHBoxLayout()
        self.hlOtherSideLayout.setObjectName(u"hlOtherSideLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.leOtherTextL = QLineEdit(TaskWeldingSymbol)
        self.leOtherTextL.setObjectName(u"leOtherTextL")

        self.gridLayout_2.addWidget(self.leOtherTextL, 0, 0, 1, 1)

        self.pbOtherSymbol = QPushButton(TaskWeldingSymbol)
        self.pbOtherSymbol.setObjectName(u"pbOtherSymbol")

        self.gridLayout_2.addWidget(self.pbOtherSymbol, 0, 1, 1, 1)

        self.leOtherTextR = QLineEdit(TaskWeldingSymbol)
        self.leOtherTextR.setObjectName(u"leOtherTextR")

        self.gridLayout_2.addWidget(self.leOtherTextR, 0, 2, 1, 1)

        self.pbOtherErase = QPushButton(TaskWeldingSymbol)
        self.pbOtherErase.setObjectName(u"pbOtherErase")
        sizePolicy1.setHeightForWidth(self.pbOtherErase.sizePolicy().hasHeightForWidth())
        self.pbOtherErase.setSizePolicy(sizePolicy1)
        self.pbOtherErase.setMinimumSize(QSize(60, 30))
        self.pbOtherErase.setMaximumSize(QSize(60, 30))
        self.pbOtherErase.setBaseSize(QSize(60, 30))

        self.gridLayout_2.addWidget(self.pbOtherErase, 1, 0, 1, 1)

        self.leOtherTextC = QLineEdit(TaskWeldingSymbol)
        self.leOtherTextC.setObjectName(u"leOtherTextC")

        self.gridLayout_2.addWidget(self.leOtherTextC, 1, 1, 1, 1)

        self.pbFlipSides = QPushButton(TaskWeldingSymbol)
        self.pbFlipSides.setObjectName(u"pbFlipSides")
        sizePolicy1.setHeightForWidth(self.pbFlipSides.sizePolicy().hasHeightForWidth())
        self.pbFlipSides.setSizePolicy(sizePolicy1)
        self.pbFlipSides.setMinimumSize(QSize(60, 30))
        self.pbFlipSides.setMaximumSize(QSize(60, 30))
        self.pbFlipSides.setBaseSize(QSize(60, 30))

        self.gridLayout_2.addWidget(self.pbFlipSides, 1, 2, 1, 1, Qt.AlignRight)


        self.hlOtherSideLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_4.addLayout(self.hlOtherSideLayout)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.line_2 = QFrame(TaskWeldingSymbol)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cbFieldWeld = QCheckBox(TaskWeldingSymbol)
        self.cbFieldWeld.setObjectName(u"cbFieldWeld")

        self.gridLayout_3.addWidget(self.cbFieldWeld, 0, 0, 1, 1)

        self.cbAllAround = QCheckBox(TaskWeldingSymbol)
        self.cbAllAround.setObjectName(u"cbAllAround")

        self.gridLayout_3.addWidget(self.cbAllAround, 0, 1, 1, 1)

        self.cbAltWeld = QCheckBox(TaskWeldingSymbol)
        self.cbAltWeld.setObjectName(u"cbAltWeld")

        self.gridLayout_3.addWidget(self.cbAltWeld, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(TaskWeldingSymbol)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.leTailText = QLineEdit(TaskWeldingSymbol)
        self.leTailText.setObjectName(u"leTailText")
        sizePolicy.setHeightForWidth(self.leTailText.sizePolicy().hasHeightForWidth())
        self.leTailText.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.leTailText, 0, 1, 1, 1)

        self.label = QLabel(TaskWeldingSymbol)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.fcSymbolDir = Gui_FileChooser(TaskWeldingSymbol)
        self.fcSymbolDir.setObjectName(u"fcSymbolDir")
        self.fcSymbolDir.setMode(Gui.FileChooser.Directory)
        self.fcSymbolDir.setFilter(u"*.svg")

        self.gridLayout_4.addWidget(self.fcSymbolDir, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)


        self.retranslateUi(TaskWeldingSymbol)

        QMetaObject.connectSlotsByName(TaskWeldingSymbol)
    # setupUi

    def retranslateUi(self, TaskWeldingSymbol):
        TaskWeldingSymbol.setWindowTitle(QCoreApplication.translate("TaskWeldingSymbol", u"Welding Symbol", None))
#if QT_CONFIG(tooltip)
        self.leArrowTextC.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Text above arrow side symbol\n"
"Angle, surface finish, root", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.leArrowTextL.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Text before arrow side symbol\n"
"Preparation depth, (weld size)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbArrowSymbol.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Pick arrow side symbol", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pbArrowSymbol.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pbArrowSymbol.setText(QCoreApplication.translate("TaskWeldingSymbol", u"Symbol", None))
#if QT_CONFIG(tooltip)
        self.leArrowTextR.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Text after arrow side symbol\n"
"Number of welds \u00d7 length, (gap)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.leOtherTextL.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Text before other side symbol\n"
"Preparation depth, (weld size)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbOtherSymbol.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Pick other side symbol", None))
#endif // QT_CONFIG(tooltip)
        self.pbOtherSymbol.setText(QCoreApplication.translate("TaskWeldingSymbol", u"Symbol", None))
#if QT_CONFIG(tooltip)
        self.leOtherTextR.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Text after other side symbol\n"
"Number of welds \u00d7 length, (gap)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbOtherErase.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Remove other side symbol", None))
#endif // QT_CONFIG(tooltip)
        self.pbOtherErase.setText(QCoreApplication.translate("TaskWeldingSymbol", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.leOtherTextC.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Text below arrow side symbol\n"
"Angle, surface finish, root", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pbFlipSides.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Flips the sides", None))
#endif // QT_CONFIG(tooltip)
        self.pbFlipSides.setText(QCoreApplication.translate("TaskWeldingSymbol", u"Flip sides", None))
#if QT_CONFIG(tooltip)
        self.cbFieldWeld.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Adds the 'Field weld' symbol (flag)\n"
"at the kink in the leader line", None))
#endif // QT_CONFIG(tooltip)
        self.cbFieldWeld.setText(QCoreApplication.translate("TaskWeldingSymbol", u"Field weld", None))
#if QT_CONFIG(tooltip)
        self.cbAllAround.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Adds the 'All around' symbol (circle)\n"
"at the kink in the leader line", None))
#endif // QT_CONFIG(tooltip)
        self.cbAllAround.setText(QCoreApplication.translate("TaskWeldingSymbol", u"All around", None))
#if QT_CONFIG(tooltip)
        self.cbAltWeld.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Offsets the lower symbol to indicate alternating welds", None))
#endif // QT_CONFIG(tooltip)
        self.cbAltWeld.setText(QCoreApplication.translate("TaskWeldingSymbol", u"Alternating", None))
        self.label_5.setText(QCoreApplication.translate("TaskWeldingSymbol", u"Tail text", None))
#if QT_CONFIG(tooltip)
        self.leTailText.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Text at end of symbol", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TaskWeldingSymbol", u"Symbol directory", None))
#if QT_CONFIG(tooltip)
        self.fcSymbolDir.setToolTip(QCoreApplication.translate("TaskWeldingSymbol", u"Directory path for welding symbols.\n"
"This directory will be used for the symbol selection.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

