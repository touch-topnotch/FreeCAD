# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UnitTest.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_TestGui_UnitTest(object):
    def setupUi(self, TestGui__UnitTest):
        if not TestGui__UnitTest.objectName():
            TestGui__UnitTest.setObjectName(u"TestGui__UnitTest")
        TestGui__UnitTest.resize(421, 434)
        TestGui__UnitTest.setSizeGripEnabled(True)
        self.gridLayout = QGridLayout(TestGui__UnitTest)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonGroup1 = QGroupBox(TestGui__UnitTest)
        self.buttonGroup1.setObjectName(u"buttonGroup1")
        self.hboxLayout = QHBoxLayout(self.buttonGroup1)
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setContentsMargins(5, 5, 5, 5)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.textLabelTest = QLabel(self.buttonGroup1)
        self.textLabelTest.setObjectName(u"textLabelTest")

        self.hboxLayout.addWidget(self.textLabelTest)

        self.comboTests = QComboBox(self.buttonGroup1)
        self.comboTests.setObjectName(u"comboTests")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboTests.sizePolicy().hasHeightForWidth())
        self.comboTests.setSizePolicy(sizePolicy)
        self.comboTests.setEditable(True)
        self.comboTests.setDuplicatesEnabled(False)

        self.hboxLayout.addWidget(self.comboTests)


        self.gridLayout.addWidget(self.buttonGroup1, 0, 0, 1, 1)

        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.spacerItem = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vboxLayout.addItem(self.spacerItem)

        self.startButton = QPushButton(TestGui__UnitTest)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setAutoDefault(True)

        self.vboxLayout.addWidget(self.startButton)

        self.spacerItem1 = QSpacerItem(77, 141, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.spacerItem1)

        self.helpButton = QPushButton(TestGui__UnitTest)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setAutoDefault(True)

        self.vboxLayout.addWidget(self.helpButton)

        self.aboutButton = QPushButton(TestGui__UnitTest)
        self.aboutButton.setObjectName(u"aboutButton")
        self.aboutButton.setAutoDefault(True)

        self.vboxLayout.addWidget(self.aboutButton)

        self.closeButton = QPushButton(TestGui__UnitTest)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setAutoDefault(True)

        self.vboxLayout.addWidget(self.closeButton)


        self.gridLayout.addLayout(self.vboxLayout, 0, 1, 3, 1)

        self.groupBox1 = QGroupBox(TestGui__UnitTest)
        self.groupBox1.setObjectName(u"groupBox1")
        self.gridLayout1 = QGridLayout(self.groupBox1)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(6, 6, 6, 6)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.progressBar = QProgressBar(self.groupBox1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setOrientation(Qt.Horizontal)

        self.gridLayout1.addWidget(self.progressBar, 0, 0, 1, 8)

        self.textLabelRun = QLabel(self.groupBox1)
        self.textLabelRun.setObjectName(u"textLabelRun")

        self.gridLayout1.addWidget(self.textLabelRun, 1, 0, 1, 1)

        self.textLabelRunCt = QLabel(self.groupBox1)
        self.textLabelRunCt.setObjectName(u"textLabelRunCt")
        self.textLabelRunCt.setText(u"<font color=\"#0000ff\">0</font>")
        self.textLabelRunCt.setAlignment(Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelRunCt, 1, 1, 1, 1)

        self.textLabelFail = QLabel(self.groupBox1)
        self.textLabelFail.setObjectName(u"textLabelFail")

        self.gridLayout1.addWidget(self.textLabelFail, 1, 2, 1, 1)

        self.textLabelFailCt = QLabel(self.groupBox1)
        self.textLabelFailCt.setObjectName(u"textLabelFailCt")
        self.textLabelFailCt.setText(u"<font color=\"#0000ff\">0</font>")
        self.textLabelFailCt.setAlignment(Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelFailCt, 1, 3, 1, 1)

        self.textLabelErr = QLabel(self.groupBox1)
        self.textLabelErr.setObjectName(u"textLabelErr")

        self.gridLayout1.addWidget(self.textLabelErr, 1, 4, 1, 1)

        self.textLabelErrCt = QLabel(self.groupBox1)
        self.textLabelErrCt.setObjectName(u"textLabelErrCt")
        self.textLabelErrCt.setText(u"<font color=\"#0000ff\">0</font>")
        self.textLabelErrCt.setAlignment(Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelErrCt, 1, 5, 1, 1)

        self.textLabelRem = QLabel(self.groupBox1)
        self.textLabelRem.setObjectName(u"textLabelRem")

        self.gridLayout1.addWidget(self.textLabelRem, 1, 6, 1, 1)

        self.textLabelRemCt = QLabel(self.groupBox1)
        self.textLabelRemCt.setObjectName(u"textLabelRemCt")
        self.textLabelRemCt.setText(u"<font color=\"#0000ff\">0</font>")
        self.textLabelRemCt.setAlignment(Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelRemCt, 1, 7, 1, 1)


        self.gridLayout.addWidget(self.groupBox1, 1, 0, 1, 1)

        self.groupBox2 = QGroupBox(TestGui__UnitTest)
        self.groupBox2.setObjectName(u"groupBox2")
        self.gridLayout2 = QGridLayout(self.groupBox2)
        self.gridLayout2.setSpacing(6)
        self.gridLayout2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.treeViewFailure = QTreeWidget(self.groupBox2)
        self.treeViewFailure.setObjectName(u"treeViewFailure")
        self.treeViewFailure.setRootIsDecorated(False)

        self.gridLayout2.addWidget(self.treeViewFailure, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox2, 2, 0, 1, 1)

        self.textLabelStatus = QLabel(TestGui__UnitTest)
        self.textLabelStatus.setObjectName(u"textLabelStatus")
        self.textLabelStatus.setFrameShape(QFrame.Panel)
        self.textLabelStatus.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.textLabelStatus, 3, 0, 1, 2)

        QWidget.setTabOrder(self.comboTests, self.startButton)
        QWidget.setTabOrder(self.startButton, self.treeViewFailure)
        QWidget.setTabOrder(self.treeViewFailure, self.helpButton)
        QWidget.setTabOrder(self.helpButton, self.aboutButton)
        QWidget.setTabOrder(self.aboutButton, self.closeButton)

        self.retranslateUi(TestGui__UnitTest)
        self.closeButton.clicked.connect(TestGui__UnitTest.close)

        self.startButton.setDefault(True)


        QMetaObject.connectSlotsByName(TestGui__UnitTest)
    # setupUi

    def retranslateUi(self, TestGui__UnitTest):
        TestGui__UnitTest.setWindowTitle(QCoreApplication.translate("TestGui::UnitTest", u"FreeCAD Unit Test", None))
        self.buttonGroup1.setTitle(QCoreApplication.translate("TestGui::UnitTest", u"Test", None))
        self.textLabelTest.setText(QCoreApplication.translate("TestGui::UnitTest", u"Select test name", None))
        self.startButton.setText(QCoreApplication.translate("TestGui::UnitTest", u"&Start", None))
#if QT_CONFIG(shortcut)
        self.startButton.setShortcut(QCoreApplication.translate("TestGui::UnitTest", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.helpButton.setText(QCoreApplication.translate("TestGui::UnitTest", u"&Help", None))
#if QT_CONFIG(shortcut)
        self.helpButton.setShortcut(QCoreApplication.translate("TestGui::UnitTest", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.aboutButton.setText(QCoreApplication.translate("TestGui::UnitTest", u"&About", None))
#if QT_CONFIG(shortcut)
        self.aboutButton.setShortcut(QCoreApplication.translate("TestGui::UnitTest", u"Alt+A", None))
#endif // QT_CONFIG(shortcut)
        self.closeButton.setText(QCoreApplication.translate("TestGui::UnitTest", u"&Close", None))
#if QT_CONFIG(shortcut)
        self.closeButton.setShortcut(QCoreApplication.translate("TestGui::UnitTest", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox1.setTitle(QCoreApplication.translate("TestGui::UnitTest", u"Progress", None))
        self.textLabelRun.setText(QCoreApplication.translate("TestGui::UnitTest", u"Run", None))
        self.textLabelFail.setText(QCoreApplication.translate("TestGui::UnitTest", u"Failures", None))
        self.textLabelErr.setText(QCoreApplication.translate("TestGui::UnitTest", u"Errors", None))
        self.textLabelRem.setText(QCoreApplication.translate("TestGui::UnitTest", u"Remaining", None))
        self.groupBox2.setTitle(QCoreApplication.translate("TestGui::UnitTest", u"Failures and Errors", None))
        ___qtreewidgetitem = self.treeViewFailure.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("TestGui::UnitTest", u"Description", None));
        self.textLabelStatus.setText(QCoreApplication.translate("TestGui::UnitTest", u"Idle", None))
    # retranslateUi

