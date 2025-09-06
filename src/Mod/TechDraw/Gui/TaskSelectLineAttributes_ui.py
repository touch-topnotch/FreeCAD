# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskSelectLineAttributes.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QDoubleSpinBox,
    QGridLayout, QLabel, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskSelectLineAttributes(object):
    def setupUi(self, TechDrawGui__TaskSelectLineAttributes):
        if not TechDrawGui__TaskSelectLineAttributes.objectName():
            TechDrawGui__TaskSelectLineAttributes.setObjectName(u"TechDrawGui__TaskSelectLineAttributes")
        TechDrawGui__TaskSelectLineAttributes.resize(424, 308)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskSelectLineAttributes.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskSelectLineAttributes.setSizePolicy(sizePolicy)
        TechDrawGui__TaskSelectLineAttributes.setMinimumSize(QSize(250, 0))
        self.verticalLayout = QVBoxLayout(TechDrawGui__TaskSelectLineAttributes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineStyles = QGridLayout()
        self.lineStyles.setObjectName(u"lineStyles")
        self.label_styles = QLabel(TechDrawGui__TaskSelectLineAttributes)
        self.label_styles.setObjectName(u"label_styles")

        self.lineStyles.addWidget(self.label_styles, 0, 0, 1, 1)

        self.cbLineStyle = QComboBox(TechDrawGui__TaskSelectLineAttributes)
        self.cbLineStyle.setObjectName(u"cbLineStyle")

        self.lineStyles.addWidget(self.cbLineStyle, 0, 1, 1, 1)

        self.lineStyles.setColumnStretch(0, 1)
        self.lineStyles.setColumnStretch(1, 2)

        self.verticalLayout.addLayout(self.lineStyles)

        self.lineWidth = QGridLayout()
        self.lineWidth.setObjectName(u"lineWidth")
        self.label_width = QLabel(TechDrawGui__TaskSelectLineAttributes)
        self.label_width.setObjectName(u"label_width")

        self.lineWidth.addWidget(self.label_width, 0, 0, 1, 1)

        self.rbThin = QRadioButton(TechDrawGui__TaskSelectLineAttributes)
        self.bgLineWidth = QButtonGroup(TechDrawGui__TaskSelectLineAttributes)
        self.bgLineWidth.setObjectName(u"bgLineWidth")
        self.bgLineWidth.setExclusive(True)
        self.bgLineWidth.addButton(self.rbThin)
        self.rbThin.setObjectName(u"rbThin")
        self.rbThin.setAutoExclusive(True)

        self.lineWidth.addWidget(self.rbThin, 1, 0, 1, 1)

        self.rbMiddle = QRadioButton(TechDrawGui__TaskSelectLineAttributes)
        self.bgLineWidth.addButton(self.rbMiddle)
        self.rbMiddle.setObjectName(u"rbMiddle")
        self.rbMiddle.setChecked(True)
        self.rbMiddle.setAutoExclusive(True)

        self.lineWidth.addWidget(self.rbMiddle, 2, 0, 1, 1)

        self.rbThick = QRadioButton(TechDrawGui__TaskSelectLineAttributes)
        self.bgLineWidth.addButton(self.rbThick)
        self.rbThick.setObjectName(u"rbThick")
        self.rbThick.setAutoExclusive(True)

        self.lineWidth.addWidget(self.rbThick, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.lineWidth)

        self.lineColors = QGridLayout()
        self.lineColors.setObjectName(u"lineColors")
        self.cbColor = Gui_PrefColorButton(TechDrawGui__TaskSelectLineAttributes)
        self.cbColor.setObjectName(u"cbColor")

        self.lineColors.addWidget(self.cbColor, 0, 1, 1, 1)

        self.label_colors = QLabel(TechDrawGui__TaskSelectLineAttributes)
        self.label_colors.setObjectName(u"label_colors")

        self.lineColors.addWidget(self.label_colors, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.lineColors)

        self.cascadeValues = QGridLayout()
        self.cascadeValues.setObjectName(u"cascadeValues")
        self.cascadeValues.setContentsMargins(0, -1, -1, -1)
        self.label_spacing = QLabel(TechDrawGui__TaskSelectLineAttributes)
        self.label_spacing.setObjectName(u"label_spacing")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_spacing.sizePolicy().hasHeightForWidth())
        self.label_spacing.setSizePolicy(sizePolicy1)

        self.cascadeValues.addWidget(self.label_spacing, 0, 0, 1, 1)

        self.sbSpacing = QDoubleSpinBox(TechDrawGui__TaskSelectLineAttributes)
        self.sbSpacing.setObjectName(u"sbSpacing")
        self.sbSpacing.setSingleStep(0.500000000000000)

        self.cascadeValues.addWidget(self.sbSpacing, 0, 1, 1, 1)

        self.label_stretch = QLabel(TechDrawGui__TaskSelectLineAttributes)
        self.label_stretch.setObjectName(u"label_stretch")

        self.cascadeValues.addWidget(self.label_stretch, 1, 0, 1, 1)

        self.sbStretch = QDoubleSpinBox(TechDrawGui__TaskSelectLineAttributes)
        self.sbStretch.setObjectName(u"sbStretch")
        self.sbStretch.setSingleStep(0.500000000000000)

        self.cascadeValues.addWidget(self.sbStretch, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.cascadeValues)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TechDrawGui__TaskSelectLineAttributes)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskSelectLineAttributes)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskSelectLineAttributes):
        TechDrawGui__TaskSelectLineAttributes.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskSelectLineAttributes", u"Line Attributes", None))
        self.label_styles.setText(QCoreApplication.translate("TechDrawGui::TaskSelectLineAttributes", u"Line style", None))
        self.label_width.setText(QCoreApplication.translate("TechDrawGui::TaskSelectLineAttributes", u"Line width", None))
        self.rbThin.setText(QCoreApplication.translate("TechDrawGui::TaskSelectLineAttributes", u"Thin 0,18", None))
        self.rbMiddle.setText(QCoreApplication.translate("TechDrawGui::TaskSelectLineAttributes", u"Middle 0,35", None))
        self.rbThick.setText(QCoreApplication.translate("TechDrawGui::TaskSelectLineAttributes", u"Thick 0,70", None))
        self.label_colors.setText(QCoreApplication.translate("TechDrawGui::TaskSelectLineAttributes", u"Line color", None))
        self.label_spacing.setText(QCoreApplication.translate("TechDrawGui::TaskSelectLineAttributes", u"Cascade spacing", None))
        self.label_stretch.setText(QCoreApplication.translate("TechDrawGui::TaskSelectLineAttributes", u"Delta distance", None))
    # retranslateUi

