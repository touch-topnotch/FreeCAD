# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskComplexSection.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskComplexSection(object):
    def setupUi(self, TechDrawGui__TaskComplexSection):
        if not TechDrawGui__TaskComplexSection.objectName():
            TechDrawGui__TaskComplexSection.setObjectName(u"TechDrawGui__TaskComplexSection")
        TechDrawGui__TaskComplexSection.resize(373, 612)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskComplexSection.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskComplexSection.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/actions/TechDraw_ComplexSection.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        TechDrawGui__TaskComplexSection.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(TechDrawGui__TaskComplexSection)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(TechDrawGui__TaskComplexSection)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.pbSectionObjects = QPushButton(self.groupBox)
        self.pbSectionObjects.setObjectName(u"pbSectionObjects")

        self.gridLayout_2.addWidget(self.pbSectionObjects, 1, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.leProfileObject = QLineEdit(self.groupBox)
        self.leProfileObject.setObjectName(u"leProfileObject")
        self.leProfileObject.setReadOnly(True)

        self.gridLayout_2.addWidget(self.leProfileObject, 2, 1, 1, 1)

        self.leSectionObjects = QLineEdit(self.groupBox)
        self.leSectionObjects.setObjectName(u"leSectionObjects")
        self.leSectionObjects.setReadOnly(True)

        self.gridLayout_2.addWidget(self.leSectionObjects, 0, 1, 1, 1)

        self.pbProfileObject = QPushButton(self.groupBox)
        self.pbProfileObject.setObjectName(u"pbProfileObject")

        self.gridLayout_2.addWidget(self.pbProfileObject, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(TechDrawGui__TaskComplexSection)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cmbScaleType = QComboBox(self.groupBox_2)
        self.cmbScaleType.addItem("")
        self.cmbScaleType.addItem("")
        self.cmbScaleType.addItem("")
        self.cmbScaleType.setObjectName(u"cmbScaleType")
        self.cmbScaleType.setMinimumSize(QSize(0, 26))

        self.gridLayout_4.addWidget(self.cmbScaleType, 3, 1, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 4, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)

        self.sbScale = QDoubleSpinBox(self.groupBox_2)
        self.sbScale.setObjectName(u"sbScale")
        self.sbScale.setMinimumSize(QSize(0, 26))
        self.sbScale.setDecimals(6)
        self.sbScale.setMaximum(999.000000000000000)
        self.sbScale.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.sbScale, 4, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)

        self.cmbStrategy = QComboBox(self.groupBox_2)
        self.cmbStrategy.addItem("")
        self.cmbStrategy.addItem("")
        self.cmbStrategy.addItem("")
        self.cmbStrategy.setObjectName(u"cmbStrategy")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cmbStrategy.sizePolicy().hasHeightForWidth())
        self.cmbStrategy.setSizePolicy(sizePolicy1)
        self.cmbStrategy.setMinimumSize(QSize(0, 26))
        self.cmbStrategy.setBaseSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.cmbStrategy, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.leSymbol = QLineEdit(self.groupBox_2)
        self.leSymbol.setObjectName(u"leSymbol")
        self.leSymbol.setMinimumSize(QSize(0, 26))

        self.gridLayout_4.addWidget(self.leSymbol, 2, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.leBaseView = QLineEdit(self.groupBox_2)
        self.leBaseView.setObjectName(u"leBaseView")
        self.leBaseView.setEnabled(False)

        self.gridLayout_4.addWidget(self.leBaseView, 0, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.gbOrientation = QGroupBox(TechDrawGui__TaskComplexSection)
        self.gbOrientation.setObjectName(u"gbOrientation")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gbOrientation.sizePolicy().hasHeightForWidth())
        self.gbOrientation.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.gbOrientation)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.viewDirectionLayout = QHBoxLayout()
        self.viewDirectionLayout.setObjectName(u"viewDirectionLayout")

        self.verticalLayout_4.addLayout(self.viewDirectionLayout)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pbUp = QPushButton(self.gbOrientation)
        self.pbUp.setObjectName(u"pbUp")
        self.pbUp.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u":/icons/actions/section-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pbUp.setIcon(icon1)
        self.pbUp.setIconSize(QSize(48, 48))
        self.pbUp.setCheckable(False)

        self.gridLayout_3.addWidget(self.pbUp, 0, 0, 1, 1)

        self.pbDown = QPushButton(self.gbOrientation)
        self.pbDown.setObjectName(u"pbDown")
        self.pbDown.setMaximumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(u":/icons/actions/section-down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pbDown.setIcon(icon2)
        self.pbDown.setIconSize(QSize(48, 48))

        self.gridLayout_3.addWidget(self.pbDown, 0, 1, 1, 1)

        self.pbLeft = QPushButton(self.gbOrientation)
        self.pbLeft.setObjectName(u"pbLeft")
        self.pbLeft.setMaximumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u":/icons/actions/section-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pbLeft.setIcon(icon3)
        self.pbLeft.setIconSize(QSize(48, 48))

        self.gridLayout_3.addWidget(self.pbLeft, 0, 2, 1, 1)

        self.pbRight = QPushButton(self.gbOrientation)
        self.pbRight.setObjectName(u"pbRight")
        self.pbRight.setMaximumSize(QSize(50, 50))
        icon4 = QIcon()
        icon4.addFile(u":/icons/actions/section-right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pbRight.setIcon(icon4)
        self.pbRight.setIconSize(QSize(48, 48))

        self.gridLayout_3.addWidget(self.pbRight, 0, 3, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.compassLayout = QVBoxLayout()
        self.compassLayout.setObjectName(u"compassLayout")

        self.verticalLayout_4.addLayout(self.compassLayout)


        self.verticalLayout_3.addWidget(self.gbOrientation)

        self.groupBox_3 = QGroupBox(TechDrawGui__TaskComplexSection)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cbLiveUpdate = QCheckBox(self.groupBox_3)
        self.cbLiveUpdate.setObjectName(u"cbLiveUpdate")

        self.gridLayout.addWidget(self.cbLiveUpdate, 0, 0, 1, 1)

        self.pbUpdateNow = QPushButton(self.groupBox_3)
        self.pbUpdateNow.setObjectName(u"pbUpdateNow")

        self.gridLayout.addWidget(self.pbUpdateNow, 0, 1, 1, 1)

        self.lPendingUpdates = QLabel(self.groupBox_3)
        self.lPendingUpdates.setObjectName(u"lPendingUpdates")

        self.gridLayout.addWidget(self.lPendingUpdates, 1, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.groupBox_3)


        self.retranslateUi(TechDrawGui__TaskComplexSection)

        self.cmbStrategy.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TechDrawGui__TaskComplexSection)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskComplexSection):
        TechDrawGui__TaskComplexSection.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Complex Section", None))
        self.groupBox.setTitle(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Object Selection", None))
        self.label_8.setText(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Objects to section", None))
        self.pbSectionObjects.setText(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Use Selection", None))
        self.label_9.setText(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Profile object", None))
        self.pbProfileObject.setText(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Use Selection", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Section Parameters", None))
        self.cmbScaleType.setItemText(0, QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Page", None))
        self.cmbScaleType.setItemText(1, QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Automatic", None))
        self.cmbScaleType.setItemText(2, QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Custom", None))

#if QT_CONFIG(tooltip)
        self.cmbScaleType.setToolTip(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Scale Page/Auto/Custom", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Scale", None))
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Scale type", None))
        self.label_7.setText(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Projection strategy", None))
        self.cmbStrategy.setItemText(0, QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Offset", None))
        self.cmbStrategy.setItemText(1, QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Aligned", None))
        self.cmbStrategy.setItemText(2, QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"No parallel", None))

        self.cmbStrategy.setCurrentText(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Offset", None))
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Identifier", None))
#if QT_CONFIG(tooltip)
        self.leSymbol.setToolTip(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Identifier for this section", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Base view", None))
        self.gbOrientation.setTitle(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Set View Direction", None))
#if QT_CONFIG(tooltip)
        self.pbUp.setToolTip(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Preset view direction looking up", None))
#endif // QT_CONFIG(tooltip)
        self.pbUp.setText("")
#if QT_CONFIG(tooltip)
        self.pbDown.setToolTip(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Preset view direction looking down", None))
#endif // QT_CONFIG(tooltip)
        self.pbDown.setText("")
#if QT_CONFIG(tooltip)
        self.pbLeft.setToolTip(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Preset view direction looking left", None))
#endif // QT_CONFIG(tooltip)
        self.pbLeft.setText("")
#if QT_CONFIG(tooltip)
        self.pbRight.setToolTip(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Preset view direction looking right", None))
#endif // QT_CONFIG(tooltip)
        self.pbRight.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Preview", None))
#if QT_CONFIG(tooltip)
        self.cbLiveUpdate.setToolTip(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Check to update display after every property change", None))
#endif // QT_CONFIG(tooltip)
        self.cbLiveUpdate.setText(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Live Update", None))
#if QT_CONFIG(tooltip)
        self.pbUpdateNow.setToolTip(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Rebuild display now. May be slow for complex models", None))
#endif // QT_CONFIG(tooltip)
        self.pbUpdateNow.setText(QCoreApplication.translate("TechDrawGui::TaskComplexSection", u"Update Now", None))
        self.lPendingUpdates.setText("")
    # retranslateUi

