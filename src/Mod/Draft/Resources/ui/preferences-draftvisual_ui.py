# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-draftvisual.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsDraft(object):
    def setupUi(self, Gui__Dialog__DlgSettingsDraft):
        if not Gui__Dialog__DlgSettingsDraft.objectName():
            Gui__Dialog__DlgSettingsDraft.setObjectName(u"Gui__Dialog__DlgSettingsDraft")
        Gui__Dialog__DlgSettingsDraft.resize(570, 552)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsDraft)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(11, 11, 11, 11)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.groupBox_1 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.gridLayout_1 = QGridLayout(self.groupBox_1)
        self.gridLayout_1.setSpacing(6)
        self.gridLayout_1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.label_HatchPatternSize = QLabel(self.groupBox_1)
        self.label_HatchPatternSize.setObjectName(u"label_HatchPatternSize")

        self.gridLayout_1.addWidget(self.label_HatchPatternSize, 0, 0, 1, 1)

        self.spinBox_HatchPatternSize = Gui_PrefDoubleSpinBox(self.groupBox_1)
        self.spinBox_HatchPatternSize.setObjectName(u"spinBox_HatchPatternSize")
        self.spinBox_HatchPatternSize.setMinimumSize(QSize(140, 0))
        self.spinBox_HatchPatternSize.setSingleStep(0.050000000000000)
        self.spinBox_HatchPatternSize.setValue(1.000000000000000)
        self.spinBox_HatchPatternSize.setProperty(u"prefEntry", u"HatchPatternSize")
        self.spinBox_HatchPatternSize.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.spinBox_HatchPatternSize, 0, 1, 1, 1)

        self.horizontalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_1.addItem(self.horizontalSpacer_1, 0, 2, 1, 1)

        self.label_patternFile = QLabel(self.groupBox_1)
        self.label_patternFile.setObjectName(u"label_patternFile")

        self.gridLayout_1.addWidget(self.label_patternFile, 1, 0, 1, 1)

        self.fileChooser_patternFile = Gui_PrefFileChooser(self.groupBox_1)
        self.fileChooser_patternFile.setObjectName(u"fileChooser_patternFile")
        self.fileChooser_patternFile.setMode(Gui.FileChooser.Directory)
        self.fileChooser_patternFile.setProperty(u"prefEntry", u"patternFile")
        self.fileChooser_patternFile.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_1.addWidget(self.fileChooser_patternFile, 1, 1, 1, 2)


        self.vboxLayout.addWidget(self.groupBox_1)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsDraft)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_svgDashedLine = QLabel(self.groupBox_2)
        self.label_svgDashedLine.setObjectName(u"label_svgDashedLine")

        self.gridLayout_2.addWidget(self.label_svgDashedLine, 0, 0, 1, 1)

        self.lineEdit_svgDashedLine = Gui_PrefLineEdit(self.groupBox_2)
        self.lineEdit_svgDashedLine.setObjectName(u"lineEdit_svgDashedLine")
        self.lineEdit_svgDashedLine.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_svgDashedLine.setText(u"2,2")
        self.lineEdit_svgDashedLine.setProperty(u"prefEntry", u"svgDashedLine")
        self.lineEdit_svgDashedLine.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.lineEdit_svgDashedLine, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.label_svgDashdotLine = QLabel(self.groupBox_2)
        self.label_svgDashdotLine.setObjectName(u"label_svgDashdotLine")

        self.gridLayout_2.addWidget(self.label_svgDashdotLine, 1, 0, 1, 1)

        self.lineEdit_svgDashdotLine = Gui_PrefLineEdit(self.groupBox_2)
        self.lineEdit_svgDashdotLine.setObjectName(u"lineEdit_svgDashdotLine")
        self.lineEdit_svgDashdotLine.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_svgDashdotLine.setText(u"3,2,0.2,2")
        self.lineEdit_svgDashdotLine.setProperty(u"prefEntry", u"svgDashdotLine")
        self.lineEdit_svgDashdotLine.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.lineEdit_svgDashdotLine, 1, 1, 1, 1)

        self.label_svgDottedLine = QLabel(self.groupBox_2)
        self.label_svgDottedLine.setObjectName(u"label_svgDottedLine")

        self.gridLayout_2.addWidget(self.label_svgDottedLine, 2, 0, 1, 1)

        self.lineEdit_svgDottedLine = Gui_PrefLineEdit(self.groupBox_2)
        self.lineEdit_svgDottedLine.setObjectName(u"lineEdit_svgDottedLine")
        self.lineEdit_svgDottedLine.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_svgDottedLine.setText(u"0.2,2")
        self.lineEdit_svgDottedLine.setProperty(u"prefEntry", u"svgDottedLine")
        self.lineEdit_svgDottedLine.setProperty(u"prefPath", u"Mod/Draft")

        self.gridLayout_2.addWidget(self.lineEdit_svgDottedLine, 2, 1, 1, 1)


        self.vboxLayout.addWidget(self.groupBox_2)

        self.verticalSpacer_1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer_1)


        self.retranslateUi(Gui__Dialog__DlgSettingsDraft)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsDraft)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsDraft):
        Gui__Dialog__DlgSettingsDraft.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Visual", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"SVG Patterns", None))
        self.label_HatchPatternSize.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"SVG pattern size", None))
#if QT_CONFIG(tooltip)
        self.spinBox_HatchPatternSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"The default size for SVG patterns. A higher value results in a denser pattern.", None))
#endif // QT_CONFIG(tooltip)
        self.label_patternFile.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Additional SVG pattern location", None))
#if QT_CONFIG(tooltip)
        self.fileChooser_patternFile.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"An optional directory with custom SVG files containing\n"
"pattern definitions to be added to the standard patterns", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Drawing View Line Definitions", None))
        self.label_svgDashedLine.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Dashed line definition", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_svgDashedLine.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"An SVG linestyle definition", None))
#endif // QT_CONFIG(tooltip)
        self.label_svgDashdotLine.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Dashdot line definition", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_svgDashdotLine.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"An SVG linestyle definition", None))
#endif // QT_CONFIG(tooltip)
        self.label_svgDottedLine.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"Dotted line definition", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_svgDottedLine.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDraft", u"An SVG linestyle definition", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

