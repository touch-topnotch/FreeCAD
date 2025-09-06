# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskCenterLine.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskCenterLine(object):
    def setupUi(self, TechDrawGui__TaskCenterLine):
        if not TechDrawGui__TaskCenterLine.objectName():
            TechDrawGui__TaskCenterLine.setObjectName(u"TechDrawGui__TaskCenterLine")
        TechDrawGui__TaskCenterLine.setEnabled(True)
        TechDrawGui__TaskCenterLine.resize(300, 390)
        icon = QIcon()
        icon.addFile(u":/icons/actions/TechDraw_FaceCenterLine.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        TechDrawGui__TaskCenterLine.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(TechDrawGui__TaskCenterLine)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(TechDrawGui__TaskCenterLine)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.leBaseView = QLineEdit(TechDrawGui__TaskCenterLine)
        self.leBaseView.setObjectName(u"leBaseView")
        self.leBaseView.setEnabled(False)
        self.leBaseView.setMouseTracking(False)
        self.leBaseView.setFocusPolicy(Qt.NoFocus)
        self.leBaseView.setAcceptDrops(False)

        self.gridLayout.addWidget(self.leBaseView, 0, 1, 1, 1)

        self.label_2 = QLabel(TechDrawGui__TaskCenterLine)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lstSubList = QListWidget(TechDrawGui__TaskCenterLine)
        self.lstSubList.setObjectName(u"lstSubList")
        self.lstSubList.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstSubList.sizePolicy().hasHeightForWidth())
        self.lstSubList.setSizePolicy(sizePolicy)
        self.lstSubList.setMaximumSize(QSize(16777215, 50))

        self.gridLayout.addWidget(self.lstSubList, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gbOrientation = QGroupBox(TechDrawGui__TaskCenterLine)
        self.gbOrientation.setObjectName(u"gbOrientation")
        self.horizontalLayout = QHBoxLayout(self.gbOrientation)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rbVertical = QRadioButton(self.gbOrientation)
        self.bgOrientation = QButtonGroup(TechDrawGui__TaskCenterLine)
        self.bgOrientation.setObjectName(u"bgOrientation")
        self.bgOrientation.setExclusive(True)
        self.bgOrientation.addButton(self.rbVertical)
        self.rbVertical.setObjectName(u"rbVertical")
        self.rbVertical.setChecked(True)

        self.horizontalLayout.addWidget(self.rbVertical)

        self.rbHorizontal = QRadioButton(self.gbOrientation)
        self.bgOrientation.addButton(self.rbHorizontal)
        self.rbHorizontal.setObjectName(u"rbHorizontal")
        self.rbHorizontal.setEnabled(True)

        self.horizontalLayout.addWidget(self.rbHorizontal)

        self.rbAligned = QRadioButton(self.gbOrientation)
        self.bgOrientation.addButton(self.rbAligned)
        self.rbAligned.setObjectName(u"rbAligned")
        self.rbAligned.setEnabled(True)

        self.horizontalLayout.addWidget(self.rbAligned)


        self.verticalLayout.addWidget(self.gbOrientation)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(TechDrawGui__TaskCenterLine)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)

        self.dsbWeight = Gui_QuantitySpinBox(TechDrawGui__TaskCenterLine)
        self.dsbWeight.setObjectName(u"dsbWeight")
        self.dsbWeight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbWeight.setSingleStep(0.100000000000000)
        self.dsbWeight.setValue(0.500000000000000)

        self.gridLayout_3.addWidget(self.dsbWeight, 3, 1, 1, 1)

        self.cpLineColor = Gui_ColorButton(TechDrawGui__TaskCenterLine)
        self.cpLineColor.setObjectName(u"cpLineColor")
        self.cpLineColor.setColor(QColor(0, 0, 0))

        self.gridLayout_3.addWidget(self.cpLineColor, 2, 1, 1, 1)

        self.label_5 = QLabel(TechDrawGui__TaskCenterLine)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_6 = QLabel(TechDrawGui__TaskCenterLine)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.cboxStyle = QComboBox(TechDrawGui__TaskCenterLine)
        self.cboxStyle.setObjectName(u"cboxStyle")

        self.gridLayout_3.addWidget(self.cboxStyle, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.line = QFrame(TechDrawGui__TaskCenterLine)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(TechDrawGui__TaskCenterLine)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.qsbVertShift = Gui_QuantitySpinBox(TechDrawGui__TaskCenterLine)
        self.qsbVertShift.setObjectName(u"qsbVertShift")
        self.qsbVertShift.setMinimumSize(QSize(0, 20))
        self.qsbVertShift.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbVertShift.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.qsbVertShift, 1, 1, 1, 1)

        self.qsbHorizShift = Gui_QuantitySpinBox(TechDrawGui__TaskCenterLine)
        self.qsbHorizShift.setObjectName(u"qsbHorizShift")
        self.qsbHorizShift.setMinimumSize(QSize(0, 20))
        self.qsbHorizShift.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbHorizShift.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.qsbHorizShift, 0, 1, 1, 1)

        self.label_8 = QLabel(TechDrawGui__TaskCenterLine)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_9 = QLabel(TechDrawGui__TaskCenterLine)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.qsbRotate = Gui_QuantitySpinBox(TechDrawGui__TaskCenterLine)
        self.qsbRotate.setObjectName(u"qsbRotate")
        self.qsbRotate.setMinimumSize(QSize(0, 20))
        self.qsbRotate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbRotate.setMinimum(-360.000000000000000)
        self.qsbRotate.setMaximum(360.000000000000000)

        self.gridLayout_2.addWidget(self.qsbRotate, 2, 1, 1, 1)

        self.label_3 = QLabel(TechDrawGui__TaskCenterLine)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.qsbExtend = Gui_QuantitySpinBox(TechDrawGui__TaskCenterLine)
        self.qsbExtend.setObjectName(u"qsbExtend")
        self.qsbExtend.setMinimumSize(QSize(0, 20))
        self.qsbExtend.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbExtend.setProperty(u"unit", u"mm")
        self.qsbExtend.setValue(3.000000000000000)

        self.gridLayout_2.addWidget(self.qsbExtend, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TechDrawGui__TaskCenterLine)

        self.cboxStyle.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(TechDrawGui__TaskCenterLine)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskCenterLine):
        TechDrawGui__TaskCenterLine.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Centerline", None))
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Base view", None))
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Elements", None))
#if QT_CONFIG(tooltip)
        self.gbOrientation.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.gbOrientation.setTitle(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Orientation", None))
#if QT_CONFIG(tooltip)
        self.rbVertical.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Top to bottom line", None))
#endif // QT_CONFIG(tooltip)
        self.rbVertical.setText(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Vertical", None))
#if QT_CONFIG(tooltip)
        self.rbHorizontal.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Left to right line", None))
#endif // QT_CONFIG(tooltip)
        self.rbHorizontal.setText(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Horizontal", None))
#if QT_CONFIG(tooltip)
        self.rbAligned.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"\n"
"         Centerline between:\n"
"         - Lines: equidistant from both lines and at half the angle between them\n"
"         - Points: equidistant from both points\n"
"         ", None))
#endif // QT_CONFIG(tooltip)
        self.rbAligned.setText(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Aligned", None))
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Color", None))
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Weight", None))
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Style", None))
        self.label_7.setText(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Shift horizontal", None))
#if QT_CONFIG(tooltip)
        self.qsbVertShift.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Move line +up or -down", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.qsbHorizShift.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Move line -left or +right", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Shift vertical", None))
        self.label_9.setText(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Rotate", None))
#if QT_CONFIG(tooltip)
        self.qsbRotate.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Rotate line +CCW or -CW", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Extend by", None))
#if QT_CONFIG(tooltip)
        self.qsbExtend.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCenterLine", u"Make the line a little longer.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

