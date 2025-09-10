# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpProfileFullEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLabel, QSizePolicy, QSpacerItem,
    QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(446, 597)
        Form.setWindowTitle(u"Form")
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.toolController = QComboBox(self.frame)
        self.toolController.setObjectName(u"toolController")

        self.gridLayout_3.addWidget(self.toolController, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.coolantController = QComboBox(self.frame)
        self.coolantController.setObjectName(u"coolantController")

        self.gridLayout_3.addWidget(self.coolantController, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cutSideLabel = QLabel(self.widget)
        self.cutSideLabel.setObjectName(u"cutSideLabel")

        self.gridLayout.addWidget(self.cutSideLabel, 0, 0, 1, 1)

        self.cutSide = QComboBox(self.widget)
        self.cutSide.addItem("")
        self.cutSide.setObjectName(u"cutSide")

        self.gridLayout.addWidget(self.cutSide, 0, 1, 1, 1)

        self.directionLabel = QLabel(self.widget)
        self.directionLabel.setObjectName(u"directionLabel")

        self.gridLayout.addWidget(self.directionLabel, 1, 0, 1, 1)

        self.direction = QComboBox(self.widget)
        self.direction.addItem("")
        self.direction.setObjectName(u"direction")

        self.gridLayout.addWidget(self.direction, 1, 1, 1, 1)

        self.extraOffsetLabel = QLabel(self.widget)
        self.extraOffsetLabel.setObjectName(u"extraOffsetLabel")

        self.gridLayout.addWidget(self.extraOffsetLabel, 2, 0, 1, 1)

        self.extraOffset = Gui_InputField(self.widget)
        self.extraOffset.setObjectName(u"extraOffset")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extraOffset.sizePolicy().hasHeightForWidth())
        self.extraOffset.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.extraOffset, 2, 1, 1, 1)

        self.numPassesLabel = QLabel(self.widget)
        self.numPassesLabel.setObjectName(u"numPassesLabel")

        self.gridLayout.addWidget(self.numPassesLabel, 3, 0, 1, 1)

        self.numPasses = QSpinBox(self.widget)
        self.numPasses.setObjectName(u"numPasses")
        self.numPasses.setMinimum(1)

        self.gridLayout.addWidget(self.numPasses, 3, 1, 1, 1)

        self.stepoverLabel = QLabel(self.widget)
        self.stepoverLabel.setObjectName(u"stepoverLabel")

        self.gridLayout.addWidget(self.stepoverLabel, 4, 0, 1, 1)

        self.stepover = Gui_InputField(self.widget)
        self.stepover.setObjectName(u"stepover")
        sizePolicy.setHeightForWidth(self.stepover.sizePolicy().hasHeightForWidth())
        self.stepover.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.stepover, 4, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 1, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.useStartPoint = QCheckBox(self.widget_2)
        self.useStartPoint.setObjectName(u"useStartPoint")

        self.gridLayout_2.addWidget(self.useStartPoint, 0, 0, 1, 1)

        self.processHoles = QCheckBox(self.widget_2)
        self.processHoles.setObjectName(u"processHoles")

        self.gridLayout_2.addWidget(self.processHoles, 0, 1, 1, 1)

        self.useCompensation = QCheckBox(self.widget_2)
        self.useCompensation.setObjectName(u"useCompensation")

        self.gridLayout_2.addWidget(self.useCompensation, 1, 0, 1, 1)

        self.processCircles = QCheckBox(self.widget_2)
        self.processCircles.setObjectName(u"processCircles")

        self.gridLayout_2.addWidget(self.processCircles, 1, 1, 1, 1)

        self.processPerimeter = QCheckBox(self.widget_2)
        self.processPerimeter.setObjectName(u"processPerimeter")

        self.gridLayout_2.addWidget(self.processPerimeter, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget_2, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 3, 0, 1, 1)

        QWidget.setTabOrder(self.toolController, self.cutSide)
        QWidget.setTabOrder(self.cutSide, self.direction)
        QWidget.setTabOrder(self.direction, self.extraOffset)
        QWidget.setTabOrder(self.extraOffset, self.useStartPoint)
        QWidget.setTabOrder(self.useStartPoint, self.useCompensation)
        QWidget.setTabOrder(self.useCompensation, self.processHoles)
        QWidget.setTabOrder(self.processHoles, self.processCircles)
        QWidget.setTabOrder(self.processCircles, self.processPerimeter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.label.setText(QCoreApplication.translate("Form", u"Tool Controller", None))
#if QT_CONFIG(tooltip)
        self.toolController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Coolant Mode", None))
#if QT_CONFIG(tooltip)
        self.coolantController.setToolTip(QCoreApplication.translate("Form", u"The tool and its settings to be used for this operation", None))
#endif // QT_CONFIG(tooltip)
        self.cutSideLabel.setText(QCoreApplication.translate("Form", u"Cut Side", None))
        self.cutSide.setItemText(0, QCoreApplication.translate("Form", u"PLACEHOLDER", None))

#if QT_CONFIG(tooltip)
        self.cutSide.setToolTip(QCoreApplication.translate("Form", u"Specify if the profile should be performed inside or outside the base geometry features. This only matters if Use Compensation is checked (the default)", None))
#endif // QT_CONFIG(tooltip)
        self.directionLabel.setText(QCoreApplication.translate("Form", u"Direction", None))
        self.direction.setItemText(0, QCoreApplication.translate("Form", u"PLACEHOLDER", None))

#if QT_CONFIG(tooltip)
        self.direction.setToolTip(QCoreApplication.translate("Form", u"The direction in which the profile is performed, clockwise or counterclockwise", None))
#endif // QT_CONFIG(tooltip)
        self.extraOffsetLabel.setText(QCoreApplication.translate("Form", u"Extra Offset", None))
#if QT_CONFIG(tooltip)
        self.extraOffset.setToolTip(QCoreApplication.translate("Form", u"The amount of extra material left by this operation in relation to the target shape", None))
#endif // QT_CONFIG(tooltip)
        self.numPassesLabel.setText(QCoreApplication.translate("Form", u"Number of Passes", None))
#if QT_CONFIG(tooltip)
        self.numPasses.setToolTip(QCoreApplication.translate("Form", u"The number of passes to do. If more than one, requires a non-zero value for Pass Stepover.", None))
#endif // QT_CONFIG(tooltip)
        self.stepoverLabel.setText(QCoreApplication.translate("Form", u"Pass Stepover", None))
#if QT_CONFIG(tooltip)
        self.stepover.setToolTip(QCoreApplication.translate("Form", u"If doing multiple passes, the extra offset of each additional pass.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.useStartPoint.setToolTip(QCoreApplication.translate("Form", u"Check if this operation should use a starting point", None))
#endif // QT_CONFIG(tooltip)
        self.useStartPoint.setText(QCoreApplication.translate("Form", u"Use Start Point", None))
#if QT_CONFIG(tooltip)
        self.processHoles.setToolTip(QCoreApplication.translate("Form", u"Check if this profile operation should also process holes in the base geometry. Found holes are automatically offset on the opposite cut side and performed in the opposite direction as perimeters. Note that this does not include cylindrical holes, the assumption being that they will get drilled", None))
#endif // QT_CONFIG(tooltip)
        self.processHoles.setText(QCoreApplication.translate("Form", u"Process Holes", None))
#if QT_CONFIG(tooltip)
        self.useCompensation.setToolTip(QCoreApplication.translate("Form", u"If checked, the profile operation is offset by the tool radius. The offset direction is determined by the Cut Side", None))
#endif // QT_CONFIG(tooltip)
        self.useCompensation.setText(QCoreApplication.translate("Form", u"Use Compensation", None))
#if QT_CONFIG(tooltip)
        self.processCircles.setToolTip(QCoreApplication.translate("Form", u"Check if you want this profile operation to also be applied to cylindrical holes, which normally get drilled. This can be useful if no drill of adequate size is available or the number of holes don't warrant a tool change. Note that the cut side and direction is reversed in respect to the specified values", None))
#endif // QT_CONFIG(tooltip)
        self.processCircles.setText(QCoreApplication.translate("Form", u"Process Circles", None))
#if QT_CONFIG(tooltip)
        self.processPerimeter.setToolTip(QCoreApplication.translate("Form", u"Check if this profile operation should also process the outside perimeter of the base geometry shapes", None))
#endif // QT_CONFIG(tooltip)
        self.processPerimeter.setText(QCoreApplication.translate("Form", u"Process Perimeter", None))
        pass
    # retranslateUi

