# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettings3DViewPart.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_PartGui_DlgSettings3DViewPart(object):
    def setupUi(self, PartGui__DlgSettings3DViewPart):
        if not PartGui__DlgSettings3DViewPart.objectName():
            PartGui__DlgSettings3DViewPart.setObjectName(u"PartGui__DlgSettings3DViewPart")
        PartGui__DlgSettings3DViewPart.resize(539, 339)
        self.gridLayout = QGridLayout(PartGui__DlgSettings3DViewPart)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.GroupBox12 = QGroupBox(PartGui__DlgSettings3DViewPart)
        self.GroupBox12.setObjectName(u"GroupBox12")
        self.gridLayout1 = QGridLayout(self.GroupBox12)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout2 = QGridLayout()
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.textLabel1 = QLabel(self.GroupBox12)
        self.textLabel1.setObjectName(u"textLabel1")

        self.gridLayout2.addWidget(self.textLabel1, 0, 0, 1, 1)

        self.maxDeviation = Gui_PrefDoubleSpinBox(self.GroupBox12)
        self.maxDeviation.setObjectName(u"maxDeviation")
        self.maxDeviation.setSuffix(u" %")
        self.maxDeviation.setDecimals(4)
        self.maxDeviation.setMinimum(0.010000000000000)
        self.maxDeviation.setMaximum(100.000000000000000)
        self.maxDeviation.setSingleStep(0.010000000000000)
        self.maxDeviation.setValue(0.500000000000000)
        self.maxDeviation.setProperty(u"prefEntry", u"MeshDeviation")
        self.maxDeviation.setProperty(u"prefPath", u"Mod/Part")

        self.gridLayout2.addWidget(self.maxDeviation, 0, 1, 1, 1)

        self.label = QLabel(self.GroupBox12)
        self.label.setObjectName(u"label")

        self.gridLayout2.addWidget(self.label, 1, 0, 1, 1)

        self.maxAngularDeflection = Gui_PrefDoubleSpinBox(self.GroupBox12)
        self.maxAngularDeflection.setObjectName(u"maxAngularDeflection")
        self.maxAngularDeflection.setSuffix(u" \u00b0")
        self.maxAngularDeflection.setDecimals(2)
        self.maxAngularDeflection.setMinimum(1.000000000000000)
        self.maxAngularDeflection.setMaximum(180.000000000000000)
        self.maxAngularDeflection.setSingleStep(0.500000000000000)
        self.maxAngularDeflection.setValue(28.500000000000000)
        self.maxAngularDeflection.setProperty(u"prefEntry", u"MeshAngularDeflection")
        self.maxAngularDeflection.setProperty(u"prefPath", u"Mod/Part")

        self.gridLayout2.addWidget(self.maxAngularDeflection, 1, 1, 1, 1)


        self.gridLayout1.addLayout(self.gridLayout2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.GroupBox12, 0, 0, 1, 1)

        self.spacerItem = QSpacerItem(20, 61, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.spacerItem, 1, 0, 1, 1)


        self.retranslateUi(PartGui__DlgSettings3DViewPart)

        QMetaObject.connectSlotsByName(PartGui__DlgSettings3DViewPart)
    # setupUi

    def retranslateUi(self, PartGui__DlgSettings3DViewPart):
        PartGui__DlgSettings3DViewPart.setWindowTitle(QCoreApplication.translate("PartGui::DlgSettings3DViewPart", u"Shape View", None))
        self.GroupBox12.setTitle(QCoreApplication.translate("PartGui::DlgSettings3DViewPart", u"Tessellation", None))
#if QT_CONFIG(tooltip)
        self.textLabel1.setToolTip(QCoreApplication.translate("PartGui::DlgSettings3DViewPart", u"Defines the deviation of tessellation to the actual surface", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.textLabel1.setWhatsThis(QCoreApplication.translate("PartGui::DlgSettings3DViewPart", u"<html><head><meta name=\"qrichtext\" content=\"1\" /></head><body style=\" white-space: pre-wrap; font-size:7.8pt; font-weight:400; font-style:normal; text-decoration:none;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Tessellation</span></p><p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"></p><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><span style=\" font-weight:400;\">Defines the maximum deviation of the tessellated mesh to the surface. The smaller the value is the slower the render speed which results in increased detail/resolution.</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.textLabel1.setText(QCoreApplication.translate("PartGui::DlgSettings3DViewPart", u"Maximum deviation depending on the model bounding box", None))
        self.label.setText(QCoreApplication.translate("PartGui::DlgSettings3DViewPart", u"Maximum angular deflection", None))
    # retranslateUi

