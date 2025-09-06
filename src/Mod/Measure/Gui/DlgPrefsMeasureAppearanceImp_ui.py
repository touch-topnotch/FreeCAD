# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPrefsMeasureAppearanceImp.ui'
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
import Measure_rc

class Ui_MeasureGui_DlgPrefsMeasureAppearanceImp(object):
    def setupUi(self, MeasureGui__DlgPrefsMeasureAppearanceImp):
        if not MeasureGui__DlgPrefsMeasureAppearanceImp.objectName():
            MeasureGui__DlgPrefsMeasureAppearanceImp.setObjectName(u"MeasureGui__DlgPrefsMeasureAppearanceImp")
        MeasureGui__DlgPrefsMeasureAppearanceImp.resize(623, 287)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MeasureGui__DlgPrefsMeasureAppearanceImp.sizePolicy().hasHeightForWidth())
        MeasureGui__DlgPrefsMeasureAppearanceImp.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/preferences-measure.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MeasureGui__DlgPrefsMeasureAppearanceImp.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(MeasureGui__DlgPrefsMeasureAppearanceImp)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gbMisc = QGroupBox(MeasureGui__DlgPrefsMeasureAppearanceImp)
        self.gbMisc.setObjectName(u"gbMisc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gbMisc.sizePolicy().hasHeightForWidth())
        self.gbMisc.setSizePolicy(sizePolicy1)
        self.gbMisc.setMinimumSize(QSize(0, 0))
        self.gbMisc.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_2 = QVBoxLayout(self.gbMisc)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.gbMisc)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gbMisc)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)

        self.sbFontSize = Gui_PrefSpinBox(self.gbMisc)
        self.sbFontSize.setObjectName(u"sbFontSize")
        self.sbFontSize.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbFontSize.setMinimum(1)
        self.sbFontSize.setValue(18)
        self.sbFontSize.setProperty(u"prefEntry", u"DefaultFontSize")
        self.sbFontSize.setProperty(u"prefPath", u"Mod/Measure/Appearance")

        self.gridLayout_5.addWidget(self.sbFontSize, 0, 1, 1, 1)

        self.cbBackground = Gui_PrefColorButton(self.gbMisc)
        self.cbBackground.setObjectName(u"cbBackground")
        self.cbBackground.setProperty(u"color", QColor(0, 0, 0))
        self.cbBackground.setProperty(u"prefEntry", u"DefaultTextBackgroundColor")
        self.cbBackground.setProperty(u"prefPath", u"Mod/Measure/Appearance")

        self.gridLayout_5.addWidget(self.cbBackground, 3, 1, 1, 1)

        self.backgroundColorLabel = QLabel(self.gbMisc)
        self.backgroundColorLabel.setObjectName(u"backgroundColorLabel")

        self.gridLayout_5.addWidget(self.backgroundColorLabel, 3, 0, 1, 1)

        self.cbLine = Gui_PrefColorButton(self.gbMisc)
        self.cbLine.setObjectName(u"cbLine")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cbLine.sizePolicy().hasHeightForWidth())
        self.cbLine.setSizePolicy(sizePolicy2)
        self.cbLine.setProperty(u"color", QColor(255, 255, 255))
        self.cbLine.setProperty(u"prefEntry", u"DefaultLineColor")
        self.cbLine.setProperty(u"prefPath", u"Mod/Measure/Appearance")

        self.gridLayout_5.addWidget(self.cbLine, 2, 1, 1, 1)

        self.textColorLabel = QLabel(self.gbMisc)
        self.textColorLabel.setObjectName(u"textColorLabel")

        self.gridLayout_5.addWidget(self.textColorLabel, 1, 0, 1, 1)

        self.cbText = Gui_PrefColorButton(self.gbMisc)
        self.cbText.setObjectName(u"cbText")
        self.cbText.setProperty(u"color", QColor(255, 255, 255))
        self.cbText.setProperty(u"prefEntry", u"DefaultTextColor")
        self.cbText.setProperty(u"prefPath", u"Mod/Measure/Appearance")

        self.gridLayout_5.addWidget(self.cbText, 1, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 2)
        self.gridLayout_5.setColumnStretch(1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_5)


        self.verticalLayout_3.addWidget(self.gbMisc)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(MeasureGui__DlgPrefsMeasureAppearanceImp)

        QMetaObject.connectSlotsByName(MeasureGui__DlgPrefsMeasureAppearanceImp)
    # setupUi

    def retranslateUi(self, MeasureGui__DlgPrefsMeasureAppearanceImp):
        MeasureGui__DlgPrefsMeasureAppearanceImp.setWindowTitle(QCoreApplication.translate("MeasureGui::DlgPrefsMeasureAppearanceImp", u"Appearance", None))
#if QT_CONFIG(tooltip)
        MeasureGui__DlgPrefsMeasureAppearanceImp.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.gbMisc.setTitle(QCoreApplication.translate("MeasureGui::DlgPrefsMeasureAppearanceImp", u"Default Property Values", None))
        self.label.setText(QCoreApplication.translate("MeasureGui::DlgPrefsMeasureAppearanceImp", u"Text size", None))
        self.label_3.setText(QCoreApplication.translate("MeasureGui::DlgPrefsMeasureAppearanceImp", u"Line color", None))
        self.sbFontSize.setSuffix(QCoreApplication.translate("MeasureGui::DlgPrefsMeasureAppearanceImp", u" px", None))
        self.backgroundColorLabel.setText(QCoreApplication.translate("MeasureGui::DlgPrefsMeasureAppearanceImp", u"Background color", None))
        self.textColorLabel.setText(QCoreApplication.translate("MeasureGui::DlgPrefsMeasureAppearanceImp", u"Text color", None))
    # retranslateUi

