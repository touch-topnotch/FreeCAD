# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskLineDecor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskLineDecor(object):
    def setupUi(self, TechDrawGui__TaskLineDecor):
        if not TechDrawGui__TaskLineDecor.objectName():
            TechDrawGui__TaskLineDecor.setObjectName(u"TechDrawGui__TaskLineDecor")
        TechDrawGui__TaskLineDecor.resize(355, 311)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskLineDecor.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskLineDecor.setSizePolicy(sizePolicy)
        TechDrawGui__TaskLineDecor.setMinimumSize(QSize(250, 0))
        self.verticalLayout = QVBoxLayout(TechDrawGui__TaskLineDecor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cc_Color = Gui_ColorButton(TechDrawGui__TaskLineDecor)
        self.cc_Color.setObjectName(u"cc_Color")
        self.cc_Color.setColor(QColor(0, 0, 0))

        self.gridLayout.addWidget(self.cc_Color, 5, 2, 1, 1)

        self.label_15 = QLabel(TechDrawGui__TaskLineDecor)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 6, 0, 1, 1)

        self.label_10 = QLabel(TechDrawGui__TaskLineDecor)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.cb_Visible = QComboBox(TechDrawGui__TaskLineDecor)
        self.cb_Visible.addItem("")
        self.cb_Visible.addItem("")
        self.cb_Visible.setObjectName(u"cb_Visible")
        self.cb_Visible.setMaxVisibleItems(2)
        self.cb_Visible.setMaxCount(2)
        self.cb_Visible.setMinimumContentsLength(2)

        self.gridLayout.addWidget(self.cb_Visible, 7, 2, 1, 1)

        self.label_14 = QLabel(TechDrawGui__TaskLineDecor)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 5, 0, 1, 1)

        self.label_4 = QLabel(TechDrawGui__TaskLineDecor)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.cb_Style = QComboBox(TechDrawGui__TaskLineDecor)
        self.cb_Style.setObjectName(u"cb_Style")
        self.cb_Style.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.cb_Style, 4, 2, 1, 1)

        self.label_6 = QLabel(TechDrawGui__TaskLineDecor)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 4, 1, 1, 1)

        self.line = QFrame(TechDrawGui__TaskLineDecor)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 3)

        self.dsb_Weight = Gui_QuantitySpinBox(TechDrawGui__TaskLineDecor)
        self.dsb_Weight.setObjectName(u"dsb_Weight")
        self.dsb_Weight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsb_Weight.setValue(0.500000000000000)

        self.gridLayout.addWidget(self.dsb_Weight, 6, 2, 1, 1)

        self.label = QLabel(TechDrawGui__TaskLineDecor)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)

        self.le_Lines = QLineEdit(TechDrawGui__TaskLineDecor)
        self.le_Lines.setObjectName(u"le_Lines")
        self.le_Lines.setEnabled(False)

        self.gridLayout.addWidget(self.le_Lines, 1, 2, 1, 1)

        self.le_View = QLineEdit(TechDrawGui__TaskLineDecor)
        self.le_View.setObjectName(u"le_View")
        self.le_View.setEnabled(False)
        self.le_View.setMouseTracking(False)
        self.le_View.setFocusPolicy(Qt.NoFocus)
        self.le_View.setAcceptDrops(False)

        self.gridLayout.addWidget(self.le_View, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TechDrawGui__TaskLineDecor)

        self.cb_Visible.setCurrentIndex(1)
        self.cb_Style.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(TechDrawGui__TaskLineDecor)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskLineDecor):
        TechDrawGui__TaskLineDecor.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskLineDecor", u"Line Decoration", None))
        self.label_15.setText(QCoreApplication.translate("TechDrawGui::TaskLineDecor", u"Weight", None))
        self.label_10.setText(QCoreApplication.translate("TechDrawGui::TaskLineDecor", u"Lines", None))
        self.cb_Visible.setItemText(0, QCoreApplication.translate("TechDrawGui::TaskLineDecor", u"False", None))
        self.cb_Visible.setItemText(1, QCoreApplication.translate("TechDrawGui::TaskLineDecor", u"True", None))

        self.label_14.setText(QCoreApplication.translate("TechDrawGui::TaskLineDecor", u"Color", None))
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::TaskLineDecor", u"View", None))
#if QT_CONFIG(tooltip)
        self.cb_Style.setToolTip(QCoreApplication.translate("TechDrawGui::TaskLineDecor", u"The use of the Qt line style is being phased out. Use a standard line style instead.", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::TaskLineDecor", u"Style", None))
#if QT_CONFIG(tooltip)
        self.dsb_Weight.setToolTip(QCoreApplication.translate("TechDrawGui::TaskLineDecor", u"Thickness of pattern lines", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskLineDecor", u"Visible", None))
    # retranslateUi

