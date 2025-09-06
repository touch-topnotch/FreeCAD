# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskHatch.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskHatch(object):
    def setupUi(self, TechDrawGui__TaskHatch):
        if not TechDrawGui__TaskHatch.objectName():
            TechDrawGui__TaskHatch.setObjectName(u"TechDrawGui__TaskHatch")
        TechDrawGui__TaskHatch.resize(398, 244)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskHatch.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskHatch.setSizePolicy(sizePolicy)
        TechDrawGui__TaskHatch.setMinimumSize(QSize(250, 0))
        self.verticalLayout_2 = QVBoxLayout(TechDrawGui__TaskHatch)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(TechDrawGui__TaskHatch)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.fcFile = Gui_FileChooser(self.groupBox)
        self.fcFile.setObjectName(u"fcFile")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fcFile.sizePolicy().hasHeightForWidth())
        self.fcFile.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.fcFile, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sbScale = Gui_QuantitySpinBox(self.groupBox)
        self.sbScale.setObjectName(u"sbScale")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sbScale.sizePolicy().hasHeightForWidth())
        self.sbScale.setSizePolicy(sizePolicy3)
        self.sbScale.setMinimumSize(QSize(0, 26))
        self.sbScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbScale.setKeyboardTracking(False)
        self.sbScale.setMinimum(0.001000000000000)
        self.sbScale.setSingleStep(0.100000000000000)
        self.sbScale.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.sbScale, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.ccColor = Gui_ColorButton(self.groupBox)
        self.ccColor.setObjectName(u"ccColor")
        sizePolicy3.setHeightForWidth(self.ccColor.sizePolicy().hasHeightForWidth())
        self.ccColor.setSizePolicy(sizePolicy3)
        self.ccColor.setMinimumSize(QSize(0, 26))

        self.gridLayout_3.addWidget(self.ccColor, 2, 1, 1, 1)

        self.dsbRotation = QDoubleSpinBox(self.groupBox)
        self.dsbRotation.setObjectName(u"dsbRotation")
        self.dsbRotation.setWrapping(True)
        self.dsbRotation.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbRotation.setMinimum(-360.000000000000000)
        self.dsbRotation.setMaximum(360.000000000000000)

        self.gridLayout_3.addWidget(self.dsbRotation, 3, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.dsbOffsetX = QDoubleSpinBox(self.groupBox)
        self.dsbOffsetX.setObjectName(u"dsbOffsetX")
        self.dsbOffsetX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.dsbOffsetX, 4, 1, 1, 1)

        self.dsbOffsetY = QDoubleSpinBox(self.groupBox)
        self.dsbOffsetY.setObjectName(u"dsbOffsetY")
        self.dsbOffsetY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.dsbOffsetY, 5, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(TechDrawGui__TaskHatch)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskHatch)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskHatch):
        TechDrawGui__TaskHatch.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskHatch", u"Apply Geometric Hatch", None))
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("TechDrawGui::TaskHatch", u"Select an SVG or bitmap file", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("TechDrawGui::TaskHatch", u"Pattern Parameters", None))
#if QT_CONFIG(tooltip)
        self.fcFile.setToolTip(QCoreApplication.translate("TechDrawGui::TaskHatch", u"Choose an SVG or bitmap file as a pattern", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskHatch", u"Pattern file", None))
#if QT_CONFIG(tooltip)
        self.sbScale.setToolTip(QCoreApplication.translate("TechDrawGui::TaskHatch", u"Enlarges/shrinks the pattern (SVG only)", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::TaskHatch", u"SVG line color", None))
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::TaskHatch", u"Offset X", None))
#if QT_CONFIG(tooltip)
        self.ccColor.setToolTip(QCoreApplication.translate("TechDrawGui::TaskHatch", u"Color of pattern lines (SVG only)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dsbRotation.setToolTip(QCoreApplication.translate("TechDrawGui::TaskHatch", u"Rotate the pattern (degrees)", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::TaskHatch", u"SVG pattern scale", None))
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::TaskHatch", u"Rotation", None))
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::TaskHatch", u"Offset Y", None))
    # retranslateUi

