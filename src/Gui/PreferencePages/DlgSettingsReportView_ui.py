# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsReportView.ui'
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

class Ui_Gui_Dialog_DlgSettingsReportView(object):
    def setupUi(self, Gui__Dialog__DlgSettingsReportView):
        if not Gui__Dialog__DlgSettingsReportView.objectName():
            Gui__Dialog__DlgSettingsReportView.setObjectName(u"Gui__Dialog__DlgSettingsReportView")
        Gui__Dialog__DlgSettingsReportView.resize(432, 500)
        self.gridLayout_3 = QGridLayout(Gui__Dialog__DlgSettingsReportView)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox1 = QGroupBox(Gui__Dialog__DlgSettingsReportView)
        self.groupBox1.setObjectName(u"groupBox1")
        self.gridLayout = QGridLayout(self.groupBox1)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.checkMessage = Gui_PrefCheckBox(self.groupBox1)
        self.checkMessage.setObjectName(u"checkMessage")
        self.checkMessage.setChecked(True)
        self.checkMessage.setProperty(u"prefEntry", u"checkMessage")
        self.checkMessage.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout.addWidget(self.checkMessage, 0, 0, 1, 1)

        self.checkLogging = Gui_PrefCheckBox(self.groupBox1)
        self.checkLogging.setObjectName(u"checkLogging")
        self.checkLogging.setProperty(u"prefEntry", u"checkLogging")
        self.checkLogging.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout.addWidget(self.checkLogging, 1, 0, 1, 1)

        self.checkWarning = Gui_PrefCheckBox(self.groupBox1)
        self.checkWarning.setObjectName(u"checkWarning")
        self.checkWarning.setChecked(True)
        self.checkWarning.setProperty(u"prefEntry", u"checkWarning")
        self.checkWarning.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout.addWidget(self.checkWarning, 2, 0, 1, 1)

        self.checkError = Gui_PrefCheckBox(self.groupBox1)
        self.checkError.setObjectName(u"checkError")
        self.checkError.setChecked(True)
        self.checkError.setProperty(u"prefEntry", u"checkError")
        self.checkError.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout.addWidget(self.checkError, 3, 0, 1, 1)

        self.checkShowReportViewOnError = Gui_PrefCheckBox(self.groupBox1)
        self.checkShowReportViewOnError.setObjectName(u"checkShowReportViewOnError")
        self.checkShowReportViewOnError.setChecked(False)
        self.checkShowReportViewOnError.setProperty(u"prefEntry", u"checkShowReportViewOnError")
        self.checkShowReportViewOnError.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout.addWidget(self.checkShowReportViewOnError, 4, 0, 1, 1)

        self.checkShowReportViewOnWarning = Gui_PrefCheckBox(self.groupBox1)
        self.checkShowReportViewOnWarning.setObjectName(u"checkShowReportViewOnWarning")
        self.checkShowReportViewOnWarning.setProperty(u"prefEntry", u"checkShowReportViewOnWarning")
        self.checkShowReportViewOnWarning.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout.addWidget(self.checkShowReportViewOnWarning, 5, 0, 1, 1)

        self.checkShowReportViewOnNormalMessage = Gui_PrefCheckBox(self.groupBox1)
        self.checkShowReportViewOnNormalMessage.setObjectName(u"checkShowReportViewOnNormalMessage")
        self.checkShowReportViewOnNormalMessage.setChecked(False)
        self.checkShowReportViewOnNormalMessage.setProperty(u"prefEntry", u"checkShowReportViewOnNormalMessage")
        self.checkShowReportViewOnNormalMessage.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout.addWidget(self.checkShowReportViewOnNormalMessage, 6, 0, 1, 1)

        self.checkShowReportViewOnLogMessage = Gui_PrefCheckBox(self.groupBox1)
        self.checkShowReportViewOnLogMessage.setObjectName(u"checkShowReportViewOnLogMessage")
        self.checkShowReportViewOnLogMessage.setChecked(False)
        self.checkShowReportViewOnLogMessage.setProperty(u"prefEntry", u"checkShowReportViewOnLogMessage")
        self.checkShowReportViewOnLogMessage.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout.addWidget(self.checkShowReportViewOnLogMessage, 7, 0, 1, 1)

        self.checkShowReportTimecode = Gui_PrefCheckBox(self.groupBox1)
        self.checkShowReportTimecode.setObjectName(u"checkShowReportTimecode")
        self.checkShowReportTimecode.setChecked(True)
        self.checkShowReportTimecode.setProperty(u"prefEntry", u"checkShowReportTimecode")
        self.checkShowReportTimecode.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout.addWidget(self.checkShowReportTimecode, 8, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox1, 0, 0, 1, 1)

        self.groupBox2 = QGroupBox(Gui__Dialog__DlgSettingsReportView)
        self.groupBox2.setObjectName(u"groupBox2")
        self.gridLayout1 = QGridLayout(self.groupBox2)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
        self.gridLayout2 = QGridLayout()
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)
        self.textLabel1 = QLabel(self.groupBox2)
        self.textLabel1.setObjectName(u"textLabel1")

        self.gridLayout2.addWidget(self.textLabel1, 0, 0, 1, 1)

        self.spacerItem = QSpacerItem(214, 23, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.spacerItem, 0, 1, 1, 1)

        self.colorText = Gui_PrefColorButton(self.groupBox2)
        self.colorText.setObjectName(u"colorText")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorText.sizePolicy().hasHeightForWidth())
        self.colorText.setSizePolicy(sizePolicy)
        self.colorText.setMinimumSize(QSize(75, 0))
        self.colorText.setColor(QColor(0, 0, 0))
        self.colorText.setProperty(u"prefEntry", u"colorText")
        self.colorText.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout2.addWidget(self.colorText, 0, 2, 1, 1)

        self.textLabel2 = QLabel(self.groupBox2)
        self.textLabel2.setObjectName(u"textLabel2")

        self.gridLayout2.addWidget(self.textLabel2, 1, 0, 1, 1)

        self.spacerItem1 = QSpacerItem(211, 23, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.spacerItem1, 1, 1, 1, 1)

        self.colorLogging = Gui_PrefColorButton(self.groupBox2)
        self.colorLogging.setObjectName(u"colorLogging")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.colorLogging.sizePolicy().hasHeightForWidth())
        self.colorLogging.setSizePolicy(sizePolicy1)
        self.colorLogging.setMinimumSize(QSize(75, 0))
        self.colorLogging.setColor(QColor(0, 0, 255))
        self.colorLogging.setProperty(u"prefEntry", u"colorLogging")
        self.colorLogging.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout2.addWidget(self.colorLogging, 1, 2, 1, 1)

        self.textLabel3 = QLabel(self.groupBox2)
        self.textLabel3.setObjectName(u"textLabel3")

        self.gridLayout2.addWidget(self.textLabel3, 2, 0, 1, 1)

        self.spacerItem2 = QSpacerItem(211, 23, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.spacerItem2, 2, 1, 1, 1)

        self.colorWarning = Gui_PrefColorButton(self.groupBox2)
        self.colorWarning.setObjectName(u"colorWarning")
        sizePolicy1.setHeightForWidth(self.colorWarning.sizePolicy().hasHeightForWidth())
        self.colorWarning.setSizePolicy(sizePolicy1)
        self.colorWarning.setMinimumSize(QSize(75, 0))
        self.colorWarning.setColor(QColor(255, 170, 0))
        self.colorWarning.setProperty(u"prefEntry", u"colorWarning")
        self.colorWarning.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout2.addWidget(self.colorWarning, 2, 2, 1, 1)

        self.textLabel4 = QLabel(self.groupBox2)
        self.textLabel4.setObjectName(u"textLabel4")

        self.gridLayout2.addWidget(self.textLabel4, 3, 0, 1, 1)

        self.spacerItem3 = QSpacerItem(211, 23, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout2.addItem(self.spacerItem3, 3, 1, 1, 1)

        self.colorError = Gui_PrefColorButton(self.groupBox2)
        self.colorError.setObjectName(u"colorError")
        sizePolicy1.setHeightForWidth(self.colorError.sizePolicy().hasHeightForWidth())
        self.colorError.setSizePolicy(sizePolicy1)
        self.colorError.setMinimumSize(QSize(75, 0))
        self.colorError.setColor(QColor(255, 0, 0))
        self.colorError.setProperty(u"prefEntry", u"colorError")
        self.colorError.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout2.addWidget(self.colorError, 3, 2, 1, 1)


        self.gridLayout1.addLayout(self.gridLayout2, 0, 0, 1, 1)

        self.spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout1.addItem(self.spacerItem4, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox2, 1, 0, 1, 1)

        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsReportView)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pythonOutput = Gui_PrefCheckBox(self.groupBox)
        self.pythonOutput.setObjectName(u"pythonOutput")
        self.pythonOutput.setChecked(True)
        self.pythonOutput.setProperty(u"prefEntry", u"RedirectPythonOutput")
        self.pythonOutput.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout_2.addWidget(self.pythonOutput, 0, 0, 1, 1)

        self.pythonError = Gui_PrefCheckBox(self.groupBox)
        self.pythonError.setObjectName(u"pythonError")
        self.pythonError.setChecked(True)
        self.pythonError.setProperty(u"prefEntry", u"RedirectPythonErrors")
        self.pythonError.setProperty(u"prefPath", u"OutputWindow")

        self.gridLayout_2.addWidget(self.pythonError, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)

        self.spacerItem5 = QSpacerItem(410, 71, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.spacerItem5, 3, 0, 1, 1)

        QWidget.setTabOrder(self.checkLogging, self.checkWarning)
        QWidget.setTabOrder(self.checkWarning, self.checkError)
        QWidget.setTabOrder(self.checkError, self.checkShowReportViewOnWarning)
        QWidget.setTabOrder(self.checkShowReportViewOnWarning, self.checkShowReportViewOnError)
        QWidget.setTabOrder(self.checkShowReportViewOnError, self.checkShowReportViewOnNormalMessage)
        QWidget.setTabOrder(self.checkShowReportViewOnNormalMessage, self.checkShowReportViewOnLogMessage)
        QWidget.setTabOrder(self.checkShowReportViewOnLogMessage, self.checkShowReportTimecode)
        QWidget.setTabOrder(self.checkShowReportTimecode, self.colorText)
        QWidget.setTabOrder(self.colorText, self.colorLogging)
        QWidget.setTabOrder(self.colorLogging, self.colorWarning)
        QWidget.setTabOrder(self.colorWarning, self.colorError)
        QWidget.setTabOrder(self.colorError, self.pythonOutput)
        QWidget.setTabOrder(self.pythonOutput, self.pythonError)

        self.retranslateUi(Gui__Dialog__DlgSettingsReportView)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsReportView)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsReportView):
        Gui__Dialog__DlgSettingsReportView.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Report View", None))
        self.groupBox1.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Output", None))
#if QT_CONFIG(tooltip)
        self.checkMessage.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Normal messages will be recorded", None))
#endif // QT_CONFIG(tooltip)
        self.checkMessage.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Record normal messages", None))
#if QT_CONFIG(tooltip)
        self.checkLogging.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Log messages will be recorded", None))
#endif // QT_CONFIG(tooltip)
        self.checkLogging.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Record log messages", None))
#if QT_CONFIG(tooltip)
        self.checkWarning.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Warnings will be recorded", None))
#endif // QT_CONFIG(tooltip)
        self.checkWarning.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Record warnings", None))
#if QT_CONFIG(tooltip)
        self.checkError.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Error messages will be recorded", None))
#endif // QT_CONFIG(tooltip)
        self.checkError.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Record error messages", None))
#if QT_CONFIG(tooltip)
        self.checkShowReportViewOnError.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"When an error has occurred, the Report View dialog becomes visible\n"
"on-screen while displaying the error", None))
#endif // QT_CONFIG(tooltip)
        self.checkShowReportViewOnError.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Show report view on error", None))
#if QT_CONFIG(tooltip)
        self.checkShowReportViewOnWarning.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"When a warning has occurred, the Report View dialog becomes visible\n"
"on-screen while displaying the warning", None))
#endif // QT_CONFIG(tooltip)
        self.checkShowReportViewOnWarning.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Show report view on warning", None))
#if QT_CONFIG(tooltip)
        self.checkShowReportViewOnNormalMessage.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"When a normal message has occurred, the Report View dialog becomes visible\n"
"on-screen while displaying the message", None))
#endif // QT_CONFIG(tooltip)
        self.checkShowReportViewOnNormalMessage.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Show report view on normal message", None))
#if QT_CONFIG(tooltip)
        self.checkShowReportViewOnLogMessage.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"When a log message has occurred, the Report View dialog becomes visible\n"
"on-screen while displaying the log message", None))
#endif // QT_CONFIG(tooltip)
        self.checkShowReportViewOnLogMessage.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Show report view on log message", None))
#if QT_CONFIG(tooltip)
        self.checkShowReportTimecode.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Include a timecode for each report", None))
#endif // QT_CONFIG(tooltip)
        self.checkShowReportTimecode.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Include a timecode for each entry", None))
        self.groupBox2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Colors", None))
        self.textLabel1.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Normal messages", None))
#if QT_CONFIG(tooltip)
        self.colorText.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Font color for normal messages in Report view panel", None))
#endif // QT_CONFIG(tooltip)
        self.colorText.setText("")
        self.textLabel2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Log messages", None))
#if QT_CONFIG(tooltip)
        self.colorLogging.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Font color for log messages in Report view panel", None))
#endif // QT_CONFIG(tooltip)
        self.colorLogging.setText("")
        self.textLabel3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Warnings", None))
#if QT_CONFIG(tooltip)
        self.colorWarning.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Font color for warning messages in Report view panel", None))
#endif // QT_CONFIG(tooltip)
        self.colorWarning.setText("")
        self.textLabel4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Errors", None))
#if QT_CONFIG(tooltip)
        self.colorError.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Font color for error messages in Report view panel", None))
#endif // QT_CONFIG(tooltip)
        self.colorError.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Python Interpreter", None))
#if QT_CONFIG(tooltip)
        self.pythonOutput.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Internal Python output will be redirected\n"
"from Python console to Report view panel", None))
#endif // QT_CONFIG(tooltip)
        self.pythonOutput.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Redirect internal Python output to report view", None))
#if QT_CONFIG(tooltip)
        self.pythonError.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Internal Python error messages will be redirected\n"
"from Python console to Report view panel", None))
#endif // QT_CONFIG(tooltip)
        self.pythonError.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsReportView", u"Redirect internal Python errors to report view", None))
    # retranslateUi

