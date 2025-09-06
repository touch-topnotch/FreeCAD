# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskBalloon.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskBalloon(object):
    def setupUi(self, TechDrawGui__TaskBalloon):
        if not TechDrawGui__TaskBalloon.objectName():
            TechDrawGui__TaskBalloon.setObjectName(u"TechDrawGui__TaskBalloon")
        TechDrawGui__TaskBalloon.resize(300, 279)
        self.verticalLayout = QVBoxLayout(TechDrawGui__TaskBalloon)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(TechDrawGui__TaskBalloon)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.leText = QLineEdit(TechDrawGui__TaskBalloon)
        self.leText.setObjectName(u"leText")

        self.gridLayout.addWidget(self.leText, 0, 1, 1, 1)

        self.label_5 = QLabel(TechDrawGui__TaskBalloon)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.textColor = Gui_ColorButton(TechDrawGui__TaskBalloon)
        self.textColor.setObjectName(u"textColor")
        self.textColor.setColor(QColor(0, 0, 0))

        self.gridLayout.addWidget(self.textColor, 1, 1, 1, 1)

        self.label_7 = QLabel(TechDrawGui__TaskBalloon)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.qsbFontSize = Gui_QuantitySpinBox(TechDrawGui__TaskBalloon)
        self.qsbFontSize.setObjectName(u"qsbFontSize")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qsbFontSize.sizePolicy().hasHeightForWidth())
        self.qsbFontSize.setSizePolicy(sizePolicy)
        self.qsbFontSize.setMinimumSize(QSize(0, 20))
        self.qsbFontSize.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbFontSize.setValue(4.000000000000000)
        self.qsbFontSize.setProperty(u"prefEntry", u"BalloonKink")
        self.qsbFontSize.setProperty(u"prefPath", u"Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.qsbFontSize, 2, 1, 1, 1)

        self.label_3 = QLabel(TechDrawGui__TaskBalloon)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.comboBubbleShape = QComboBox(TechDrawGui__TaskBalloon)
        icon = QIcon()
        icon.addFile(u":/icons/circular.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comboBubbleShape.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/icons/none.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comboBubbleShape.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/icons/triangle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comboBubbleShape.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/icons/inspection.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comboBubbleShape.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/icons/hexagon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comboBubbleShape.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/icons/square.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comboBubbleShape.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/icons/rectangle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comboBubbleShape.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/icons/bottomline.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comboBubbleShape.addItem(icon7, "")
        self.comboBubbleShape.setObjectName(u"comboBubbleShape")

        self.gridLayout.addWidget(self.comboBubbleShape, 3, 1, 1, 1)

        self.label_2 = QLabel(TechDrawGui__TaskBalloon)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.qsbShapeScale = Gui_QuantitySpinBox(TechDrawGui__TaskBalloon)
        self.qsbShapeScale.setObjectName(u"qsbShapeScale")
        self.qsbShapeScale.setMinimumSize(QSize(0, 20))
        self.qsbShapeScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbShapeScale.setMinimum(0.000000000000000)
        self.qsbShapeScale.setSingleStep(0.100000000000000)
        self.qsbShapeScale.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.qsbShapeScale, 4, 1, 1, 1)

        self.label_4 = QLabel(TechDrawGui__TaskBalloon)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.comboEndSymbol = QComboBox(TechDrawGui__TaskBalloon)
        self.comboEndSymbol.setObjectName(u"comboEndSymbol")

        self.gridLayout.addWidget(self.comboEndSymbol, 5, 1, 1, 1)

        self.label_10 = QLabel(TechDrawGui__TaskBalloon)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)

        self.qsbSymbolScale = Gui_QuantitySpinBox(TechDrawGui__TaskBalloon)
        self.qsbSymbolScale.setObjectName(u"qsbSymbolScale")
        self.qsbSymbolScale.setMinimumSize(QSize(0, 20))
        self.qsbSymbolScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbSymbolScale.setMinimum(0.000000000000000)
        self.qsbSymbolScale.setSingleStep(0.100000000000000)
        self.qsbSymbolScale.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.qsbSymbolScale, 6, 1, 1, 1)

        self.label_9 = QLabel(TechDrawGui__TaskBalloon)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.comboLineVisible = QComboBox(TechDrawGui__TaskBalloon)
        self.comboLineVisible.addItem("")
        self.comboLineVisible.addItem("")
        self.comboLineVisible.setObjectName(u"comboLineVisible")

        self.gridLayout.addWidget(self.comboLineVisible, 7, 1, 1, 1)

        self.label_8 = QLabel(TechDrawGui__TaskBalloon)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)

        self.qsbLineWidth = Gui_QuantitySpinBox(TechDrawGui__TaskBalloon)
        self.qsbLineWidth.setObjectName(u"qsbLineWidth")
        sizePolicy.setHeightForWidth(self.qsbLineWidth.sizePolicy().hasHeightForWidth())
        self.qsbLineWidth.setSizePolicy(sizePolicy)
        self.qsbLineWidth.setMinimumSize(QSize(0, 20))
        self.qsbLineWidth.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbLineWidth.setValue(0.350000000000000)
        self.qsbLineWidth.setProperty(u"prefEntry", u"BalloonKink")
        self.qsbLineWidth.setProperty(u"prefPath", u"Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.qsbLineWidth, 8, 1, 1, 1)

        self.label_6 = QLabel(TechDrawGui__TaskBalloon)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)

        self.qsbKinkLength = Gui_QuantitySpinBox(TechDrawGui__TaskBalloon)
        self.qsbKinkLength.setObjectName(u"qsbKinkLength")
        sizePolicy.setHeightForWidth(self.qsbKinkLength.sizePolicy().hasHeightForWidth())
        self.qsbKinkLength.setSizePolicy(sizePolicy)
        self.qsbKinkLength.setMinimumSize(QSize(0, 20))
        self.qsbKinkLength.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbKinkLength.setValue(5.000000000000000)
        self.qsbKinkLength.setProperty(u"prefEntry", u"BalloonKink")
        self.qsbKinkLength.setProperty(u"prefPath", u"Mod/TechDraw/Dimensions")

        self.gridLayout.addWidget(self.qsbKinkLength, 9, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(TechDrawGui__TaskBalloon)

        self.comboLineVisible.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TechDrawGui__TaskBalloon)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskBalloon):
        TechDrawGui__TaskBalloon.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Balloon", None))
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Text", None))
#if QT_CONFIG(tooltip)
        self.leText.setToolTip(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Text to be displayed", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Text color", None))
#if QT_CONFIG(tooltip)
        self.textColor.setToolTip(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Color for text", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Font size", None))
#if QT_CONFIG(tooltip)
        self.qsbFontSize.setToolTip(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Font size for text", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Bubble shape", None))
        self.comboBubbleShape.setItemText(0, QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Circular", None))
        self.comboBubbleShape.setItemText(1, QCoreApplication.translate("TechDrawGui::TaskBalloon", u"None", None))
        self.comboBubbleShape.setItemText(2, QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Triangle", None))
        self.comboBubbleShape.setItemText(3, QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Inspection", None))
        self.comboBubbleShape.setItemText(4, QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Hexagon", None))
        self.comboBubbleShape.setItemText(5, QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Square", None))
        self.comboBubbleShape.setItemText(6, QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Rectangle", None))
        self.comboBubbleShape.setItemText(7, QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Line", None))

#if QT_CONFIG(tooltip)
        self.comboBubbleShape.setToolTip(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Shape of the balloon bubble", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Shape scale", None))
#if QT_CONFIG(tooltip)
        self.qsbShapeScale.setToolTip(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Bubble shape scale factor", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"End symbol", None))
#if QT_CONFIG(tooltip)
        self.comboEndSymbol.setToolTip(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"End symbol for the balloon line", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"End symbol scale", None))
#if QT_CONFIG(tooltip)
        self.qsbSymbolScale.setToolTip(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"End symbol scale factor", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Line visible", None))
        self.comboLineVisible.setItemText(0, QCoreApplication.translate("TechDrawGui::TaskBalloon", u"False", None))
        self.comboLineVisible.setItemText(1, QCoreApplication.translate("TechDrawGui::TaskBalloon", u"True", None))

#if QT_CONFIG(tooltip)
        self.comboLineVisible.setToolTip(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Controls whether the leader line is visible or not", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Line width", None))
#if QT_CONFIG(tooltip)
        self.qsbLineWidth.setToolTip(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Leader line width", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Leader kink length", None))
#if QT_CONFIG(tooltip)
        self.qsbKinkLength.setToolTip(QCoreApplication.translate("TechDrawGui::TaskBalloon", u"Length of balloon leader line kink", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

