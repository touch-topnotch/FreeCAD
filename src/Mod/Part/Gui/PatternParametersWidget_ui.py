# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PatternParametersWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_PartGui_PatternParametersWidget(object):
    def setupUi(self, PartGui__PatternParametersWidget):
        if not PartGui__PatternParametersWidget.objectName():
            PartGui__PatternParametersWidget.setObjectName(u"PartGui__PatternParametersWidget")
        PartGui__PatternParametersWidget.resize(270, 200)
        self.generalLayout = QVBoxLayout(PartGui__PatternParametersWidget)
        self.generalLayout.setObjectName(u"generalLayout")
        self.generalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(PartGui__PatternParametersWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.mainLayout = QVBoxLayout(self.groupBox)
        self.mainLayout.setObjectName(u"mainLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.PushButtonReverse = QToolButton(self.groupBox)
        self.PushButtonReverse.setObjectName(u"PushButtonReverse")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButtonReverse.sizePolicy().hasHeightForWidth())
        self.PushButtonReverse.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/button_sort.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PushButtonReverse.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.PushButtonReverse)

        self.comboDirection = QComboBox(self.groupBox)
        self.comboDirection.setObjectName(u"comboDirection")

        self.horizontalLayout_3.addWidget(self.comboDirection)


        self.mainLayout.addLayout(self.horizontalLayout_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelMode = QLabel(self.groupBox)
        self.labelMode.setObjectName(u"labelMode")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelMode)

        self.comboMode = QComboBox(self.groupBox)
        self.comboMode.addItem("")
        self.comboMode.addItem("")
        self.comboMode.setObjectName(u"comboMode")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboMode)

        self.labelLength = QLabel(self.groupBox)
        self.labelLength.setObjectName(u"labelLength")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelLength)

        self.spinExtent = Gui_QuantitySpinBox(self.groupBox)
        self.spinExtent.setObjectName(u"spinExtent")
        self.spinExtent.setProperty(u"keyboardTracking", False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinExtent)

        self.labelOffset = QLabel(self.groupBox)
        self.labelOffset.setObjectName(u"labelOffset")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelOffset)

        self.spacingControlsWidget = QWidget(self.groupBox)
        self.spacingControlsWidget.setObjectName(u"spacingControlsWidget")
        self.spacingControlsLayout = QHBoxLayout(self.spacingControlsWidget)
        self.spacingControlsLayout.setSpacing(3)
        self.spacingControlsLayout.setObjectName(u"spacingControlsLayout")
        self.spacingControlsLayout.setContentsMargins(0, 0, 0, 0)
        self.spinSpacing = Gui_QuantitySpinBox(self.spacingControlsWidget)
        self.spinSpacing.setObjectName(u"spinSpacing")
        self.spinSpacing.setProperty(u"keyboardTracking", False)

        self.spacingControlsLayout.addWidget(self.spinSpacing)

        self.addSpacingButton = QToolButton(self.spacingControlsWidget)
        self.addSpacingButton.setObjectName(u"addSpacingButton")
        sizePolicy.setHeightForWidth(self.addSpacingButton.sizePolicy().hasHeightForWidth())
        self.addSpacingButton.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/icons/list-add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addSpacingButton.setIcon(icon1)

        self.spacingControlsLayout.addWidget(self.addSpacingButton)


        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spacingControlsWidget)

        self.labelOccurrences = QLabel(self.groupBox)
        self.labelOccurrences.setObjectName(u"labelOccurrences")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelOccurrences)

        self.spinOccurrences = Gui_UIntSpinBox(self.groupBox)
        self.spinOccurrences.setObjectName(u"spinOccurrences")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.spinOccurrences)


        self.mainLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer)


        self.generalLayout.addWidget(self.groupBox)


        self.retranslateUi(PartGui__PatternParametersWidget)

        QMetaObject.connectSlotsByName(PartGui__PatternParametersWidget)
    # setupUi

    def retranslateUi(self, PartGui__PatternParametersWidget):
        self.groupBox.setTitle(QCoreApplication.translate("PartGui::PatternParametersWidget", u"Direction", None))
#if QT_CONFIG(tooltip)
        self.PushButtonReverse.setToolTip(QCoreApplication.translate("PartGui::PatternParametersWidget", u"Reverse the direction of the pattern.", None))
#endif // QT_CONFIG(tooltip)
        self.labelMode.setText(QCoreApplication.translate("PartGui::PatternParametersWidget", u"Mode", None))
        self.comboMode.setItemText(0, QCoreApplication.translate("PartGui::PatternParametersWidget", u"Extent", None))
        self.comboMode.setItemText(1, QCoreApplication.translate("PartGui::PatternParametersWidget", u"Spacing", None))

        self.labelLength.setText(QCoreApplication.translate("PartGui::PatternParametersWidget", u"Length", None))
        self.labelOffset.setText(QCoreApplication.translate("PartGui::PatternParametersWidget", u"Spacing", None))
#if QT_CONFIG(tooltip)
        self.addSpacingButton.setToolTip(QCoreApplication.translate("PartGui::PatternParametersWidget", u"Add spacing to create spacing patterns.", None))
#endif // QT_CONFIG(tooltip)
        self.addSpacingButton.setText("")
        self.labelOccurrences.setText(QCoreApplication.translate("PartGui::PatternParametersWidget", u"Occurrences", None))
        pass
    # retranslateUi

