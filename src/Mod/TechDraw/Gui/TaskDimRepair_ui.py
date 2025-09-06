# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskDimRepair.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_TaskDimRepair(object):
    def setupUi(self, TaskDimRepair):
        if not TaskDimRepair.objectName():
            TaskDimRepair.setObjectName(u"TaskDimRepair")
        TaskDimRepair.resize(355, 512)
        self.verticalLayout = QVBoxLayout(TaskDimRepair)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gbDimension = QGroupBox(TaskDimRepair)
        self.gbDimension.setObjectName(u"gbDimension")
        self.verticalLayout_2 = QVBoxLayout(self.gbDimension)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.gbDimension)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.gbDimension)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.leName = QLineEdit(self.gbDimension)
        self.leName.setObjectName(u"leName")
        self.leName.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leName.sizePolicy().hasHeightForWidth())
        self.leName.setSizePolicy(sizePolicy)
        self.leName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.leName.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leName)

        self.leLabel = QLineEdit(self.gbDimension)
        self.leLabel.setObjectName(u"leLabel")
        self.leLabel.setEnabled(True)
        sizePolicy.setHeightForWidth(self.leLabel.sizePolicy().hasHeightForWidth())
        self.leLabel.setSizePolicy(sizePolicy)
        self.leLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.leLabel.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.leLabel)

        self.pbSelection = QPushButton(self.gbDimension)
        self.pbSelection.setObjectName(u"pbSelection")
        sizePolicy.setHeightForWidth(self.pbSelection.sizePolicy().hasHeightForWidth())
        self.pbSelection.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pbSelection)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.gbDimension)

        self.gbReferences2D = QGroupBox(TaskDimRepair)
        self.gbReferences2D.setObjectName(u"gbReferences2D")
        self.verticalLayout_3 = QVBoxLayout(self.gbReferences2D)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.gbReferences2D)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.leObject2d = QLineEdit(self.gbReferences2D)
        self.leObject2d.setObjectName(u"leObject2d")
        sizePolicy.setHeightForWidth(self.leObject2d.sizePolicy().hasHeightForWidth())
        self.leObject2d.setSizePolicy(sizePolicy)
        self.leObject2d.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.leObject2d.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.leObject2d)

        self.label_6 = QLabel(self.gbReferences2D)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 90))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.lwGeometry2d = QListWidget(self.gbReferences2D)
        self.lwGeometry2d.setObjectName(u"lwGeometry2d")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lwGeometry2d.sizePolicy().hasHeightForWidth())
        self.lwGeometry2d.setSizePolicy(sizePolicy1)
        self.lwGeometry2d.setMinimumSize(QSize(0, 64))
        self.lwGeometry2d.setMaximumSize(QSize(16777215, 90))
        self.lwGeometry2d.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lwGeometry2d.setAlternatingRowColors(True)
        self.lwGeometry2d.setResizeMode(QListView.Adjust)
        self.lwGeometry2d.setItemAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lwGeometry2d)


        self.verticalLayout_3.addLayout(self.formLayout_2)


        self.verticalLayout.addWidget(self.gbReferences2D)

        self.gbReferences3d = QGroupBox(TaskDimRepair)
        self.gbReferences3d.setObjectName(u"gbReferences3d")
        self.verticalLayout_4 = QVBoxLayout(self.gbReferences3d)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.twReferences3d = QTableWidget(self.gbReferences3d)
        if (self.twReferences3d.columnCount() < 3):
            self.twReferences3d.setColumnCount(3)
        self.twReferences3d.setObjectName(u"twReferences3d")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.twReferences3d.sizePolicy().hasHeightForWidth())
        self.twReferences3d.setSizePolicy(sizePolicy2)
        self.twReferences3d.setAlternatingRowColors(True)
        self.twReferences3d.setSelectionMode(QAbstractItemView.NoSelection)
        self.twReferences3d.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.twReferences3d.setColumnCount(3)
        self.twReferences3d.horizontalHeader().setStretchLastSection(True)
        self.twReferences3d.verticalHeader().setVisible(False)

        self.verticalLayout_4.addWidget(self.twReferences3d)


        self.verticalLayout.addWidget(self.gbReferences3d)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TaskDimRepair)

        QMetaObject.connectSlotsByName(TaskDimRepair)
    # setupUi

    def retranslateUi(self, TaskDimRepair):
        TaskDimRepair.setWindowTitle(QCoreApplication.translate("TaskDimRepair", u"Dimension Repair", None))
        self.gbDimension.setTitle(QCoreApplication.translate("TaskDimRepair", u"Dimension", None))
        self.label.setText(QCoreApplication.translate("TaskDimRepair", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("TaskDimRepair", u"Label", None))
        self.pbSelection.setText(QCoreApplication.translate("TaskDimRepair", u"Replace references with current selection", None))
        self.gbReferences2D.setTitle(QCoreApplication.translate("TaskDimRepair", u"References 2D", None))
        self.label_5.setText(QCoreApplication.translate("TaskDimRepair", u"Object", None))
#if QT_CONFIG(tooltip)
        self.leObject2d.setToolTip(QCoreApplication.translate("TaskDimRepair", u"The view that owns this dimension", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("TaskDimRepair", u"Geometry", None))
#if QT_CONFIG(tooltip)
        self.lwGeometry2d.setToolTip(QCoreApplication.translate("TaskDimRepair", u"The sub-elements of the view that define the geometry for this dimension", None))
#endif // QT_CONFIG(tooltip)
        self.gbReferences3d.setTitle(QCoreApplication.translate("TaskDimRepair", u"References 3D", None))
    # retranslateUi

