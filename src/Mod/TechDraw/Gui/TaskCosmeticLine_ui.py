# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskCosmeticLine.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QLabel,
    QLineEdit, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_TechDrawGui_TaskCosmeticLine(object):
    def setupUi(self, TechDrawGui__TaskCosmeticLine):
        if not TechDrawGui__TaskCosmeticLine.objectName():
            TechDrawGui__TaskCosmeticLine.setObjectName(u"TechDrawGui__TaskCosmeticLine")
        TechDrawGui__TaskCosmeticLine.resize(350, 331)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskCosmeticLine.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskCosmeticLine.setSizePolicy(sizePolicy)
        TechDrawGui__TaskCosmeticLine.setMinimumSize(QSize(250, 0))
        self.verticalLayout = QVBoxLayout(TechDrawGui__TaskCosmeticLine)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(TechDrawGui__TaskCosmeticLine)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.le_View = QLineEdit(TechDrawGui__TaskCosmeticLine)
        self.le_View.setObjectName(u"le_View")
        self.le_View.setEnabled(False)
        self.le_View.setMouseTracking(False)
        self.le_View.setFocusPolicy(Qt.NoFocus)
        self.le_View.setAcceptDrops(False)

        self.gridLayout.addWidget(self.le_View, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rb2d1 = QRadioButton(TechDrawGui__TaskCosmeticLine)
        self.buttonGroup = QButtonGroup(TechDrawGui__TaskCosmeticLine)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.rb2d1)
        self.rb2d1.setObjectName(u"rb2d1")
        self.rb2d1.setChecked(True)
        self.rb2d1.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.rb2d1, 0, 0, 1, 1)

        self.rb3d1 = QRadioButton(TechDrawGui__TaskCosmeticLine)
        self.buttonGroup.addButton(self.rb3d1)
        self.rb3d1.setObjectName(u"rb3d1")
        self.rb3d1.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.rb3d1, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(TechDrawGui__TaskCosmeticLine)
        self.label.setObjectName(u"label")
        self.label.setText(u"X")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.qsbx1 = Gui_QuantitySpinBox(TechDrawGui__TaskCosmeticLine)
        self.qsbx1.setObjectName(u"qsbx1")
        self.qsbx1.setProperty(u"unit", u"")

        self.gridLayout_3.addWidget(self.qsbx1, 0, 1, 1, 1)

        self.label_2 = QLabel(TechDrawGui__TaskCosmeticLine)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"Y")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.qsby1 = Gui_QuantitySpinBox(TechDrawGui__TaskCosmeticLine)
        self.qsby1.setObjectName(u"qsby1")
        self.qsby1.setProperty(u"unit", u"")

        self.gridLayout_3.addWidget(self.qsby1, 1, 1, 1, 1)

        self.label_3 = QLabel(TechDrawGui__TaskCosmeticLine)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"Z")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.qsbz1 = Gui_QuantitySpinBox(TechDrawGui__TaskCosmeticLine)
        self.qsbz1.setObjectName(u"qsbz1")
        self.qsbz1.setProperty(u"unit", u"")

        self.gridLayout_3.addWidget(self.qsbz1, 2, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 4)

        self.verticalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.rb2d2 = QRadioButton(TechDrawGui__TaskCosmeticLine)
        self.buttonGroup_2 = QButtonGroup(TechDrawGui__TaskCosmeticLine)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.rb2d2)
        self.rb2d2.setObjectName(u"rb2d2")
        self.rb2d2.setChecked(True)
        self.rb2d2.setAutoExclusive(True)

        self.gridLayout_4.addWidget(self.rb2d2, 0, 0, 1, 1)

        self.rb3d2 = QRadioButton(TechDrawGui__TaskCosmeticLine)
        self.buttonGroup_2.addButton(self.rb3d2)
        self.rb3d2.setObjectName(u"rb3d2")
        self.rb3d2.setAutoExclusive(True)

        self.gridLayout_4.addWidget(self.rb3d2, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_5 = QLabel(TechDrawGui__TaskCosmeticLine)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setText(u"X")

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.qsbx2 = Gui_QuantitySpinBox(TechDrawGui__TaskCosmeticLine)
        self.qsbx2.setObjectName(u"qsbx2")
        self.qsbx2.setProperty(u"unit", u"")

        self.gridLayout_5.addWidget(self.qsbx2, 0, 1, 1, 1)

        self.label_6 = QLabel(TechDrawGui__TaskCosmeticLine)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setText(u"Y")

        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)

        self.qsby2 = Gui_QuantitySpinBox(TechDrawGui__TaskCosmeticLine)
        self.qsby2.setObjectName(u"qsby2")
        self.qsby2.setProperty(u"unit", u"")

        self.gridLayout_5.addWidget(self.qsby2, 1, 1, 1, 1)

        self.label_7 = QLabel(TechDrawGui__TaskCosmeticLine)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setText(u"Z")

        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)

        self.qsbz2 = Gui_QuantitySpinBox(TechDrawGui__TaskCosmeticLine)
        self.qsbz2.setObjectName(u"qsbz2")
        self.qsbz2.setProperty(u"unit", u"")

        self.gridLayout_5.addWidget(self.qsbz2, 2, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 4)

        self.verticalLayout.addLayout(self.gridLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TechDrawGui__TaskCosmeticLine)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskCosmeticLine)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskCosmeticLine):
        TechDrawGui__TaskCosmeticLine.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskCosmeticLine", u"Cosmetic Line", None))
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticLine", u"View", None))
        self.rb2d1.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticLine", u"2D point", None))
        self.rb3d1.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticLine", u"3D point", None))
        self.rb2d2.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticLine", u"2D point", None))
        self.rb3d2.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticLine", u"3D point", None))
    # retranslateUi

