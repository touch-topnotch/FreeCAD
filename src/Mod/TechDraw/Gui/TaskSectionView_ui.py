# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskSectionView.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskSectionView(object):
    def setupUi(self, TechDrawGui__TaskSectionView):
        if not TechDrawGui__TaskSectionView.objectName():
            TechDrawGui__TaskSectionView.setObjectName(u"TechDrawGui__TaskSectionView")
        TechDrawGui__TaskSectionView.resize(442, 528)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskSectionView.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskSectionView.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(TechDrawGui__TaskSectionView)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(TechDrawGui__TaskSectionView)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.leBaseView = QLineEdit(TechDrawGui__TaskSectionView)
        self.leBaseView.setObjectName(u"leBaseView")
        self.leBaseView.setEnabled(False)
        self.leBaseView.setMinimumSize(QSize(0, 24))

        self.gridLayout_4.addWidget(self.leBaseView, 0, 2, 1, 1)

        self.label_2 = QLabel(TechDrawGui__TaskSectionView)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.leSymbol = QLineEdit(TechDrawGui__TaskSectionView)
        self.leSymbol.setObjectName(u"leSymbol")
        self.leSymbol.setMinimumSize(QSize(0, 24))

        self.gridLayout_4.addWidget(self.leSymbol, 1, 2, 1, 1)

        self.label_3 = QLabel(TechDrawGui__TaskSectionView)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.cmbScaleType = QComboBox(TechDrawGui__TaskSectionView)
        self.cmbScaleType.addItem("")
        self.cmbScaleType.addItem("")
        self.cmbScaleType.addItem("")
        self.cmbScaleType.setObjectName(u"cmbScaleType")
        self.cmbScaleType.setMinimumSize(QSize(0, 24))

        self.gridLayout_4.addWidget(self.cmbScaleType, 2, 2, 1, 1)

        self.label = QLabel(TechDrawGui__TaskSectionView)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 3, 0, 1, 1)

        self.sbScale = QDoubleSpinBox(TechDrawGui__TaskSectionView)
        self.sbScale.setObjectName(u"sbScale")
        self.sbScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbScale.setDecimals(6)
        self.sbScale.setMaximum(999.000000000000000)
        self.sbScale.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.sbScale, 3, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_4)

        self.gbOrientation = QGroupBox(TechDrawGui__TaskSectionView)
        self.gbOrientation.setObjectName(u"gbOrientation")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gbOrientation.sizePolicy().hasHeightForWidth())
        self.gbOrientation.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.gbOrientation)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.viewDirectionLayout = QHBoxLayout()
        self.viewDirectionLayout.setObjectName(u"viewDirectionLayout")

        self.verticalLayout_2.addLayout(self.viewDirectionLayout)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pbUp = QPushButton(self.gbOrientation)
        self.pbUp.setObjectName(u"pbUp")
        self.pbUp.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/icons/actions/section-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pbUp.setIcon(icon)
        self.pbUp.setIconSize(QSize(48, 48))
        self.pbUp.setCheckable(True)

        self.gridLayout_3.addWidget(self.pbUp, 0, 0, 1, 1)

        self.pbDown = QPushButton(self.gbOrientation)
        self.pbDown.setObjectName(u"pbDown")
        self.pbDown.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u":/icons/actions/section-down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pbDown.setIcon(icon1)
        self.pbDown.setIconSize(QSize(48, 48))
        self.pbDown.setCheckable(True)

        self.gridLayout_3.addWidget(self.pbDown, 0, 1, 1, 1)

        self.pbLeft = QPushButton(self.gbOrientation)
        self.pbLeft.setObjectName(u"pbLeft")
        self.pbLeft.setMaximumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(u":/icons/actions/section-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pbLeft.setIcon(icon2)
        self.pbLeft.setIconSize(QSize(48, 48))
        self.pbLeft.setCheckable(True)

        self.gridLayout_3.addWidget(self.pbLeft, 0, 2, 1, 1)

        self.pbRight = QPushButton(self.gbOrientation)
        self.pbRight.setObjectName(u"pbRight")
        self.pbRight.setMaximumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u":/icons/actions/section-right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pbRight.setIcon(icon3)
        self.pbRight.setIconSize(QSize(48, 48))
        self.pbRight.setCheckable(True)

        self.gridLayout_3.addWidget(self.pbRight, 0, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.compassLayout = QVBoxLayout()
        self.compassLayout.setObjectName(u"compassLayout")

        self.verticalLayout_2.addLayout(self.compassLayout)


        self.verticalLayout_3.addWidget(self.gbOrientation)

        self.gbPlane = QGroupBox(TechDrawGui__TaskSectionView)
        self.gbPlane.setObjectName(u"gbPlane")
        self.verticalLayoutPlane = QVBoxLayout(self.gbPlane)
        self.verticalLayoutPlane.setObjectName(u"verticalLayoutPlane")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sbOrgY = Gui_QuantitySpinBox(self.gbPlane)
        self.sbOrgY.setObjectName(u"sbOrgY")
        sizePolicy.setHeightForWidth(self.sbOrgY.sizePolicy().hasHeightForWidth())
        self.sbOrgY.setSizePolicy(sizePolicy)
        self.sbOrgY.setMinimumSize(QSize(150, 24))
        self.sbOrgY.setKeyboardTracking(False)
        self.sbOrgY.setProperty(u"unit", u"")

        self.gridLayout.addWidget(self.sbOrgY, 1, 1, 1, 1)

        self.label_12 = QLabel(self.gbPlane)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setText(u"Z")

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_10 = QLabel(self.gbPlane)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setText(u"X")

        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.sbOrgX = Gui_QuantitySpinBox(self.gbPlane)
        self.sbOrgX.setObjectName(u"sbOrgX")
        sizePolicy.setHeightForWidth(self.sbOrgX.sizePolicy().hasHeightForWidth())
        self.sbOrgX.setSizePolicy(sizePolicy)
        self.sbOrgX.setMinimumSize(QSize(150, 24))
        self.sbOrgX.setKeyboardTracking(False)
        self.sbOrgX.setProperty(u"unit", u"")

        self.gridLayout.addWidget(self.sbOrgX, 0, 1, 1, 1)

        self.sbOrgZ = Gui_QuantitySpinBox(self.gbPlane)
        self.sbOrgZ.setObjectName(u"sbOrgZ")
        sizePolicy.setHeightForWidth(self.sbOrgZ.sizePolicy().hasHeightForWidth())
        self.sbOrgZ.setSizePolicy(sizePolicy)
        self.sbOrgZ.setMinimumSize(QSize(150, 24))
        self.sbOrgZ.setKeyboardTracking(False)
        self.sbOrgZ.setProperty(u"unit", u"")

        self.gridLayout.addWidget(self.sbOrgZ, 2, 1, 1, 1)

        self.label_11 = QLabel(self.gbPlane)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setText(u"Y")

        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)

        self.verticalLayoutPlane.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.gbPlane)

        self.gbUpdate = QGroupBox(TechDrawGui__TaskSectionView)
        self.gbUpdate.setObjectName(u"gbUpdate")
        self.verticalLayoutUpdate = QVBoxLayout(self.gbUpdate)
        self.verticalLayoutUpdate.setObjectName(u"verticalLayoutUpdate")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pbUpdateNow = QPushButton(self.gbUpdate)
        self.pbUpdateNow.setObjectName(u"pbUpdateNow")

        self.gridLayout_5.addWidget(self.pbUpdateNow, 0, 1, 1, 1)

        self.cbLiveUpdate = QCheckBox(self.gbUpdate)
        self.cbLiveUpdate.setObjectName(u"cbLiveUpdate")

        self.gridLayout_5.addWidget(self.cbLiveUpdate, 0, 0, 1, 1)

        self.lPendingUpdates = QLabel(self.gbUpdate)
        self.lPendingUpdates.setObjectName(u"lPendingUpdates")
        self.lPendingUpdates.setEnabled(True)

        self.gridLayout_5.addWidget(self.lPendingUpdates, 1, 0, 1, 1)


        self.verticalLayoutUpdate.addLayout(self.gridLayout_5)


        self.verticalLayout_3.addWidget(self.gbUpdate)


        self.retranslateUi(TechDrawGui__TaskSectionView)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskSectionView)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskSectionView):
        TechDrawGui__TaskSectionView.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Section Parameters", None))
        self.label_7.setText(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Base view", None))
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Identifier", None))
#if QT_CONFIG(tooltip)
        self.leSymbol.setToolTip(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Identifier for this section", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Scale type", None))
        self.cmbScaleType.setItemText(0, QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Page", None))
        self.cmbScaleType.setItemText(1, QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Automatic", None))
        self.cmbScaleType.setItemText(2, QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Custom", None))

#if QT_CONFIG(tooltip)
        self.cmbScaleType.setToolTip(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Scale Page/Auto/Custom", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Scale", None))
#if QT_CONFIG(tooltip)
        self.sbScale.setToolTip(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Scale factor for the section view", None))
#endif // QT_CONFIG(tooltip)
        self.gbOrientation.setTitle(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Set View Direction", None))
#if QT_CONFIG(tooltip)
        self.pbUp.setToolTip(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Preset view direction looking up", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pbUp.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pbUp.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pbUp.setText("")
#if QT_CONFIG(tooltip)
        self.pbDown.setToolTip(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Preset view direction looking down", None))
#endif // QT_CONFIG(tooltip)
        self.pbDown.setText("")
#if QT_CONFIG(tooltip)
        self.pbLeft.setToolTip(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Preset view direction looking left", None))
#endif // QT_CONFIG(tooltip)
        self.pbLeft.setText("")
#if QT_CONFIG(tooltip)
        self.pbRight.setToolTip(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Preset view direction looking right", None))
#endif // QT_CONFIG(tooltip)
        self.pbRight.setText("")
#if QT_CONFIG(tooltip)
        self.gbPlane.setToolTip(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Global 3D coordinates defining the shortest distance from the 3D origin to the section plane", None))
#endif // QT_CONFIG(tooltip)
        self.gbPlane.setTitle(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Section Plane Location", None))
        self.gbUpdate.setTitle(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Preview", None))
#if QT_CONFIG(tooltip)
        self.pbUpdateNow.setToolTip(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"<html><head/><body><p>Rebuild display now. May be slow for complex models.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pbUpdateNow.setText(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Update Now", None))
#if QT_CONFIG(tooltip)
        self.cbLiveUpdate.setToolTip(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Check to update display after every property change", None))
#endif // QT_CONFIG(tooltip)
        self.cbLiveUpdate.setText(QCoreApplication.translate("TechDrawGui::TaskSectionView", u"Live update", None))
        self.lPendingUpdates.setText("")
    # retranslateUi

