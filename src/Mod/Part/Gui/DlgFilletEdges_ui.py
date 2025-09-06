# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgFilletEdges.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTreeView,
    QWidget)

class Ui_PartGui_DlgFilletEdges(object):
    def setupUi(self, PartGui__DlgFilletEdges):
        if not PartGui__DlgFilletEdges.objectName():
            PartGui__DlgFilletEdges.setObjectName(u"PartGui__DlgFilletEdges")
        PartGui__DlgFilletEdges.resize(290, 441)
        self.gridLayout_3 = QGridLayout(PartGui__DlgFilletEdges)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(PartGui__DlgFilletEdges)
        self.groupBox.setObjectName(u"groupBox")
        self.hboxLayout = QHBoxLayout(self.groupBox)
#ifndef Q_OS_MAC
        self.hboxLayout.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.hboxLayout.setContentsMargins(9, 9, 9, 9)
#endif
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.hboxLayout.addWidget(self.label)

        self.shapeObject = QComboBox(self.groupBox)
        self.shapeObject.addItem("")
        self.shapeObject.setObjectName(u"shapeObject")

        self.hboxLayout.addWidget(self.shapeObject)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.parameterName = QGroupBox(PartGui__DlgFilletEdges)
        self.parameterName.setObjectName(u"parameterName")
        self.gridLayout_2 = QGridLayout(self.parameterName)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_3 = QGroupBox(self.parameterName)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.selectEdges = QRadioButton(self.groupBox_3)
        self.selectEdges.setObjectName(u"selectEdges")
        self.selectEdges.setChecked(True)

        self.gridLayout.addWidget(self.selectEdges, 0, 0, 1, 2)

        self.selectFaces = QRadioButton(self.groupBox_3)
        self.selectFaces.setObjectName(u"selectFaces")

        self.gridLayout.addWidget(self.selectFaces, 0, 2, 1, 2)

        self.selectAllButton = QPushButton(self.groupBox_3)
        self.selectAllButton.setObjectName(u"selectAllButton")

        self.gridLayout.addWidget(self.selectAllButton, 1, 0, 1, 1)

        self.selectNoneButton = QPushButton(self.groupBox_3)
        self.selectNoneButton.setObjectName(u"selectNoneButton")

        self.gridLayout.addWidget(self.selectNoneButton, 1, 1, 1, 2)

        self.horizontalSpacer = QSpacerItem(221, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 3, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 2)

        self.labelfillet = QLabel(self.parameterName)
        self.labelfillet.setObjectName(u"labelfillet")

        self.gridLayout_2.addWidget(self.labelfillet, 1, 0, 1, 1)

        self.filletType = QComboBox(self.parameterName)
        self.filletType.addItem("")
        self.filletType.addItem("")
        self.filletType.setObjectName(u"filletType")

        self.gridLayout_2.addWidget(self.filletType, 1, 1, 1, 1)

        self.treeView = QTreeView(self.parameterName)
        self.treeView.setObjectName(u"treeView")

        self.gridLayout_2.addWidget(self.treeView, 2, 0, 1, 2)

        self.hboxLayout1 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.hboxLayout1.setSpacing(6)
#endif
        self.hboxLayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.labelRadius = QLabel(self.parameterName)
        self.labelRadius.setObjectName(u"labelRadius")

        self.hboxLayout1.addWidget(self.labelRadius)

        self.filletStartRadius = Gui_QuantitySpinBox(self.parameterName)
        self.filletStartRadius.setObjectName(u"filletStartRadius")
        self.filletStartRadius.setProperty(u"unit", u"mm")
        self.filletStartRadius.setSingleStep(0.100000000000000)
        self.filletStartRadius.setValue(1.000000000000000)

        self.hboxLayout1.addWidget(self.filletStartRadius)

        self.filletEndRadius = Gui_QuantitySpinBox(self.parameterName)
        self.filletEndRadius.setObjectName(u"filletEndRadius")
        self.filletEndRadius.setProperty(u"unit", u"mm")
        self.filletEndRadius.setSingleStep(0.100000000000000)
        self.filletEndRadius.setValue(1.000000000000000)

        self.hboxLayout1.addWidget(self.filletEndRadius)

        self.spacerItem = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.hboxLayout1.addItem(self.spacerItem)


        self.gridLayout_2.addLayout(self.hboxLayout1, 3, 0, 1, 2)


        self.gridLayout_3.addWidget(self.parameterName, 1, 0, 1, 1)

        QWidget.setTabOrder(self.shapeObject, self.filletType)
        QWidget.setTabOrder(self.filletType, self.treeView)
        QWidget.setTabOrder(self.treeView, self.filletStartRadius)
        QWidget.setTabOrder(self.filletStartRadius, self.filletEndRadius)

        self.retranslateUi(PartGui__DlgFilletEdges)

        QMetaObject.connectSlotsByName(PartGui__DlgFilletEdges)
    # setupUi

    def retranslateUi(self, PartGui__DlgFilletEdges):
        PartGui__DlgFilletEdges.setWindowTitle(QCoreApplication.translate("PartGui::DlgFilletEdges", u"Fillet Edges", None))
        self.groupBox.setTitle(QCoreApplication.translate("PartGui::DlgFilletEdges", u"Shape", None))
        self.label.setText(QCoreApplication.translate("PartGui::DlgFilletEdges", u"Selected shape", None))
        self.shapeObject.setItemText(0, QCoreApplication.translate("PartGui::DlgFilletEdges", u"No selection", None))

        self.parameterName.setTitle(QCoreApplication.translate("PartGui::DlgFilletEdges", u"Parameters", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("PartGui::DlgFilletEdges", u"Selection", None))
        self.selectEdges.setText(QCoreApplication.translate("PartGui::DlgFilletEdges", u"Select edges", None))
        self.selectFaces.setText(QCoreApplication.translate("PartGui::DlgFilletEdges", u"Select faces", None))
        self.selectAllButton.setText(QCoreApplication.translate("PartGui::DlgFilletEdges", u"All", None))
        self.selectNoneButton.setText(QCoreApplication.translate("PartGui::DlgFilletEdges", u"None", None))
        self.labelfillet.setText(QCoreApplication.translate("PartGui::DlgFilletEdges", u"Type", None))
        self.filletType.setItemText(0, QCoreApplication.translate("PartGui::DlgFilletEdges", u"Constant Radius", None))
        self.filletType.setItemText(1, QCoreApplication.translate("PartGui::DlgFilletEdges", u"Variable Radius", None))

        self.labelRadius.setText(QCoreApplication.translate("PartGui::DlgFilletEdges", u"Radius", None))
    # retranslateUi

