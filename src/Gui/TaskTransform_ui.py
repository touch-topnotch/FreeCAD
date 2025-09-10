# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskTransform.ui'
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
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_TaskTransformDialog(object):
    def setupUi(self, Gui__TaskTransformDialog):
        if not Gui__TaskTransformDialog.objectName():
            Gui__TaskTransformDialog.setObjectName(u"Gui__TaskTransformDialog")
        Gui__TaskTransformDialog.resize(450, 1012)
        self.gridLayout = QGridLayout(Gui__TaskTransformDialog)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(Gui__TaskTransformDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.positionModeComboBox = QComboBox(Gui__TaskTransformDialog)
        self.positionModeComboBox.addItem("")
        self.positionModeComboBox.addItem("")
        self.positionModeComboBox.setObjectName(u"positionModeComboBox")

        self.horizontalLayout_5.addWidget(self.positionModeComboBox)

        self.horizontalLayout_5.setStretch(1, 1)

        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.alignRotationCheckBox = QCheckBox(Gui__TaskTransformDialog)
        self.alignRotationCheckBox.setObjectName(u"alignRotationCheckBox")

        self.horizontalLayout_4.addWidget(self.alignRotationCheckBox)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.vSpacer = QSpacerItem(20, 41, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.vSpacer, 7, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.positionGroupBox = QGroupBox(Gui__TaskTransformDialog)
        self.positionGroupBox.setObjectName(u"positionGroupBox")
        self.gridLayout1 = QGridLayout(self.positionGroupBox)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
        self.positionStackWidget = QWidget(self.positionGroupBox)
        self.positionStackWidget.setObjectName(u"positionStackWidget")
        self.absolutePositionLayout = QGridLayout(self.positionStackWidget)
        self.absolutePositionLayout.setSpacing(6)
        self.absolutePositionLayout.setContentsMargins(11, 11, 11, 11)
        self.absolutePositionLayout.setObjectName(u"absolutePositionLayout")
        self.absolutePositionLayout.setContentsMargins(0, 0, 0, 0)
        self.zPositionSpinBox = Gui_QuantitySpinBox(self.positionStackWidget)
        self.zPositionSpinBox.setObjectName(u"zPositionSpinBox")

        self.absolutePositionLayout.addWidget(self.zPositionSpinBox, 4, 1, 1, 1)

        self.xPositionSpinBox = Gui_QuantitySpinBox(self.positionStackWidget)
        self.xPositionSpinBox.setObjectName(u"xPositionSpinBox")

        self.absolutePositionLayout.addWidget(self.xPositionSpinBox, 2, 1, 1, 1)

        self.xPositionLabel = QLabel(self.positionStackWidget)
        self.xPositionLabel.setObjectName(u"xPositionLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xPositionLabel.sizePolicy().hasHeightForWidth())
        self.xPositionLabel.setSizePolicy(sizePolicy)

        self.absolutePositionLayout.addWidget(self.xPositionLabel, 2, 0, 1, 1)

        self.yPositionLabel = QLabel(self.positionStackWidget)
        self.yPositionLabel.setObjectName(u"yPositionLabel")
        sizePolicy.setHeightForWidth(self.yPositionLabel.sizePolicy().hasHeightForWidth())
        self.yPositionLabel.setSizePolicy(sizePolicy)

        self.absolutePositionLayout.addWidget(self.yPositionLabel, 3, 0, 1, 1)

        self.zPositionLabel = QLabel(self.positionStackWidget)
        self.zPositionLabel.setObjectName(u"zPositionLabel")
        sizePolicy.setHeightForWidth(self.zPositionLabel.sizePolicy().hasHeightForWidth())
        self.zPositionLabel.setSizePolicy(sizePolicy)

        self.absolutePositionLayout.addWidget(self.zPositionLabel, 4, 0, 1, 1)

        self.yPositionSpinBox = Gui_QuantitySpinBox(self.positionStackWidget)
        self.yPositionSpinBox.setObjectName(u"yPositionSpinBox")

        self.absolutePositionLayout.addWidget(self.yPositionSpinBox, 3, 1, 1, 1)

        self.absolutePositionLayout.setColumnStretch(0, 1)

        self.gridLayout1.addWidget(self.positionStackWidget, 0, 0, 1, 1)

        self.gridLayout1.setColumnMinimumWidth(0, 100)

        self.gridLayout.addWidget(self.positionGroupBox, 4, 0, 1, 1)

        self.groupBox = QGroupBox(Gui__TaskTransformDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.alignToOtherObjectButton = QPushButton(self.groupBox)
        self.alignToOtherObjectButton.setObjectName(u"alignToOtherObjectButton")

        self.verticalLayout.addWidget(self.alignToOtherObjectButton)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.flipPartButton = QPushButton(self.groupBox)
        self.flipPartButton.setObjectName(u"flipPartButton")

        self.verticalLayout.addWidget(self.flipPartButton)


        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 1)

        self.transformOriginGroupBox = QGroupBox(Gui__TaskTransformDialog)
        self.transformOriginGroupBox.setObjectName(u"transformOriginGroupBox")
        self.transformOriginLayout = QGridLayout(self.transformOriginGroupBox)
        self.transformOriginLayout.setSpacing(6)
        self.transformOriginLayout.setContentsMargins(11, 11, 11, 11)
        self.transformOriginLayout.setObjectName(u"transformOriginLayout")
        self.transformOriginLayout.setContentsMargins(9, 9, 9, 9)
        self.placementComboBox = QComboBox(self.transformOriginGroupBox)
        self.placementComboBox.setObjectName(u"placementComboBox")

        self.transformOriginLayout.addWidget(self.placementComboBox, 0, 1, 1, 1)

        self.snappingLabel = QLabel(self.transformOriginGroupBox)
        self.snappingLabel.setObjectName(u"snappingLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.snappingLabel.sizePolicy().hasHeightForWidth())
        self.snappingLabel.setSizePolicy(sizePolicy1)
        self.snappingLabel.setFrameShape(QFrame.Shape.NoFrame)
        self.snappingLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.transformOriginLayout.addWidget(self.snappingLabel, 5, 0, 1, 2)

        self.translationIncrementLabel = QLabel(self.transformOriginGroupBox)
        self.translationIncrementLabel.setObjectName(u"translationIncrementLabel")
        sizePolicy.setHeightForWidth(self.translationIncrementLabel.sizePolicy().hasHeightForWidth())
        self.translationIncrementLabel.setSizePolicy(sizePolicy)

        self.transformOriginLayout.addWidget(self.translationIncrementLabel, 6, 0, 1, 1)

        self.rotationIncrementSpinBox = Gui_QuantitySpinBox(self.transformOriginGroupBox)
        self.rotationIncrementSpinBox.setObjectName(u"rotationIncrementSpinBox")
        self.rotationIncrementSpinBox.setMinimum(0.000000000000000)
        self.rotationIncrementSpinBox.setMaximum(360.000000000000000)
        self.rotationIncrementSpinBox.setValue(5.000000000000000)

        self.transformOriginLayout.addWidget(self.rotationIncrementSpinBox, 7, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.transformOriginLayout.addItem(self.verticalSpacer_4, 4, 0, 1, 2)

        self.referencePickerWidget = QWidget(self.transformOriginGroupBox)
        self.referencePickerWidget.setObjectName(u"referencePickerWidget")
        self.referencePickerLayout = QGridLayout(self.referencePickerWidget)
        self.referencePickerLayout.setSpacing(6)
        self.referencePickerLayout.setContentsMargins(11, 11, 11, 11)
        self.referencePickerLayout.setObjectName(u"referencePickerLayout")
        self.referencePickerLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.referencePickerLayout.setContentsMargins(0, 0, 0, 0)
        self.referenceLabel = QLabel(self.referencePickerWidget)
        self.referenceLabel.setObjectName(u"referenceLabel")
        self.referenceLabel.setMinimumSize(QSize(68, 0))

        self.referencePickerLayout.addWidget(self.referenceLabel, 0, 0, 1, 1)

        self.pickTransformOriginButton = QPushButton(self.referencePickerWidget)
        self.pickTransformOriginButton.setObjectName(u"pickTransformOriginButton")

        self.referencePickerLayout.addWidget(self.pickTransformOriginButton, 1, 1, 1, 1)

        self.referenceLineEdit = QLineEdit(self.referencePickerWidget)
        self.referenceLineEdit.setObjectName(u"referenceLineEdit")
        self.referenceLineEdit.setReadOnly(True)

        self.referencePickerLayout.addWidget(self.referenceLineEdit, 0, 1, 1, 1)

        self.referencePickerLayout.setColumnStretch(1, 1)

        self.transformOriginLayout.addWidget(self.referencePickerWidget, 1, 0, 1, 2)

        self.translationIncrementSpinBox = Gui_QuantitySpinBox(self.transformOriginGroupBox)
        self.translationIncrementSpinBox.setObjectName(u"translationIncrementSpinBox")
        self.translationIncrementSpinBox.setMinimum(0.000000000000000)
        self.translationIncrementSpinBox.setMaximum(2147483647.000000000000000)
        self.translationIncrementSpinBox.setValue(1.000000000000000)

        self.transformOriginLayout.addWidget(self.translationIncrementSpinBox, 6, 1, 1, 1)

        self.label = QLabel(self.transformOriginGroupBox)
        self.label.setObjectName(u"label")

        self.transformOriginLayout.addWidget(self.label, 0, 0, 1, 1)

        self.rotationIncrementLabel = QLabel(self.transformOriginGroupBox)
        self.rotationIncrementLabel.setObjectName(u"rotationIncrementLabel")
        sizePolicy.setHeightForWidth(self.rotationIncrementLabel.sizePolicy().hasHeightForWidth())
        self.rotationIncrementLabel.setSizePolicy(sizePolicy)

        self.transformOriginLayout.addWidget(self.rotationIncrementLabel, 7, 0, 1, 1)


        self.gridLayout.addWidget(self.transformOriginGroupBox, 0, 0, 1, 1)

        self.rotationGroupBox = QGroupBox(Gui__TaskTransformDialog)
        self.rotationGroupBox.setObjectName(u"rotationGroupBox")
        self.gridLayout2 = QGridLayout(self.rotationGroupBox)
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayout2.setContentsMargins(9, 9, 9, 9)
        self.rotationStackWidget = QWidget(self.rotationGroupBox)
        self.rotationStackWidget.setObjectName(u"rotationStackWidget")
        self.absoluteRotationLayout = QGridLayout(self.rotationStackWidget)
        self.absoluteRotationLayout.setSpacing(6)
        self.absoluteRotationLayout.setContentsMargins(11, 11, 11, 11)
        self.absoluteRotationLayout.setObjectName(u"absoluteRotationLayout")
        self.absoluteRotationLayout.setContentsMargins(0, 0, 0, 0)
        self.zRotationSpinBox = Gui_QuantitySpinBox(self.rotationStackWidget)
        self.zRotationSpinBox.setObjectName(u"zRotationSpinBox")

        self.absoluteRotationLayout.addWidget(self.zRotationSpinBox, 2, 1, 1, 1)

        self.yRotationLabel = QLabel(self.rotationStackWidget)
        self.yRotationLabel.setObjectName(u"yRotationLabel")
        sizePolicy.setHeightForWidth(self.yRotationLabel.sizePolicy().hasHeightForWidth())
        self.yRotationLabel.setSizePolicy(sizePolicy)

        self.absoluteRotationLayout.addWidget(self.yRotationLabel, 1, 0, 1, 1)

        self.zRotationLabel = QLabel(self.rotationStackWidget)
        self.zRotationLabel.setObjectName(u"zRotationLabel")
        sizePolicy.setHeightForWidth(self.zRotationLabel.sizePolicy().hasHeightForWidth())
        self.zRotationLabel.setSizePolicy(sizePolicy)

        self.absoluteRotationLayout.addWidget(self.zRotationLabel, 2, 0, 1, 1)

        self.yRotationSpinBox = Gui_QuantitySpinBox(self.rotationStackWidget)
        self.yRotationSpinBox.setObjectName(u"yRotationSpinBox")

        self.absoluteRotationLayout.addWidget(self.yRotationSpinBox, 1, 1, 1, 1)

        self.xRotationSpinBox = Gui_QuantitySpinBox(self.rotationStackWidget)
        self.xRotationSpinBox.setObjectName(u"xRotationSpinBox")

        self.absoluteRotationLayout.addWidget(self.xRotationSpinBox, 0, 1, 1, 1)

        self.xRotationLabel = QLabel(self.rotationStackWidget)
        self.xRotationLabel.setObjectName(u"xRotationLabel")
        sizePolicy.setHeightForWidth(self.xRotationLabel.sizePolicy().hasHeightForWidth())
        self.xRotationLabel.setSizePolicy(sizePolicy)

        self.absoluteRotationLayout.addWidget(self.xRotationLabel, 0, 0, 1, 1)

        self.absoluteRotationLayout.setColumnStretch(0, 1)

        self.gridLayout2.addWidget(self.rotationStackWidget, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.rotationGroupBox, 5, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.positionModeComboBox)
        self.xPositionLabel.setBuddy(self.xPositionSpinBox)
        self.yPositionLabel.setBuddy(self.yPositionSpinBox)
        self.zPositionLabel.setBuddy(self.zPositionSpinBox)
        self.translationIncrementLabel.setBuddy(self.translationIncrementSpinBox)
        self.referenceLabel.setBuddy(self.referenceLineEdit)
        self.label.setBuddy(self.placementComboBox)
        self.rotationIncrementLabel.setBuddy(self.rotationIncrementSpinBox)
        self.yRotationLabel.setBuddy(self.yRotationSpinBox)
        self.zRotationLabel.setBuddy(self.zRotationSpinBox)
        self.xRotationLabel.setBuddy(self.xRotationSpinBox)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.placementComboBox, self.referenceLineEdit)
        QWidget.setTabOrder(self.referenceLineEdit, self.pickTransformOriginButton)
        QWidget.setTabOrder(self.pickTransformOriginButton, self.translationIncrementSpinBox)
        QWidget.setTabOrder(self.translationIncrementSpinBox, self.rotationIncrementSpinBox)
        QWidget.setTabOrder(self.rotationIncrementSpinBox, self.positionModeComboBox)
        QWidget.setTabOrder(self.positionModeComboBox, self.alignRotationCheckBox)
        QWidget.setTabOrder(self.alignRotationCheckBox, self.xPositionSpinBox)
        QWidget.setTabOrder(self.xPositionSpinBox, self.yPositionSpinBox)
        QWidget.setTabOrder(self.yPositionSpinBox, self.zPositionSpinBox)
        QWidget.setTabOrder(self.zPositionSpinBox, self.xRotationSpinBox)
        QWidget.setTabOrder(self.xRotationSpinBox, self.yRotationSpinBox)
        QWidget.setTabOrder(self.yRotationSpinBox, self.zRotationSpinBox)
        QWidget.setTabOrder(self.zRotationSpinBox, self.alignToOtherObjectButton)
        QWidget.setTabOrder(self.alignToOtherObjectButton, self.flipPartButton)

        self.retranslateUi(Gui__TaskTransformDialog)

        QMetaObject.connectSlotsByName(Gui__TaskTransformDialog)
    # setupUi

    def retranslateUi(self, Gui__TaskTransformDialog):
        Gui__TaskTransformDialog.setWindowTitle(QCoreApplication.translate("Gui::TaskTransformDialog", u"Placement", None))
        self.label_2.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"Coordinate System", None))
        self.positionModeComboBox.setItemText(0, QCoreApplication.translate("Gui::TaskTransformDialog", u"Local Coordinate System", None))
        self.positionModeComboBox.setItemText(1, QCoreApplication.translate("Gui::TaskTransformDialog", u"Global Coordinate System", None))

        self.alignRotationCheckBox.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"align dragger rotation with selected coordinate system", None))
        self.positionGroupBox.setTitle(QCoreApplication.translate("Gui::TaskTransformDialog", u"Translation", None))
        self.xPositionLabel.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"X", None))
        self.yPositionLabel.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"Y", None))
        self.zPositionLabel.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"Z", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::TaskTransformDialog", u"Utilities", None))
        self.alignToOtherObjectButton.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"Move to other object", None))
        self.flipPartButton.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"Flip", None))
        self.transformOriginGroupBox.setTitle(QCoreApplication.translate("Gui::TaskTransformDialog", u"Dragger", None))
        self.snappingLabel.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"<b>Snapping</b>", None))
        self.translationIncrementLabel.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"Translation", None))
        self.referenceLabel.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"Reference", None))
        self.pickTransformOriginButton.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"pick reference", None))
        self.label.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"Mode", None))
        self.rotationIncrementLabel.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"Rotation", None))
        self.rotationGroupBox.setTitle(QCoreApplication.translate("Gui::TaskTransformDialog", u"Rotation", None))
        self.yRotationLabel.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"Y", None))
        self.zRotationLabel.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"Z", None))
        self.xRotationLabel.setText(QCoreApplication.translate("Gui::TaskTransformDialog", u"X", None))
    # retranslateUi

