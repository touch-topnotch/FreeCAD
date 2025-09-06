# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsPythonConsole.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Gui_Dialog_DlgSettingsPythonConsole(object):
    def setupUi(self, Gui__Dialog__DlgSettingsPythonConsole):
        if not Gui__Dialog__DlgSettingsPythonConsole.objectName():
            Gui__Dialog__DlgSettingsPythonConsole.setObjectName(u"Gui__Dialog__DlgSettingsPythonConsole")
        Gui__Dialog__DlgSettingsPythonConsole.resize(654, 259)
        self.gridLayout_2 = QGridLayout(Gui__Dialog__DlgSettingsPythonConsole)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.GroupBox_console = QGroupBox(Gui__Dialog__DlgSettingsPythonConsole)
        self.GroupBox_console.setObjectName(u"GroupBox_console")
        self.gridLayout = QGridLayout(self.GroupBox_console)
        self.gridLayout.setObjectName(u"gridLayout")
        self.PythonWordWrap = Gui_PrefCheckBox(self.GroupBox_console)
        self.PythonWordWrap.setObjectName(u"PythonWordWrap")
        self.PythonWordWrap.setChecked(True)
        self.PythonWordWrap.setProperty(u"prefEntry", u"PythonWordWrap")
        self.PythonWordWrap.setProperty(u"prefPath", u"PythonConsole")

        self.gridLayout.addWidget(self.PythonWordWrap, 0, 0, 1, 1)

        self.PythonBlockCursor = Gui_PrefCheckBox(self.GroupBox_console)
        self.PythonBlockCursor.setObjectName(u"PythonBlockCursor")
        self.PythonBlockCursor.setChecked(False)
        self.PythonBlockCursor.setProperty(u"prefEntry", u"PythonBlockCursor")
        self.PythonBlockCursor.setProperty(u"prefPath", u"PythonConsole")

        self.gridLayout.addWidget(self.PythonBlockCursor, 1, 0, 1, 1)

        self.PythonSaveHistory = Gui_PrefCheckBox(self.GroupBox_console)
        self.PythonSaveHistory.setObjectName(u"PythonSaveHistory")
        self.PythonSaveHistory.setChecked(False)
        self.PythonSaveHistory.setProperty(u"prefEntry", u"SavePythonHistory")
        self.PythonSaveHistory.setProperty(u"prefPath", u"PythonConsole")

        self.gridLayout.addWidget(self.PythonSaveHistory, 2, 0, 1, 1)

        self.labelProfilerInterval = QLabel(self.GroupBox_console)
        self.labelProfilerInterval.setObjectName(u"labelProfilerInterval")

        self.gridLayout.addWidget(self.labelProfilerInterval, 3, 0, 1, 1)

        self.ProfilerInterval = Gui_PrefSpinBox(self.GroupBox_console)
        self.ProfilerInterval.setObjectName(u"ProfilerInterval")
        self.ProfilerInterval.setMinimum(0)
        self.ProfilerInterval.setMaximum(5000)
        self.ProfilerInterval.setValue(200)
        self.ProfilerInterval.setProperty(u"prefEntry", u"ProfilerInterval")
        self.ProfilerInterval.setProperty(u"prefPath", u"PythonConsole")

        self.gridLayout.addWidget(self.ProfilerInterval, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.GroupBox_console, 0, 0, 1, 1)

        self.GroupBox_other = QGroupBox(Gui__Dialog__DlgSettingsPythonConsole)
        self.GroupBox_other.setObjectName(u"GroupBox_other")
        self.gridLayout_3 = QGridLayout(self.GroupBox_other)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.fclabel = QLabel(self.GroupBox_other)
        self.fclabel.setObjectName(u"fclabel")

        self.gridLayout_3.addWidget(self.fclabel, 0, 0, 1, 1)

        self.ExternalPythonExecutable = Gui_PrefFileChooser(self.GroupBox_other)
        self.ExternalPythonExecutable.setObjectName(u"ExternalPythonExecutable")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExternalPythonExecutable.sizePolicy().hasHeightForWidth())
        self.ExternalPythonExecutable.setSizePolicy(sizePolicy)
        self.ExternalPythonExecutable.setMinimumSize(QSize(300, 0))
        self.ExternalPythonExecutable.setProperty(u"prefEntry", u"ExternalPythonExecutable")
        self.ExternalPythonExecutable.setProperty(u"prefPath", u"PythonConsole")

        self.gridLayout_3.addWidget(self.ExternalPythonExecutable, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.GroupBox_other, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 63, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgSettingsPythonConsole)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsPythonConsole)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsPythonConsole):
        Gui__Dialog__DlgSettingsPythonConsole.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u"General", None))
        self.GroupBox_console.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u"Console", None))
#if QT_CONFIG(tooltip)
        self.PythonWordWrap.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u"Words will be wrapped when they exceed available\n"
"horizontal space in Python console", None))
#endif // QT_CONFIG(tooltip)
        self.PythonWordWrap.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u"Enable word wrap", None))
#if QT_CONFIG(tooltip)
        self.PythonBlockCursor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u"The cursor shape will be a block", None))
#endif // QT_CONFIG(tooltip)
        self.PythonBlockCursor.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u"Enable block cursor", None))
#if QT_CONFIG(tooltip)
        self.PythonSaveHistory.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u"Saves Python history across sessions", None))
#endif // QT_CONFIG(tooltip)
        self.PythonSaveHistory.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u"Save history", None))
        self.labelProfilerInterval.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u"Python profiler interval (ms)", None))
#if QT_CONFIG(tooltip)
        self.ProfilerInterval.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u"The interval in milliseconds at which the profiler runs when there is Python code running (to keep the GUI responding). Set to 0 to disable.", None))
#endif // QT_CONFIG(tooltip)
        self.ProfilerInterval.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u" ms", None))
        self.GroupBox_other.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u"Other", None))
        self.fclabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u"Path to external Python executable (optional)", None))
#if QT_CONFIG(tooltip)
        self.ExternalPythonExecutable.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsPythonConsole", u"Used for package installation with pip and debugging with debugpy. Autodetected if needed and not specified.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

