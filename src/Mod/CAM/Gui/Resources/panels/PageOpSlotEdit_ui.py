# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpSlotEdit.ui'
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
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 400)
        Form.setWindowTitle(u"Form")
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolOptions = QFrame(Form)
        self.toolOptions.setObjectName(u"toolOptions")
        self.toolOptions.setFrameShape(QFrame.StyledPanel)
        self.toolOptions.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.toolOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 3)
        self.toolController_label = QLabel(self.toolOptions)
        self.toolController_label.setObjectName(u"toolController_label")

        self.gridLayout.addWidget(self.toolController_label, 0, 0, 1, 1)

        self.toolController = QComboBox(self.toolOptions)
        self.toolController.setObjectName(u"toolController")

        self.gridLayout.addWidget(self.toolController, 0, 1, 1, 1)

        self.coolantController = QComboBox(self.toolOptions)
        self.coolantController.setObjectName(u"coolantController")

        self.gridLayout.addWidget(self.coolantController, 1, 1, 1, 1)

        self.coolantController_label = QLabel(self.toolOptions)
        self.coolantController_label.setObjectName(u"coolantController_label")

        self.gridLayout.addWidget(self.coolantController_label, 1, 0, 1, 1)

        self.editToolController = QCheckBox(self.toolOptions)
        self.editToolController.setObjectName(u"editToolController")

        self.gridLayout.addWidget(self.editToolController, 2, 0, 1, 2)


        self.verticalLayout.addWidget(self.toolOptions)

        self.featureReferences = QFrame(Form)
        self.featureReferences.setObjectName(u"featureReferences")
        self.gridLayout_3 = QGridLayout(self.featureReferences)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 3, -1, 3)
        self.geo1Reference_label = QLabel(self.featureReferences)
        self.geo1Reference_label.setObjectName(u"geo1Reference_label")
        self.geo1Reference_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.geo1Reference_label, 0, 0, 1, 1)

        self.geo1Reference = QComboBox(self.featureReferences)
        self.geo1Reference.addItem("")
        self.geo1Reference.addItem("")
        self.geo1Reference.addItem("")
        self.geo1Reference.addItem("")
        self.geo1Reference.addItem("")
        self.geo1Reference.addItem("")
        self.geo1Reference.addItem("")
        self.geo1Reference.setObjectName(u"geo1Reference")
        self.geo1Reference.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geo1Reference.sizePolicy().hasHeightForWidth())
        self.geo1Reference.setSizePolicy(sizePolicy)
        self.geo1Reference.setEditable(False)

        self.gridLayout_3.addWidget(self.geo1Reference, 0, 1, 1, 1)

        self.geo2Reference_label = QLabel(self.featureReferences)
        self.geo2Reference_label.setObjectName(u"geo2Reference_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.geo2Reference_label.sizePolicy().hasHeightForWidth())
        self.geo2Reference_label.setSizePolicy(sizePolicy1)
        self.geo2Reference_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.geo2Reference_label, 1, 0, 1, 1)

        self.geo2Reference = QComboBox(self.featureReferences)
        self.geo2Reference.addItem("")
        self.geo2Reference.addItem("")
        self.geo2Reference.addItem("")
        self.geo2Reference.addItem("")
        self.geo2Reference.addItem("")
        self.geo2Reference.setObjectName(u"geo2Reference")
        sizePolicy.setHeightForWidth(self.geo2Reference.sizePolicy().hasHeightForWidth())
        self.geo2Reference.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(8)
        self.geo2Reference.setFont(font)
        self.geo2Reference.setEditable(False)

        self.gridLayout_3.addWidget(self.geo2Reference, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.featureReferences)

        self.customPoints = QFrame(Form)
        self.customPoints.setObjectName(u"customPoints")
        self.customPoints.setFrameShape(QFrame.StyledPanel)
        self.customPoints.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.customPoints)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 3, -1, 3)
        self.noBaseGeometry = QLabel(self.customPoints)
        self.noBaseGeometry.setObjectName(u"noBaseGeometry")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.noBaseGeometry.setFont(font1)
        self.noBaseGeometry.setStyleSheet(u"color:blue")
        self.noBaseGeometry.setAlignment(Qt.AlignCenter)
        self.noBaseGeometry.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.noBaseGeometry)

        self.usingCustomPoints = QLabel(self.customPoints)
        self.usingCustomPoints.setObjectName(u"usingCustomPoints")
        self.usingCustomPoints.setAlignment(Qt.AlignCenter)
        self.usingCustomPoints.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.usingCustomPoints)


        self.verticalLayout.addWidget(self.customPoints)

        self.extendPath = QFrame(Form)
        self.extendPath.setObjectName(u"extendPath")
        self.gridLayout_2 = QGridLayout(self.extendPath)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 3, -1, 3)
        self.geo1Extension_label = QLabel(self.extendPath)
        self.geo1Extension_label.setObjectName(u"geo1Extension_label")
        sizePolicy1.setHeightForWidth(self.geo1Extension_label.sizePolicy().hasHeightForWidth())
        self.geo1Extension_label.setSizePolicy(sizePolicy1)
        self.geo1Extension_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.geo1Extension_label, 0, 0, 1, 1)

        self.geo1Extension = Gui_InputField(self.extendPath)
        self.geo1Extension.setObjectName(u"geo1Extension")
        sizePolicy.setHeightForWidth(self.geo1Extension.sizePolicy().hasHeightForWidth())
        self.geo1Extension.setSizePolicy(sizePolicy)
        self.geo1Extension.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.geo1Extension, 0, 1, 1, 1)

        self.geo2Extensionlabel = QLabel(self.extendPath)
        self.geo2Extensionlabel.setObjectName(u"geo2Extensionlabel")
        self.geo2Extensionlabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.geo2Extensionlabel, 3, 0, 1, 1)

        self.geo2Extension = Gui_InputField(self.extendPath)
        self.geo2Extension.setObjectName(u"geo2Extension")
        sizePolicy.setHeightForWidth(self.geo2Extension.sizePolicy().hasHeightForWidth())
        self.geo2Extension.setSizePolicy(sizePolicy)
        self.geo2Extension.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.geo2Extension, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.extendPath)

        self.pathOptions = QFrame(Form)
        self.pathOptions.setObjectName(u"pathOptions")
        self.pathOptions.setFrameShape(QFrame.StyledPanel)
        self.pathOptions.setFrameShadow(QFrame.Raised)
        self.gridLayout1 = QGridLayout(self.pathOptions)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(-1, 3, -1, 3)
        self.layerMode_label = QLabel(self.pathOptions)
        self.layerMode_label.setObjectName(u"layerMode_label")

        self.gridLayout1.addWidget(self.layerMode_label, 0, 0, 1, 1)

        self.layerMode = QComboBox(self.pathOptions)
        self.layerMode.addItem("")
        self.layerMode.addItem("")
        self.layerMode.setObjectName(u"layerMode")
        self.layerMode.setFont(font)

        self.gridLayout1.addWidget(self.layerMode, 0, 1, 1, 1)

        self.pathOrientation_label = QLabel(self.pathOptions)
        self.pathOrientation_label.setObjectName(u"pathOrientation_label")

        self.gridLayout1.addWidget(self.pathOrientation_label, 1, 0, 1, 1)

        self.pathOrientation = QComboBox(self.pathOptions)
        self.pathOrientation.addItem("")
        self.pathOrientation.addItem("")
        self.pathOrientation.setObjectName(u"pathOrientation")

        self.gridLayout1.addWidget(self.pathOrientation, 1, 1, 1, 1)

        self.reverseDirection = QCheckBox(self.pathOptions)
        self.reverseDirection.setObjectName(u"reverseDirection")

        self.gridLayout1.addWidget(self.reverseDirection, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.pathOptions)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        QWidget.setTabOrder(self.toolController, self.coolantController)
        QWidget.setTabOrder(self.coolantController, self.geo1Reference)
        QWidget.setTabOrder(self.geo1Reference, self.geo2Reference)
        QWidget.setTabOrder(self.geo2Reference, self.geo1Extension)
        QWidget.setTabOrder(self.geo1Extension, self.geo2Extension)
        QWidget.setTabOrder(self.geo2Extension, self.layerMode)
        QWidget.setTabOrder(self.layerMode, self.pathOrientation)
        QWidget.setTabOrder(self.pathOrientation, self.reverseDirection)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.toolController_label.setText(QCoreApplication.translate("Form", u"Tool controller", None))
#if QT_CONFIG(tooltip)
        self.toolController.setToolTip(QCoreApplication.translate("Form", u" The tool and its settings to be used for this operation", None))
#endif // QT_CONFIG(tooltip)
        self.coolantController_label.setText(QCoreApplication.translate("Form", u"Coolant mode", None))
        self.editToolController.setText(QCoreApplication.translate("Form", u"Edit Tool Controller", None))
        self.geo1Reference_label.setText(QCoreApplication.translate("Form", u"Start feature reference", None))
        self.geo1Reference.setItemText(0, QCoreApplication.translate("Form", u"Center of mass", None))
        self.geo1Reference.setItemText(1, QCoreApplication.translate("Form", u"Center of bounding box", None))
        self.geo1Reference.setItemText(2, QCoreApplication.translate("Form", u"Lowest point", None))
        self.geo1Reference.setItemText(3, QCoreApplication.translate("Form", u"Highest point", None))
        self.geo1Reference.setItemText(4, QCoreApplication.translate("Form", u"Long edge", None))
        self.geo1Reference.setItemText(5, QCoreApplication.translate("Form", u"Short edge", None))
        self.geo1Reference.setItemText(6, QCoreApplication.translate("Form", u"Vertex", None))

#if QT_CONFIG(tooltip)
        self.geo1Reference.setToolTip(QCoreApplication.translate("Form", u"Choose what point to use on the first selected feature", None))
#endif // QT_CONFIG(tooltip)
        self.geo2Reference_label.setText(QCoreApplication.translate("Form", u"End Feature Reference", None))
        self.geo2Reference.setItemText(0, QCoreApplication.translate("Form", u"Center of mass", None))
        self.geo2Reference.setItemText(1, QCoreApplication.translate("Form", u"Center of bounding box", None))
        self.geo2Reference.setItemText(2, QCoreApplication.translate("Form", u"Lowest point", None))
        self.geo2Reference.setItemText(3, QCoreApplication.translate("Form", u"Highest point", None))
        self.geo2Reference.setItemText(4, QCoreApplication.translate("Form", u"Vertex", None))

#if QT_CONFIG(tooltip)
        self.geo2Reference.setToolTip(QCoreApplication.translate("Form", u"Choose what point to use on the second selected feature", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.noBaseGeometry.setToolTip(QCoreApplication.translate("Form", u"No base geometry Selected", None))
#endif // QT_CONFIG(tooltip)
        self.noBaseGeometry.setText(QCoreApplication.translate("Form", u"No base geometry selected", None))
#if QT_CONFIG(tooltip)
        self.usingCustomPoints.setToolTip(QCoreApplication.translate("Form", u"Currently using custom point inputs in the property view of the data tab", None))
#endif // QT_CONFIG(tooltip)
        self.usingCustomPoints.setText(QCoreApplication.translate("Form", u"Currently using custom point inputs available in the property view of the data tab", None))
        self.geo1Extension_label.setText(QCoreApplication.translate("Form", u"Extend path start", None))
#if QT_CONFIG(tooltip)
        self.geo1Extension.setToolTip(QCoreApplication.translate("Form", u"Positive extends the beginning of the path, negative shortens", None))
#endif // QT_CONFIG(tooltip)
        self.geo2Extensionlabel.setText(QCoreApplication.translate("Form", u"Extend Path End", None))
#if QT_CONFIG(tooltip)
        self.geo2Extension.setToolTip(QCoreApplication.translate("Form", u"Positive extends the end of the path, negative shortens", None))
#endif // QT_CONFIG(tooltip)
        self.layerMode_label.setText(QCoreApplication.translate("Form", u"Layer mode", None))
        self.layerMode.setItemText(0, QCoreApplication.translate("Form", u"Single-pass", None))
        self.layerMode.setItemText(1, QCoreApplication.translate("Form", u"Multi-pass", None))

#if QT_CONFIG(tooltip)
        self.layerMode.setToolTip(QCoreApplication.translate("Form", u"Complete the operation in a single pass at depth, or multiple passes to final depth", None))
#endif // QT_CONFIG(tooltip)
        self.pathOrientation_label.setText(QCoreApplication.translate("Form", u"Path orientation", None))
        self.pathOrientation.setItemText(0, QCoreApplication.translate("Form", u"Start to end", None))
        self.pathOrientation.setItemText(1, QCoreApplication.translate("Form", u"Perpendicular", None))

#if QT_CONFIG(tooltip)
        self.pathOrientation.setToolTip(QCoreApplication.translate("Form", u"Choose the path orientation with regard to the features selected", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.reverseDirection.setToolTip(QCoreApplication.translate("Form", u"Enable to reverse the cut direction of the slot path", None))
#endif // QT_CONFIG(tooltip)
        self.reverseDirection.setText(QCoreApplication.translate("Form", u"Reverse cut direction", None))
        pass
    # retranslateUi

