# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'openscadprefs-base.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgSettingsOpenSCAD(object):
    def setupUi(self, Gui__Dialog__DlgSettingsOpenSCAD):
        if not Gui__Dialog__DlgSettingsOpenSCAD.objectName():
            Gui__Dialog__DlgSettingsOpenSCAD.setObjectName(u"Gui__Dialog__DlgSettingsOpenSCAD")
        Gui__Dialog__DlgSettingsOpenSCAD.resize(577, 636)
        self.vboxLayout = QVBoxLayout(Gui__Dialog__DlgSettingsOpenSCAD)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(11, 11, 11, 11)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(9, 9, 9, 9)
        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsOpenSCAD)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.fclabel = QLabel(self.groupBox)
        self.fclabel.setObjectName(u"fclabel")

        self.horizontalLayout_2.addWidget(self.fclabel)

        self.gui__preffilechooser = Gui_PrefFileChooser(self.groupBox)
        self.gui__preffilechooser.setObjectName(u"gui__preffilechooser")
        self.gui__preffilechooser.setMinimumSize(QSize(300, 0))
        self.gui__preffilechooser.setProperty(u"prefEntry", u"openscadexecutable")
        self.gui__preffilechooser.setProperty(u"prefPath", u"Mod/OpenSCAD")

        self.horizontalLayout_2.addWidget(self.gui__preffilechooser)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.vboxLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsOpenSCAD)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setProperty(u"prefEntry", u"printVerbose")
        self.checkBox.setProperty(u"prefPath", u"Mod/OpenSCAD")

        self.horizontalLayout_4.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gui__prefcheckboxviewtreeprovider = Gui_PrefCheckBox(self.groupBox_2)
        self.gui__prefcheckboxviewtreeprovider.setObjectName(u"gui__prefcheckboxviewtreeprovider")
        self.gui__prefcheckboxviewtreeprovider.setProperty(u"prefEntry", u"useViewProviderTree")
        self.gui__prefcheckboxviewtreeprovider.setProperty(u"prefPath", u"Mod/OpenSCAD")

        self.horizontalLayout_5.addWidget(self.gui__prefcheckboxviewtreeprovider)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gui__prefcheckboxmultmatrixfeature = Gui_PrefCheckBox(self.groupBox_2)
        self.gui__prefcheckboxmultmatrixfeature.setObjectName(u"gui__prefcheckboxmultmatrixfeature")
        self.gui__prefcheckboxmultmatrixfeature.setProperty(u"prefEntry", u"useMultmatrixFeature")
        self.gui__prefcheckboxmultmatrixfeature.setProperty(u"prefPath", u"Mod/OpenSCAD")

        self.horizontalLayout_6.addWidget(self.gui__prefcheckboxmultmatrixfeature)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_7.addWidget(self.label_12)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.gui__prefmaxfnsp = Gui_PrefSpinBox(self.groupBox_2)
        self.gui__prefmaxfnsp.setObjectName(u"gui__prefmaxfnsp")
        self.gui__prefmaxfnsp.setValue(16)
        self.gui__prefmaxfnsp.setProperty(u"prefEntry", u"useMaxFN")
        self.gui__prefmaxfnsp.setProperty(u"prefPath", u"Mod/OpenSCAD")

        self.horizontalLayout_7.addWidget(self.gui__prefmaxfnsp)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.guiprefcomboSendVia = Gui_PrefComboBox(self.groupBox_2)
        self.guiprefcomboSendVia.addItem("")
        self.guiprefcomboSendVia.addItem("")
        self.guiprefcomboSendVia.addItem("")
        self.guiprefcomboSendVia.setObjectName(u"guiprefcomboSendVia")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guiprefcomboSendVia.sizePolicy().hasHeightForWidth())
        self.guiprefcomboSendVia.setSizePolicy(sizePolicy)
        self.guiprefcomboSendVia.setProperty(u"prefEntry", u"transfermechanism")
        self.guiprefcomboSendVia.setProperty(u"prefPath", u"Mod/OpenSCAD")

        self.horizontalLayout_3.addWidget(self.guiprefcomboSendVia)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.transferDirectoryLayout = QHBoxLayout()
        self.transferDirectoryLayout.setSpacing(6)
        self.transferDirectoryLayout.setObjectName(u"transferDirectoryLayout")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.transferDirectoryLayout.addWidget(self.label_7)

        self.gui__preffilechooser1 = Gui_PrefFileChooser(self.groupBox_2)
        self.gui__preffilechooser1.setObjectName(u"gui__preffilechooser1")
        self.gui__preffilechooser1.setMinimumSize(QSize(300, 0))
        self.gui__preffilechooser1.setMode(Gui.FileChooser.Directory)
        self.gui__preffilechooser1.setProperty(u"prefEntry", u"transferdirectory")
        self.gui__preffilechooser1.setProperty(u"prefPath", u"Mod/OpenSCAD")

        self.transferDirectoryLayout.addWidget(self.gui__preffilechooser1)


        self.verticalLayout.addLayout(self.transferDirectoryLayout)


        self.vboxLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Gui__Dialog__DlgSettingsOpenSCAD)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(6)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_21.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_21.addWidget(self.label_3)

        self.doubleSpinBox_2 = Gui_PrefDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setSuffix(u"\u00b0")
        self.doubleSpinBox_2.setMinimum(0.010000000000000)
        self.doubleSpinBox_2.setMaximum(360.000000000000000)
        self.doubleSpinBox_2.setValue(12.000000000000000)
        self.doubleSpinBox_2.setProperty(u"prefEntry", u"exportFa")
        self.doubleSpinBox_2.setProperty(u"prefPath", u"Mod/OpenSCAD")

        self.horizontalLayout_21.addWidget(self.doubleSpinBox_2)

        self.line_2 = QFrame(self.groupBox_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_21.addWidget(self.line_2)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_21.addWidget(self.label_4)

        self.doubleSpinBox_3 = Gui_PrefDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_3.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_3.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_3.setMinimumSize(QSize(0, 0))
        self.doubleSpinBox_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_3.setMinimum(0.010000000000000)
        self.doubleSpinBox_3.setMaximum(10000.000000000000000)
        self.doubleSpinBox_3.setValue(2.000000000000000)
        self.doubleSpinBox_3.setProperty(u"prefEntry", u"exportFs")
        self.doubleSpinBox_3.setProperty(u"prefPath", u"Mod/OpenSCAD")

        self.horizontalLayout_21.addWidget(self.doubleSpinBox_3)


        self.verticalLayout_21.addLayout(self.horizontalLayout_21)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.spinBox = Gui_PrefSpinBox(self.groupBox_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(10)
        self.spinBox.setProperty(u"prefEntry", u"exportConvexity")
        self.spinBox.setProperty(u"prefPath", u"Mod/OpenSCAD")

        self.horizontalLayout.addWidget(self.spinBox)


        self.verticalLayout_21.addLayout(self.horizontalLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label1 = QLabel(self.groupBox_3)
        self.label1.setObjectName(u"label1")

        self.gridLayout_2.addWidget(self.label1, 0, 0, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_21, 0, 1, 1, 1)

        self.label_41 = QLabel(self.groupBox_3)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_2.addWidget(self.label_41, 0, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.doubleSpinBox_2a = Gui_PrefDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_2a.setObjectName(u"doubleSpinBox_2a")
        self.doubleSpinBox_2a.setMinimum(0.000000000000000)
        self.doubleSpinBox_2a.setMaximum(1000.000000000000000)
        self.doubleSpinBox_2a.setValue(0.000000000000000)
        self.doubleSpinBox_2a.setProperty(u"prefEntry", u"meshdeflection")
        self.doubleSpinBox_2a.setProperty(u"prefPath", u"Mod/OpenSCAD")

        self.gridLayout_2.addWidget(self.doubleSpinBox_2a, 1, 2, 1, 1)


        self.verticalLayout_21.addLayout(self.gridLayout_2)


        self.vboxLayout.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Gui__Dialog__DlgSettingsOpenSCAD)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsOpenSCAD)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsOpenSCAD):
        Gui__Dialog__DlgSettingsOpenSCAD.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"General", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"General OpenSCAD Settings", None))
        self.fclabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"OpenSCAD executable", None))
#if QT_CONFIG(tooltip)
        self.gui__preffilechooser.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"The path to the OpenSCAD executable", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"OpenSCAD Import", None))
        self.checkBox.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Print debug information in the Console", None))
#if QT_CONFIG(tooltip)
        self.gui__prefcheckboxviewtreeprovider.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"If this is checked, Features will claim their children in the tree view", None))
#endif // QT_CONFIG(tooltip)
        self.gui__prefcheckboxviewtreeprovider.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Use ViewProviders in Tree View", None))
#if QT_CONFIG(tooltip)
        self.gui__prefcheckboxmultmatrixfeature.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"If this is checked, Multmatrix Object will be Parametric", None))
#endif // QT_CONFIG(tooltip)
        self.gui__prefcheckboxmultmatrixfeature.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Use Multmatrix Feature", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"The maximum number of faces of a polygon, prism or frustum. If fn is greater than this value the object is considered to be a circular. Set to 0 for no limit", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Maximum number of faces for polygons (fn)", None))
#if QT_CONFIG(tooltip)
        self.gui__prefmaxfnsp.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"The maximum number of faces of a polygon, prism or frustum. If fn is greater than this value the object is considered to be a circular. Set to 0 for no limit", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Send to OpenSCAD via", None))
        self.guiprefcomboSendVia.setItemText(0, QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Standard temp directory", None))
        self.guiprefcomboSendVia.setItemText(1, QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"User-specified directory", None))
        self.guiprefcomboSendVia.setItemText(2, QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"stdout pipe (requires OpenSCAD >= 2021.1)", None))

#if QT_CONFIG(tooltip)
        self.guiprefcomboSendVia.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"The transfer mechanism for getting data to and from OpenSCAD", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Transfer directory", None))
#if QT_CONFIG(tooltip)
        self.gui__preffilechooser1.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"The path to the directory for transferring files to and from OpenSCAD", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"OpenSCAD Export", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Maximum fragment size", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Minimum angle for a fragment", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"angle (fa)", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox_2.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Minimum angle for a fragment", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Minimum size of a fragment", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"size (fs)", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox_3.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Minimum size of a fragment", None))
#endif // QT_CONFIG(tooltip)
        self.doubleSpinBox_3.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"mm", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Convexity", None))
        self.label1.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Mesh fallback", None))
#if QT_CONFIG(tooltip)
        self.label_41.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Deflection", None))
#endif // QT_CONFIG(tooltip)
        self.label_41.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"deflection", None))
        self.label_5.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Triangulation settings", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox_2a.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsOpenSCAD", u"Deflection", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

