# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgExtrusion.ui'
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
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_PartGui_DlgExtrusion(object):
    def setupUi(self, PartGui__DlgExtrusion):
        if not PartGui__DlgExtrusion.objectName():
            PartGui__DlgExtrusion.setObjectName(u"PartGui__DlgExtrusion")
        PartGui__DlgExtrusion.resize(300, 564)
        self.verticalLayout = QVBoxLayout(PartGui__DlgExtrusion)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(PartGui__DlgExtrusion)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rbDirModeNormal = QRadioButton(self.groupBox_2)
        self.rbDirModeNormal.setObjectName(u"rbDirModeNormal")
        self.rbDirModeNormal.setChecked(True)

        self.gridLayout_2.addWidget(self.rbDirModeNormal, 3, 0, 1, 1)

        self.rbDirModeEdge = QRadioButton(self.groupBox_2)
        self.rbDirModeEdge.setObjectName(u"rbDirModeEdge")

        self.gridLayout_2.addWidget(self.rbDirModeEdge, 4, 0, 1, 1)

        self.chkReversed = QCheckBox(self.groupBox_2)
        self.chkReversed.setObjectName(u"chkReversed")

        self.gridLayout_2.addWidget(self.chkReversed, 4, 2, 1, 1)

        self.txtLink = QLineEdit(self.groupBox_2)
        self.txtLink.setObjectName(u"txtLink")

        self.gridLayout_2.addWidget(self.txtLink, 5, 0, 1, 1)

        self.btnSelectEdge = QPushButton(self.groupBox_2)
        self.btnSelectEdge.setObjectName(u"btnSelectEdge")

        self.gridLayout_2.addWidget(self.btnSelectEdge, 5, 2, 1, 1)

        self.rbDirModeCustom = QRadioButton(self.groupBox_2)
        self.rbDirModeCustom.setObjectName(u"rbDirModeCustom")

        self.gridLayout_2.addWidget(self.rbDirModeCustom, 6, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btnX = QPushButton(self.groupBox_2)
        self.btnX.setObjectName(u"btnX")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnX.sizePolicy().hasHeightForWidth())
        self.btnX.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.btnX, 0, 0, 1, 1)

        self.dirX = QDoubleSpinBox(self.groupBox_2)
        self.dirX.setObjectName(u"dirX")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dirX.sizePolicy().hasHeightForWidth())
        self.dirX.setSizePolicy(sizePolicy2)
        self.dirX.setMinimum(-2147480000.000000000000000)
        self.dirX.setMaximum(2147480000.000000000000000)

        self.gridLayout_3.addWidget(self.dirX, 0, 1, 1, 1)

        self.btnY = QPushButton(self.groupBox_2)
        self.btnY.setObjectName(u"btnY")

        self.gridLayout_3.addWidget(self.btnY, 1, 0, 1, 1)

        self.dirY = QDoubleSpinBox(self.groupBox_2)
        self.dirY.setObjectName(u"dirY")
        sizePolicy2.setHeightForWidth(self.dirY.sizePolicy().hasHeightForWidth())
        self.dirY.setSizePolicy(sizePolicy2)
        self.dirY.setMinimum(-2147480000.000000000000000)
        self.dirY.setMaximum(2147480000.000000000000000)

        self.gridLayout_3.addWidget(self.dirY, 1, 1, 1, 1)

        self.btnZ = QPushButton(self.groupBox_2)
        self.btnZ.setObjectName(u"btnZ")

        self.gridLayout_3.addWidget(self.btnZ, 2, 0, 1, 1)

        self.dirZ = QDoubleSpinBox(self.groupBox_2)
        self.dirZ.setObjectName(u"dirZ")
        sizePolicy2.setHeightForWidth(self.dirZ.sizePolicy().hasHeightForWidth())
        self.dirZ.setSizePolicy(sizePolicy2)
        self.dirZ.setKeyboardTracking(False)
        self.dirZ.setMinimum(-2147480000.000000000000000)
        self.dirZ.setMaximum(2147480000.000000000000000)
        self.dirZ.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.dirZ, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 7, 0, 1, 3)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(PartGui__DlgExtrusion)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.spinLenFwd = Gui_QuantitySpinBox(self.groupBox)
        self.spinLenFwd.setObjectName(u"spinLenFwd")
        sizePolicy2.setHeightForWidth(self.spinLenFwd.sizePolicy().hasHeightForWidth())
        self.spinLenFwd.setSizePolicy(sizePolicy2)
        self.spinLenFwd.setMinimumSize(QSize(0, 0))
        self.spinLenFwd.setProperty(u"unit", u"mm")
        self.spinLenFwd.setMinimum(-2147480000.000000000000000)
        self.spinLenFwd.setMaximum(2147480000.000000000000000)
        self.spinLenFwd.setValue(10.000000000000000)

        self.gridLayout.addWidget(self.spinLenFwd, 0, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.spinLenRev = Gui_QuantitySpinBox(self.groupBox)
        self.spinLenRev.setObjectName(u"spinLenRev")
        sizePolicy2.setHeightForWidth(self.spinLenRev.sizePolicy().hasHeightForWidth())
        self.spinLenRev.setSizePolicy(sizePolicy2)
        self.spinLenRev.setMinimumSize(QSize(0, 0))
        self.spinLenRev.setProperty(u"unit", u"mm")
        self.spinLenRev.setMinimum(-2147480000.000000000000000)
        self.spinLenRev.setMaximum(2147480000.000000000000000)
        self.spinLenRev.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.spinLenRev, 1, 1, 1, 1)

        self.chkSymmetric = QCheckBox(self.groupBox)
        self.chkSymmetric.setObjectName(u"chkSymmetric")

        self.gridLayout.addWidget(self.chkSymmetric, 2, 0, 1, 2)


        self.verticalLayout.addWidget(self.groupBox)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(PartGui__DlgExtrusion)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.spinTaperAngle = Gui_QuantitySpinBox(PartGui__DlgExtrusion)
        self.spinTaperAngle.setObjectName(u"spinTaperAngle")
        sizePolicy2.setHeightForWidth(self.spinTaperAngle.sizePolicy().hasHeightForWidth())
        self.spinTaperAngle.setSizePolicy(sizePolicy2)
        self.spinTaperAngle.setProperty(u"unit", u"deg")
        self.spinTaperAngle.setMinimum(-89.999999000000003)
        self.spinTaperAngle.setMaximum(89.999999000000003)

        self.gridLayout_4.addWidget(self.spinTaperAngle, 0, 1, 1, 1)

        self.label_2 = QLabel(PartGui__DlgExtrusion)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinTaperAngleRev = Gui_QuantitySpinBox(PartGui__DlgExtrusion)
        self.spinTaperAngleRev.setObjectName(u"spinTaperAngleRev")
        sizePolicy2.setHeightForWidth(self.spinTaperAngleRev.sizePolicy().hasHeightForWidth())
        self.spinTaperAngleRev.setSizePolicy(sizePolicy2)
        self.spinTaperAngleRev.setProperty(u"unit", u"deg")
        self.spinTaperAngleRev.setMinimum(-89.999999000000003)
        self.spinTaperAngleRev.setMaximum(89.999999000000003)

        self.gridLayout_4.addWidget(self.spinTaperAngleRev, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.chkSolid = QCheckBox(PartGui__DlgExtrusion)
        self.chkSolid.setObjectName(u"chkSolid")

        self.verticalLayout.addWidget(self.chkSolid)

        self.line = QFrame(PartGui__DlgExtrusion)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.treeWidget = QTreeWidget(PartGui__DlgExtrusion)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy3)
        self.treeWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.treeWidget.setIndentation(20)
        self.treeWidget.setRootIsDecorated(False)

        self.verticalLayout.addWidget(self.treeWidget)

        self.statusLabel = QLabel(PartGui__DlgExtrusion)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setText(u"StatusLabel")

        self.verticalLayout.addWidget(self.statusLabel)

        self.groupBox_2.raise_()
        self.chkSolid.raise_()
        self.treeWidget.raise_()
        self.statusLabel.raise_()
        self.groupBox.raise_()
        self.line.raise_()
        QWidget.setTabOrder(self.rbDirModeNormal, self.rbDirModeEdge)
        QWidget.setTabOrder(self.rbDirModeEdge, self.chkReversed)
        QWidget.setTabOrder(self.chkReversed, self.txtLink)
        QWidget.setTabOrder(self.txtLink, self.btnSelectEdge)
        QWidget.setTabOrder(self.btnSelectEdge, self.rbDirModeCustom)
        QWidget.setTabOrder(self.rbDirModeCustom, self.btnX)
        QWidget.setTabOrder(self.btnX, self.dirX)
        QWidget.setTabOrder(self.dirX, self.btnY)
        QWidget.setTabOrder(self.btnY, self.dirY)
        QWidget.setTabOrder(self.dirY, self.btnZ)
        QWidget.setTabOrder(self.btnZ, self.dirZ)
        QWidget.setTabOrder(self.dirZ, self.spinLenFwd)
        QWidget.setTabOrder(self.spinLenFwd, self.spinLenRev)
        QWidget.setTabOrder(self.spinLenRev, self.chkSymmetric)
        QWidget.setTabOrder(self.chkSymmetric, self.spinTaperAngle)
        QWidget.setTabOrder(self.spinTaperAngle, self.spinTaperAngleRev)
        QWidget.setTabOrder(self.spinTaperAngleRev, self.chkSolid)
        QWidget.setTabOrder(self.chkSolid, self.treeWidget)

        self.retranslateUi(PartGui__DlgExtrusion)

        QMetaObject.connectSlotsByName(PartGui__DlgExtrusion)
    # setupUi

    def retranslateUi(self, PartGui__DlgExtrusion):
        PartGui__DlgExtrusion.setWindowTitle(QCoreApplication.translate("PartGui::DlgExtrusion", u"Extrude", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PartGui::DlgExtrusion", u"Direction", None))
#if QT_CONFIG(tooltip)
        self.rbDirModeNormal.setToolTip(QCoreApplication.translate("PartGui::DlgExtrusion", u"Extrudes perpendicularly to the plane of the input shape", None))
#endif // QT_CONFIG(tooltip)
        self.rbDirModeNormal.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"Along normal", None))
#if QT_CONFIG(tooltip)
        self.rbDirModeEdge.setToolTip(QCoreApplication.translate("PartGui::DlgExtrusion", u"Set direction to match a direction of straight edge. Hint: to account for length of the edge too, set both lengths to zero.", None))
#endif // QT_CONFIG(tooltip)
        self.rbDirModeEdge.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"Along edge", None))
#if QT_CONFIG(tooltip)
        self.chkReversed.setToolTip(QCoreApplication.translate("PartGui::DlgExtrusion", u"Reverses the direction of the extrusion", None))
#endif // QT_CONFIG(tooltip)
        self.chkReversed.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"Reversed", None))
#if QT_CONFIG(tooltip)
        self.btnSelectEdge.setToolTip(QCoreApplication.translate("PartGui::DlgExtrusion", u"Starts the selection of edges in the 3D view", None))
#endif // QT_CONFIG(tooltip)
        self.btnSelectEdge.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"Select", None))
#if QT_CONFIG(tooltip)
        self.rbDirModeCustom.setToolTip(QCoreApplication.translate("PartGui::DlgExtrusion", u"Specify direction manually using X, Y, Z values", None))
#endif // QT_CONFIG(tooltip)
        self.rbDirModeCustom.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"Custom direction", None))
#if QT_CONFIG(tooltip)
        self.btnX.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btnX.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"X", None))
        self.btnY.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"Y", None))
        self.btnZ.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"Z", None))
        self.groupBox.setTitle(QCoreApplication.translate("PartGui::DlgExtrusion", u"Length", None))
        self.label_5.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"Along", None))
#if QT_CONFIG(tooltip)
        self.spinLenFwd.setToolTip(QCoreApplication.translate("PartGui::DlgExtrusion", u"Length to extrude along direction (can be negative).\n"
"If both lengths are zero, magnitude of direction is used.", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"Against", None))
#if QT_CONFIG(tooltip)
        self.spinLenRev.setToolTip(QCoreApplication.translate("PartGui::DlgExtrusion", u"Length to extrude against the direction (can be negative)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.chkSymmetric.setToolTip(QCoreApplication.translate("PartGui::DlgExtrusion", u"Distributes the extrusion length equally to both sides", None))
#endif // QT_CONFIG(tooltip)
        self.chkSymmetric.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"Symmetric", None))
        self.label.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"Taper angle along", None))
#if QT_CONFIG(tooltip)
        self.spinTaperAngle.setToolTip(QCoreApplication.translate("PartGui::DlgExtrusion", u"Taper (draft) angle along extrusion direction", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"Taper angle against", None))
#if QT_CONFIG(tooltip)
        self.spinTaperAngleRev.setToolTip(QCoreApplication.translate("PartGui::DlgExtrusion", u"Taper (draft) angle against extrusion direction", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.chkSolid.setToolTip(QCoreApplication.translate("PartGui::DlgExtrusion", u"Results in solids if wires are closed, otherwise in shells", None))
#endif // QT_CONFIG(tooltip)
        self.chkSolid.setText(QCoreApplication.translate("PartGui::DlgExtrusion", u"Create solid", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("PartGui::DlgExtrusion", u"Shape", None));
#if QT_CONFIG(tooltip)
        self.treeWidget.setToolTip(QCoreApplication.translate("PartGui::DlgExtrusion", u"Select shape(s) that should be extruded", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

