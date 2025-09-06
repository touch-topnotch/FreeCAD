# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskAssemblyCreateBom.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QToolButton,
    QWidget)

class Ui_TaskAssemblyCreateView(object):
    def setupUi(self, TaskAssemblyCreateBom):
        if not TaskAssemblyCreateBom.objectName():
            TaskAssemblyCreateBom.setObjectName(u"TaskAssemblyCreateBom")
        TaskAssemblyCreateBom.resize(376, 387)
        self.gridLayout = QGridLayout(TaskAssemblyCreateBom)
        self.gridLayout.setObjectName(u"gridLayout")
        self.CheckBox_detailSubAssemblies = Gui_PrefCheckBox(TaskAssemblyCreateBom)
        self.CheckBox_detailSubAssemblies.setObjectName(u"CheckBox_detailSubAssemblies")
        self.CheckBox_detailSubAssemblies.setChecked(True)
        self.CheckBox_detailSubAssemblies.setProperty(u"prefEntry", u"BOMDetailSubAssemblies")
        self.CheckBox_detailSubAssemblies.setProperty(u"prefPath", u"Mod/Assembly")

        self.gridLayout.addWidget(self.CheckBox_detailSubAssemblies, 0, 0, 1, 2)

        self.CheckBox_detailParts = Gui_PrefCheckBox(TaskAssemblyCreateBom)
        self.CheckBox_detailParts.setObjectName(u"CheckBox_detailParts")
        self.CheckBox_detailParts.setChecked(True)
        self.CheckBox_detailParts.setProperty(u"prefEntry", u"BOMDetailParts")
        self.CheckBox_detailParts.setProperty(u"prefPath", u"Mod/Assembly")

        self.gridLayout.addWidget(self.CheckBox_detailParts, 1, 0, 1, 2)

        self.CheckBox_onlyParts = Gui_PrefCheckBox(TaskAssemblyCreateBom)
        self.CheckBox_onlyParts.setObjectName(u"CheckBox_onlyParts")
        self.CheckBox_onlyParts.setChecked(True)
        self.CheckBox_onlyParts.setProperty(u"prefEntry", u"BOMOnlyParts")
        self.CheckBox_onlyParts.setProperty(u"prefPath", u"Mod/Assembly")

        self.gridLayout.addWidget(self.CheckBox_onlyParts, 2, 0, 1, 2)

        self.groupBox_1 = QGroupBox(TaskAssemblyCreateBom)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.gridLayout2 = QGridLayout(self.groupBox_1)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.columnList = QListWidget(self.groupBox_1)
        self.columnList.setObjectName(u"columnList")

        self.gridLayout2.addWidget(self.columnList, 0, 0, 1, 1)

        self.btnAddColumn = QPushButton(self.groupBox_1)
        self.btnAddColumn.setObjectName(u"btnAddColumn")

        self.gridLayout2.addWidget(self.btnAddColumn, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_1, 3, 0, 1, 2)

        self.btnExport = QPushButton(TaskAssemblyCreateBom)
        self.btnExport.setObjectName(u"btnExport")

        self.gridLayout.addWidget(self.btnExport, 5, 0, 1, 1)

        self.helpButton = QToolButton(TaskAssemblyCreateBom)
        self.helpButton.setObjectName(u"helpButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpButton.sizePolicy().hasHeightForWidth())
        self.helpButton.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/help-browser.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpButton.setIcon(icon)

        self.gridLayout.addWidget(self.helpButton, 5, 1, 1, 1)


        self.retranslateUi(TaskAssemblyCreateBom)

        QMetaObject.connectSlotsByName(TaskAssemblyCreateBom)
    # setupUi

    def retranslateUi(self, TaskAssemblyCreateBom):
        TaskAssemblyCreateBom.setWindowTitle(QCoreApplication.translate("TaskAssemblyCreateView", u"Bill of Materials", None))
#if QT_CONFIG(tooltip)
        self.CheckBox_detailSubAssemblies.setToolTip(QCoreApplication.translate("TaskAssemblyCreateView", u"Includes children of sub-assemblies in the bill of materials", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox_detailSubAssemblies.setText(QCoreApplication.translate("TaskAssemblyCreateView", u"Sub-assemblies children", None))
#if QT_CONFIG(tooltip)
        self.CheckBox_detailParts.setToolTip(QCoreApplication.translate("TaskAssemblyCreateView", u"Include child parts in the bill of materials", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox_detailParts.setText(QCoreApplication.translate("TaskAssemblyCreateView", u"Parts children", None))
#if QT_CONFIG(tooltip)
        self.CheckBox_onlyParts.setToolTip(QCoreApplication.translate("TaskAssemblyCreateView", u"Adds only part containers and sub-assemblies to the bill of materials. Solids (e.g. bodies, fasteners, primitives) are excluded.", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox_onlyParts.setText(QCoreApplication.translate("TaskAssemblyCreateView", u"Only parts", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("TaskAssemblyCreateView", u"Columns", None))
        self.btnAddColumn.setText(QCoreApplication.translate("TaskAssemblyCreateView", u"Add Column", None))
        self.btnExport.setText(QCoreApplication.translate("TaskAssemblyCreateView", u"Export", None))
#if QT_CONFIG(tooltip)
        self.helpButton.setToolTip(QCoreApplication.translate("TaskAssemblyCreateView", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpButton.setText("")
    # retranslateUi

