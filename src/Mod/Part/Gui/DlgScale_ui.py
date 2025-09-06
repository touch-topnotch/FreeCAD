# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgScale.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QFrame,
    QGridLayout, QHeaderView, QLabel, QRadioButton,
    QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_PartGui_DlgScale(object):
    def setupUi(self, PartGui__DlgScale):
        if not PartGui__DlgScale.objectName():
            PartGui__DlgScale.setObjectName(u"PartGui__DlgScale")
        PartGui__DlgScale.resize(319, 360)
        self.verticalLayout = QVBoxLayout(PartGui__DlgScale)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(PartGui__DlgScale)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)

        self.label = QLabel(PartGui__DlgScale)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.dsbYScale = QDoubleSpinBox(PartGui__DlgScale)
        self.dsbYScale.setObjectName(u"dsbYScale")
        self.dsbYScale.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsbYScale.sizePolicy().hasHeightForWidth())
        self.dsbYScale.setSizePolicy(sizePolicy)
        self.dsbYScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbYScale.setDecimals(4)
        self.dsbYScale.setMinimum(-2147480000.000000000000000)
        self.dsbYScale.setMaximum(2147480000.000000000000000)
        self.dsbYScale.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.dsbYScale, 4, 1, 1, 1)

        self.label_7 = QLabel(PartGui__DlgScale)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 5, 0, 1, 1)

        self.rbUniform = QRadioButton(PartGui__DlgScale)
        self.rbUniform.setObjectName(u"rbUniform")
        self.rbUniform.setChecked(True)

        self.gridLayout_4.addWidget(self.rbUniform, 0, 0, 1, 1)

        self.dsbXScale = QDoubleSpinBox(PartGui__DlgScale)
        self.dsbXScale.setObjectName(u"dsbXScale")
        self.dsbXScale.setEnabled(False)
        sizePolicy.setHeightForWidth(self.dsbXScale.sizePolicy().hasHeightForWidth())
        self.dsbXScale.setSizePolicy(sizePolicy)
        self.dsbXScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbXScale.setDecimals(4)
        self.dsbXScale.setMinimum(-2147480000.000000000000000)
        self.dsbXScale.setMaximum(2147480000.000000000000000)
        self.dsbXScale.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.dsbXScale, 3, 1, 1, 1)

        self.label_4 = QLabel(PartGui__DlgScale)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 4, 0, 1, 1)

        self.rbNonUniform = QRadioButton(PartGui__DlgScale)
        self.rbNonUniform.setObjectName(u"rbNonUniform")

        self.gridLayout_4.addWidget(self.rbNonUniform, 2, 0, 1, 1)

        self.dsbUniformScale = QDoubleSpinBox(PartGui__DlgScale)
        self.dsbUniformScale.setObjectName(u"dsbUniformScale")
        self.dsbUniformScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbUniformScale.setDecimals(4)
        self.dsbUniformScale.setMinimum(-2147480000.000000000000000)
        self.dsbUniformScale.setMaximum(2147480000.000000000000000)
        self.dsbUniformScale.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.dsbUniformScale, 1, 1, 1, 1)

        self.dsbZScale = QDoubleSpinBox(PartGui__DlgScale)
        self.dsbZScale.setObjectName(u"dsbZScale")
        self.dsbZScale.setEnabled(False)
        sizePolicy.setHeightForWidth(self.dsbZScale.sizePolicy().hasHeightForWidth())
        self.dsbZScale.setSizePolicy(sizePolicy)
        self.dsbZScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbZScale.setKeyboardTracking(False)
        self.dsbZScale.setDecimals(4)
        self.dsbZScale.setMinimum(-2147480000.000000000000000)
        self.dsbZScale.setMaximum(2147480000.000000000000000)
        self.dsbZScale.setValue(1.000000000000000)

        self.gridLayout_4.addWidget(self.dsbZScale, 5, 1, 1, 1)

        self.label_2 = QLabel(PartGui__DlgScale)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 6, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.line = QFrame(PartGui__DlgScale)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.treeWidget = QTreeWidget(PartGui__DlgScale)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout.addWidget(self.treeWidget)

        self.statusLabel = QLabel(PartGui__DlgScale)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setEnabled(False)

        self.verticalLayout.addWidget(self.statusLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(PartGui__DlgScale)

        QMetaObject.connectSlotsByName(PartGui__DlgScale)
    # setupUi

    def retranslateUi(self, PartGui__DlgScale):
        PartGui__DlgScale.setWindowTitle(QCoreApplication.translate("PartGui::DlgScale", u"Scale", None))
        self.label_3.setText(QCoreApplication.translate("PartGui::DlgScale", u"X factor", None))
        self.label.setText(QCoreApplication.translate("PartGui::DlgScale", u"Factor", None))
        self.label_7.setText(QCoreApplication.translate("PartGui::DlgScale", u"Z factor", None))
#if QT_CONFIG(tooltip)
        self.rbUniform.setToolTip(QCoreApplication.translate("PartGui::DlgScale", u"Scale the object by a single factor in all directions.", None))
#endif // QT_CONFIG(tooltip)
        self.rbUniform.setText(QCoreApplication.translate("PartGui::DlgScale", u"Uniform Scaling", None))
        self.label_4.setText(QCoreApplication.translate("PartGui::DlgScale", u"Y factor", None))
#if QT_CONFIG(tooltip)
        self.rbNonUniform.setToolTip(QCoreApplication.translate("PartGui::DlgScale", u"Specify a different scale factor for each cardinal direction", None))
#endif // QT_CONFIG(tooltip)
        self.rbNonUniform.setText(QCoreApplication.translate("PartGui::DlgScale", u"Non-uniform scaling", None))
        self.label_2.setText("")
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("PartGui::DlgScale", u"Shape", None));
#if QT_CONFIG(tooltip)
        self.treeWidget.setToolTip(QCoreApplication.translate("PartGui::DlgScale", u"Select shapes to be scaled", None))
#endif // QT_CONFIG(tooltip)
        self.statusLabel.setText("")
    # retranslateUi

