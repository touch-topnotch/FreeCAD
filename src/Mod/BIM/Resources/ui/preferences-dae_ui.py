# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences-dae.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsArch(object):
    def setupUi(self, Gui__Dialog__DlgSettingsArch):
        if not Gui__Dialog__DlgSettingsArch.objectName():
            Gui__Dialog__DlgSettingsArch.setObjectName(u"Gui__Dialog__DlgSettingsArch")
        Gui__Dialog__DlgSettingsArch.resize(333, 414)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsArch)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(9, 9, 9, 9)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.groupBox_3 = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.doubleSpinBox = Gui_PrefDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setMaximum(999999.989999999990687)
        self.doubleSpinBox.setValue(1.000000000000000)
        self.doubleSpinBox.setProperty(u"prefEntry", u"ColladaScalingFactor")
        self.doubleSpinBox.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout_7.addWidget(self.doubleSpinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = Gui_PrefComboBox(self.groupBox_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setProperty(u"prefEntry", u"ColladaMesher")
        self.comboBox.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.vboxLayout.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.doubleSpinBox_2 = Gui_PrefDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setDecimals(4)
        self.doubleSpinBox_2.setValue(1.000000000000000)
        self.doubleSpinBox_2.setProperty(u"prefEntry", u"ColladaTessellation")
        self.doubleSpinBox_2.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.vboxLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsArch)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.doubleSpinBox_3 = Gui_PrefDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setDecimals(4)
        self.doubleSpinBox_3.setValue(0.300000000000000)
        self.doubleSpinBox_3.setProperty(u"prefEntry", u"ColladaGrading")
        self.doubleSpinBox_3.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.spinBox = Gui_PrefSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setValue(1)
        self.spinBox.setProperty(u"prefEntry", u"ColladaSegsPerEdge")
        self.spinBox.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout_4.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.spinBox_2 = Gui_PrefSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setValue(2)
        self.spinBox_2.setProperty(u"prefEntry", u"ColladaSegsPerRadius")
        self.spinBox_2.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout_5.addWidget(self.spinBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox = Gui_PrefCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setProperty(u"prefEntry", u"ColladaSecondOrder")
        self.checkBox.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout_6.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox_2 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setProperty(u"prefEntry", u"ColladaOptimize")
        self.checkBox_2.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout_8.addWidget(self.checkBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBox_3 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setProperty(u"prefEntry", u"ColladaAllowQuads")
        self.checkBox_3.setProperty(u"prefPath", u"Mod/Arch")

        self.horizontalLayout_9.addWidget(self.checkBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.vboxLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Gui__Dialog__DlgSettingsArch)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsArch)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsArch):
        Gui__Dialog__DlgSettingsArch.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"DAE", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Export options", None))
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Scaling factor", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"All dimensions in the file will be scaled with this factor", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Mesher", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Builtin", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Mefisto", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Netgen", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Meshing program that should be used.\n"
"If using Netgen, make sure that it is available.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Builtin and Mefisto mesher options", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Tessellation", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox_2.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Tessellation value to use with the Builtin and the Mefisto meshing program.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Netgen mesher options", None))
        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Grading", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox_3.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Grading value to use for meshing using Netgen.\n"
"This value describes how fast the mesh size decreases.\n"
"The gradient of the local mesh size h(x) is bound by |\u0394h(x)| \u2264 1/value.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Segments per edge", None))
#if QT_CONFIG(tooltip)
        self.spinBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Maximum number of segments per edge", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Segments per radius", None))
#if QT_CONFIG(tooltip)
        self.spinBox_2.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Number of segments per radius", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Allow a second order mesh", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Second order", None))
#if QT_CONFIG(tooltip)
        self.checkBox_2.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Allows optimization", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Optimize", None))
#if QT_CONFIG(tooltip)
        self.checkBox_3.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Allow quadrilateral faces", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsArch", u"Allow quads", None))
    # retranslateUi

