# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPreferences.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractScrollArea, QApplication, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTreeView, QVBoxLayout, QWidget)

class Ui_Gui_Dialog_DlgPreferences(object):
    def setupUi(self, Gui__Dialog__DlgPreferences):
        if not Gui__Dialog__DlgPreferences.objectName():
            Gui__Dialog__DlgPreferences.setObjectName(u"Gui__Dialog__DlgPreferences")
        Gui__Dialog__DlgPreferences.setStyleSheet(u"#sidebar { background-color: rgba(0, 0, 0, 25); }\n"
"      #groupsTreeView { background-color: transparent; }\n"
"      #groupsTreeView::item { padding: 6px 8px; }")
        Gui__Dialog__DlgPreferences.resize(900, 900)
        Gui__Dialog__DlgPreferences.setMinimumSize(QSize(600, 500))
        Gui__Dialog__DlgPreferences.setSizeGripEnabled(True)
        Gui__Dialog__DlgPreferences.setModal(True)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgPreferences)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar = QFrame(Gui__Dialog__DlgPreferences)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QSize(180, 0))
        self.sidebar.setMaximumSize(QSize(240, 16777215))
        self.sidebar.setAutoFillBackground(False)
        self.sidebar.setFrameShape(QFrame.NoFrame)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.sidebar.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.sidebar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 12, 0, 0)
        self.groupsTreeView = QTreeView(self.sidebar)
        self.groupsTreeView.setObjectName(u"groupsTreeView")
        self.groupsTreeView.setContextMenuPolicy(Qt.NoContextMenu)
        self.groupsTreeView.setAutoFillBackground(False)
        self.groupsTreeView.setFrameShape(QFrame.NoFrame)
        self.groupsTreeView.setLineWidth(0)
        self.groupsTreeView.setAutoScroll(False)
        self.groupsTreeView.setIconSize(QSize(24, 24))
        self.groupsTreeView.header().setVisible(False)

        self.verticalLayout_4.addWidget(self.groupsTreeView)

        self.actions = QVBoxLayout()
        self.actions.setSpacing(8)
        self.actions.setObjectName(u"actions")
        self.actions.setContentsMargins(16, 16, 16, 16)
        self.buttonReset = QPushButton(self.sidebar)
        self.buttonReset.setObjectName(u"buttonReset")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonReset.sizePolicy().hasHeightForWidth())
        self.buttonReset.setSizePolicy(sizePolicy1)

        self.actions.addWidget(self.buttonReset)


        self.verticalLayout_4.addLayout(self.actions)


        self.horizontalLayout.addWidget(self.sidebar)

        self.verticalFrame = QFrame(Gui__Dialog__DlgPreferences)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.content = QVBoxLayout(self.verticalFrame)
        self.content.setSpacing(12)
        self.content.setContentsMargins(11, 11, 11, 11)
        self.content.setObjectName(u"content")
        self.content.setContentsMargins(16, 16, 16, 16)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.headerLabel = QLabel(self.verticalFrame)
        self.headerLabel.setObjectName(u"headerLabel")
        font = QFont()
        font.setPointSize(18)
        self.headerLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.headerLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.content.addLayout(self.horizontalLayout_3)

        self.scrollArea = QScrollArea(self.verticalFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 626, 772))
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupWidgetStack = QStackedWidget(self.scrollAreaWidgetContents)
        self.groupWidgetStack.setObjectName(u"groupWidgetStack")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.groupWidgetStack.sizePolicy().hasHeightForWidth())
        self.groupWidgetStack.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.groupWidgetStack)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.content.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(self.verticalFrame)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy4)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.content.addWidget(self.buttonBox)


        self.horizontalLayout.addWidget(self.verticalFrame)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgPreferences)
        self.buttonBox.accepted.connect(Gui__Dialog__DlgPreferences.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__DlgPreferences.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgPreferences)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgPreferences):
        Gui__Dialog__DlgPreferences.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgPreferences", u"Preferences", None))
        self.buttonReset.setText(QCoreApplication.translate("Gui::Dialog::DlgPreferences", u"Reset", None))
        self.headerLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgPreferences", u"Header", None))
    # retranslateUi

