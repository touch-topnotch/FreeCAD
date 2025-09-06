# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Assembly.ui'
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
    QSizePolicy, QSpacerItem, QWidget)

class Ui_AssemblyGui_DlgSettingsAssembly(object):
    def setupUi(self, AssemblyGui__DlgSettingsAssembly):
        if not AssemblyGui__DlgSettingsAssembly.objectName():
            AssemblyGui__DlgSettingsAssembly.setObjectName(u"AssemblyGui__DlgSettingsAssembly")
        AssemblyGui__DlgSettingsAssembly.resize(487, 691)
        self.verticalLayout_1 = QGridLayout(AssemblyGui__DlgSettingsAssembly)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.checkBoxEnableEscape = Gui_PrefCheckBox(AssemblyGui__DlgSettingsAssembly)
        self.checkBoxEnableEscape.setObjectName(u"checkBoxEnableEscape")
        self.checkBoxEnableEscape.setChecked(True)
        self.checkBoxEnableEscape.setProperty(u"prefEntry", u"LeaveEditWithEscape")
        self.checkBoxEnableEscape.setProperty(u"prefPath", u"Mod/Assembly")

        self.verticalLayout_1.addWidget(self.checkBoxEnableEscape, 0, 0, 1, 1)

        self.checkBoxSolverDebug = Gui_PrefCheckBox(AssemblyGui__DlgSettingsAssembly)
        self.checkBoxSolverDebug.setObjectName(u"checkBoxSolverDebug")
        self.checkBoxSolverDebug.setChecked(False)
        self.checkBoxSolverDebug.setProperty(u"prefEntry", u"LogSolverDebug")
        self.checkBoxSolverDebug.setProperty(u"prefPath", u"Mod/Assembly")

        self.verticalLayout_1.addWidget(self.checkBoxSolverDebug, 1, 0, 1, 1)

        self.groundFirstPartLabel = QLabel(AssemblyGui__DlgSettingsAssembly)
        self.groundFirstPartLabel.setObjectName(u"groundFirstPartLabel")

        self.verticalLayout_1.addWidget(self.groundFirstPartLabel, 2, 0, 1, 1)

        self.groundFirstPart = QComboBox(AssemblyGui__DlgSettingsAssembly)
        self.groundFirstPart.setObjectName(u"groundFirstPart")

        self.verticalLayout_1.addWidget(self.groundFirstPart, 2, 1, 1, 1)

        self.horSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_1.addItem(self.horSpacer, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 217, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_1.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.retranslateUi(AssemblyGui__DlgSettingsAssembly)

        self.groundFirstPart.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AssemblyGui__DlgSettingsAssembly)
    # setupUi

    def retranslateUi(self, AssemblyGui__DlgSettingsAssembly):
        AssemblyGui__DlgSettingsAssembly.setWindowTitle(QCoreApplication.translate("AssemblyGui::DlgSettingsAssembly", u"General", None))
#if QT_CONFIG(tooltip)
        self.checkBoxEnableEscape.setToolTip(QCoreApplication.translate("AssemblyGui::DlgSettingsAssembly", u"Allows leaving edit mode when pressing the Esc key", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxEnableEscape.setText(QCoreApplication.translate("AssemblyGui::DlgSettingsAssembly", u"Esc leaves edit mode", None))
#if QT_CONFIG(tooltip)
        self.checkBoxSolverDebug.setToolTip(QCoreApplication.translate("AssemblyGui::DlgSettingsAssembly", u"Log the dragging steps of the solver. Useful to report a bug.\n"
"The files are named \"runPreDrag.asmt\" and \"dragging.log\" and are located in the default directory of std::ofstream (on Windows it's the desktop)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSolverDebug.setText(QCoreApplication.translate("AssemblyGui::DlgSettingsAssembly", u"Log dragging steps", None))
        self.groundFirstPartLabel.setText(QCoreApplication.translate("AssemblyGui::DlgSettingsAssembly", u"Ground first part", None))
#if QT_CONFIG(tooltip)
        self.groundFirstPart.setToolTip(QCoreApplication.translate("AssemblyGui::DlgSettingsAssembly", u"When inserting the first part in the assembly, it can be grounded automatically", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

