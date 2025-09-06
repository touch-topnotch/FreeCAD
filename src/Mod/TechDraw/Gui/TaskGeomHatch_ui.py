# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskGeomHatch.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskGeomHatch(object):
    def setupUi(self, TechDrawGui__TaskGeomHatch):
        if not TechDrawGui__TaskGeomHatch.objectName():
            TechDrawGui__TaskGeomHatch.setObjectName(u"TechDrawGui__TaskGeomHatch")
        TechDrawGui__TaskGeomHatch.resize(385, 314)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskGeomHatch.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskGeomHatch.setSizePolicy(sizePolicy)
        TechDrawGui__TaskGeomHatch.setMinimumSize(QSize(250, 0))
        self.verticalLayout_2 = QVBoxLayout(TechDrawGui__TaskGeomHatch)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(TechDrawGui__TaskGeomHatch)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.fcFile = Gui_FileChooser(self.groupBox)
        self.fcFile.setObjectName(u"fcFile")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fcFile.sizePolicy().hasHeightForWidth())
        self.fcFile.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.fcFile, 0, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)

        self.ccColor = Gui_ColorButton(self.groupBox)
        self.ccColor.setObjectName(u"ccColor")
        self.ccColor.setMinimumSize(QSize(0, 22))

        self.gridLayout_2.addWidget(self.ccColor, 3, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)

        self.cbName = QComboBox(self.groupBox)
        self.cbName.setObjectName(u"cbName")
        self.cbName.setMinimumSize(QSize(0, 22))

        self.gridLayout_2.addWidget(self.cbName, 0, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.dsbRotation = QDoubleSpinBox(self.groupBox)
        self.dsbRotation.setObjectName(u"dsbRotation")
        self.dsbRotation.setWrapping(True)
        self.dsbRotation.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbRotation.setMinimum(-360.000000000000000)
        self.dsbRotation.setMaximum(360.000000000000000)

        self.gridLayout_2.addWidget(self.dsbRotation, 4, 2, 1, 1)

        self.sbWeight = Gui_QuantitySpinBox(self.groupBox)
        self.sbWeight.setObjectName(u"sbWeight")
        self.sbWeight.setMinimumSize(QSize(0, 22))
        self.sbWeight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbWeight.setKeyboardTracking(False)
        self.sbWeight.setMinimum(0.001000000000000)
        self.sbWeight.setSingleStep(0.100000000000000)
        self.sbWeight.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.sbWeight, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.sbScale = Gui_QuantitySpinBox(self.groupBox)
        self.sbScale.setObjectName(u"sbScale")
        self.sbScale.setMinimumSize(QSize(0, 22))
        self.sbScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbScale.setKeyboardTracking(False)
        self.sbScale.setMinimum(0.100000000000000)
        self.sbScale.setSingleStep(0.100000000000000)
        self.sbScale.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.sbScale, 1, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)

        self.dsbOffsetX = QDoubleSpinBox(self.groupBox)
        self.dsbOffsetX.setObjectName(u"dsbOffsetX")
        self.dsbOffsetX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.dsbOffsetX, 5, 2, 1, 1)

        self.dsbOffsetY = QDoubleSpinBox(self.groupBox)
        self.dsbOffsetY.setObjectName(u"dsbOffsetY")
        self.dsbOffsetY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.dsbOffsetY, 6, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(TechDrawGui__TaskGeomHatch)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskGeomHatch)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskGeomHatch):
        TechDrawGui__TaskGeomHatch.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Geometric Hatch", None))
        self.groupBox.setTitle(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Define Pattern", None))
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Pattern file", None))
#if QT_CONFIG(tooltip)
        self.fcFile.setToolTip(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"The PAT file containing the pattern", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Pattern scale", None))
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Rotation", None))
#if QT_CONFIG(tooltip)
        self.ccColor.setToolTip(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Color of pattern lines", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Pattern name", None))
        self.label_7.setText(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Offset X", None))
#if QT_CONFIG(tooltip)
        self.cbName.setToolTip(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Name of pattern within file", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Line width", None))
#if QT_CONFIG(tooltip)
        self.sbWeight.setToolTip(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Thickness of the lines within the pattern", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Line color", None))
#if QT_CONFIG(tooltip)
        self.sbScale.setToolTip(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Enlarges/shrinks the pattern", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("TechDrawGui::TaskGeomHatch", u"Offset Y", None))
    # retranslateUi

