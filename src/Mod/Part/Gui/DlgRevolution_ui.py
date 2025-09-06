# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgRevolution.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDialog,
    QFormLayout, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_PartGui_DlgRevolution(object):
    def setupUi(self, PartGui__DlgRevolution):
        if not PartGui__DlgRevolution.objectName():
            PartGui__DlgRevolution.setObjectName(u"PartGui__DlgRevolution")
        PartGui__DlgRevolution.resize(426, 599)
        PartGui__DlgRevolution.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(PartGui__DlgRevolution)
#ifndef Q_OS_MAC
        self.gridLayout.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
#endif
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeWidget = QTreeWidget(PartGui__DlgRevolution)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.treeWidget.setIndentation(20)
        self.treeWidget.setRootIsDecorated(False)

        self.gridLayout.addWidget(self.treeWidget, 0, 3, 1, 1)

        self.groupBox = QGroupBox(PartGui__DlgRevolution)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_1 = QGridLayout()
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_1.addWidget(self.label, 0, 0, 1, 1)

        self.xPos = Gui_QuantitySpinBox(self.groupBox)
        self.xPos.setObjectName(u"xPos")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xPos.sizePolicy().hasHeightForWidth())
        self.xPos.setSizePolicy(sizePolicy)
        self.xPos.setProperty(u"unit", u"mm")

        self.gridLayout_1.addWidget(self.xPos, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_1.addWidget(self.label_2, 1, 0, 1, 1)

        self.yPos = Gui_QuantitySpinBox(self.groupBox)
        self.yPos.setObjectName(u"yPos")
        sizePolicy.setHeightForWidth(self.yPos.sizePolicy().hasHeightForWidth())
        self.yPos.setSizePolicy(sizePolicy)
        self.yPos.setProperty(u"unit", u"mm")

        self.gridLayout_1.addWidget(self.yPos, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_1.addWidget(self.label_3, 2, 0, 1, 1)

        self.zPos = Gui_QuantitySpinBox(self.groupBox)
        self.zPos.setObjectName(u"zPos")
        sizePolicy.setHeightForWidth(self.zPos.sizePolicy().hasHeightForWidth())
        self.zPos.setSizePolicy(sizePolicy)
        self.zPos.setProperty(u"unit", u"mm")

        self.gridLayout_1.addWidget(self.zPos, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnX = QPushButton(self.groupBox)
        self.btnX.setObjectName(u"btnX")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnX.sizePolicy().hasHeightForWidth())
        self.btnX.setSizePolicy(sizePolicy1)
        self.btnX.setMinimumSize(QSize(0, 0))
        self.btnX.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.btnX, 0, 0, 1, 1)

        self.xDir = Gui_QuantitySpinBox(self.groupBox)
        self.xDir.setObjectName(u"xDir")
        sizePolicy.setHeightForWidth(self.xDir.sizePolicy().hasHeightForWidth())
        self.xDir.setSizePolicy(sizePolicy)
        self.xDir.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.xDir, 0, 1, 1, 1)

        self.btnY = QPushButton(self.groupBox)
        self.btnY.setObjectName(u"btnY")
        sizePolicy1.setHeightForWidth(self.btnY.sizePolicy().hasHeightForWidth())
        self.btnY.setSizePolicy(sizePolicy1)
        self.btnY.setMinimumSize(QSize(0, 0))
        self.btnY.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.btnY, 1, 0, 1, 1)

        self.yDir = Gui_QuantitySpinBox(self.groupBox)
        self.yDir.setObjectName(u"yDir")
        sizePolicy.setHeightForWidth(self.yDir.sizePolicy().hasHeightForWidth())
        self.yDir.setSizePolicy(sizePolicy)
        self.yDir.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.yDir, 1, 1, 1, 1)

        self.btnZ = QPushButton(self.groupBox)
        self.btnZ.setObjectName(u"btnZ")
        sizePolicy1.setHeightForWidth(self.btnZ.sizePolicy().hasHeightForWidth())
        self.btnZ.setSizePolicy(sizePolicy1)
        self.btnZ.setMinimumSize(QSize(0, 0))
        self.btnZ.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.btnZ, 2, 0, 1, 1)

        self.zDir = Gui_QuantitySpinBox(self.groupBox)
        self.zDir.setObjectName(u"zDir")
        sizePolicy.setHeightForWidth(self.zDir.sizePolicy().hasHeightForWidth())
        self.zDir.setSizePolicy(sizePolicy)
        self.zDir.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.zDir, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.selectLine = QPushButton(self.groupBox)
        self.selectLine.setObjectName(u"selectLine")

        self.verticalLayout.addWidget(self.selectLine)

        self.txtAxisLink = QLineEdit(self.groupBox)
        self.txtAxisLink.setObjectName(u"txtAxisLink")
        sizePolicy.setHeightForWidth(self.txtAxisLink.sizePolicy().hasHeightForWidth())
        self.txtAxisLink.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.txtAxisLink)


        self.gridLayout.addWidget(self.groupBox, 1, 3, 2, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(6)
        self.formLayout_3.setVerticalSpacing(6)
        self.label_5 = QLabel(PartGui__DlgRevolution)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.angle = Gui_QuantitySpinBox(PartGui__DlgRevolution)
        self.angle.setObjectName(u"angle")
        sizePolicy.setHeightForWidth(self.angle.sizePolicy().hasHeightForWidth())
        self.angle.setSizePolicy(sizePolicy)
        self.angle.setProperty(u"unit", u"deg")
        self.angle.setMinimum(-360.000000000000000)
        self.angle.setMaximum(360.000000000000000)
        self.angle.setValue(360.000000000000000)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.angle)


        self.gridLayout.addLayout(self.formLayout_3, 3, 3, 1, 1)

        self.checkSymmetric = QCheckBox(PartGui__DlgRevolution)
        self.checkSymmetric.setObjectName(u"checkSymmetric")

        self.gridLayout.addWidget(self.checkSymmetric, 4, 3, 1, 1)

        self.checkSolid = QCheckBox(PartGui__DlgRevolution)
        self.checkSolid.setObjectName(u"checkSolid")

        self.gridLayout.addWidget(self.checkSolid, 5, 3, 1, 1)

        QWidget.setTabOrder(self.treeWidget, self.btnX)
        QWidget.setTabOrder(self.btnX, self.btnY)
        QWidget.setTabOrder(self.btnY, self.btnZ)
        QWidget.setTabOrder(self.btnZ, self.selectLine)
        QWidget.setTabOrder(self.selectLine, self.txtAxisLink)
        QWidget.setTabOrder(self.txtAxisLink, self.checkSolid)

        self.retranslateUi(PartGui__DlgRevolution)

        QMetaObject.connectSlotsByName(PartGui__DlgRevolution)
    # setupUi

    def retranslateUi(self, PartGui__DlgRevolution):
        PartGui__DlgRevolution.setWindowTitle(QCoreApplication.translate("PartGui::DlgRevolution", u"Revolve", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("PartGui::DlgRevolution", u"Shape", None));
        self.groupBox.setTitle(QCoreApplication.translate("PartGui::DlgRevolution", u"Revolution Axis", None))
        self.label.setText(QCoreApplication.translate("PartGui::DlgRevolution", u"Center X", None))
        self.label_2.setText(QCoreApplication.translate("PartGui::DlgRevolution", u"Center Y", None))
        self.label_3.setText(QCoreApplication.translate("PartGui::DlgRevolution", u"Center Z", None))
#if QT_CONFIG(tooltip)
        self.btnX.setToolTip(QCoreApplication.translate("PartGui::DlgRevolution", u"Sets this as axis", None))
#endif // QT_CONFIG(tooltip)
        self.btnX.setText(QCoreApplication.translate("PartGui::DlgRevolution", u"X-Direction", None))
#if QT_CONFIG(tooltip)
        self.btnY.setToolTip(QCoreApplication.translate("PartGui::DlgRevolution", u"Sets this as axis", None))
#endif // QT_CONFIG(tooltip)
        self.btnY.setText(QCoreApplication.translate("PartGui::DlgRevolution", u"Y-Direction", None))
        self.btnZ.setText(QCoreApplication.translate("PartGui::DlgRevolution", u"Z-Direction", None))
        self.selectLine.setText(QCoreApplication.translate("PartGui::DlgRevolution", u"Select Reference", None))
        self.label_5.setText(QCoreApplication.translate("PartGui::DlgRevolution", u"Angle", None))
#if QT_CONFIG(tooltip)
        self.checkSymmetric.setToolTip(QCoreApplication.translate("PartGui::DlgRevolution", u"Extends the revolution forwards and backwards by half the angle", None))
#endif // QT_CONFIG(tooltip)
        self.checkSymmetric.setText(QCoreApplication.translate("PartGui::DlgRevolution", u"Symmetric angle", None))
#if QT_CONFIG(tooltip)
        self.checkSolid.setToolTip(QCoreApplication.translate("PartGui::DlgRevolution", u"Creates a solid. Otherwise it results in a shell.", None))
#endif // QT_CONFIG(tooltip)
        self.checkSolid.setText(QCoreApplication.translate("PartGui::DlgRevolution", u"Create solid", None))
    # retranslateUi

