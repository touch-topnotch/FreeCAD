# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskPadPocketParameters.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_PartDesignGui_TaskPadPocketParameters(object):
    def setupUi(self, PartDesignGui__TaskPadPocketParameters):
        if not PartDesignGui__TaskPadPocketParameters.objectName():
            PartDesignGui__TaskPadPocketParameters.setObjectName(u"PartDesignGui__TaskPadPocketParameters")
        PartDesignGui__TaskPadPocketParameters.resize(300, 772)
        PartDesignGui__TaskPadPocketParameters.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(PartDesignGui__TaskPadPocketParameters)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sidesLabel = QLabel(PartDesignGui__TaskPadPocketParameters)
        self.sidesLabel.setObjectName(u"sidesLabel")

        self.gridLayout.addWidget(self.sidesLabel, 0, 0, 1, 1)

        self.sidesMode = QComboBox(PartDesignGui__TaskPadPocketParameters)
        self.sidesMode.setObjectName(u"sidesMode")

        self.gridLayout.addWidget(self.sidesMode, 0, 1, 1, 1)

        self.verticalLayout_22 = QHBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.side1Label = QLabel(PartDesignGui__TaskPadPocketParameters)
        self.side1Label.setObjectName(u"side1Label")

        self.verticalLayout_22.addWidget(self.side1Label)

        self.line1 = QFrame(PartDesignGui__TaskPadPocketParameters)
        self.line1.setObjectName(u"line1")
        self.line1.setFrameShape(QFrame.Shape.HLine)
        self.line1.setFrameShadow(QFrame.Shadow.Sunken)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line1.sizePolicy().hasHeightForWidth())
        self.line1.setSizePolicy(sizePolicy)

        self.verticalLayout_22.addWidget(self.line1)


        self.gridLayout.addLayout(self.verticalLayout_22, 1, 0, 1, 2)

        self.textLabel1 = QLabel(PartDesignGui__TaskPadPocketParameters)
        self.textLabel1.setObjectName(u"textLabel1")

        self.gridLayout.addWidget(self.textLabel1, 2, 0, 1, 1)

        self.changeMode = QComboBox(PartDesignGui__TaskPadPocketParameters)
        self.changeMode.addItem("")
        self.changeMode.setObjectName(u"changeMode")

        self.gridLayout.addWidget(self.changeMode, 2, 1, 1, 1)

        self.labelLength = QLabel(PartDesignGui__TaskPadPocketParameters)
        self.labelLength.setObjectName(u"labelLength")

        self.gridLayout.addWidget(self.labelLength, 3, 0, 1, 1)

        self.lengthEdit = Gui_PrefQuantitySpinBox(PartDesignGui__TaskPadPocketParameters)
        self.lengthEdit.setObjectName(u"lengthEdit")
        self.lengthEdit.setProperty(u"keyboardTracking", False)
        self.lengthEdit.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.lengthEdit, 3, 1, 1, 1)

        self.labelOffset = QLabel(PartDesignGui__TaskPadPocketParameters)
        self.labelOffset.setObjectName(u"labelOffset")

        self.gridLayout.addWidget(self.labelOffset, 4, 0, 1, 1)

        self.offsetEdit = Gui_PrefQuantitySpinBox(PartDesignGui__TaskPadPocketParameters)
        self.offsetEdit.setObjectName(u"offsetEdit")
        self.offsetEdit.setProperty(u"keyboardTracking", False)
        self.offsetEdit.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.offsetEdit, 4, 1, 1, 1)

        self.labelTaperAngle = QLabel(PartDesignGui__TaskPadPocketParameters)
        self.labelTaperAngle.setObjectName(u"labelTaperAngle")

        self.gridLayout.addWidget(self.labelTaperAngle, 5, 0, 1, 1)

        self.taperEdit = Gui_PrefQuantitySpinBox(PartDesignGui__TaskPadPocketParameters)
        self.taperEdit.setObjectName(u"taperEdit")
        self.taperEdit.setProperty(u"keyboardTracking", False)
        self.taperEdit.setProperty(u"unit", u"deg")

        self.gridLayout.addWidget(self.taperEdit, 5, 1, 1, 1)

        self.upToShapeList = QFrame(PartDesignGui__TaskPadPocketParameters)
        self.upToShapeList.setObjectName(u"upToShapeList")
        self.upToShapeList.setFrameShadow(QFrame.Plain)
        self.upToShapeList.setLineWidth(0)
        self.vboxLayout = QVBoxLayout(self.upToShapeList)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self._2 = QGridLayout()
        self._2.setObjectName(u"_2")
        self.lineShapeName = QLineEdit(self.upToShapeList)
        self.lineShapeName.setObjectName(u"lineShapeName")
        self.lineShapeName.setReadOnly(True)

        self._2.addWidget(self.lineShapeName, 0, 1, 1, 1)

        self.buttonShape = QToolButton(self.upToShapeList)
        self.buttonShape.setObjectName(u"buttonShape")
        self.buttonShape.setMinimumSize(QSize(0, 22))
        self.buttonShape.setCheckable(True)

        self._2.addWidget(self.buttonShape, 0, 0, 1, 1)


        self.vboxLayout.addLayout(self._2)

        self.checkBoxAllFaces = QCheckBox(self.upToShapeList)
        self.checkBoxAllFaces.setObjectName(u"checkBoxAllFaces")
        self.checkBoxAllFaces.setEnabled(True)

        self.vboxLayout.addWidget(self.checkBoxAllFaces)

        self.upToShapeFaces = QWidget(self.upToShapeList)
        self.upToShapeFaces.setObjectName(u"upToShapeFaces")
        self.verticalLayout_2 = QVBoxLayout(self.upToShapeFaces)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.buttonShapeFace = QToolButton(self.upToShapeFaces)
        self.buttonShapeFace.setObjectName(u"buttonShapeFace")
        self.buttonShapeFace.setCheckable(True)

        self.verticalLayout_2.addWidget(self.buttonShapeFace)

        self.listWidgetReferences = QListWidget(self.upToShapeFaces)
        self.listWidgetReferences.setObjectName(u"listWidgetReferences")
        self.listWidgetReferences.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_2.addWidget(self.listWidgetReferences)


        self.vboxLayout.addWidget(self.upToShapeFaces)


        self.gridLayout.addWidget(self.upToShapeList, 6, 0, 1, 2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineFaceName = QLineEdit(PartDesignGui__TaskPadPocketParameters)
        self.lineFaceName.setObjectName(u"lineFaceName")
        self.lineFaceName.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineFaceName, 0, 1, 1, 1)

        self.buttonFace = QToolButton(PartDesignGui__TaskPadPocketParameters)
        self.buttonFace.setObjectName(u"buttonFace")
        self.buttonFace.setMinimumSize(QSize(0, 22))
        self.buttonFace.setCheckable(True)

        self.gridLayout_5.addWidget(self.buttonFace, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_5, 7, 0, 1, 2)

        self.verticalLayout_221 = QHBoxLayout()
        self.verticalLayout_221.setObjectName(u"verticalLayout_221")
        self.verticalLayout_221.setContentsMargins(0, 0, 0, 0)
        self.side2Label = QLabel(PartDesignGui__TaskPadPocketParameters)
        self.side2Label.setObjectName(u"side2Label")

        self.verticalLayout_221.addWidget(self.side2Label)

        self.line2 = QFrame(PartDesignGui__TaskPadPocketParameters)
        self.line2.setObjectName(u"line2")
        self.line2.setFrameShape(QFrame.Shape.HLine)
        self.line2.setFrameShadow(QFrame.Shadow.Sunken)
        sizePolicy.setHeightForWidth(self.line2.sizePolicy().hasHeightForWidth())
        self.line2.setSizePolicy(sizePolicy)

        self.verticalLayout_221.addWidget(self.line2)


        self.gridLayout.addLayout(self.verticalLayout_221, 8, 0, 1, 2)

        self.typeLabel2 = QLabel(PartDesignGui__TaskPadPocketParameters)
        self.typeLabel2.setObjectName(u"typeLabel2")

        self.gridLayout.addWidget(self.typeLabel2, 9, 0, 1, 1)

        self.changeMode2 = QComboBox(PartDesignGui__TaskPadPocketParameters)
        self.changeMode2.setObjectName(u"changeMode2")

        self.gridLayout.addWidget(self.changeMode2, 9, 1, 1, 1)

        self.labelLength2 = QLabel(PartDesignGui__TaskPadPocketParameters)
        self.labelLength2.setObjectName(u"labelLength2")

        self.gridLayout.addWidget(self.labelLength2, 10, 0, 1, 1)

        self.lengthEdit2 = Gui_PrefQuantitySpinBox(PartDesignGui__TaskPadPocketParameters)
        self.lengthEdit2.setObjectName(u"lengthEdit2")
        self.lengthEdit2.setProperty(u"keyboardTracking", False)
        self.lengthEdit2.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.lengthEdit2, 10, 1, 1, 1)

        self.labelOffset2 = QLabel(PartDesignGui__TaskPadPocketParameters)
        self.labelOffset2.setObjectName(u"labelOffset2")

        self.gridLayout.addWidget(self.labelOffset2, 11, 0, 1, 1)

        self.offsetEdit2 = Gui_PrefQuantitySpinBox(PartDesignGui__TaskPadPocketParameters)
        self.offsetEdit2.setObjectName(u"offsetEdit2")
        self.offsetEdit2.setProperty(u"keyboardTracking", False)
        self.offsetEdit2.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.offsetEdit2, 11, 1, 1, 1)

        self.labelTaperAngle2 = QLabel(PartDesignGui__TaskPadPocketParameters)
        self.labelTaperAngle2.setObjectName(u"labelTaperAngle2")

        self.gridLayout.addWidget(self.labelTaperAngle2, 12, 0, 1, 1)

        self.taperEdit2 = Gui_PrefQuantitySpinBox(PartDesignGui__TaskPadPocketParameters)
        self.taperEdit2.setObjectName(u"taperEdit2")
        self.taperEdit2.setProperty(u"keyboardTracking", False)
        self.taperEdit2.setProperty(u"unit", u"deg")

        self.gridLayout.addWidget(self.taperEdit2, 12, 1, 1, 1)

        self.upToShapeList2 = QFrame(PartDesignGui__TaskPadPocketParameters)
        self.upToShapeList2.setObjectName(u"upToShapeList2")
        self.upToShapeList2.setFrameShadow(QFrame.Plain)
        self.upToShapeList2.setLineWidth(0)
        self.vboxLayout1 = QVBoxLayout(self.upToShapeList2)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.vboxLayout1.setContentsMargins(0, 0, 0, 0)
        self._22 = QGridLayout()
        self._22.setObjectName(u"_22")
        self.lineShapeName2 = QLineEdit(self.upToShapeList2)
        self.lineShapeName2.setObjectName(u"lineShapeName2")
        self.lineShapeName2.setReadOnly(True)

        self._22.addWidget(self.lineShapeName2, 0, 1, 1, 1)

        self.buttonShape2 = QToolButton(self.upToShapeList2)
        self.buttonShape2.setObjectName(u"buttonShape2")
        self.buttonShape2.setMinimumSize(QSize(0, 22))
        self.buttonShape2.setCheckable(True)

        self._22.addWidget(self.buttonShape2, 0, 0, 1, 1)


        self.vboxLayout1.addLayout(self._22)

        self.checkBoxAllFaces2 = QCheckBox(self.upToShapeList2)
        self.checkBoxAllFaces2.setObjectName(u"checkBoxAllFaces2")
        self.checkBoxAllFaces2.setEnabled(True)

        self.vboxLayout1.addWidget(self.checkBoxAllFaces2)

        self.upToShapeFaces2 = QWidget(self.upToShapeList2)
        self.upToShapeFaces2.setObjectName(u"upToShapeFaces2")
        self.verticalLayout_222 = QVBoxLayout(self.upToShapeFaces2)
        self.verticalLayout_222.setObjectName(u"verticalLayout_222")
        self.verticalLayout_222.setContentsMargins(0, 0, 0, 0)
        self.buttonShapeFace2 = QToolButton(self.upToShapeFaces2)
        self.buttonShapeFace2.setObjectName(u"buttonShapeFace2")
        self.buttonShapeFace2.setCheckable(True)

        self.verticalLayout_222.addWidget(self.buttonShapeFace2)

        self.listWidgetReferences2 = QListWidget(self.upToShapeFaces2)
        self.listWidgetReferences2.setObjectName(u"listWidgetReferences2")
        self.listWidgetReferences2.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_222.addWidget(self.listWidgetReferences2)


        self.vboxLayout1.addWidget(self.upToShapeFaces2)


        self.gridLayout.addWidget(self.upToShapeList2, 13, 0, 1, 2)

        self.gridLayout_52 = QGridLayout()
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.lineFaceName2 = QLineEdit(PartDesignGui__TaskPadPocketParameters)
        self.lineFaceName2.setObjectName(u"lineFaceName2")
        self.lineFaceName2.setReadOnly(True)

        self.gridLayout_52.addWidget(self.lineFaceName2, 0, 1, 1, 1)

        self.buttonFace2 = QToolButton(PartDesignGui__TaskPadPocketParameters)
        self.buttonFace2.setObjectName(u"buttonFace2")
        self.buttonFace2.setMinimumSize(QSize(0, 22))
        self.buttonFace2.setCheckable(True)

        self.gridLayout_52.addWidget(self.buttonFace2, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_52, 14, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.line = QFrame(PartDesignGui__TaskPadPocketParameters)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.checkBoxReversed = QCheckBox(PartDesignGui__TaskPadPocketParameters)
        self.checkBoxReversed.setObjectName(u"checkBoxReversed")

        self.verticalLayout.addWidget(self.checkBoxReversed)

        self.groupBox = QGroupBox(PartDesignGui__TaskPadPocketParameters)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelEdge = QLabel(self.groupBox)
        self.labelEdge.setObjectName(u"labelEdge")

        self.gridLayout_3.addWidget(self.labelEdge, 0, 0, 1, 1)

        self.directionCB = QComboBox(self.groupBox)
        self.directionCB.addItem("")
        self.directionCB.addItem("")
        self.directionCB.addItem("")
        self.directionCB.setObjectName(u"directionCB")

        self.gridLayout_3.addWidget(self.directionCB, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.checkBoxDirection = QCheckBox(self.groupBox)
        self.checkBoxDirection.setObjectName(u"checkBoxDirection")

        self.gridLayout_4.addWidget(self.checkBoxDirection, 1, 0, 1, 1)

        self.groupBoxDirection = QGroupBox(self.groupBox)
        self.groupBoxDirection.setObjectName(u"groupBoxDirection")
        self.groupBoxDirection.setEnabled(True)
        self.groupBoxDirection.setCheckable(False)
        self.groupBoxDirection.setChecked(False)
        self.gridLayout_2 = QGridLayout(self.groupBoxDirection)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelXSkew = QLabel(self.groupBoxDirection)
        self.labelXSkew.setObjectName(u"labelXSkew")

        self.gridLayout_2.addWidget(self.labelXSkew, 0, 0, 1, 1)

        self.XDirectionEdit = Gui_DoubleSpinBox(self.groupBoxDirection)
        self.XDirectionEdit.setObjectName(u"XDirectionEdit")
        self.XDirectionEdit.setKeyboardTracking(False)
        self.XDirectionEdit.setMinimum(-100.000000000000000)
        self.XDirectionEdit.setMaximum(100.000000000000000)
        self.XDirectionEdit.setSingleStep(0.100000000000000)
        self.XDirectionEdit.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.XDirectionEdit, 0, 1, 1, 1)

        self.labelYSkew = QLabel(self.groupBoxDirection)
        self.labelYSkew.setObjectName(u"labelYSkew")

        self.gridLayout_2.addWidget(self.labelYSkew, 1, 0, 1, 1)

        self.YDirectionEdit = Gui_DoubleSpinBox(self.groupBoxDirection)
        self.YDirectionEdit.setObjectName(u"YDirectionEdit")
        self.YDirectionEdit.setKeyboardTracking(False)
        self.YDirectionEdit.setMinimum(-100.000000000000000)
        self.YDirectionEdit.setMaximum(100.000000000000000)
        self.YDirectionEdit.setSingleStep(0.100000000000000)
        self.YDirectionEdit.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.YDirectionEdit, 1, 1, 1, 1)

        self.labelZSkew = QLabel(self.groupBoxDirection)
        self.labelZSkew.setObjectName(u"labelZSkew")

        self.gridLayout_2.addWidget(self.labelZSkew, 2, 0, 1, 1)

        self.ZDirectionEdit = Gui_DoubleSpinBox(self.groupBoxDirection)
        self.ZDirectionEdit.setObjectName(u"ZDirectionEdit")
        self.ZDirectionEdit.setKeyboardTracking(False)
        self.ZDirectionEdit.setMinimum(-100.000000000000000)
        self.ZDirectionEdit.setMaximum(100.000000000000000)
        self.ZDirectionEdit.setSingleStep(0.100000000000000)
        self.ZDirectionEdit.setValue(1.000000000000000)
        self.ZDirectionEdit.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.ZDirectionEdit, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBoxDirection, 2, 0, 1, 1)

        self.checkBoxAlongDirection = QCheckBox(self.groupBox)
        self.checkBoxAlongDirection.setObjectName(u"checkBoxAlongDirection")
        self.checkBoxAlongDirection.setEnabled(True)

        self.gridLayout_4.addWidget(self.checkBoxAlongDirection, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.checkBoxUpdateView = QCheckBox(PartDesignGui__TaskPadPocketParameters)
        self.checkBoxUpdateView.setObjectName(u"checkBoxUpdateView")
        self.checkBoxUpdateView.setChecked(True)

        self.verticalLayout.addWidget(self.checkBoxUpdateView)


        self.retranslateUi(PartDesignGui__TaskPadPocketParameters)

        QMetaObject.connectSlotsByName(PartDesignGui__TaskPadPocketParameters)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskPadPocketParameters):
        self.sidesLabel.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Mode", None))
        self.side1Label.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Side 1", None))
        self.textLabel1.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Type", None))
        self.changeMode.setItemText(0, QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Dimension", None))

        self.labelLength.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Length", None))
        self.labelOffset.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Offset to face", None))
#if QT_CONFIG(tooltip)
        self.labelTaperAngle.setToolTip(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Angle to taper the extrusion", None))
#endif // QT_CONFIG(tooltip)
        self.labelTaperAngle.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Taper angle", None))
        self.buttonShape.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Select Shape", None))
#if QT_CONFIG(tooltip)
        self.checkBoxAllFaces.setToolTip(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Selects all faces of the shape", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxAllFaces.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Select all faces", None))
#if QT_CONFIG(tooltip)
        self.buttonShapeFace.setToolTip(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Toggles between selection and preview mode", None))
#endif // QT_CONFIG(tooltip)
        self.buttonShapeFace.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Select", None))
        self.buttonFace.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Select Face", None))
        self.side2Label.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Side 2", None))
        self.typeLabel2.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Type", None))
        self.labelLength2.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Length", None))
        self.labelOffset2.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Offset to face", None))
#if QT_CONFIG(tooltip)
        self.labelTaperAngle2.setToolTip(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Angle to taper the extrusion", None))
#endif // QT_CONFIG(tooltip)
        self.labelTaperAngle2.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Taper angle", None))
        self.buttonShape2.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Select Shape", None))
#if QT_CONFIG(tooltip)
        self.checkBoxAllFaces2.setToolTip(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Selects all faces of the shape", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxAllFaces2.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Select all faces", None))
#if QT_CONFIG(tooltip)
        self.buttonShapeFace2.setToolTip(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Toggles between selection and preview mode", None))
#endif // QT_CONFIG(tooltip)
        self.buttonShapeFace2.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Select", None))
        self.buttonFace2.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Select Face", None))
        self.checkBoxReversed.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Reversed", None))
        self.groupBox.setTitle(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Direction", None))
        self.labelEdge.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Direction/edge", None))
        self.directionCB.setItemText(0, QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Sketch normal", None))
        self.directionCB.setItemText(1, QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Select reference\u2026", None))
        self.directionCB.setItemText(2, QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Custom direction", None))

#if QT_CONFIG(tooltip)
        self.directionCB.setToolTip(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Set a direction or select an edge\n"
"from the model as reference", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxDirection.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Show direction", None))
#if QT_CONFIG(tooltip)
        self.groupBoxDirection.setToolTip(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Use custom vector for pad direction, otherwise\n"
"the sketch plane's normal vector will be used", None))
#endif // QT_CONFIG(tooltip)
        self.labelXSkew.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"X", None))
#if QT_CONFIG(tooltip)
        self.XDirectionEdit.setToolTip(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"X-component of direction vector", None))
#endif // QT_CONFIG(tooltip)
        self.labelYSkew.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Y", None))
#if QT_CONFIG(tooltip)
        self.YDirectionEdit.setToolTip(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Y-component of direction vector", None))
#endif // QT_CONFIG(tooltip)
        self.labelZSkew.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Z", None))
#if QT_CONFIG(tooltip)
        self.ZDirectionEdit.setToolTip(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Z-component of direction vector", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBoxAlongDirection.setToolTip(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"If unchecked, the length will be\n"
"measured along the specified direction", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxAlongDirection.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Length along sketch normal", None))
        self.checkBoxUpdateView.setText(QCoreApplication.translate("PartDesignGui::TaskPadPocketParameters", u"Recompute on change", None))
        pass
    # retranslateUi

