# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskCosmeticCircle.ui'
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
    QLineEdit, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_TechDrawGui_TaskCosmeticCircle(object):
    def setupUi(self, TechDrawGui__TaskCosmeticCircle):
        if not TechDrawGui__TaskCosmeticCircle.objectName():
            TechDrawGui__TaskCosmeticCircle.setObjectName(u"TechDrawGui__TaskCosmeticCircle")
        TechDrawGui__TaskCosmeticCircle.resize(350, 409)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskCosmeticCircle.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskCosmeticCircle.setSizePolicy(sizePolicy)
        TechDrawGui__TaskCosmeticCircle.setMinimumSize(QSize(250, 0))
        self.verticalLayout = QVBoxLayout(TechDrawGui__TaskCosmeticCircle)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(TechDrawGui__TaskCosmeticCircle)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.le_View = QLineEdit(TechDrawGui__TaskCosmeticCircle)
        self.le_View.setObjectName(u"le_View")
        self.le_View.setEnabled(False)
        self.le_View.setMouseTracking(False)
        self.le_View.setFocusPolicy(Qt.NoFocus)
        self.le_View.setAcceptDrops(False)

        self.gridLayout.addWidget(self.le_View, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rb2d1 = QRadioButton(TechDrawGui__TaskCosmeticCircle)
        self.rb2d1.setObjectName(u"rb2d1")
        self.rb2d1.setChecked(True)
        self.rb2d1.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.rb2d1, 1, 0, 1, 1)

        self.rb3d1 = QRadioButton(TechDrawGui__TaskCosmeticCircle)
        self.rb3d1.setObjectName(u"rb3d1")
        self.rb3d1.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.rb3d1, 1, 1, 1, 1)

        self.label_8 = QLabel(TechDrawGui__TaskCosmeticCircle)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(TechDrawGui__TaskCosmeticCircle)
        self.label.setObjectName(u"label")
        self.label.setText(u"X")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.qsbCenterX = Gui_QuantitySpinBox(TechDrawGui__TaskCosmeticCircle)
        self.qsbCenterX.setObjectName(u"qsbCenterX")
        self.qsbCenterX.setProperty(u"unit", u"")

        self.gridLayout_3.addWidget(self.qsbCenterX, 0, 1, 1, 1)

        self.label_2 = QLabel(TechDrawGui__TaskCosmeticCircle)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"Y")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.qsbCenterY = Gui_QuantitySpinBox(TechDrawGui__TaskCosmeticCircle)
        self.qsbCenterY.setObjectName(u"qsbCenterY")
        self.qsbCenterY.setProperty(u"unit", u"")

        self.gridLayout_3.addWidget(self.qsbCenterY, 1, 1, 1, 1)

        self.label_3 = QLabel(TechDrawGui__TaskCosmeticCircle)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"Z")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.qsbCenterZ = Gui_QuantitySpinBox(TechDrawGui__TaskCosmeticCircle)
        self.qsbCenterZ.setObjectName(u"qsbCenterZ")
        self.qsbCenterZ.setProperty(u"unit", u"")

        self.gridLayout_3.addWidget(self.qsbCenterZ, 2, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 4)

        self.verticalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_9 = QLabel(TechDrawGui__TaskCosmeticCircle)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.qsbRadius = Gui_QuantitySpinBox(TechDrawGui__TaskCosmeticCircle)
        self.qsbRadius.setObjectName(u"qsbRadius")
        self.qsbRadius.setProperty(u"unit", u"")
        self.qsbRadius.setProperty(u"minimum", 0.000000000000000)
        self.qsbRadius.setProperty(u"value", 10.000000000000000)

        self.gridLayout_4.addWidget(self.qsbRadius, 0, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 4)

        self.verticalLayout.addLayout(self.gridLayout_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.qsbStartAngle = Gui_QuantitySpinBox(TechDrawGui__TaskCosmeticCircle)
        self.qsbStartAngle.setObjectName(u"qsbStartAngle")
        self.qsbStartAngle.setProperty(u"unit", u"")

        self.gridLayout_5.addWidget(self.qsbStartAngle, 1, 1, 1, 1)

        self.label_6 = QLabel(TechDrawGui__TaskCosmeticCircle)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)

        self.cbClockwise = QCheckBox(TechDrawGui__TaskCosmeticCircle)
        self.cbClockwise.setObjectName(u"cbClockwise")

        self.gridLayout_5.addWidget(self.cbClockwise, 3, 0, 1, 1)

        self.qsbEndAngle = Gui_QuantitySpinBox(TechDrawGui__TaskCosmeticCircle)
        self.qsbEndAngle.setObjectName(u"qsbEndAngle")
        self.qsbEndAngle.setProperty(u"unit", u"")

        self.gridLayout_5.addWidget(self.qsbEndAngle, 2, 1, 1, 1)

        self.label_5 = QLabel(TechDrawGui__TaskCosmeticCircle)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)

        self.rbArc = QRadioButton(TechDrawGui__TaskCosmeticCircle)
        self.rbArc.setObjectName(u"rbArc")

        self.gridLayout_5.addWidget(self.rbArc, 0, 0, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)

        self.verticalLayout.addLayout(self.gridLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TechDrawGui__TaskCosmeticCircle)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskCosmeticCircle)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskCosmeticCircle):
        TechDrawGui__TaskCosmeticCircle.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"Cosmetic Circle", None))
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"View", None))
#if QT_CONFIG(tooltip)
        self.rb2d1.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"Treats the center point as a 2D point within the parent view. The Z coordinate is ignored.", None))
#endif // QT_CONFIG(tooltip)
        self.rb2d1.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"2D point", None))
#if QT_CONFIG(tooltip)
        self.rb3d1.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"Treats the center point as a 3D point and project it onto the parent view", None))
#endif // QT_CONFIG(tooltip)
        self.rb3d1.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"3D point", None))
        self.label_8.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"Circle center", None))
        self.label_9.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"Radius", None))
#if QT_CONFIG(tooltip)
        self.qsbStartAngle.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"Start angle (conventional) of arc in degrees.", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"End angle", None))
#if QT_CONFIG(tooltip)
        self.cbClockwise.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"Creates an arc from start angle to end angle in a clockwise direction", None))
#endif // QT_CONFIG(tooltip)
        self.cbClockwise.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"Clockwise Angle", None))
#if QT_CONFIG(tooltip)
        self.qsbEndAngle.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"End angle (conventional) of arc in degrees", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"Start angle", None))
#if QT_CONFIG(tooltip)
        self.rbArc.setToolTip(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"Uses angles and create a circular arc", None))
#endif // QT_CONFIG(tooltip)
        self.rbArc.setText(QCoreApplication.translate("TechDrawGui::TaskCosmeticCircle", u"Arc of circle", None))
    # retranslateUi

