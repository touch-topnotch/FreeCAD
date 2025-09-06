# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mirroring.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_PartGui_Mirroring(object):
    def setupUi(self, PartGui__Mirroring):
        if not PartGui__Mirroring.objectName():
            PartGui__Mirroring.setObjectName(u"PartGui__Mirroring")
        PartGui__Mirroring.resize(279, 543)
        self.gridLayout_2 = QGridLayout(PartGui__Mirroring)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(PartGui__Mirroring)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.baseX = Gui_QuantitySpinBox(self.groupBox)
        self.baseX.setObjectName(u"baseX")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baseX.sizePolicy().hasHeightForWidth())
        self.baseX.setSizePolicy(sizePolicy)
        self.baseX.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.baseX, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.baseY = Gui_QuantitySpinBox(self.groupBox)
        self.baseY.setObjectName(u"baseY")
        sizePolicy.setHeightForWidth(self.baseY.sizePolicy().hasHeightForWidth())
        self.baseY.setSizePolicy(sizePolicy)
        self.baseY.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.baseY, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.baseZ = Gui_QuantitySpinBox(self.groupBox)
        self.baseZ.setObjectName(u"baseZ")
        sizePolicy.setHeightForWidth(self.baseZ.sizePolicy().hasHeightForWidth())
        self.baseZ.setSizePolicy(sizePolicy)
        self.baseZ.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.baseZ, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 2)

        self.label = QLabel(PartGui__Mirroring)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.comboBox = QComboBox(PartGui__Mirroring)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)

        self.shapes = QTreeWidget(PartGui__Mirroring)
        self.shapes.setObjectName(u"shapes")
        self.shapes.setEditTriggers(QAbstractItemView.CurrentChanged|QAbstractItemView.EditKeyPressed)
        self.shapes.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.shapes.setRootIsDecorated(False)
        self.shapes.setExpandsOnDoubleClick(False)

        self.gridLayout_2.addWidget(self.shapes, 0, 0, 1, 2)

        self.selectButton = QPushButton(PartGui__Mirroring)
        self.selectButton.setObjectName(u"selectButton")
        self.selectButton.setCheckable(True)
        self.selectButton.setChecked(True)

        self.gridLayout_2.addWidget(self.selectButton, 2, 0, 1, 1)

        self.referenceLineEdit = QLineEdit(PartGui__Mirroring)
        self.referenceLineEdit.setObjectName(u"referenceLineEdit")
        self.referenceLineEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.referenceLineEdit, 2, 1, 1, 1)


        self.retranslateUi(PartGui__Mirroring)

        QMetaObject.connectSlotsByName(PartGui__Mirroring)
    # setupUi

    def retranslateUi(self, PartGui__Mirroring):
        PartGui__Mirroring.setWindowTitle(QCoreApplication.translate("PartGui::Mirroring", u"Mirror", None))
        self.groupBox.setTitle(QCoreApplication.translate("PartGui::Mirroring", u"Base Point", None))
        self.label_3.setText(QCoreApplication.translate("PartGui::Mirroring", u"X", None))
        self.label_4.setText(QCoreApplication.translate("PartGui::Mirroring", u"Y", None))
        self.label_5.setText(QCoreApplication.translate("PartGui::Mirroring", u"Z", None))
        self.label.setText(QCoreApplication.translate("PartGui::Mirroring", u"Mirror plane", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("PartGui::Mirroring", u"XY-plane", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("PartGui::Mirroring", u"XZ-plane", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("PartGui::Mirroring", u"YZ-plane", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("PartGui::Mirroring", u"Use selected reference", None))

        ___qtreewidgetitem = self.shapes.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("PartGui::Mirroring", u"Shapes", None));
        self.selectButton.setText(QCoreApplication.translate("PartGui::Mirroring", u"Selecting", None))
        self.referenceLineEdit.setPlaceholderText(QCoreApplication.translate("PartGui::Mirroring", u"Mirror plane reference", None))
    # retranslateUi

