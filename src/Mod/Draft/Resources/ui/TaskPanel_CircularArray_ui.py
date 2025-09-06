# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskPanel_CircularArray.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_DraftCircularArrayTaskPanel(object):
    def setupUi(self, DraftCircularArrayTaskPanel):
        if not DraftCircularArrayTaskPanel.objectName():
            DraftCircularArrayTaskPanel.setObjectName(u"DraftCircularArrayTaskPanel")
        DraftCircularArrayTaskPanel.resize(445, 511)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DraftCircularArrayTaskPanel.sizePolicy().hasHeightForWidth())
        DraftCircularArrayTaskPanel.setSizePolicy(sizePolicy)
        DraftCircularArrayTaskPanel.setMinimumSize(QSize(250, 0))
        self.gridLayout_3 = QGridLayout(DraftCircularArrayTaskPanel)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.grid_values = QGridLayout()
        self.grid_values.setObjectName(u"grid_values")
        self.label_r_distance = QLabel(DraftCircularArrayTaskPanel)
        self.label_r_distance.setObjectName(u"label_r_distance")

        self.grid_values.addWidget(self.label_r_distance, 0, 0, 1, 1)

        self.spinbox_r_distance = Gui_QuantitySpinBox(DraftCircularArrayTaskPanel)
        self.spinbox_r_distance.setObjectName(u"spinbox_r_distance")
        self.spinbox_r_distance.setProperty(u"unit", u"mm")
        self.spinbox_r_distance.setValue(200.000000000000000)

        self.grid_values.addWidget(self.spinbox_r_distance, 0, 1, 1, 1)

        self.label_tan_distance = QLabel(DraftCircularArrayTaskPanel)
        self.label_tan_distance.setObjectName(u"label_tan_distance")

        self.grid_values.addWidget(self.label_tan_distance, 1, 0, 1, 1)

        self.spinbox_tan_distance = Gui_QuantitySpinBox(DraftCircularArrayTaskPanel)
        self.spinbox_tan_distance.setObjectName(u"spinbox_tan_distance")
        self.spinbox_tan_distance.setProperty(u"unit", u"mm")
        self.spinbox_tan_distance.setValue(100.000000000000000)

        self.grid_values.addWidget(self.spinbox_tan_distance, 1, 1, 1, 1)

        self.label_number = QLabel(DraftCircularArrayTaskPanel)
        self.label_number.setObjectName(u"label_number")

        self.grid_values.addWidget(self.label_number, 2, 0, 1, 1)

        self.spinbox_number = QSpinBox(DraftCircularArrayTaskPanel)
        self.spinbox_number.setObjectName(u"spinbox_number")
        self.spinbox_number.setMinimum(2)
        self.spinbox_number.setMaximum(1000000)
        self.spinbox_number.setValue(3)

        self.grid_values.addWidget(self.spinbox_number, 2, 1, 1, 1)

        self.label_symmetry = QLabel(DraftCircularArrayTaskPanel)
        self.label_symmetry.setObjectName(u"label_symmetry")

        self.grid_values.addWidget(self.label_symmetry, 3, 0, 1, 1)

        self.spinbox_symmetry = QSpinBox(DraftCircularArrayTaskPanel)
        self.spinbox_symmetry.setObjectName(u"spinbox_symmetry")
        self.spinbox_symmetry.setMinimum(1)
        self.spinbox_symmetry.setValue(1)

        self.grid_values.addWidget(self.spinbox_symmetry, 3, 1, 1, 1)


        self.gridLayout_3.addLayout(self.grid_values, 0, 0, 1, 1)

        self.group_center = QGroupBox(DraftCircularArrayTaskPanel)
        self.group_center.setObjectName(u"group_center")
        self.gridLayout_2 = QGridLayout(self.group_center)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_c_x = QLabel(self.group_center)
        self.label_c_x.setObjectName(u"label_c_x")

        self.gridLayout.addWidget(self.label_c_x, 0, 0, 1, 1)

        self.input_c_x = Gui_InputField(self.group_center)
        self.input_c_x.setObjectName(u"input_c_x")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_c_x.sizePolicy().hasHeightForWidth())
        self.input_c_x.setSizePolicy(sizePolicy1)
        self.input_c_x.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.input_c_x, 0, 1, 1, 1)

        self.label_c_y = QLabel(self.group_center)
        self.label_c_y.setObjectName(u"label_c_y")

        self.gridLayout.addWidget(self.label_c_y, 1, 0, 1, 1)

        self.input_c_y = Gui_InputField(self.group_center)
        self.input_c_y.setObjectName(u"input_c_y")
        sizePolicy1.setHeightForWidth(self.input_c_y.sizePolicy().hasHeightForWidth())
        self.input_c_y.setSizePolicy(sizePolicy1)
        self.input_c_y.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.input_c_y, 1, 1, 1, 1)

        self.label_c_z = QLabel(self.group_center)
        self.label_c_z.setObjectName(u"label_c_z")

        self.gridLayout.addWidget(self.label_c_z, 2, 0, 1, 1)

        self.input_c_z = Gui_InputField(self.group_center)
        self.input_c_z.setObjectName(u"input_c_z")
        sizePolicy1.setHeightForWidth(self.input_c_z.sizePolicy().hasHeightForWidth())
        self.input_c_z.setSizePolicy(sizePolicy1)
        self.input_c_z.setProperty(u"unit", u"mm")

        self.gridLayout.addWidget(self.input_c_z, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.button_reset = QPushButton(self.group_center)
        self.button_reset.setObjectName(u"button_reset")

        self.gridLayout_2.addWidget(self.button_reset, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.group_center, 1, 0, 1, 1)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.checkbox_fuse = QCheckBox(DraftCircularArrayTaskPanel)
        self.checkbox_fuse.setObjectName(u"checkbox_fuse")

        self.vertical_layout.addWidget(self.checkbox_fuse)

        self.checkbox_link = QCheckBox(DraftCircularArrayTaskPanel)
        self.checkbox_link.setObjectName(u"checkbox_link")
        self.checkbox_link.setChecked(True)

        self.vertical_layout.addWidget(self.checkbox_link)


        self.gridLayout_3.addLayout(self.vertical_layout, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 1)

        QWidget.setTabOrder(self.spinbox_r_distance, self.spinbox_tan_distance)
        QWidget.setTabOrder(self.spinbox_tan_distance, self.spinbox_number)
        QWidget.setTabOrder(self.spinbox_number, self.spinbox_symmetry)
        QWidget.setTabOrder(self.spinbox_symmetry, self.input_c_x)
        QWidget.setTabOrder(self.input_c_x, self.input_c_y)
        QWidget.setTabOrder(self.input_c_y, self.input_c_z)
        QWidget.setTabOrder(self.input_c_z, self.button_reset)
        QWidget.setTabOrder(self.button_reset, self.checkbox_fuse)
        QWidget.setTabOrder(self.checkbox_fuse, self.checkbox_link)

        self.retranslateUi(DraftCircularArrayTaskPanel)

        QMetaObject.connectSlotsByName(DraftCircularArrayTaskPanel)
    # setupUi

    def retranslateUi(self, DraftCircularArrayTaskPanel):
        DraftCircularArrayTaskPanel.setWindowTitle(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Circular Array", None))
#if QT_CONFIG(tooltip)
        self.label_r_distance.setToolTip(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Distance from one layer of objects to the next layer of objects", None))
#endif // QT_CONFIG(tooltip)
        self.label_r_distance.setText(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Radial distance", None))
#if QT_CONFIG(tooltip)
        self.spinbox_r_distance.setToolTip(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Distance from one layer of objects to the next layer of objects", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_tan_distance.setToolTip(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Distance from one element in one ring of the array to the next element in the same ring.\n"
"It cannot be zero.", None))
#endif // QT_CONFIG(tooltip)
        self.label_tan_distance.setText(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Tangential distance", None))
#if QT_CONFIG(tooltip)
        self.spinbox_tan_distance.setToolTip(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Distance from one element in one ring of the array to the next element in the same ring.\n"
"It cannot be zero.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_number.setToolTip(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Number of concentric circles to create, including a copy of the original object.\n"
"It must be at least 2.", None))
#endif // QT_CONFIG(tooltip)
        self.label_number.setText(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Number of concentric circles", None))
#if QT_CONFIG(tooltip)
        self.spinbox_number.setToolTip(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Number of concentric circles to create, including a copy of the original object.\n"
"It must be at least 2.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_symmetry.setToolTip(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"The number of symmetry lines in the circular array", None))
#endif // QT_CONFIG(tooltip)
        self.label_symmetry.setText(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Symmetry", None))
#if QT_CONFIG(tooltip)
        self.spinbox_symmetry.setToolTip(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"The number of symmetry lines in the circular array", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.group_center.setToolTip(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"The coordinates of the point through which the axis of rotation passes.\n"
"Change the direction of the axis itself in the property editor.", None))
#endif // QT_CONFIG(tooltip)
        self.group_center.setTitle(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Center of Rotation", None))
        self.label_c_x.setText(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"X", None))
        self.label_c_y.setText(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Y", None))
        self.label_c_z.setText(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Z", None))
#if QT_CONFIG(tooltip)
        self.button_reset.setToolTip(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Resets the coordinates of the center of rotation", None))
#endif // QT_CONFIG(tooltip)
        self.button_reset.setText(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Reset Point", None))
#if QT_CONFIG(tooltip)
        self.checkbox_fuse.setToolTip(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"If checked, the resulting objects in the array will be fused if they touch each other.\n"
"This only works if \"Link array\" is off.", None))
#endif // QT_CONFIG(tooltip)
        self.checkbox_fuse.setText(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Fuse", None))
#if QT_CONFIG(tooltip)
        self.checkbox_link.setToolTip(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"If checked, the resulting object will be a \"Link array\" instead of a regular array.\n"
"A Link array is more efficient when creating multiple copies, but it cannot be fused together.", None))
#endif // QT_CONFIG(tooltip)
        self.checkbox_link.setText(QCoreApplication.translate("DraftCircularArrayTaskPanel", u"Link array", None))
    # retranslateUi

