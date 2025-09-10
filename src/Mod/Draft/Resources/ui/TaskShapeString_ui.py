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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
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
        self.groupBox = QGroupBox(DraftShapeStringGui)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.labelX = QLabel(self.groupBox)
        self.labelX.setObjectName(u"labelX")

        self.gridLayout_7.addWidget(self.labelX, 0, 0, 1, 1)

        self.sbX = Gui_QuantitySpinBox(self.groupBox)
        self.sbX.setObjectName(u"sbX")
        self.sbX.setProperty(u"unit", u"")

        self.gridLayout_7.addWidget(self.sbX, 0, 1, 1, 1)

        self.labelY = QLabel(self.groupBox)
        self.labelY.setObjectName(u"labelY")

        self.gridLayout_7.addWidget(self.labelY, 1, 0, 1, 1)

        self.sbY = Gui_QuantitySpinBox(self.groupBox)
        self.sbY.setObjectName(u"sbY")
        self.sbY.setProperty(u"unit", u"")

        self.gridLayout_7.addWidget(self.sbY, 1, 1, 1, 1)

        self.labelZ = QLabel(self.groupBox)
        self.labelZ.setObjectName(u"labelZ")

        self.gridLayout_7.addWidget(self.labelZ, 2, 0, 1, 1)

        self.sbZ = Gui_QuantitySpinBox(self.groupBox)
        self.sbZ.setObjectName(u"sbZ")
        self.sbZ.setProperty(u"unit", u"")

        self.gridLayout_7.addWidget(self.sbZ, 2, 1, 1, 1)

        self.cbGlobalMode = QCheckBox(self.groupBox)
        self.cbGlobalMode.setObjectName(u"cbGlobalMode")

        self.gridLayout_7.addWidget(self.cbGlobalMode, 3, 0, 1, 1)

        self.pbReset = QPushButton(self.groupBox)
        self.pbReset.setObjectName(u"pbReset")

        self.gridLayout_7.addWidget(self.pbReset, 3, 1, 1, 1)

        self.labelHeight = QLabel(self.groupBox)
        self.labelHeight.setObjectName(u"labelHeight")

        self.gridLayout_7.addWidget(self.labelHeight, 4, 0, 1, 1)

        self.sbHeight = Gui_QuantitySpinBox(self.groupBox)
        self.sbHeight.setObjectName(u"sbHeight")
        self.sbHeight.setProperty(u"unit", u"")
        self.sbHeight.setMinimum(0.000000000000000)
        self.sbHeight.setValue(10.000000000000000)

        self.gridLayout_7.addWidget(self.sbHeight, 4, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.labelText = QLabel(self.groupBox)
        self.labelText.setObjectName(u"labelText")

        self.gridLayout_6.addWidget(self.labelText, 0, 0, 1, 1)

        self.leText = QLineEdit(self.groupBox)
        self.leText.setObjectName(u"leText")

        self.gridLayout_6.addWidget(self.leText, 0, 1, 1, 1)

        self.labelFontFile = QLabel(self.groupBox)
        self.labelFontFile.setObjectName(u"labelFontFile")

        self.gridLayout_6.addWidget(self.labelFontFile, 1, 0, 1, 1)

        self.fcFontFile = Gui_FileChooser(self.groupBox)
        self.fcFontFile.setObjectName(u"fcFontFile")

        self.gridLayout_6.addWidget(self.fcFontFile, 1, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.verticalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_1, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(DraftShapeStringGui)

        QMetaObject.connectSlotsByName(DraftShapeStringGui)
    # setupUi

    def retranslateUi(self, DraftShapeStringGui):
        DraftShapeStringGui.setWindowTitle(QCoreApplication.translate("DraftShapeStringGui", u"ShapeString", None))
        self.groupBox.setTitle("")
        self.labelX.setText(QCoreApplication.translate("DraftShapeStringGui", u"X", None))
#if QT_CONFIG(tooltip)
        self.sbX.setToolTip(QCoreApplication.translate("DraftShapeStringGui", u"Enter coordinates or select point with mouse.", None))
#endif // QT_CONFIG(tooltip)
        self.labelY.setText(QCoreApplication.translate("DraftShapeStringGui", u"Y", None))
#if QT_CONFIG(tooltip)
        self.sbY.setToolTip(QCoreApplication.translate("DraftShapeStringGui", u"Enter coordinates or select point with mouse.", None))
#endif // QT_CONFIG(tooltip)
        self.labelZ.setText(QCoreApplication.translate("DraftShapeStringGui", u"Z", None))
#if QT_CONFIG(tooltip)
        self.sbZ.setToolTip(QCoreApplication.translate("DraftShapeStringGui", u"Enter coordinates or select point with mouse.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cbGlobalMode.setToolTip(QCoreApplication.translate("DraftShapeStringGui", u"Coordinates relative to global coordinate system.\n"
"Uncheck to use working plane coordinate system", None))
#endif // QT_CONFIG(tooltip)
        self.cbGlobalMode.setText(QCoreApplication.translate("DraftShapeStringGui", u"Global", None))
#if QT_CONFIG(tooltip)
        self.pbReset.setToolTip(QCoreApplication.translate("DraftShapeStringGui", u"Reset 3D point selection", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pbReset.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pbReset.setText(QCoreApplication.translate("DraftShapeStringGui", u"Reset point", None))
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

