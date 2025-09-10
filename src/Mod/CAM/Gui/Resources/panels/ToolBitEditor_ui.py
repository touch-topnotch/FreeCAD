# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ToolBitEditor.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QTabWidget,
    QToolButton, QTreeView, QVBoxLayout, QWidget)
import resource_rc

class Ui_ToolBitAttributes(object):
    def setupUi(self, ToolBitAttributes):
        if not ToolBitAttributes.objectName():
            ToolBitAttributes.setObjectName(u"ToolBitAttributes")
        ToolBitAttributes.resize(489, 715)
        self.gridLayout = QGridLayout(ToolBitAttributes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(ToolBitAttributes)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_2 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.tabWidgetPage1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.toolName = QLineEdit(self.groupBox_2)
        self.toolName.setObjectName(u"toolName")
        self.toolName.setMaxLength(50)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.toolName)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.shapePath = QLineEdit(self.widget)
        self.shapePath.setObjectName(u"shapePath")

        self.horizontalLayout.addWidget(self.shapePath)

        self.shapeSet = QToolButton(self.widget)
        self.shapeSet.setObjectName(u"shapeSet")
        self.shapeSet.setText(u"...")

        self.horizontalLayout.addWidget(self.shapeSet)


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.widget)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.bitParams = QGroupBox(self.tabWidgetPage1)
        self.bitParams.setObjectName(u"bitParams")
        self.formLayout_2 = QFormLayout(self.bitParams)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_9 = QLabel(self.bitParams)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.toolCuttingEdgeAngle = Gui_InputField(self.bitParams)
        self.toolCuttingEdgeAngle.setObjectName(u"toolCuttingEdgeAngle")
        self.toolCuttingEdgeAngle.setText(u"0 \u00b0")
        self.toolCuttingEdgeAngle.setProperty(u"unit", u"\u00b0")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.toolCuttingEdgeAngle)

        self.label_8 = QLabel(self.bitParams)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.toolCuttingEdgeHeight = Gui_InputField(self.bitParams)
        self.toolCuttingEdgeHeight.setObjectName(u"toolCuttingEdgeHeight")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.toolCuttingEdgeHeight)


        self.verticalLayout_2.addWidget(self.bitParams)

        self.image = QLabel(self.tabWidgetPage1)
        self.image.setObjectName(u"image")
        self.image.setMaximumSize(QSize(210, 297))
        self.image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.image)

        self.verticalSpacer = QSpacerItem(20, 277, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.verticalLayout_3 = QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.attrTree = QTreeView(self.tabWidgetPage2)
        self.attrTree.setObjectName(u"attrTree")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.attrTree.sizePolicy().hasHeightForWidth())
        self.attrTree.setSizePolicy(sizePolicy1)
        self.attrTree.setMinimumSize(QSize(0, 300))
        self.attrTree.setEditTriggers(QAbstractItemView.AllEditTriggers)

        self.verticalLayout_3.addWidget(self.attrTree)

        self.tabWidget.addTab(self.tabWidgetPage2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(ToolBitAttributes)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ToolBitAttributes)
    # setupUi

    def retranslateUi(self, ToolBitAttributes):
        ToolBitAttributes.setWindowTitle(QCoreApplication.translate("ToolBitAttributes", u"Tool Bit Attributes", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ToolBitAttributes", u"Tool Bit", None))
        self.label.setText(QCoreApplication.translate("ToolBitAttributes", u"Name", None))
#if QT_CONFIG(tooltip)
        self.toolName.setToolTip(QCoreApplication.translate("ToolBitAttributes", u"Display name of the Tool Bit (initial value taken from the shape file).", None))
#endif // QT_CONFIG(tooltip)
        self.toolName.setPlaceholderText(QCoreApplication.translate("ToolBitAttributes", u"Display Name", None))
        self.label_2.setText(QCoreApplication.translate("ToolBitAttributes", u"Shape File", None))
#if QT_CONFIG(tooltip)
        self.shapePath.setToolTip(QCoreApplication.translate("ToolBitAttributes", u"The file which defines the type and shape of the Tool Bit.", None))
#endif // QT_CONFIG(tooltip)
        self.shapePath.setPlaceholderText(QCoreApplication.translate("ToolBitAttributes", u"path", None))
#if QT_CONFIG(tooltip)
        self.shapeSet.setToolTip(QCoreApplication.translate("ToolBitAttributes", u"Change file defining type and shape of Tool Bit.", None))
#endif // QT_CONFIG(tooltip)
        self.bitParams.setTitle(QCoreApplication.translate("ToolBitAttributes", u"Parameter", None))
        self.label_9.setText(QCoreApplication.translate("ToolBitAttributes", u"Point/Tip Angle", None))
        self.label_8.setText(QCoreApplication.translate("ToolBitAttributes", u"Cutting Edge Height", None))
        self.toolCuttingEdgeHeight.setText(QCoreApplication.translate("ToolBitAttributes", u"0 mm", None))
        self.toolCuttingEdgeHeight.setProperty(u"unit", QCoreApplication.translate("ToolBitAttributes", u"mm", None))
        self.image.setText(QCoreApplication.translate("ToolBitAttributes", u"Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("ToolBitAttributes", u"Shape", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("ToolBitAttributes", u"Attributes", None))
    # retranslateUi

