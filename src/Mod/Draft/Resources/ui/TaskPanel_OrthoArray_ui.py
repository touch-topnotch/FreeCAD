# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskPanel_OrthoArray.ui'
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

class Ui_DraftOrthoArrayTaskPanel(object):
    def setupUi(self, DraftOrthoArrayTaskPanel):
        if not DraftOrthoArrayTaskPanel.objectName():
            DraftOrthoArrayTaskPanel.setObjectName(u"DraftOrthoArrayTaskPanel")
        DraftOrthoArrayTaskPanel.resize(440, 883)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DraftOrthoArrayTaskPanel.sizePolicy().hasHeightForWidth())
        DraftOrthoArrayTaskPanel.setSizePolicy(sizePolicy)
        DraftOrthoArrayTaskPanel.setMinimumSize(QSize(250, 0))
        self.gridLayout_3 = QGridLayout(DraftOrthoArrayTaskPanel)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.main_group = QGroupBox(DraftOrthoArrayTaskPanel)
        self.main_group.setObjectName(u"main_group")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_group.sizePolicy().hasHeightForWidth())
        self.main_group.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.main_group)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_icon = QLabel(self.main_group)
        self.label_icon.setObjectName(u"label_icon")
        self.label_icon.setText(u"(Placeholder for the icon)")

        self.gridLayout_4.addWidget(self.label_icon, 0, 0, 1, 1)

        self.group_copies = QGroupBox(self.main_group)
        self.group_copies.setObjectName(u"group_copies")
        self.gridLayout_5 = QGridLayout(self.group_copies)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.grid_number = QGridLayout()
        self.grid_number.setObjectName(u"grid_number")
        self.label_n_X = QLabel(self.group_copies)
        self.label_n_X.setObjectName(u"label_n_X")

        self.grid_number.addWidget(self.label_n_X, 0, 0, 1, 1)

        self.spinbox_n_X = QSpinBox(self.group_copies)
        self.spinbox_n_X.setObjectName(u"spinbox_n_X")
        self.spinbox_n_X.setMinimum(1)
        self.spinbox_n_X.setMaximum(1000000)
        self.spinbox_n_X.setValue(2)

        self.grid_number.addWidget(self.spinbox_n_X, 0, 1, 1, 1)

        self.label_n_Y = QLabel(self.group_copies)
        self.label_n_Y.setObjectName(u"label_n_Y")

        self.grid_number.addWidget(self.label_n_Y, 1, 0, 1, 1)

        self.spinbox_n_Y = QSpinBox(self.group_copies)
        self.spinbox_n_Y.setObjectName(u"spinbox_n_Y")
        self.spinbox_n_Y.setMinimum(1)
        self.spinbox_n_Y.setMaximum(1000000)
        self.spinbox_n_Y.setValue(2)

        self.grid_number.addWidget(self.spinbox_n_Y, 1, 1, 1, 1)

        self.label_n_Z = QLabel(self.group_copies)
        self.label_n_Z.setObjectName(u"label_n_Z")

        self.grid_number.addWidget(self.label_n_Z, 2, 0, 1, 1)

        self.spinbox_n_Z = QSpinBox(self.group_copies)
        self.spinbox_n_Z.setObjectName(u"spinbox_n_Z")
        self.spinbox_n_Z.setMinimum(1)
        self.spinbox_n_Z.setMaximum(1000000)
        self.spinbox_n_Z.setValue(1)

        self.grid_number.addWidget(self.spinbox_n_Z, 2, 1, 1, 1)


        self.gridLayout_5.addLayout(self.grid_number, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.group_copies, 1, 0, 1, 1)

        self.group_X = QGroupBox(self.main_group)
        self.group_X.setObjectName(u"group_X")
        self.gridLayout_2 = QGridLayout(self.group_X)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.grid_X = QGridLayout()
        self.grid_X.setObjectName(u"grid_X")
        self.label_X_x = QLabel(self.group_X)
        self.label_X_x.setObjectName(u"label_X_x")

        self.grid_X.addWidget(self.label_X_x, 0, 0, 1, 1)

        self.input_X_x = Gui_InputField(self.group_X)
        self.input_X_x.setObjectName(u"input_X_x")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_X_x.sizePolicy().hasHeightForWidth())
        self.input_X_x.setSizePolicy(sizePolicy2)
        self.input_X_x.setProperty(u"unit", u"")
        self.input_X_x.setProperty(u"quantity", 100.000000000000000)

        self.grid_X.addWidget(self.input_X_x, 0, 1, 1, 1)

        self.label_X_y = QLabel(self.group_X)
        self.label_X_y.setObjectName(u"label_X_y")

        self.grid_X.addWidget(self.label_X_y, 1, 0, 1, 1)

        self.input_X_y = Gui_InputField(self.group_X)
        self.input_X_y.setObjectName(u"input_X_y")
        sizePolicy2.setHeightForWidth(self.input_X_y.sizePolicy().hasHeightForWidth())
        self.input_X_y.setSizePolicy(sizePolicy2)
        self.input_X_y.setProperty(u"unit", u"")

        self.grid_X.addWidget(self.input_X_y, 1, 1, 1, 1)

        self.label_X_z = QLabel(self.group_X)
        self.label_X_z.setObjectName(u"label_X_z")

        self.grid_X.addWidget(self.label_X_z, 2, 0, 1, 1)

        self.input_X_z = Gui_InputField(self.group_X)
        self.input_X_z.setObjectName(u"input_X_z")
        sizePolicy2.setHeightForWidth(self.input_X_z.sizePolicy().hasHeightForWidth())
        self.input_X_z.setSizePolicy(sizePolicy2)
        self.input_X_z.setProperty(u"unit", u"")

        self.grid_X.addWidget(self.input_X_z, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.grid_X, 0, 0, 1, 1)

        self.button_reset_X = QPushButton(self.group_X)
        self.button_reset_X.setObjectName(u"button_reset_X")

        self.gridLayout_2.addWidget(self.button_reset_X, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.group_X, 4, 0, 1, 1)

        self.group_Y = QGroupBox(self.main_group)
        self.group_Y.setObjectName(u"group_Y")
        self.gridLayout_6 = QGridLayout(self.group_Y)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.grid_Y = QGridLayout()
        self.grid_Y.setObjectName(u"grid_Y")
        self.label_Y_x = QLabel(self.group_Y)
        self.label_Y_x.setObjectName(u"label_Y_x")

        self.grid_Y.addWidget(self.label_Y_x, 0, 0, 1, 1)

        self.input_Y_x = Gui_InputField(self.group_Y)
        self.input_Y_x.setObjectName(u"input_Y_x")
        sizePolicy2.setHeightForWidth(self.input_Y_x.sizePolicy().hasHeightForWidth())
        self.input_Y_x.setSizePolicy(sizePolicy2)
        self.input_Y_x.setProperty(u"unit", u"")

        self.grid_Y.addWidget(self.input_Y_x, 0, 1, 1, 1)

        self.label_Y_y = QLabel(self.group_Y)
        self.label_Y_y.setObjectName(u"label_Y_y")

        self.grid_Y.addWidget(self.label_Y_y, 1, 0, 1, 1)

        self.input_Y_y = Gui_InputField(self.group_Y)
        self.input_Y_y.setObjectName(u"input_Y_y")
        sizePolicy2.setHeightForWidth(self.input_Y_y.sizePolicy().hasHeightForWidth())
        self.input_Y_y.setSizePolicy(sizePolicy2)
        self.input_Y_y.setProperty(u"unit", u"")
        self.input_Y_y.setProperty(u"quantity", 100.000000000000000)

        self.grid_Y.addWidget(self.input_Y_y, 1, 1, 1, 1)

        self.label_Y_z = QLabel(self.group_Y)
        self.label_Y_z.setObjectName(u"label_Y_z")

        self.grid_Y.addWidget(self.label_Y_z, 2, 0, 1, 1)

        self.input_Y_z = Gui_InputField(self.group_Y)
        self.input_Y_z.setObjectName(u"input_Y_z")
        sizePolicy2.setHeightForWidth(self.input_Y_z.sizePolicy().hasHeightForWidth())
        self.input_Y_z.setSizePolicy(sizePolicy2)
        self.input_Y_z.setProperty(u"unit", u"")

        self.grid_Y.addWidget(self.input_Y_z, 2, 1, 1, 1)


        self.gridLayout_6.addLayout(self.grid_Y, 0, 0, 1, 1)

        self.button_reset_Y = QPushButton(self.group_Y)
        self.button_reset_Y.setObjectName(u"button_reset_Y")

        self.gridLayout_6.addWidget(self.button_reset_Y, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.group_Y, 5, 0, 1, 1)

        self.group_Z = QGroupBox(self.main_group)
        self.group_Z.setObjectName(u"group_Z")
        self.gridLayout = QGridLayout(self.group_Z)
        self.gridLayout.setObjectName(u"gridLayout")
        self.grid_Z = QGridLayout()
        self.grid_Z.setObjectName(u"grid_Z")
        self.label_Z_x = QLabel(self.group_Z)
        self.label_Z_x.setObjectName(u"label_Z_x")

        self.grid_Z.addWidget(self.label_Z_x, 0, 0, 1, 1)

        self.input_Z_x = Gui_InputField(self.group_Z)
        self.input_Z_x.setObjectName(u"input_Z_x")
        sizePolicy2.setHeightForWidth(self.input_Z_x.sizePolicy().hasHeightForWidth())
        self.input_Z_x.setSizePolicy(sizePolicy2)
        self.input_Z_x.setProperty(u"unit", u"")

        self.grid_Z.addWidget(self.input_Z_x, 0, 1, 1, 1)

        self.label_Z_y = QLabel(self.group_Z)
        self.label_Z_y.setObjectName(u"label_Z_y")

        self.grid_Z.addWidget(self.label_Z_y, 1, 0, 1, 1)

        self.input_Z_y = Gui_InputField(self.group_Z)
        self.input_Z_y.setObjectName(u"input_Z_y")
        sizePolicy2.setHeightForWidth(self.input_Z_y.sizePolicy().hasHeightForWidth())
        self.input_Z_y.setSizePolicy(sizePolicy2)
        self.input_Z_y.setProperty(u"unit", u"")

        self.grid_Z.addWidget(self.input_Z_y, 1, 1, 1, 1)

        self.label_Z_z = QLabel(self.group_Z)
        self.label_Z_z.setObjectName(u"label_Z_z")

        self.grid_Z.addWidget(self.label_Z_z, 2, 0, 1, 1)

        self.input_Z_z = Gui_InputField(self.group_Z)
        self.input_Z_z.setObjectName(u"input_Z_z")
        sizePolicy2.setHeightForWidth(self.input_Z_z.sizePolicy().hasHeightForWidth())
        self.input_Z_z.setSizePolicy(sizePolicy2)
        self.input_Z_z.setProperty(u"unit", u"")
        self.input_Z_z.setProperty(u"quantity", 100.000000000000000)

        self.grid_Z.addWidget(self.input_Z_z, 2, 1, 1, 1)


        self.gridLayout.addLayout(self.grid_Z, 0, 0, 1, 1)

        self.button_reset_Z = QPushButton(self.group_Z)
        self.button_reset_Z.setObjectName(u"button_reset_Z")

        self.gridLayout.addWidget(self.button_reset_Z, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.group_Z, 6, 0, 1, 1)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.checkbox_fuse = QCheckBox(self.main_group)
        self.checkbox_fuse.setObjectName(u"checkbox_fuse")

        self.vertical_layout.addWidget(self.checkbox_fuse)

        self.checkbox_link = QCheckBox(self.main_group)
        self.checkbox_link.setObjectName(u"checkbox_link")
        self.checkbox_link.setChecked(True)

        self.vertical_layout.addWidget(self.checkbox_link)


        self.gridLayout_4.addLayout(self.vertical_layout, 8, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 11, 0, 1, 1)


        self.gridLayout_3.addWidget(self.main_group, 1, 0, 1, 1)

        QWidget.setTabOrder(self.spinbox_n_X, self.spinbox_n_Y)
        QWidget.setTabOrder(self.spinbox_n_Y, self.spinbox_n_Z)
        QWidget.setTabOrder(self.spinbox_n_Z, self.input_X_x)
        QWidget.setTabOrder(self.input_X_x, self.input_X_y)
        QWidget.setTabOrder(self.input_X_y, self.input_X_z)
        QWidget.setTabOrder(self.input_X_z, self.button_reset_X)
        QWidget.setTabOrder(self.button_reset_X, self.input_Y_x)
        QWidget.setTabOrder(self.input_Y_x, self.input_Y_y)
        QWidget.setTabOrder(self.input_Y_y, self.input_Y_z)
        QWidget.setTabOrder(self.input_Y_z, self.button_reset_Y)
        QWidget.setTabOrder(self.button_reset_Y, self.input_Z_x)
        QWidget.setTabOrder(self.input_Z_x, self.input_Z_y)
        QWidget.setTabOrder(self.input_Z_y, self.input_Z_z)
        QWidget.setTabOrder(self.input_Z_z, self.button_reset_Z)
        QWidget.setTabOrder(self.button_reset_Z, self.checkbox_fuse)
        QWidget.setTabOrder(self.checkbox_fuse, self.checkbox_link)

        self.retranslateUi(DraftOrthoArrayTaskPanel)

        QMetaObject.connectSlotsByName(DraftOrthoArrayTaskPanel)
    # setupUi

    def retranslateUi(self, DraftOrthoArrayTaskPanel):
        DraftOrthoArrayTaskPanel.setWindowTitle(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Orthogonal array", None))
        self.main_group.setTitle("")
#if QT_CONFIG(tooltip)
        self.group_copies.setToolTip(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Number of elements in the array in the specified direction, including a copy of the original object.\n"
"The number must be at least 1 in each direction.", None))
#endif // QT_CONFIG(tooltip)
        self.group_copies.setTitle(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Number of elements", None))
        self.label_n_X.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"X", None))
        self.label_n_Y.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Y", None))
        self.label_n_Z.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Z", None))
#if QT_CONFIG(tooltip)
        self.group_X.setToolTip(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Distance between the elements in the X direction.\n"
"Normally, only the X value is necessary; the other two values can give an additional shift in their respective directions.\n"
"Negative values will result in copies produced in the negative direction.", None))
#endif // QT_CONFIG(tooltip)
        self.group_X.setTitle(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"X intervals", None))
        self.label_X_x.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"X", None))
        self.label_X_y.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Y", None))
        self.label_X_z.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Z", None))
#if QT_CONFIG(tooltip)
        self.button_reset_X.setToolTip(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Reset the distances.", None))
#endif // QT_CONFIG(tooltip)
        self.button_reset_X.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Reset X", None))
#if QT_CONFIG(tooltip)
        self.group_Y.setToolTip(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Distance between the elements in the Y direction.\n"
"Normally, only the Y value is necessary; the other two values can give an additional shift in their respective directions.\n"
"Negative values will result in copies produced in the negative direction.", None))
#endif // QT_CONFIG(tooltip)
        self.group_Y.setTitle(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Y intervals", None))
        self.label_Y_x.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"X", None))
        self.label_Y_y.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Y", None))
        self.label_Y_z.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Z", None))
#if QT_CONFIG(tooltip)
        self.button_reset_Y.setToolTip(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Reset the distances.", None))
#endif // QT_CONFIG(tooltip)
        self.button_reset_Y.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Reset Y", None))
#if QT_CONFIG(tooltip)
        self.group_Z.setToolTip(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Distance between the elements in the Z direction.\n"
"Normally, only the Z value is necessary; the other two values can give an additional shift in their respective directions.\n"
"Negative values will result in copies produced in the negative direction.", None))
#endif // QT_CONFIG(tooltip)
        self.group_Z.setTitle(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Z intervals", None))
        self.label_Z_x.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"X", None))
        self.label_Z_y.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Y", None))
        self.label_Z_z.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Z", None))
#if QT_CONFIG(tooltip)
        self.button_reset_Z.setToolTip(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Reset the distances.", None))
#endif // QT_CONFIG(tooltip)
        self.button_reset_Z.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Reset Z", None))
#if QT_CONFIG(tooltip)
        self.checkbox_fuse.setToolTip(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"If checked, the resulting objects in the array will be fused if they touch each other.\n"
"This only works if \"Link array\" is off.", None))
#endif // QT_CONFIG(tooltip)
        self.checkbox_fuse.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Fuse", None))
#if QT_CONFIG(tooltip)
        self.checkbox_link.setToolTip(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"If checked, the resulting object will be a \"Link array\" instead of a regular array.\n"
"A Link array is more efficient when creating multiple copies, but it cannot be fused together.", None))
#endif // QT_CONFIG(tooltip)
        self.checkbox_link.setText(QCoreApplication.translate("DraftOrthoArrayTaskPanel", u"Link array", None))
    # retranslateUi

