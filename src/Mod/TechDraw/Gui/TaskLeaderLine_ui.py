# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskLeaderLine.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskLeaderLine(object):
    def setupUi(self, TechDrawGui__TaskLeaderLine):
        if not TechDrawGui__TaskLeaderLine.objectName():
            TechDrawGui__TaskLeaderLine.setObjectName(u"TechDrawGui__TaskLeaderLine")
        TechDrawGui__TaskLeaderLine.resize(350, 225)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskLeaderLine.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskLeaderLine.setSizePolicy(sizePolicy)
        TechDrawGui__TaskLeaderLine.setMinimumSize(QSize(250, 0))
        icon = QIcon()
        icon.addFile(u":/icons/actions/TechDraw_LeaderLine.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        TechDrawGui__TaskLeaderLine.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(TechDrawGui__TaskLeaderLine)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(TechDrawGui__TaskLeaderLine)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.tbBaseView = QTextBrowser(TechDrawGui__TaskLeaderLine)
        self.tbBaseView.setObjectName(u"tbBaseView")
        self.tbBaseView.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tbBaseView.sizePolicy().hasHeightForWidth())
        self.tbBaseView.setSizePolicy(sizePolicy1)
        self.tbBaseView.setMaximumSize(QSize(16777215, 22))
        self.tbBaseView.setMouseTracking(False)
        self.tbBaseView.setFocusPolicy(Qt.NoFocus)
        self.tbBaseView.setAcceptDrops(False)
        self.tbBaseView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.tbBaseView, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pbCancelEdit = QPushButton(TechDrawGui__TaskLeaderLine)
        self.pbCancelEdit.setObjectName(u"pbCancelEdit")

        self.horizontalLayout.addWidget(self.pbCancelEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pbTracker = QPushButton(TechDrawGui__TaskLeaderLine)
        self.pbTracker.setObjectName(u"pbTracker")

        self.horizontalLayout.addWidget(self.pbTracker)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(TechDrawGui__TaskLeaderLine)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(TechDrawGui__TaskLeaderLine)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.cboxStartSym = QComboBox(TechDrawGui__TaskLeaderLine)
        self.cboxStartSym.setObjectName(u"cboxStartSym")
        self.cboxStartSym.setMinimumSize(QSize(0, 22))

        self.gridLayout_2.addWidget(self.cboxStartSym, 0, 2, 1, 1)

        self.label_3 = QLabel(TechDrawGui__TaskLeaderLine)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.cboxEndSym = QComboBox(TechDrawGui__TaskLeaderLine)
        self.cboxEndSym.setObjectName(u"cboxEndSym")
        self.cboxEndSym.setMinimumSize(QSize(0, 22))

        self.gridLayout_2.addWidget(self.cboxEndSym, 1, 2, 1, 1)

        self.label = QLabel(TechDrawGui__TaskLeaderLine)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.cpLineColor = Gui_ColorButton(TechDrawGui__TaskLeaderLine)
        self.cpLineColor.setObjectName(u"cpLineColor")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(22)
        sizePolicy2.setHeightForWidth(self.cpLineColor.sizePolicy().hasHeightForWidth())
        self.cpLineColor.setSizePolicy(sizePolicy2)
        self.cpLineColor.setColor(QColor(0, 0, 0))

        self.gridLayout_2.addWidget(self.cpLineColor, 2, 2, 1, 1)

        self.label_5 = QLabel(TechDrawGui__TaskLeaderLine)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.dsbWeight = Gui_QuantitySpinBox(TechDrawGui__TaskLeaderLine)
        self.dsbWeight.setObjectName(u"dsbWeight")
        self.dsbWeight.setEnabled(True)
        self.dsbWeight.setMinimumSize(QSize(0, 22))
        self.dsbWeight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbWeight.setSingleStep(0.100000000000000)
        self.dsbWeight.setValue(0.500000000000000)

        self.gridLayout_2.addWidget(self.dsbWeight, 3, 2, 1, 1)

        self.label_6 = QLabel(TechDrawGui__TaskLeaderLine)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)

        self.cboxStyle = QComboBox(TechDrawGui__TaskLeaderLine)
        icon1 = QIcon()
        icon1.addFile(u":/icons/none.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cboxStyle.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/icons/continuous-line.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cboxStyle.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/icons/dash-line.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cboxStyle.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/icons/dot-line.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cboxStyle.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/icons/dashDot-line.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cboxStyle.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/icons/dashDotDot-line.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cboxStyle.addItem(icon6, "")
        self.cboxStyle.setObjectName(u"cboxStyle")
        self.cboxStyle.setMinimumSize(QSize(0, 22))

        self.gridLayout_2.addWidget(self.cboxStyle, 4, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.retranslateUi(TechDrawGui__TaskLeaderLine)

        self.cboxStartSym.setCurrentIndex(-1)
        self.cboxStyle.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(TechDrawGui__TaskLeaderLine)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskLeaderLine):
        TechDrawGui__TaskLeaderLine.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Leader Line", None))
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Base view", None))
        self.pbCancelEdit.setText(QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Discard Changes", None))
#if QT_CONFIG(tooltip)
        self.pbTracker.setToolTip(QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"First pick the start point of the line,\n"
"then at least one more point.\n"
"You can pick further points to get line segments.", None))
#endif // QT_CONFIG(tooltip)
        self.pbTracker.setText(QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Pick Points", None))
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Start symbol", None))
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"End symbol", None))
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Color", None))
#if QT_CONFIG(tooltip)
        self.cpLineColor.setToolTip(QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Line color", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Width", None))
#if QT_CONFIG(tooltip)
        self.dsbWeight.setToolTip(QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Line width", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Style", None))
        self.cboxStyle.setItemText(0, QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"No line", None))
        self.cboxStyle.setItemText(1, QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Continuous", None))
        self.cboxStyle.setItemText(2, QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Dash", None))
        self.cboxStyle.setItemText(3, QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Dot", None))
        self.cboxStyle.setItemText(4, QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"DashDot", None))
        self.cboxStyle.setItemText(5, QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"DashDotDot", None))

#if QT_CONFIG(tooltip)
        self.cboxStyle.setToolTip(QCoreApplication.translate("TechDrawGui::TaskLeaderLine", u"Line style", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

