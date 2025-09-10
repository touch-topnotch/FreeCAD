# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ToolBitSelector.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDockWidget,
    QHBoxLayout, QHeaderView, QPushButton, QSizePolicy,
    QSpacerItem, QTreeView, QVBoxLayout, QWidget)
import resource_rc
import Path_rc

class Ui_ToolSelector(object):
    def setupUi(self, ToolSelector):
        if not ToolSelector.objectName():
            ToolSelector.setObjectName(u"ToolSelector")
        ToolSelector.resize(350, 542)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ToolSelector.sizePolicy().hasHeightForWidth())
        ToolSelector.setSizePolicy(sizePolicy)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cboLibraries = QComboBox(self.dockWidgetContents)
        self.cboLibraries.setObjectName(u"cboLibraries")

        self.horizontalLayout.addWidget(self.cboLibraries)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.libraryEditorOpen = QPushButton(self.dockWidgetContents)
        self.libraryEditorOpen.setObjectName(u"libraryEditorOpen")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.libraryEditorOpen.sizePolicy().hasHeightForWidth())
        self.libraryEditorOpen.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/icons/edit-edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.libraryEditorOpen.setIcon(icon)
        self.libraryEditorOpen.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.libraryEditorOpen)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tools = QTreeView(self.dockWidgetContents)
        self.tools.setObjectName(u"tools")
        self.tools.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tools.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tools.setSortingEnabled(False)

        self.horizontalLayout_2.addWidget(self.tools)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.addToolController = QPushButton(self.dockWidgetContents)
        self.addToolController.setObjectName(u"addToolController")
        self.addToolController.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/icons/edit_OK.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addToolController.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.addToolController)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        ToolSelector.setWidget(self.dockWidgetContents)

        self.retranslateUi(ToolSelector)

        QMetaObject.connectSlotsByName(ToolSelector)
    # setupUi

    def retranslateUi(self, ToolSelector):
        ToolSelector.setWindowTitle(QCoreApplication.translate("ToolSelector", u"Tool Selector", None))
#if QT_CONFIG(tooltip)
        self.libraryEditorOpen.setToolTip(QCoreApplication.translate("ToolSelector", u"Library editor...", None))
#endif // QT_CONFIG(tooltip)
        self.libraryEditorOpen.setText("")
#if QT_CONFIG(tooltip)
        self.tools.setToolTip(QCoreApplication.translate("ToolSelector", u"Available Tool Bits to choose from.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.addToolController.setToolTip(QCoreApplication.translate("ToolSelector", u"Create ToolControllers for the selected toolbits and add them to the Job", None))
#endif // QT_CONFIG(tooltip)
        self.addToolController.setText(QCoreApplication.translate("ToolSelector", u"Add To Job", None))
    # retranslateUi

