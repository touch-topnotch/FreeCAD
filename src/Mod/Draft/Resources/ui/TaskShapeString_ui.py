# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskShapeString.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import Draft_rc

class Ui_DraftShapeStringGui(object):
    def setupUi(self, DraftShapeStringGui):
        if not DraftShapeStringGui.objectName():
            DraftShapeStringGui.setObjectName(u"DraftShapeStringGui")
        DraftShapeStringGui.resize(445, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DraftShapeStringGui.sizePolicy().hasHeightForWidth())
        DraftShapeStringGui.setSizePolicy(sizePolicy)
        DraftShapeStringGui.setMinimumSize(QSize(250, 0))
        self.gridLayout = QGridLayout(DraftShapeStringGui)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.labelX = QLabel(DraftShapeStringGui)
        self.labelX.setObjectName(u"labelX")

        self.gridLayout_7.addWidget(self.labelX, 0, 0, 1, 1)

        self.sbX = Gui_QuantitySpinBox(DraftShapeStringGui)
        self.sbX.setObjectName(u"sbX")
        self.sbX.setProperty(u"unit", u"mm")

        self.gridLayout_7.addWidget(self.sbX, 0, 1, 1, 1)

        self.labelY = QLabel(DraftShapeStringGui)
        self.labelY.setObjectName(u"labelY")

        self.gridLayout_7.addWidget(self.labelY, 1, 0, 1, 1)

        self.sbY = Gui_QuantitySpinBox(DraftShapeStringGui)
        self.sbY.setObjectName(u"sbY")
        self.sbY.setProperty(u"unit", u"mm")

        self.gridLayout_7.addWidget(self.sbY, 1, 1, 1, 1)

        self.labelZ = QLabel(DraftShapeStringGui)
        self.labelZ.setObjectName(u"labelZ")

        self.gridLayout_7.addWidget(self.labelZ, 2, 0, 1, 1)

        self.sbZ = Gui_QuantitySpinBox(DraftShapeStringGui)
        self.sbZ.setObjectName(u"sbZ")
        self.sbZ.setProperty(u"unit", u"mm")

        self.gridLayout_7.addWidget(self.sbZ, 2, 1, 1, 1)

        self.cbGlobalMode = QCheckBox(DraftShapeStringGui)
        self.cbGlobalMode.setObjectName(u"cbGlobalMode")

        self.gridLayout_7.addWidget(self.cbGlobalMode, 3, 0, 1, 1)

        self.pbReset = QPushButton(DraftShapeStringGui)
        self.pbReset.setObjectName(u"pbReset")

        self.gridLayout_7.addWidget(self.pbReset, 3, 1, 1, 1)

        self.labelHeight = QLabel(DraftShapeStringGui)
        self.labelHeight.setObjectName(u"labelHeight")

        self.gridLayout_7.addWidget(self.labelHeight, 4, 0, 1, 1)

        self.sbHeight = Gui_QuantitySpinBox(DraftShapeStringGui)
        self.sbHeight.setObjectName(u"sbHeight")
        self.sbHeight.setProperty(u"unit", u"mm")
        self.sbHeight.setMinimum(0.000000000000000)
        self.sbHeight.setValue(10.000000000000000)

        self.gridLayout_7.addWidget(self.sbHeight, 4, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.labelText = QLabel(DraftShapeStringGui)
        self.labelText.setObjectName(u"labelText")

        self.gridLayout_6.addWidget(self.labelText, 0, 0, 1, 1)

        self.leText = QLineEdit(DraftShapeStringGui)
        self.leText.setObjectName(u"leText")

        self.gridLayout_6.addWidget(self.leText, 0, 1, 1, 1)

        self.labelFontFile = QLabel(DraftShapeStringGui)
        self.labelFontFile.setObjectName(u"labelFontFile")

        self.gridLayout_6.addWidget(self.labelFontFile, 1, 0, 1, 1)

        self.fcFontFile = Gui_FileChooser(DraftShapeStringGui)
        self.fcFontFile.setObjectName(u"fcFontFile")

        self.gridLayout_6.addWidget(self.fcFontFile, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.verticalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_1, 2, 0, 1, 1)


        self.retranslateUi(DraftShapeStringGui)

        QMetaObject.connectSlotsByName(DraftShapeStringGui)
    # setupUi

    def retranslateUi(self, DraftShapeStringGui):
        DraftShapeStringGui.setWindowTitle(QCoreApplication.translate("DraftShapeStringGui", u"ShapeString", None))
        self.labelX.setText(QCoreApplication.translate("DraftShapeStringGui", u"X", None))
#if QT_CONFIG(tooltip)
        self.sbX.setToolTip(QCoreApplication.translate("DraftShapeStringGui", u"Enter coordinates or pick a point with the mouse", None))
#endif // QT_CONFIG(tooltip)
        self.labelY.setText(QCoreApplication.translate("DraftShapeStringGui", u"Y", None))
#if QT_CONFIG(tooltip)
        self.sbY.setToolTip(QCoreApplication.translate("DraftShapeStringGui", u"Enter coordinates or pick a point with the mouse", None))
#endif // QT_CONFIG(tooltip)
        self.labelZ.setText(QCoreApplication.translate("DraftShapeStringGui", u"Z", None))
#if QT_CONFIG(tooltip)
        self.sbZ.setToolTip(QCoreApplication.translate("DraftShapeStringGui", u"Enter coordinates or pick a point with the mouse", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cbGlobalMode.setToolTip(QCoreApplication.translate("DraftShapeStringGui", u"Coordinates relative to global coordinate system.\n"
"Uncheck to use working plane coordinate system", None))
#endif // QT_CONFIG(tooltip)
        self.cbGlobalMode.setText(QCoreApplication.translate("DraftShapeStringGui", u"Global", None))
#if QT_CONFIG(tooltip)
        self.pbReset.setToolTip(QCoreApplication.translate("DraftShapeStringGui", u"Resets the picked point", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pbReset.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pbReset.setText(QCoreApplication.translate("DraftShapeStringGui", u"Reset Point", None))
        self.labelHeight.setText(QCoreApplication.translate("DraftShapeStringGui", u"Height", None))
#if QT_CONFIG(tooltip)
        self.sbHeight.setToolTip(QCoreApplication.translate("DraftShapeStringGui", u"Height of the result", None))
#endif // QT_CONFIG(tooltip)
        self.labelText.setText(QCoreApplication.translate("DraftShapeStringGui", u"Text", None))
#if QT_CONFIG(tooltip)
        self.leText.setToolTip(QCoreApplication.translate("DraftShapeStringGui", u"Text to be made into ShapeString", None))
#endif // QT_CONFIG(tooltip)
        self.labelFontFile.setText(QCoreApplication.translate("DraftShapeStringGui", u"Font file", None))
        self.fcFontFile.setFilter(QCoreApplication.translate("DraftShapeStringGui", u"Font files (*.ttc *.ttf *.otf *.pfb *.TTC *.TTF *.OTF *.PFB)", None))
    # retranslateUi

