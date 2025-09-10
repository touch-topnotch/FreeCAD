# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgThemeEditor.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QComboBox, QDialog, QDialogButtonBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QPushButton,
    QRadioButton, QScrollBar, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QWidget)

class Ui_Gui_DlgThemeEditor(object):
    def setupUi(self, Gui__DlgThemeEditor):
        if not Gui__DlgThemeEditor.objectName():
            Gui__DlgThemeEditor.setObjectName(u"Gui__DlgThemeEditor")
        Gui__DlgThemeEditor.resize(1169, 562)
        self.gridLayout = QGridLayout(Gui__DlgThemeEditor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Gui__DlgThemeEditor)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_3.addWidget(self.checkBox, 3, 1, 1, 1)

        self.horizontalScrollBar = QScrollBar(self.groupBox)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.horizontalScrollBar, 5, 1, 1, 1)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_3.addWidget(self.spinBox, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 8, 1, 1, 1)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_3.addWidget(self.radioButton, 2, 1, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 6, 1, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 0, 1, 1, 1)

        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 7, 1, 1, 1)

        self.colorButton = Gui_ColorButton(self.groupBox)
        self.colorButton.setObjectName(u"colorButton")

        self.gridLayout_3.addWidget(self.colorButton, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonBox = QDialogButtonBox(Gui__DlgThemeEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok|QDialogButtonBox.StandardButton.Reset)

        self.horizontalLayout_2.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)

        self.tokensTreeView = Gui_TokenTreeView(Gui__DlgThemeEditor)
        self.tokensTreeView.setObjectName(u"tokensTreeView")
        self.tokensTreeView.setMouseTracking(True)
        self.tokensTreeView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tokensTreeView.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.tokensTreeView.setAlternatingRowColors(True)
        self.tokensTreeView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tokensTreeView.setRootIsDecorated(False)
        self.tokensTreeView.setUniformRowHeights(True)

        self.gridLayout.addWidget(self.tokensTreeView, 1, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(Gui__DlgThemeEditor)

        QMetaObject.connectSlotsByName(Gui__DlgThemeEditor)
    # setupUi

    def retranslateUi(self, Gui__DlgThemeEditor):
        Gui__DlgThemeEditor.setWindowTitle(QCoreApplication.translate("Gui::DlgThemeEditor", u"Theme Editor", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::DlgThemeEditor", u"Preview", None))
        self.checkBox.setText(QCoreApplication.translate("Gui::DlgThemeEditor", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("Gui::DlgThemeEditor", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Gui::DlgThemeEditor", u"Item 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Gui::DlgThemeEditor", u"Item 2", None))

        self.pushButton.setText(QCoreApplication.translate("Gui::DlgThemeEditor", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Gui::DlgThemeEditor", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Gui::DlgThemeEditor", u"Tab 2", None))
    # retranslateUi

