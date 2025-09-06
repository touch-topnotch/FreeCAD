# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VectorListEditor.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableView, QToolButton,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_Gui_VectorListEditor(object):
    def setupUi(self, Gui__VectorListEditor):
        if not Gui__VectorListEditor.objectName():
            Gui__VectorListEditor.setObjectName(u"Gui__VectorListEditor")
        Gui__VectorListEditor.resize(288, 476)
        self.gridLayout_3 = QGridLayout(Gui__VectorListEditor)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(Gui__VectorListEditor)
        self.label.setObjectName(u"label")
        self.label.setText(u"Id")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.spinBox = QSpinBox(Gui__VectorListEditor)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)

        self.gridLayout_2.addWidget(self.spinBox, 0, 1, 1, 1)

        self.label_2 = QLabel(Gui__VectorListEditor)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"X")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.coordX = QDoubleSpinBox(Gui__VectorListEditor)
        self.coordX.setObjectName(u"coordX")

        self.gridLayout_2.addWidget(self.coordX, 1, 1, 1, 1)

        self.label_3 = QLabel(Gui__VectorListEditor)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"Y")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.coordY = QDoubleSpinBox(Gui__VectorListEditor)
        self.coordY.setObjectName(u"coordY")

        self.gridLayout_2.addWidget(self.coordY, 2, 1, 1, 1)

        self.label_4 = QLabel(Gui__VectorListEditor)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setText(u"Z")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.coordZ = QDoubleSpinBox(Gui__VectorListEditor)
        self.coordZ.setObjectName(u"coordZ")

        self.gridLayout_2.addWidget(self.coordZ, 3, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(47, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonBox = QDialogButtonBox(Gui__VectorListEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.horizontalSpacer = QSpacerItem(20, 17, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Gui__VectorListEditor)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButton)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 2, 2, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButtonMouse = QToolButton(Gui__VectorListEditor)
        self.toolButtonMouse.setObjectName(u"toolButtonMouse")
        self.toolButtonMouse.setText(u"\u2026")
        icon = QIcon()
        icon.addFile(u":/icons/mouse_pointer.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButtonMouse.setIcon(icon)

        self.horizontalLayout.addWidget(self.toolButtonMouse)

        self.toolButtonAdd = QToolButton(Gui__VectorListEditor)
        self.toolButtonAdd.setObjectName(u"toolButtonAdd")
        self.toolButtonAdd.setText(u"\u2026")
        icon1 = QIcon()
        icon1.addFile(u":/icons/list-add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButtonAdd.setIcon(icon1)

        self.horizontalLayout.addWidget(self.toolButtonAdd)

        self.toolButtonRemove = QToolButton(Gui__VectorListEditor)
        self.toolButtonRemove.setObjectName(u"toolButtonRemove")
        self.toolButtonRemove.setText(u"\u2026")
        icon2 = QIcon()
        icon2.addFile(u":/icons/list-remove.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButtonRemove.setIcon(icon2)

        self.horizontalLayout.addWidget(self.toolButtonRemove)

        self.toolButtonAccept = QToolButton(Gui__VectorListEditor)
        self.toolButtonAccept.setObjectName(u"toolButtonAccept")
        self.toolButtonAccept.setText(u"\u2026")
        icon3 = QIcon()
        icon3.addFile(u":/icons/edit_OK.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButtonAccept.setIcon(icon3)

        self.horizontalLayout.addWidget(self.toolButtonAccept)


        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.widget = QWidget(Gui__VectorListEditor)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 300))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableView(self.widget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 2, 0, 1, 3)

        QWidget.setTabOrder(self.spinBox, self.coordX)
        QWidget.setTabOrder(self.coordX, self.coordY)
        QWidget.setTabOrder(self.coordY, self.coordZ)
        QWidget.setTabOrder(self.coordZ, self.toolButtonMouse)
        QWidget.setTabOrder(self.toolButtonMouse, self.toolButtonAdd)
        QWidget.setTabOrder(self.toolButtonAdd, self.toolButtonRemove)
        QWidget.setTabOrder(self.toolButtonRemove, self.toolButtonAccept)
        QWidget.setTabOrder(self.toolButtonAccept, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.pushButton)

        self.retranslateUi(Gui__VectorListEditor)
        self.pushButton.toggled.connect(self.widget.setVisible)

        QMetaObject.connectSlotsByName(Gui__VectorListEditor)
    # setupUi

    def retranslateUi(self, Gui__VectorListEditor):
        Gui__VectorListEditor.setWindowTitle(QCoreApplication.translate("Gui::VectorListEditor", u"Vectors", None))
        self.pushButton.setText(QCoreApplication.translate("Gui::VectorListEditor", u"Table", None))
    # retranslateUi

