# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskProjGroup.ui'
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
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskProjGroup(object):
    def setupUi(self, TechDrawGui__TaskProjGroup):
        if not TechDrawGui__TaskProjGroup.objectName():
            TechDrawGui__TaskProjGroup.setObjectName(u"TechDrawGui__TaskProjGroup")
        TechDrawGui__TaskProjGroup.resize(250, 477)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskProjGroup.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskProjGroup.setSizePolicy(sizePolicy)
        TechDrawGui__TaskProjGroup.setMinimumSize(QSize(250, 0))
        self.verticalLayout = QVBoxLayout(TechDrawGui__TaskProjGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(TechDrawGui__TaskProjGroup)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.cmbScaleType = QComboBox(TechDrawGui__TaskProjGroup)
        self.cmbScaleType.addItem("")
        self.cmbScaleType.addItem("")
        self.cmbScaleType.addItem("")
        self.cmbScaleType.setObjectName(u"cmbScaleType")

        self.horizontalLayout_5.addWidget(self.cmbScaleType)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.sbScaleNum = QSpinBox(TechDrawGui__TaskProjGroup)
        self.sbScaleNum.setObjectName(u"sbScaleNum")
        self.sbScaleNum.setKeyboardTracking(False)
        self.sbScaleNum.setMinimum(1)
        self.sbScaleNum.setValue(1)

        self.horizontalLayout_5.addWidget(self.sbScaleNum)

        self.label_4 = QLabel(TechDrawGui__TaskProjGroup)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setText(u":")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.sbScaleDen = QSpinBox(TechDrawGui__TaskProjGroup)
        self.sbScaleDen.setObjectName(u"sbScaleDen")
        self.sbScaleDen.setKeyboardTracking(False)
        self.sbScaleDen.setMinimum(1)
        self.sbScaleDen.setMaximum(999)
        self.sbScaleDen.setValue(1)

        self.horizontalLayout_5.addWidget(self.sbScaleDen)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.directionGroupbox = QGroupBox(TechDrawGui__TaskProjGroup)
        self.directionGroupbox.setObjectName(u"directionGroupbox")
        self.gridLayout = QGridLayout(self.directionGroupbox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.butCWRotate = QPushButton(self.directionGroupbox)
        self.butCWRotate.setObjectName(u"butCWRotate")
        icon = QIcon()
        icon.addFile(u":/icons/arrow-cw.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.butCWRotate.setIcon(icon)
        self.butCWRotate.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.butCWRotate, 0, 0, 1, 1)

        self.butTopRotate = QPushButton(self.directionGroupbox)
        self.butTopRotate.setObjectName(u"butTopRotate")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.butTopRotate.sizePolicy().hasHeightForWidth())
        self.butTopRotate.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/arrow-up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.butTopRotate.setIcon(icon1)
        self.butTopRotate.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.butTopRotate, 0, 1, 1, 1)

        self.butCCWRotate = QPushButton(self.directionGroupbox)
        self.butCCWRotate.setObjectName(u"butCCWRotate")
        icon2 = QIcon()
        icon2.addFile(u":/icons/arrow-ccw.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.butCCWRotate.setIcon(icon2)
        self.butCCWRotate.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.butCCWRotate, 0, 2, 1, 1)

        self.butLeftRotate = QPushButton(self.directionGroupbox)
        self.butLeftRotate.setObjectName(u"butLeftRotate")
        icon3 = QIcon()
        icon3.addFile(u":/icons/arrow-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.butLeftRotate.setIcon(icon3)
        self.butLeftRotate.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.butLeftRotate, 1, 0, 1, 1)

        self.lePrimary = QPushButton(self.directionGroupbox)
        self.lePrimary.setObjectName(u"lePrimary")
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.lePrimary.setFont(font)

        self.gridLayout.addWidget(self.lePrimary, 1, 1, 1, 1)

        self.butRightRotate = QPushButton(self.directionGroupbox)
        self.butRightRotate.setObjectName(u"butRightRotate")
        icon4 = QIcon()
        icon4.addFile(u":/icons/arrow-right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.butRightRotate.setIcon(icon4)
        self.butRightRotate.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.butRightRotate, 1, 2, 1, 1)

        self.butFront = QPushButton(self.directionGroupbox)
        self.butFront.setObjectName(u"butFront")
        icon5 = QIcon()
        icon5.addFile(u":/icons/TechDraw_ProjFront.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.butFront.setIcon(icon5)
        self.butFront.setIconSize(QSize(24, 24))
        self.butFront.setCheckable(True)
        self.butFront.setChecked(True)
        self.butFront.setAutoExclusive(True)

        self.gridLayout.addWidget(self.butFront, 2, 0, 1, 1)

        self.butDownRotate = QPushButton(self.directionGroupbox)
        self.butDownRotate.setObjectName(u"butDownRotate")
        icon6 = QIcon()
        icon6.addFile(u":/icons/arrow-down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.butDownRotate.setIcon(icon6)
        self.butDownRotate.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.butDownRotate, 2, 1, 1, 1)

        self.butCam = QPushButton(self.directionGroupbox)
        self.butCam.setObjectName(u"butCam")
        icon7 = QIcon()
        icon7.addFile(u":/icons/TechDraw_CameraOrientation.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.butCam.setIcon(icon7)
        self.butCam.setIconSize(QSize(24, 24))
        self.butCam.setCheckable(True)
        self.butCam.setAutoExclusive(True)

        self.gridLayout.addWidget(self.butCam, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.directionGroupbox)

        self.secondaryProjGroupbox = QGroupBox(TechDrawGui__TaskProjGroup)
        self.secondaryProjGroupbox.setObjectName(u"secondaryProjGroupbox")
        self.gridLayout_2 = QGridLayout(self.secondaryProjGroupbox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.chkView0 = QCheckBox(self.secondaryProjGroupbox)
        self.chkView0.setObjectName(u"chkView0")
        self.chkView0.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 24px;\n"
"height: 24px;\n"
"}\n"
"")
        self.chkView0.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.chkView0, 2, 1, 1, 1)

        self.chkView1 = QCheckBox(self.secondaryProjGroupbox)
        self.chkView1.setObjectName(u"chkView1")
        self.chkView1.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 24px;\n"
"height: 24px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.chkView1, 2, 2, 1, 1)

        self.chkView2 = QCheckBox(self.secondaryProjGroupbox)
        self.chkView2.setObjectName(u"chkView2")
        self.chkView2.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 24px;\n"
"height: 24px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.chkView2, 2, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.chkView3 = QCheckBox(self.secondaryProjGroupbox)
        self.chkView3.setObjectName(u"chkView3")
        self.chkView3.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 24px;\n"
"height: 24px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.chkView3, 3, 1, 1, 1)

        self.chkView4 = QCheckBox(self.secondaryProjGroupbox)
        self.chkView4.setObjectName(u"chkView4")
        self.chkView4.setEnabled(False)
        self.chkView4.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 24px;\n"
"height: 24px;\n"
"}\n"
"")
        self.chkView4.setChecked(True)

        self.gridLayout_2.addWidget(self.chkView4, 3, 2, 1, 1)

        self.chkView5 = QCheckBox(self.secondaryProjGroupbox)
        self.chkView5.setObjectName(u"chkView5")
        self.chkView5.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 24px;\n"
"height: 24px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.chkView5, 3, 3, 1, 1)

        self.chkView6 = QCheckBox(self.secondaryProjGroupbox)
        self.chkView6.setObjectName(u"chkView6")
        self.chkView6.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 24px;\n"
"height: 24px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.chkView6, 3, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 5, 1, 1)

        self.chkView7 = QCheckBox(self.secondaryProjGroupbox)
        self.chkView7.setObjectName(u"chkView7")
        self.chkView7.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 24px;\n"
"height: 24px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.chkView7, 5, 1, 1, 1)

        self.chkView8 = QCheckBox(self.secondaryProjGroupbox)
        self.chkView8.setObjectName(u"chkView8")
        self.chkView8.setEnabled(True)
        self.chkView8.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 24px;\n"
"height: 24px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.chkView8, 5, 2, 1, 1)

        self.chkView9 = QCheckBox(self.secondaryProjGroupbox)
        self.chkView9.setObjectName(u"chkView9")
        self.chkView9.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 24px;\n"
"height: 24px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.chkView9, 5, 3, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.secondaryProjGroupbox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.projection = QComboBox(self.secondaryProjGroupbox)
        self.projection.addItem("")
        self.projection.addItem("")
        self.projection.addItem("")
        self.projection.setObjectName(u"projection")

        self.horizontalLayout_3.addWidget(self.projection)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 6, 0, 1, 6)

        self.cbAutoDistribute = QCheckBox(self.secondaryProjGroupbox)
        self.cbAutoDistribute.setObjectName(u"cbAutoDistribute")

        self.gridLayout_2.addWidget(self.cbAutoDistribute, 7, 0, 1, 6)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_10 = QLabel(self.secondaryProjGroupbox)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_10, 0, 1, 1, 1)

        self.sbXSpacing = Gui_QuantitySpinBox(self.secondaryProjGroupbox)
        self.sbXSpacing.setObjectName(u"sbXSpacing")
        sizePolicy2.setHeightForWidth(self.sbXSpacing.sizePolicy().hasHeightForWidth())
        self.sbXSpacing.setSizePolicy(sizePolicy2)
        self.sbXSpacing.setMinimumSize(QSize(150, 22))
        self.sbXSpacing.setKeyboardTracking(False)
        self.sbXSpacing.setProperty(u"unit", u"")
        self.sbXSpacing.setMinimum(0.000000000000000)

        self.gridLayout_3.addWidget(self.sbXSpacing, 0, 2, 1, 1)

        self.label_11 = QLabel(self.secondaryProjGroupbox)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 2)

        self.sbYSpacing = Gui_QuantitySpinBox(self.secondaryProjGroupbox)
        self.sbYSpacing.setObjectName(u"sbYSpacing")
        sizePolicy2.setHeightForWidth(self.sbYSpacing.sizePolicy().hasHeightForWidth())
        self.sbYSpacing.setSizePolicy(sizePolicy2)
        self.sbYSpacing.setMinimumSize(QSize(150, 22))
        self.sbYSpacing.setKeyboardTracking(False)
        self.sbYSpacing.setProperty(u"unit", u"")
        self.sbYSpacing.setMinimum(0.000000000000000)

        self.gridLayout_3.addWidget(self.sbYSpacing, 1, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 8, 0, 1, 6)


        self.verticalLayout.addWidget(self.secondaryProjGroupbox)


        self.retranslateUi(TechDrawGui__TaskProjGroup)
        self.cbAutoDistribute.clicked["bool"].connect(self.sbXSpacing.setEnabled)
        self.cbAutoDistribute.clicked["bool"].connect(self.sbYSpacing.setEnabled)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskProjGroup)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskProjGroup):
        TechDrawGui__TaskProjGroup.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Projection Group", None))
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Scale", None))
        self.cmbScaleType.setItemText(0, QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Page", None))
        self.cmbScaleType.setItemText(1, QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Automatic", None))
        self.cmbScaleType.setItemText(2, QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Custom", None))

#if QT_CONFIG(tooltip)
        self.cmbScaleType.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Scale Page/Auto/Custom", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sbScaleNum.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Scale numerator", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sbScaleDen.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Scale denominator", None))
#endif // QT_CONFIG(tooltip)
        self.directionGroupbox.setTitle(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Direction", None))
#if QT_CONFIG(tooltip)
        self.butCWRotate.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Spin clockwise", None))
#endif // QT_CONFIG(tooltip)
        self.butCWRotate.setText("")
#if QT_CONFIG(tooltip)
        self.butTopRotate.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Rotate up", None))
#endif // QT_CONFIG(tooltip)
        self.butTopRotate.setText("")
#if QT_CONFIG(tooltip)
        self.butCCWRotate.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Spin counter-clockwise", None))
#endif // QT_CONFIG(tooltip)
        self.butCCWRotate.setText("")
#if QT_CONFIG(tooltip)
        self.butLeftRotate.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Rotate left", None))
#endif // QT_CONFIG(tooltip)
        self.butLeftRotate.setText("")
#if QT_CONFIG(tooltip)
        self.lePrimary.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Current primary view direction", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.butRightRotate.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Rotate right", None))
#endif // QT_CONFIG(tooltip)
        self.butRightRotate.setText("")
#if QT_CONFIG(tooltip)
        self.butFront.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Sets the document front view as primary direction", None))
#endif // QT_CONFIG(tooltip)
        self.butFront.setText("")
#if QT_CONFIG(tooltip)
        self.butDownRotate.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Rotate down", None))
#endif // QT_CONFIG(tooltip)
        self.butDownRotate.setText("")
#if QT_CONFIG(tooltip)
        self.butCam.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Sets the direction of the camera, or selected face if any, as the primary direction", None))
#endif // QT_CONFIG(tooltip)
        self.butCam.setText("")
        self.secondaryProjGroupbox.setTitle(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Secondary Projections", None))
#if QT_CONFIG(tooltip)
        self.chkView0.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"LeftFrontTop", None))
#endif // QT_CONFIG(tooltip)
        self.chkView0.setText("")
#if QT_CONFIG(tooltip)
        self.chkView1.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Top", None))
#endif // QT_CONFIG(tooltip)
        self.chkView1.setText("")
#if QT_CONFIG(tooltip)
        self.chkView2.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"RightFrontTop", None))
#endif // QT_CONFIG(tooltip)
        self.chkView2.setText("")
#if QT_CONFIG(tooltip)
        self.chkView3.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Left", None))
#endif // QT_CONFIG(tooltip)
        self.chkView3.setText("")
#if QT_CONFIG(tooltip)
        self.chkView4.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Primary", None))
#endif // QT_CONFIG(tooltip)
        self.chkView4.setText("")
#if QT_CONFIG(tooltip)
        self.chkView5.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Right", None))
#endif // QT_CONFIG(tooltip)
        self.chkView5.setText("")
#if QT_CONFIG(tooltip)
        self.chkView6.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Rear", None))
#endif // QT_CONFIG(tooltip)
        self.chkView6.setText("")
#if QT_CONFIG(tooltip)
        self.chkView7.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"LeftFrontBottom", None))
#endif // QT_CONFIG(tooltip)
        self.chkView7.setText("")
#if QT_CONFIG(tooltip)
        self.chkView8.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Bottom", None))
#endif // QT_CONFIG(tooltip)
        self.chkView8.setText("")
#if QT_CONFIG(tooltip)
        self.chkView9.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"RightFrontBottom", None))
#endif // QT_CONFIG(tooltip)
        self.chkView9.setText("")
        self.label_7.setText(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Projection", None))
        self.projection.setItemText(0, QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"First angle", None))
        self.projection.setItemText(1, QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Third angle", None))
        self.projection.setItemText(2, QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Page", None))

#if QT_CONFIG(tooltip)
        self.projection.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"First or third angle", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cbAutoDistribute.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Distributes projections automatically\n"
"using the given X/Y spacings", None))
#endif // QT_CONFIG(tooltip)
        self.cbAutoDistribute.setText(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Auto distribute", None))
        self.label_10.setText(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"X spacing", None))
#if QT_CONFIG(tooltip)
        self.sbXSpacing.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Horizontal space between borders of projections", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Y spacing", None))
#if QT_CONFIG(tooltip)
        self.sbYSpacing.setToolTip(QCoreApplication.translate("TechDrawGui::TaskProjGroup", u"Vertical space between borders of projections", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

