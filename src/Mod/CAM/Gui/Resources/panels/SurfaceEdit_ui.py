# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SurfaceEdit.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QToolBox, QWidget)
import Path_rc
import Path_rc

class Ui_TaskPanel(object):
    def setupUi(self, TaskPanel):
        if not TaskPanel.objectName():
            TaskPanel.setObjectName(u"TaskPanel")
        TaskPanel.resize(363, 523)
        TaskPanel.setMinimumSize(QSize(0, 400))
        self.gridLayout = QGridLayout(TaskPanel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolBox = QToolBox(TaskPanel)
        self.toolBox.setObjectName(u"toolBox")
        self.Geometry = QWidget()
        self.Geometry.setObjectName(u"Geometry")
        self.Geometry.setEnabled(True)
        self.Geometry.setGeometry(QRect(0, 0, 347, 391))
        self.gridLayout_2 = QGridLayout(self.Geometry)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.baseList = QListWidget(self.Geometry)
        self.baseList.setObjectName(u"baseList")
        self.baseList.setDragDropMode(QAbstractItemView.DragDrop)
        self.baseList.setDefaultDropAction(Qt.MoveAction)
        self.baseList.setSortingEnabled(False)

        self.gridLayout_2.addWidget(self.baseList, 0, 0, 1, 3)

        self.addBase = QPushButton(self.Geometry)
        self.addBase.setObjectName(u"addBase")

        self.gridLayout_2.addWidget(self.addBase, 1, 0, 1, 1)

        self.deleteBase = QPushButton(self.Geometry)
        self.deleteBase.setObjectName(u"deleteBase")

        self.gridLayout_2.addWidget(self.deleteBase, 1, 1, 1, 1)

        self.reorderBase = QPushButton(self.Geometry)
        self.reorderBase.setObjectName(u"reorderBase")

        self.gridLayout_2.addWidget(self.reorderBase, 1, 2, 1, 1)

        self.label = QLabel(self.Geometry)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 3)

        icon = QIcon()
        icon.addFile(u":/icons/CAM_BaseGeometry.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolBox.addItem(self.Geometry, icon, u"Base Geometry")
        self.Depths = QWidget()
        self.Depths.setObjectName(u"Depths")
        self.Depths.setGeometry(QRect(0, 0, 347, 391))
        self.formLayout_3 = QFormLayout(self.Depths)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.startDepth = Gui_InputField(self.Depths)
        self.startDepth.setObjectName(u"startDepth")
        self.startDepth.setProperty(u"unit", u"mm")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.startDepth)

        self.label_3 = QLabel(self.Depths)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.label_3)

        self.finalDepth = Gui_InputField(self.Depths)
        self.finalDepth.setObjectName(u"finalDepth")
        self.finalDepth.setProperty(u"unit", u"mm")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.finalDepth)

        self.label_4 = QLabel(self.Depths)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.label_4)

        self.stepDown = Gui_InputField(self.Depths)
        self.stepDown.setObjectName(u"stepDown")
        self.stepDown.setProperty(u"unit", u"mm")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.stepDown)

        self.label_2 = QLabel(self.Depths)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.label_2)

        self.finishDepth = Gui_InputField(self.Depths)
        self.finishDepth.setObjectName(u"finishDepth")
        self.finishDepth.setProperty(u"unit", u"mm")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.finishDepth)

        self.label_13 = QLabel(self.Depths)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.label_13)

        icon1 = QIcon()
        icon1.addFile(u":/icons/CAM_Depths.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolBox.addItem(self.Depths, icon1, u"Depths")
        self.Heights = QWidget()
        self.Heights.setObjectName(u"Heights")
        self.Heights.setGeometry(QRect(0, 0, 347, 391))
        self.formLayout = QFormLayout(self.Heights)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.safeHeight = Gui_InputField(self.Heights)
        self.safeHeight.setObjectName(u"safeHeight")
        self.safeHeight.setProperty(u"unit", u"mm")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.safeHeight)

        self.label_5 = QLabel(self.Heights)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_5)

        self.clearanceHeight = Gui_InputField(self.Heights)
        self.clearanceHeight.setObjectName(u"clearanceHeight")
        self.clearanceHeight.setProperty(u"unit", u"mm")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.clearanceHeight)

        self.label_6 = QLabel(self.Heights)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_6)

        icon2 = QIcon()
        icon2.addFile(u":/icons/CAM_Heights.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolBox.addItem(self.Heights, icon2, u"Heights")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 347, 391))
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_2 = QFrame(self.page_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.uiToolController = QComboBox(self.frame_2)
        self.uiToolController.setObjectName(u"uiToolController")

        self.gridLayout_3.addWidget(self.uiToolController, 0, 1, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)

        self.coolantController = QComboBox(self.frame_2)
        self.coolantController.setObjectName(u"coolantController")

        self.gridLayout_3.addWidget(self.coolantController, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame = QFrame(self.page_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.algorithmSelect = QComboBox(self.frame)
        self.algorithmSelect.addItem("")
        self.algorithmSelect.addItem("")
        self.algorithmSelect.setObjectName(u"algorithmSelect")

        self.horizontalLayout.addWidget(self.algorithmSelect)


        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 274, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 2, 0, 1, 1)

        icon3 = QIcon()
        icon3.addFile(u":/icons/CAM_OperationB.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolBox.addItem(self.page_3, icon3, u"Operation")

        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)


        self.retranslateUi(TaskPanel)

        self.toolBox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(TaskPanel)
    # setupUi

    def retranslateUi(self, TaskPanel):
        TaskPanel.setWindowTitle(QCoreApplication.translate("TaskPanel", u"Surface", None))
#if QT_CONFIG(tooltip)
        self.baseList.setToolTip(QCoreApplication.translate("TaskPanel", u"Drag to reorder, then update.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.addBase.setToolTip(QCoreApplication.translate("TaskPanel", u"Add item selected in window.", None))
#endif // QT_CONFIG(tooltip)
        self.addBase.setText(QCoreApplication.translate("TaskPanel", u"add", None))
#if QT_CONFIG(tooltip)
        self.deleteBase.setToolTip(QCoreApplication.translate("TaskPanel", u"Remove Item selected in list, then update.", None))
#endif // QT_CONFIG(tooltip)
        self.deleteBase.setText(QCoreApplication.translate("TaskPanel", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.reorderBase.setToolTip(QCoreApplication.translate("TaskPanel", u"Update the path with the removed and reordered items.", None))
#endif // QT_CONFIG(tooltip)
        self.reorderBase.setText(QCoreApplication.translate("TaskPanel", u"Update", None))
        self.label.setText(QCoreApplication.translate("TaskPanel", u"All objects will be profiled using the same depth and speed settings", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Geometry), QCoreApplication.translate("TaskPanel", u"Base Geometry", None))
        self.label_3.setText(QCoreApplication.translate("TaskPanel", u"Start Depth", None))
        self.label_4.setText(QCoreApplication.translate("TaskPanel", u"Final Depth", None))
        self.label_2.setText(QCoreApplication.translate("TaskPanel", u"Step Down", None))
        self.label_13.setText(QCoreApplication.translate("TaskPanel", u"Finish Step Down", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Depths), QCoreApplication.translate("TaskPanel", u"Depths", None))
        self.label_5.setText(QCoreApplication.translate("TaskPanel", u"Safe Height", None))
        self.label_6.setText(QCoreApplication.translate("TaskPanel", u"Clearance Height", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Heights), QCoreApplication.translate("TaskPanel", u"Heights", None))
        self.label_8.setText(QCoreApplication.translate("TaskPanel", u"Tool Controller", None))
        self.label_9.setText(QCoreApplication.translate("TaskPanel", u"Coolant Mode", None))
#if QT_CONFIG(tooltip)
        self.coolantController.setToolTip(QCoreApplication.translate("TaskPanel", u"The tool and its settings to be used for this operation.", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("TaskPanel", u"Algorithm", None))
        self.algorithmSelect.setItemText(0, QCoreApplication.translate("TaskPanel", u"OCL Dropcutter", None))
        self.algorithmSelect.setItemText(1, QCoreApplication.translate("TaskPanel", u"OCL Waterline", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("TaskPanel", u"Operation", None))
    # retranslateUi

