# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsImage.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QSpinBox, QTextEdit, QToolButton,
    QWidget)

class Ui_Gui_Dialog_DlgSettingsImage(object):
    def setupUi(self, Gui__Dialog__DlgSettingsImage):
        if not Gui__Dialog__DlgSettingsImage.objectName():
            Gui__Dialog__DlgSettingsImage.setObjectName(u"Gui__Dialog__DlgSettingsImage")
        Gui__Dialog__DlgSettingsImage.resize(291, 498)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgSettingsImage)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.groupBoxDim = QGroupBox(Gui__Dialog__DlgSettingsImage)
        self.groupBoxDim.setObjectName(u"groupBoxDim")
        self.gridLayout1 = QGridLayout(self.groupBoxDim)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
        self.gridLayout2 = QGridLayout()
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.groupBoxDim)
        self.label.setObjectName(u"label")

        self.gridLayout2.addWidget(self.label, 0, 0, 1, 1)

        self.standardSizeBox = QComboBox(self.groupBoxDim)
        self.standardSizeBox.addItem("")
        self.standardSizeBox.addItem("")
        self.standardSizeBox.addItem("")
        self.standardSizeBox.addItem("")
        self.standardSizeBox.addItem(u"CGA       320 x 200")
        self.standardSizeBox.addItem(u"QVGA     320 x 240")
        self.standardSizeBox.addItem(u"VGA       640 x 480")
        self.standardSizeBox.addItem(u"NTSC     720 x 480")
        self.standardSizeBox.addItem(u"PAL        768 x 578")
        self.standardSizeBox.addItem(u"SVGA     800 x 600")
        self.standardSizeBox.addItem(u"XGA       1024 x 768")
        self.standardSizeBox.addItem(u"HD720   1280 x 720")
        self.standardSizeBox.addItem(u"SXGA     1280 x 1024")
        self.standardSizeBox.addItem(u"SXGA+   1400 x 1050")
        self.standardSizeBox.addItem(u"UXGA     1600 x 1200")
        self.standardSizeBox.addItem(u"HD1080 1920 x 1080")
        self.standardSizeBox.addItem(u"WUXGA  1920 x 1200")
        self.standardSizeBox.addItem(u"QXGA     2048 x 1538")
        self.standardSizeBox.addItem(u"WQXGA  2560 x 1600")
        self.standardSizeBox.addItem(u"QSXGA   2560 x 2048")
        self.standardSizeBox.addItem(u"QUXGA   3200 \u00d7 2400")
        self.standardSizeBox.addItem(u"HUXGA   6400 \u00d7 4800")
        self.standardSizeBox.addItem(u"!!!          10000 x 10000")
        self.standardSizeBox.setObjectName(u"standardSizeBox")

        self.gridLayout2.addWidget(self.standardSizeBox, 0, 1, 1, 2)

        self.textLabelWidth = QLabel(self.groupBoxDim)
        self.textLabelWidth.setObjectName(u"textLabelWidth")

        self.gridLayout2.addWidget(self.textLabelWidth, 1, 0, 1, 1)

        self.spinWidth = QSpinBox(self.groupBoxDim)
        self.spinWidth.setObjectName(u"spinWidth")
        self.spinWidth.setMinimum(1)
        self.spinWidth.setMaximum(32767)

        self.gridLayout2.addWidget(self.spinWidth, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBoxDim)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout2.addWidget(self.label_2, 1, 2, 1, 1)

        self.textLabelHeight = QLabel(self.groupBoxDim)
        self.textLabelHeight.setObjectName(u"textLabelHeight")

        self.gridLayout2.addWidget(self.textLabelHeight, 2, 0, 1, 1)

        self.spinHeight = QSpinBox(self.groupBoxDim)
        self.spinHeight.setObjectName(u"spinHeight")
        self.spinHeight.setMinimum(1)
        self.spinHeight.setMaximum(32767)

        self.gridLayout2.addWidget(self.spinHeight, 2, 1, 1, 1)

        self.label_3 = QLabel(self.groupBoxDim)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout2.addWidget(self.label_3, 2, 2, 1, 1)


        self.gridLayout1.addLayout(self.gridLayout2, 0, 0, 1, 1)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.textLabel1 = QLabel(self.groupBoxDim)
        self.textLabel1.setObjectName(u"textLabel1")

        self.hboxLayout.addWidget(self.textLabel1)

        self.buttonRatioScreen = QToolButton(self.groupBoxDim)
        self.buttonRatioScreen.setObjectName(u"buttonRatioScreen")

        self.hboxLayout.addWidget(self.buttonRatioScreen)

        self.buttonRatio4x3 = QToolButton(self.groupBoxDim)
        self.buttonRatio4x3.setObjectName(u"buttonRatio4x3")

        self.hboxLayout.addWidget(self.buttonRatio4x3)

        self.buttonRatio16x9 = QToolButton(self.groupBoxDim)
        self.buttonRatio16x9.setObjectName(u"buttonRatio16x9")

        self.hboxLayout.addWidget(self.buttonRatio16x9)

        self.buttonRatio1x1 = QToolButton(self.groupBoxDim)
        self.buttonRatio1x1.setObjectName(u"buttonRatio1x1")

        self.hboxLayout.addWidget(self.buttonRatio1x1)


        self.gridLayout1.addLayout(self.hboxLayout, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBoxDim, 0, 0, 1, 1)

        self.groupBoxProp = QGroupBox(Gui__Dialog__DlgSettingsImage)
        self.groupBoxProp.setObjectName(u"groupBoxProp")
        self.gridLayout3 = QGridLayout(self.groupBoxProp)
        self.gridLayout3.setSpacing(6)
        self.gridLayout3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.gridLayout3.setContentsMargins(9, 9, 9, 9)
        self.textLabelColor = QLabel(self.groupBoxProp)
        self.textLabelColor.setObjectName(u"textLabelColor")

        self.gridLayout3.addWidget(self.textLabelColor, 0, 0, 1, 1)

        self.comboBackground = QComboBox(self.groupBoxProp)
        self.comboBackground.addItem("")
        self.comboBackground.addItem("")
        self.comboBackground.addItem("")
        self.comboBackground.addItem("")
        self.comboBackground.setObjectName(u"comboBackground")

        self.gridLayout3.addWidget(self.comboBackground, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBoxProp)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout3.addWidget(self.label_4, 1, 0, 1, 1)

        self.comboMethod = QComboBox(self.groupBoxProp)
        self.comboMethod.setObjectName(u"comboMethod")

        self.gridLayout3.addWidget(self.comboMethod, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBoxProp, 1, 0, 1, 1)

        self.buttonGroupComment = QGroupBox(Gui__Dialog__DlgSettingsImage)
        self.buttonGroupComment.setObjectName(u"buttonGroupComment")
        self.buttonGroupComment.setEnabled(False)
        self.gridLayout4 = QGridLayout(self.buttonGroupComment)
        self.gridLayout4.setSpacing(6)
        self.gridLayout4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.gridLayout4.setContentsMargins(9, 9, 9, 9)
        self.radioButtonMiba = QRadioButton(self.buttonGroupComment)
        self.radioButtonMiba.setObjectName(u"radioButtonMiba")
        self.radioButtonMiba.setChecked(True)

        self.gridLayout4.addWidget(self.radioButtonMiba, 0, 0, 1, 1)

        self.radioButtonComment = QRadioButton(self.buttonGroupComment)
        self.radioButtonComment.setObjectName(u"radioButtonComment")

        self.gridLayout4.addWidget(self.radioButtonComment, 1, 0, 1, 1)

        self.textEditComment = QTextEdit(self.buttonGroupComment)
        self.textEditComment.setObjectName(u"textEditComment")
        self.textEditComment.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditComment.sizePolicy().hasHeightForWidth())
        self.textEditComment.setSizePolicy(sizePolicy)
        self.textEditComment.setMinimumSize(QSize(0, 70))

        self.gridLayout4.addWidget(self.textEditComment, 2, 0, 1, 1)

        self.checkWatermark = QCheckBox(self.buttonGroupComment)
        self.checkWatermark.setObjectName(u"checkWatermark")

        self.gridLayout4.addWidget(self.checkWatermark, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.buttonGroupComment, 2, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.textLabelWidth.setBuddy(self.spinWidth)
        self.textLabelHeight.setBuddy(self.spinHeight)
        self.textLabelColor.setBuddy(self.comboBackground)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.standardSizeBox, self.spinWidth)
        QWidget.setTabOrder(self.spinWidth, self.spinHeight)
        QWidget.setTabOrder(self.spinHeight, self.buttonRatioScreen)
        QWidget.setTabOrder(self.buttonRatioScreen, self.buttonRatio4x3)
        QWidget.setTabOrder(self.buttonRatio4x3, self.buttonRatio16x9)
        QWidget.setTabOrder(self.buttonRatio16x9, self.buttonRatio1x1)
        QWidget.setTabOrder(self.buttonRatio1x1, self.comboBackground)
        QWidget.setTabOrder(self.comboBackground, self.comboMethod)
        QWidget.setTabOrder(self.comboMethod, self.radioButtonMiba)
        QWidget.setTabOrder(self.radioButtonMiba, self.radioButtonComment)
        QWidget.setTabOrder(self.radioButtonComment, self.textEditComment)

        self.retranslateUi(Gui__Dialog__DlgSettingsImage)
        self.radioButtonComment.toggled.connect(self.textEditComment.setEnabled)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsImage)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsImage):
        Gui__Dialog__DlgSettingsImage.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Image settings", None))
        self.groupBoxDim.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Image dimensions", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Standard sizes:", None))
        self.standardSizeBox.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Current screen", None))
        self.standardSizeBox.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Icon       32  x 32", None))
        self.standardSizeBox.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Icon       64 x 64", None))
        self.standardSizeBox.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Icon       128 x 128", None))

        self.textLabelWidth.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"&Width:", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Pixel", None))
        self.textLabelHeight.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"&Height:", None))
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Pixel", None))
        self.textLabel1.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Aspect ratio:", None))
        self.buttonRatioScreen.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"&Screen", None))
#if QT_CONFIG(shortcut)
        self.buttonRatioScreen.setShortcut(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.buttonRatio4x3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"&4:3", None))
#if QT_CONFIG(shortcut)
        self.buttonRatio4x3.setShortcut(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Alt+4", None))
#endif // QT_CONFIG(shortcut)
        self.buttonRatio16x9.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"1&6:9", None))
#if QT_CONFIG(shortcut)
        self.buttonRatio16x9.setShortcut(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Alt+6", None))
#endif // QT_CONFIG(shortcut)
        self.buttonRatio1x1.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"&1:1", None))
#if QT_CONFIG(shortcut)
        self.buttonRatio1x1.setShortcut(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Alt+1", None))
#endif // QT_CONFIG(shortcut)
        self.groupBoxProp.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Image properties", None))
        self.textLabelColor.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Back&ground:", None))
        self.comboBackground.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Current", None))
        self.comboBackground.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"White", None))
        self.comboBackground.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Black", None))
        self.comboBackground.setItemText(3, QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Transparent", None))

        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Creation method:", None))
        self.buttonGroupComment.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Image comment", None))
        self.radioButtonMiba.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Insert MIBA", None))
        self.radioButtonComment.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Insert comment", None))
        self.checkWatermark.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsImage", u"Add watermark", None))
    # retranslateUi

