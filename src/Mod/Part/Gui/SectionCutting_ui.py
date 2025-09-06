# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SectionCutting.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QGridLayout, QGroupBox,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QWidget)

class Ui_PartGui_SectionCut(object):
    def setupUi(self, PartGui__SectionCut):
        if not PartGui__SectionCut.objectName():
            PartGui__SectionCut.setObjectName(u"PartGui__SectionCut")
        PartGui__SectionCut.resize(230, 514)
        PartGui__SectionCut.setMaximumSize(QSize(450, 16777215))
        self.gridLayout_6 = QGridLayout(PartGui__SectionCut)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBoxX = QGroupBox(PartGui__SectionCut)
        self.groupBoxX.setObjectName(u"groupBoxX")
        self.groupBoxX.setMaximumSize(QSize(16777215, 16777215))
        self.groupBoxX.setCheckable(True)
        self.groupBoxX.setChecked(False)
        self.gridLayout = QGridLayout(self.groupBoxX)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBoxX)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.cutX = QDoubleSpinBox(self.groupBoxX)
        self.cutX.setObjectName(u"cutX")
        self.cutX.setKeyboardTracking(False)

        self.gridLayout.addWidget(self.cutX, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.flipX = QPushButton(self.groupBoxX)
        self.flipX.setObjectName(u"flipX")
        self.flipX.setCheckable(True)
        self.flipX.setFlat(False)

        self.gridLayout.addWidget(self.flipX, 0, 3, 1, 1)

        self.cutXHS = QSlider(self.groupBoxX)
        self.cutXHS.setObjectName(u"cutXHS")
        self.cutXHS.setMaximum(100)
        self.cutXHS.setSliderPosition(50)
        self.cutXHS.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.cutXHS, 1, 0, 1, 4)


        self.gridLayout_6.addWidget(self.groupBoxX, 0, 0, 1, 3)

        self.groupBoxY = QGroupBox(PartGui__SectionCut)
        self.groupBoxY.setObjectName(u"groupBoxY")
        self.groupBoxY.setMaximumSize(QSize(16777215, 16777215))
        self.groupBoxY.setCheckable(True)
        self.groupBoxY.setChecked(False)
        self.gridLayout_2 = QGridLayout(self.groupBoxY)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBoxY)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.cutY = QDoubleSpinBox(self.groupBoxY)
        self.cutY.setObjectName(u"cutY")
        self.cutY.setKeyboardTracking(False)

        self.gridLayout_2.addWidget(self.cutY, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.flipY = QPushButton(self.groupBoxY)
        self.flipY.setObjectName(u"flipY")
        self.flipY.setCheckable(True)

        self.gridLayout_2.addWidget(self.flipY, 0, 3, 1, 1)

        self.cutYHS = QSlider(self.groupBoxY)
        self.cutYHS.setObjectName(u"cutYHS")
        self.cutYHS.setValue(50)
        self.cutYHS.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.cutYHS, 1, 0, 1, 4)


        self.gridLayout_6.addWidget(self.groupBoxY, 1, 0, 1, 3)

        self.groupBoxZ = QGroupBox(PartGui__SectionCut)
        self.groupBoxZ.setObjectName(u"groupBoxZ")
        self.groupBoxZ.setMaximumSize(QSize(16777215, 16777215))
        self.groupBoxZ.setCheckable(True)
        self.groupBoxZ.setChecked(False)
        self.gridLayout_3 = QGridLayout(self.groupBoxZ)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBoxZ)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.cutZ = QDoubleSpinBox(self.groupBoxZ)
        self.cutZ.setObjectName(u"cutZ")
        self.cutZ.setKeyboardTracking(False)

        self.gridLayout_3.addWidget(self.cutZ, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.flipZ = QPushButton(self.groupBoxZ)
        self.flipZ.setObjectName(u"flipZ")
        self.flipZ.setCheckable(True)

        self.gridLayout_3.addWidget(self.flipZ, 0, 3, 1, 1)

        self.cutZHS = QSlider(self.groupBoxZ)
        self.cutZHS.setObjectName(u"cutZHS")
        self.cutZHS.setMinimum(0)
        self.cutZHS.setMaximum(100)
        self.cutZHS.setValue(50)
        self.cutZHS.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.cutZHS, 1, 0, 1, 4)


        self.gridLayout_6.addWidget(self.groupBoxZ, 2, 0, 1, 3)

        self.CutfaceGB = QGroupBox(PartGui__SectionCut)
        self.CutfaceGB.setObjectName(u"CutfaceGB")
        self.gridLayout_4 = QGridLayout(self.CutfaceGB)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.CutfaceGB)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.CutColor = Gui_PrefColorButton(self.CutfaceGB)
        self.CutColor.setObjectName(u"CutColor")
        self.CutColor.setEnabled(False)
        self.CutColor.setMinimumSize(QSize(50, 20))
        self.CutColor.setMaximumSize(QSize(16777215, 16777215))
        self.CutColor.setColor(QColor(203, 203, 203))
        self.CutColor.setProperty(u"prefEntry", u"DefaultShapeColor")
        self.CutColor.setProperty(u"prefPath", u"View")

        self.gridLayout_4.addWidget(self.CutColor, 0, 1, 1, 1)

        self.autoCutfaceColorCB = Gui_PrefCheckBox(self.CutfaceGB)
        self.autoCutfaceColorCB.setObjectName(u"autoCutfaceColorCB")
        self.autoCutfaceColorCB.setMinimumSize(QSize(0, 0))
        self.autoCutfaceColorCB.setChecked(True)
        self.autoCutfaceColorCB.setProperty(u"prefEntry", u"TwoSideRendering")
        self.autoCutfaceColorCB.setProperty(u"prefPath", u"Mod/Part")

        self.gridLayout_4.addWidget(self.autoCutfaceColorCB, 0, 2, 1, 1)

        self.label_7 = QLabel(self.CutfaceGB)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)

        self.CutTransparencyHS = Gui_PrefSlider(self.CutfaceGB)
        self.CutTransparencyHS.setObjectName(u"CutTransparencyHS")
        self.CutTransparencyHS.setEnabled(False)
#if QT_CONFIG(tooltip)
        self.CutTransparencyHS.setToolTip(u"0 %")
#endif // QT_CONFIG(tooltip)
        self.CutTransparencyHS.setMaximum(100)
        self.CutTransparencyHS.setOrientation(Qt.Horizontal)
        self.CutTransparencyHS.setProperty(u"prefEntry", u"DefaultShapeTransparency")
        self.CutTransparencyHS.setProperty(u"prefPath", u"View")

        self.gridLayout_4.addWidget(self.CutTransparencyHS, 1, 1, 1, 2)


        self.gridLayout_6.addWidget(self.CutfaceGB, 3, 0, 1, 3)

        self.groupBoxIntersecting = QGroupBox(PartGui__SectionCut)
        self.groupBoxIntersecting.setObjectName(u"groupBoxIntersecting")
        self.groupBoxIntersecting.setMaximumSize(QSize(16777215, 16777215))
        self.groupBoxIntersecting.setCheckable(True)
        self.groupBoxIntersecting.setChecked(False)
        self.gridLayout_5 = QGridLayout(self.groupBoxIntersecting)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_9 = QLabel(self.groupBoxIntersecting)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)

        self.BFragColor = Gui_PrefColorButton(self.groupBoxIntersecting)
        self.BFragColor.setObjectName(u"BFragColor")
        self.BFragColor.setEnabled(False)
        self.BFragColor.setMinimumSize(QSize(50, 20))
        self.BFragColor.setMaximumSize(QSize(16777215, 16777215))
        self.BFragColor.setColor(QColor(203, 203, 203))
        self.BFragColor.setProperty(u"prefEntry", u"DefaultShapeColor")
        self.BFragColor.setProperty(u"prefPath", u"View")

        self.gridLayout_5.addWidget(self.BFragColor, 0, 1, 1, 1)

        self.autoBFColorCB = Gui_PrefCheckBox(self.groupBoxIntersecting)
        self.autoBFColorCB.setObjectName(u"autoBFColorCB")
        self.autoBFColorCB.setMinimumSize(QSize(0, 0))
        self.autoBFColorCB.setChecked(True)
        self.autoBFColorCB.setProperty(u"prefEntry", u"TwoSideRendering")
        self.autoBFColorCB.setProperty(u"prefPath", u"Mod/Part")

        self.gridLayout_5.addWidget(self.autoBFColorCB, 0, 2, 1, 1)

        self.label_8 = QLabel(self.groupBoxIntersecting)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)

        self.BFragTransparencyHS = Gui_PrefSlider(self.groupBoxIntersecting)
        self.BFragTransparencyHS.setObjectName(u"BFragTransparencyHS")
        self.BFragTransparencyHS.setEnabled(False)
#if QT_CONFIG(tooltip)
        self.BFragTransparencyHS.setToolTip(u"0 %")
#endif // QT_CONFIG(tooltip)
        self.BFragTransparencyHS.setMaximum(100)
        self.BFragTransparencyHS.setOrientation(Qt.Horizontal)
        self.BFragTransparencyHS.setProperty(u"prefEntry", u"DefaultShapeTransparency")
        self.BFragTransparencyHS.setProperty(u"prefPath", u"View")

        self.gridLayout_5.addWidget(self.BFragTransparencyHS, 1, 1, 1, 2)


        self.gridLayout_6.addWidget(self.groupBoxIntersecting, 4, 0, 1, 3)

        self.RefreshCutPB = QPushButton(PartGui__SectionCut)
        self.RefreshCutPB.setObjectName(u"RefreshCutPB")
        self.RefreshCutPB.setEnabled(True)

        self.gridLayout_6.addWidget(self.RefreshCutPB, 5, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_6, 5, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(PartGui__SectionCut)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.gridLayout_6.addWidget(self.buttonBox, 5, 2, 1, 1)

        self.keepOnlyCutCB = QCheckBox(PartGui__SectionCut)
        self.keepOnlyCutCB.setObjectName(u"keepOnlyCutCB")

        self.gridLayout_6.addWidget(self.keepOnlyCutCB, 6, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 7, 1, 1, 1)

        QWidget.setTabOrder(self.groupBoxX, self.cutX)
        QWidget.setTabOrder(self.cutX, self.flipX)
        QWidget.setTabOrder(self.flipX, self.groupBoxY)
        QWidget.setTabOrder(self.groupBoxY, self.cutY)
        QWidget.setTabOrder(self.cutY, self.flipY)
        QWidget.setTabOrder(self.flipY, self.groupBoxZ)
        QWidget.setTabOrder(self.groupBoxZ, self.cutZ)
        QWidget.setTabOrder(self.cutZ, self.flipZ)

        self.retranslateUi(PartGui__SectionCut)
        self.buttonBox.rejected.connect(PartGui__SectionCut.reject)
        self.autoCutfaceColorCB.toggled.connect(self.CutTransparencyHS.setDisabled)
        self.autoCutfaceColorCB.toggled.connect(self.CutColor.setDisabled)
        self.autoBFColorCB.toggled.connect(self.BFragColor.setDisabled)
        self.autoBFColorCB.toggled.connect(self.BFragTransparencyHS.setDisabled)

        QMetaObject.connectSlotsByName(PartGui__SectionCut)
    # setupUi

    def retranslateUi(self, PartGui__SectionCut):
        PartGui__SectionCut.setWindowTitle(QCoreApplication.translate("PartGui::SectionCut", u"Persistent Section Cut", None))
        self.groupBoxX.setTitle(QCoreApplication.translate("PartGui::SectionCut", u"Cutting X", None))
        self.label.setText(QCoreApplication.translate("PartGui::SectionCut", u"Offset", None))
        self.flipX.setText(QCoreApplication.translate("PartGui::SectionCut", u"Flip", None))
        self.groupBoxY.setTitle(QCoreApplication.translate("PartGui::SectionCut", u"Cutting Y", None))
        self.label_2.setText(QCoreApplication.translate("PartGui::SectionCut", u"Offset", None))
        self.flipY.setText(QCoreApplication.translate("PartGui::SectionCut", u"Flip", None))
        self.groupBoxZ.setTitle(QCoreApplication.translate("PartGui::SectionCut", u"Cutting Z", None))
        self.label_3.setText(QCoreApplication.translate("PartGui::SectionCut", u"Offset", None))
        self.flipZ.setText(QCoreApplication.translate("PartGui::SectionCut", u"Flip", None))
        self.CutfaceGB.setTitle(QCoreApplication.translate("PartGui::SectionCut", u"Cut Face", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("PartGui::SectionCut", u"Color of the cut face", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("PartGui::SectionCut", u"Color", None))
#if QT_CONFIG(tooltip)
        self.autoCutfaceColorCB.setToolTip(QCoreApplication.translate("PartGui::SectionCut", u"Takes the color and transparency\n"
"from the cut objects.\n"
"Works only properly if all objects\n"
"have the same values.", None))
#endif // QT_CONFIG(tooltip)
        self.autoCutfaceColorCB.setText(QCoreApplication.translate("PartGui::SectionCut", u"Auto", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("PartGui::SectionCut", u"Transparency of the cut face", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("PartGui::SectionCut", u"Transparency", None))
#if QT_CONFIG(tooltip)
        self.groupBoxIntersecting.setToolTip(QCoreApplication.translate("PartGui::SectionCut", u"Allows cutting objects intersecting each other\n"
"for the price that all cut objects\n"
"will get the same color", None))
#endif // QT_CONFIG(tooltip)
        self.groupBoxIntersecting.setTitle(QCoreApplication.translate("PartGui::SectionCut", u"Cut Intersecting Objects", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("PartGui::SectionCut", u"Color of the cut face", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("PartGui::SectionCut", u"Color", None))
#if QT_CONFIG(tooltip)
        self.BFragColor.setToolTip(QCoreApplication.translate("PartGui::SectionCut", u"Color for all objects", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.autoBFColorCB.setToolTip(QCoreApplication.translate("PartGui::SectionCut", u"Takes the color and transparency\n"
"from the cut objects.\n"
"Works only properly if all objects\n"
"have the same values.", None))
#endif // QT_CONFIG(tooltip)
        self.autoBFColorCB.setText(QCoreApplication.translate("PartGui::SectionCut", u"Auto", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("PartGui::SectionCut", u"Transparency of the cut face", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("PartGui::SectionCut", u"Transparency", None))
#if QT_CONFIG(tooltip)
        self.RefreshCutPB.setToolTip(QCoreApplication.translate("PartGui::SectionCut", u"Refreshes the list of visible objects", None))
#endif // QT_CONFIG(tooltip)
        self.RefreshCutPB.setText(QCoreApplication.translate("PartGui::SectionCut", u"Refresh View", None))
#if QT_CONFIG(tooltip)
        self.keepOnlyCutCB.setToolTip(QCoreApplication.translate("PartGui::SectionCut", u"When the dialog is closed,\n"
"only created cuts will be visible", None))
#endif // QT_CONFIG(tooltip)
        self.keepOnlyCutCB.setText(QCoreApplication.translate("PartGui::SectionCut", u"Keep only cuts visible when closing", None))
    # retranslateUi

